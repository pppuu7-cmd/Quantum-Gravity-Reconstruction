#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

# QGR Iter003-G2 exact finite toy audit.
# No continuum metric is used as input. The Lorentzian form below is derived
# conditionally from S4-equivalence plus the candidate null-cover hypothesis.

EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]


def rank(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r,m) if a[i][c] != 0), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        q = a[r][c]
        a[r] = [x/q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [a[i][j]-q*a[r][j] for j in range(n)]
        r += 1
    return r


def mv(mat, v):
    return [sum(Fraction(a)*Fraction(b) for a,b in zip(row,v)) for row in mat]


def dot(a,b):
    return sum(Fraction(x)*Fraction(y) for x,y in zip(a,b))

# Unsigned vertex-edge incidence matrix of K4 / the six pair directions.
M = [[0]*6 for _ in range(4)]
for j,(a,b) in enumerate(EDGES):
    M[a][j] = 1
    M[b][j] = 1
assert rank(M) == 4

# Exact two-dimensional kernel M x = 0.
TT1 = [0,1,-1,-1,1,0]
TT2 = [1,0,-1,-1,0,1]
assert mv(M, TT1) == [0,0,0,0]
assert mv(M, TT2) == [0,0,0,0]
assert rank([TT1,TT2]) == 2

SCALAR = [1]*6

def pair_from_vertex(u):
    return [u[a]+u[b] for a,b in EDGES]

V1 = pair_from_vertex([1,-1,0,0])
V2 = pair_from_vertex([0,1,-1,0])
V3 = pair_from_vertex([0,0,1,-1])

# 6 = 1 + 3 + 2 exact decomposition.
cols = [SCALAR,V1,V2,V3,TT1,TT2]
mat6 = [[cols[c][r] for c in range(6)] for r in range(6)]
assert rank(mat6) == 6
for t in (TT1,TT2):
    assert dot(t, SCALAR) == 0
    assert dot(t,V1) == dot(t,V2) == dot(t,V3) == 0

# S4-invariant direction-space bilinear form is alpha I + beta J.
# If the four equivalent elementary causal generators are additionally required
# to be null, diagonal entries vanish: alpha + beta = 0. Setting alpha=1 fixes
# only the irrelevant overall scale, giving g0 = I - J.
g0 = [[(1 if i==j else 0)-1 for j in range(4)] for i in range(4)]
# On the all-ones direction g0 has eigenvalue -3; on sum-zero directions +1.
ones4 = [1,1,1,1]
assert mv(g0,ones4) == [-3]*4
for u in ([1,-1,0,0],[0,1,-1,0],[0,0,1,-1]):
    assert mv(g0,u) == u
# Therefore signature is (-,+,+,+), up to overall sign.

# g0^{-1} = I - J/3.
ginv = [[Fraction(1 if i==j else 0)-Fraction(1,3) for j in range(4)] for i in range(4)]

def edge_tensor(x):
    H = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for coeff,(a,b) in zip(x,EDGES):
        H[a][b] = H[b][a] = Fraction(coeff)
    return H

def trace_product(A,B):
    # trace(A B)
    return sum(A[i][j]*B[j][i] for i in range(4) for j in range(4))

for t in (TT1,TT2):
    H = edge_tensor(t)
    # exact transversality against symmetric direction
    assert mv(H,ones4) == [0,0,0,0]
    # exact background trace zero
    assert trace_product(ginv,H) == 0

# The 2D sector is an irreducible S4 module. Two generator matrices in the
# {TT1,TT2} basis are enough to test its commutant.
Rswap = [[-1,-1],[0,1]]
Rcycle = [[1,0],[-1,-1]]
# Solving X R = R X for both generators gives X=lambda I. Verify by a small
# linear-system rank count in variables (a,b,c,d): 3 independent constraints.
def commutator_equations(R):
    # coefficient rows for entries of X R - R X = 0, X=(a b;c d)
    basisX = [
        [[1,0],[0,0]], [[0,1],[0,0]],
        [[0,0],[1,0]], [[0,0],[0,1]],
    ]
    rows=[]
    for p in range(2):
        for q in range(2):
            row=[]
            for X in basisX:
                XR = sum(X[p][k]*R[k][q] for k in range(2))
                RX = sum(R[p][k]*X[k][q] for k in range(2))
                row.append(XR-RX)
            rows.append(row)
    return rows
C = commutator_equations(Rswap)+commutator_equations(Rcycle)
assert rank(C) == 3  # commutant dimension 4-3 = 1

# Hence any S4-equivariant linear transfer on this sector is lambda I.
# Exact idempotent refinement T^2=T allows only lambda=0 or 1; a surviving
# nonzero tensor-like sector has lambda=1 and introduces no continuous coupling.
assert [q for q in (0,1) if q*q == q] == [0,1]

# Microscopic path-response witness. For F(pi)=sum of pair perturbations on
# adjacent directions in a maximal B4 chain, the TT-like sector has zero mean
# over all 24 chains (so first-order scalar normalization is unchanged) but
# nonzero variance (so the perturbation is not identically absent).
edge_index = {e:i for i,e in enumerate(EDGES)}
def path_response(t, p):
    s=0
    for k in range(3):
        e=tuple(sorted((p[k],p[k+1])))
        s += t[edge_index[e]]
    return s
for t in (TT1,TT2):
    vals=[path_response(t,p) for p in permutations(range(4))]
    assert sum(vals) == 0
    assert sum(v*v for v in vals) == 48  # variance = 48/24 = 2

print({
    'pair_space_decomposition': '6 = 1 + 3 + 2 under S4',
    'tt_like_dimension': 2,
    'conditional_null_frame_metric': 'g ~ I-J',
    'conditional_signature': '(-,+,+,+)',
    'tt_like_transverse_to_symmetric_direction': True,
    'tt_like_background_traceless': True,
    'S4_equivariant_transfer_commutant_dimension': 1,
    'idempotent_nonzero_transfer': 'lambda=1',
    'path_response_mean': 0,
    'path_response_variance': 2,
    'wave_equation_derived': False,
    'graviton_claim_authorized': False,
})
