#!/usr/bin/env python3
"""Independent unreduced covariant control for the Iter057M exact Q4 candidate.

The Q4 is obtained from qgr_iter057m_q4_exact_constructor, but the field equation is
re-evaluated here from the unreduced linearized Ricci/Einstein variation rather than
the reduced de Donder operator used to construct the affine system.
"""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

import qgr_iter057m_q4_exact_constructor as ctor

GATE = ctor.GATE
X = ctor.X
t, x, y, z = X
ETA = ctor.ETA
PAIRS = ctor.PAIRS
KAPPA = ctor.KAPPA


def mon(alpha):
    return ctor.mon(alpha)


def fact(alpha):
    return ctor.fact(alpha)


def truncate(expr, degree):
    p = sp.Poly(sp.expand(expr), *X)
    return sp.expand(sum(c * mon(a) for a, c in p.terms() if sum(a) <= degree))


def check():
    built = ctor.construct()
    source_obj, S0, S2 = ctor.parse_source()
    a2, a4 = ctor.alphas(2), ctor.alphas(4)
    Q2 = ctor.q2_from_source(S0)
    eta, g, gi2, Gamma, Rlow0 = ctor.background_jets()

    q4map = {}
    for item in built["particular_Q4_normalized"]:
        pair = tuple(item["pair"])
        p = PAIRS.index(pair)
        q4map[p, tuple(item["alpha"])] = sp.Rational(item["value"])

    def pindex(a, b):
        return ctor.pair_index(a, b)

    def s0(a, b):
        return S0[pindex(a, b)]

    def s2(a, b, alpha):
        return S2[pindex(a, b)][a2.index(alpha)]

    qbar = {}
    for a, b in product(range(4), repeat=2):
        p = pindex(a, b)
        expr = sum(sp.Rational(1, 2) * Q2[a, b, c, d] * X[c] * X[d]
                   for c, d in product(range(4), repeat=2))
        for alpha in a4:
            value = q4map.get((p, alpha), 0)
            if value:
                expr += value * mon(alpha) / fact(alpha)
        qbar[a, b] = truncate(expr, 4)

    # Direct de Donder vector through cubic order.
    gauge = {}
    for b in range(4):
        val = 0
        for a, c in product(range(4), repeat=2):
            cov = sp.diff(qbar[a, b], X[c])
            for r in range(4):
                cov -= Gamma[r, c, a] * qbar[r, b] + Gamma[r, c, b] * qbar[a, r]
            val += gi2[a, c] * cov
        gauge[b] = truncate(val, 3)

    # In four dimensions trace reversal is involutive:
    # h_ab = qbar_ab - 1/2 g_ab qbar, with the background trace.
    qbar_trace = truncate(sum(gi2[a, b] * qbar[a, b]
                              for a, b in product(range(4), repeat=2)), 4)
    h = {}
    for a, b in product(range(4), repeat=2):
        h[a, b] = truncate(qbar[a, b] - sp.Rational(1, 2) * g[a, b] * qbar_trace, 4)
    htrace = truncate(sum(gi2[a, b] * h[a, b]
                          for a, b in product(range(4), repeat=2)), 4)

    # First covariant derivative of h_bc: T_{a b c}=nabla_a h_bc.
    first = {}
    for a, b, c in product(range(4), repeat=3):
        val = sp.diff(h[b, c], X[a])
        for r in range(4):
            val -= Gamma[r, a, b] * h[r, c] + Gamma[r, a, c] * h[b, r]
        first[a, b, c] = truncate(val, 3)

    # Second derivative: second[d,a,b,c]=nabla_d nabla_a h_bc.
    second = {}
    for d, a, b, c in product(range(4), repeat=4):
        val = sp.diff(first[a, b, c], X[d])
        for r in range(4):
            val -= Gamma[r, d, a] * first[r, b, c]
            val -= Gamma[r, d, b] * first[a, r, c]
            val -= Gamma[r, d, c] * first[a, b, r]
        second[d, a, b, c] = truncate(val, 2)

    hess_trace = {}
    for a, b in product(range(4), repeat=2):
        val = sp.diff(sp.diff(htrace, X[a]), X[b])
        for r in range(4):
            val -= Gamma[r, a, b] * sp.diff(htrace, X[r])
        hess_trace[a, b] = truncate(val, 2)

    # Unreduced covariant delta R_ab. Background-Ricci*h terms enter only at
    # degree four for the G3 jet and therefore cannot affect this degree-two control.
    delta_R = {}
    for a, b in product(range(4), repeat=2):
        term1 = sum(gi2[c, d] * second[d, a, b, c]
                    for c, d in product(range(4), repeat=2))
        term2 = sum(gi2[c, d] * second[d, b, a, c]
                    for c, d in product(range(4), repeat=2))
        box = sum(gi2[c, d] * second[c, d, a, b]
                  for c, d in product(range(4), repeat=2))
        delta_R[a, b] = truncate(sp.Rational(1, 2) *
                                 (term1 + term2 - box - hess_trace[a, b]), 2)

    delta_scalar = truncate(sum(gi2[a, b] * delta_R[a, b]
                                for a, b in product(range(4), repeat=2)), 2)
    delta_G = {}
    for a, b in product(range(4), repeat=2):
        delta_G[a, b] = truncate(delta_R[a, b]
                                 - sp.Rational(1, 2) * g[a, b] * delta_scalar, 2)

    residuals = {}
    for a, b in PAIRS:
        source = s0(a, b) + sum(s2(a, b, alpha) * mon(alpha) / fact(alpha)
                                for alpha in a2)
        residuals[f"{a}{b}"] = sp.simplify(truncate(delta_G[a, b] - source, 2))

    gauge_zero = all(sp.simplify(v) == 0 for v in gauge.values())
    field_zero = all(v == 0 for v in residuals.values())
    out = {
        "gate": GATE,
        "constructor_controls_pass": built["pass_constructor_controls"],
        "source_evaluator_status": source_obj["status"],
        "gauge_through_degree3": {str(b): str(sp.factor(gauge[b])) for b in range(4)},
        "unreduced_DG_minus_S_through_degree2": {k: str(v) for k, v in residuals.items()},
        "gauge_all_zero_exact": gauge_zero,
        "unreduced_field_all_zero_exact": field_zero,
        "pass_unreduced_controls": bool(built["pass_constructor_controls"] and gauge_zero and field_zero),
        "exact_zero_uses_tolerance": False,
    }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    args = ap.parse_args()
    out = check()
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text)
    print(text, end="")
    if out["pass_unreduced_controls"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
