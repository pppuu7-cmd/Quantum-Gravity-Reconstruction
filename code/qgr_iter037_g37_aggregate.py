#!/usr/bin/env python3
"""Aggregate frozen QGR Iter037 G37 two-stream gate."""
import glob,json,os,sys
from collections import defaultdict

EXPECTED_DEEP=24
EXPECTED_RADIUS=12
EXPECTED=36


def main():
    paths=glob.glob('iter037-g37-results/**/result.json',recursive=True)
    rows=[]
    for p in paths:
        try:
            with open(p,encoding='utf-8') as f: rows.append(json.load(f))
        except Exception:
            pass
    seen={(r.get('stream'),r.get('seed_slot'),r.get('target_index')) for r in rows}
    by=defaultdict(lambda:defaultdict(dict))
    for r in rows:
        by[r.get('seed_slot')][r.get('stream')][r.get('target_index')]=r
    deep_seq=[]; radius_seq=[]; joint=[]
    for slot in range(6):
        ds=[by[slot]['deep'].get(i) for i in range(4)]
        rs=[by[slot]['radius'].get(i) for i in range(2)]
        dp=all(x is not None and x.get('reference_controls_valid') and x.get('lane_pass') for x in ds)
        rp=all(x is not None and x.get('reference_controls_valid') and x.get('lane_pass') for x in rs)
        if dp: deep_seq.append(slot)
        if rp: radius_seq.append(slot)
        if dp and rp: joint.append(slot)
    controls=sum(bool(r.get('reference_controls_valid')) for r in rows)
    passes=sum(bool(r.get('lane_pass')) for r in rows)
    deep_rows=[r for r in rows if r.get('stream')=='deep']
    radius_rows=[r for r in rows if r.get('stream')=='radius']
    complete=(len(seen)==EXPECTED and len(deep_rows)==EXPECTED_DEEP and len(radius_rows)==EXPECTED_RADIUS)
    if not complete:
        classification='CONTROL_INVALID_OR_INCOMPLETE'
    elif joint:
        classification='SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_SURVIVES_DEEPER_REFINEMENT_AND_RADIUS4_PATH_CONSISTENCY'
    elif deep_seq or radius_seq:
        classification='PARTIAL_SCOPED_DEEP_REFINEMENT_OR_RADIUS_PERSISTENCE_ONLY'
    elif controls==EXPECTED:
        classification='NO_FULL_SEQUENCE_PASS_IN_FROZEN_G37_STRESS'
    else:
        classification='CONTROL_INVALID_OR_INCOMPLETE'
    # Diagnostic envelopes only; they do not promote the terminal class.
    mins_ref=[]; mins_cand=[]; hids=[]; fps=[]; parent_dis=[]
    for r in rows:
        if r.get('stream')=='deep':
            for key,dst in [('reference_jacobian',mins_ref),('candidate_jacobian',mins_cand)]:
                v=(r.get(key) or {}).get('min_singular')
                if isinstance(v,(int,float)): dst.append(v)
            for key,dst in [('expanded_holonomy_invariant_distance',hids),('edge_fingerprint_distance',fps)]:
                v=r.get(key)
                if isinstance(v,(int,float)): dst.append(v)
        else:
            for key in ('reference_max_parent_transport_disagreement','candidate_max_parent_transport_disagreement'):
                v=r.get(key)
                if isinstance(v,(int,float)): parent_dis.append(v)
    summary={
        'gate':'ITER037-G37-DEEP-REFINEMENT-AND-RADIUS-GROWTH',
        'expected_lanes':EXPECTED,'found_unique_lanes':len(seen),
        'reference_control_valid_lanes':controls,'lane_passes':passes,
        'deep_refinement_sequence_pass_seed_slots':deep_seq,
        'radius4_sequence_pass_seed_slots':radius_seq,
        'joint_sequence_pass_seed_slots':joint,
        'minimum_reference_origin_jacobian_singular_value':min(mins_ref) if mins_ref else None,
        'minimum_candidate_origin_jacobian_singular_value':min(mins_cand) if mins_cand else None,
        'minimum_resolved_deep_holonomy_distance':min(hids) if hids else None,
        'minimum_deep_edge_fingerprint_distance':min(fps) if fps else None,
        'maximum_observed_parent_transport_disagreement':max(parent_dis) if parent_dis else None,
        'classification':classification,
        'claim_lock':'Scoped finite numerical stress only: h is a shrinking-cell proxy and R<=4 is a finite positive-orthant patch; no continuum/global theorem is established.'
    }
    os.makedirs('iter037-g37-summary',exist_ok=True)
    with open('iter037-g37-summary/summary.json','w',encoding='utf-8') as f:
        json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(summary,sort_keys=True))
    if not complete: sys.exit(2)

if __name__=='__main__':
    main()
