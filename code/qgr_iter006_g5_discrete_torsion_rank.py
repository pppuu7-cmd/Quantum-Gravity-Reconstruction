#!/usr/bin/env python3
from fractions import Fraction

# Exact dependency-free certificate for the local discrete torsion-free
# connection Jacobian at the symmetric QGR seed.

C=[
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,1,1,0],
]

# Exact rational/integer basis of o(C): X^T C + C X = 0.
B=[
    [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
    [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
    [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
    [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
    [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
    [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
]


def transpose(A): return [list(r) for r in zip(*A)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Verify Lie-algebra basis exactly.
for X in B:
    z=add(mm(transpose(X),C),mm(C,X))
    assert all(v==0 for row in z for v in row)

# 24 unknowns c_{i,m}: four directions i, six Lorentz generators m.
# At e_j^a=delta_j^a, homogeneous torsion equation is
# (omega_i)^a_j - (omega_j)^a_i = 0 for every i<j and internal a.
M=[]
for i in range(4):
    for j in range(i+1,4):
        for a in range(4):
            row=[0]*24
            for m in range(6):
                row[6*i+m]+=B[m][a][j]
                row[6*j+m]-=B[m][a][i]
            M.append(row)
assert len(M)==24 and all(len(r)==24 for r in M)


def bareiss_det(A):
    A=[list(map(int,row)) for row in A]
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
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]


def rank_q(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        r+=1
    return r

rank=rank_q(M)
det=bareiss_det(M)
assert rank==24
assert det==11664

print({
    'lorentz_lie_algebra_dimension':6,
    'outgoing_connection_unknowns':24,
    'torsion_equations':24,
    'exact_jacobian_rank':rank,
    'exact_jacobian_determinant_in_recorded_basis':det,
    'homogeneous_kernel_dimension':24-rank,
    'classification':'PASS_SCOPED_LINEARIZED_DISCRETE_TORSION_MAP_FULL_RANK_24_OF_24',
    'consequence':'implicit-function theorem gives locally unique finite torsion-free holonomies near the symmetric seed',
    'guard':'global strong-curvature uniqueness and coarse/fine projective consistency remain open',
})
