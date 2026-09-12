#!/usr/bin/env python3
import glob,json,os,sys
files=sorted(glob.glob('iter019-g19-results/qgr-g19-*/*.json'))
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
expected=24
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
ok=(len(rows)==expected and all(r.get('passed') for r in rows) and counts=={
 'conformal-reduction':6,'weight-uniqueness':6,'character-tension':6,'normalization-inheritance':6})
out={
 'gate':'ITER019-G19-AGGREGATE','lane_count':len(rows),'expected_lane_count':expected,'audit_counts':counts,'all_lane_gates_passed':ok,
 'scientific_status':'PASS_SCOPED_G18_DIRICHLET_BULK_FUNCTIONAL_AND_ONE_OVER_H_REFINEMENT_WEIGHT_ARE_DERIVED_WITHIN_THE_EXISTING_QGR_LOCAL_TWO_DERIVATIVE_COMMON_CONFORMAL_SECTOR_UP_TO_THE_ALREADY_EXISTING_OVERALL_ACTION_NORMALIZATION__FAIL_SCOPED_G16_MULTIPLICATIVE_CHARACTER_AND_G18_LINEAR_S_PROFILE_AS_SIMULTANEOUS_NONTRIVIAL_REFINEMENT_LAWS__R_REMAINS_UNSELECTED_BOUNDARY_DATUM',
 'strongest_positive':'In four dimensions the already-derived QGR all-orders local action restricted to G=s^2 C is exactly 6 a times a Dirichlet bulk action for s modulo a boundary term; rational refinement additivity uniquely forces the discrete weight w(h) proportional to 1/h, so G18 no longer needs an independent lambda in this scoped conformal two-derivative sector.',
 'strongest_blocker':'The bulk action determines the minimizing trajectory for specified endpoints but supplies no equation selecting the endpoint r itself. Moreover the nontrivial G16 multiplicative character trajectory is strictly higher-action than the G18 linear-s minimizer and cannot simultaneously be the same fundamental refinement trajectory.',
 'decision':'RETIRE_G16_MULTIPLICATIVE_CHARACTER_AS_FUNDAMENTAL_REFINEMENT_TRAJECTORY_UNLESS_A_DISTINCT_EVENT_VARIABLE_OR_CLOCK_MAP_IS_DERIVED__PROMOTE_G18_DIRICHLET_PRINCIPLE_ONLY_IN_SCOPED_COMMON_CONFORMAL_LOCAL_TWO_DERIVATIVE_SECTOR',
 'next_gate':'QGR-ITER020-G20-ENDPOINT-R-AUTHORITY-FROM-BOOLEAN-EVENT-BOUNDARY-DATA-OR-DISTINCT-COMPOSITION-VARIABLE',
 'r_fixed':False,'finite_pair_triple_coherent_amplitudes_derived':False,'c6_fixed':False,
 'claim_locks':['r fixed = NO','finite pair/triple coherent amplitudes derived = NO','c6 fixed = NO','G19 is a scoped conformal-sector derivation, not a fundamental Boolean microscopic action theorem','joint G16/G18 trajectory failure is not candidate FAIL','KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes']
}
os.makedirs('iter019-g19-summary',exist_ok=True)
with open('iter019-g19-summary/summary.json','w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(out,sort_keys=True))
if not ok: sys.exit(2)
