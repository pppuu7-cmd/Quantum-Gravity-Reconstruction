#!/usr/bin/env python3
import argparse, json, math
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
GINV=ETA.copy()

def make_q(seed, scale=0.18):
    rng=np.random.default_rng(seed)
    q=rng.normal(size=(4,4,4,4))*scale
    q=(q+q.swapaxes(0,1))/2
    q=(q+q.swapaxes(2,3))/2
    return q

def riemann_from_q(q):
    R=np.zeros((4,4,4,4))
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
         R[a,b,c,d]=0.5*(q[a,d,b,c]+q[b,c,a,d]-q[a,c,b,d]-q[b,d,a,c])
    return R

def ricci_scalar(R,g,gi):
    Ric=np.einsum('ac,abcd->bd',gi,R)
    scal=np.einsum('bd,bd->',gi,Ric)
    return Ric,scal

def weyl(R,g,gi):
    Ric,scal=ricci_scalar(R,g,gi)
    C=np.empty_like(R)
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
         C[a,b,c,d]=(R[a,b,c,d]
          -0.5*(g[a,c]*Ric[b,d]-g[a,d]*Ric[b,c]-g[b,c]*Ric[a,d]+g[b,d]*Ric[a,c])
          +(scal/6.0)*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
    return C

def i3_from_C(C,gi):
    Cup=np.einsum('ce,df,abef->abcd',gi,gi,C)
    return float(np.einsum('abcd,cdef,efab->',Cup,Cup,Cup))

def i3(R,g,gi): return i3_from_C(weyl(R,g,gi),gi)

def analytic_dir(R,dR,g,gi):
    C=weyl(R,g,gi); dC=weyl(dR,g,gi)
    Cu=np.einsum('ce,df,abef->abcd',gi,gi,C)
    dCu=np.einsum('ce,df,abef->abcd',gi,gi,dC)
    t1=np.einsum('abcd,cdef,efab->',dCu,Cu,Cu)
    t2=np.einsum('abcd,cdef,efab->',Cu,dCu,Cu)
    t3=np.einsum('abcd,cdef,efab->',Cu,Cu,dCu)
    return float(t1+t2+t3)

def controls(R,C,g,gi):
    vals=[]
    vals += [np.max(np.abs(R+R.swapaxes(0,1))),np.max(np.abs(R+R.swapaxes(2,3))),np.max(np.abs(R-R.transpose(2,3,0,1)))]
    cyc=R+R.transpose(0,2,3,1)+R.transpose(0,3,1,2)
    vals.append(np.max(np.abs(cyc)))
    tr=np.einsum('ac,abcd->bd',gi,C)
    return float(max(vals)),float(np.max(np.abs(tr)))

def boost_x(v):
    ga=1/math.sqrt(1-v*v)
    A=np.eye(4); A[0,0]=ga; A[1,1]=ga; A[0,1]=-ga*v; A[1,0]=-ga*v
    return A

def rot_yz(th):
    A=np.eye(4); c=math.cos(th); s=math.sin(th)
    A[2,2]=c; A[2,3]=-s; A[3,2]=s; A[3,3]=c
    return A

def transform4(T,A): return np.einsum('ia,jb,kc,ld,ijkl->abcd',A,A,A,A,T)

def conformally_flat_from_ricci(seed):
    rng=np.random.default_rng(seed)
    X=rng.normal(size=(4,4)); Ric=(X+X.T)/2
    scal=float(np.einsum('ab,ab->',GINV,Ric))
    R=np.zeros((4,4,4,4))
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
         R[a,b,c,d]=0.5*(ETA[a,c]*Ric[b,d]-ETA[a,d]*Ric[b,c]-ETA[b,c]*Ric[a,d]+ETA[b,d]*Ric[a,c])-(scal/6)*(ETA[a,c]*ETA[b,d]-ETA[a,d]*ETA[b,c])
    return R

def rel(a,b,floor=1e-14): return abs(a-b)/max(abs(a),abs(b),floor)

def run(lane):
    seed=1009+lane*97
    R=riemann_from_q(make_q(seed)); dR=riemann_from_q(make_q(seed+41,0.11))
    C=weyl(R,ETA,GINV)
    alg_res,tr_res=controls(R,C,ETA,GINV)
    base=i3_from_C(C,GINV); ana=analytic_dir(R,dR,ETA,GINV)
    hs=[1e-3,5e-4,2.5e-4,1.25e-4]; errs=[]; fds=[]
    for h in hs:
        fd=(i3(R+h*dR,ETA,GINV)-i3(R-h*dR,ETA,GINV))/(2*h)
        fds.append(fd); errs.append(abs(fd-ana))
    finest_rel=rel(fds[-1],ana,1e-12)
    conv=((errs[-1] <= 1.05*errs[-2]) and ((errs[-1] < 1e-10) or (errs[-2]/max(errs[-1],1e-30) >= 2.5)))
    cov=[]
    for A in (boost_x(0.27), boost_x(-0.19)@rot_yz(0.37)):
        Rt=transform4(R,A); dRt=transform4(dR,A); gt=A.T@ETA@A; git=np.linalg.inv(gt)
        cov.append((rel(i3(Rt,gt,git),base,1e-12),rel(analytic_dir(Rt,dRt,gt,git),ana,1e-12)))
    cf=conformally_flat_from_ricci(seed+777); cfC=weyl(cf,ETA,GINV); cf_i3=i3_from_C(cfC,GINV); cf_d=analytic_dir(cf,dR,ETA,GINV)
    valid=alg_res<=1e-11 and tr_res<=1e-10 and abs(cf_i3)<=1e-11 and abs(cf_d)<=1e-10
    derivative_ok=(finest_rel<=2e-6 or abs(fds[-1]-ana)<=1e-9) and conv
    covariance_ok=max(x[0] for x in cov)<=1e-9 and max(x[1] for x in cov)<=1e-8
    nonzero=abs(base)>1e-7 and abs(ana)>1e-7
    passed=valid and derivative_ok and covariance_ok
    out={"lane":lane,"seed":seed,"I3":base,"analytic_directional":ana,"fd":fds,"errors":errs,"finest_rel":finest_rel,"convergence_ok":conv,"algebraic_residual":alg_res,"weyl_trace_residual":tr_res,"covariance":cov,"cf_I3":cf_i3,"cf_directional":cf_d,"valid":valid,"derivative_ok":derivative_ok,"covariance_ok":covariance_ok,"nonzero_calibration":nonzero,"pass":passed}
    print(json.dumps(out,sort_keys=True))
    if not passed: raise SystemExit(2)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); a=ap.parse_args(); run(a.lane)
