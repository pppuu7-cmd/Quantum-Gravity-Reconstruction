#!/usr/bin/env python3
from fractions import Fraction

# QGR Iter003-G3: exact linearized kinetic-seed audit.
# Field values live in the already isolated 2D S4 TT-like irrep. By the G2
# commutant result, any S4-equivariant internal kinetic matrix is proportional
# to the 2x2 identity, so only the four causal-direction tensor is audited here.

# Most general S4-invariant symmetric contravariant principal tensor:
# G = A I + B J. Set the irrelevant overall A=1 after solving the ratio.
# Its inverse is
# G^{-1} = (1/A) I - B/[A(A+4B)] J.
# Every diagonal entry is (A+3B)/[A(A+4B)].
# Requiring the four elementary causal cover directions e_i to be null tangent
# directions of the inverse metric therefore gives A+3B=0.

A = Fraction(1)
B = -Fraction(1,3)

G = [[(A if i==j else 0) + B for j in range(4)] for i in range(4)]
g = [[(Fraction(1) if i==j else 0) - Fraction(1) for j in range(4)] for i in range(4)]


def mv(M,v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

I4 = [[Fraction(1 if i==j else 0) for j in range(4)] for i in range(4)]
assert mm(G,g) == I4

# Elementary cover directions are exactly null in g.
for i in range(4):
    assert g[i][i] == 0

# Signature audit by invariant subspaces.
ones = [Fraction(1)]*4
assert mv(G,ones) == [-Fraction(1,3)]*4
for u in ([1,-1,0,0],[0,1,-1,0],[0,0,1,-1]):
    assert mv(G,[Fraction(x) for x in u]) == [Fraction(x) for x in u]
# So G has eigenvalues (-1/3,+1,+1,+1), hence a hyperbolic principal symbol.

# In an orthonormal decomposition p=p0*u0+p_perp with
# u0=(1,1,1,1)/2, principal symbol is
# K(p)=-(1/3) p0^2 + |p_perp|^2.
# Its characteristic cone is nonempty and Lorentzian.

# Exact lattice realization using forward differences d_i and adjoint backward
# differences: L = sum_ij G_ij D_i^- D_j^+.  The coefficient matrix is fixed
# up to a single overall normalization. No relative kinetic coefficient remains.

# Check S4 invariance directly for all 24 permutations: P^T G P = G.
from itertools import permutations
for p in permutations(range(4)):
    GP = [[G[i][p[j]] for j in range(4)] for i in range(4)]
    PTGP = [[GP[p[i]][j] for j in range(4)] for i in range(4)]
    assert PTGP == G

# Two TT-like polarizations receive exactly the same operator because the G2
# commutant of their S4 representation is one-dimensional.

print({
    'general_S4_direction_tensor': 'A I + B J',
    'null_cover_condition': 'diag((A I + B J)^-1)=0',
    'exact_ratio': 'B/A=-1/3',
    'normalized_principal_tensor': 'I-J/3',
    'inverse_metric_seed': 'I-J',
    'principal_eigenvalues': ['-1/3','1','1','1'],
    'hyperbolic_signature': True,
    'relative_kinetic_freedom': 0,
    'overall_normalization_freedom': 1,
    'two_TT_like_components_degenerate': True,
    'nonlinear_GR_dynamics_derived': False,
    'microscopic_origin_of_quadratic_update_derived': False,
})
