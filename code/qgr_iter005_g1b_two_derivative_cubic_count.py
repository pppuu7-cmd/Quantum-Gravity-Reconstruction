#!/usr/bin/env python3
from fractions import Fraction

# Exact representation-theory count of local bosonic cubic vertices with total
# momentum degree two, after momentum conservation (translation / IBP quotient),
# invariant under simultaneous S4 action on QGR-L1 field and derivative directions.
#
# Field: H = Sym^2(W4), dim 10.
# Three bosonic legs are permuted by S3.
# Momentum conservation leaves, for each of four derivative directions, the
# 2D standard representation U of S3 on (k1,k2,k3) with k1+k2+k3=0.
# Degree-two momentum polynomials form Sym^2(W4 tensor U).

# S4 classes: e, (12), (12)(34), (123), (1234)
s4_sizes = [1, 6, 3, 8, 6]
chi_H = [10, 4, 2, 1, 0]   # Sym^2(W4)
chi_W4 = [4, 2, 0, 1, 0]
s4_square = [0, 0, 0, 3, 2]
s4_cube   = [0, 1, 2, 0, 4]

# S3 classes: e, transposition, 3-cycle
s3_sizes = [1, 3, 2]
chi_U = [2, 0, -1]          # standard 2D leg-momentum representation
s3_square = [0, 0, 2]
cycle_lengths = [[1,1,1], [2,1], [3]]


def field_tensor_char(g_class, s_class):
    # Trace of (g,g,g) combined with an S3 permutation on H^tensor3:
    # product over permutation cycles of chi_H(g^cycle_length).
    out = 1
    for L in cycle_lengths[s_class]:
        if L == 1:
            idx = g_class
        elif L == 2:
            idx = s4_square[g_class]
        else:
            idx = s4_cube[g_class]
        out *= chi_H[idx]
    return out


def momentum_sym2_char(g_class, s_class):
    # A = W4 tensor U under S4 x S3.
    chi_A = chi_W4[g_class] * chi_U[s_class]
    g2 = s4_square[g_class]
    s2 = s3_square[s_class]
    chi_A_sq_element = chi_W4[g2] * chi_U[s2]
    return Fraction(chi_A*chi_A + chi_A_sq_element, 2)

weighted = Fraction(0)
for gi, gs in enumerate(s4_sizes):
    for si, ss in enumerate(s3_sizes):
        weighted += gs * ss * field_tensor_char(gi,si) * momentum_sym2_char(gi,si)

invariant_dimension = weighted / (24*6)
assert invariant_dimension == 317

print({
    'field_representation': 'H=Sym^2(W4), dim 10',
    'bosonic_leg_group': 'S3',
    'momentum_conservation_representation': 'W4 tensor U_standard(S3)',
    'momentum_degree': 2,
    'IBP_translation_quotient': 'implemented by k1+k2+k3=0 / U_standard leg momentum representation',
    'S4xS3_invariant_two_derivative_cubic_vertex_dimension': int(invariant_dimension),
    'interpretation': 'complete kinematic cubic vertex space before nonlinear Noether constraints',
    'classification': 'PASS_SCOPED_COMPLETE_KINEMATIC_TWO_DERIVATIVE_CUBIC_VERTEX_COUNT_317',
    'guard': '317 is not the number of consistent self-couplings; delta0 S3 + delta1 S2 must still be solved',
})
