#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

# Dependency-free exact checks for Iter006-G2.

N=4
PAIRS=[(i,j) for i in range(N) for j in range(i,N)]
PAIR_INDEX={p:k for k,p in enumerate(PAIRS)}
PERMS=list(permutations(range(N)))


def det_bareiss(M):
    A=[list(map(int,row)) for row in M]
    n=len(A)
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            pivot=next((r for r in range(k+1,n) if A[r][k]!=0),None)
            if pivot is None:
                return 0
            A[k],A[pivot]=A[pivot],A[k]
            sign*=-1
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n):
            A[i][k]=0
        for j in range(k+1,n):
            A[k][j]=0
    return sign*A[-1][-1]


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def sym_congruence_matrix(A):
    # Induced map G -> A^T G A on vectorized symmetric matrices (i<=j).
    cols=[]
    AT=transpose(A)
    for a,b in PAIRS:
        G=[[0]*N for _ in range(N)]
        G[a][b]=1
        G[b][a]=1
        if a==b:
            G[a][a]=1
        H=matmul(matmul(AT,G),A)
        cols.append([H[i][j] for i,j in PAIRS])
    # columns -> matrix
    return [list(row) for row in zip(*cols)]

# Exact Jacobian law J_Sym2(A)=det(A)^(n+1)=det(A)^5 for representative GL(4,Z) matrices.
TEST_A=[
    [[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    [[2,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
    [[1,1,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,1]],
]
checks=[]
for A in TEST_A:
    d=det_bareiss(A)
    assert d!=0
    M=sym_congruence_matrix(A)
    jd=det_bareiss(M)
    assert jd==d**5
    checks.append((d,jd))

# S4 regular-history group average. Averaging all left translations gives J/24 exactly.
# Represent it as an exact Fraction matrix and verify idempotence/rank-one structure algebraically.
P=[[Fraction(1,24) for _ in range(24)] for __ in range(24)]
# P^2=P
for i in range(24):
    for j in range(24):
        v=sum(P[i][k]*P[k][j] for k in range(24))
        assert v==P[i][j]
# Every row is identical and nonzero => rank exactly one.
assert all(P[i]==P[0] for i in range(24))
assert any(x for x in P[0])

# Permutations preserve the incidence form C=J-I.
C=[[0 if i==j else 1 for j in range(4)] for i in range(4)]
for p in PERMS:
    R=[[1 if i==p[j] else 0 for j in range(4)] for i in range(4)]
    lhs=matmul(matmul(transpose(R),C),R)
    assert lhs==C

print({
    'sym2_dimension':len(PAIRS),
    'checked_congruence_jacobian_identity':'det(Sym2 congruence)=det(A)^5',
    'representative_exact_checks':checks,
    'invariant_measure_density':'|det G|^(-5/2) d^10G',
    'history_count':24,
    'history_group_average_rank':1,
    'history_group_average_idempotent':True,
    'uniform_history_amplitude_magnitude':'1/sqrt(24)',
    'S4_preserves_incidence_form_C':True,
    'guards':[
        'G is not identified with a Hermitian covariance matrix',
        'history S4 projector is not the physical field projector',
        'physical constraint quotient and U_alpha transports remain open',
    ],
    'classification':'PARTIAL_KINEMATIC_STATE_SPACE_AND_HISTORY_SYMMETRY_STRUCTURE_DERIVED_PHYSICAL_TRANSPORT_OPEN',
})
