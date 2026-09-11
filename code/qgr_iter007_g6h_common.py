#!/usr/bin/env python3
"""Shared broadband future-null-cone integration utilities for Iter007 G6H."""
import math
import numpy as np
from qgr_iter007_g6g_common import solve_paths,to_minkowski,standard_null_map,Q0,OMEGA0,ETA

U0=np.array([1.,0.,0.,0.])

def branch_lorentz(h):
    dat=solve_paths(h)
    return dat,[to_minkowski(L) for L in dat['L_paths']]

def sphere_grid(ntheta=18,nphi=36):
    z,wz=np.polynomial.legendre.leggauss(ntheta)
    rows=[]
    for zz,ww in zip(z,wz):
        r=math.sqrt(max(0.,1.-zz*zz))
        for j in range(nphi):
            ph=2*math.pi*(j+0.5)/nphi
            n=np.array([r*math.cos(ph),r*math.sin(ph),zz])
            rows.append((n,float(ww*2*math.pi/nphi)))
    assert abs(sum(w for _,w in rows)-4*math.pi)<1e-12
    return rows

def direction_data(Lams,n,energy_scale=1.0):
    q=OMEGA0*energy_scale*np.array([1.,n[0],n[1],n[2]])
    Sq=standard_null_map(q);Sqi=np.linalg.inv(Sq)
    aa=[];th=[];closure=[]
    for Lam in Lams:
        k=np.linalg.solve(Lam,q)
        # Source envelope uses the source barycentric observer U0.
        a=float((U0@ETA@k)/(OMEGA0*energy_scale))
        assert a>1e-10,a
        W=Sqi@Lam@standard_null_map(k)
        closure.append(float(np.linalg.norm(W@Q0-Q0)))
        R2=W[1:3,1:3]
        theta=math.atan2(float(R2[1,0]-R2[0,1]),float(R2[0,0]+R2[1,1]))
        aa.append(a);th.append(theta)
    return np.asarray(aa),np.asarray(th),max(closure)

def radial_pair(profile,a,b):
    if profile=='m0': return 1.0/(a+b)**2
    if profile=='m1': return 6.0*a*b/(a+b)**4
    raise ValueError(profile)

def radial_norm(profile,a):
    if profile=='m0': return 1.0/(4.0*a*a)
    if profile=='m1': return 3.0/(8.0*a*a)
    raise ValueError(profile)

def overlap_matrix(Lams,profile='m0',polarization='linear',ntheta=18,nphi=36):
    nbranch=len(Lams);num=np.zeros((nbranch,nbranch),complex);norm=np.zeros(nbranch);maxclose=0.0
    for n,w in sphere_grid(ntheta,nphi):
        a,theta,cl=direction_data(Lams,n);maxclose=max(maxclose,cl)
        for p in range(nbranch): norm[p]+=w*radial_norm(profile,a[p])
        D=theta[:,None]-theta[None,:]
        if polarization=='envelope': pol=np.ones((nbranch,nbranch),complex)
        elif polarization=='linear': pol=np.cos(2.0*D).astype(complex)
        elif polarization=='helicity': pol=np.exp(2.0j*D)
        else: raise ValueError(polarization)
        for p in range(nbranch):
            for q in range(nbranch):
                num[p,q]+=w*radial_pair(profile,a[p],a[q])*pol[p,q]
    den=np.sqrt(norm[:,None]*norm[None,:]);O=num/den
    diag=float(np.max(np.abs(np.diag(O)-1.0)))
    herm=float(np.max(np.abs(O-O.conj().T)))
    purity=float(np.mean(np.abs(O)**2))
    return O,{'purity':purity,'loss':1.0-purity,'max_diagonal_error':diag,'max_hermiticity_error':herm,'max_little_group_closure_error':maxclose,'norm_spread':float((norm.max()-norm.min())/norm.mean())}

def exact_envelope_matrix(Lams,profile='m0'):
    us=np.array([L@U0 for L in Lams])
    gam=us@ETA@us.T
    if profile=='m0': return 2.0/(1.0+gam)
    if profile=='m1': return 4.0*(2.0+gam)/(3.0*(1.0+gam)**2)
    raise ValueError(profile)
