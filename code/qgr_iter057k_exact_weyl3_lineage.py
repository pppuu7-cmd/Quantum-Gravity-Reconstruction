#!/usr/bin/env python3
"""Iter057K exact transliteration of the authorized Weyl3 source lineage.

This module mirrors, without fitting or new physics input, the algebraic objects used by
qgr_iter051b1_weyl3_p_insertion.py, qgr_iter051b0_double_divergence_operator.py,
qgr_iter051c_full_eom.py and qgr_iter051c_d2n_near_null.py, but on the exact G3/H0
geometry exposed by qgr_iter057k_exact_g3_geometry.py.

Normalization authority is the terminal Iter056X derivation commit
5b2acf5a47f4ba66fb126bdeab28505dd0dfb852, section D: for covariant metric
variation delta g_ab=h_ab it proves exactly

    H5^{ab} = A^{ab}+I^{ab}-2*sqrt(-g) D5^{ab}
            = sqrt(-g) E_W3^{ab}.

Therefore E_W3^{ab}=H5^{ab}/sqrt(-g). This is an authority lookup/transliteration,
not a fitted normalization and not a new physics primitive.
"""
from functools import lru_cache
from itertools import permutations, product

import sympy as sp

from qgr_iter057k_exact_g3_geometry import COORDS, N, exact_g3_geometry

EPS = sp.symbols("eps_iter057k")


def _zero4():
    return sp.MutableDenseNDimArray.zeros(N, N, N, N)


def _copy4(T):
    out = _zero4()
    for idx in product(range(N), repeat=4):
        out[idx] = T[idx]
    return out


def _perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inv % 2 else 1


def weyl_from_riemann(Rlow, g, gi):
    """Exact 4D Weyl tensor with the already-used lowered-index convention."""
    Ric = sp.MutableDenseMatrix.zeros(N, N)
    for b in range(N):
        for d in range(N):
            Ric[b, d] = sp.factor(sum(gi[a, c] * Rlow[a, b, c, d]
                                      for a in range(N) for c in range(N)))
    Scal = sp.factor(sum(gi[b, d] * Ric[b, d] for b in range(N) for d in range(N)))
    C = _zero4()
    for a, b, c, d in product(range(N), repeat=4):
        C[a, b, c, d] = sp.factor(
            Rlow[a, b, c, d]
            - sp.Rational(1, 2) * (
                g[a, c] * Ric[b, d] - g[a, d] * Ric[b, c]
                - g[b, c] * Ric[a, d] + g[b, d] * Ric[a, c]
            )
            + Scal * (g[a, c] * g[b, d] - g[a, d] * g[b, c]) / 6
        )
    return C


def cup_component(C, gi, a, b, c, d):
    return sp.factor(sum(gi[c, e] * gi[d, f] * C[a, b, e, f]
                         for e in range(N) for f in range(N)))


def weyl3_scalar_from_C(C, gi):
    """I3=C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}, matching the authorized lineage."""
    Cup = {(a, b, c, d): cup_component(C, gi, a, b, c, d)
           for a, b, c, d in product(range(N), repeat=4)}
    expr = 0
    for a, b, c, d, e, f in product(range(N), repeat=6):
        expr += Cup[a, b, c, d] * Cup[c, d, e, f] * Cup[e, f, a, b]
    return sp.factor(expr)


@lru_cache(maxsize=1)
def exact_i3():
    obj = exact_g3_geometry()
    return weyl3_scalar_from_C(obj["W"], obj["gi"])


@lru_cache(maxsize=None)
def raw_p_gradient_component(a, b, c, d):
    obj = exact_g3_geometry()
    Rpert = _copy4(obj["Rlow"])
    Rpert[a, b, c, d] = Rpert[a, b, c, d] + EPS
    Cpert = weyl_from_riemann(Rpert, obj["g"], obj["gi"])
    expr = weyl3_scalar_from_C(Cpert, obj["gi"])
    return sp.factor(sp.diff(expr, EPS).subs(EPS, 0))


def _pair_projected_component(a, b, c, d):
    def A(i, j, k, l):
        return sp.Rational(1, 4) * (
            raw_p_gradient_component(i, j, k, l)
            - raw_p_gradient_component(j, i, k, l)
            - raw_p_gradient_component(i, j, l, k)
            + raw_p_gradient_component(j, i, l, k)
        )
    return sp.factor((A(a, b, c, d) + A(c, d, a, b)) / 2)


@lru_cache(maxsize=None)
def p_component(a, b, c, d):
    inds = (a, b, c, d)
    T = _pair_projected_component(a, b, c, d)
    alt = 0
    for p in permutations(range(4)):
        alt += _perm_sign(p) * _pair_projected_component(
            inds[p[0]], inds[p[1]], inds[p[2]], inds[p[3]])
    return sp.factor(T - alt / 24)


