#!/usr/bin/env python3
import glob,json

files=sorted(glob.glob('iter010-g1-results/**/result.json',recursive=True))
assert len(files)==6,(len(files),files)
rows=[]
for f in files:
    with open(f) as fh:d=json.load(fh)
    rows.append({'gate':d.get('gate'),'classification':d.get('classification'),'file':f})
classes=[r['classification'] for r in rows]
assert sum(c.startswith('PASS_SCOPED') for c in classes)==5,classes
assert sum(c.startswith('BLOCKED_SCOPED') for c in classes)==1,classes
required={
 'ITER010-G1-CONNECTION-DENSITY-DERIVATIVE-ORDER',
 'ITER010-G1-C6-SENSITIVITY-RANK',
 'ITER010-G1-HISTORY-C6-SENSITIVITY-ORDER',
 'ITER010-G1-HIGHER-DERIVATIVE-AUTHORITY-SCAN',
 'ITER010-G1-WEYL3-CONTINUOUS-FAMILY-WITNESS',
 'ITER010-G1-MINIMAL-MATCHING-DATUM'
}
assert {r['gate'] for r in rows}==required
out={
 'iteration':'010-G1',
 'parallel_lanes':6,
 'aggregate_success':True,
 'lane_results':rows,
 'key_results':[
  'The exact Iter005 connection-density construction is structurally two-derivative at every field order because it contains exactly two one-derivative gamma factors dressed by algebraic metric/determinant series; it cannot itself generate a six-derivative Weyl^3 coefficient.',
  'The exact frozen lower-order sensitivity matrix retains a one-dimensional null direction aligned with c6.',
  'The leading O(h^4) history-mixture comparator has zero c6 sensitivity; branch-dependent c6 sensitivity starts at O(h^6) under the regular expansion already established in Iter009.',
  'No already-frozen exact higher-derivative finite-cell action or equivalent derived-c6 rule is present in repository authority.',
  'An explicit continuous Weyl^3 deformation is invisible through the flat Hessian/lower-order sector while remaining nontrivial at cubic-curvature order.',
  'Because the residual UV coefficient sector is one-dimensional, one internally derived and absolutely normalized curved microscopic O(h^4) datum with nonzero Weyl^3 sensitivity is the minimal sufficient new information to fix c6.'
 ],
 'classification':'BLOCKED_SCOPED_EXISTING_QGR_MICROSCOPIC_AUTHORITY_DOES_NOT_IDENTIFY_C6__THE_FROZEN_CONNECTION_DENSITY_IS_TWO_DERIVATIVE_AND_ONE_WEYL_CUBED_COEFFICIENT_DIRECTION_REMAINS_FREE',
 'decision':'DO_NOT_FIT_C6__DERIVE_ONE_NEW_ABSOLUTE_CURVED_MICROSCOPIC_UV_MATCHING_CONDITION_OR_PROVE_A_CANONICAL_FINITE_CELL_SIX_DERIVATIVE_EXTENSION',
 'recommended_next_gate':'QGR-ITER010-G2-CANONICAL-SIX-DERIVATIVE-FINITE-CELL-EXTENSION-CENSUS',
 'claim_lock':'Operator-shape uniqueness is not coefficient uniqueness; no c6 value is derived by G1.'
}
with open('iter010-g1-summary.json','w') as fh:json.dump(out,fh,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
