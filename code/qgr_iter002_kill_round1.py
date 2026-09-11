#!/usr/bin/env python3
"""QGR Iter002 kill-round-1 exact toy checks.

This script is intentionally small and dependency-free. It does not establish a
physical quantum-gravity theory. It verifies scoped algebraic/combinatorial
claims used to rank the pre-ansatz architecture branches A/CCRC, C/PCMH and
E/RQEC under QGR Constitution v1.0.
"""

from fractions import Fraction
from itertools import product


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def is_zero(A):
    return all(x == 0 for row in A for x in row)


def eye(n):
    return [[Fraction(int(i == j), 1) for j in range(n)] for i in range(n)]


def ones(n):
    return [[Fraction(1, 1) for _ in range(n)] for _ in range(n)]


def scale(c, A):
    return [[c * x for x in row] for row in A]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


# ---------------------------------------------------------------------------
# A / CCRC
# S3-invariant 3-label gluing operator K = a I + b J.
# Exact refinement/composition closure K^2=K forces the trivial and standard
# representation eigenvalues to lie in {0,1}; hence only four discrete
# projectors exist. Two are nontrivial: J/3 and I-J/3.
# ---------------------------------------------------------------------------

I3 = eye(3)
J3 = ones(3)
P_triv = scale(Fraction(1, 3), J3)
P_std = add(I3, scale(Fraction(-1, 3), J3))
assert is_zero(matsub(matmul(P_triv, P_triv), P_triv))
assert is_zero(matsub(matmul(P_std, P_std), P_std))

G = [
    [Fraction(-1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)],
]
PGP_triv = matmul(matmul(P_triv, G), P_triv)
PGP_std = matmul(matmul(P_std, G), P_std)
assert is_zero(PGP_triv)
assert not is_zero(PGP_std)

ccrc = {
    "idempotent_projector_classes": 4,
    "nontrivial_projector_classes": 2,
    "continuous_coefficient_freedom_after_S3_and_idempotence": 0,
    "P_trivial_preserves_traceless_geometry": False,
    "P_standard_preserves_traceless_geometry": True,
    "classification": "PASS_SCOPED_TOY_COMPOSITION_GEOMETRY_RIGIDITY",
}


# ---------------------------------------------------------------------------
# C / PCMH
# Binary projective refinement in its positive classical subcase already shows
# the rigidity problem. For every internal history h, projective consistency
# p(h)=p(h0)+p(h1) leaves one split parameter q_h in [0,1]:
# p(h0)=q_h p(h), p(h1)=(1-q_h)p(h).
# At depth d the number of independent internal split parameters is 2^d-1.
# Setting exchange symmetry q_h=1/2 removes them, but then the branch becomes
# the unique uniform refinement and carries no nontrivial local dynamics.
# ---------------------------------------------------------------------------

pcmh_freedom = {depth: 2 ** depth - 1 for depth in range(1, 7)}
assert pcmh_freedom == {1: 1, 2: 3, 3: 7, 4: 15, 5: 31, 6: 63}

pcmh = {
    "free_split_parameters_by_depth": pcmh_freedom,
    "freedom_growth": "exponential in refinement depth",
    "exchange_symmetric_choice": "q_h=1/2 for every internal node",
    "exchange_symmetric_result": "uniform refinement; rigidity obtained only by trivializing local split dynamics",
    "classification": "FAIL_SCOPED_RIGIDITY_MECHANISM_AS_STATED",
}


# ---------------------------------------------------------------------------
# E / RQEC
# Exact 3-qutrit erasure code:
# |0L>=(|000>+|111>+|222>)/sqrt(3)
# |1L>=(|012>+|120>+|201>)/sqrt(3)
# |2L>=(|021>+|102>+|210>)/sqrt(3)
# For each single site, Tr_rest |iL><jL| = delta_ij I/3, so any one-qutrit
# erasure is exactly correctable. Yet for the maximally mixed logical state,
# every two-qutrit reduced state is exactly I_9/9. Therefore all pair mutual
# informations vanish: recoverability/isometry alone supplies no adjacency
# signal, no dimension, and no causal orientation.
# ---------------------------------------------------------------------------

code_terms = [
    [(0, 0, 0), (1, 1, 1), (2, 2, 2)],
    [(0, 1, 2), (1, 2, 0), (2, 0, 1)],
    [(0, 2, 1), (1, 0, 2), (2, 1, 0)],
]


def one_site_reduced(i, j, site):
    # coefficient in |iL><jL| is 1/3 for each term pair
    M = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    other = [k for k in range(3) if k != site]
    for x in code_terms[i]:
        for y in code_terms[j]:
            if all(x[k] == y[k] for k in other):
                M[x[site]][y[site]] += Fraction(1, 3)
    return M


for site in range(3):
    for i in range(3):
        for j in range(3):
            M = one_site_reduced(i, j, site)
            target = [[Fraction(int(i == j and a == b), 3)
                       for b in range(3)] for a in range(3)]
            assert M == target


def pair_reduced_maximally_mixed(pair):
    # rho = (1/3) sum_i |iL><iL|, each outer-product term contributes 1/9.
    basis = list(product(range(3), repeat=2))
    index = {b: k for k, b in enumerate(basis)}
    M = [[Fraction(0) for _ in range(9)] for _ in range(9)]
    traced = ({0, 1, 2} - set(pair)).pop()
    for i in range(3):
        for x in code_terms[i]:
            for y in code_terms[i]:
                if x[traced] == y[traced]:
                    bx = (x[pair[0]], x[pair[1]])
                    by = (y[pair[0]], y[pair[1]])
                    M[index[bx]][index[by]] += Fraction(1, 9)
    return M


I9_over_9 = [[Fraction(int(i == j), 9) for j in range(9)] for i in range(9)]
for pair in ((0, 1), (0, 2), (1, 2)):
    assert pair_reduced_maximally_mixed(pair) == I9_over_9

rqec = {
    "single_qutrit_erasure_correctable": True,
    "maximally_mixed_logical_pair_state": "I_9/9 for every pair",
    "pair_mutual_information_bits": 0,
    "adjacency_derived_from_recoverability": False,
    "causal_orientation_derived_from_isometry": False,
    "classification": "FAIL_SCOPED_STANDALONE_GEOMETRY_CAUSALITY",
}


print("A/CCRC", ccrc)
print("C/PCMH", pcmh)
print("E/RQEC", rqec)
print("QGR Iter002 kill round 1: PASS")
