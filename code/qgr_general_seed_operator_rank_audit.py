#!/usr/bin/env python3
"""Exact structural audit for the homogeneous Einstein-seed principal operator.

For every homogeneous metric correction degree n >= 2 in four variables, the
frozen QGR operator contains:
  * 4*C(n+2,3) de Donder rows of degree n-1;
  * 10*C(n+1,3) trace-reversed Einstein rows of degree n-2;
  * 10*C(n+3,3) symmetric-tensor unknowns of degree n.

The accompanying algebraic proof shows that the complete left kernel is the
canonical Bianchi family of dimension 4*C(n,3).  This script independently
checks the resulting rank formula over a finite field.  Because the matrix is
integral after multiplying field rows by two, a nonzero minor modulo an odd
prime is an exact lower-bound certificate over QQ; the Bianchi theorem supplies
the matching upper bound.  No floating-point arithmetic or tolerance is used.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from math import comb
from pathlib import Path

import sympy as sp
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix

ETA = (-1, 1, 1, 1)
PAIRS = tuple((a, b) for a in range(4) for b in range(a, 4))


def alphas(n: int):
    return tuple(sorted(a for a in product(range(n + 1), repeat=4) if sum(a) == n))


def pair_index(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    return PAIRS.index((a, b))


def dimensions(n: int) -> dict[str, int]:
    if n < 2:
        raise ValueError("n must be >= 2")
    unknowns = 10 * comb(n + 3, 3)
    gauge_rows = 4 * comb(n + 2, 3)
    field_rows = 10 * comb(n + 1, 3)
    rows = gauge_rows + field_rows
    bianchi = 4 * comb(n, 3) if n >= 3 else 0
    rank = rows - bianchi
    nullity = unknowns - rank
    return {
        "n": n,
        "unknowns": unknowns,
        "gauge_rows": gauge_rows,
        "field_rows": field_rows,
        "rows": rows,
        "matrix_nnz": 4 * rows,
        "left_nullity_bianchi": bianchi,
        "rank_formula": rank,
        "rank_closed_form": n * (5 * n * n + 12 * n - 5) // 3,
        "nullity": nullity,
        "nullity_closed_form": 6 * n * n + 20 * n + 10,
    }


def build_integral_matrix(n: int) -> sp.MutableSparseMatrix:
    """Build the frozen matrix with all field rows multiplied by 2.

    Row scaling preserves rank and converts every nonzero entry to +/-1.
    """
    a_n = alphas(n)
    a_nm1 = alphas(n - 1)
    a_nm2 = alphas(n - 2)
    col = {(p, alpha): p * len(a_n) + j for p in range(10) for j, alpha in enumerate(a_n)}
    rows: list[dict[int, int]] = []

    # de Donder: d^a hbar_ab
    for b in range(4):
        for alpha in a_nm1:
            row: dict[int, int] = {}
            for a in range(4):
                beta = list(alpha)
                beta[a] += 1
                j = col[(pair_index(a, b), tuple(beta))]
                row[j] = row.get(j, 0) + ETA[a]
            rows.append(row)

    # trace-reversed Einstein principal row: -1/2 Box hbar_ab.
    # Multiply the complete row by two.
    for p, _pair in enumerate(PAIRS):
        for alpha in a_nm2:
            row = {}
            for m in range(4):
                beta = list(alpha)
                beta[m] += 2
                j = col[(p, tuple(beta))]
                row[j] = row.get(j, 0) - ETA[m]
            rows.append(row)

    entries = {(i, j): v for i, row in enumerate(rows) for j, v in row.items() if v}
    return sp.MutableSparseMatrix(len(rows), 10 * len(a_n), entries)


def audit_degree(n: int, prime: int) -> dict:
    d = dimensions(n)
    M = build_integral_matrix(n)
    rank_mod_p = DomainMatrix.from_Matrix(M).convert_to(GF(prime)).rank()
    controls = {
        "shape_matches_formula": [M.rows, M.cols] == [d["rows"], d["unknowns"]],
        "nnz_matches_four_per_row": len(M.todok()) == d["matrix_nnz"],
        "closed_rank_formula_agrees": d["rank_formula"] == d["rank_closed_form"],
        "closed_nullity_formula_agrees": d["nullity"] == d["nullity_closed_form"],
        "modular_rank_hits_bianchi_upper_bound": rank_mod_p == d["rank_formula"],
    }
    return {
        **d,
        "prime": prime,
        "rank_mod_prime": rank_mod_p,
        "controls": controls,
        "pass": all(controls.values()),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-n", type=int, default=2)
    ap.add_argument("--max-n", type=int, default=12)
    ap.add_argument("--prime", type=int, default=1000003)
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.min_n < 2 or args.max_n < args.min_n:
        raise SystemExit("invalid degree range")
    if args.prime == 2:
        raise SystemExit("prime must be odd because field rows were scaled by 2")

    cases = [audit_degree(n, args.prime) for n in range(args.min_n, args.max_n + 1)]
    result = {
        "gate": "GENERAL-HOMOGENEOUS-EINSTEIN-SEED-OPERATOR-RANK-LAW",
        "scope": "FOUR_VARIABLE_FROZEN_TRACE_REVERSED_PRINCIPAL_OPERATOR_ONLY",
        "theorem": {
            "unknowns": "10*C(n+3,3)",
            "rows": "4*C(n+2,3) + 10*C(n+1,3)",
            "left_nullity": "4*C(n,3)",
            "rank": "n*(5*n^2 + 12*n - 5)/3",
            "nullity": "6*n^2 + 20*n + 10",
            "matrix_nnz": "4*rows",
        },
        "proof_status": "ALGEBRAIC_LEFT_KERNEL_COMPLETENESS_PROVED_SEPARATELY__MODULAR_IMPLEMENTATION_AUDIT",
        "exact_zero_uses_tolerance": False,
        "cases": cases,
        "pass": all(c["pass"] for c in cases),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(text)
    print(text, end="")
    if result["pass"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
