#!/usr/bin/env python3
"""Exact unrestricted Iter057M Q4 constructor for a supplied controlled G3 source jet.

Consumes the exact normalized source jet from qgr_iter057m_exact_g3_weyl3_source_jet,
assembles the frozen cubic-gauge/quadratic-field affine system, checks all canonical
Bianchi/Noether compatibility functionals, and returns one exact particular Q4 with
all nonpivot homogeneous directions set to zero.
"""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

import qgr_iter057m_exact_g3_weyl3_source_jet as source_jet
import qgr_iter057m_universal_q4_matrix as uq4

GATE = "ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION"
PREREG = "9760ca0324dce13cf141a9f93b6ff69ea4c75605"
PAIRS = uq4.PAIRS
ETA = uq4.ETA
X = sp.symbols("t x y z")
t, x, y, z = X
KAPPA = sp.Rational(2, 25)


def alphas(n):
    return uq4.alphas(n)


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


def homogeneous(expr, degree):
    p = sp.Poly(sp.expand(expr), *X)
    return sp.expand(sum(c * mon(a) for a, c in p.terms() if sum(a) == degree))


def normalized_coeff(expr, alpha):
    p = sp.Poly(sp.expand(expr), *X)
    return sp.expand(p.coeff_monomial(mon(alpha)) * fact(alpha))


def pair_index(a, b):
    return uq4.pair_index(a, b)


def parse_source():
    obj = source_jet.compute()
    a2 = alphas(2)
    S0 = [sp.Integer(0)] * 10
    S2 = [[sp.Integer(0)] * len(a2) for _ in range(10)]
    for p, (a, b) in enumerate(PAIRS):
        rec = obj["source_Shat_normalized"][f"{a}{b}"]
        if rec["order0"] is not None:
            S0[p] = sp.Rational(rec["order0"]["value"])
        for item in rec["order2"]:
            alpha = tuple(item["alpha"])
            S2[p][a2.index(alpha)] = sp.Rational(item["value"])
    return obj, S0, S2


def background_jets():
    q = KAPPA * (x*x + y*y - 2*z*z)
    eta = sp.diag(-1, 1, 1, 1)
    g = sp.diag(-1-q, 1-q, 1-q, 1-q)
    gi2 = sp.diag(-1+q, 1+q, 1+q, 1+q)
    Gamma = {}
    for a, b, c in product(range(4), repeat=3):
        val = 0
        for d in range(4):
            val += eta[a, d] * (sp.diff(g[d, c], X[b]) + sp.diff(g[d, b], X[c])
                                - sp.diff(g[b, c], X[d])) / 2
        Gamma[a, b, c] = sp.expand(val)

    origin = {u: 0 for u in X}
    Rlow0 = {}
    for A, b, c, d in product(range(4), repeat=4):
        val = 0
        for e in range(4):
            rup = sp.diff(Gamma[e, d, b], X[c]) - sp.diff(Gamma[e, c, b], X[d])
            val += eta[A, e] * rup
        Rlow0[A, b, c, d] = sp.simplify(val.subs(origin))
    return eta, g, gi2, Gamma, Rlow0


def q2_from_source(S0):
    eta = sp.diag(-1, 1, 1, 1)
    def s0(a, b):
        return S0[pair_index(a, b)]
    Strace = sum(ETA[a] * s0(a, a) for a in range(4))
    Q2 = {}
    for a, b, c, d in product(range(4), repeat=4):
        val = -sp.Rational(5, 9) * eta[c, d] * s0(a, b)
        val += sp.Rational(1, 18) * (
            eta[a, c] * s0(b, d) + eta[a, d] * s0(b, c)
            + eta[b, c] * s0(a, d) + eta[b, d] * s0(a, c))
        val += sp.Rational(2, 9) * eta[a, b] * s0(c, d)
        val -= sp.Rational(1, 18) * eta[a, b] * eta[c, d] * Strace
        Q2[a, b, c, d] = sp.factor(val)
    return Q2


