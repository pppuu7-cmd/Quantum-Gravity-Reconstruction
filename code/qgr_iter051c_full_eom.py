#!/usr/bin/env python3
import argparse, itertools, json, math, os
import numpy as np

import qgr_iter051b0_double_divergence_operator as b0
import qgr_iter051b1_weyl3_p_insertion as w3

N=4
ETA=np.diag([-1.0,1.0,1.0,1.0])
HCS=1e-30
HS=(1.0e-3,5.0e-4,2.5e-4)
PQ=[(-0.5,1.0/3.0),(0.25,0.75),(-2.0/3.0,0.5),(0.4,-0.2),(1.5,0.25),(-0.25,5.0/6.0)]
BT=[0.5,2.0/3.0,1.0,1.5,2.0,3.0]


def relnorm(A,B,floor=1e-14):
    return float(np.linalg.norm(A-B)/max(np.linalg.norm(A),np.linalg.norm(B),floor))

def relscalar(a,b,floor=1e-14):
    return float(abs(a-b)/max(abs(a),abs(b),floor))

def sym2(X): return 0.5*(X+X.T)

def sym_coord(T,k):
    out=np.zeros_like(T)
    perms=list(itertools.permutations(range(k)))
    for p in perms:
        out += np.transpose(T,p+tuple(range(k,T.ndim)))
    return out/len(perms)


class PolyMetric:
    def __init__(self,seed):
        rng=np.random.default_rng(seed)
        self.A=np.array([sym2(rng.normal(size=(N,N))) for _ in range(N)])*0.015
        H=np.empty((N,N,N,N))
        for c in range(N):
            for d in range(N): H[c,d]=sym2(rng.normal(size=(N,N)))
        self.H=sym_coord(H,2)*0.035
        J=np.empty((N,N,N,N,N))
        for c,d,e in itertools.product(range(N),repeat=3): J[c,d,e]=sym2(rng.normal(size=(N,N)))
        self.J=sym_coord(J,3)*0.050
        K=np.empty((N,N,N,N,N,N))
        for c,d,e,f in itertools.product(range(N),repeat=4): K[c,d,e,f]=sym2(rng.normal(size=(N,N)))
        self.K=sym_coord(K,4)*0.070
    def jets(self,x):
        x=np.asarray(x,float)
        g=ETA.copy()
        g += np.einsum('cij,c->ij',self.A,x)
        g += 0.5*np.einsum('cdij,c,d->ij',self.H,x,x)
        g += (1.0/6.0)*np.einsum('cdeij,c,d,e->ij',self.J,x,x,x)
        g += (1.0/24.0)*np.einsum('cdefij,c,d,e,f->ij',self.K,x,x,x,x)
        dg=np.empty((N,N,N))
        ddg=np.empty((N,N,N,N))
        for c in range(N):
            dg[c]=self.A[c]+np.einsum('dij,d->ij',self.H[c],x)
            dg[c]+=0.5*np.einsum('deij,d,e->ij',self.J[c],x,x)
            dg[c]+=(1.0/6.0)*np.einsum('defij,d,e,f->ij',self.K[c],x,x,x)
            for d in range(N):
                ddg[c,d]=self.H[c,d]+np.einsum('eij,e->ij',self.J[c,d],x)
                ddg[c,d]+=0.5*np.einsum('efij,e,f->ij',self.K[c,d],x,x)
        return g,dg,ddg


class BianchiMetric:
    def __init__(self,p,q): self.p=float(p); self.q=float(q)
    def jets(self,x):
        t=float(np.asarray(x)[0]); p,q=self.p,self.q
        if t<=0: raise ValueError('positive t required')
        a=t**p; bb=t**q
        g=np.diag([-1.0,a*a,bb*bb,bb*bb])
        dg=np.zeros((N,N,N)); ddg=np.zeros((N,N,N,N))
        dg[0,1,1]=2*p*t**(2*p-1)
        dg[0,2,2]=dg[0,3,3]=2*q*t**(2*q-1)
        ddg[0,0,1,1]=2*p*(2*p-1)*t**(2*p-2)
        ddg[0,0,2,2]=ddg[0,0,3,3]=2*q*(2*q-1)*t**(2*q-2)
        return g,dg,ddg


