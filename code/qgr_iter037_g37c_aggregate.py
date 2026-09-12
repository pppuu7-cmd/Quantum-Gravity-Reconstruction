#!/usr/bin/env python3
"""Aggregate QGR Iter037 G37C prospective G10B same-realization audit."""
import glob,json,os,sys

EXPECTED=6

def main():
    paths=glob.glob('iter037-g37c-results/**/result.json',recursive=True)
    rows=[]
    for p in paths:
        try:
            with open(p,encoding='utf-8') as f: rows.append(json.load(f))
        except Exception:
            pass
    seen={r.get('seed_slot') for r in rows if isinstance(r.get('seed_slot'),int)}
    classes={
        'REFINEMENT_CONNECTED_MERGE_TO_PRINCIPAL_SCOPED':[],
        'FINITE_RESOLUTION_REFINEMENT_CONNECTED_DISTINCT_CANDIDATE':[],
        'DISTANT_BRANCH_FAILS_G10B_SAME_REALIZATION_ADMISSIBILITY_SCOPED':[],
        'BLOCKED_NUMERICALLY':[]
    }
    for r in rows:
        c=r.get('classification')
        if c in classes: classes[c].append(r.get('seed_slot'))
        else: classes['BLOCKED_NUMERICALLY'].append(r.get('seed_slot'))
    complete=(len(seen)==EXPECTED)
    distinct=classes['FINITE_RESOLUTION_REFINEMENT_CONNECTED_DISTINCT_CANDIDATE']
    blocked=classes['BLOCKED_NUMERICALLY']
    merge=classes['REFINEMENT_CONNECTED_MERGE_TO_PRINCIPAL_SCOPED']
    fail=classes['DISTANT_BRANCH_FAILS_G10B_SAME_REALIZATION_ADMISSIBILITY_SCOPED']
    controls=sum(bool(r.get('reference_controls_valid')) for r in rows)
    if not complete:
        classification='PARTIAL_BLOCKED_G10B_ADMISSIBILITY_AUDIT'
    elif distinct:
        classification='PARTIAL_SCOPED_PHYSICALLY_ADMISSIBLE_DISTINCT_CANDIDATE_REQUIRES_DEEPER_PROJECTIVE_LIMIT'
    elif not blocked and len(merge)+len(fail)==EXPECTED:
        classification='SCOPED_EVIDENCE_G35_G36_DISTANT_ROOTS_DO_NOT_YET_SUPPLY_ADDITIONAL_PHYSICAL_CONNECTION_BRANCHES_UNDER_FROZEN_G10B'
    else:
        classification='PARTIAL_BLOCKED_G10B_ADMISSIBILITY_AUDIT'
    final_errors=[]; path_dists=[]
    for r in rows:
        sr=r.get('scaling_rows') or []
        if sr and isinstance(sr[-1].get('candidate_scaled_linear_error'),(int,float)):
            final_errors.append(sr[-1]['candidate_scaled_linear_error'])
        v=r.get('candidate_principal_path_distance_N32')
        if isinstance(v,(int,float)): path_dists.append(v)
    summary={
        'gate':'ITER037-G37C-G10B-SAME-REALIZATION-ADMISSIBILITY',
        'expected_seeds':EXPECTED,'found_unique_seeds':len(seen),'reference_control_valid_seeds':controls,
        'merge_to_principal_seed_slots':sorted(x for x in merge if isinstance(x,int)),
        'finite_resolution_refinement_connected_distinct_seed_slots':sorted(x for x in distinct if isinstance(x,int)),
        'fails_g10b_same_realization_seed_slots':sorted(x for x in fail if isinstance(x,int)),
        'numerically_blocked_seed_slots':sorted(x for x in blocked if isinstance(x,int)),
        'minimum_final_scaled_linear_error':min(final_errors) if final_errors else None,
        'maximum_final_scaled_linear_error':max(final_errors) if final_errors else None,
        'minimum_candidate_principal_path_distance_N32':min(path_dists) if path_dists else None,
        'maximum_candidate_principal_path_distance_N32':max(path_dists) if path_dists else None,
        'classification':classification,
        'claim_lock':'Prospective G10B finite numerical audit only; no finite sequence proves an asymptotic continuum theorem.'
    }
    os.makedirs('iter037-g37c-summary',exist_ok=True)
    with open('iter037-g37c-summary/summary.json','w',encoding='utf-8') as f:
        json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(summary,sort_keys=True))
    if not complete: sys.exit(2)

if __name__=='__main__': main()
