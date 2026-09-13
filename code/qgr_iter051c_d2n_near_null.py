#!/usr/bin/env python3
import argparse, json, math, os
from functools import lru_cache
import numpy as np
import sympy as sp

import qgr_iter051c_full_eom as c
import qgr_iter051c_d2_sign_heldout as d2
import qgr_iter051b0_double_divergence_operator as b0
import qgr_iter051b1_weyl3_p_insertion as w3

N=4
H3=(1.0e-3,5.0e-4,2.5e-4)
H5=(2.0e-3,1.0e-3,5.0e-4)
A_R=[1.00,1.10,1.15,1.20,1.25,1.30]


def relnorm(a,b,floor=1e-14):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(b),floor))


def relscalar(a,b,floor=1e-14):
    return float(abs(a-b)/max(abs(b),floor))


def p_actual(metric,x):
    return c.P_actual(metric,np.asarray(x,float))


def derivative5(func,x,axis,h):
    x=np.asarray(x,float)
    e=np.zeros(N); e[axis]=h
    return (-func(x+2*e)+8.0*func(x+e)-8.0*func(x-e)+func(x-2*e))/(12.0*h)


def first_div5(metric,x,h):
    x=np.asarray(x,float)
    g,dg,ddg,gi,G,R=c.geometry(metric,x)
    P0=w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))
    dP=np.empty((N,N,N,N,N))
    for axis in range(N):
        dP[axis]=derivative5(lambda z:p_actual(metric,z),x,axis,h)
    S=b0.first_cov(P0,dP,G)
    return np.einsum('aambn->mbn',S)


def direct_D5(metric,x,h):
    x=np.asarray(x,float)
    g,dg,ddg,gi,G,R=c.geometry(metric,x)
    R0=first_div5(metric,x,h)
    D=np.zeros((N,N))
    for bb in range(N):
        dR=derivative5(lambda z:first_div5(metric,z,h),x,bb,h)
        D += dR[:,bb,:]
        for m in range(N):
            for n in range(N):
                for rr in range(N):
                    D[m,n]+=G[m,bb,rr]*R0[rr,bb,n]+G[bb,bb,rr]*R0[m,rr,n]+G[n,bb,rr]*R0[m,bb,rr]
    return D


def assemble_minus3(metric,x,h):
    z=c.assemble(metric,np.asarray(x,float),h)
    sg=math.sqrt(-float(np.linalg.det(z['g'])))
    H=z['A']+z['I']-2.0*sg*z['D']
    return H,z


def assemble_minus5(metric,x,h):
    g,dg,ddg,gi,G,R=c.geometry(metric,np.asarray(x,float))
    P=w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))
    A=c.algebraic_A(R,g)
    I=c.lowering_insertion(R,g,P)
    D=direct_D5(metric,np.asarray(x,float),h)
    sg=math.sqrt(-float(np.linalg.det(g)))
    H=A+I-2.0*sg*D
    return H,{'g':g,'R':R,'P':P,'A':A,'I':I,'D':D}


def extended_controls(metric,x):
    x=np.asarray(x,float); sig=[]; inv=[]; dets=[]
    h=max(H5)
    # Nested five-point outer+inner coordinate offsets can reach 4h.
    pts=[x]
    for axis in range(N):
        for k in (-4,-3,-2,-1,1,2,3,4):
            e=np.zeros(N); e[axis]=k*h; pts.append(x+e)
    for z in pts:
        g=metric.jets(z)[0]; gi=np.linalg.inv(g)
        ev=np.linalg.eigvalsh(0.5*(g+g.T))
        sig.append(bool(np.sum(ev<0)==1 and np.sum(ev>0)==3))
        inv.append(float(np.max(np.abs(g@gi-np.eye(N)))))
        dets.append(float(np.linalg.det(g)))
    return bool(all(sig) and max(dets)<0),float(max(inv)),float(max(dets))


@lru_cache(maxsize=1)
def authority():
    return d2.spherical_authority()


def profile_expr(profile):
    # Exact symbolic profiles matching d2.SphericalMetric.
    r=d2.s49.r; R=sp.Rational
    if profile==0:
        return 1+r/R(6)+r**2/R(25),1+r**2/R(8),1+r+r**2/R(13)
    if profile==1:
        return R(3,2)+r**2/R(10),1+r/R(7)+r**2/R(30),2+r/R(3)+r**3/R(40)
    if profile==3:
        return 2+r/R(8)+r**2/R(12),1+r/R(5),R(3,2)+r+r**3/R(50)
    raise ValueError(profile)


