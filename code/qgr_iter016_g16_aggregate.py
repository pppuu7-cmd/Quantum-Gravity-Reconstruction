#!/usr/bin/env python3
import glob,json,os
files=glob.glob('iter016-g16-results/**/result.json',recursive=True)
recs=[json.load(open(f)) for f in files]
audits=('character-composition','history-order','scale-nonuniqueness','amplitude-sensitivity')
expected={(a,l) for a in audits for l in range(6)}
seen={(r['audit'],r['lane']) for r in recs}
assert seen==expected,(len(seen),sorted(expected-seen),sorted(seen-expected))
assert all(r.get('passed') is True for r in recs)
char=[r for r in recs if r['audit']=='character-composition']
hist=[r for r in recs if r['audit']=='history-order']
non=[r for r in recs if r['audit']=='scale-nonuniqueness']
amp=[r for r in recs if r['audit']=='amplitude-sensitivity']
assert all(r['multiplicative_composition_exact'] and r['s4_common_generator_value'] for r in char)
assert {r['distinct_final_G'] for r in hist}=={1}
assert {r['history_weight_sum'] for r in hist}=={'1'}
assert all(r['distinct_final_G'] and r['both_composition_exact'] for r in non)
assert all(r['history_weight_sum']=='1' for r in amp)
out={
 'gate':'QGR-ITER016-G16-MICROSCOPIC-FINITE-PROFILE-ACTION-FROM-BOOLEAN-CELL-COMPOSITION',
 'parallel_lanes':24,'aggregate_success':True,'c6_fixed':False,
 'classification':'PARTIAL_SCOPED_BOOLEAN_REFINEMENT_COMPOSITION_PLUS_S4_REDUCES_THE_GENERATOR_LOCAL_FRAME_RESCALE_AMBIGUITY_TO_ONE_COMMON_MULTIPLICATIVE_CHARACTER_R__BUT_R_REMAINS_UNFIXED_AND_THE_REQUIRED_FINITE_PAIR_TRIPLE_COHERENT_AMPLITUDES_ARE_NOT_DERIVED',
 'strongest_positive':'Under the explicitly scoped repeated-event refinement composition hypothesis, s(n+m)=s(n)s(m), unit normalization and S4 force the four generator-local rescalings into a one-parameter common character s_i(n)=r^n. All 24 Boolean orderings share the same endpoint for every r.',
 'strongest_blocker':'Different exact rational r satisfy all tested composition, S4 and history-normalization rules but produce distinct G endpoints and distinct finite profile/pair/triple scales. No existing authority equation selects r, so the microscopic amplitude scale remains a genuine UV datum.',
 'next_gate':'QGR-ITER017-G17-COMMON-EVENT-CHARACTER-R-AUTHORITY-FROM-INCIDENCE-SECOND-MOMENT-OR-STOP',
 'claim_locks':['repeated-event character law is a refinement-composition hypothesis, not a primitive Boolean-cell theorem','r fixed = NO','finite pair/triple coherent amplitudes derived = NO','c6 fixed = NO','BLOCKED is not candidate FAIL']
}
os.makedirs('iter016-g16-summary',exist_ok=True)
with open('iter016-g16-summary/summary.json','w') as f:json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
