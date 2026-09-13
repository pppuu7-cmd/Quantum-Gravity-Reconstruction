#!/usr/bin/env python3
import argparse, json, math, os
from functools import lru_cache
import numpy as np
import sympy as sp

import qgr_iter051c_full_eom as c
import qgr_iter051b1_weyl3_p_insertion as w3
import qgr_iter049_weyl3_spherical_variational as s49

N=4
HS=(1.0e-3,5.0e-4,2.5e-4)

A_PQ=[
    (-3/4,1/5),(1/3,-2/5),(2/3,1/6),(4/3,-1/4),
    (5/4,2/5),(-1/3,3/5),(3/4,-1/2),(7/5,1/3),
]
A_T=[4/5,5/4,7/6,9/8,6/5,7/5,5/3,11/10]
C_SEEDS=[121003,121211,121417,121621]


def relnorm(a,b,floor=1e-14):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),floor))

def relscalar(a,b,floor=1e-14):
    return float(abs(a-b)/max(abs(a),abs(b),floor))

def metric_signature_ok(g):
    ev=np.linalg.eigvalsh(0.5*(g+g.T))
    return bool(np.sum(ev<0)==1 and np.sum(ev>0)==3)


def assemble_both(metric,x,h):
    g,dg,ddg,gi,G,R=c.geometry(metric,x)
    P=w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))
    A=c.algebraic_A(R,g)
    I=c.lowering_insertion(R,g,P)
    D=c.direct_D(metric,np.asarray(x,float),h)
    sg=math.sqrt(-float(np.linalg.det(g)))
    Hminus=A+I-2.0*sg*D
    Hplus=A+I+2.0*sg*D
    I3=float(np.real(w3.i3_complex(R,g,gi)))
    return {'minus':Hminus,'plus':Hplus,'A':A,'I':I,'D':D,'g':g,'gi':gi,'R':R,'P':P,'I3':I3}


def stencil_controls(metric,x):
    sig=[]; inv=[]; dets=[]
    x=np.asarray(x,float)
    for h in HS:
        pts=[x]
        for k in range(N):
            e=np.zeros(N); e[k]=2*h
            pts += [x+e,x-e]
        for z in pts:
            g=metric.jets(z)[0]; gi=np.linalg.inv(g)
            sig.append(metric_signature_ok(g))
            inv.append(float(np.max(np.abs(g@gi-np.eye(N)))))
            dets.append(float(np.linalg.det(g)))
    return bool(all(sig) and max(dets)<0),float(max(inv)),float(max(dets))


def reduced_bianchi(H,t,p,q):
    a=t**p; b=t**q
    return np.array([-2.0*H[0,0],2.0*a*H[1,1],2.0*b*(H[2,2]+H[3,3])],float)


