#!/usr/bin/env python3
"""Iter057K exact-source exposure checkpoint.

This file exposes only source-owned exact G3/H0 geometry. It deliberately does
NOT encode a new Weyl3 Euler formula: that part must be transliterated from the
already-authorized Iter056X lineage without changing conventions.

Scientific status: implementation checkpoint only; not PASS/FAIL for Iter057K
or Iter057J and not a physical-characteristic calculation.
"""
from functools import lru_cache
import json
import sympy as sp

N = 4
R = sp.Rational
KAPPA = R(2, 25)  # exact version of source KAPPA=0.08

# Frozen coordinates/signature inherited from qgr_iter057f_g3_origin_weyl3_k2.py.
t, x, y, z = sp.symbols("t x y z", real=True)
COORDS = (t, x, y, z)


def _zero_tensor(shape):
    return sp.MutableDenseNDimArray.zeros(*shape)


@lru_cache(maxsize=1)
def exact_g3_geometry():
    """Return exact analytic G3/H0 metric and curvature tensors.

    Source potential:
        Phi = (kappa/2) (x^2 + y^2 - 2 z^2)
    Frozen signature: (-,+,+,+)
        g = diag(-1-2 Phi, 1-2 Phi, 1-2 Phi, 1-2 Phi)
    """
    phi = R(1, 2) * KAPPA * (x**2 + y**2 - 2*z**2)
    g = sp.diag(-1 - 2*phi, 1 - 2*phi, 1 - 2*phi, 1 - 2*phi)
    gi = sp.simplify(g.inv())

    Gamma = _zero_tensor((N, N, N))
    for a in range(N):
        for b in range(N):
            for c in range(N):
                expr = 0
                for d in range(N):
                    expr += gi[a, d] * (
                        sp.diff(g[d, c], COORDS[b])
                        + sp.diff(g[d, b], COORDS[c])
                        - sp.diff(g[b, c], COORDS[d])
                    )
                Gamma[a, b, c] = sp.factor(expr / 2)

    # R^a_{ b c d } = d_c Gamma^a_{db} - d_d Gamma^a_{cb}
    #                  + Gamma^a_{ce} Gamma^e_{db} - Gamma^a_{de} Gamma^e_{cb}
    Rup = _zero_tensor((N, N, N, N))
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    expr = sp.diff(Gamma[a, d, b], COORDS[c]) - sp.diff(Gamma[a, c, b], COORDS[d])
                    for e in range(N):
                        expr += Gamma[a, c, e]*Gamma[e, d, b] - Gamma[a, d, e]*Gamma[e, c, b]
                    Rup[a, b, c, d] = sp.factor(expr)

    Rlow = _zero_tensor((N, N, N, N))
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    Rlow[a, b, c, d] = sp.factor(sum(g[a, e]*Rup[e, b, c, d] for e in range(N)))

    Ric = sp.MutableDenseMatrix.zeros(N, N)
    for b in range(N):
        for d in range(N):
            Ric[b, d] = sp.factor(sum(Rup[a, b, a, d] for a in range(N)))
    Scal = sp.factor(sum(gi[a, b]*Ric[a, b] for a in range(N) for b in range(N)))

    # 4D Weyl tensor, all indices lowered.
    W = _zero_tensor((N, N, N, N))
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    ric_part = (
                        g[a, c]*Ric[d, b] - g[a, d]*Ric[c, b]
                        - g[b, c]*Ric[d, a] + g[b, d]*Ric[c, a]
                    ) / 2
                    scal_part = Scal * (g[a, c]*g[d, b] - g[a, d]*g[c, b]) / 6
                    W[a, b, c, d] = sp.factor(Rlow[a, b, c, d] - ric_part + scal_part)

    return {
        "phi": phi,
        "g": g,
        "gi": gi,
        "Gamma": Gamma,
        "Rup": Rup,
        "Rlow": Rlow,
        "Ric": Ric,
        "Scal": Scal,
        "W": W,
    }


def exact_controls(obj):
    g, gi, Rlow, W = obj["g"], obj["gi"], obj["Rlow"], obj["W"]
    inv_res = sp.simplify(g*gi - sp.eye(N))
    metric_sym = all(sp.simplify(g[a, b] - g[b, a]) == 0 for a in range(N) for b in range(N))
    inv_ok = all(sp.simplify(inv_res[a, b]) == 0 for a in range(N) for b in range(N))

    riemann_pair_antisym = True
    riemann_exchange = True
    weyl_pair_antisym = True
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    if sp.simplify(Rlow[a,b,c,d] + Rlow[b,a,c,d]) != 0:
                        riemann_pair_antisym = False
                    if sp.simplify(Rlow[a,b,c,d] - Rlow[c,d,a,b]) != 0:
                        riemann_exchange = False
                    if sp.simplify(W[a,b,c,d] + W[b,a,c,d]) != 0:
                        weyl_pair_antisym = False

    # Exact Weyl trace g^{ac} C_abcd = 0.
    weyl_trace = True
    for b in range(N):
        for d in range(N):
            tr = sum(gi[a, c]*W[a, b, c, d] for a in range(N) for c in range(N))
            if sp.simplify(tr) != 0:
                weyl_trace = False

    return {
        "metric_symmetric": metric_sym,
        "inverse_identity": inv_ok,
        "riemann_first_pair_antisymmetry": riemann_pair_antisym,
        "riemann_pair_exchange": riemann_exchange,
        "weyl_first_pair_antisymmetry": weyl_pair_antisym,
        "weyl_traceless": weyl_trace,
        "exact_weyl3_euler_exposed": False,
        "iter057k_terminal_classification": None,
        "note": "Exact G3 geometry checkpoint only. Authorized Iter056X Weyl3 Euler source and its derivative oracle remain to be exposed exactly before Iter057K can classify.",
    }


def main():
    obj = exact_g3_geometry()
    print(json.dumps(exact_controls(obj), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
