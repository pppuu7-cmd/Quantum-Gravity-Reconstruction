#!/usr/bin/env python3
"""Frozen aggregate classifier for QGR Iter044."""
from __future__ import annotations
import glob
import json
import os

EXPECTED = {'A': 24, 'B': 12, 'C': 8, 'D': 4}

files = glob.glob('iter044-results/**/result.json', recursive=True)
rows = []
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        rows.append(json.load(f))

unique = {}
for r in rows:
    key = (r.get('stream'), int(r.get('index', -1)))
    if key in unique:
        raise SystemExit(f'duplicate lane {key}')
    unique[key] = r
rows = list(unique.values())

counts = {s: sum(r.get('stream') == s for r in rows) for s in EXPECTED}
passes = {s: sum(r.get('stream') == s and r.get('lane_pass') is True for r in rows) for s in EXPECTED}
controls = all(r.get('control_valid') is True for r in rows)
complete = all(counts[s] == EXPECTED[s] for s in EXPECTED) and len(rows) == sum(EXPECTED.values())
stream_full = {s: passes[s] == EXPECTED[s] for s in EXPECTED}

if not complete or not controls:
    classification = 'ITER044_CONTROL_OR_IMPLEMENTATION_INVALID'
elif all(stream_full.values()):
    classification = 'PASS_SCOPED_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION_CONTRACT'
elif any(stream_full.values()):
    classification = 'PARTIAL_SCOPED_QGR_L1_LINEARIZED_RADIATION_CONTRACT'
else:
    classification = 'FAIL_SCOPED_QGR_L1_LINEARIZED_RADIATION_CONTRACT'

A = [r for r in rows if r.get('stream') == 'A']
B = [r for r in rows if r.get('stream') == 'B']
C = [r for r in rows if r.get('stream') == 'C']
D = [r for r in rows if r.get('stream') == 'D']

def mx(rs, key):
    return max((float(r[key]) for r in rs if key in r), default=None)

def mn(rs, key):
    return min((float(r[key]) for r in rs if key in r), default=None)

summary = {
    'gate': 'ITER044-QGR-L1-END-TO-END-LINEARIZED-TT-RADIATION',
    'classification': classification,
    'expected_lanes': sum(EXPECTED.values()),
    'found_unique_lanes': len(rows),
    'counts': counts,
    'passes': passes,
    'controls_valid': bool(controls and complete),
    'stream_full_pass': stream_full,
    'A_max_tt_qgr_residual': mx(A, 'tt_qgr_residual'),
    'A_max_gauge_qgr_residual': mx(A, 'max_gauge_qgr_residual'),
    'A_max_curvature_bridge_error': mx(A, 'curvature_bridge_error'),
    'B_minimum_offshell_residual': mn(B, 'minimum_offshell_residual'),
    'C_max_pure_gauge_qgr_residual': mx(C, 'pure_gauge_qgr_residual'),
    'C_max_shifted_curvature_error': mx(C, 'shifted_curvature_error'),
    'D_max_oddness_e1': mx(D, 'oddness_e1'),
    'D_max_centered_second_variation_e1': mx(D, 'centered_second_variation_e1'),
    'claim_lock': 'Scoped linearized end-to-end QGR-L1 radiative contract only; no generic nonlinear radiation theorem, no quantum radiation amplitude, beta and c6 remain unfixed, no experimental confirmation, theory established remains 0%.',
}

os.makedirs('iter044-summary', exist_ok=True)
with open('iter044-summary/summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, sort_keys=True, allow_nan=False)
print(json.dumps(summary, sort_keys=True, allow_nan=False))
