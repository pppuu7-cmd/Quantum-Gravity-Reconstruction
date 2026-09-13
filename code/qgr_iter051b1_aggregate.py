#!/usr/bin/env python3
import glob, json, os, sys

files = sorted(glob.glob('artifacts/**/lane-*.json', recursive=True))
rows = []
parse_errors = []
for path in files:
    try:
        with open(path, 'r', encoding='utf-8-sig') as f:
            text = f.read().strip().splitlines()
        if not text:
            raise ValueError('empty artifact')
        rows.append(json.loads(text[-1]))
    except Exception as exc:
        parse_errors.append({'path': path, 'error': repr(exc)})

expected = 8
valid = [r for r in rows if r.get('valid') is True]
passed = [r for r in rows if r.get('pass') is True]
structurally_complete = len(rows) == expected and len({r.get('lane') for r in rows}) == expected and not parse_errors

if not structurally_complete:
    status = 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_G51B1'
elif len(valid) == expected and len(passed) == expected:
    status = 'PASS_SCOPED_WEYL3_P_INSERTION_CERTIFICATE'
else:
    status = 'SCIENTIFIC_FAIL_G51B1_WEYL3_P_INSERTION_CERTIFICATE'

summary = {
    'gate': 'ITER051B1-WEYL3-P-INSERTION-CERTIFICATE',
    'scientific_status': status,
    'expected_lanes': expected,
    'artifact_rows': len(rows),
    'valid_count': len(valid),
    'passed_count': len(passed),
    'parse_errors': parse_errors,
    'frozen_thresholds': {
        'input_algebraic_max': 1e-11,
        'input_weyl_trace_max': 1e-10,
        'P_algebraic_max': 2e-11,
        'heldout_direction_max': 2e-10,
        'euler_relative_max': 2e-10,
        'P_covariance_relative_max': 2e-9,
        'scalar_covariance_relative_max': 1e-10,
        'conformally_flat_I3_max': 1e-11,
        'conformally_flat_P_norm_max': 2e-10,
        'nonzero_I3_min': 1e-7,
        'nonzero_P_norm_min': 1e-6,
    },
}

if rows:
    summary['worst'] = {
        'input_algebraic': max(float(r.get('input_algebraic_residual', float('inf'))) for r in rows),
        'input_weyl_trace': max(float(r.get('input_weyl_trace_residual', float('inf'))) for r in rows),
        'P_algebraic': max(float(r.get('P_algebraic_residual', float('inf'))) for r in rows),
        'heldout_direction': max(max(map(float, r.get('heldout_direction_residuals', [float('inf')]))) for r in rows),
        'euler_relative': max(float(r.get('euler_relative_residual', float('inf'))) for r in rows),
        'P_covariance_relative': max(max(map(float, r.get('P_covariance_residuals', [float('inf')]))) for r in rows),
        'scalar_covariance_relative': max(max(map(float, r.get('scalar_covariance_residuals', [float('inf')]))) for r in rows),
        'conformally_flat_I3': max(float(r.get('conformally_flat_I3', float('inf'))) for r in rows),
        'conformally_flat_P_norm': max(float(r.get('conformally_flat_P_norm', float('inf'))) for r in rows),
        'min_abs_I3': min(abs(float(r.get('I3', 0.0))) for r in rows),
        'min_P_norm': min(float(r.get('P_norm', 0.0)) for r in rows),
    }

with open('iter051b1-summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, sort_keys=True)
print(json.dumps(summary, indent=2, sort_keys=True))

if status == 'INFRASTRUCTURE_OR_NUMERICAL_FAIL_G51B1':
    sys.exit(2)
