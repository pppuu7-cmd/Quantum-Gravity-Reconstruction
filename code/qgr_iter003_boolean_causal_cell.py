#!/usr/bin/env python3
"""QGR Iter003 Boolean causal-cell exact combinatorics.

Tests a background-metric-free branching/recombining causal complex B_d and the
unique symmetric path normalization required to keep the CCRC projector
refinement-consistent. This is a scoped pre-ansatz construction, not a GR proof.
"""

from fractions import Fraction
from math import comb, factorial


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


def power(A, n):
    R = eye(len(A))
    for _ in range(n):
        R = mul(R, A)
    return R


# Nontrivial S3-standard CCRC label projector inherited prospectively from
# Iter002. No new coefficient is introduced here.
P = add(eye(3), scale(Fraction(-1, 3), ones(3)))
assert mul(P, P) == P

rows = []
for d in range(1, 7):
    rank_counts = [comb(d, r) for r in range(d + 1)]
    assert sum(rank_counts) == 2 ** d
    assert rank_counts[1] == d

    # B_d has d! maximal monotone chains from empty set to full set: each is
    # an ordering of the d independent generators.
    n_chains = factorial(d)
    chain_kernel = power(P, d)
    assert chain_kernel == P

    # Equal-chain symmetry plus the requirement K_coarse=P fixes w uniquely:
    # n_chains * w * P = P -> w=1/d! for nonzero P.
    w = Fraction(1, n_chains)
    coarse = scale(n_chains * w, chain_kernel)
    assert coarse == P

    rows.append({
        "d": d,
        "events": 2 ** d,
        "rank_counts": rank_counts,
        "maximal_chains": n_chains,
        "unique_equal_chain_weight": str(w),
        "coarse_kernel_equals_P": coarse == P,
    })

# Explicit 4-direction cell used as the Iter003 seed.
b4 = rows[3]
assert b4["d"] == 4
assert b4["events"] == 16
assert b4["rank_counts"] == [1, 4, 6, 4, 1]
assert b4["maximal_chains"] == 24
assert b4["unique_equal_chain_weight"] == "1/24"

print("QGR Iter003 Boolean causal-cell rows:")
for row in rows:
    print(row)
print("B4 seed: PASS_SCOPED_DERIVED_COMBINATORIAL_DIMENSION_AND_UNIQUE_PATH_NORMALIZATION")
