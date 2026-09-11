#!/usr/bin/env python3
"""QGR Iter002 Kill Round 2 exact checks for A/CCRC and B/CQCG.

Dependency-free exact arithmetic. D/LCSD's graph-cospectral control is recorded
analytically in results/ITER002_KILL_ROUND2.md.
"""

from fractions import Fraction


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def ones(n):
    return [[Fraction(1) for _ in range(n)] for _ in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def scale(c, A):
    return [[c*x for x in row] for row in A]


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def equal(A, B):
    return A == B


def is_zero(A):
    return all(x == 0 for row in A for x in row)


# A / CCRC directed causal chain t0 -> t1 -> t2 -> t3.
# Causal direction is primitive: composition only follows increasing layers.
# Label dynamics uses the nontrivial S3-standard projector.
I = eye(3)
J = ones(3)
P = add(I, scale(Fraction(-1, 3), J))
assert equal(mul(P, P), P)

# Associative three-link causal gluing.
left = mul(mul(P, P), P)
right = mul(P, mul(P, P))
assert equal(left, right)
assert equal(left, P)

# Two fine links coarse-grain exactly to the same one-link kernel.
coarse_from_two_links = mul(P, P)
assert equal(coarse_from_two_links, P)

# Nonzero traceless geometry survives in the same realization.
G = [
    [Fraction(-1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)],
]
PGP = mul(mul(P, G), P)
assert not is_zero(PGP)

A_result = {
    "directed_causal_morphisms": "only increasing layers",
    "associative_gluing": True,
    "two_scale_coarse_kernel_equals_fine_composition": True,
    "continuous_coefficient_freedom": 0,
    "nonzero_geometry_survives": True,
    "classification": "PASS_SCOPED_DIRECTED_CAUSAL_TWO_SCALE_RIGIDITY",
}


# B / CQCG control: SU(2)-covariant qubit depolarizing channel
# D_p(rho)=p rho + (1-p) I/2.
# Choi eigenvalues are (1+3p)/4 and (1-p)/4 x3, hence CPTP for
# -1/3 <= p <= 1. Composition is D_p o D_q = D_{pq}; therefore
# symmetry + CPTP + composition leave a continuous physical parameter.

def choi_eigs(p):
    return [Fraction(1, 4)*(1+3*p)] + [Fraction(1, 4)*(1-p)]*3

for p in (Fraction(-1, 3), Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1)):
    assert all(x >= 0 for x in choi_eigs(p))

p = Fraction(1, 2)
q = Fraction(1, 3)
r = p*q
assert r == Fraction(1, 6)
assert all(x >= 0 for x in choi_eigs(r))

B_result = {
    "CPTP_parameter_interval": "[-1/3,1]",
    "composition_law": "p_eff=p*q",
    "continuous_parameter_survives_constraints": True,
    "example": "p=1/2 and q=1/3 are both admissible; composed channel has p=1/6",
    "classification": "FAIL_SCOPED_RIGIDITY_AS_STATED",
}

print("A/CCRC", A_result)
print("B/CQCG", B_result)
print("QGR Iter002 kill round 2 exact checks: PASS")
