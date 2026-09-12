#!/usr/bin/env python3
import glob,json,os
files=glob.glob('iter017-g17-results/**/result.json',recursive=True)
recs=[json.load(open(f)) for f in files]
audits=('kinematic-measure','flat-family','history-authority','authority-rank')
expected={(a,l) for a in audits for l in range(6)}
seen={(r['audit'],r['lane']) for r in recs}
assert seen==expected,(len(seen),sorted(expected-seen),sorted(seen-expected))
assert all(r.get('passed') is True for r in recs)
meas=[r for r in recs if r['audit']=='kinematic-measure']
flat=[r for r in recs if r['audit']=='flat-family']
hist=[r for r in recs if r['audit']=='history-authority']
rank=[r for r in recs if r['audit']=='authority-rank']
assert {r['total_measure_power'] for r in meas}=={'0'}
assert {r['two_derivative_local_action'] for r in flat}=={'0'}
assert {r['completeness'] for r in hist}=={'1'}
assert {r['authority_rank_on_log_r'] for r in rank}=={0}
assert {r['r_nullity'] for r in rank}=={1}
out={
 'gate':'QGR-ITER017-G17-COMMON-EVENT-CHARACTER-R-AUTHORITY-FROM-INCIDENCE-SECOND-MOMENT-OR-STOP',
 'parallel_lanes':24,'aggregate_success':True,'c6_fixed':False,'r_fixed':False,
 'classification':'BLOCKED_SCOPED_COMMON_EVENT_CHARACTER_R_IS_NOT_FIXED_BY_THE_EXISTING_ZERO_EVENT_INCIDENCE_SEED_SCALE_INVARIANT_KINEMATIC_MEASURE_CONSTANT_FLAT_TWO_DERIVATIVE_ACTION_OR_EQUAL_HISTORY_NORMALIZATION',
 'strongest_positive':'The remaining ambiguity has been reduced to one scalar r, and its immediate authority audit is exact: dmu is scale invariant, every constant G=r^2 C endpoint is flat with zero local action on the zero-cosmological branch, and 24-history completeness is r-blind.',
 'strongest_blocker':'The four currently available constant-family authority rows have rank zero on log r. Any further attempt to fix r must derive a nonconstant microscopic event profile/action or a genuinely new same-realization quantum/matter relation; choosing r by convention or fit is forbidden.',
 'stop_decision':'STOP_IMMEDIATE_INCIDENCE_SECOND_MOMENT_NORMALIZATION_ROUTE_FOR_R__DO_NOT_REPEAT_SCALE_SYMMETRY_TESTS',
 'next_gate':'QGR-ITER017-G18-DERIVE-NONCONSTANT-MICROSCOPIC-EVENT-PROFILE-FROM-BOOLEAN-REFINEMENT-OR-PROVE-NONUNIQUENESS',
 'claim_locks':['r fixed = NO','finite pair/triple coherent amplitudes derived = NO','c6 fixed = NO','constant-family rank zero is not a global no-go for all future microscopic profiles','KMQGB D7 remains open and NEW_REQUIRED unauthorized']
}
os.makedirs('iter017-g17-summary',exist_ok=True)
with open('iter017-g17-summary/summary.json','w') as f:json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
