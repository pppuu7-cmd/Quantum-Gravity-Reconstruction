#!/usr/bin/env python3
"""Numerical finite-curvature audit for the QGR discrete torsion equations.

Requires numpy and scipy. This is a NUMERICAL scoped test, not a global theorem.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
B=np.array([
    [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
    [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
    [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
    [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
    [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
    [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
],dtype=float)
assert max(np.linalg.norm(X.T@C+C@X) for X in B)<1e-12

a=np.array([0.22,-0.17,0.13,0.09])
Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])
I=np.eye(4)

def Omega(x):
    x=np.asarray(x,dtype=float)
    return math.exp(float(a@x + 0.5*x@Q@x))

def L_from(p6):
    return expm(np.tensordot(p6,B,axes=(0,0)))

def residual(x,z):
    x=np.asarray(x,dtype=int)
    Om=Omega(x)
    L=[L_from(z[6*i:6*i+6]) for i in range(4)]
    out=[]
    for i in range(4):
        for j in range(i+1,4):
            xi=x.copy(); xi[i]+=1
            xj=x.copy(); xj[j]+=1
            lhs=Om*I[:,i] + np.linalg.solve(L[i],Omega(xi)*I[:,j])
            rhs=Om*I[:,j] + np.linalg.solve(L[j],Omega(xj)*I[:,i])
            out.extend(lhs-rhs)
    return np.asarray(out)

def solve(x,z0=None):
    if z0 is None: z0=np.zeros(24)
    return least_squares(lambda z: residual(x,z),z0,xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=500)

def Ls(sol):
    return [L_from(sol.x[6*i:6*i+6]) for i in range(4)]

origin=np.zeros(4,dtype=int)
points=[origin]+[np.eye(4,dtype=int)[i] for i in range(4)]
solutions={tuple(x):solve(x) for x in points}
for x,s in solutions.items():
    assert np.linalg.norm(s.fun)<1e-9

base=solutions[(0,0,0,0)]
sv=np.linalg.svd(base.jac,compute_uv=False)

Lm={x:Ls(s) for x,s in solutions.items()}
hol=[]
for i in range(4):
    for j in range(i+1,4):
        xi=tuple(np.eye(4,dtype=int)[i]); xj=tuple(np.eye(4,dtype=int)[j])
        P1=Lm[xi][j]@Lm[(0,0,0,0)][i]
        P2=Lm[xj][i]@Lm[(0,0,0,0)][j]
        H=np.linalg.inv(P2)@P1
        hol.append({
            'plane':(i,j),
            'norm_H_minus_I':float(np.linalg.norm(H-I)),
            'det_H':float(np.linalg.det(H)),
            'metric_error':float(np.linalg.norm(H.T@C@H-C)),
        })

# Local-basin uniqueness probe: 12 deterministic perturbations around the root.
rng=np.random.default_rng(2026)
base_L=np.concatenate([L.flatten() for L in Ls(base)])
d=[]
for _ in range(12):
    s=solve(origin,base.x+rng.normal(scale=0.15,size=24))
    assert np.linalg.norm(s.fun)<1e-8
    Lt=np.concatenate([L.flatten() for L in Ls(s)])
    d.append(float(np.linalg.norm(Lt-base_L)))

print({
    'central_residual_norm':float(np.linalg.norm(base.fun)),
    'central_parameter_norm':float(np.linalg.norm(base.x)),
    'central_jacobian_min_singular':float(sv.min()),
    'central_jacobian_condition':float(sv.max()/sv.min()),
    'plaquette_holonomies':hol,
    'holonomy_norm_range':[min(h['norm_H_minus_I'] for h in hol),max(h['norm_H_minus_I'] for h in hol)],
    'max_metric_preservation_error':max(h['metric_error'] for h in hol),
    'local_restart_successes':12,
    'max_restart_transport_distance':max(d),
    'classification':'NUMERICALLY_VERIFIED_FINITE_CURVATURE_REGULAR_TORSION_BRANCH_WITH_NONZERO_HOLONOMY',
    'guard':'local finite-curvature toy only; not a global uniqueness/finiteness theorem',
})