class FLRWMetric:
    def __init__(self,kind): self.kind=kind
    def vals(self,t):
        if self.kind==0: return 1+t,1.0,0.0
        if self.kind==1: return 1+t*t,2*t,2.0
        if self.kind==2: return 1+0.2*t+t*t/3.0,0.2+2*t/3.0,2.0/3.0
        return 2+t+t**3/5.0,1+3*t*t/5.0,6*t/5.0
    def jets(self,x):
        t=float(np.asarray(x)[0]); a,ap,app=self.vals(t)
        g=np.diag([-1.0,a*a,a*a,a*a])
        dg=np.zeros((N,N,N)); ddg=np.zeros((N,N,N,N))
        for i in (1,2,3):
            dg[0,i,i]=2*a*ap
            ddg[0,0,i,i]=2*(ap*ap+a*app)
        return g,dg,ddg


class TransformMetric:
    def __init__(self,base,L): self.base=base; self.L=np.asarray(L,float)
    def jets(self,y):
        y=np.asarray(y,float); L=self.L; x=L@y
        g,dg,ddg=self.base.jets(x)
        gt=L.T@g@L
        dgt=np.empty_like(dg); ddgt=np.empty_like(ddg)
        for k in range(N):
            dgt[k]=L.T@sum(L[c,k]*dg[c] for c in range(N))@L
            for l in range(N):
                ddgt[k,l]=L.T@sum(L[c,k]*L[d,l]*ddg[c,d] for c in range(N) for d in range(N))@L
        return gt,dgt,ddgt


def geometry(metric,x):
    g,dg,ddg=metric.jets(x)
    gi,G,dG=b0.conn(g,dg,ddg)
    Rup=np.zeros((N,N,N,N))
    for a,b,c,d in itertools.product(range(N),repeat=4):
        val=dG[c,a,b,d]-dG[d,a,b,c]
        for e in range(N): val += G[a,c,e]*G[e,b,d]-G[a,d,e]*G[e,b,c]
        Rup[a,b,c,d]=val
    R=np.einsum('ae,ebcd->abcd',g,Rup)
    return g,dg,ddg,gi,G,R


def metric_signature_ok(g):
    ev=np.linalg.eigvalsh(sym2(g)); return np.sum(ev<0)==1 and np.sum(ev>0)==3


def riemann_alg(R): return w3.algebraic_residual(R)


def P_actual(metric,x):
    g,dg,ddg,gi,G,R=geometry(metric,x)
    return w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))


def first_div(metric,x,h):
    g,dg,ddg,gi,G,R=geometry(metric,x)
    P0=w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))
    dP=np.empty((N,N,N,N,N))
    for c in range(N):
        e=np.zeros(N); e[c]=h
        dP[c]=(P_actual(metric,x+e)-P_actual(metric,x-e))/(2*h)
    S=b0.first_cov(P0,dP,G)
    return np.einsum('aambn->mbn',S)


def direct_D(metric,x,h):
    g,dg,ddg,gi,G,R=geometry(metric,x)
    R0=first_div(metric,x,h)
    D=np.zeros((N,N))
    for bb in range(N):
        e=np.zeros(N); e[bb]=h
        dR=(first_div(metric,x+e,h)-first_div(metric,x-e,h))/(2*h)
        D += dR[:,bb,:]
        for m,n,rr in itertools.product(range(N),repeat=3):
            D[m,n]+=G[m,bb,rr]*R0[rr,bb,n]+G[bb,bb,rr]*R0[m,rr,n]+G[n,bb,rr]*R0[m,bb,rr]
    return D


def density_complex(R,g):
    gi=np.linalg.inv(g)
    return np.sqrt(-np.linalg.det(g))*w3.i3_complex(R,g,gi)


def algebraic_A(R,g):
    A=np.zeros((N,N)); Rc=R.astype(complex)
    for i in range(N):
        B=np.zeros((N,N)); B[i,i]=1.0
        gc=g.astype(complex)+1j*HCS*B
        A[i,i]=float(np.imag(density_complex(Rc,gc))/HCS)
    for i in range(N):
        for j in range(i+1,N):
            B=np.zeros((N,N)); B[i,j]=B[j,i]=1.0
            gc=g.astype(complex)+1j*HCS*B
            v=float(np.imag(density_complex(Rc,gc))/HCS)/2.0
            A[i,j]=A[j,i]=v
    return A


