#!/usr/bin/env python3
"""Iter057O exact unrestricted quartic c6^0 Einstein-seed completion."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

import qgr_iter057m_universal_q4_matrix as uq4

GATE = "ITER057O-QUARTIC-EINSTEIN-SEED-COMPLETION"
PREREG = "f4d06a6b97cb063bca8887731d7999d010863e93"
ITER057N = "32c6f1b077d72a616f52dc41bbef8a39ba0cf1af"
PAIRS = uq4.PAIRS
ETA = uq4.ETA
X = sp.symbols("t x y z")
t, x, y, z = X
k = sp.symbols("kappa", nonzero=True)
eta = sp.diag(-1, 1, 1, 1)

# Exact Iter057N G_ab^(2)/kappa^2 raw polynomial coefficients in (x,y,z).
G2 = {
    (0,0): {(2,0,0):3, (0,2,0):3, (0,0,2):12},
    (1,1): {(2,0,0):1, (0,2,0):-1, (0,0,2):-16},
    (1,2): {(1,1,0):2},
    (1,3): {(1,0,1):-4},
    (2,2): {(2,0,0):-1, (0,2,0):1, (0,0,2):-16},
    (2,3): {(0,1,1):-4},
    (3,3): {(2,0,0):-7, (0,2,0):-7, (0,0,2):4},
}


def mon(alpha):
    out = 1
    for u, n in zip(X, alpha):
        out *= u**n
    return out


def fact(alpha):
    out = 1
    for n in alpha:
        out *= sp.factorial(n)
    return out


def truncate(expr, degree):
    p = sp.Poly(sp.expand(expr), *X)
    return sp.expand(sum(c * mon(a) for a, c in p.terms() if sum(a) <= degree))


def target_rhs():
    a2 = uq4.alphas(2)
    rhs = [sp.Integer(0)] * 80
    for pair in PAIRS:
        raw = G2.get(pair, {})
        for alpha in a2:
            exp3 = (alpha[1], alpha[2], alpha[3])
            c = raw.get(exp3, 0)
            norm = sp.Integer(c) * sp.factorial(exp3[0]) * sp.factorial(exp3[1]) * sp.factorial(exp3[2])
            rhs.append(-norm)  # target DG[r4]/kappa^2 = -G2/kappa^2
    return sp.Matrix(rhs)


def solve_q4():
    M, meta, a4 = uq4.assemble()
    rhs = target_rhs()
    canonical, labels = uq4.canonical_bianchi_basis(meta)
    compatibility = [sp.factor((v.T * rhs)[0]) for v in canonical]
    rank_M = M.rank()
    rank_aug = M.row_join(rhs).rank()

    _, pivot_cols = M.rref()
    _, pivot_rows = M.T.rref()
    A = M.extract(list(pivot_rows), list(pivot_cols))
    rr = rhs.extract(list(pivot_rows), [0])
    sol = A.inv() * rr
    q4 = [sp.Integer(0)] * M.cols
    for j, v in zip(pivot_cols, sol):
        q4[j] = sp.factor(v)
    residual = M * sp.Matrix(q4) - rhs
    sparse = []
    for idx, value in enumerate(q4):
        if value == 0:
            continue
        p = idx // len(a4)
        alpha = a4[idx % len(a4)]
        sparse.append({"pair":list(PAIRS[p]), "alpha":list(alpha), "R4_over_kappa2":str(value)})
    return M, rhs, compatibility, rank_M, rank_aug, residual, sparse


def build_corrected_metric(sparse):
    q = k * (x*x + y*y - 2*z*z)
    g0 = sp.diag(-1-q, 1-q, 1-q, 1-q)
    rbar = sp.MutableDenseMatrix(4, 4, [0]*16)
    for item in sparse:
        a, b = item["pair"]
        alpha = tuple(item["alpha"])
        value = sp.Rational(item["R4_over_kappa2"])
        term = k**2 * value * mon(alpha) / fact(alpha)
        rbar[a,b] += term
        if a != b:
            rbar[b,a] += term
    tr = sum(eta[a,b] * rbar[a,b] for a,b in product(range(4), repeat=2))
    r = sp.MutableDenseMatrix(4, 4, [0]*16)
    for a,b in product(range(4), repeat=2):
        r[a,b] = sp.expand(rbar[a,b] - sp.Rational(1,2) * eta[a,b] * tr)
    return g0, rbar, r, sp.MutableDenseMatrix(g0 + r)


def full_metric_controls(sparse):
    g0, rbar, r, g = build_corrected_metric(sparse)
    origin = {u:0 for u in X}
    preserve = {
        "r_origin_zero": all(sp.simplify(r[a,b].subs(origin)) == 0 for a,b in product(range(4), repeat=2)),
        "dr_origin_zero": all(sp.simplify(sp.diff(r[a,b], X[c]).subs(origin)) == 0 for a,b,c in product(range(4), repeat=3)),
        "d2r_origin_zero": all(sp.simplify(sp.diff(r[a,b], X[c], X[d]).subs(origin)) == 0 for a,b,c,d in product(range(4), repeat=4)),
    }

    # Verify total linear de Donder gauge: G3 quadratic piece + quartic correction.
    h = g - eta
    trh = sum(eta[a,b] * h[a,b] for a,b in product(range(4), repeat=2))
    hbar = sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4), repeat=2):
        hbar[a,b] = sp.expand(h[a,b] - sp.Rational(1,2) * eta[a,b] * trh)
    gauge = []
    for b in range(4):
        v = sum(eta[a,c] * sp.diff(hbar[a,b], X[c]) for a,c in product(range(4), repeat=2))
        gauge.append(sp.factor(v))

    # Independent full-metric nonlinear check through coordinate degree two.
    # For Gamma through degree3, inverse metric is required only through degree2.
    h2 = g0 - eta
    gi2 = sp.MutableDenseMatrix(eta)
    for a,b in product(range(4), repeat=2):
        gi2[a,b] = truncate(eta[a,b] - sum(eta[a,c]*h2[c,d]*eta[d,b]
                                           for c,d in product(range(4), repeat=2)), 2)
    inverse_control = all(
        truncate(sum(g[a,c]*gi2[c,b] for c in range(4)) - (1 if a == b else 0), 2) == 0
        for a,b in product(range(4), repeat=2))

    Gamma = {}
    for a,b,c in product(range(4), repeat=3):
        v = 0
        for d in range(4):
            v += gi2[a,d] * (sp.diff(g[d,c], X[b]) + sp.diff(g[d,b], X[c]) - sp.diff(g[b,c], X[d])) / 2
        Gamma[a,b,c] = truncate(v, 3)

    Ric = sp.MutableDenseMatrix(4,4,[0]*16)
    for b,d in product(range(4), repeat=2):
        v = 0
        for a in range(4):
            v += sp.diff(Gamma[a,d,b], X[a]) - sp.diff(Gamma[a,a,b], X[d])
            for e in range(4):
                v += Gamma[a,a,e]*Gamma[e,d,b] - Gamma[a,d,e]*Gamma[e,a,b]
        Ric[b,d] = truncate(v, 2)
    scalar = truncate(sum(gi2[a,b]*Ric[a,b] for a,b in product(range(4), repeat=2)), 2)
    Ein = sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4), repeat=2):
        Ein[a,b] = truncate(Ric[a,b] - sp.Rational(1,2)*g[a,b]*scalar, 2)

    return {
        **preserve,
        "origin_metric_connection_curvature_preserved": all(preserve.values()),
        "combined_linear_deDonder_exact": all(v == 0 for v in gauge),
        "combined_linear_deDonder": [str(v) for v in gauge],
        "inverse_identity_through_degree2": inverse_control,
        "full_metric_Ricci_through_degree2_zero": all(sp.simplify(Ric[a,b]) == 0 for a,b in product(range(4), repeat=2)),
        "full_metric_scalar_through_degree2_zero": sp.simplify(scalar) == 0,
        "full_metric_Einstein_through_degree2_zero": all(sp.simplify(Ein[a,b]) == 0 for a,b in product(range(4), repeat=2)),
        "full_metric_Einstein_components": {f"{a}{b}":str(sp.factor(Ein[a,b])) for a,b in PAIRS},
    }


def compute():
    M, rhs, compatibility, rank_M, rank_aug, residual, sparse = solve_q4()
    metric = full_metric_controls(sparse)
    controls = {
        "rank_M_exact_164": rank_M == 164,
        "rank_augmented_equals_rank": rank_aug == rank_M,
        "all_16_Bianchi_compatibility_zero": len(compatibility) == 16 and all(v == 0 for v in compatibility),
        "exact_linear_system_residual_zero": all(v == 0 for v in residual),
        **{k:v for k,v in metric.items() if isinstance(v, bool)},
        "Weyl3_source_reset_lock_recorded": True,
    }
    passed = all(controls.values())
    return {
        "gate":GATE,
        "preregistration_commit":PREREG,
        "iter057n_target_commit":ITER057N,
        "matrix_shape":[M.rows,M.cols],
        "rank_M":rank_M,
        "rank_augmented":rank_aug,
        "nullity":M.cols-rank_M,
        "canonical_compatibility":[str(v) for v in compatibility],
        "particular_nonzero_count":len(sparse),
        "particular_R4_normalized":sparse,
        "metric_controls":metric,
        "controls":controls,
        "pass":passed,
        "classification":("PASS_SCOPED_ITER057O_QUARTIC_EINSTEIN_SEED_COMPLETES_G3_THROUGH_QUADRATIC_ORDER__WEYL3_SOURCE_MUST_BE_RECOMPUTED" if passed else "INVALID_OR_UNRESOLVED_ITER057O"),
        "exact_zero_uses_tolerance":False,
        "c6_status":"NOT_USED_ZERO_ORDER_SEED_COMPLETION",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out"); args=ap.parse_args()
    out=compute(); text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True: raise SystemExit(2)

if __name__ == "__main__": main()
