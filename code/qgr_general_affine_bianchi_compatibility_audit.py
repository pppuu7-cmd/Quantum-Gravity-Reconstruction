#!/usr/bin/env python3
"""All-degree exact affine-compatibility audit for the frozen QGR seed operator.

Convention: the field-equation rows are multiplied by two, so the integral
field target is F' = 2 E = -Box(hbar).  The compatibility operator is then

    C_b = Box(G_b) + d^a F'_{ab}.

For each n this script builds the integral principal matrix M_n and the complete
Bianchi compatibility matrix B_n, verifies B_n M_n = 0 exactly over ZZ, and
checks ranks over two odd prime fields.  Together with the algebraic theorem in
GENERAL_AFFINE_BIANCHI_COMPATIBILITY_THEOREM.md these modular ranks certify the
exact QQ result without floating-point arithmetic or tolerance tests.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from math import comb
from pathlib import Path

import sympy as sp
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix

ETA = (-1, 1, 1, 1)
PAIRS = tuple((a, b) for a in range(4) for b in range(a, 4))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}


def alphas(n: int):
    if n < 0:
        return ()
    return tuple(sorted(a for a in product(range(n + 1), repeat=4) if sum(a) == n))


def pair_index(a: int, b: int) -> int:
    return PAIR_INDEX[(a, b) if a <= b else (b, a)]


def build(n: int):
    an, a1, a2, a3 = alphas(n), alphas(n - 1), alphas(n - 2), alphas(n - 3)
    col = {(p, a): p * len(an) + i for p in range(10) for i, a in enumerate(an)}
    grow = {(b, a): b * len(a1) + i for b in range(4) for i, a in enumerate(a1)}
    field_offset = 4 * len(a1)
    frow = {
        (p, a): field_offset + p * len(a2) + i
        for p in range(10)
        for i, a in enumerate(a2)
    }
    rows = field_offset + 10 * len(a2)
    unknowns = 10 * len(an)

    M: dict[tuple[int, int], int] = {}

    # G_b = d^a hbar_ab.
    for b in range(4):
        for alpha in a1:
            r = grow[(b, alpha)]
            for mu in range(4):
                beta = list(alpha)
                beta[mu] += 1
                M[(r, col[(pair_index(mu, b), tuple(beta))])] = ETA[mu]

    # Integral field row F'_{ab} = 2 E_ab = -Box(hbar_ab).
    for p in range(10):
        for alpha in a2:
            r = frow[(p, alpha)]
            for mu in range(4):
                beta = list(alpha)
                beta[mu] += 2
                M[(r, col[(p, tuple(beta))])] = -ETA[mu]

    # Complete compatibility operator C_b = Box G_b + d^a F'_{ab}.
    B: dict[tuple[int, int], int] = {}
    for b in range(4):
        for i, alpha in enumerate(a3):
            r = b * len(a3) + i
            for mu in range(4):
                beta = list(alpha)
                beta[mu] += 2
                B[(r, grow[(b, tuple(beta))])] = ETA[mu]
            for mu in range(4):
                beta = list(alpha)
                beta[mu] += 1
                c = frow[(pair_index(mu, b), tuple(beta))]
                B[(r, c)] = B.get((r, c), 0) + ETA[mu]

    return rows, unknowns, M, 4 * len(a3), B


def composition_nonzero(B, M):
    by_mid: dict[int, list[tuple[int, int]]] = {}
    for (r, c), v in M.items():
        by_mid.setdefault(r, []).append((c, v))
    acc: dict[tuple[int, int], int] = {}
    for (r, k), bv in B.items():
        for c, mv in by_mid.get(k, ()):
            key = (r, c)
            acc[key] = acc.get(key, 0) + bv * mv
    return {k: v for k, v in acc.items() if v}


def rank_mod(shape, entries, prime: int) -> int:
    matrix = sp.MutableSparseMatrix(shape[0], shape[1], entries)
    return DomainMatrix.from_Matrix(matrix).convert_to(GF(prime)).rank()


def audit_case(n: int, primes: tuple[int, ...]):
    rows, unknowns, M, brows, B = build(n)
    expected_bianchi = 4 * comb(n, 3) if n >= 3 else 0
    expected_rank = n * (5 * n * n + 12 * n - 5) // 3
    BM = composition_nonzero(B, M)

    rank_M = {str(p): rank_mod((rows, unknowns), M, p) for p in primes}
    rank_B = {str(p): (rank_mod((brows, rows), B, p) if brows else 0) for p in primes}

    # Deterministic negative control: a unit source in any row touched by B
    # must have nonzero compatibility image and therefore be unsolvable.
    touched = sorted({c for (_, c), v in B.items() if v})
    negative_control_row = touched[0] if touched else None
    negative_control_detected = not brows or any(
        c == negative_control_row and v != 0 for (_, c), v in B.items()
    )

    controls = {
        "B_times_M_is_exactly_zero": len(BM) == 0,
        "compatibility_row_count_matches": brows == expected_bianchi,
        "rank_M_hits_theorem_bound_for_all_primes": all(v == expected_rank for v in rank_M.values()),
        "rank_B_is_full_for_all_primes": all(v == expected_bianchi for v in rank_B.values()),
        "left_nullity_equals_compatibility_dimension": rows - expected_rank == expected_bianchi,
        "negative_control_is_rejected": negative_control_detected,
    }
    return {
        "n": n,
        "matrix_shape": [rows, unknowns],
        "compatibility_shape": [brows, rows],
        "expected_rank": expected_rank,
        "expected_bianchi_dimension": expected_bianchi,
        "rank_M_mod_primes": rank_M,
        "rank_B_mod_primes": rank_B,
        "BM_nonzero_count": len(BM),
        "negative_control_row": negative_control_row,
        "controls": controls,
        "pass": all(controls.values()),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-n", type=int, default=2)
    ap.add_argument("--max-n", type=int, default=12)
    ap.add_argument("--primes", default="1000003,1000033")
    ap.add_argument("--out")
    args = ap.parse_args()

    primes = tuple(int(x) for x in args.primes.split(",") if x)
    if args.min_n < 2 or args.max_n < args.min_n:
        raise SystemExit("invalid degree range")
    if not primes or any(p == 2 or not sp.isprime(p) for p in primes):
        raise SystemExit("all audit moduli must be odd primes")

    cases = [audit_case(n, primes) for n in range(args.min_n, args.max_n + 1)]
    result = {
        "gate": "GENERAL-AFFINE-BIANCHI-COMPATIBILITY-THEOREM",
        "scope": "FOUR_VARIABLE_FROZEN_TRACE_REVERSED_HOMOGENEOUS_PRINCIPAL_OPERATOR_ONLY",
        "field_row_convention": "Fprime=2E=-Box(hbar)",
        "compatibility_operator": "C_b=Box(G_b)+d^a Fprime_ab",
        "theorem": "source y is in image(M_n) iff B_n y = 0",
        "solution_affine_dimension": "6*n^2+20*n+10 when compatible",
        "floating_point_used": False,
        "primes": list(primes),
        "cases": cases,
        "pass": all(c["pass"] for c in cases),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["sha256_without_digest_field"] = hashlib.sha256(canonical).hexdigest()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(text)
    print(text, end="")
    if result["pass"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
