#!/usr/bin/env python3
"""Fast exact finite-Taylor G3/H0 Weyl3 source jet for Iter057M.

The G3 metric is exactly quadratic.  To expose E_W3 through coordinate degree two,
P=dI3/dR is needed only through degree four because the Euler tensor contains two
covariant derivatives of P.  This module therefore performs all tensor algebra in
an exact rational polynomial ring truncated at total spatial degree four, avoiding
the global rational factor/simplify cost that blocked Iter057K.

Until the dedicated source-component audit is consumed, this evaluator is a
controlled candidate implementation, not terminal scientific authority.
"""
import argparse
import json
import math
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

N = 4
MAX = 4
KAPPA = F(2, 25)
GATE = "ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION"
PREREG = "9760ca0324dce13cf141a9f93b6ff69ea4c75605"
AUDIT_PLAN = "f087b579e0c13714178bfc43e9a8e2f7fa907312"

# Polynomial dictionaries use spatial monomials (x,y,z); time derivatives vanish.
def const(c):
    c = F(c)
    return {} if c == 0 else {(0, 0, 0): c}


def mono(exp, c=1):
    c = F(c)
    return {} if c == 0 else {tuple(exp): c}


def add(a, b):
    out = dict(a)
    for m, c in b.items():
        v = out.get(m, F(0)) + c
        if v:
            out[m] = v
        elif m in out:
            del out[m]
    return out


def neg(a):
    return {m: -c for m, c in a.items()}


def sub(a, b):
    return add(a, neg(b))


def scale(a, c):
    c = F(c)
    return {} if c == 0 else {m: c * v for m, v in a.items() if c * v}


def mul(a, b, maxdeg=MAX):
    out = {}
    for m, c in a.items():
        for n, d in b.items():
            e = (m[0] + n[0], m[1] + n[1], m[2] + n[2])
            if sum(e) <= maxdeg:
                out[e] = out.get(e, F(0)) + c * d
    return {m: c for m, c in out.items() if c}


def deriv(a, coord):
    if coord == 0:
        return {}
    j = coord - 1
    out = {}
    for m, c in a.items():
        if m[j]:
            e = list(m)
            n = e[j]
            e[j] -= 1
            e = tuple(e)
            out[e] = out.get(e, F(0)) + c * n
    return out


def truncate(a, maxdeg):
    return {m: c for m, c in a.items() if sum(m) <= maxdeg and c}


def value0(a):
    return a.get((0, 0, 0), F(0))


def perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inv % 2 else 1


def fracstr(v):
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def normalized_coeff(raw, exp3):
    return raw * math.prod(math.factorial(n) for n in exp3)


