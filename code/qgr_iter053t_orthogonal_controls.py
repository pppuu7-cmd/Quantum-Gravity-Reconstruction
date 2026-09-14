#!/usr/bin/env python3
from __future__ import annotations

import argparse
import glob
import json
import math
import os
from pathlib import Path

import numpy as np
from scipy.special import roots_jacobi

import qgr_iter053_compact_support_action as g53
import qgr_iter052_4d_directional_variation as it

GATE = "ITER053T-ORTHOGONAL-CONTROLS-NONAUTHORITATIVE"
MODES = ("stencil", "weight", "wrapper", "tensor")


def rel(a, b, floor=1e-30):
    return float(abs(a - b) / max(abs(a), abs(b), floor))


def relmat(a, b, floor=1e-30):
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(a), np.linalg.norm(b), floor))


def stencil_control():
    ks = np.array([2.0, 1.0, -1.0, -2.0])
    cs = np.array([-1.0, 8.0, -8.0, 1.0]) / 12.0
    moments = {str(m): float(np.sum(cs * ks**m)) for m in range(6)}
    target = {"0": 0.0, "1": 1.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": -4.0}
    maxerr = max(abs(moments[k] - v) for k, v in target.items())
    leading = moments["5"] / math.factorial(5)
    passed = bool(maxerr <= 2e-15 and abs(leading + 1.0 / 30.0) <= 2e-15)
    return {
        "gate": GATE,
        "mode": "stencil",
        "moments": moments,
        "max_moment_abs_error": maxerr,
        "leading_h4_f5_coefficient": leading,
        "pass": passed,
    }


def weight_scalar(order):
    z, w = roots_jacobi(order, 4.0, 4.0)
    one = float(np.sum(w))
    extra = float(np.sum(w * (1.0 - z*z)**4))
    return (extra / one) ** 4


def weight_control():
    s2 = weight_scalar(2)
    s3 = weight_scalar(3)
    drift = rel(s2, s3)
    ref_s3 = 0.3063851988551639
    ref_drift = 0.2896878290952537
    e1 = abs(s3 - ref_s3)
    e2 = abs(drift - ref_drift)
    passed = bool(e1 <= 5e-13 and e2 <= 5e-13)
    return {
        "gate": GATE,
        "mode": "weight",
        "GJ2_extra_weight_suppression": s2,
        "GJ3_extra_weight_suppression": s3,
        "GJ2_to_GJ3_relative_drift": drift,
        "GJ3_reference_abs_error": e1,
        "drift_reference_abs_error": e2,
        "pass": passed,
    }


def wrapper_control():
    u = np.array([0.05, -0.04, 0.03, -0.02], dtype=float)
    pert = g53.CompactPerturbation(g53.C_PERT[0])
    L = it.shear(0)
    pt = it.TransformPerturbation(pert, L)
    B = float(g53.bump_jets(u)[0])
    p = np.asarray(pert.base.jets(u)[0], dtype=float)
    legacy = np.asarray(pt.base.jets(u)[0], dtype=float)
    identity_res = relmat(legacy, B * p)
    legacy_vs_unfactored = relmat(legacy, p)
    same_object = bool(pt.base is pert)
    finite = bool(np.isfinite([B, identity_res, legacy_vs_unfactored, *p.ravel(), *legacy.ravel()]).all())
    passed = bool(same_object and finite and identity_res <= 2e-12 and legacy_vs_unfactored >= 1e-3)
    return {
        "gate": GATE,
        "mode": "wrapper",
        "source_point": u.tolist(),
        "B": B,
        "transform_wrapper_base_is_compact_perturbation": same_object,
        "factorization_relative_residual": identity_res,
        "legacy_vs_unfactored_relative_difference": legacy_vs_unfactored,
        "finite": finite,
        "pass": passed,
    }


def tensor_control():
    L = np.array([
        [1.0, 0.2, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, -0.15],
        [0.0, 0.0, 0.0, 1.0],
    ])
    Linv = np.linalg.inv(L)
    H = np.array([
        [1.2, -0.3, 0.2, 0.1],
        [-0.3, 0.7, -0.1, 0.05],
        [0.2, -0.1, -0.4, 0.25],
        [0.1, 0.05, 0.25, 0.9],
    ])
    p = np.array([
        [0.6, 0.12, -0.08, 0.03],
        [0.12, -0.5, 0.2, -0.04],
        [-0.08, 0.2, 0.8, 0.11],
        [0.03, -0.04, 0.11, -0.2],
    ])
    Ht = Linv @ H @ Linv.T
    pt = L.T @ p @ L
    base = float(np.einsum("ab,ab->", H, p))
    transformed = float(np.einsum("ab,ab->", Ht, pt))
    exact_res = rel(base, transformed)
    Hwrong = L @ H @ L.T
    wrong = float(np.einsum("ab,ab->", Hwrong, pt))
    wrong_res = rel(transformed, wrong)
    detres = abs(float(np.linalg.det(L)) - 1.0)
    passed = bool(detres <= 1e-15 and exact_res <= 1e-13 and wrong_res >= 1e-3)
    return {
        "gate": GATE,
        "mode": "tensor",
        "det_L": float(np.linalg.det(L)),
        "det_residual": detres,
        "base_contraction": base,
        "transformed_contraction": transformed,
        "exact_contraction_relative_residual": exact_res,
        "wrong_congruence_relative_residual": wrong_res,
        "pass": passed,
    }


def aggregate(root):
    rows = []
    for fn in glob.glob(os.path.join(root, "**", "*.json"), recursive=True):
        try:
            with open(fn, encoding="utf-8") as f:
                obj = json.load(f)
        except Exception:
            continue
        if obj.get("gate") == GATE and obj.get("mode") in MODES:
            rows.append(obj)
    by = {r["mode"]: r for r in rows}
    complete = set(by) == set(MODES)
    passed = bool(complete and all(bool(by[m].get("pass")) for m in MODES))
    return {
        "gate": GATE,
        "mode": "aggregate",
        "classification": "ORTHOGONAL_CONTROLS_PASS" if passed else "ORTHOGONAL_CONTROLS_INVALID",
        "complete": complete,
        "modes_found": sorted(by),
        "all_controls_pass": passed,
        "claim_lock": "Non-authoritative controls only; no Iter053T scientific classification or evidence pooling.",
    }


def write(obj, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(obj, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=MODES + ("aggregate",), required=True)
    ap.add_argument("--input-dir")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.mode == "stencil":
        out = stencil_control()
    elif a.mode == "weight":
        out = weight_control()
    elif a.mode == "wrapper":
        out = wrapper_control()
    elif a.mode == "tensor":
        out = tensor_control()
    else:
        if not a.input_dir:
            raise SystemExit("aggregate requires --input-dir")
        out = aggregate(a.input_dir)
    write(out, a.out)
    if a.mode != "aggregate" and not out["pass"]:
        raise SystemExit(2)
    if a.mode == "aggregate" and out["classification"] != "ORTHOGONAL_CONTROLS_PASS":
        raise SystemExit(3)


if __name__ == "__main__":
    main()
