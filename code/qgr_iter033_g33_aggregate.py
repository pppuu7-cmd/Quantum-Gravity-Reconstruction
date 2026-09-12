#!/usr/bin/env python3
import glob,json,os
from collections import Counter
EXPECTED={
 'local-ift-inverse-bound':6,
 'existing-finite-regularity-anchors':6,
 'pointwise-not-uniform':6,
 'compact-gap-sufficient-control':6,
 'bounded-action-not-coercive':6,
}
rows=[]
for p in glob.glob('iter033-g33-results/**/result.json',recursive=True):
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
counts=Counter(r.get('audit') for r in rows)
all_present=len(rows)==30 and all(counts.get(k,0)==v for k,v in EXPECTED.items())
all_passed=all(bool(r.get('passed')) for r in rows) if rows else False
summary={
 'gate':'ITER033-G33-AGGREGATE','lane_count':len(rows),'audit_counts':dict(sorted(counts.items())),
 'all_required_artifacts_present':all_present,'all_lane_gates_passed':all_passed,
 'local_torsion_regularity_mechanism':'PASS_SCOPED',
 'finite_qgr_regularity_anchors_present':True,
 'tower_wide_uniform_jacobian_gap_derived':False,
 'branch_compactness_derived':False,
 'uniform_qgr_regularity_authority_derived':False,
 'scientific_status':'PARTIAL_SCOPED_LOCAL_TORSION_REGULARITY_AND_QUANTITATIVE_IFT_SUPPLY_THE_G32_REGULARITY_MECHANISM_ON_ANY_COMPACT_NONDEGENERATE_BRANCH_PATCH__BLOCKED_NO_DERIVED_COMPACTNESS_OR_TOWER_WIDE_UNIFORM_TORSION_JACOBIAN_GAP_AND_POINTWISE_FINITE_LEVEL_REGULARITY_IS_INSUFFICIENT',
 'strongest_positive':'The G32 regularity hypothesis has been reduced to a precise QGR object: a uniform positive lower bound on the torsion-Jacobian singular gap over the refinement-relevant branch family. G5/G9 provide real finite regular anchors, and compact nondegenerate branch control would be sufficient by the quantitative implicit-function mechanism.',
 'strongest_blocker':'Existing QGR results do not prove compactness of the full refinement branch family or exclude singular/noncompact escape. Exact controls show that every finite level may remain regular while the infimum gap tends to zero, and bounded action by itself is not generically coercive.',
 'decision':'PROMOTE_LOCAL_AND_COMPACT_PATCH_REGULARITY_ONLY__DO_NOT_PROMOTE_TOWER_WIDE_UNIFORM_REGULARITY__NEXT_TEST_QGR_SPECIFIC_COERCIVITY_COMPACTNESS_OR_CONSTRUCT_A_RUNAWAY_BRANCH_COUNTEREXAMPLE',
 'next_gate':'QGR-ITER034-G34-QGR-SPECIFIC-COERCIVITY-COMPACTNESS-OR-RUNAWAY-BRANCH-COUNTEREXAMPLE',
 'claim_locks':[
   'G5/G9 finite regular anchors do not imply tower-wide regularity',
   'tower-wide uniform Jacobian gap derived = NO',
   'branch compactness derived = NO',
   'global strong-curvature branch finiteness remains open',
   'absolute beta derived = NO','absolute quantum phase normalization fixed = NO',
   'physical Weyl-active absolute phase target derived = NO','c6 fixed = NO','theory established = 0%',
   'KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes'
 ]
}
os.makedirs('iter033-g33-summary',exist_ok=True)
with open('iter033-g33-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(summary,sort_keys=True))
if not all_present or not all_passed: raise SystemExit(2)