def compute():
    k = KAPPA
    q = add(add(mono((2, 0, 0), k), mono((0, 2, 0), k)), mono((0, 0, 2), -2 * k))
    q2 = mul(q, q)

    # Frozen (-,+,+,+) G3 source metric and inverse through the required jet order.
    g = [sub(const(-1), q), sub(const(1), q), sub(const(1), q), sub(const(1), q)]
    gi = [add(add(const(-1), q), neg(q2)),
          add(add(const(1), q), q2),
          add(add(const(1), q), q2),
          add(add(const(1), q), q2)]

    # Christoffel through degree three.
    G = [[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a, b, c in product(range(N), repeat=3):
        t = {}
        if a == c:
            t = add(t, deriv(g[a], b))
        if a == b:
            t = add(t, deriv(g[a], c))
        if b == c:
            t = sub(t, deriv(g[b], a))
        G[a][b][c] = scale(mul(gi[a], t, 3), F(1, 2))

    # Riemann / Ricci / scalar.
    Rup = [[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a, b, c, d in product(range(N), repeat=4):
        e = sub(deriv(G[a][d][b], c), deriv(G[a][c][b], d))
        for r in range(N):
            e = add(e, sub(mul(G[a][c][r], G[r][d][b]), mul(G[a][d][r], G[r][c][b])))
        Rup[a][b][c][d] = e
    Rlow = [[[[mul(g[a], Rup[a][b][c][d]) for d in range(N)]
              for c in range(N)] for b in range(N)] for a in range(N)]
    Ric = [[{} for _ in range(N)] for _ in range(N)]
    for b, d in product(range(N), repeat=2):
        e = {}
        for a in range(N):
            e = add(e, Rup[a][b][a][d])
        Ric[b][d] = e
    Scal = {}
    for a in range(N):
        Scal = add(Scal, mul(gi[a], Ric[a][a]))

    # Weyl tensor, all lowered.
    C = [[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a, b, c, d in product(range(N), repeat=4):
        rp = {}
        if a == c:
            rp = add(rp, mul(g[a], Ric[d][b]))
        if a == d:
            rp = sub(rp, mul(g[a], Ric[c][b]))
        if b == c:
            rp = sub(rp, mul(g[b], Ric[d][a]))
        if b == d:
            rp = add(rp, mul(g[b], Ric[c][a]))
        rp = scale(rp, F(1, 2))
        gg = {}
        if a == c and d == b:
            gg = add(gg, mul(g[a], g[d]))
        if a == d and c == b:
            gg = sub(gg, mul(g[a], g[c]))
        C[a][b][c][d] = add(sub(Rlow[a][b][c][d], rp), scale(mul(Scal, gg), F(1, 6)))

    # Q_abcd = C_ab{}^{rs} C_rs cd, then algebraic-Riemann and Weyl projections.
    Q = [[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a, b, c, d in product(range(N), repeat=4):
        e = {}
        for r, s in product(range(N), repeat=2):
            e = add(e, mul(mul(mul(gi[r], gi[s]), C[a][b][r][s]), C[r][s][c][d]))
        Q[a][b][c][d] = e

    perms = list(permutations(range(4)))
    Qr = [[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a, b, c, d in product(range(N), repeat=4):
        inds = (a, b, c, d)
        alt = {}
        for p in perms:
            alt = add(alt, scale(Q[inds[p[0]]][inds[p[1]]][inds[p[2]]][inds[p[3]]], F(perm_sign(p), 24)))
        Qr[a][b][c][d] = sub(Q[a][b][c][d], alt)

    # I3 = Q^{abef} C_efab in the diagonal metric presentation.
    I3 = {}
    for a, b, e, f in product(range(N), repeat=4):
        term = Q[a][b][e][f]
        for idx in (a, b, e, f):
            term = mul(term, gi[idx])
        I3 = add(I3, mul(term, C[e][f][a][b]))

    QRic = [[{} for _ in range(N)] for _ in range(N)]
    for b, d in product(range(N), repeat=2):
        e = {}
        for a in range(N):
            e = add(e, mul(gi[a], Qr[a][b][a][d]))
        QRic[b][d] = e
    QSc = {}
    for b in range(N):
        QSc = add(QSc, mul(gi[b], QRic[b][b]))

    Plow = [[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a, b, c, d in product(range(N), repeat=4):
        t = {}
        if a == c:
            t = add(t, mul(g[a], QRic[d][b]))
        if a == d:
            t = sub(t, mul(g[a], QRic[c][b]))
        if b == c:
            t = sub(t, mul(g[b], QRic[d][a]))
        if b == d:
            t = add(t, mul(g[b], QRic[c][a]))
        t = scale(t, F(1, 2))
        gg = {}
        if a == c and d == b:
            gg = add(gg, mul(g[a], g[d]))
        if a == d and c == b:
            gg = sub(gg, mul(g[a], g[c]))
        gg = scale(gg, F(1, 2))
        Plow[a][b][c][d] = scale(add(sub(Qr[a][b][c][d], t), scale(mul(QSc, gg), F(1, 3))), 3)

    P = [[[[mul(mul(mul(mul(gi[a], gi[b]), gi[c]), gi[d]), Plow[a][b][c][d])
            for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]

    PR = {}
    for a, b, c, d in product(range(N), repeat=4):
        PR = add(PR, mul(P[a][b][c][d], Rlow[a][b][c][d]))

    # First and second covariant divergences of contravariant P.
    FD = [[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m, b, n in product(range(N), repeat=3):
        val = {}
        for a in range(N):
            term = deriv(P[a][m][b][n], a)
            for r in range(N):
                term = add(term, mul(G[a][a][r], P[r][m][b][n], 3))
                term = add(term, mul(G[m][a][r], P[a][r][b][n], 3))
                term = add(term, mul(G[b][a][r], P[a][m][r][n], 3))
                term = add(term, mul(G[n][a][r], P[a][m][b][r], 3))
            val = add(val, term)
        FD[m][b][n] = truncate(val, 3)

    D = [[{} for _ in range(N)] for _ in range(N)]
    for m, n in product(range(N), repeat=2):
        val = {}
        for b in range(N):
            term = deriv(FD[m][b][n], b)
            for r in range(N):
                term = add(term, mul(G[m][b][r], FD[r][b][n], 2))
                term = add(term, mul(G[b][b][r], FD[m][r][n], 2))
                term = add(term, mul(G[n][b][r], FD[m][b][r], 2))
            val = add(val, term)
        D[m][n] = truncate(val, 2)

    # Algebraic insertion B^{ab}=P^{(a|cde|}R^{b)}_cde.
    def bone(a, b):
        val = {}
        for c, d, e in product(range(N), repeat=3):
            val = add(val, mul(mul(P[a][c][d][e], gi[b], 2), Rlow[b][c][d][e], 2))
        return val

    B = [[{} for _ in range(N)] for _ in range(N)]
    for a, b in product(range(N), repeat=2):
        B[a][b] = scale(add(bone(a, b), bone(b, a)), F(1, 2))

    # Iter056X covariant Euler tensor E^{ab}=1/2 g^{ab}I3-B^{ab}-2D^{ab}.
    Eup = [[{} for _ in range(N)] for _ in range(N)]
    for a, b in product(range(N), repeat=2):
        e = add(neg(B[a][b]), scale(D[a][b], -2))
        if a == b:
            e = add(e, scale(mul(gi[a], I3, 2), F(1, 2)))
        Eup[a][b] = truncate(e, 2)
    Edown = [[mul(mul(g[a], g[b], 2), Eup[a][b], 2) for b in range(N)] for a in range(N)]

    trace = {}
    for a in range(N):
        trace = add(trace, mul(gi[a], Edown[a][a], 2))
    trace_ward = truncate(add(trace, truncate(I3, 2)), 2)

    # Exact Noether divergence through the coefficient order required by Iter057M compatibility.
    noether = []
    for b in range(N):
        v = {}
        for a in range(N):
            v = add(v, deriv(Eup[a][b], a))
            for r in range(N):
                v = add(v, mul(G[a][a][r], Eup[r][b], 1))
                v = add(v, mul(G[b][a][r], Eup[a][r], 1))
        noether.append(truncate(v, 1))

    e_sym = all(truncate(sub(Edown[a][b], Edown[b][a]), 2) == {} for a in range(N) for b in range(N))
    pr_control = value0(sub(PR, scale(I3, 3))) == 0
    controls = {
        "P_dot_R_equals_3I3_at_origin": pr_control,
        "trace_Ward_through_degree2": trace_ward == {},
        "Noether_divergence_through_degree1": all(v == {} for v in noether),
        "E_W3_down_symmetric_through_degree2": e_sym,
    }

    # Shat=A_E*S=-E_down.  Export normalized source coefficients and dimensionless kappa factors.
    source = {}
    pairs = [(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
    for a, b in pairs:
        s = neg(Edown[a][b])
        rec = {"order0": None, "order2": []}
        s0 = value0(s)
        if s0:
            rec["order0"] = {
                "value": fracstr(s0),
                "over_kappa3": fracstr(s0 / (k ** 3)),
            }
        for exp3, raw in sorted(s.items()):
            if sum(exp3) != 2:
                continue
            norm = normalized_coeff(raw, exp3)
            rec["order2"].append({
                "alpha": [0, exp3[0], exp3[1], exp3[2]],
                "value": fracstr(norm),
                "over_kappa4": fracstr(norm / (k ** 4)),
            })
        source[f"{a}{b}"] = rec

    out = {
        "gate": GATE,
        "preregistration_commit": PREREG,
        "component_audit_plan_commit": AUDIT_PLAN,
        "status": "CONTROLLED_CANDIDATE_PENDING_AUTHORIZED_COMPONENT_AUDIT",
        "kappa": fracstr(k),
        "I3_origin": fracstr(value0(I3)),
        "I3_origin_over_kappa3": fracstr(value0(I3) / (k ** 3)),
        "B_up_diagonal_origin_over_kappa3": [fracstr(value0(B[i][i]) / (k ** 3)) for i in range(N)],
        "D_up_diagonal_origin_over_kappa3": [fracstr(value0(D[i][i]) / (k ** 3)) for i in range(N)],
        "E_down_diagonal_origin_over_kappa3": [fracstr(value0(Edown[i][i]) / (k ** 3)) for i in range(N)],
        "controls": controls,
        "source_Shat_normalized": source,
        "exact_zero_uses_tolerance": False,
        "c6_status": "SYMBOLIC_UNFIXED_FACTORED_OUT",
    }
    out["pass_controls"] = all(controls.values())
    return out


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
    if out["pass_controls"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
