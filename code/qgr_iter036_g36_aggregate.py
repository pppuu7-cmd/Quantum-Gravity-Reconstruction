#!/usr/bin/env python3
"""Aggregate QGR Iter036 frozen 48-lane persistence gate."""
import glob,json,os,sys
from collections import defaultdict

EXPECTED=48

def main():
    paths=glob.glob('iter036-g36-results/**/result.json',recursive=True)
    rows=[]
    for p in paths:
        try:
            with open(p,encoding='utf-8') as f: rows.append(json.load(f))
        except Exception:
            pass
    seen={(r.get('mode'),r.get('seed_index'),r.get('param_index')) for r in rows}
    by=defaultdict(lambda:defaultdict(dict))
    for r in rows:
        by[r.get('seed_index')][r.get('mode')][r.get('param_index')]=r
    amp_persistent=[]; ref_persistent=[]; joint=[]
    for seed in range(8):
        arows=[by[seed]['amplitude'].get(i) for i in range(3)]
        rrows=[by[seed]['refine'].get(i) for i in range(3)]
        ap=all(x is not None and x.get('reference_controls_valid') and x.get('verified_persistent_distinct_branch') for x in arows)
        rp=all(x is not None and x.get('reference_controls_valid') and x.get('verified_persistent_distinct_branch') for x in rrows)
        if ap: amp_persistent.append(seed)
        if rp: ref_persistent.append(seed)
        if ap and rp: joint.append(seed)
    controls_valid=sum(bool(r.get('reference_controls_valid')) for r in rows)
    passes=sum(bool(r.get('verified_persistent_distinct_branch')) for r in rows)
    complete=(len(seen)==EXPECTED)
    if not complete:
        classification='CONTROL_INVALID_OR_INCOMPLETE'
    elif joint:
        classification='SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_PERSISTS_ACROSS_BACKGROUND_AND_REFINEMENT_PROXY'
    elif amp_persistent or ref_persistent:
        classification='PARTIAL_SCOPED_PERSISTENCE_ONLY'
    elif controls_valid==EXPECTED:
        classification='NO_VERIFIED_PERSISTENT_BRANCH_IN_FROZEN_STRESS'
    else:
        classification='CONTROL_INVALID_OR_INCOMPLETE'
    summary={
        'gate':'ITER036-G36-EXPANDED-PATCH-PERSISTENCE',
        'expected_lanes':EXPECTED,'found_unique_lanes':len(seen),
        'reference_control_valid_lanes':controls_valid,
        'lane_passes':passes,
        'background_persistent_seed_indices':amp_persistent,
        'refinement_proxy_persistent_seed_indices':ref_persistent,
        'jointly_persistent_seed_indices':joint,
        'classification':classification,
        'claim_lock':'Finite 15-cell numerical persistence only. Refinement mode is a local shrinking-cell proxy, not the full projective refinement limit or a tower-wide/global theorem.'
    }
    os.makedirs('iter036-g36-summary',exist_ok=True)
    with open('iter036-g36-summary/summary.json','w',encoding='utf-8') as f:
        json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(summary,sort_keys=True))
    if not complete:
        sys.exit(2)

if __name__=='__main__':
    main()