def lowering_insertion(R,g,P):
    gi=np.linalg.inv(g); sg=math.sqrt(-float(np.linalg.det(g)))
    Rup=np.einsum('ef,fbcd->ebcd',gi,R)
    Q=sg*np.einsum('abcd,ebcd->ae',P,Rup)
    return sym2(Q)


def assemble(metric,x,h):
    g,dg,ddg,gi,G,R=geometry(metric,x)
    P=w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))
    A=algebraic_A(R,g)
    I=lowering_insertion(R,g,P)
    D=direct_D(metric,np.asarray(x,float),h)
    sg=math.sqrt(-float(np.linalg.det(g)))
    H=A+I+2.0*sg*D
    I3=float(np.real(w3.i3_complex(R,g,gi)))
    return {'H':H,'A':A,'I':I,'D':D,'g':g,'gi':gi,'R':R,'P':P,'I3':I3}


def stencil_controls(metric,x):
    dets=[]; invs=[]; sig=[]
    for h in HS:
        pts=[np.asarray(x,float)]
        for c in range(N):
            e=np.zeros(N); e[c]=2*h; pts += [np.asarray(x,float)+e,np.asarray(x,float)-e]
        for z in pts:
            g=metric.jets(z)[0]; gi=np.linalg.inv(g)
            dets.append(float(np.linalg.det(g))); invs.append(float(np.max(np.abs(g@gi-np.eye(N)))))
            sig.append(metric_signature_ok(g))
    return bool(all(sig) and max(dets)<0),float(max(invs)),float(max(dets))


def exact_targets(t,p,q):
    W=(4.0/9.0)*t**-6*(p-1)**3*(p-q)**3
    EN=-(8.0/9.0)*t**(p+2*q-6)*(p-1)**2*(p-q)**3*(p-3*q+5)
    EA=-(8.0/9.0)*t**(2*q-6)*(p-1)**2*(p-q)**2*(p*p-p*q-p-9*q*q+34*q-30)
    EB=(8.0/9.0)*t**(p+q-6)*(p-1)**2*(p-q)**2*(p*p-4*p*q+5*p-6*q*q+28*q-30)
    return W,EN,EA,EB


