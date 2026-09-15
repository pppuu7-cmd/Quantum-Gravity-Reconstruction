#!/usr/bin/env python3
"""Iter057M exact diagonal source-component audit using only authorized Iter057K lineage."""
import argparse
import json
from pathlib import Path

import sympy as sp

from qgr_iter057k_exact_g3_geometry import COORDS, exact_g3_geometry
from qgr_iter057k_exact_weyl3_lineage import (
    assembled_minus5_density_component,
    double_div_p_component,
    e_w3_down_component,
    e_w3_up_component,
    exact_i3,
    lowering_insertion_component,
    metric_density_variation_component,
)

GATE = "ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION"
AUDIT_PLAN = "f087b579e0c13714178bfc43e9a8e2f7fa907312"
ORIGIN = {c: sp.Integer(0) for c in COORDS}


def at0(expr):
    return sp.factor(sp.simplify(expr.subs(ORIGIN)))


def lane(i):
    obj = exact_g3_geometry()
    sg0 = at0(sp.sqrt(-sp.det(obj["g"])))
    i30 = at0(exact_i3())
    d = at0(double_div_p_component(i, i))
    a = at0(metric_density_variation_component(i, i))
    ins = at0(lowering_insertion_component(i, i))
    h5 = at0(assembled_minus5_density_component(i, i))
    eup = at0(e_w3_up_component(i, i))
    edn = at0(e_w3_down_component(i, i))
    h5_direct = sp.factor(a + ins - 2 * sg0 * d)
    identities = {
        "H5_decomposition_exact": sp.simplify(h5 - h5_direct) == 0,
        "Eup_normalization_exact": sp.simplify(eup - h5 / sg0) == 0,
    }
    return {
        "gate": GATE,
        "audit_plan_commit": AUDIT_PLAN,
        "diagonal_index": i,
        "sqrt_minus_g_origin": str(sg0),
        "I3_origin": str(i30),
        "D_up_origin": str(d),
        "A_density_origin": str(a),
        "I_density_origin": str(ins),
        "H5_density_origin": str(h5),
        "E_W3_up_origin": str(eup),
        "E_W3_down_origin": str(edn),
        "identities": identities,
        "pass": all(identities.values()),
        "exact_zero_uses_tolerance": False,
        "c6_status": "SYMBOLIC_UNFIXED_FACTORED_OUT",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", type=int, required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if args.index not in range(4):
        raise SystemExit("index must be 0..3")
    out = lane(args.index)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, sort_keys=True))
    if out["pass"] is not True:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
