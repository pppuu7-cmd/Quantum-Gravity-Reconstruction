#!/usr/bin/env python3
from fractions import Fraction

# QGR Iter005-G1A representation-level census of zero-derivative cubic
# invariants on H = Sym^2(W4).
# S4 class order: e, (12), (12)(34), (123), (1234).

class_sizes = [1, 6, 3, 8, 6]
chi_H = [10, 4, 2, 1, 0]

# Character values on g^2 and g^3 for the same classes.
chi_H_g2 = [10, 10, 10, 1, 2]
chi_H_g3 = [10, 4, 2, 10, 0]

# Symmetric-cube character:
# chi_Sym3(g) = (chi(g)^3 + 3 chi(g) chi(g^2) + 2 chi(g^3))/6.
chi_sym3 = [
    Fraction(a**3 + 3*a*b + 2*c, 6)
    for a, b, c in zip(chi_H, chi_H_g2, chi_H_g3)
]
assert chi_sym3 == [220, 32, 12, 4, 0]

trivial_multiplicity = Fraction(
    sum(n*x for n, x in zip(class_sizes, chi_sym3)), 24
)
assert trivial_multiplicity == 20

print({
    'field_representation': 'H = Sym^2(W4), dim 10',
    'Sym3_character': [int(x) for x in chi_sym3],
    'S4_invariant_zero_derivative_cubic_dimension': int(trivial_multiplicity),
    'gauge_elimination_argument': (
        'For constant h and affine gauge parameter xi, the constant symmetric '
        'gradient delta0 h_ij = D_i xi_j + D_j xi_i spans all Sym^2(W4). '
        'A derivative quadratic action has no constant-field term capable of '
        'cancelling variation of a nonconstant algebraic cubic potential; '
        'therefore all 20 zero-derivative cubic directions are forbidden if '
        'the derived linear gauge symmetry is retained.'
    ),
    'classification': 'PASS_SCOPED_20_S4_CUBIC_POTENTIALS_CENSUSED_AND_ALL_EXCLUDED_BY_DERIVED_AFFINE_GAUGE_SHIFT',
    'next_sector': 'two-derivative cubic interactions',
})