def stream_a(i):
    p,q=A_PQ[i]; t=A_T[i]
    metric=c.BianchiMetric(p,q); x=np.array([t,0,0,0],float)
    sig,inv,det=stencil_controls(metric,x)
    vals=[assemble_both(metric,x,h) for h in HS]
    corr=[reduced_bianchi(z['minus'],t,p,q) for z in vals]
    hist=reduced_bianchi(vals[-1]['plus'],t,p,q)
    _,EN,EA,EB=c.exact_targets(t,p,q); target=np.array([EN,EA,EB],float)
    residuals=[relscalar(corr[-1][k],target[k],1e-12) for k in range(3)]
    step=relnorm(corr[-1],corr[-2],1e-12)
    hist_res=relnorm(hist,target,1e-12)
    valid=bool(sig and inv<=2e-11 and np.min(np.abs(target))>1e-10)
    passed=bool(valid and max(residuals)<=5e-4 and step<=2e-4 and hist_res>=1e-2)
    return {
        'gate':'ITER051C-D2-VARIATIONAL-SIGN-AND-HELDOUT-VALIDATION','stream':'A','index':i,
        'p':p,'q':q,'time':t,'corrected_pred':corr[-1].tolist(),'historical_pred':hist.tolist(),
        'exact_target':target.tolist(),'corrected_component_residuals':residuals,
        'corrected_max_residual':max(residuals),'corrected_final_step_change':step,
        'historical_plus2_vector_residual':hist_res,'signature_valid':sig,'max_inverse_residual':inv,
        'control_valid':valid,'lane_pass':passed,'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }


class SphericalMetric:
    def __init__(self,idx): self.idx=idx
    def values(self,r):
        i=self.idx
        if i==0:
            F=1+r/6+r*r/25; Fp=1/6+2*r/25; Fpp=2/25
            Nv=1+r*r/8; Np=r/4; Npp=1/4
            S=1+r+r*r/13; Sp=1+2*r/13; Spp=2/13
        elif i==1:
            F=1.5+r*r/10; Fp=r/5; Fpp=1/5
            Nv=1+r/7+r*r/30; Np=1/7+r/15; Npp=1/15
            S=2+r/3+r**3/40; Sp=1/3+3*r*r/40; Spp=3*r/20
        elif i==2:
            F=1+r/4+r**3/60; Fp=1/4+r*r/20; Fpp=r/10
            Nv=4/3+r*r/9; Np=2*r/9; Npp=2/9
            S=1+r/2+r*r/7; Sp=1/2+2*r/7; Spp=2/7
        else:
            F=2+r/8+r*r/12; Fp=1/8+r/6; Fpp=1/6
            Nv=1+r/5; Np=1/5; Npp=0.0
            S=1.5+r+r**3/50; Sp=1+3*r*r/50; Spp=3*r/25
        return (F,Fp,Fpp,Nv,Np,Npp,S,Sp,Spp)
    def jets(self,x):
        x=np.asarray(x,float); r=float(x[1]); th=float(x[2])
        F,Fp,Fpp,Nv,Np,Npp,S,Sp,Spp=self.values(r)
        st=math.sin(th); ct=math.cos(th)
        g=np.diag([-F*F,Nv*Nv,S*S,S*S*st*st])
        dg=np.zeros((N,N,N)); ddg=np.zeros((N,N,N,N))
        dg[1,0,0]=-2*F*Fp; dg[1,1,1]=2*Nv*Np; dg[1,2,2]=2*S*Sp; dg[1,3,3]=2*S*Sp*st*st
        dg[2,3,3]=2*S*S*st*ct
        ddg[1,1,0,0]=-2*(Fp*Fp+F*Fpp)
        ddg[1,1,1,1]=2*(Np*Np+Nv*Npp)
        ddg[1,1,2,2]=2*(Sp*Sp+S*Spp)
        ddg[1,1,3,3]=2*(Sp*Sp+S*Spp)*st*st
        ddg[1,2,3,3]=ddg[2,1,3,3]=4*S*Sp*st*ct
        ddg[2,2,3,3]=2*S*S*(ct*ct-st*st)
        return g,dg,ddg


B_R=[5/4,4/3,3/4,6/5]

def spherical_sympy_profile(i):
    r=s49.r; R=sp.Rational
    if i==0:
        return 1+r/R(6)+r**2/R(25),1+r**2/R(8),1+r+r**2/R(13),R(5,4)
    if i==1:
        return R(3,2)+r**2/R(10),1+r/R(7)+r**2/R(30),2+r/R(3)+r**3/R(40),R(4,3)
    if i==2:
        return 1+r/R(4)+r**3/R(60),R(4,3)+r**2/R(9),1+r/R(2)+r**2/R(7),R(3,4)
    return 2+r/R(8)+r**2/R(12),1+r/R(5),R(3,2)+r+r**3/R(50),R(6,5)

@lru_cache(maxsize=1)
def spherical_authority():
    return s49.authority()

def exact_spherical_target(i):
    auth=spherical_authority(); EF,EN,ES=auth[7],auth[8],auth[9]
    fv,nv,sv,rv=spherical_sympy_profile(i)
    vals=[s49.prof(expr,fv,nv,sv).subs(s49.r,rv) for expr in (EF,EN,ES)]
    return np.array([float(sp.N(v,30)) for v in vals],float)

def reduced_spherical(H,metric,r):
    F,_,_,Nv,_,_,S,_,_=metric.values(r)
    return np.array([-2*F*H[0,0],2*Nv*H[1,1],2*S*(H[2,2]+H[3,3])],float)

def stream_b(i):
    metric=SphericalMetric(i); r=B_R[i]; x=np.array([0.0,r,math.pi/2,0.0],float)
    sig,inv,det=stencil_controls(metric,x)
    vals=[assemble_both(metric,x,h) for h in HS]
    corr=[reduced_spherical(z['minus'],metric,r) for z in vals]
    hist=reduced_spherical(vals[-1]['plus'],metric,r)
    target=exact_spherical_target(i)
    residuals=[relscalar(corr[-1][k],target[k],1e-12) for k in range(3)]
    step=relnorm(corr[-1],corr[-2],1e-12); hist_res=relnorm(hist,target,1e-12)
    valid=bool(sig and inv<=2e-11 and np.min(np.abs(target))>1e-10)
    passed=bool(valid and max(residuals)<=1e-3 and step<=4e-4 and hist_res>=1e-2)
    return {
      'gate':'ITER051C-D2-VARIATIONAL-SIGN-AND-HELDOUT-VALIDATION','stream':'B','index':i,'radius':r,
      'corrected_pred':corr[-1].tolist(),'historical_pred':hist.tolist(),'exact_target':target.tolist(),
      'corrected_component_residuals':residuals,'corrected_max_residual':max(residuals),
      'corrected_final_step_change':step,'historical_plus2_vector_residual':hist_res,
      'signature_valid':sig,'max_inverse_residual':inv,'control_valid':valid,'lane_pass':passed,
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }


def stream_c(i):
    base=c.PolyMetric(C_SEEDS[i]); L=c.lorentz(i); trans=c.TransformMetric(base,L); x=np.zeros(N)
    sig0,inv0,_=stencil_controls(base,x); sig1,inv1,_=stencil_controls(trans,x)
    zb=[assemble_both(base,x,h) for h in HS]; zt=assemble_both(trans,x,HS[-1])
    H=zb[-1]['minus']; Hprev=zb[-2]['minus']; Ht=zt['minus']; M=np.linalg.inv(L)
    expected=M@H@M.T
    cov=relnorm(Ht,expected); sym=float(np.max(np.abs(H-H.T))); norm=float(np.linalg.norm(H)); step=relnorm(H,Hprev)
    metric_control=float(np.max(np.abs(trans.jets(x)[0]-L.T@base.jets(x)[0]@L)))
    valid=bool(sig0 and sig1 and max(inv0,inv1)<=2e-11 and metric_control<=2e-11)
    passed=bool(valid and norm>1e-7 and sym<=3e-7 and step<=2e-3 and cov<=1e-3)
    return {
      'gate':'ITER051C-D2-VARIATIONAL-SIGN-AND-HELDOUT-VALIDATION','stream':'C','index':i,'seed':C_SEEDS[i],
      'H_norm':norm,'H_symmetry_residual':sym,'H_final_step_change':step,'H_covariance_residual':cov,
      'metric_transform_control':metric_control,'max_inverse_residual':max(inv0,inv1),
      'signature_valid':bool(sig0 and sig1),'control_valid':valid,'lane_pass':passed,
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }


class FreshFLRW:
    def __init__(self,i): self.i=i
    def vals(self,t):
        if self.i==0: return 1+0.1*t+t*t/4,0.1+t/2,0.5
        if self.i==1: return 1.5+t/3+t**3/12,1/3+t*t/4,t/2
        if self.i==2: return 2+0.2*t*t+t**3/20,0.4*t+3*t*t/20,0.4+3*t/10
        return 1+t/5+t*t/7+t**3/30,1/5+2*t/7+t*t/10,2/7+t/5
    def jets(self,x):
        t=float(np.asarray(x)[0]); a,ap,app=self.vals(t)
        g=np.diag([-1.0,a*a,a*a,a*a]); dg=np.zeros((N,N,N)); ddg=np.zeros((N,N,N,N))
        for j in (1,2,3):
            dg[0,j,j]=2*a*ap; ddg[0,0,j,j]=2*(ap*ap+a*app)
        return g,dg,ddg

D_T=[0.45,0.7,0.9,1.1]
def stream_d(i):
    metric=FreshFLRW(i); x=np.array([D_T[i],0,0,0],float)
    sig,inv,_=stencil_controls(metric,x); z=assemble_both(metric,x,HS[-1])
    rnorm=float(np.linalg.norm(z['R'])); pnorm=float(np.linalg.norm(z['P'])); hnorm=float(np.linalg.norm(z['minus']))
    valid=bool(sig and inv<=2e-11 and rnorm>1e-6)
    passed=bool(valid and abs(z['I3'])<=2e-10 and pnorm<=3e-9 and hnorm<=2e-7)
    return {
      'gate':'ITER051C-D2-VARIATIONAL-SIGN-AND-HELDOUT-VALIDATION','stream':'D','index':i,'time':D_T[i],
      'riemann_norm':rnorm,'I3_abs':abs(z['I3']),'P_norm':pnorm,'H_norm':hnorm,
      'signature_valid':sig,'max_inverse_residual':inv,'control_valid':valid,'lane_pass':passed,
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',required=True,choices='ABCD'); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    limits={'A':8,'B':4,'C':4,'D':4}
    if not 0<=args.index<limits[args.stream]: raise SystemExit('index out of range')
    out={'A':stream_a,'B':stream_b,'C':stream_c,'D':stream_d}[args.stream](args.index)
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
