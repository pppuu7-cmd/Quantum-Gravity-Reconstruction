#!/usr/bin/env python3
"""Iter053S: prospective pointwise H5 tensor-density covariance localization.

Frozen by status/ITER053S_H5_TENSOR_DENSITY_COVARIANCE_PREREG.md.
This diagnostic never reclassifies terminal Iter053R.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
from pathlib import Path

import numpy as np

import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c
import qgr_iter052_4d_directional_variation as it
import qgr_iter053_compact_support_action as g53

N = 4
HSTEPS = (1.0e-3, 5.0e-4, 2.5e-4)
PROBES = (
    np.array([0.0, 0.0, 0.0, 0.0], float),
    np.array([0.08, -0.06, 0.05, -0.04], float),
)
EPS = 5.0e-5


def relscalar(a, b, floor=1e-30):
    return float(abs(a - b) / max(abs(a), abs(b), floor))


def relmat(a, b, floor=1e-30):
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(a), np.linalg.norm(b), floor))


def sym(a):
    return 0.5 * (a + a.T)


def c_objects(index):
    metric = c.PolyMetric(g53.C_METRIC[index])
    pert = g53.CompactPerturbation(g53.C_PERT[index])
    L = it.shear(index)
    M = np.linalg.inv(L)
    mt = c.TransformMetric(metric, L)
    pt = it.TransformPerturbation(pert, L)
    return metric, pert, L, M, mt, pt


def density_push(Q, L, M):
    return abs(float(np.linalg.det(L))) * (M @ Q @ M.T)


def algebra_control():
    H = sym(np.array([
        [2.0, 0.3, -0.4, 0.2],
        [0.3, -1.2, 0.5, 0.1],
        [-0.4, 0.5, 0.7, -0.6],
        [0.2, 0.1, -0.6, 1.5],
    ], float))
    p = sym(np.array([
        [-0.8, 0.4, 0.2, -0.1],
        [0.4, 1.1, -0.3, 0.6],
        [0.2, -0.3, 0.9, 0.25],
        [-0.1, 0.6, 0.25, -1.4],
    ], float))
    rows = []
    for index in range(2):
        L = it.shear(index)
        M = np.linalg.inv(L)
        det = float(np.linalg.det(L))
        Hy = density_push(H, L, M)
        py = L.T @ p @ L
        lhs = float(np.einsum("ab,ab->", Hy, py))
        rhs = abs(det) * float(np.einsum("ab,ab->", H, p))
        exact_res = relscalar(lhs, rhs)
        wrong = L.T @ H @ L
        wrong_lhs = float(np.einsum("ab,ab->", wrong, py))
        wrong_res = relscalar(wrong_lhs, rhs)
        rows.append({
            "index": index,
            "det_L": det,
            "contraction_identity_residual": exact_res,
            "wrong_congruence_relative_residual": wrong_res,
        })
    valid = bool(
        all(abs(r["det_L"] - 1.0) <= 2e-12 for r in rows)
        and all(r["contraction_identity_residual"] <= 2e-12 for r in rows)
        and max(r["wrong_congruence_relative_residual"] for r in rows) >= 1e-2
    )
    return {
        "gate": "ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION",
        "mode": "algebra",
        "rows": rows,
        "valid": valid,
        "claim_lock": "Exact transformation-law control only; no Iter053R reclassification or downstream promotion.",
    }


def probe(index, point_index, hstep):
    metric, pert, L, M, mt, pt = c_objects(index)
    x = PROBES[point_index]
    y = M @ x
    det = float(np.linalg.det(L))

    # Existing implementation controls, deliberately stricter than the local comparison.
    sig0, inv0, _ = d2n.extended_controls(metric, x)
    sig1, inv1, _ = d2n.extended_controls(mt, y)

    g0 = metric.jets(x)[0]
    gt = mt.jets(y)[0]
    h0 = pert.jets(x)[0]
    ht = pt.jets(y)[0]
    metric_map_res = float(np.max(np.abs(gt - L.T @ g0 @ L)))
    pert_map_res = float(np.max(np.abs(ht - L.T @ h0 @ L)))

    H0, z0 = d2n.assemble_minus5(metric, x, hstep)
    H1, z1 = d2n.assemble_minus5(mt, y, hstep)

    alg0 = z0["A"] + z0["I"]
    alg1 = z1["A"] + z1["I"]
    sg0 = math.sqrt(-float(np.linalg.det(z0["g"])))
    sg1 = math.sqrt(-float(np.linalg.det(z1["g"])))
    td0 = -2.0 * sg0 * z0["D"]
    td1 = -2.0 * sg1 * z1["D"]

    exp_alg = density_push(alg0, L, M)
    exp_td = density_push(td0, L, M)
    exp_H = density_push(H0, L, M)

    alg_res = relmat(alg1, exp_alg)
    td_res = relmat(td1, exp_td)
    H_res = relmat(H1, exp_H)

    # Pointwise contraction is the physical scalar-density witness for this gate.
    base_contr = float(np.einsum("ab,ab->", H0, h0))
    trans_contr = float(np.einsum("ab,ab->", H1, ht))
    expected_contr = abs(det) * base_contr
    contraction_res = relscalar(trans_contr, expected_contr)

    direct0 = float(g53.direct_density(metric, pert, x, EPS))
    direct1 = float(g53.direct_density(mt, pt, y, EPS))
    direct_res = relscalar(direct1, abs(det) * direct0)

    vals = [
        det, inv0, inv1, metric_map_res, pert_map_res, alg_res, td_res, H_res,
        base_contr, trans_contr, direct0, direct1, contraction_res, direct_res,
    ]
    valid = bool(
        sig0 and sig1
        and max(inv0, inv1) <= 3e-11
        and abs(det - 1.0) <= 2e-12
        and metric_map_res <= 3e-11
        and pert_map_res <= 3e-11
        and np.isfinite(vals).all()
    )

    return {
        "gate": "ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION",
        "mode": "probe",
        "index": index,
        "point_index": point_index,
        "point_x": x.tolist(),
        "point_y": y.tolist(),
        "hstep": float(hstep),
        "det_L": det,
        "signature_valid_base": bool(sig0),
        "signature_valid_transformed": bool(sig1),
        "max_inverse_residual": float(max(inv0, inv1)),
        "metric_transform_residual": metric_map_res,
        "perturbation_transform_residual": pert_map_res,
        "algebraic_A_plus_I_covariance_residual": alg_res,
        "derivative_density_D5_covariance_residual": td_res,
        "total_H5_covariance_residual": H_res,
        "H_dot_h_covariance_residual": contraction_res,
        "direct_density_covariance_residual": direct_res,
        "base_H_dot_h": base_contr,
        "transformed_H_dot_h": trans_contr,
        "base_direct_density": direct0,
        "transformed_direct_density": direct1,
        "valid": valid,
        "claim_lock": "Pointwise implementation localization only; no Iter053R reclassification.",
    }


def _strictly_decreasing(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def aggregate(root):
    objs = []
    for fn in glob.glob(os.path.join(root, "**", "*.json"), recursive=True):
        try:
            with open(fn, encoding="utf-8") as f:
                o = json.load(f)
        except Exception:
            continue
        if o.get("gate") == "ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION":
            objs.append(o)

    algebra = [o for o in objs if o.get("mode") == "algebra"]
    probes = [o for o in objs if o.get("mode") == "probe"]
    expected_probe_keys = {
        (i, p, float(h)) for i in range(2) for p in range(2) for h in HSTEPS
    }
    found_probe_keys = {
        (int(o["index"]), int(o["point_index"]), float(o["hstep"])) for o in probes
    }

    complete = len(algebra) == 1 and found_probe_keys == expected_probe_keys
    valid = bool(complete and algebra[0].get("valid") and all(o.get("valid") for o in probes)) if complete else False

    finest = [o for o in probes if abs(float(o["hstep"]) - HSTEPS[-1]) < 1e-15]
    direct_ok = bool(finest) and all(o["direct_density_covariance_residual"] <= 2e-6 for o in finest)
    alg_ok = bool(finest) and all(o["algebraic_A_plus_I_covariance_residual"] <= 2e-5 for o in finest)
    d_ok = bool(finest) and all(o["derivative_density_D5_covariance_residual"] <= 2e-3 for o in finest)
    H_ok = bool(finest) and all(o["total_H5_covariance_residual"] <= 2e-3 for o in finest)
    contraction_ok = bool(finest) and all(o["H_dot_h_covariance_residual"] <= 2e-3 for o in finest)

    convergence = {}
    for i in range(2):
        for p in range(2):
            rows = sorted(
                [o for o in probes if int(o["index"]) == i and int(o["point_index"]) == p],
                key=lambda o: float(o["hstep"]),
                reverse=True,
            )
            if len(rows) == 3:
                convergence[f"C{i}_P{p}"] = {
                    "H5_strictly_decreasing": _strictly_decreasing([o["total_H5_covariance_residual"] for o in rows]),
                    "D5_strictly_decreasing": _strictly_decreasing([o["derivative_density_D5_covariance_residual"] for o in rows]),
                    "H5_residuals": [o["total_H5_covariance_residual"] for o in rows],
                    "D5_residuals": [o["derivative_density_D5_covariance_residual"] for o in rows],
                }

    if not valid or not direct_ok:
        classification = "ITER053S_INVALID_IMPLEMENTATION_OR_REFERENCE_CONTROL"
    elif not alg_ok:
        classification = "ITER053S_ALGEBRAIC_H5_COVARIANCE_DEFECT_LOCALIZED"
    elif not (d_ok and H_ok and contraction_ok):
        classification = "ITER053S_D5_COVARIANCE_DEFECT_LOCALIZED"
    else:
        classification = "ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED"

    return {
        "gate": "ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION",
        "mode": "aggregate",
        "classification": classification,
        "complete": complete,
        "valid": valid,
        "probe_count": len(probes),
        "expected_probe_count": 12,
        "direct_reference_control_pass": direct_ok,
        "algebraic_A_plus_I_pass": alg_ok,
        "derivative_density_D5_pass": d_ok,
        "total_H5_pass": H_ok,
        "H_dot_h_contraction_pass": contraction_ok,
        "worst_finest_direct_density_covariance_residual": max((o["direct_density_covariance_residual"] for o in finest), default=None),
        "worst_finest_algebraic_covariance_residual": max((o["algebraic_A_plus_I_covariance_residual"] for o in finest), default=None),
        "worst_finest_D5_covariance_residual": max((o["derivative_density_D5_covariance_residual"] for o in finest), default=None),
        "worst_finest_H5_covariance_residual": max((o["total_H5_covariance_residual"] for o in finest), default=None),
        "worst_finest_contraction_covariance_residual": max((o["H_dot_h_covariance_residual"] for o in finest), default=None),
        "step_convergence": convergence,
        "claim_lock": (
            "Diagnostic/localization only. Terminal Iter053R remains SCIENTIFIC_FAIL. No global Weyl3 EOM, "
            "quantum amplitude/measure, c6, beta=1, unitarity, GR-recovery or theory-establishment promotion."
        ),
    }


def write(obj, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(obj, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("algebra", "probe", "aggregate"), required=True)
    ap.add_argument("--index", type=int)
    ap.add_argument("--point", type=int)
    ap.add_argument("--hstep", type=float)
    ap.add_argument("--input-dir")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    if a.mode == "algebra":
        out = algebra_control()
    elif a.mode == "probe":
        if a.index not in (0, 1) or a.point not in (0, 1) or a.hstep not in HSTEPS:
            raise SystemExit("probe mode requires frozen --index 0/1, --point 0/1, --hstep 1e-3/5e-4/2.5e-4")
        out = probe(a.index, a.point, a.hstep)
    else:
        if not a.input_dir:
            raise SystemExit("aggregate mode requires --input-dir")
        out = aggregate(a.input_dir)

    write(out, a.out)
    if a.mode != "aggregate" and not out.get("valid", False):
        raise SystemExit(3)
    if a.mode == "aggregate" and out["classification"] == "ITER053S_INVALID_IMPLEMENTATION_OR_REFERENCE_CONTROL":
        raise SystemExit(3)


if __name__ == "__main__":
    main()