def first_cov_p_component(c, a, m, b, n):
    obj = exact_g3_geometry(); G = obj["Gamma"]
    val = sp.diff(p_component(a, m, b, n), COORDS[c])
    for r in range(N):
        val += G[a, c, r] * p_component(r, m, b, n)
        val += G[m, c, r] * p_component(a, r, b, n)
        val += G[b, c, r] * p_component(a, m, r, n)
        val += G[n, c, r] * p_component(a, m, b, r)
    return sp.factor(val)


@lru_cache(maxsize=None)
def first_div_p_component(m, b, n):
    return sp.factor(sum(first_cov_p_component(a, a, m, b, n) for a in range(N)))


@lru_cache(maxsize=None)
def double_div_p_component(m, n):
    obj = exact_g3_geometry(); G = obj["Gamma"]
    val = 0
    for b in range(N):
        val += sp.diff(first_div_p_component(m, b, n), COORDS[b])
        for r in range(N):
            val += G[m, b, r] * first_div_p_component(r, b, n)
            val += G[b, b, r] * first_div_p_component(m, r, n)
            val += G[n, b, r] * first_div_p_component(m, b, r)
    return sp.factor(val)


@lru_cache(maxsize=None)
def metric_density_variation_component(a, b):
    obj = exact_g3_geometry(); gpert = sp.MutableDenseMatrix(obj["g"])
    if a == b:
        gpert[a, b] += EPS; divisor = 1
    else:
        gpert[a, b] += EPS; gpert[b, a] += EPS; divisor = 2
    gipert = sp.simplify(gpert.inv())
    Cpert = weyl_from_riemann(obj["Rlow"], gpert, gipert)
    density = sp.sqrt(-sp.det(gpert)) * weyl3_scalar_from_C(Cpert, gipert)
    return sp.factor(sp.diff(density, EPS).subs(EPS, 0) / divisor)


@lru_cache(maxsize=None)
def lowering_insertion_component(a, e):
    obj = exact_g3_geometry(); g, gi, Rlow = obj["g"], obj["gi"], obj["Rlow"]
    sg = sp.sqrt(-sp.det(g))
    def Q(i, j):
        val = 0
        for b, c, d, f in product(range(N), repeat=4):
            val += p_component(i, b, c, d) * gi[j, f] * Rlow[f, b, c, d]
        return sg * val
    return sp.factor((Q(a, e) + Q(e, a)) / 2)


@lru_cache(maxsize=None)
def assembled_minus5_density_component(a, b):
    obj = exact_g3_geometry(); sg = sp.sqrt(-sp.det(obj["g"]))
    return sp.factor(metric_density_variation_component(a, b)
                     + lowering_insertion_component(a, b)
                     - 2 * sg * double_div_p_component(a, b))


@lru_cache(maxsize=None)
def e_w3_up_component(a, b):
    """Authorized Iter056X E_W3^{ab}=H5^{ab}/sqrt(-g), with c6 factored out."""
    obj = exact_g3_geometry(); sg = sp.sqrt(-sp.det(obj["g"]))
    return sp.factor(assembled_minus5_density_component(a, b) / sg)


@lru_cache(maxsize=None)
def e_w3_down_component(a, b):
    """Lowered E_W3_ab, useful for Iter057J H_ab construction."""
    obj = exact_g3_geometry(); g = obj["g"]
    return sp.factor(sum(g[a, m] * g[b, n] * e_w3_up_component(m, n)
                         for m in range(N) for n in range(N)))


def exact_lineage_controls_at_source_level():
    p_pair1 = all(sp.simplify(p_component(a,b,c,d) + p_component(b,a,c,d)) == 0
                  for a,b,c,d in product(range(N), repeat=4))
    p_pair2 = all(sp.simplify(p_component(a,b,c,d) + p_component(a,b,d,c)) == 0
                  for a,b,c,d in product(range(N), repeat=4))
    p_exchange = all(sp.simplify(p_component(a,b,c,d) - p_component(c,d,a,b)) == 0
                     for a,b,c,d in product(range(N), repeat=4))
    density_sym = all(sp.simplify(assembled_minus5_density_component(a,b)
                                  - assembled_minus5_density_component(b,a)) == 0
                      for a in range(N) for b in range(N))
    e_sym = all(sp.simplify(e_w3_up_component(a,b)-e_w3_up_component(b,a)) == 0
                for a in range(N) for b in range(N))
    return {
        "p_first_pair_antisymmetry": p_pair1,
        "p_second_pair_antisymmetry": p_pair2,
        "p_pair_exchange": p_exchange,
        "assembled_minus5_density_symmetric": density_sym,
        "covariant_iter056x_E_W3_normalization_resolved": True,
        "normalization_authority_commit": "5b2acf5a47f4ba66fb126bdeab28505dd0dfb852",
        "normalization_identity": "H5^{ab}=sqrt(-g)*E_W3^{ab}",
        "E_W3_symmetric": e_sym,
        "iter057k_terminal_classification": None,
    }
