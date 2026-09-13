#!/usr/bin/env python3
import argparse, json, math, os
import numpy as np

import qgr_iter051c_full_eom as c
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051b1_weyl3_p_insertion as w3

N=4
COORD_H=(1.0e-3,5.0e-4)
EPS=(2.0e-4,1.0e-4,5.0e-5)
A_METRIC_SEEDS=[162011,162223,162437,162653,162869,163087]
A_PERT_SEEDS=[172019,172237,172459,172681,172903,173129]
A_POINTS=[
    [0.12,-0.08,0.06,-0.04],[-0.09,0.11,-0.05,0.07],[0.08,0.04,-0.12,0.09],
    [-0.06,-0.10,0.07,0.13],[0.10,-0.03,-0.09,-0.08],[-0.11,0.06,0.10,-0.05]
]
B_METRIC_SEEDS=[182033,182261,182489]
B_PERT_SEEDS=[192047,192277,192509]
B_POINTS=[[0.09,-0.07,0.05,0.08],[-0.08,0.06,-0.10,0.04],[0.07,0.10,0.04,-0.09]]
C_METRIC_SEEDS=[202061,202291,202523]
C_PERT_SEEDS=[212063,212297,212531]
C_POINTS=[[0.08,-0.06,0.09,-0.05],[-0.10,0.07,0.03,0.11],[0.06,0.09,-0.08,-0.07]]


def sym2(x): return 0.5*(x+x.T)

def relscalar(a,b,floor=1e-12):
    return float(abs(a-b)/max(abs(a),abs(b),floor))

def relnorm(a,b,floor=1e-12):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),floor))


class Perturbation:
    def __init__(self,seed):
        rng=np.random.default_rng(seed)
        self.S=sym2(rng.normal(size=(N,N)))*0.11
        self.A=np.array([sym2(rng.normal(size=(N,N))) for _ in range(N)])*0.08
        Q=np.empty((N,N,N,N))
        for a in range(N):
            for b in range(N): Q[a,b]=sym2(rng.normal(size=(N,N)))
        self.Q=0.5*(Q+Q.swapaxes(0,1))*0.055
    def jets(self,x):
        x=np.asarray(x,float)
        h=self.S.copy()+np.einsum('aij,a->ij',self.A,x)
        h+=0.5*np.einsum('abij,a,b->ij',self.Q,x,x)
        dh=np.empty((N,N,N)); ddh=np.empty((N,N,N,N))
        for a in range(N):
            dh[a]=self.A[a]+np.einsum('bij,b->ij',self.Q[a],x)
            for b in range(N): ddh[a,b]=self.Q[a,b]
        return h,dh,ddh


class PerturbedMetric:
    def __init__(self,base,pert,eps): self.base=base; self.pert=pert; self.eps=float(eps)
    def jets(self,x):
        g,dg,ddg=self.base.jets(x); h,dh,ddh=self.pert.jets(x)
        return g+self.eps*h,dg+self.eps*dh,ddg+self.eps*ddh


class ConformalMetric:
    def __init__(self,seed):
        rng=np.random.default_rng(seed)
        self.a=rng.normal(size=N)*0.035
        B=rng.normal(size=(N,N))*0.025
        self.B=0.5*(B+B.T)
    def jets(self,x):
        x=np.asarray(x,float)
        om=1.0+float(self.a@x)+0.5*float(x@self.B@x)
        dom=self.a+self.B@x
        f=om*om
        g=f*c.ETA
        dg=np.empty((N,N,N)); ddg=np.empty((N,N,N,N))
        for a in range(N):
            dg[a]=(2.0*om*dom[a])*c.ETA
            for b in range(N):
                ddg[a,b]=(2.0*dom[a]*dom[b]+2.0*om*self.B[a,b])*c.ETA
        return g,dg,ddg


class TransformPerturbation:
    def __init__(self,base,L): self.base=base; self.L=np.asarray(L,float)
    def jets(self,y):
        y=np.asarray(y,float); L=self.L; x=L@y
        h,dh,ddh=self.base.jets(x)
        ht=L.T@h@L
        dht=np.empty_like(dh); ddht=np.empty_like(ddh)
        for k in range(N):
            dht[k]=L.T@sum(L[a,k]*dh[a] for a in range(N))@L
            for l in range(N):
                ddht[k,l]=L.T@sum(L[a,k]*L[b,l]*ddh[a,b] for a in range(N) for b in range(N))@L
        return ht,dht,ddht


def shear(i):
    L=np.eye(N)
    if i==0:
        L[0,1]=0.17; L[1,2]=-0.11; L[2,3]=0.09
    elif i==1:
        L[0,2]=-0.13; L[1,3]=0.16; L[2,0]=0.07
    else:
        L[0,3]=0.12; L[1,0]=-0.08; L[2,1]=0.10; L[3,2]=-0.06
    # Control-only determinant normalization.  det(L) is affine in a single
    # matrix entry; solve that affine equation exactly instead of dividing the
    # entry by the pre-correction determinant (which is invalid for cyclic C2).
    L[3,3]=0.0
    d0=float(np.linalg.det(L))
    L[3,3]=1.0
    d1=float(np.linalg.det(L))
    slope=d1-d0
    if abs(slope)<1e-14:
        raise RuntimeError('degenerate determinant normalization slope')
    L[3,3]=(1.0-d0)/slope
    return L


