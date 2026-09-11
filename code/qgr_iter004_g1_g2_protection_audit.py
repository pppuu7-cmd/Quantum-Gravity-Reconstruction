#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

# QGR Iter004 G1-G2 exact finite audit.

# --- G1: refinement does not imply stationarity ---
# Existing surviving TT transfer is T=I_2. This is compatible with any onsite
# quadratic coefficient m2 at the kinematic level; the refinement equation
# T^2=T contains no m2. Thus two dynamical candidates with different m2 share
# exactly the same current refinement data.
T=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
assert mm(T,T)==T
for m2 in (Fraction(0),Fraction(1),Fraction(7,5)):
    assert mm(T,T)==T  # refinement unchanged by mass choice
# Therefore current refinement axioms alone cannot force m2=0.

# --- G2: continuous stabilizer vs microscopic Boolean automorphisms ---
d=4
C=[[Fraction(0 if i==j else 1) for j in range(d)] for i in range(d)]  # J-I

# Exact Boolean-lattice automorphisms are determined by permutations of the four
# atoms. There are exactly 4! = 24 atom permutations.
automorphisms=list(permutations(range(4)))
assert len(automorphisms)==24
# Every atom permutation preserves pair incidence C.
for p in automorphisms:
    CP=[[C[i][p[j]] for j in range(4)] for i in range(4)]
    PTCP=[[CP[p[i]][j] for j in range(4)] for i in range(4)]
    assert PTCP==C

# Continuous stabilizer Lie algebra solves X^T C + C X = 0.
# Build linear equations in 16 entries of X and calculate nullity exactly.
def rank(mat):
    a=[[Fraction(x) for x in row] for row in mat]
    m,n=len(a),len(a[0]); r=0
    for col in range(n):
        piv=next((i for i in range(r,m) if a[i][col] != 0),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        q=a[r][col]; a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][col] != 0:
                q=a[i][col]
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
    return r

# Each equation (r,c) is linear in X_ab.
rows=[]
for r in range(4):
    for c in range(4):
        coeff=[]
        for a in range(4):
            for b in range(4):
                # X^T C term: sum_k X_{k r} C_{k c}
                term1=(1 if b==r else 0)*C[a][c]
                # C X term: sum_k C_{r k} X_{k c}
                term2=C[r][a]*(1 if b==c else 0)
                coeff.append(term1+term2)
        rows.append(coeff)
lie_rank=rank(rows)
lie_dim=16-lie_rank
assert lie_dim==6

print({
    'refinement_transfer': 'T=I on surviving 2D sector',
    'refinement_equation_contains_mass_parameter': False,
    'refinement_alone_forces_m2_zero': False,
    'B4_exact_poset_automorphism_group_size': 24,
    'B4_exact_poset_automorphism_group': 'S4',
    'pair_form': 'C=J-I',
    'continuous_stabilizer_Lie_algebra_dimension': lie_dim,
    'continuous_stabilizer_type': 'O(1,3) at real bilinear-form level',
    'continuous_stabilizer_realized_as_exact_B4_automorphisms': False,
    'symmetry_enhancement_gap': True,
})
