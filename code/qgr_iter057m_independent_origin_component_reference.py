#!/usr/bin/env python3
"""Independent symbolic origin-component reference for Iter057M source-jet audit.

This deliberately does not import the fast Fraction polynomial evaluator or the
historical Iter057K raw-gradient implementation.  It realizes the analytic
Iter056X formula P=3 Pi_W Pi_R[C^2] with ordinary SymPy tensor expressions and
symbolic kappa, sufficient to determine the exact origin double divergence.
"""
import argparse
import json
from itertools import permutations, product
from pathlib import Path

import sympy as sp

GATE = "ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION"
PREREG = "253fc53238ac58bbe4395e154e188e3d865217c2"
N = 4
x, y, z = sp.symbols("x y z")
k = sp.symbols("kappa", nonzero=True)
VARS = (x, y, z)
COORD = (None, x, y, z)
ORIGIN = {x: 0, y: 0, z: 0}
ETA = (-1, 1, 1, 1)


def diff(expr, i):
    return 0 if i == 0 else sp.diff(expr, COORD[i])


def trunc(expr, degree=2):
    p = sp.Poly(sp.expand(expr), *VARS)
    return sp.expand(sum(c * x**a[0] * y**a[1] * z**a[2]
                         for a, c in p.terms() if sum(a) <= degree))


def trunc3(expr):
    p = sp.Poly(sp.expand(expr), *VARS)
    return sp.expand(sum(c * x**a[0] * y**a[1] * z**a[2]
                         for a, c in p.terms() if sum(a) <= 3))


def psign(p):
    inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inv % 2 else 1


