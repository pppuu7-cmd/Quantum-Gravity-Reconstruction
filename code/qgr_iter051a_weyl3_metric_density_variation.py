#!/usr/bin/env python3
import argparse, json, math
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])


def make_q(seed, scale=0.18):
    rng=np.random.default_rng(seed)
    q=rng.normal(size=(4,4,4,4))*scale
    q=(q+q.swapaxes(0,1))/2
    q=(q+q.swapaxes(2,3))/2
    return q


def riemann_from_q(q):
    R=np.zeros((4,4,4,4),dtype=q.dtype)
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
    dtype=np.result_type(R,g,gi)
    C=np.empty((4,4,4,4),dtype=dtype)
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
    return np.einsum('abcd,cdef,efab->',Cup,Cup,Cup)


def density(g,R):
    gi=np.linalg.inv(g)
    C=weyl(R,g,gi)
    return np.sqrt(-np.linalg.det(g))*i3_from_C(C,gi)


def algebraic_controls(R,g):
    gi=np.linalg.inv(g)
    vals=[np.max(np.abs(R+R.swapaxes(0,1))),
          np.max(np.abs(R+R.swapaxes(2,3))),
          np.max(np.abs(R-R.transpose(2,3,0,1)))]
    cyc=R+R.transpose(0,2,3,1)+R.transpose(0,3,1,2)
    vals.append(np.max(np.abs(cyc)))
    C=weyl(R,g,gi)
    tr=np.einsum('ac,abcd->bd',gi,C)
    return float(max(vals)),float(np.max(np.abs(tr)))


def transform2(T,A):
    return A.T@T@A


def transform4(T,A):
    return np.einsum('ia,jb,kc,ld,ijkl->abcd',A,A,A,A,T)


def boost_x(v):
    ga=1/math.sqrt(1-v*v)
    A=np.eye(4); A[0,0]=ga; A[1,1]=ga; A[0,1]=-ga*v; A[1,0]=-ga*v
    return A


def generic_A():
    A=np.array([[1.08,0.06,0.00,0.02],
                [0.03,0.94,0.05,0.00],
                [0.00,0.04,1.11,0.03],
                [0.01,0.00,0.02,0.91]],dtype=float)
    if np.linalg.det(A)<=0: raise RuntimeError('bad transform determinant')
    return A


def rel(a,b,floor=1e-14):
    return float(abs(a-b)/max(abs(a),abs(b),floor))


def signature_ok(g):
    ev=np.linalg.eigvalsh(g)
    return int(np.sum(ev<0))==1 and int(np.sum(ev>0))==3


def run(lane):
    seed=4001+lane*131
    rng=np.random.default_rng(seed)
    R=riemann_from_q(make_q(seed))
    X=rng.normal(size=(4,4)); h=(X+X.T)*0.025
    g=ETA.copy()
    alg_res,tr_res=algebraic_controls(R,g)
    L0=density(g,R)
    cs_eps=1e-30
    cs=float(np.imag(density(g.astype(complex)+1j*cs_eps*h,R.astype(complex)))/cs_eps)
    epss=[2e-4,1e-4,5e-5,2.5e-5]
    fds=[]; errs=[]; sigs=[]
    for e in epss:
        gp=g+e*h; gm=g-e*h
        sigs.extend([signature_ok(gp),signature_ok(gm)])
        fd=float(np.real((density(gp,R)-density(gm,R))/(2*e)))
        fds.append(fd); errs.append(abs(fd-cs))
    finest_rel=rel(fds[-1],cs,1e-12)
    conv=(errs[-1] <= 1.05*errs[-2]) and ((errs[-1] < 1e-10) or (errs[-2]/max(errs[-1],1e-30) >= 2.5))
    cov=[]
    for A in (boost_x(0.23),generic_A()):
        gt=transform2(g,A); ht=transform2(h,A); Rt=transform4(R,A)
        jac=abs(float(np.linalg.det(A)))
        Lt=density(gt,Rt)
        cst=float(np.imag(density(gt.astype(complex)+1j*cs_eps*ht,Rt.astype(complex)))/cs_eps)
        cov.append({"density_rel":rel(float(np.real(Lt))/jac,float(np.real(L0)),1e-12),
                    "direction_rel":rel(cst/jac,cs,1e-12),"jacobian":jac})
    valid=all(sigs) and alg_res<=1e-11 and tr_res<=1e-10
    derivative_ok=(finest_rel<=2e-6 or abs(fds[-1]-cs)<=1e-9) and conv
    covariance_ok=max(x['density_rel'] for x in cov)<=1e-9 and max(x['direction_rel'] for x in cov)<=1e-8
    nonzero=abs(L0)>1e-8 and abs(cs)>1e-8
    passed=valid and derivative_ok and covariance_ok
    out={"lane":lane,"seed":seed,"density":float(np.real(L0)),"complex_step_directional":cs,
         "fd":fds,"errors":errs,"finest_rel":finest_rel,"convergence_ok":conv,
         "signature_controls":sigs,"algebraic_residual":alg_res,"weyl_trace_residual":tr_res,
         "covariance":cov,"valid":valid,"derivative_ok":derivative_ok,"covariance_ok":covariance_ok,
         "nonzero_calibration":nonzero,"pass":passed}
    print(json.dumps(out,sort_keys=True))
    if not passed: raise SystemExit(2)


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); args=ap.parse_args(); run(args.lane)
