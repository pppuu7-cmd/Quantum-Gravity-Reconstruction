#!/usr/bin/env python3
"""Supplemental Iter057Y Actions reproduction with corrected frozen-V metadata validation.

This wrapper does not change any response/source coefficients or scientific decision
rules. It repairs only the provenance predicate: the canonical frozen Iter057V data
file predates the `terminal_commit` metadata field and instead carries the terminal
classification plus exact production head/run/job/artifact/digest/ranks.
"""
import argparse
import json
from pathlib import Path

import qgr_iter057y_onshell_q2_q4_q6_q8_response as y

V_CLASSIFICATION = (
    'PASS_SCOPED_ITER057V_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_RESPONSE_'
    'MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_FOURTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN'
)
V_PRODUCTION_HEAD = '723598530f1c42cdc12eef25cd3e6fe169e807dd'
V_RUN = 35017363408
V_JOB = 104544061621
V_ARTIFACT = 10416157241

_original_consume = y.consume_authorities


def consume_authorities_corrected():
    q, source, _, sub = _original_consume()
    v = json.loads(y.V_PATH.read_text())
    sub['V'] = (
        v.get('source_digest') == y.V_DIGEST
        and v.get('classification') == V_CLASSIFICATION
        and v.get('production_head') == V_PRODUCTION_HEAD
        and v.get('source_run') == V_RUN
        and v.get('source_job') == V_JOB
        and v.get('source_artifact') == V_ARTIFACT
        and len(v.get('Q6_particular_normalized', [])) == 88
        and v.get('rank_M') == 494
        and v.get('rank_augmented') == 494
    )
    return q, source, all(sub.values()), sub


y.consume_authorities = consume_authorities_corrected


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out')
    args = ap.parse_args()
    obj = y.compute()
    obj['supplemental_reproduction_note'] = (
        'Corrected only Iter057V provenance metadata validation; scientific inputs, '
        'coefficients, affine system, solve and replay are unchanged.'
    )
    text = json.dumps(obj, indent=2, sort_keys=True) + '\n'
    if args.out:
        p = Path(args.out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    print(json.dumps({
        'pass': obj['pass'],
        'classification': obj['classification'],
        'authority_subcontrols': obj.get('authority_subcontrols'),
        'matrix_shape': obj['matrix_shape'],
        'rank_M': obj['rank_M'],
        'rank_augmented': obj['rank_augmented'],
        'compatibility_nonzero_count': obj['compatibility_nonzero_count'],
        'Q8_particular_nonzero_count': obj['Q8_particular_nonzero_count'],
        'reduced_DG_minus_source_nonzero_component_count': obj['reduced_DG_minus_source_nonzero_component_count'],
        'unreduced_DG_minus_source_nonzero_component_count': obj['unreduced_DG_minus_source_nonzero_component_count'],
    }, indent=2))
    if not obj['pass']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