def compute():
    q = k * (x*x + y*y - 2*z*z)
    g = [[-1-q,0,0,0],[0,1-q,0,0],[0,0,1-q,0],[0,0,0,1-q]]
    gi = [[-1+q,0,0,0],[0,1+q,0,0],[0,0,1+q,0],[0,0,0,1+q]]

    G = {}
    for a,b,c in product(range(4), repeat=3):
        v = 0
        for d in range(4):
            v += gi[a][d] * (diff(g[d][c], b) + diff(g[d][b], c) - diff(g[b][c], d)) / 2
        G[a,b,c] = trunc3(v)

    Rup = {}
    Rlow = {}
    for a,b,c,d in product(range(4), repeat=4):
        v = diff(G[a,d,b], c) - diff(G[a,c,b], d)
        for e in range(4):
            v += G[a,c,e]*G[e,d,b] - G[a,d,e]*G[e,c,b]
        Rup[a,b,c,d] = trunc(v)
    for a,b,c,d in product(range(4), repeat=4):
        Rlow[a,b,c,d] = trunc(sum(g[a][e]*Rup[e,b,c,d] for e in range(4)))

    Ric = {}
    for b,d in product(range(4), repeat=2):
        Ric[b,d] = trunc(sum(Rup[a,b,a,d] for a in range(4)))
    Scal = trunc(sum(gi[a][b]*Ric[a,b] for a,b in product(range(4), repeat=2)))

    C = {}
    for a,b,c,d in product(range(4), repeat=4):
        ric = (g[a][c]*Ric[d,b] - g[a][d]*Ric[c,b]
               - g[b][c]*Ric[d,a] + g[b][d]*Ric[c,a]) / 2
        scal = Scal * (g[a][c]*g[d][b] - g[a][d]*g[c][b]) / 6
        C[a,b,c,d] = trunc(Rlow[a,b,c,d] - ric + scal)

    def cup_first(a,b,e,f):
        return trunc(sum(gi[a][i]*gi[b][j]*C[i,j,e,f]
                         for i,j in product(range(4), repeat=2)))

    def callup(a,b,c,d):
        return trunc(sum(gi[a][i]*gi[b][j]*gi[c][m]*gi[d][n]*C[i,j,m,n]
                         for i,j,m,n in product(range(4), repeat=4)))

    CF = {(a,b,e,f): cup_first(a,b,e,f) for a,b,e,f in product(range(4), repeat=4)}
    CA = {(a,b,c,d): callup(a,b,c,d) for a,b,c,d in product(range(4), repeat=4)}

    Qup = {}
    for a,b,c,d in product(range(4), repeat=4):
        Qup[a,b,c,d] = trunc(sum(CF[a,b,e,f] * CA[e,f,c,d]
                                 for e,f in product(range(4), repeat=2)))

    Qlow = {}
    for a,b,c,d in product(range(4), repeat=4):
        Qlow[a,b,c,d] = trunc(sum(g[a][i]*g[b][j]*g[c][m]*g[d][n]*Qup[i,j,m,n]
                                  for i,j,m,n in product(range(4), repeat=4)))

    perms = list(permutations(range(4)))
    T = {}
    for a,b,c,d in product(range(4), repeat=4):
        inds = (a,b,c,d)
        alt = 0
        for p in perms:
            alt += psign(p) * Qlow[inds[p[0]],inds[p[1]],inds[p[2]],inds[p[3]]]
        T[a,b,c,d] = trunc(Qlow[a,b,c,d] - alt/24)

    TRic = {}
    for b,d in product(range(4), repeat=2):
        TRic[b,d] = trunc(sum(gi[a][c]*T[a,b,c,d]
                              for a,c in product(range(4), repeat=2)))
    TSc = trunc(sum(gi[b][d]*TRic[b,d] for b,d in product(range(4), repeat=2)))

    Plow = {}
    for a,b,c,d in product(range(4), repeat=4):
        ric = (g[a][c]*TRic[d,b] - g[a][d]*TRic[c,b]
               - g[b][c]*TRic[d,a] + g[b][d]*TRic[c,a]) / 2
        scal = TSc * (g[a][c]*g[d][b] - g[a][d]*g[c][b]) / 6
        Plow[a,b,c,d] = trunc(3*(T[a,b,c,d] - ric + scal))

    P = {}
    for a,b,c,d in product(range(4), repeat=4):
        P[a,b,c,d] = trunc(sum(gi[a][i]*gi[b][j]*gi[c][m]*gi[d][n]*Plow[i,j,m,n]
                               for i,j,m,n in product(range(4), repeat=4)))

    Cup = {}
    for a,b,c,d in product(range(4), repeat=4):
        Cup[a,b,c,d] = trunc(sum(gi[c][m]*gi[d][n]*C[a,b,m,n]
                                 for m,n in product(range(4), repeat=2)))
    I3 = 0
    for a,b,c,d,e,f in product(range(4), repeat=6):
        I3 += Cup[a,b,c,d]*Cup[c,d,e,f]*Cup[e,f,a,b]
    I3 = trunc(I3)

    PR = trunc(sum(P[a,b,c,d]*Rlow[a,b,c,d]
                   for a,b,c,d in product(range(4), repeat=4)))

    def firstcov(c,a,m,b,n):
        v = diff(P[a,m,b,n], c)
        for r in range(4):
            v += G[a,c,r]*P[r,m,b,n]
            v += G[m,c,r]*P[a,r,b,n]
            v += G[b,c,r]*P[a,m,r,n]
            v += G[n,c,r]*P[a,m,b,r]
        return trunc(v, 1)

    firstdiv = {}
    for m,b,n in product(range(4), repeat=3):
        firstdiv[m,b,n] = trunc(sum(firstcov(a,a,m,b,n) for a in range(4)), 1)

    D = {}
    for m,n in product(range(4), repeat=2):
        v = 0
        for b in range(4):
            v += diff(firstdiv[m,b,n], b)
            for r in range(4):
                v += G[m,b,r]*firstdiv[r,b,n]
                v += G[b,b,r]*firstdiv[m,r,n]
                v += G[n,b,r]*firstdiv[m,b,r]
        D[m,n] = sp.factor(trunc(v,0).subs(ORIGIN))

    Bdiag = []
    Ediag = []
    for a in range(4):
        bv = 0
        for c,d,e in product(range(4), repeat=3):
            bv += P[a,c,d,e].subs(ORIGIN) * ETA[a] * Rlow[a,c,d,e].subs(ORIGIN)
        bv = sp.factor(bv)
        Bdiag.append(sp.simplify(bv/k**3))
        detpart = sp.Rational(1,2) * ETA[a] * I3.subs(ORIGIN)
        ev = sp.factor(detpart - bv - 2*D[a,a])
        Ediag.append(sp.simplify(ev/k**3))

    i30 = sp.factor(I3.subs(ORIGIN))
    prdiff = sp.factor((PR - 3*I3).subs(ORIGIN))
    ddiag = [sp.simplify(D[i,i]/k**3) for i in range(4)]

    return {
        "gate":GATE,
        "preregistration_commit":PREREG,
        "I3_origin_over_kappa3":str(sp.simplify(i30/k**3)),
        "P_dot_R_minus_3I3_origin":str(prdiff),
        "D_up_diagonal_origin_over_kappa3":[str(v) for v in ddiag],
        "B_up_diagonal_origin_over_kappa3":[str(v) for v in Bdiag],
        "E_up_diagonal_origin_over_kappa3":[str(v) for v in Ediag],
        "pass":prdiff == 0,
        "exact_zero_uses_tolerance":False,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out")
    args=ap.parse_args()
    out=compute()
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True)
        Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
