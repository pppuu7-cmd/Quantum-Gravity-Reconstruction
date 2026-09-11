#!/usr/bin/env python3
from fractions import Fraction

# QGR Iter003-G6: exact lower-rank redefinition quotient and mass protection audit.
# Pair variables x_ij live on the six rank-2 B4 events. Rank-1 redefinitions
# u_i induce x_ij -> x_ij + u_i + u_j = x + M^T u.

EDGES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]


def rank(mat):
    a=[[Fraction(x) for x in row] for row in mat]
    m,n=len(a),len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c] != 0),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c] != 0:
                q=a[i][c]; a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
    return r


def transpose(A): return [list(row) for row in zip(*A)]
def mm(A,B): return [[sum(Fraction(A[i][k])*Fraction(B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum(Fraction(a)*Fraction(b) for a,b in zip(row,v)) for row in A]
def madd(A,B,s=1): return [[A[i][j]+s*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

M=[[Fraction(0) for _ in range(6)] for _ in range(4)]
for e,(a,b) in enumerate(EDGES):
    M[a][e]=M[b][e]=Fraction(1)
assert rank(M)==4
MT=transpose(M)

# M M^T = 2 I + J for K4 unsigned incidence.
MMT=mm(M,MT)
expected=[[Fraction(3 if i==j else 1) for j in range(4)] for i in range(4)]
assert MMT==expected

# (2 I + J)^-1 = (1/2) I - (1/12) J.
MMTinv=[[Fraction(1,2)*(1 if i==j else 0)-Fraction(1,12) for j in range(4)] for i in range(4)]
I4=[[Fraction(1 if i==j else 0) for j in range(4)] for i in range(4)]
assert mm(MMT,MMTinv)==I4

# Orthogonal projector onto ker(M): P = I - M^T (M M^T)^-1 M.
I6=[[Fraction(1 if i==j else 0) for j in range(6)] for i in range(6)]
P=madd(I6,mm(mm(MT,MMTinv),M),s=-1)
assert mm(P,P)==P
zero46=[[Fraction(0) for _ in range(6)] for _ in range(4)]
assert mm(M,P)==zero46
assert rank(P)==2

# Gauge/redefinition invariance q=P x under x -> x+M^T u.
for u in ([1,0,0,0],[1,-2,3,0],[1,1,1,1]):
    du=mv(MT,[Fraction(x) for x in u])
    assert mv(P,du)==[Fraction(0)]*6

# Exact basis of physical quotient / balanced sector.
TT1=[Fraction(x) for x in [0,1,-1,-1,1,0]]
TT2=[Fraction(x) for x in [1,0,-1,-1,0,1]]
assert mv(P,TT1)==TT1
assert mv(P,TT2)==TT2

# Crucial negative result: a quadratic onsite term in q is invariant under the
# lower-rank redefinition because q itself is invariant. Current microscopic
# quotient therefore does not forbid m^2 q^2.
def norm2(v): return sum(x*x for x in v)
assert norm2(TT1)>0 and norm2(TT2)>0
# Any m^2 * norm2(Px) is unchanged by x -> x+M^T u.

print({
    'pair_space_dimension': 6,
    'rank1_redefinition_dimension': 4,
    'physical_quotient_dimension': 2,
    'physical_projector_rank': rank(P),
    'redefinition': 'x -> x + M^T u, i.e. x_ij -> x_ij+u_i+u_j',
    'TT_like_sector_is_gauge_invariant_quotient': True,
    'scalar_vector_pair_sectors_removed_by_rank1_redefinition': True,
    'onsite_mass_term_q2_allowed_by_current_redefinition': True,
    'masslessness_protected_by_current_microscopic_gauge': False,
    'global_shift_symmetry_of_G5_action_is_microscopically_derived': False,
})
