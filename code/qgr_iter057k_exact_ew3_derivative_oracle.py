#!/usr/bin/env python3
"""Iter057K exact covariant derivative oracle for the authorized Iter056X E_W3.

This is a pure transliteration layer on top of qgr_iter057k_exact_weyl3_lineage.py.
No coefficient fitting, numerical tolerance, new background primitive, or new physics
input is introduced. c6 remains factored out and symbolic/unfixed.
"""
from functools import lru_cache
from itertools import product

import sympy as sp

from qgr_iter057k_exact_g3_geometry import COORDS, N, exact_g3_geometry
from qgr_iter057k_exact_weyl3_lineage import e_w3_down_component, e_w3_up_component


@lru_cache(maxsize=None)
def first_cov_e_down_component(c, a, b):
    """(nabla_c E)_ab for the authorized lowered Weyl3 Euler tensor."""
    G = exact_g3_geometry()["Gamma"]
    val = sp.diff(e_w3_down_component(a, b), COORDS[c])
    for r in range(N):
        val -= G[r, c, a] * e_w3_down_component(r, b)
        val -= G[r, c, b] * e_w3_down_component(a, r)
    return sp.factor(val)


@lru_cache(maxsize=None)
def second_cov_e_down_component(e, c, a, b):
    """(nabla_e nabla_c E)_ab, retaining the derivative index c covariantly."""
    G = exact_g3_geometry()["Gamma"]
    val = sp.diff(first_cov_e_down_component(c, a, b), COORDS[e])
    for r in range(N):
        val -= G[r, e, c] * first_cov_e_down_component(r, a, b)
        val -= G[r, e, a] * first_cov_e_down_component(c, r, b)
        val -= G[r, e, b] * first_cov_e_down_component(c, a, r)
    return sp.factor(val)


@lru_cache(maxsize=None)
def divergence_e_up_component(b):
    """Exact Noether object nabla_a E^{ab}."""
    G = exact_g3_geometry()["Gamma"]
    val = 0
    for a in range(N):
        val += sp.diff(e_w3_up_component(a, b), COORDS[a])
        for r in range(N):
            val += G[a, a, r] * e_w3_up_component(r, b)
            val += G[b, a, r] * e_w3_up_component(a, r)
    return sp.factor(val)


def exact_derivative_controls():
    """Frozen exact controls. Equality is symbolic exact equality, never tolerance based."""
    e_sym = all(sp.simplify(e_w3_down_component(a, b)-e_w3_down_component(b, a)) == 0
                for a, b in product(range(N), repeat=2))
    d1_sym = all(sp.simplify(first_cov_e_down_component(c, a, b)
                             - first_cov_e_down_component(c, b, a)) == 0
                 for c, a, b in product(range(N), repeat=3))
    d2_sym = all(sp.simplify(second_cov_e_down_component(e, c, a, b)
                             - second_cov_e_down_component(e, c, b, a)) == 0
                 for e, c, a, b in product(range(N), repeat=4))
    noether = [sp.simplify(divergence_e_up_component(b)) for b in range(N)]
    noether_zero = all(v == 0 for v in noether)
    return {
        "E_W3_down_symmetric_exact": e_sym,
        "nabla_E_W3_down_symmetric_exact": d1_sym,
        "nabla2_E_W3_down_symmetric_exact": d2_sym,
        "noether_divergence_components": noether,
        "noether_divergence_zero_exact": noether_zero,
        "second_covariant_derivative_oracle_exposed": True,
        "exact_zero_decision_uses_tolerance": False,
        "c6_status": "symbolic_unfixed_factored_out",
        "iter057k_terminal_classification": None,
    }


if __name__ == "__main__":
    print(exact_derivative_controls())
