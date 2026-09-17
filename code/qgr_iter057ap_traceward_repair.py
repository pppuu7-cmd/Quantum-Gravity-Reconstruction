#!/usr/bin/env python3
"""Target-blind execution/control repair for Iter057AP trace Ward sign.

Parent scientific object and constructor are frozen by preregistration
6de62a559381a7c86e01c58a62ea7d8c91606884. This wrapper changes no source
coefficient formula and opens no Iter057U/X target data. It independently
replays the constructor and validates the correct d=4 covariant-metric trace
identity g^{ab} Shat_ab + I3 = 0.
"""
import argparse, json
from pathlib import Path
from itertools import product

import qgr_iter057ap_independent_covariant_source_repair as r

m = r.m


def corrected_compute():
    d = m.compute()

    # Independent exact replay of the trace identity from constructor primitives.
    g, _, _, _ = m.seed_metric10()
    gi, Gamma, Rlow, Ric, Scal, Ein, C, invok = m.geometry8(g)
    Cup = m.raise_last(C, gi, 8)
    I, Q = m.cubic_and_Q(C, Cup, 6)
    P, Plow = m.p_from_frechet_projection(g, gi, C, Cup, Q, 8)
    Eup, Shat, U, T, A = m.ao_source(g, gi, Gamma, Rlow, P, I)

    tr = {}
    for a, b in product(range(m.N), repeat=2):
        tr = m.add(tr, m.mul(gi[a][b], Shat[a][b], 6))
    trace_plus_I_zero = not m.trunc(m.add(tr, I), 6)

    controls = dict(d['controls'])
    old = controls.pop('E_trace_Ward_trace_Shat_minus_I3_zero', None)
    controls['E_trace_Ward_trace_Shat_plus_I3_zero'] = bool(trace_plus_I_zero)
    controls['E_trace_Ward_old_minus_identity_rejected'] = (old is False)
    d['controls'] = controls
    d['trace_ward_repair'] = {
        'defect_record_commit': '92eb386bffe25d8781b1e62a1426703970bb7a73',
        'old_minus_control_was_false': old is False,
        'correct_plus_control_exact': bool(trace_plus_I_zero),
        'target_coefficients_loaded': False,
    }
    d['classification'] = (
        'CONSTRUCTOR_EXACT_FROZEN__NO_TARGET_COMPARISON_YET'
        if all(controls.values()) else
        'INVALID_ITER057AP_CONSTRUCTOR_CONTROL_FAILURE'
    )
    q = dict(d)
    q.pop('source_slots', None)
    q.pop('source_sparse', None)
    q.pop('complete_payload_sha256', None)
    q.pop('scientific_summary_sha256', None)
    d['scientific_summary_sha256'] = m.phash(q)
    d.pop('complete_payload_sha256', None)
    d['complete_payload_sha256'] = m.phash(d)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    d = corrected_compute()
    p = Path(a.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, sort_keys=True, indent=2) + '\n')
    print(json.dumps({k:v for k,v in d.items() if k not in ('source_slots','source_sparse')}, sort_keys=True, indent=2))
    return 0 if all(d['controls'].values()) else 2


if __name__ == '__main__':
    raise SystemExit(main())
