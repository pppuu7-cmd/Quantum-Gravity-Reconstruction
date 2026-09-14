#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path
import sympy as sp

GATE = 'ITER054F-WEYL3-MIXED-ORDER-STRONG-HYPERBOLICITY-OBJECT-DEFINITION-AUDIT'
PREREG = 'f4838c50ded00c6d62c9ef822f1f75285eceddf9'
SOURCE_LOCK = PREREG
BLOCKED_CLASS = 'BLOCKED_OBJECT_DEFINITION_ITER054F_MIXED_ORDER_EVOLUTION_REDUCTION_NOT_FIXED'
READY_CLASS = 'ITER054F_EVOLUTION_OBJECT_DEFINED_READY_FOR_SEPARATE_STRONG_HYPERBOLICITY_GATE'
INVALID_CLASS = 'INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER054F'

FROZEN_SOURCES = [
    'recovery/state.json',
    'recovery/CURRENT_FRONT.md',
    'prereg/ITER054D-WEYL3-PRINCIPAL-ORDER-GAUGE-FIXING-CHARACTERISTIC-AUDIT.md',
    'results/ITER054D_TERMINAL_RESULT.md',
    'prereg/ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT.md',
    'results/ITER054E_TERMINAL_RESULT.md',
]

REQUIRED_FIELDS = [
    'state_vector_or_reduction_variables',
    'time_direction_and_spatial_covector_domain',
    'first_order_in_time_or_equivalent_higher_order_formulation',
    'principal_evolution_matrix_or_equivalent',
    'gauge_variables_and_gauge_evolution_equations',
    'constraint_variables_and_principal_constraint_propagation',
    'norm_or_symmetrizer_and_open_domain',
    'map_to_mixed_einstein_weyl3_and_gr_limit',
]


def locked_text(path):
    return subprocess.check_output(
        ['git', 'show', f'{SOURCE_LOCK}:{path}'], text=True
    )


def stream_a0():
    texts = {}
    errors = []
    for path in FROZEN_SOURCES:
        try:
            texts[path] = locked_text(path)
        except Exception as ex:
            errors.append(f'{path}:{type(ex).__name__}:{ex}')
    if errors:
        return {
            'stream': 'A0', 'gate': GATE, 'valid': False,
            'outcome': 'INVALID_PROVENANCE', 'errors': errors,
            'source_lock': SOURCE_LOCK,
        }

    state = json.loads(texts['recovery/state.json'])
    front = texts['recovery/CURRENT_FRONT.md']
    d_prereg = texts['prereg/ITER054D-WEYL3-PRINCIPAL-ORDER-GAUGE-FIXING-CHARACTERISTIC-AUDIT.md']
    d_result = texts['results/ITER054D_TERMINAL_RESULT.md']
    e_prereg = texts['prereg/ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT.md']
    e_result = texts['results/ITER054E_TERMINAL_RESULT.md']

    explicit_blocker = (
        state.get('active_blocker') == 'STRONG_HYPERBOLICITY_EVOLUTION_OBJECT_NOT_YET_DEFINED_OR_CERTIFIED'
        and state.get('claim_locks', {}).get('strong_hyperbolicity_evolution_object_defined') is False
        and 'complete mixed-order first-order evolution reduction' in front
        and 'not established' in front
    )

    prior_scope_lock = all([
        'strong hyperbolicity' in d_prereg.lower(),
        'constraint propagation' in d_prereg.lower(),
        'strong hyperbolicity' in d_result.lower(),
        'full tensor' in e_prereg.lower(),
        'symmetrizer' in e_prereg.lower(),
        'strong hyperbolicity' in e_result.lower(),
    ])

    missing = list(REQUIRED_FIELDS) if explicit_blocker and prior_scope_lock else []
    outcome = 'BLOCKED_OBJECT_DEFINITION' if missing else 'OBJECT_DEFINED'
    return {
        'stream': 'A0', 'gate': GATE, 'valid': True,
        'outcome': outcome,
        'source_lock': SOURCE_LOCK,
        'frozen_sources': FROZEN_SOURCES,
        'explicit_blocker_confirmed': bool(explicit_blocker),
        'prior_scope_lock_confirmed': bool(prior_scope_lock),
        'required_field_count': len(REQUIRED_FIELDS),
        'missing_fields': missing,
        'interpretation': 'authority census only; no preferred evolution reduction is constructed',
    }


def stream_a1():
    mu, v = sp.symbols('mu v', real=True)
    A_diag = sp.Matrix([[v, 0], [0, v]])
    A_j = sp.Matrix([[v, 1], [0, v]])
    cp_diag = sp.expand((mu*sp.eye(2) - A_diag).det())
    cp_j = sp.expand((mu*sp.eye(2) - A_j).det())
    target = sp.expand((mu - v)**2)
    same_poly = sp.simplify(cp_diag - cp_j) == 0 and sp.simplify(cp_diag - target) == 0
    eigdim_diag = len((A_diag - v*sp.eye(2)).nullspace())
    eigdim_j = len((A_j - v*sp.eye(2)).nullspace())
    diag_ok = eigdim_diag == 2 and A_diag.is_diagonalizable(reals_only=True)
    jordan_defective = eigdim_j == 1 and not A_j.is_diagonalizable(reals_only=True)
    real_root = bool(v.is_real)
    valid = bool(same_poly and diag_ok and jordan_defective and real_root)
    return {
        'stream': 'A1', 'gate': GATE, 'valid': valid,
        'same_characteristic_polynomial': bool(same_poly),
        'characteristic_polynomial': str(cp_diag),
        'only_eigenvalue_symbol': str(v),
        'eigenvalue_real_assumption': real_root,
        'diag_eigenspace_dimension': eigdim_diag,
        'jordan_eigenspace_dimension': eigdim_j,
        'diagonalizable_control': bool(diag_ok),
        'defective_jordan_control': bool(jordan_defective),
        'logical_consequence': 'real characteristic roots/polynomial alone do not imply diagonalizability or strong hyperbolicity',
    }


