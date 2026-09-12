#!/usr/bin/env python3
import glob,json

files=sorted(glob.glob('iter010-g3-results/**/result.json',recursive=True))
assert len(files)==6,(len(files),files)
rows=[]
for f in files:
    with open(f) as fh:d=json.load(fh)
    rows.append({'gate':d.get('gate'),'classification':d.get('classification'),'file':f})
assert all(r['classification'].startswith('PASS_SCOPED') for r in rows),rows
required={
 'ITER010-G3-SAME-FIELD-CONTENT',
 'ITER010-G3-TORSION-HOLONOMY-SCALING',
 'ITER010-G3-RICCI-WEYL-CONTINUUM',
 'ITER010-G3-WEYL-CUBIC-NONZERO',
 'ITER010-G3-WEYL-ACTIVE-CELL-H4-SCALING',
 'ITER010-G3-WEYL-AMPLITUDE-SCALING'
}
assert {r['gate'] for r in rows}==required
out={
 'iteration':'010-G3',
 'parallel_lanes':6,
 'aggregate_success':True,
 'lane_results':rows,
 'key_results':[
  'A non-conformally-flat background can be constructed inside the already-established ten-component symmetric second-moment field content by replacing the conformal special-case tetrad with a general invertible tetrad while keeping the same E-Lorentz connection and discrete torsion closure.',
  'For a harmonic weak vacuum tidal profile, all tested finite cells have tiny torsion residuals, a positive connection-Jacobian singular-value margin, and relative holonomy logarithms scaling as h^2.',
  'The Ricci/scalar proxies vanish as approximately h^2 while the Weyl norm extrapolates to a nonzero continuum value.',
  'The Weyl-cubed invariant extrapolates to a nonzero continuum value, making the background c6-sensitive in principle.',
  'h^4 times the Weyl-cubed finite-cell proxy scales as h^4 rather than the h^7 artifact law of the conformally-flat repaired-G9 background.',
  'Weyl curvature scales linearly and Weyl^3 cubically with the tidal amplitude, validating the weak-curvature interpretation.'
 ],
 'classification':'PASS_SCOPED_WEYL_ACTIVE_SAME_FIELD_CONTENT_MICROSCOPIC_BACKGROUND_ESTABLISHED_WITH_STABLE_TORSION_CLOSURE_NONZERO_CONTINUUM_WEYL_CUBED_AND_CORRECT_H4_CELL_SCALING',
 'decision':'USE_THIS_BACKGROUND_ONLY_AS_A_C6_SENSITIVITY_WITNESS__NEXT_TEST_MUST_SUPPLY_A_NONHOMOGENEOUS_ABSOLUTE_MICROSCOPIC_ACTION_PHASE_OR_REFINEMENT_MATCH',
 'recommended_next_gate':'QGR-ITER010-G4-ABSOLUTE-MICROSCOPIC-C6-MATCHING-OR-NO-GO',
 'claim_lock':'The background removes the Weyl-flat identifiability obstruction but does not by itself fix c6 or prove that its chosen tidal profile is dynamically selected by a completed UV action.'
}
with open('iter010-g3-summary.json','w') as fh:json.dump(out,fh,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
