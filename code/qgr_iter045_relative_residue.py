#!/usr/bin/env python3
"""Iter045: relative two-polarization residue/signature audit for QGR-L1.

Prospectively preregistered in status/ITERATION_045.md before implementation.
This gate is independent of Iter044 production results.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import numpy as np

from qgr_iter044_end_to_end_radiative import (
    AINV, AMAP, ETA, chart_errors, gauge_matrix, hessian,
    polarization, relative_rank, vecsym,
)

RAW_DIRECTIONS = [
    (1.0, 1.0, 0.0),
    (1.0, 2.0, 2.0),
    (2.0, -1.0, 2.0),
    (1.0, -2.0, 2.0),
    (2.0, 2.0, -1.0),
    (-1.0, 2.0, 2.0),
]
DIRECTIONS = [np.array(v, float) / np.linalg.norm(np.array(v, float)) for v in RAW_DIRECTIONS]
KAPPAS = [0.7, 1.3, 2.1]
RATIOS = [0.75, 0.90, 1.00, 1.10, 1.25]


def tt_columns(n: np.ndarray) -> np.ndarray:
    cols = []
    for psi in (0.0, math.pi / 2.0):
        hm = np.zeros((4, 4), float)
        hm[1:, 1:] = polarization(n, psi)
        hi = AINV @ hm @ AINV.T
        cols.append(vecsym(hi))
    return np.column_stack(cols)


def rel(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), 1e-30)


def spread(vals) -> float:
    vals = [float(x) for x in vals]
    mean = sum(vals) / len(vals)
    return (max(vals) - min(vals)) / max(abs(mean), 1e-30)


def lane(index: int) -> dict:
    di = index // len(KAPPAS)
    ki = index % len(KAPPAS)
    n = DIRECTIONS[di]
    kappa = KAPPAS[ki]
    P = tt_columns(n)
    rows = []

    for r in RATIOS:
        p = kappa * np.concatenate(([1.0], -r * n))
        k = np.linalg.solve(AMAP, p)
        H = hessian(k)
        Ktt = P.T @ H @ P
        shell = float(p @ ETA @ p)
        rows.append({
            'ratio': r,
            'shell': shell,
            'full_hessian_rank': relative_rank(H),
            'gauge_rank': relative_rank(gauge_matrix(k)),
            'ktt': Ktt.tolist(),
            'ktt_norm': float(np.linalg.norm(Ktt)),
        })

    on = rows[2]
    off = rows[:2] + rows[3:]
    off_scale = max(x['ktt_norm'] for x in off)
    on_ratio = on['ktt_norm'] / max(off_scale, 1e-30)

    coeff_plus = []
    coeff_cross = []
    pair_agreement = []
    mixing = []
    sign_products = []
    for row in off:
        M = np.asarray(row['ktt'], float)
        s = float(row['shell'])
        cp = float(M[0, 0] / s)
        cc = float(M[1, 1] / s)
        coeff_plus.append(cp)
        coeff_cross.append(cc)
        pair_agreement.append(rel(cp, cc))
        mixing.append(abs(float(M[0, 1])) / max(abs(float(M[0, 0])), abs(float(M[1, 1])), 1e-30))
        sign_products.append(cp * cc)

    ce1, ce2 = chart_errors()
    finite = all(np.isfinite(x) for x in coeff_plus + coeff_cross + pair_agreement + mixing)
    nonzero = all(abs(x) > 1e-8 for x in coeff_plus + coeff_cross)
    controls = bool(ce1 < 1e-12 and ce2 < 1e-12 and finite and off_scale > 1e-12)
    science = bool(
        on['full_hessian_rank'] == 4
        and on['gauge_rank'] == 4
        and on_ratio < 1e-10
        and all(x['full_hessian_rank'] == 6 for x in off)
        and all(x['gauge_rank'] == 4 for x in off)
        and nonzero
        and max(pair_agreement) < 1e-9
        and min(sign_products) > 0.0
        and max(mixing) < 1e-9
        and spread(coeff_plus) < 1e-9
        and spread(coeff_cross) < 1e-9
    )

    return {
        'gate': 'ITER045-QGR-L1-RELATIVE-TT-RESIDUE-SIGNATURE',
        'index': index,
        'direction_index': di,
        'raw_direction': list(RAW_DIRECTIONS[di]),
        'unit_direction': n.tolist(),
        'kappa': kappa,
        'rows': rows,
        'chart_C_error': ce1,
        'chart_E_error': ce2,
        'on_shell_projected_kernel_relative_norm': on_ratio,
        'plus_shell_normalized_coefficients': coeff_plus,
        'cross_shell_normalized_coefficients': coeff_cross,
        'max_plus_cross_relative_difference': max(pair_agreement),
        'max_cross_polarization_mixing': max(mixing),
        'min_relative_sign_product': min(sign_products),
        'plus_coefficient_relative_spread': spread(coeff_plus),
        'cross_coefficient_relative_spread': spread(coeff_cross),
        'control_valid': controls,
        'scientific_relation_pass': science,
        'lane_pass': bool(controls and science),
        'classification': (
            'ITER045_RELATIVE_RESIDUE_LANE_PASS' if controls and science
            else ('ITER045_CONTROL_INVALID' if not controls else 'ITER045_RELATIVE_RESIDUE_LANE_FAIL')
        ),
        'claim_guard': 'relative two-polarization coefficient only; absolute action sign/energy positivity and quantum unitarity are not fixed',
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', type=int, required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    assert 0 <= args.index < len(DIRECTIONS) * len(KAPPAS)
    out = lane(args.index)
    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(out, f, sort_keys=True, allow_nan=False)
    print(json.dumps(out, sort_keys=True, allow_nan=False))


if __name__ == '__main__':
    main()
