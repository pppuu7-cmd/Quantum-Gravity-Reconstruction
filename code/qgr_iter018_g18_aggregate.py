#!/usr/bin/env python3
import glob,json,os

paths=glob.glob('iter018-g18-results/**/result.json',recursive=True)
rows=[]
for p in paths:
    with open(p) as f: rows.append(json.load(f))
expected=24
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
all_pass=(len(rows)==expected and all(r.get('passed') for r in rows) and counts=={'linear-profile':6,'strict-minimality':6,'s4-lift':6,'authority-rank':6})
summary={
  'gate':'ITER018-G18-AGGREGATE','lane_count':len(rows),'expected_lane_count':expected,'audit_counts':counts,
  'all_lane_gates_passed':all_pass,
  'scientific_status':('PASS_SCOPED_PROFILE_SEGMENTATION_OBSTRUCTION_CAN_BE_REMOVED_BY_A_CANDIDATE_REFINEMENT_CONSISTENT_DIRICHLET_VARIATIONAL_PRINCIPLE_BUT_COMMON_R_OR_NORMALIZATION_AUTHORITY_REMAINS_OPEN' if all_pass else 'FAIL'),
  'claim_lock':'This is an exact audit of a candidate discretized two-derivative refinement principle. It is not a derivation of that microscopic principle from QGR and does not fix the absolute event scale r.'
}
os.makedirs('iter018-g18-summary',exist_ok=True)
with open('iter018-g18-summary/summary.json','w') as f: json.dump(summary,f,indent=2,sort_keys=True)
print(json.dumps(summary,sort_keys=True))
if not all_pass: raise SystemExit(1)