def assemble_affine_rhs(S0, S2, Q2):
    a2, a3 = alphas(2), alphas(3)
    eta, g, gi2, Gamma, Rlow0 = background_jets()
    def s0(a, b):
        return S0[pair_index(a, b)]
    def s2(a, b, alpha):
        return S2[pair_index(a, b)][a2.index(alpha)]

    qbar2 = {}
    for a, b in product(range(4), repeat=2):
        qbar2[a, b] = sp.expand(sum(sp.Rational(1, 2) * Q2[a, b, c, d] * X[c] * X[d]
                                    for c, d in product(range(4), repeat=2)))

    Gbg = {}
    for b in range(4):
        val = 0
        for a, c in product(range(4), repeat=2):
            val += gi2[a, c] * sp.diff(qbar2[a, b], X[c])
            for r in range(4):
                val -= eta[a, c] * (Gamma[r, c, a] * qbar2[r, b]
                                     + Gamma[r, c, b] * qbar2[a, r])
        if sp.simplify(homogeneous(val, 1)) != 0:
            raise RuntimeError("Iter057L Q2 failed degree-one de Donder control")
        Gbg[b] = homogeneous(val, 3)

    first = {}
    for n, a, b in product(range(4), repeat=3):
        val = sp.diff(qbar2[a, b], X[n])
        for r in range(4):
            val -= Gamma[r, n, a] * qbar2[r, b] + Gamma[r, n, b] * qbar2[a, r]
        first[n, a, b] = sp.expand(val)

    second = {}
    for m, n, a, b in product(range(4), repeat=4):
        val = sp.diff(first[n, a, b], X[m])
        for r in range(4):
            val -= Gamma[r, m, n] * first[r, a, b]
            val -= Gamma[r, m, a] * first[n, r, b]
            val -= Gamma[r, m, b] * first[n, a, r]
        second[m, n, a, b] = sp.expand(val)

    DGbg = {}
    for a, b in product(range(4), repeat=2):
        box = sum(gi2[m, n] * second[m, n, a, b]
                  for m, n in product(range(4), repeat=2))
        curv = 0
        for c, d in product(range(4), repeat=2):
            q_up = ETA[c] * ETA[d] * qbar2[c, d]
            curv += 2 * Rlow0[a, c, b, d] * q_up
        full = sp.expand(-sp.Rational(1, 2) * (box + curv))
        if sp.simplify(homogeneous(full, 0) - s0(a, b)) != 0:
            raise RuntimeError("Iter057L Q2 failed degree-zero field control")
        DGbg[a, b] = homogeneous(full, 2)

    rhs = []
    for b in range(4):
        for alpha in a3:
            rhs.append(-normalized_coeff(Gbg[b], alpha))
    for p, (a, b) in enumerate(PAIRS):
        for alpha in a2:
            rhs.append(s2(a, b, alpha) - normalized_coeff(DGbg[a, b], alpha))
    return sp.Matrix(rhs), qbar2


def construct():
    source_obj, S0, S2 = parse_source()
    Q2 = q2_from_source(S0)
    rhs, qbar2 = assemble_affine_rhs(S0, S2, Q2)
    M, meta, a4 = uq4.assemble()
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
    for j, value in zip(pivot_cols, sol):
        q4[j] = sp.factor(value)
    qv = sp.Matrix(q4)
    residual = M * qv - rhs
    residual_zero = all(sp.simplify(v) == 0 for v in residual)

    sparse = []
    for idx, value in enumerate(q4):
        if value == 0:
            continue
        p = idx // len(a4)
        alpha = a4[idx % len(a4)]
        sparse.append({
            "pair": list(PAIRS[p]),
            "alpha": list(alpha),
            "value": str(value),
            "over_kappa4": str(sp.factor(value / KAPPA**4)),
        })

    out = {
        "gate": GATE,
        "preregistration_commit": PREREG,
        "source_evaluator_status": source_obj["status"],
        "source_controls_pass": source_obj["pass_controls"],
        "matrix_shape": [M.rows, M.cols],
        "rank_M": rank_M,
        "rank_augmented": rank_aug,
        "nullity": M.cols-rank_M,
        "canonical_compatibility": [str(v) for v in compatibility],
        "all_16_compatibility_zero": all(v == 0 for v in compatibility),
        "particular_solution_residual_zero": residual_zero,
        "particular_nonzero_count": len(sparse),
        "particular_Q4_normalized": sparse,
        "exact_zero_uses_tolerance": False,
    }
    passed = (source_obj["pass_controls"] and rank_M == 164 and rank_aug == 164
              and out["all_16_compatibility_zero"] and residual_zero)
    out["pass_constructor_controls"] = bool(passed)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    args = ap.parse_args()
    out = construct()
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text)
    print(text, end="")
    if out["pass_constructor_controls"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
