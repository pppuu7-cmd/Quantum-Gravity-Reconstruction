#!/usr/bin/env python3
"""Iter053T: source-parameter-faithful weighted pushforward covariance audit.

Prospectively frozen by status/ITER053T_WEIGHTED_SUPPORT_PUSHFORWARD_PREREG.md.
This is a distinct diagnostic/bridge gate and never reclassifies terminal Iter053R.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
from pathlib import Path

import numpy as np

import qgr_iter053_compact_support_action as g53
import qgr_iter053r_weighted_h5_compact_support as r
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c

GATE = "ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE"
ORDERS = (2, 3)


def rel(a, b, floor=1e-30):
    return float(abs(a - b) / max(abs(a), abs(b), floor))


def relmat(a, b, floor=1e-30):
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(a), np.linalg.norm(b), floor))


def c_objects(index):
    metric = c.PolyMetric(g53.C_METRIC[index])
    pert = g53.CompactPerturbation(g53.C_PERT[index])
    L = it.shear(index)
    M = np.linalg.inv(L)
    mt = c.TransformMetric(metric, L)
    pt = it.TransformPerturbation(pert, L)
    return metric, pert, L, M, mt, pt


def structural_lane():
    worst_factor = 0.0
    max_legacy_vs_correct = 0.0
    rows = []
    for index in range(2):
        _, pert, L, _, _, pt = c_objects(index)
        for order in ORDERS:
            n = 0
            local_worst = 0.0
            local_diff = 0.0
            bmin, bmax = float("inf"), float("-inf")
            for u, _ in r.gj_tasks(order):
                B = float(g53.bump_jets(u)[0])
                p = pert.base.jets(u)[0]
                correct = L.T @ p @ L
                # Exact Iter053R wrapper-depth path: pt.base is the full CompactPerturbation.
                legacy = L.T @ pt.base.jets(u)[0] @ L
                local_worst = max(local_worst, relmat(legacy, B * correct))
                local_diff = max(local_diff, relmat(legacy, correct))
                bmin = min(bmin, B)
                bmax = max(bmax, B)
                n += 1
            worst_factor = max(worst_factor, local_worst)
            max_legacy_vs_correct = max(max_legacy_vs_correct, local_diff)
            rows.append({
                "index": index,
                "order": order,
                "nodes": n,
                "min_B": bmin,
                "max_B": bmax,
                "max_factorization_residual": local_worst,
                "max_legacy_vs_correct_relative_difference": local_diff,
            })
    valid = bool(np.isfinite([worst_factor, max_legacy_vs_correct]).all())
    factor_ok = bool(worst_factor <= 2e-12)
    negative_ok = bool(max_legacy_vs_correct >= 1e-1)
    return {
        "gate": GATE,
        "mode": "structural",
        "valid": valid,
        "factorization_identity_pass": factor_ok,
        "legacy_negative_control_pass": negative_ok,
        "worst_factorization_residual": worst_factor,
        "max_legacy_vs_correct_relative_difference": max_legacy_vs_correct,
        "rows": rows,
        "claim_lock": "Structural wrapper-depth audit only; Iter053R history is immutable.",
    }


def numeric_lane(index, order):
    metric, pert, L, M, mt, _ = c_objects(index)
    detL = float(np.linalg.det(L))
    base_bulk = 0.0
    corrected_bulk = 0.0
    legacy_bulk = 0.0
    max_node_residual = 0.0
    max_inv = 0.0
    sig = True
    node_count = 0
    max_legacy_node_residual = 0.0

    for u, wt in r.gj_tasks(order):
        y = M @ u
        s0, iv0, _ = d2n.extended_controls(metric, u)
        s1, iv1, _ = d2n.extended_controls(mt, y)
        sig = sig and bool(s0) and bool(s1)
        max_inv = max(max_inv, float(iv0), float(iv1))

        Hx, _ = d2n.assemble_minus5(metric, u, r.HSTEP)
        Hy, _ = d2n.assemble_minus5(mt, y, r.HSTEP)

        p = pert.base.jets(u)[0]
        py = L.T @ p @ L
        B = float(g53.bump_jets(u)[0])

        base_node = float(np.einsum("ab,ab->", Hx, p))
        corrected_node = float(np.einsum("ab,ab->", Hy, py))
        legacy_node = float(np.einsum("ab,ab->", Hy, B * py))

        max_node_residual = max(max_node_residual, rel(base_node, corrected_node))
        max_legacy_node_residual = max(max_legacy_node_residual, rel(base_node, legacy_node))
        base_bulk += wt * base_node
        corrected_bulk += wt * corrected_node
        legacy_bulk += wt * legacy_node
        node_count += 1

    corrected_cov = rel(base_bulk, corrected_bulk)
    legacy_cov = rel(base_bulk, legacy_bulk)
    nums = [detL, base_bulk, corrected_bulk, legacy_bulk, corrected_cov, legacy_cov,
            max_node_residual, max_legacy_node_residual, max_inv]
    valid = bool(
        sig
        and max_inv <= 3e-11
        and abs(detL - 1.0) <= 2e-12
        and np.isfinite(nums).all()
    )
    corrected_pass = bool(valid and max_node_residual <= 2e-3 and corrected_cov <= 2e-3)

    return {
        "gate": GATE,
        "mode": "numeric",
        "index": index,
        "order": order,
        "node_count": node_count,
        "det_L": detL,
        "signature_valid": bool(sig),
        "max_inverse_residual": max_inv,
        "base_weighted_bulk": float(base_bulk),
        "corrected_transformed_weighted_bulk": float(corrected_bulk),
        "legacy_transformed_weighted_bulk": float(legacy_bulk),
        "max_nodewise_corrected_covariance_residual": max_node_residual,
        "max_nodewise_legacy_covariance_residual": max_legacy_node_residual,
        "corrected_integrated_covariance_residual": corrected_cov,
        "legacy_integrated_covariance_residual": legacy_cov,
        "valid": valid,
        "corrected_lane_pass": corrected_pass,
        "claim_lock": "C-lane weighted pushforward only; no full A4+B2+C2 closure or Iter053R rewrite.",
    }


def aggregate(root):
    objs = []
    for fn in glob.glob(os.path.join(root, "**", "*.json"), recursive=True):
        try:
            with open(fn, encoding="utf-8") as f:
                obj = json.load(f)
        except Exception:
            continue
        if obj.get("gate") == GATE:
            objs.append(obj)

    structural = [o for o in objs if o.get("mode") == "structural"]
    numeric = [o for o in objs if o.get("mode") == "numeric"]
    expected = {(i, q) for i in range(2) for q in ORDERS}
    found = {(int(o["index"]), int(o["order"])) for o in numeric}
    complete = len(structural) == 1 and found == expected
    all_valid = bool(complete and structural[0].get("valid") and all(o.get("valid") for o in numeric)) if complete else False
    factor_ok = bool(complete and structural[0].get("factorization_identity_pass"))
    structural_negative_ok = bool(complete and structural[0].get("legacy_negative_control_pass"))
    corrected_lanes_ok = bool(complete and all(o.get("corrected_lane_pass") for o in numeric))

    by = {(int(o["index"]), int(o["order"])): o for o in numeric}
    convergence = {}
    convergence_ok = True
    legacy_controls_ok = True
    improvement_ok = True
    for i in range(2):
        if (i, 2) not in by or (i, 3) not in by:
            convergence_ok = legacy_controls_ok = improvement_ok = False
            continue
        q2, q3 = by[(i, 2)], by[(i, 3)]
        base_change = rel(q2["base_weighted_bulk"], q3["base_weighted_bulk"])
        corrected_change = rel(q2["corrected_transformed_weighted_bulk"], q3["corrected_transformed_weighted_bulk"])
        legacy3 = float(q3["legacy_integrated_covariance_residual"])
        corrected3 = float(q3["corrected_integrated_covariance_residual"])
        ratio = legacy3 / max(corrected3, 1e-30)
        convergence[f"C{i}"] = {
            "base_GJ2_to_GJ3_relative_change": base_change,
            "corrected_GJ2_to_GJ3_relative_change": corrected_change,
            "legacy_GJ3_covariance_residual": legacy3,
            "corrected_GJ3_covariance_residual": corrected3,
            "legacy_to_corrected_residual_ratio": ratio,
        }
        convergence_ok = convergence_ok and base_change <= 2e-3 and corrected_change <= 2e-3
        legacy_controls_ok = legacy_controls_ok and legacy3 >= 1e-1
        improvement_ok = improvement_ok and ratio >= 50.0

    if not all_valid:
        classification = "ITER053T_INVALID_IMPLEMENTATION_OR_REFERENCE_CONTROL"
    elif not factor_ok:
        classification = "ITER053T_LEGACY_DOUBLE_WEIGHT_DIAGNOSIS_NOT_CONFIRMED"
    elif not (structural_negative_ok and corrected_lanes_ok and convergence_ok and legacy_controls_ok and improvement_ok):
        classification = "ITER053T_DOUBLE_WEIGHT_DIAGNOSIS_CONFIRMED_CORRECTED_PUSHFORWARD_FAIL"
    else:
        classification = "ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED"

    return {
        "gate": GATE,
        "mode": "aggregate",
        "complete": complete,
        "valid": all_valid,
        "classification": classification,
        "structural_factorization_pass": factor_ok,
        "structural_negative_control_pass": structural_negative_ok,
        "corrected_numeric_lanes_pass": corrected_lanes_ok,
        "GJ2_GJ3_convergence_pass": convergence_ok,
        "legacy_GJ3_negative_controls_pass": legacy_controls_ok,
        "legacy_to_corrected_improvement_pass": improvement_ok,
        "numeric_lanes_found": sorted([list(x) for x in found]),
        "convergence": convergence,
        "worst_structural_factorization_residual": structural[0].get("worst_factorization_residual") if structural else None,
        "worst_corrected_nodewise_covariance_residual": max((o["max_nodewise_corrected_covariance_residual"] for o in numeric), default=None),
        "worst_corrected_integrated_covariance_residual": max((o["corrected_integrated_covariance_residual"] for o in numeric), default=None),
        "claim_lock": (
            "Weighted C pushforward diagnosis only. Iter053R remains historical SCIENTIFIC_FAIL; no full A4+B2+C2 closure, "
            "global Weyl3 theorem, quantum-layer transition, c6/beta fixing, unitarity, UV/GR/new-physics or theory-establishment claim."
        ),
    }


def write(obj, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(obj, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("structural", "numeric", "aggregate"), required=True)
    ap.add_argument("--index", type=int)
    ap.add_argument("--order", type=int)
    ap.add_argument("--input-dir")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    if a.mode == "structural":
        out = structural_lane()
    elif a.mode == "numeric":
        if a.index not in (0, 1) or a.order not in ORDERS:
            raise SystemExit("numeric mode requires frozen --index 0/1 and --order 2/3")
        out = numeric_lane(a.index, a.order)
    else:
        if not a.input_dir:
            raise SystemExit("aggregate mode requires --input-dir")
        out = aggregate(a.input_dir)

    write(out, a.out)
    if a.mode == "structural" and not (out["valid"] and out["factorization_identity_pass"] and out["legacy_negative_control_pass"]):
        raise SystemExit(3)
    if a.mode == "numeric" and not out["valid"]:
        raise SystemExit(3)
    if a.mode == "aggregate" and out["classification"] == "ITER053T_INVALID_IMPLEMENTATION_OR_REFERENCE_CONTROL":
        raise SystemExit(3)


if __name__ == "__main__":
    main()