def stream_b0():
    A = sp.Matrix([[0, 1], [1, 0]])
    H = sp.eye(2)
    eigvals = sorted([sp.simplify(x) for x in A.eigenvals().keys()], key=str)
    eigvec_count = sum(len(vs) for _, _, vs in A.eigenvects())
    h_pos = H.is_positive_definite is True
    symmetric = (H*A - (H*A).T) == sp.zeros(2)
    diagonalizable = A.is_diagonalizable(reals_only=True)
    valid = bool(set(eigvals) == {sp.Integer(-1), sp.Integer(1)} and eigvec_count == 2 and h_pos and symmetric and diagonalizable)
    return {
        'stream': 'B0', 'gate': GATE, 'valid': valid,
        'eigenvalues': [str(x) for x in eigvals],
        'independent_eigenvector_count': int(eigvec_count),
        'H_positive_definite': bool(h_pos),
        'H_times_A_symmetric': bool(symmetric),
        'nondefective': bool(diagonalizable),
        'interpretation': 'detector positive control only; not a QGR claim',
    }


def stream_b1():
    locks = {
        'strong_hyperbolicity_established': False,
        'well_posedness_established': False,
        'energy_positivity_established': False,
        'constraint_propagation_established': False,
        'physical_mode_count_established': False,
        'ghost_or_residue_sign_established': False,
        'quantum_unitarity_established': False,
        'quantum_amplitude_measure_authorized': False,
        'uv_complete': False,
        'full_gr_recovery_established': False,
        'experimentally_confirmed': False,
        'new_physics_found': False,
        'c6_fixed': False,
        'beta_equal_one_authorized': False,
        'theory_established_pct': 0,
    }
    valid = all(v is False for k, v in locks.items() if k != 'theory_established_pct') and locks['theory_established_pct'] == 0
    return {
        'stream': 'B1', 'gate': GATE, 'valid': bool(valid),
        'claim_locks': locks,
        'interpretation': 'fail-closed authority boundary; object-definition result is not hyperbolicity or physical-spectrum evidence',
    }


def run_stream(name):
    return {'A0': stream_a0, 'A1': stream_a1, 'B0': stream_b0, 'B1': stream_b1}[name]()


def aggregate(root):
    rows = []
    parse_errors = []
    for path in sorted(Path(root).rglob('*.json')):
        try:
            rows.append(json.loads(path.read_text()))
        except Exception as ex:
            parse_errors.append(f'{path}:{type(ex).__name__}:{ex}')
    by = {r.get('stream'): r for r in rows if r.get('stream') in {'A0','A1','B0','B1'}}
    missing = sorted({'A0','A1','B0','B1'} - set(by))
    controls_valid = not missing and not parse_errors and all(by[s].get('valid') is True for s in ['A0','A1','B0','B1'])
    if not controls_valid:
        classification = INVALID_CLASS
        terminal_valid = False
    elif by['A0'].get('outcome') == 'BLOCKED_OBJECT_DEFINITION':
        classification = BLOCKED_CLASS
        terminal_valid = True
    elif by['A0'].get('outcome') == 'OBJECT_DEFINED':
        classification = READY_CLASS
        terminal_valid = True
    else:
        classification = INVALID_CLASS
        terminal_valid = False
    return {
        'gate': GATE,
        'classification': classification,
        'terminal_valid': bool(terminal_valid),
        'scientific_pass': False,
        'source_lock': SOURCE_LOCK,
        'preregistration_commit': PREREG,
        'found_streams': sorted(by),
        'missing_streams': missing,
        'parse_errors': parse_errors,
        'stream_valid': {s: by[s].get('valid') for s in by},
        'object_outcome': by.get('A0', {}).get('outcome'),
        'missing_object_fields': by.get('A0', {}).get('missing_fields', []),
        'interpretation_lock': 'OBJECT-DEFINITION/LOGICAL-SUFFICIENCY AUDIT ONLY; NO STRONG-HYPERBOLICITY, WELL-POSEDNESS, PHYSICAL-SPECTRUM OR QUANTUM CLAIM',
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stream', choices=['A0','A1','B0','B1'])
    ap.add_argument('--aggregate')
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    data = aggregate(args.aggregate) if args.aggregate else run_stream(args.stream)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2, sort_keys=True))
    print(json.dumps(data, sort_keys=True))
    if args.aggregate and not data.get('terminal_valid', False):
        raise SystemExit(2)
    if not args.aggregate and not data.get('valid', False):
        raise SystemExit(2)

if __name__ == '__main__':
    main()
