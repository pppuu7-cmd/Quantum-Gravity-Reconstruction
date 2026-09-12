#!/usr/bin/env python3
import glob,json

files=sorted(glob.glob('iter010-g4-results/**/result.json',recursive=True))
assert len(files)==6,(len(files),files)
rows=[]
for f in files:
    with open(f) as fh:d=json.load(fh)
    rows.append({'gate':d.get('gate'),'classification':d.get('classification'),'file':f})
classes=[r['classification'] for r in rows]
assert sum(c.startswith('PASS_SCOPED') for c in classes)==2,classes
assert sum(c.startswith('FAIL_SCOPED') for c in classes)==2,classes
assert sum(c.startswith('BLOCKED_SCOPED') for c in classes)==2,classes
required={
 'ITER010-G4-TWO-VS-SIX-DERIVATIVE-NORMALIZATION',
 'ITER010-G4-HISTORY-PHASE-C6-NOFIX',
 'ITER010-G4-CONTINUOUS-LOOP-C6-NOQUANTIZATION',
 'ITER010-G4-REFINEMENT-HOMOGENEITY',
 'ITER010-G4-ABSOLUTE-PHASE-SENSITIVITY',
 'ITER010-G4-NONHOMOGENEOUS-AUTHORITY-SCAN'
}
assert {r['gate'] for r in rows}==required
out={
 'iteration':'010-G4',
 'parallel_lanes':6,
 'aggregate_success':True,
 'lane_results':rows,
 'key_results':[
  'The frozen Einstein-Hilbert/two-derivative normalization fixes the geometric conversion for that operator but leaves the independent dimensionless six-derivative c6 direction free.',
  'History Kraus normalization and additive/projective action-phase composition remain exact for arbitrary real c6 and cannot select its value.',
  'Because the G3 Weyl-active background admits continuously variable small phases, root-of-unity/loop-single-valuedness cannot quantize a nonzero c6 without an independently derived discrete flux spectrum.',
  'Pure additive/homogeneous refinement conditions are homogeneous in c6: they either leave every normalization free when the geometric identity closes or kill the operator when it does not; they do not select a unique nonzero coefficient.',
  'The G3 background has a nonzero absolute action-phase derivative with respect to c6, so one genuinely derived absolute microscopic phase/action target would be sufficient to determine c6.',
  'No current canonical QGR record supplies that nonhomogeneous absolute microscopic target.'
 ],
 'classification':'BLOCKED_SCOPED_NO_EXISTING_QGR_NORMALIZATION_PHASE_LOOP_OR_HOMOGENEOUS_REFINEMENT_RULE_FIXES_C6__THE_WEYL_ACTIVE_BACKGROUND_IS_SENSITIVE_BUT_THE_REQUIRED_ABSOLUTE_MICROSCOPIC_TARGET_IS_MISSING',
 'iteration_decision':'ITER010_CAN_CLOSE_100_PERCENT_WITH_C6_EXPLICITLY_UNFIXED_AND_THE_MISSING_NONHOMOGENEOUS_UV_DATUM_ISOLATED',
 'recommended_next_gate':'ITER011_G1_MICROSCOPIC_FINITE_CELL_ACTION_PRINCIPLE_CENSUS_AND_MINIMAL_UV_EXTENSION',
 'claim_lock':'Do not set c6 by convention, by external continuum two-loop coefficients, by leading history loss, or by root-of-unity assumptions.'
}
with open('iter010-g4-summary.json','w') as fh:json.dump(out,fh,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
