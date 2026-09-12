#!/usr/bin/env python3
"""Iter043: independent analytic linearized TT-wave Weyl/covariance gate."""
from __future__ import annotations
import argparse,json,math,os
import numpy as np
from qgr_iter010_g2_common import weyl_proxy,weyl_cubic
from qgr_iter042_boosted_weyl import ETA,boost_matrix,weyl_quadratic,electric_magnetic

A=0.013
K=1.7
PSIS=[0.0,math.pi/8,math.pi/4,3*math.pi/8]
PHIS=[0.23,1.07]
DIRECTIONS=[np.array([1.,0.,0.]),np.array([0.,1.,0.]),np.array([0.,0.,1.])]
BOOSTS=[np.array([.11,.03,-.04]),np.array([-.06,.12,.02]),np.array([.04,-.05,.14]),np.array([.09,-.08,.05])]


def transverse_basis(n):
    refs=[np.array([1.,0.,0.]),np.array([0.,1.,0.]),np.array([0.,0.,1.])]
    ref=min(refs,key=lambda r:abs(float(np.dot(n,r))))
    u=np.cross(n,ref); u=u/np.linalg.norm(u)
    v=np.cross(n,u); v=v/np.linalg.norm(v)
    return u,v


def polarization(n,psi):
    u,v=transverse_basis(n)
    ep=np.outer(u,u)-np.outer(v,v)
    ex=np.outer(u,v)+np.outer(v,u)
    return math.cos(psi)*ep+math.sin(psi)*ex


def linearized_riemann(n,psi,phi):
    P3=polarization(n,psi)
    P=np.zeros((4,4),float); P[1:,1:]=P3
    q=np.concatenate(([1.0],-np.asarray(n,float)))
    # h''(q) for cos(K q + phi) at q=0.
    fac=-A*K*K*math.cos(phi)
    def d2(mu,nu,a,b):
        return fac*q[mu]*q[nu]*P[a,b]
    R=np.zeros((4,4,4,4),float)
    for a in range(4):
      for b in range(4):
       for c in range(4):
        for d in range(4):
         R[a,b,c,d]=0.5*(d2(c,b,a,d)+d2(d,a,b,c)-d2(d,b,a,c)-d2(c,a,b,d))
    return R,P3


def contractions(R):
    Ric=np.einsum('ac,abcd->bd',ETA,R)
    scal=float(np.einsum('bd,bd->',ETA,Ric))
    return Ric,scal


def normed_abs_diff(a,b,scale):
    return abs(float(a)-float(b))/max(float(scale),1e-30)


def lane(index):
    di=index//8; rem=index%8; pi=rem//2; fi=rem%2
    n=DIRECTIONS[di]; psi=PSIS[pi]; phi=PHIS[fi]; vel=BOOSTS[index%len(BOOSTS)]
    R,P3=linearized_riemann(n,psi,phi)
    Ric,scal=contractions(R)
    W,RicW,scalW=weyl_proxy(R)
    rn=float(np.linalg.norm(R)); wn=float(np.linalg.norm(W))
    trace=abs(float(np.trace(P3))); trans=float(np.linalg.norm(n@P3))
    ric_ratio=float(np.linalg.norm(Ric))/max(rn,1e-30)
    scalar_ratio=abs(scal)/max(rn,1e-30)
    weyl_reconstruction=float(np.linalg.norm(W-R))/max(rn,1e-30)
    proxy_ric_ratio=float(np.linalg.norm(RicW))/max(rn,1e-30)
    proxy_scalar_ratio=abs(float(scalW))/max(rn,1e-30)
    w2=float(weyl_quadratic(W)); w3=float(weyl_cubic(W))
    null2=abs(w2)/max(wn*wn,1e-30); null3=abs(w3)/max(wn**3,1e-30)
    E,B=electric_magnetic(W); en=float(np.linalg.norm(E)); bn=float(np.linalg.norm(B))
    balance=abs(en/max(bn,1e-30)-1.0)

    Lam=boost_matrix(vel); Linv=np.linalg.inv(Lam)
    lorentz_error=float(np.linalg.norm(Lam.T@ETA@Lam-ETA))
    Wt=np.einsum('pa,qb,rc,sd,pqrs->abcd',Linv,Linv,Linv,Linv,W)
    w2t=float(weyl_quadratic(Wt)); w3t=float(weyl_cubic(Wt)); wnt=float(np.linalg.norm(Wt))
    cov2=normed_abs_diff(w2t,w2,max(wn*wn,wnt*wnt))
    cov3=normed_abs_diff(w3t,w3,max(wn**3,wnt**3))

    controls=(trace<1e-13 and trans<1e-13 and ric_ratio<1e-11 and scalar_ratio<1e-11
              and weyl_reconstruction<1e-11 and proxy_ric_ratio<1e-11 and proxy_scalar_ratio<1e-11
              and lorentz_error<1e-12 and rn>1e-12)
    science=(cov2<1e-10 and cov3<1e-10 and en>1e-8 and bn>1e-8 and balance<1e-10
             and null2<1e-10 and null3<1e-10)
    passed=bool(controls and science)
    return {
      'gate':'ITER043-INDEPENDENT-TT-RADIATIVE-WEYL-COVARIANCE','index':index,
      'direction':n.tolist(),'psi':psi,'phi':phi,'velocity':vel.tolist(),
      'tt_trace':trace,'tt_transverse_norm':trans,'riemann_norm':rn,'weyl_norm':wn,
      'ricci_ratio':ric_ratio,'scalar_ratio':scalar_ratio,'proxy_ricci_ratio':proxy_ric_ratio,
      'proxy_scalar_ratio':proxy_scalar_ratio,'weyl_reconstruction_error':weyl_reconstruction,
      'lorentz_error':lorentz_error,'w2':w2,'w3':w3,'boosted_w2':w2t,'boosted_w3':w3t,
      'w2_covariance_error':cov2,'w3_covariance_error':cov3,'typeN_w2_null':null2,'typeN_w3_null':null3,
      'electric_norm':en,'magnetic_norm':bn,'electric_magnetic_balance_error':balance,
      'control_valid':bool(controls),'scientific_relation_pass':bool(science),'lane_pass':passed,
      'classification':'TT_RADIATIVE_LANE_PASS' if passed else ('TT_RADIATIVE_CONTROL_INVALID' if not controls else 'TT_RADIATIVE_SCIENTIFIC_FAIL')
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    assert 0<=a.index<24
    out=lane(a.index); os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,allow_nan=False)
    print(json.dumps(out,sort_keys=True,allow_nan=False))

if __name__=='__main__': main()
