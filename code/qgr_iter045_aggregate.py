#!/usr/bin/env python3
from __future__ import annotations
import argparse, glob, json, os

EXPECTED = 18


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(a.root, '**', 'result.json'), recursive=True))
    rows = []
    for p in files:
        try:
            with open(p, encoding='utf-8') as f:
                x = json.load(f)
            if x.get('gate') == 'ITER045-QGR-L1-RELATIVE-TT-RESIDUE-SIGNATURE':
                rows.append(x)
        except Exception:
            pass

    by_index = {int(x['index']): x for x in rows}
    found = len(by_index)
    controls_valid = found == EXPECTED and all(x.get('control_valid') for x in by_index.values())
    passes = sum(bool(x.get('lane_pass')) for x in by_index.values())

    if found != EXPECTED:
        cls = 'INFRASTRUCTURE_INCOMPLETE_ITER045_RELATIVE_RESIDUE_AUDIT'
    elif not controls_valid:
        cls = 'CONTROL_INVALID_ITER045_RELATIVE_RESIDUE_AUDIT'
    elif passes == EXPECTED:
        cls = 'PASS_SCOPED_QGR_L1_TWO_POLARIZATION_RELATIVE_RESIDUE_DEGENERACY'
    else:
        cls = 'FAIL_SCOPED_QGR_L1_RELATIVE_RESIDUE_OR_POLARIZATION_SIGNATURE'

    summary = {
        'gate': 'ITER045-QGR-L1-RELATIVE-TT-RESIDUE-SIGNATURE',
        'expected_lanes': EXPECTED,
        'found_lanes': found,
        'passes': passes,
        'controls_valid': controls_valid,
        'terminal_classification': cls,
        'max_on_shell_projected_kernel_relative_norm': max((x.get('on_shell_projected_kernel_relative_norm', 0.0) for x in by_index.values()), default=None),
        'max_plus_cross_relative_difference': max((x.get('max_plus_cross_relative_difference', 0.0) for x in by_index.values()), default=None),
        'max_cross_polarization_mixing': max((x.get('max_cross_polarization_mixing', 0.0) for x in by_index.values()), default=None),
        'min_relative_sign_product': min((x.get('min_relative_sign_product', 0.0) for x in by_index.values()), default=None),
        'max_plus_coefficient_relative_spread': max((x.get('plus_coefficient_relative_spread', 0.0) for x in by_index.values()), default=None),
        'max_cross_coefficient_relative_spread': max((x.get('cross_coefficient_relative_spread', 0.0) for x in by_index.values()), default=None),
        'indices_found': sorted(by_index),
        'claim_guard': 'relative two-polarization coefficient only; absolute action sign/energy positivity and quantum unitarity are not fixed',
    }
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w', encoding='utf-8') as f:
        json.dump(summary, f, sort_keys=True, indent=2, allow_nan=False)
    print(json.dumps(summary, sort_keys=True, allow_nan=False))

if __name__ == '__main__':
    main()
