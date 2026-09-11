#!/usr/bin/env python3
"""QGR Iter006-G10A: reduced Gram-system audit of disconnected torsion branches.

This script eliminates the four Lorentz matrices from the flat symmetric seed
and works with six unordered edge vectors z_ij.  It verifies the regular
identity branch and a disconnected rank-22 solution, then performs a local
predictor/corrector continuation along the rank-22 solution manifold.

Requires numpy and scipy.  This is a scoped numerical/algebraic certificate;
it does not claim a classification of every branch.
"""
import itertools
import numpy as np
from scipy.linalg import qr
from scipy.optimize import least_squares, root

C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
E=np.eye(4)
PAIRS=[(i,j) for i in range(4) for j in range(i+1,4)]
PINDEX={p:k for k,p in enumerate(PAIRS)}

# At the flat seed e_i(v)=e_i(v+j)=standard basis.  Put
# y_ij=L_i^{-1}e_j and use torsion y_ij-y_ji=e_j-e_i.
# For i<j choose z_ij=y_ij.  The reverse orientation is then fixed linearly.
def y_affine(z,i,j):
    if i<j:
        q=PINDEX[(i,j)]
        return z[4*q:4*q+4],q
    q=PINDEX[(j,i)]
    return z[4*q:4*q+4]-(E[:,i]-E[:,j]),q

CONSTRAINTS=[]
for i in range(4):
    js=[j for j in range(4) if j!=i]
    for a,j in enumerate(js):
        for k in js[a:]:
            CONSTRAINTS.append((i,j,k))
assert len(CONSTRAINTS)==24

# Each L_i is Lorentz, so the three vectors y_ij (j!=i) have the same Gram
# matrix as the three seed null directions e_j.  This gives 24 quadrics in
# the 24 components of six z_ij.
def fun_jac(z):
    r=np.empty(24)
    J=np.zeros((24,24))
    for row,(i,j,k) in enumerate(CONSTRAINTS):
        yj,ej=y_affine(z,i,j)
        yk,ek=y_affine(z,i,k)
        r[row]=yj@C@yk-E[:,j]@C@E[:,k]
        J[row,4*ej:4*ej+4]+=C@yk
        J[row,4*ek:4*ek+4]+=C@yj
    return r,J

# Identity-connected flat solution: y_ij=e_j.
z_identity=np.concatenate([E[:,j] for i,j in PAIRS])
r0,J0=fun_jac(z_identity)
assert np.linalg.norm(r0)==0
s0=np.linalg.svd(J0,compute_uv=False)
assert np.sum(s0>1e-10)==24

# Exact integer Bareiss determinant of the identity-branch Jacobian.
def bareiss_det(A):
    A=[list(map(int,row)) for row in np.asarray(A,dtype=int)]
    n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next((r for r in range(k+1,n) if A[r][k]!=0),None)
            if p is None:return 0
            A[k],A[p]=A[p],A[k]; sign*=-1
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n):A[i][k]=0
    return sign*A[-1][-1]
identity_det=bareiss_det(J0)
assert identity_det==47775744

# Recorded distant solution from a deterministic broad search; correct it
# back onto the quadratic variety before continuation.
z_guess=np.array([
0.027361536996392908,1.0273615369963929,4.725938899305624,-0.8671441120818085,
-0.358813379423703,0.5309472439822166,0.641186620576297,0.09853562706300707,
-1.4035404628157553,2.2180630738413725,8.374655978690924,-0.4035404628157532,
-0.29732761473731917,0.4507676389312415,1.4507676389312416,-0.05521738660729675,
0.49670659715687704,-0.6912026586921711,3.529136227034926,0.308797341307829,
-0.40549432047045286,0.60633167293469,0.03141922267948116,1.0314192226794812])
sol=least_squares(lambda z:fun_jac(z)[0],z_guess,jac=lambda z:fun_jac(z)[1],
                  xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=200)
z=sol.x
r,J=fun_jac(z)
s=np.linalg.svd(J,compute_uv=False)
rank=int(np.sum(s>1e-8))
assert np.linalg.norm(r)<1e-10
assert rank==22
start_norm=float(np.linalg.norm(z))

# Continue outward along the radial projection onto the two-dimensional
# Jacobian null space.  At each step 22 independent quadratic equations plus
# two normal-plane constraints define the corrected point.
path=[z.copy()]
ds=0.4
for step in range(50):
    r,J=fun_jac(z)
    U,s,Vh=np.linalg.svd(J)
    assert int(np.sum(s>1e-8))==22
    N=Vh[-2:].T
    radial=N@(N.T@z)
    t=N[:,0] if np.linalg.norm(radial)<1e-10 else radial/np.linalg.norm(radial)
    cand=N[:,0]-t*(t@N[:,0])
    if np.linalg.norm(cand)<1e-7:
        cand=N[:,1]-t*(t@N[:,1])
    t2=cand/np.linalg.norm(cand)
    pred=z+ds*t
    _,_,piv_rows=qr(J.T,pivoting=True,mode='economic')
    rows=np.asarray(piv_rows[:22])
    def Fcorr(zz):
        rr,_=fun_jac(zz)
        return np.r_[rr[rows],t@(zz-pred),t2@(zz-pred)]
    def Jcorr(zz):
        _,JJ=fun_jac(zz)
        return np.vstack([JJ[rows],t,t2])
    rr=root(Fcorr,pred,jac=Jcorr,method='hybr',options={'xtol':1e-11})
    z=rr.x
    full=np.linalg.norm(fun_jac(z)[0])
    assert full<1e-9
    assert int(np.sum(np.linalg.svd(fun_jac(z)[1],compute_uv=False)>1e-8))==22
    path.append(z.copy())

end_norm=float(np.linalg.norm(path[-1]))
end_residual=float(np.linalg.norm(fun_jac(path[-1])[0]))
assert end_norm>30.0

print({
    'reduced_unknowns':24,
    'quadratic_gram_constraints':24,
    'identity_branch_rank':24,
    'identity_branch_exact_jacobian_det':identity_det,
    'distant_branch_rank':rank,
    'distant_branch_local_dimension':24-rank,
    'continuation_steps':50,
    'continuation_start_norm':start_norm,
    'continuation_end_norm':end_norm,
    'continuation_end_residual':end_residual,
    'classification':'REFUTED_IN_SCOPE_ALL_TORSION_ROOTS_FINITE__DISCONNECTED_UNBOUNDED_RANK22_BRANCH_EXISTS_AT_FLAT_SEED',
    'guard':'this does not refute the identity-connected refinement branch; it refutes summing all finite-cell torsion roots as physical connection branches',
})