def density(metric,x):
    g,dg,ddg,gi,G,R=c.geometry(metric,np.asarray(x,float))
    return float(np.real(c.density_complex(R,g)))


def direct_directional(metric,pert,x,eps):
    def f(e): return density(PerturbedMetric(metric,pert,e),x)
    e=float(eps)
    return float((-f(2*e)+8*f(e)-8*f(-e)+f(-2*e))/(12*e))


def derivative5(func,x,axis,h):
    x=np.asarray(x,float); e=np.zeros(N); e[axis]=h
    return (-func(x+2*e)+8.0*func(x+e)-8.0*func(x-e)+func(x-2*e))/(12.0*h)


def p_and_covdiv_sym(metric,x,hstep):
    x=np.asarray(x,float)
    g,dg,ddg,gi,G,R=c.geometry(metric,x)
    P=c.P_actual(metric,x)
    Q=0.5*(P+P.swapaxes(1,2))  # P^{a(bc)d}
    dP=np.empty((N,N,N,N,N))
    for nu in range(N):
        dP[nu]=derivative5(lambda z:c.P_actual(metric,z),x,nu,hstep)
    dQ=0.5*(dP+dP.swapaxes(2,3))
    div=np.zeros((N,N,N))
    for a in range(N):
      for b in range(N):
       for cc in range(N):
        v=0.0
        for nu in range(N):
            term=dQ[nu,a,b,cc,nu]
            for r in range(N):
                term += G[a,nu,r]*Q[r,b,cc,nu]
                term += G[b,nu,r]*Q[a,r,cc,nu]
                term += G[cc,nu,r]*Q[a,b,r,nu]
                term += G[nu,nu,r]*Q[a,b,cc,r]
            v += term
        div[a,b,cc]=v
    return g,G,P,Q,div,R


def theta_density(metric,pert,x,hstep):
    x=np.asarray(x,float)
    g,G,P,Q,divP,R=p_and_covdiv_sym(metric,x,hstep)
    h,dh,ddh=pert.jets(x)
    nabh=np.empty_like(dh)
    for nu in range(N):
      for b in range(N):
       for cc in range(N):
        v=dh[nu,b,cc]
        for r in range(N):
            v -= G[r,nu,b]*h[r,cc] + G[r,nu,cc]*h[b,r]
        nabh[nu,b,cc]=v
    sg=math.sqrt(-float(np.linalg.det(g)))
    th=np.zeros(N)
    for a in range(N):
        first=0.0; second=0.0
        for b in range(N):
          for cc in range(N):
            second += h[b,cc]*divP[a,b,cc]
            for nu in range(N): first += Q[a,b,cc,nu]*nabh[nu,b,cc]
        th[a]=2.0*sg*(first-second)
    return th,{'g':g,'P':P,'R':R}


def div_theta(metric,pert,x,hstep):
    x=np.asarray(x,float); total=0.0
    for mu in range(N):
        total += derivative5(lambda z:theta_density(metric,pert,z,hstep)[0][mu],x,mu,hstep)
    return float(total)


def signature_ok(g):
    ev=np.linalg.eigvalsh(sym2(g)); return bool(np.sum(ev<0)==1 and np.sum(ev>0)==3)


def controls(metric,pert,x):
    sig,inv,det=d2n.extended_controls(metric,np.asarray(x,float))
    invs=[inv]; sigs=[sig]
    for e in (-2*EPS[0],-EPS[0],EPS[0],2*EPS[0]):
        g=PerturbedMetric(metric,pert,e).jets(x)[0]
        gi=np.linalg.inv(g); sigs.append(signature_ok(g)); invs.append(float(np.max(np.abs(g@gi-np.eye(N)))))
    return bool(all(sigs)),float(max(invs)),float(det)


def identity_data(metric,pert,x):
    x=np.asarray(x,float)
    sig,inv,det=controls(metric,pert,x)
    directs=[direct_directional(metric,pert,x,e) for e in EPS]
    dstep=relscalar(directs[-1],directs[-2])
    rows=[]
    hfield=pert.jets(x)[0]
    for hs in COORD_H:
        H,z=d2n.assemble_minus5(metric,x,hs)
        divth=div_theta(metric,pert,x,hs)
        bulk=float(np.einsum('ab,ab->',H,hfield))
        rhs=bulk+divth
        res=relscalar(directs[-1],rhs)
        rows.append((hs,H,bulk,divth,rhs,res,z))
    fine=rows[-1]; coarse=rows[-2]
    H=fine[1]; z=fine[6]
    return {
      'signature_valid':sig,'max_inverse_residual':inv,'max_metric_det':det,
      'direct_values':directs,'direct_final_step_change':dstep,
      'bulk_H_dot_h':fine[2],'theta_divergence':fine[3],'rhs':fine[4],
      'identity_relative_residual':fine[5],
      'coarse_identity_relative_residual':coarse[5],
      'identity_residual_step_change_abs':float(abs(fine[5]-coarse[5])),
      'H_norm':float(np.linalg.norm(H)),'H_symmetry_residual':float(np.max(np.abs(H-H.T))),
      'P_norm':float(np.linalg.norm(z['P'])),'R_norm':float(np.linalg.norm(z['R'])),
      'W3':float(np.real(w3.i3_complex(z['R'],z['g'],np.linalg.inv(z['g'])))),
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }


