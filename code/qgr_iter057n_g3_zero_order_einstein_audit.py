#!/usr/bin/env python3
"""Iter057N exact G3/H0 zeroth-order Einstein-seed neighborhood audit."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

GATE = "ITER057N-G3-ZERO-ORDER-EINSTEIN-SEED-NEIGHBORHOOD-AUDIT"
PREREG = "ebaead95ba38dc4521b57477c54bf7d4f1b11c83"
N = 4
t, x, y, z = sp.symbols("t x y z")
k = sp.symbols("kappa", nonzero=True)
COORDS = (t, x, y, z)
SPATIAL = (x, y, z)
ORIGIN = {t: 0, x: 0, y: 0, z: 0}
PAIRS = [(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]


def spatial_truncate(expr, degree):
    lam = sp.symbols("lam")
    scaled = sp.expand(expr.subs({x:lam*x, y:lam*y, z:lam*z}))
    return sp.factor(sp.series(scaled, lam, 0, degree+1).removeO().subs(lam, 1))


def build_geometry():
    q = k * (x*x + y*y - 2*z*z)  # q=2 Phi
    g = sp.diag(-1-q, 1-q, 1-q, 1-q)
    gi = sp.simplify(g.inv())

    Gamma = [[ [sp.Integer(0) for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N), repeat=3):
        Gamma[a][b][c] = sp.factor(sp.Rational(1,2) * sum(
            gi[a,d] * (sp.diff(g[d,c], COORDS[b]) + sp.diff(g[d,b], COORDS[c])
                       - sp.diff(g[b,c], COORDS[d]))
            for d in range(N)))

    Rup = [[[[sp.Integer(0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N), repeat=4):
        val = sp.diff(Gamma[a][d][b], COORDS[c]) - sp.diff(Gamma[a][c][b], COORDS[d])
        for e in range(N):
            val += Gamma[a][c][e]*Gamma[e][d][b] - Gamma[a][d][e]*Gamma[e][c][b]
        Rup[a][b][c][d] = sp.factor(val)

    Ric = sp.MutableDenseMatrix(N, N, [0]*(N*N))
    for b,d in product(range(N), repeat=2):
        Ric[b,d] = sp.factor(sum(Rup[a][b][a][d] for a in range(N)))

    R = sp.factor(sum(gi[a,b]*Ric[a,b] for a,b in product(range(N), repeat=2)))
    Ein = sp.MutableDenseMatrix(N, N, [0]*(N*N))
    for a,b in product(range(N), repeat=2):
        Ein[a,b] = sp.factor(Ric[a,b] - sp.Rational(1,2)*g[a,b]*R)
    return q, g, gi, Gamma, Ric, R, Ein


def normalized_hessian(expr, i, j):
    return sp.factor(sp.diff(expr, COORDS[i], COORDS[j]).subs(ORIGIN) / k**2)


def compute():
    q, g, gi, Gamma, Ric, R, Ein = build_geometry()

    origin_controls = {
        "Ricci_origin_zero": all(sp.simplify(Ric[a,b].subs(ORIGIN)) == 0 for a,b in product(range(N), repeat=2)),
        "scalar_origin_zero": sp.simplify(R.subs(ORIGIN)) == 0,
        "Einstein_origin_zero": all(sp.simplify(Ein[a,b].subs(ORIGIN)) == 0 for a,b in product(range(N), repeat=2)),
    }

    ric2 = {f"{a}{b}": str(spatial_truncate(Ric[a,b], 2)) for a,b in PAIRS
            if spatial_truncate(Ric[a,b], 2) != 0}
    ein2 = {f"{a}{b}": str(spatial_truncate(Ein[a,b], 2)) for a,b in PAIRS
            if spatial_truncate(Ein[a,b], 2) != 0}
    r2 = spatial_truncate(R, 2)

    coeffs = []
    for a,b in PAIRS:
        for i in (1,2,3):
            for j in range(i,4):
                v = normalized_hessian(Ein[a,b], i, j)
                if v != 0:
                    coeffs.append({"pair":[a,b], "derivatives":[i,j], "over_kappa2":str(v)})

    # Contracted Bianchi identity through the first order implied by G=O(x^2).
    div = []
    for b in range(N):
        val = 0
        for a,c in product(range(N), repeat=2):
            cov = sp.diff(Ein[a,b], COORDS[c])
            for r in range(N):
                cov -= Gamma[r][c][a]*Ein[r,b] + Gamma[r][c][b]*Ein[a,r]
            val += gi[a,c]*cov
        div.append(sp.factor(spatial_truncate(val, 1)))

    trace_ein = sp.factor(sum(gi[a,b]*Ein[a,b] for a,b in product(range(N), repeat=2)))
    trace_control = sp.simplify(trace_ein + R) == 0

    # Full rational exact cross-check: not a Taylor expression.
    full_g00 = sp.factor(Ein[0,0])
    expected_full_g00 = sp.factor(-3*k**2*(x*x+y*y+4*z*z)*(q+1)/(q-1)**3)
    full_control = sp.simplify(full_g00 - expected_full_g00) == 0

    controls = {
        **origin_controls,
        "contracted_Bianchi_through_degree1": all(v == 0 for v in div),
        "Einstein_trace_equals_minus_scalar_exact": trace_control,
        "full_rational_G00_factorization_exact": full_control,
    }
    nonzero = len(coeffs) > 0
    classification = (
        "SCIENTIFIC_FAIL_SCOPED_ITER057N_FIXED_G3_SEED_HAS_NONZERO_C6_ZERO_ORDER_EINSTEIN_RESIDUAL__SEED_CORRECTION_REQUIRED_BEFORE_OPEN_NEIGHBORHOOD_C6_SERIES"
        if all(controls.values()) and nonzero else
        "INVALID_OR_UNRESOLVED_ITER057N"
    )
    return {
        "gate": GATE,
        "preregistration_commit": PREREG,
        "signature": "(-,+,+,+)",
        "controls": controls,
        "all_controls_pass": all(controls.values()),
        "Ricci_degree2": ric2,
        "scalar_degree2": str(r2),
        "Einstein_degree2": ein2,
        "Einstein_normalized_second_derivatives": coeffs,
        "nonzero_quadratic_Einstein_coefficient_count": len(coeffs),
        "full_rational_G00": str(full_g00),
        "contracted_Bianchi_degree1": [str(v) for v in div],
        "classification": classification,
        "pass": all(controls.values()) and nonzero,
        "exact_zero_uses_tolerance": False,
        "c6_status": "SYMBOLIC_UNFIXED_NOT_USED_IN_ZERO_ORDER_GATE",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    args = ap.parse_args()
    out = compute()
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text)
    print(text, end="")
    if out["pass"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