def exact_target(profile,rval):
    EF,EN,ES=authority()[7],authority()[8],authority()[9]
    fv,nv,sv=profile_expr(profile)
    rr=sp.Rational(str(rval))
    vals=[]
    for expr in (EF,EN,ES):
        v=d2.s49.prof(expr,fv,nv,sv).subs(d2.s49.r,rr)
        vals.append(float(sp.N(v,35)))
    return np.array(vals,float)


def reduced(H,metric,r):
    return d2.reduced_spherical(H,metric,r)


def lane(stream,index):
    if stream=='A':
        profile=3; r=A_R[index]; replay=(index==3)
    else:
        profile=index; r=[1.25,4.0/3.0][index]; replay=False
    metric=d2.SphericalMetric(profile); x=np.array([0.0,r,math.pi/2,0.0],float)
    sig,inv,det=extended_controls(metric,x)
    target=exact_target(profile,r)

    m3=[]
    hist=None
    for h in H3:
        H,z=assemble_minus3(metric,x,h)
        m3.append(reduced(H,metric,r))
        if h==H3[-1]:
            hist=reduced(z['A']+z['I']+2.0*math.sqrt(-float(np.linalg.det(z['g'])))*z['D'],metric,r)

    m5=[]
    for h in H5:
        H,z5=assemble_minus5(metric,x,h)
        m5.append(reduced(H,metric,r))

    m3f=m3[-1]; m5f=m5[-1]
    m3_abs=np.abs(m3f-target); m5_abs=np.abs(m5f-target)
    m3_rel=np.array([relscalar(m3f[k],target[k],1e-14) for k in range(3)])
    m5_rel=np.array([relscalar(m5f[k],target[k],1e-14) for k in range(3)])
    step5=relnorm(m5[-1],m5[-2],1e-14)
    vec5=relnorm(m5f,target,1e-14)
    hist_res=relnorm(hist,target,1e-14)
    angular_ratio=float(m5_abs[2]/max(m3_abs[2],1e-30))
    sign_ok=bool(np.sign(m5f[2])==np.sign(target[2])) if target[2]!=0 else bool(abs(m5f[2])<=2e-9)
    valid=bool(sig and inv<=2e-11 and np.linalg.norm(target)>1e-10)

    if replay:
        passed=bool(valid and sign_ok and m5_abs[2]<=2e-9 and angular_ratio<=0.35 and vec5<=5e-5 and step5<=5e-5 and hist_res>=1e-2)
    else:
        passed=bool(valid and vec5<=1e-4 and step5<=5e-5 and float(np.max(m5_abs))<=2e-7 and hist_res>=1e-2)

    return {
      'gate':'ITER051C-D2N-NEAR-NULL-SPHERICAL-CONDITIONING','stream':stream,'index':index,
      'profile':profile,'radius':r,'is_D2_B3_replay':replay,'exact_target':target.tolist(),
      'M3_finest_prediction':m3f.tolist(),'M3_abs_errors':m3_abs.tolist(),'M3_rel_errors':m3_rel.tolist(),
      'M5_predictions':[v.tolist() for v in m5],'M5_finest_prediction':m5f.tolist(),
      'M5_abs_errors':m5_abs.tolist(),'M5_rel_errors':m5_rel.tolist(),
      'M5_vector_relative_residual':vec5,'M5_final_step_change':step5,
      'M5_over_M3_angular_abs_error_ratio':angular_ratio,'M5_angular_sign_ok':sign_ok,
      'historical_plus2_vector_residual':hist_res,'signature_valid':sig,'max_inverse_residual':inv,
      'max_metric_det':det,'control_valid':valid,'lane_pass':passed,
      'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A','B'],required=True); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); args=ap.parse_args()
    lim=6 if args.stream=='A' else 2
    if not 0<=args.index<lim: raise SystemExit('index out of range')
    out=lane(args.stream,args.index)
    os.makedirs(os.path.dirname(args.out) or '.',exist_ok=True)
    with open(args.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
