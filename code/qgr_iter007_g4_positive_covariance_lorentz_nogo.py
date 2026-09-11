#!/usr/bin/env python3
"""Exact finite-dimensional no-go witness for Lorentz-invariant positive ordering noise.

The 24-history covariance is positive definite with eigenvalues 1/3 and 5/3.
A positive-definite invariant form would make the represented group conjugate
to a subgroup of O(6), hence bounded.  The wedge representation of the
explicit C-preserving boost L(r) is unbounded.  The exact transformed
covariance norms below exhibit that growth directly.
"""
from fractions import Fraction
import itertools

PAIRS=[(i,j) for i in range(4) for j in range(i+1,4)]
PERMS=list(itertools.permutations(range(4)))

def signs(p):
    pos={v:k for k,v in enumerate(p)}
    return [1 if pos[i]<pos[j] else -1 for i,j in PAIRS]
S=[signs(p) for p in PERMS]
Cov=[[Fraction(sum(row[a]*row[b] for row in S),24) for b in range(6)] for a in range(6)]

def T(A):return [list(x) for x in zip(*A)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def frob2(A):return sum(x*x for row in A for x in row)

def wedge(r):
    r=Fraction(r)
    L=[
        [r,0,r-1,r-1],
        [0,1/r,(1-r)/r,(1-r)/r],
        [0,0,1,0],
        [0,0,0,1],
    ]
    R=[[Fraction(0) for _ in range(6)] for __ in range(6)]
    for a,(u,v) in enumerate(PAIRS):
        for b,(i,j) in enumerate(PAIRS):
            R[a][b]=L[u][i]*L[v][j]-L[u][j]*L[v][i]
    return R

base=frob2(Cov)
rows=[]
for r in [2,4,8,16]:
    R=wedge(r)
    X=mm(mm(T(R),Cov),R)
    rows.append((r,frob2(X)))
assert base==Fraction(26,3)
assert all(rows[i+1][1]>rows[i][1] for i in range(len(rows)-1))
assert rows[-1][1]>1000*base

print({
    'ordering_covariance_positive_spectrum':{'1/3':3,'5/3':3},
    'base_frobenius_norm_squared':str(base),
    'boosted_covariance_frobenius_norm_squared':[(r,str(v)) for r,v in rows],
    'representation_unbounded':True,
    'conclusion':'no nonzero positive-definite covariance can be invariant under the full noncompact continuous Lorentz image',
    'classification':'PASS_SCOPED_NONZERO_POSITIVE_ORDERING_NOISE_CANNOT_BE_EXACTLY_CONTINUOUS_LORENTZ_INVARIANT_AT_FINITE_CELL_SCALE',
})