def stream_a(idx):
    metric=PolyMetric(81001+193*idx); x=np.zeros(N)
    sig,inv,det=stencil_controls(metric,x)
    vals=[assemble(metric,x,h) for h in HS]
    z=vals[-1]; H=z['H']; prev=vals[-2]['H']
    out={
      'gate':'ITER051C-FULL-WEYL3-EOM-ASSEMBLY','stream':'A','index':idx,
      'signature_valid':sig,'max_inverse_residual':inv,'max_metric_det':det,
      'riemann_algebraic_residual':riemann_alg(z['R']),'P_algebraic_residual':w3.algebraic_residual(z['P']),
      'H_norm':float(np.linalg.norm(H)),'H_symmetry_residual':float(np.max(np.abs(H-H.T))),
      'H_final_step_change':relnorm(H,prev),'I3':z['I3'],
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=(sig and inv<=2e-11 and out['riemann_algebraic_residual']<=2e-9 and out['P_algebraic_residual']<=2e-9)
    passed=(valid and out['H_symmetry_residual']<=3e-7 and out['H_norm']>1e-7 and out['H_final_step_change']<=2e-3)
    out['control_valid']=bool(valid); out['lane_pass']=bool(passed); return out


def stream_b(idx):
    p,q=PQ[idx]; t=BT[idx]; metric=BianchiMetric(p,q); x=np.array([t,0,0,0],float)
    sig,inv,det=stencil_controls(metric,x)
    preds=[]
    for h in HS:
        z=assemble(metric,x,h); H=z['H']; a=t**p; bb=t**q
        preds.append(np.array([-2.0*H[0,0],2.0*a*H[1,1],2.0*bb*(H[2,2]+H[3,3])]))
    W,EN,EA,EB=exact_targets(t,p,q); target=np.array([EN,EA,EB])
    residuals=[relscalar(preds[-1][k],target[k],1e-12) for k in range(3)]
    step=relnorm(preds[-1],preds[-2],1e-12)
    out={'gate':'ITER051C-FULL-WEYL3-EOM-ASSEMBLY','stream':'B','index':idx,'p':p,'q':q,'time':t,
         'predicted_EN_EA_EB':preds[-1].tolist(),'exact_EN_EA_EB':target.tolist(),
         'relative_residuals':residuals,'final_step_change':step,'W3_exact':W,
         'signature_valid':sig,'max_inverse_residual':inv,'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=sig and inv<=2e-11 and np.min(np.abs(target))>1e-10
    passed=valid and max(residuals)<=3e-4 and step<=2e-4
    out['control_valid']=bool(valid); out['lane_pass']=bool(passed); return out


def stream_c(idx):
    metric=FLRWMetric(idx); times=[0.4,0.6,0.5,0.7]; x=np.array([times[idx],0,0,0],float)
    sig,inv,det=stencil_controls(metric,x); z=assemble(metric,x,HS[-1])
    rnorm=float(np.linalg.norm(z['R'])); pnorm=float(np.linalg.norm(z['P'])); hnorm=float(np.linalg.norm(z['H']))
    out={'gate':'ITER051C-FULL-WEYL3-EOM-ASSEMBLY','stream':'C','index':idx,'time':times[idx],
         'riemann_norm':rnorm,'I3_abs':abs(z['I3']),'P_norm':pnorm,'H_norm':hnorm,
         'signature_valid':sig,'max_inverse_residual':inv,'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=sig and inv<=2e-11 and rnorm>1e-6
    passed=valid and out['I3_abs']<=2e-10 and pnorm<=3e-9 and hnorm<=2e-7
    out['control_valid']=bool(valid); out['lane_pass']=bool(passed); return out


def lorentz(idx):
    if idx==0: return b0.boost(0.17)
    if idx==1: return b0.boost(-0.21)@b0.rot(0.31)
    if idx==2: return b0.boost(0.11)@b0.rot(-0.43)
    return b0.boost(-0.15)@b0.rot(0.22)


def stream_d(idx):
    base=PolyMetric(91001+211*idx); L=lorentz(idx); trans=TransformMetric(base,L); x=np.zeros(N)
    z=assemble(base,x,HS[-1]); zt=assemble(trans,x,HS[-1]); M=np.linalg.inv(L)
    expected=M@z['H']@M.T
    cov=relnorm(zt['H'],expected)
    gb=base.jets(x)[0]; gt=trans.jets(x)[0]
    metric_control=float(np.max(np.abs(gt-L.T@gb@L)))
    inv_control=float(np.max(np.abs(np.linalg.inv(L)@L-np.eye(N))))
    out={'gate':'ITER051C-FULL-WEYL3-EOM-ASSEMBLY','stream':'D','index':idx,
         'H_norm':float(np.linalg.norm(z['H'])),'Ht_norm':float(np.linalg.norm(zt['H'])),
         'covariance_relative_residual':cov,'metric_transform_residual':metric_control,
         'inverse_transform_residual':inv_control,'det_L':float(np.linalg.det(L)),
         'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'}
    valid=(abs(np.linalg.det(L)-1.0)<=2e-12 and metric_control<=2e-11 and inv_control<=2e-11 and out['H_norm']>1e-7)
    passed=valid and cov<=8e-4
    out['control_valid']=bool(valid); out['lane_pass']=bool(passed); return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCD'),required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True)
    args=ap.parse_args(); limits={'A':4,'B':6,'C':4,'D':4}
    if not 0<=args.index<limits[args.stream]: raise SystemExit('index outside frozen stream')
    out={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[args.stream](args.index)
    out['classification']=f"ITER051C_{args.stream}_LANE_PASS" if out['lane_pass'] else f"ITER051C_{args.stream}_LANE_FAIL"
    os.makedirs(os.path.dirname(args.out),exist_ok=True)
    with open(args.out,'w',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
