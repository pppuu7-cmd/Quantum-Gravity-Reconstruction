#!/usr/bin/env python3
import glob,json,os
rows=[]
for p in glob.glob('iter034-g34-results/**/result.json',recursive=True):
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
large=[r for r in rows if r.get('mode')=='large-start']
cont=[r for r in rows if r.get('mode')=='background-continuation']
all_present=len(large)==6 and len(cont)==6 and len(rows)==12
large_trials=sum(len(r.get('starts',[])) for r in large)
large_converged=sum(r.get('converged_count',0) for r in large)
distinct=sum(r.get('distinct_transport_root_candidates',0) for r in large)
requested=sum(r.get('requested_steps',0) for r in cont)
completed=sum(r.get('completed_steps',0) for r in cont)
gaps=[r.get('minimum_observed_jacobian_gap') for r in cont if r.get('minimum_observed_jacobian_gap') is not None]
min_gap=min(gaps) if gaps else None
max_gamma=max((r.get('target_gamma',0) for r in cont),default=None)
if distinct>0:
    status='NUMERICAL_COUNTEREXAMPLE_CANDIDATE_DISTINCT_FINITE_TRANSPORT_ROOT_FOUND_FROM_LARGE_START_SCAN__REQUIRES_HIGH_PRECISION_AND_BRANCH_EQUIVALENCE_VERIFICATION_BEFORE_PROMOTION'
    decision='FREEZE_THE_CANDIDATE_DISTANT_ROOTS_AND_RUN_HIGH_PRECISION_BRANCH_EQUIVALENCE_GAUGE_AND_COAREA_WEIGHT_AUDIT'
elif completed<requested or (min_gap is not None and min_gap<1e-5):
    status='NUMERICAL_DEGENERATION_CANDIDATE_BACKGROUND_CONTINUATION_LOST_REGULARITY_OR_APPROACHED_A_SMALL_TORSION_JACOBIAN_GAP_IN_THE_SCANNED_DOMAIN__GLOBAL_REGULARITY_NOT_AUTHORIZED'
    decision='LOCALIZE_THE_CONTINUATION_DEGENERATION_AND_TEST_BRANCH_MERGER_OR_RUNAWAY_SCALING'
else:
    status='NUMERICALLY_VERIFIED_SCOPED_NO_DISTINCT_TRANSPORT_ROOT_IN_THE_TESTED_LARGE_START_BASINS_AND_NO_TORSION_JACOBIAN_COLLAPSE_ALONG_THE_TESTED_G9_BACKGROUND_STRENGTH_CONTINUATIONS__GLOBAL_COMPACTNESS_AND_UNIQUENESS_REMAIN_BLOCKED'
    decision='PROMOTE_ONLY_THE_SCANNED_DOMAIN_STABILITY__NEXT_EXPAND_TO_ADVERSARIAL_RAPIDITY_DIRECTIONS_AND_NONCONFORMAL_FRAME_FAMILIES_OR_DERIVE_ANALYTIC_COERCIVITY'
summary={
 'gate':'ITER034-G34-AGGREGATE','row_count':len(rows),'large_start_lanes':len(large),'continuation_lanes':len(cont),
 'all_required_artifacts_present':all_present,'large_start_trial_count':large_trials,'large_start_converged_count':large_converged,
 'distinct_transport_root_candidates':distinct,'continuation_completed_steps':completed,'continuation_requested_steps':requested,
 'minimum_observed_jacobian_gap':min_gap,'maximum_target_gamma':max_gamma,'scientific_status':status,'decision':decision,
 'global_branch_compactness_derived':False,'global_torsion_uniqueness_derived':False,'uniform_tower_gap_derived':False,
 'claim_locks':['finite numerical scans are not global uniqueness theorems','solver nonconvergence is not proof of no root','transport distance candidates require gauge/equivalence verification','global strong-curvature branch finiteness remains open','c6 fixed = NO','theory established = 0%','KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes']
}
os.makedirs('iter034-g34-summary',exist_ok=True)
with open('iter034-g34-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,indent=2,sort_keys=True,allow_nan=False); f.write('\n')
print(json.dumps(summary,sort_keys=True,allow_nan=False))
if not all_present: raise SystemExit(2)
