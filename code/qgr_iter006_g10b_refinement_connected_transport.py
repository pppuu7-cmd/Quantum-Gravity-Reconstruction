#!/usr/bin/env python3
"""QGR Iter006-G10B: principal identity-connected refinement transport audit.

The finite torsion equation has disconnected spurious branches.  This script
checks the branch selected by the already-derived infinitesimal connection:
solve from the identity on progressively finer cells and verify
L-I = O(h), agreement with the linearized Levi-Civita solve, and convergence
of products on a fixed physical path.

Requires numpy and scipy.
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
I=np.eye(4)
PAIRS=[(i,j) for i in range(4) for j in range(i+1,4)]

a=np.array([0.22,-0.17,0.13,0.09])
Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])

assert max(np.linalg.norm(X.T@C+C@X) for X in B)<1e-12

def Omega(x):
    x=np.asarray(x,dtype=float)
    return math.exp(float(a@x+0.5*x@Q@x))

def L_from(p6):
    return expm(np.tensordot(p6,B,axes=(0,0)))

def residual_at(z,x,h):
    x=np.asarray(x,dtype=float)
    Om=Omega(x)
    L=[L_from(z[6*i:6*i+6]) for i in range(4)]
    out=[]
    for i,j in PAIRS:
        xi=x.copy(); xi[i]+=h
        xj=x.copy(); xj[j]+=h
        lhs=Om*I[:,i]+np.linalg.solve(L[i],Omega(xi)*I[:,j])
        rhs=Om*I[:,j]+np.linalg.solve(L[j],Omega(xj)*I[:,i])
        out.extend(lhs-rhs)
    return np.asarray(out)

def principal_solve(x,h):
    # The zero start implements the previously fixed identity-connected branch.
    s=least_squares(lambda z:residual_at(z,x,h),np.zeros(24),
                    xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=700)
    assert np.linalg.norm(s.fun)<1e-8
    return s

# Linearized torsion solve at the origin.  For Omega=1+h a_i+O(h^2),
# omega_i e_j-omega_j e_i = h(a_i e_j-a_j e_i).
M=[]; src=[]
for i,j in PAIRS:
    for aa in range(4):
        row=np.zeros(24)
        for m in range(6):
            row[6*i+m]+=B[m,aa,j]
            row[6*j+m]-=B[m,aa,i]
        M.append(row)
        src.append(a[i]*(1 if aa==j else 0)-a[j]*(1 if aa==i else 0))
M=np.asarray(M); src=np.asarray(src)
assert np.linalg.matrix_rank(M)==24
linear=np.linalg.solve(M,src)

hs=[1.,0.5,0.25,0.125,0.0625]
rows=[]
for h in hs:
    s=principal_solve(np.zeros(4),h)
    L=[L_from(s.x[6*i:6*i+6]) for i in range(4)]
    rows.append({
        'h':h,
        'parameter_norm':float(np.linalg.norm(s.x)),
        'max_L_minus_I':float(max(np.linalg.norm(X-I) for X in L)),
        'residual_norm':float(np.linalg.norm(s.fun)),
        'linearized_scaled_error':float(np.linalg.norm(s.x/h-linear)),
    })

# Observed convergence orders for L-I.
orders=[]
for lo,hi in zip(rows[:-1],rows[1:]):
    p=math.log(hi['max_L_minus_I']/lo['max_L_minus_I'])/math.log(hi['h']/lo['h'])
    orders.append(float(p))
assert orders[-1]>0.98
assert rows[-1]['linearized_scaled_error']<0.01

# Fixed physical path x:0->e0, subdivided into N equal cells.
def path_transport(N,direction=0):
    h=1.0/N
    A=np.eye(4)
    max_res=0.0
    for n in range(N):
        x=np.zeros(4); x[direction]=n*h
        s=principal_solve(x,h)
        max_res=max(max_res,float(np.linalg.norm(s.fun)))
        L=L_from(s.x[6*direction:6*direction+6])
        xp=x.copy(); xp[direction]+=h
        # Coordinate/relational transport A=F_w^{-1} L F_v for F=Omega I.
        Aedge=(Omega(x)/Omega(xp))*L
        A=Aedge@A
    return A,max_res

Ns=[1,2,4,8,16]
paths={}
for N in Ns:
    A,max_res=path_transport(N)
    paths[N]={'A':A,'max_residual':max_res}

diffs=[]
for N in Ns[:-1]:
    diffs.append(float(np.linalg.norm(paths[2*N]['A']-paths[N]['A'])))
# First-order product convergence: successive differences should contract
# monotonically and the final contraction is close to 1/2.
assert all(diffs[i+1]<diffs[i] for i in range(len(diffs)-1))
assert diffs[-1]/diffs[-2]<0.6

print({
    'cell_scaling_rows':rows,
    'observed_L_minus_I_orders':orders,
    'linearized_connection_norm':float(np.linalg.norm(linear)),
    'fixed_path_subdivisions':Ns,
    'fixed_path_successive_differences':diffs,
    'classification':'PASS_SCOPED_REFINEMENT_CONNECTED_PRINCIPAL_BRANCH_CONVERGES_TO_INFINITESIMAL_LEVI_CIVITA_AND_HAS_PROJECTIVE_PRODUCT_LIMIT',
    'guard':'tested on deterministic curved conformal-frame family; general theorem requires regular Lorentzian fields with bounded jets and identity-connected local branch',
})
