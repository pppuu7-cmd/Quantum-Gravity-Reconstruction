#!/usr/bin/env python3
"""QGR Iter015 / G13 — cubic microscopic-amplitude authority audit.

G12 established that S4 symmetry + elementary-axis nullity + pair locality can
select a unique pair-local cubic *shape*, while a genuine three-direction event
adds a second cubic shape.  The remaining question is authority: can the
quadratic pair action already derived in G5 determine either cubic coefficient?

Use the minimal S4-symmetric local jet through cubic order

  F(q) = k * sum_{i<j} q_i q_j
       + a * sum_{i<j} (q_i^2 q_j + q_i q_j^2)
       + b * sum_{i<j<k} q_i q_j q_k .

The G5 quadratic Hessian fixes k (up to the separately tracked overall scale),
but its quadratic jet contains no information about a or b.  G13 checks by
exact rational algebra that:

  * quadratic pair authority has a two-dimensional cubic nullspace (a,b);
  * one finite nonzero pair-amplitude datum, with k known, fixes a in this
    cubic truncation;
  * one connected three-event log-cumulant fixes b;
  * together those two microscopic data close the cubic coefficient rank;
  * all statements survive exact S4 and elementary-null checks.

This is an identifiability/authority result only.  It does not assume that QGR
already supplies the required finite-pair or connected-triple amplitudes.
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
from fractions import Fraction

N = 4
PERMS = list(itertools.permutations(range(N)))


def rank_frac(rows):
    A = [[Fraction(x) for x in r] for r in rows if any(x for x in r)]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                z = A[i][c]
                A[i] = [A[i][j] - z * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def F(q, k, a, b):
    q = [Fraction(x) for x in q]
    out = Fraction(0)
    for i, j in itertools.combinations(range(N), 2):
        out += k * q[i] * q[j]
        out += a * (q[i] * q[i] * q[j] + q[i] * q[j] * q[j])
    for i, j, l in itertools.combinations(range(N), 3):
        out += b * q[i] * q[j] * q[l]
    return out


def permute(q, p):
    out = [0] * N
    for i, x in enumerate(q):
        out[p[i]] = x
    return out


def subset_log_weight(A, k, a, b):
    """F evaluated on the Boolean indicator of subset A."""
    q = [1 if i in A else 0 for i in range(N)]
    return F(q, k, a, b)


def mobius_log_cumulant(A, k, a, b):
    A = tuple(sorted(A))
    total = Fraction(0)
    for r in range(len(A) + 1):
        for B in itertools.combinations(A, r):
            total += ((-1) ** (len(A) - r)) * subset_log_weight(set(B), k, a, b)
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', type=int, default=0)
    ap.add_argument('--out', default='g13.json')
    args = ap.parse_args()
    rng = random.Random(150913 + args.lane)

    # Lane-dependent exact rational coefficients.  Nonzero a,b make the
    # identifiability witnesses explicit without privileging a fitted value.
    k = Fraction(2 * args.lane + 3, args.lane + 2)
    a = Fraction((args.lane % 7) + 1, (args.lane % 5) + 3)
    b = Fraction((args.lane % 11) + 2, (args.lane % 6) + 5)

    # Parameter order is (k,a,b). Existing G5 quadratic authority observes k.
    M_quad = [[1, 0, 0]]
    # A finite unit pair datum L({i,j}) = k + 2a.
    M_pair = M_quad + [[1, 2, 0]]
    # A connected unit triple cumulant is exactly b.
    M_full = M_pair + [[0, 0, 1]]

    rank_quad = rank_frac(M_quad)
    rank_pair = rank_frac(M_pair)
    rank_full = rank_frac(M_full)
    cubic_nullity_from_quad = 3 - rank_quad
    residual_nullity_after_pair = 3 - rank_pair
    residual_nullity_after_triple = 3 - rank_full

    # Exact microscopic witnesses.
    pair = (0, 1)
    triple = (0, 1, 2)
    L2 = subset_log_weight(set(pair), k, a, b)
    K2 = mobius_log_cumulant(pair, k, a, b)
    K3 = mobius_log_cumulant(triple, k, a, b)
    a_recovered = (L2 - k) / 2
    b_recovered = K3

    # The quadratic jet is insensitive to arbitrary cubic deformations.
    # In coefficient language its only nonzero row is [1,0,0].
    alt_a = a + Fraction(args.lane + 1, 13)
    alt_b = b - Fraction(args.lane + 2, 17)
    quadratic_same = (k == k)
    cubic_changes = F([1, 2, -1, 3], k, a, b) != F([1, 2, -1, 3], k, alt_a, alt_b)

    perm_fail = 0
    axis_fail = 0
    cumulant_fail = 0
    for _ in range(128):
        q = [rng.randint(-5, 5) for _ in range(N)]
        p = PERMS[rng.randrange(len(PERMS))]
        if F(q, k, a, b) != F(permute(q, p), k, a, b):
            perm_fail += 1
        i = rng.randrange(N)
        t = rng.randint(-9, 9)
        ax = [0] * N
        ax[i] = t
        if F(ax, k, a, b) != 0:
            axis_fail += 1
        tri = tuple(sorted(rng.sample(range(N), 3)))
        if mobius_log_cumulant(tri, k, a, b) != b:
            cumulant_fail += 1

    # All six pair cumulants and four triple cumulants must be S4-degenerate.
    pair_vals = {mobius_log_cumulant(p, k, a, b) for p in itertools.combinations(range(N), 2)}
    triple_vals = {mobius_log_cumulant(t, k, a, b) for t in itertools.combinations(range(N), 3)}
    expected_pair_cumulant = k + 2 * a

    passed = all([
        rank_quad == 1,
        cubic_nullity_from_quad == 2,
        rank_pair == 2,
        residual_nullity_after_pair == 1,
        rank_full == 3,
        residual_nullity_after_triple == 0,
        a_recovered == a,
        b_recovered == b,
        K2 == expected_pair_cumulant,
        pair_vals == {expected_pair_cumulant},
        triple_vals == {b},
        quadratic_same,
        cubic_changes,
        perm_fail == 0,
        axis_fail == 0,
        cumulant_fail == 0,
    ])

    result = {
        'lane': args.lane,
        'coefficients': {'k': str(k), 'a': str(a), 'b': str(b)},
        'rank_quadratic_authority': rank_quad,
        'cubic_nullity_from_quadratic_authority': cubic_nullity_from_quad,
        'rank_after_finite_pair_datum': rank_pair,
        'residual_nullity_after_finite_pair_datum': residual_nullity_after_pair,
        'rank_after_connected_triple_datum': rank_full,
        'residual_nullity_after_connected_triple_datum': residual_nullity_after_triple,
        'finite_pair_log_weight': str(L2),
        'pair_connected_cumulant': str(K2),
        'triple_connected_cumulant': str(K3),
        'recovered_a': str(a_recovered),
        'recovered_b': str(b_recovered),
        'permutation_failures': perm_fail,
        'axis_null_failures': axis_fail,
        'triple_cumulant_failures': cumulant_fail,
        'conclusion': (
            'the G5 quadratic pair Hessian alone cannot fix either cubic coupling; '
            'within the G12 cubic truncation, one finite nonzero pair-amplitude datum fixes '
            'the pair-local cubic coefficient and one connected three-event datum fixes the '
            'genuine triadic coefficient'
        ),
        'claim_lock': (
            'exact finite four-direction identifiability audit; the needed microscopic '
            'finite-pair and connected-triple amplitudes are requirements, not yet derived QGR physics'
        ),
        'passed': passed,
    }
    with open(args.out, 'w') as f:
        json.dump(result, f, indent=2, sort_keys=True)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
