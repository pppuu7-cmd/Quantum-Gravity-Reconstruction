#!/usr/bin/env python3
from fractions import Fraction

# QGR Iter004-G3 exact S4 representation audit.
# Conjugacy classes order: e, (12), (12)(34), (123), (1234)
class_sizes=[1,6,3,8,6]

# Standard 3D representation = 4D vertex permutation rep minus trivial.
chi_V3=[3,1,-1,0,-1]
# Character evaluated on squares of class representatives:
# e->e, transposition->e, double-transposition->e, 3cycle->3cycle,
# 4cycle->double-transposition.
chi_V3_g2=[3,3,3,0,-1]
chi_sym2=[(a*a+b)//2 for a,b in zip(chi_V3,chi_V3_g2)]
assert chi_sym2==[6,2,2,0,0]

# Six unordered pairs of four atoms: character = number of fixed 2-subsets.
chi_pair6=[6,2,2,0,0]
assert chi_pair6==chi_sym2

# S4 irreducible character table in the same class order.
irreps={
    '1_trivial':[1,1,1,1,1],
    '3_standard':[3,1,-1,0,-1],
    '2_E':[2,0,2,-1,0],
    '3_sign_twist':[3,-1,-1,0,1],
    '1_sign':[1,-1,1,1,-1],
}

def inner(chi,psi):
    return Fraction(sum(n*a*b for n,a,b in zip(class_sizes,chi,psi)),24)

mult={name:inner(chi_pair6,chi) for name,chi in irreps.items()}
assert mult['1_trivial']==1
assert mult['3_standard']==1
assert mult['2_E']==1
assert mult['3_sign_twist']==0
assert mult['1_sign']==0

# The rank-1-to-rank-2 map M^T is injective for K4 (rank M=4), equivariant,
# so its image is isomorphic to the four-vertex permutation representation
# 4=1+3. The quotient of pair6 by that image is exactly the 2D E irrep.

print({
    'pair6_character': chi_pair6,
    'Sym2_standard3_character': chi_sym2,
    'pair6_is_Sym2_standard3': True,
    'decomposition': '6 = 1 + 3 + 2',
    'rank1_redefinition_image': '4 = 1 + 3',
    'physical_pair_quotient': '2',
    'interpretation_guard': 'exact tensor-like representation/counting only; no continuum SO3/Lorentz spin-2 theorem',
})