def pass_A(d):
    valid=bool(d['signature_valid'] and d['max_inverse_residual']<=3e-11 and np.isfinite(list_numeric(d)).all())
    passed=bool(valid and abs(d['direct_values'][-1])>=1e-8 and d['direct_final_step_change']<=5e-5 and
                d['identity_relative_residual']<=3e-4 and d['identity_residual_step_change_abs']<=3e-4 and
                d['H_symmetry_residual']<=5e-7)
    return valid,passed


def list_numeric(d):
    vals=[]
    for v in d.values():
        if isinstance(v,(int,float,np.floating)): vals.append(float(v))
        elif isinstance(v,list):
            for q in v:
                if isinstance(q,(int,float,np.floating)): vals.append(float(q))
    return np.asarray(vals,float)


def lane_a(i):
    metric=c.PolyMetric(A_METRIC_SEEDS[i]); pert=Perturbation(A_PERT_SEEDS[i]); x=np.array(A_POINTS[i],float)
    d=identity_data(metric,pert,x); valid,passed=pass_A(d)
    d.update({'gate':'ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION','stream':'A','index':i,
              'metric_seed':A_METRIC_SEEDS[i],'perturbation_seed':A_PERT_SEEDS[i],'point':x.tolist(),
              'control_valid':valid,'lane_pass':passed})
    return d


def lane_b(i):
    metric=ConformalMetric(B_METRIC_SEEDS[i]); pert=Perturbation(B_PERT_SEEDS[i]); x=np.array(B_POINTS[i],float)
    d=identity_data(metric,pert,x)
    mismatch=float(abs(d['direct_values'][-1]-d['rhs']))
    valid=bool(d['signature_valid'] and d['max_inverse_residual']<=3e-11 and d['R_norm']>=1e-6 and np.isfinite(list_numeric(d)).all())
    passed=bool(valid and abs(d['W3'])<=2e-10 and d['P_norm']<=3e-9 and abs(d['direct_values'][-1])<=2e-8 and
                d['H_norm']<=3e-7 and mismatch<=3e-8)
    d.update({'gate':'ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION','stream':'B','index':i,
              'metric_seed':B_METRIC_SEEDS[i],'perturbation_seed':B_PERT_SEEDS[i],'point':x.tolist(),
              'absolute_identity_mismatch':mismatch,'control_valid':valid,'lane_pass':passed})
    return d


def lane_c(i):
    metric=c.PolyMetric(C_METRIC_SEEDS[i]); pert=Perturbation(C_PERT_SEEDS[i]); x=np.array(C_POINTS[i],float)
    L=shear(i); M=np.linalg.inv(L); y=M@x
    mt=c.TransformMetric(metric,L); pt=TransformPerturbation(pert,L)
    d0=identity_data(metric,pert,x); d1=identity_data(mt,pt,y)
    v0,p0=pass_A(d0); v1,p1=pass_A(d1)
    g0=metric.jets(x)[0]; h0=pert.jets(x)[0]
    gt=mt.jets(y)[0]; ht=pt.jets(y)[0]
    metric_res=float(np.max(np.abs(gt-L.T@g0@L)))
    pert_res=float(np.max(np.abs(ht-L.T@h0@L)))
    dcov=relscalar(d1['direct_values'][-1],d0['direct_values'][-1])
    rcov=relscalar(d1['rhs'],d0['rhs'])
    valid=bool(v0 and v1 and abs(np.linalg.det(L)-1.0)<=2e-12 and metric_res<=3e-11 and pert_res<=3e-11)
    passed=bool(valid and p0 and p1 and dcov<=5e-4 and rcov<=5e-4)
    return {
      'gate':'ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION','stream':'C','index':i,
      'metric_seed':C_METRIC_SEEDS[i],'perturbation_seed':C_PERT_SEEDS[i],
      'point_x':x.tolist(),'point_y':y.tolist(),'det_L':float(np.linalg.det(L)),
      'metric_transform_residual':metric_res,'perturbation_transform_residual':pert_res,
      'direct_covariance_relative_residual':dcov,'rhs_covariance_relative_residual':rcov,
      'base':d0,'transformed':d1,'control_valid':valid,'lane_pass':passed,
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices='ABC',required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    limits={'A':6,'B':3,'C':3}
    if not 0<=a.index<limits[a.stream]: raise SystemExit('index outside frozen panel')
    out={'A':lane_a,'B':lane_b,'C':lane_c}[a.stream](a.index)
    out['classification']='LANE_PASS' if out['lane_pass'] else 'LANE_FAIL'
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
