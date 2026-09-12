#!/usr/bin/env python3
import glob,json

files=sorted(glob.glob('iter010-g2-results/**/result.json',recursive=True))
assert len(files)==6,(len(files),files)
rows=[]
for f in files:
    with open(f) as fh:d=json.load(fh)
    rows.append({'gate':d.get('gate'),'classification':d.get('classification'),'file':f})
classes=[r['classification'] for r in rows]
assert sum(c.startswith('PASS_SCOPED') for c in classes)==4,classes
assert sum(c.startswith('BLOCKED_SCOPED') for c in classes)==2,classes
required={
 'ITER010-G2-G9-CONFORMAL-WEYL-OBSTRUCTION',
 'ITER010-G2-HOLONOMY-CURVATURE-SCALING',
 'ITER010-G2-DISCRETE-WEYL-PROXY-VANISHING',
 'ITER010-G2-CELL-WEYL3-SCALING',
 'ITER010-G2-FINITE-CELL-CUBIC-ORBIT-AMBIGUITY',
 'ITER010-G2-NORMALIZATION-HOMOGENEITY'
}
assert {r['gate'] for r in rows}==required
out={
 'iteration':'010-G2',
 'parallel_lanes':6,
 'aggregate_success':True,
 'lane_results':rows,
 'key_results':[
  'The repaired-G9 edge transport factorizes as a scalar conformal ratio times an E-Lorentz matrix, so its continuum background family is conformally flat and has identically zero Weyl tensor.',
  'Adjacent-swap relative holonomy logarithms scale as h^2 and define a controlled finite-cell curvature proxy; the reconstructed Riemann pair-symmetry defect vanishes toward the continuum.',
  'The discrete Weyl proxy on repaired G9 vanishes approximately linearly with h, while its cubic vanishes approximately as h^3, confirming it is a discretization artifact of a Weyl-flat continuum background.',
  'Consequently h^4 times the discrete Weyl-cubed proxy vanishes approximately as h^7 instead of providing a nonzero h^4 absolute c6 matching signal.',
  'S4 vertex symmetry leaves six degree-three plane-label orbit types before curvature identities, so finite-cell cubic representatives are not selected uniquely by S4 symmetry alone.',
  'All existing symmetry/scaling/homogeneous refinement conditions are homogeneous in an overall six-derivative coefficient and cannot fix its normalization.'
 ],
 'classification':'BLOCKED_SCOPED_REPAIRED_G9_SUPPLIES_A_CONTROLLED_CURVATURE_PROXY_BUT_IS_WEYL_FLAT_IN_THE_CONTINUUM_AND_EXISTING_FINITE_CELL_SYMMETRIES_DO_NOT_SELECT_OR_NORMALIZE_A_UNIQUE_WEYL_CUBED_EXTENSION',
 'decision':'CONSTRUCT_A_SAME_REALIZATION_NON_CONFORMALLY_FLAT_WEYL_ACTIVE_MICROSCOPIC_BACKGROUND_AND_THEN_TEST_NONHOMOGENEOUS_ABSOLUTE_ACTION_OR_REFINEMENT_MATCHING',
 'recommended_next_gate':'QGR-ITER010-G3-WEYL-ACTIVE-SAME-REALIZATION-MICROSCOPIC-BACKGROUND',
 'claim_lock':'Finite-h discrete Weyl artifacts on repaired G9 must not be used to fit c6; no canonical finite-cell Weyl^3 action or normalization is derived by G2.'
}
with open('iter010-g2-summary.json','w') as fh:json.dump(out,fh,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
