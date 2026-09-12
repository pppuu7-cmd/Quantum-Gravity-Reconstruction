#!/usr/bin/env python3
import glob,json,os,sys
paths=sorted(glob.glob('iter035-g35-results/**/result.json',recursive=True))
expected=24
rows=[]
for p in paths:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
controls_ok=(len(rows)==expected and all(r.get('reference_neighbor_extension_successes')==4 and r.get('reference_holonomy_available') for r in rows))
verified=[r for r in rows if r.get('verified_patch_distinct_branch') is True]
origin_candidates=[r for r in rows if r.get('origin_solver_success') is True]
if not controls_ok:
    cls='CONTROL_INVALID'
elif verified:
    cls='SCIENTIFIC_PASS_SCOPED_DISTINCT_EXTENDABLE_BRANCH_COUNTEREXAMPLE'
else:
    cls='NO_VERIFIED_DISTINCT_PATCH_IN_FROZEN_SCAN'
summary={
 'gate':'ITER035-G35-DISTANT-BRANCH-VERIFICATION',
 'expected_lanes':expected,'found_lanes':len(rows),'reference_controls_valid':controls_ok,
 'origin_residual_qualified_candidates':len(origin_candidates),
 'verified_distinct_extendable_patches':len(verified),
 'verified_lane_scale_pairs':[[r.get('lane'),r.get('scale_index'),r.get('start_scale')] for r in verified],
 'classification':cls,
 'claim_lock':'Scoped finite-patch numerical result only; not a global branch-count/nonuniqueness theorem.'
}
os.makedirs('iter035-g35-summary',exist_ok=True)
with open('iter035-g35-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(summary,sort_keys=True))
if not controls_ok: sys.exit(2)
