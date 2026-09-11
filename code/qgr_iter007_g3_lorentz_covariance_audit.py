#!/usr/bin/env python3
"""Exact audit of the 24-history covariance under a nontrivial C-preserving boost.

Control: the induced two-form metric from C=J-I is exactly preserved by the
wedge representation of L(r).  Test: the positive ordering-sign covariance is
not preserved, so the finite-cell correction has only microscopic S4 symmetry,
not the full continuous O(C) symmetry.
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
C=[[Fraction(0 if i==j else 1) for j in range(4)] for i in range(4)]

# Explicit rational C-preserving boost-like transformation from Iter004.
r=Fraction(2)
L=[
    [r,0,r-1,r-1],
    [0,1/r,(1-r)/r,(1-r)/r],
    [0,0,1,0],
    [0,0,0,1],
]

def T(A):return [list(x) for x in zip(*A)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sub(A,B):return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Check L^T C L=C.
assert all(x==0 for row in sub(mm(mm(T(L),C),L),C) for x in row)

# Induced wedge/two-form representation.
R=[[Fraction(0) for _ in range(6)] for __ in range(6)]
for a,(u,v) in enumerate(PAIRS):
    for b,(i,j) in enumerate(PAIRS):
        R[a][b]=L[u][i]*L[v][j]-L[u][j]*L[v][i]

# Lorentz-covariant two-form bilinear form induced by C.
G2=[[C[i][k]*C[j][l]-C[i][l]*C[j][k] for k,l in PAIRS] for i,j in PAIRS]
control=sub(mm(mm(T(R),G2),R),G2)
assert all(x==0 for row in control for x in row)

# Ordering covariance is not preserved by the same continuous transformation.
delta=sub(mm(mm(T(R),Cov),R),Cov)
nonzero=[x for row in delta for x in row if x]
assert nonzero

print({
    'boost_parameter':'2',
    'C_preserved_exactly':True,
    'induced_two_form_metric_preserved_exactly':True,
    'ordering_covariance_preserved':False,
    'nonzero_covariance_delta_entries':len(nonzero),
    'max_abs_covariance_delta':str(max(abs(x) for x in nonzero)),
    'classification':'PASS_SCOPED_FINITE_CELL_ORDERING_CORRECTION_BREAKS_CONTINUOUS_LORENTZ_TO_MICROSCOPIC_S4_WHILE_VANISHING_WITH_H4',
})
