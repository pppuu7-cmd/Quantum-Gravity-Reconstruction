#!/usr/bin/env python3
import glob,json
recs={}
for f in glob.glob('iter011-g2-results/*/result.json'):
    d=json.load(open(f));recs[d['gate']]=d
required={
 'ITER011-G2-UNIQUE-ANCHOR-GLUED-REFINEMENT',
 'ITER011-G2-FLAT-SUBTRACTED-JACOBIAN-REPARAMETRIZATION',
 'ITER011-G2-CURVATURE2-PURE-VACUUM-BULK-QUOTIENT',
 'ITER011-G2-COMMON-COAREA-HISTORY-CANCELLATION',
}
assert required<=set(recs),(required,set(recs))
ua=recs['ITER011-G2-UNIQUE-ANCHOR-GLUED-REFINEMENT']
assert ua['prospective_unique_anchor_convergence_hypothesis_passed'] is False
out={
 'gate':'ITER011-G2-AGGREGATE',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'PARTIAL_SCOPED_FLAT_SUBTRACTED_TORSION_JACOBIAN_HAS_CONSTANT_BASIS_INVARIANCE_AND_A_CONSTRAINED_MEASURE_SECTOR_ROLE__BUT_SIMPLE_UNIQUE_ANCHOR_FACTORISATION_FAILS_AND_FULL_GLUED_SHARED_VARIABLE_COAREA_PUSHFORWARD_REMAINS_OPEN',
 'key_results':[
  'Prospective simple unique-anchor factorisation fails strongly: the forward local Jacobian retains lower-order first-jet/coordinate pieces and its summed flat-subtracted log determinant does not converge under n=1,2,3 refinement.',
  'Therefore the full glued constraint map on shared variables, or an equivalent projective/coarea pushforward, must be constructed before a global determinant can be assigned.',
  'Flat-subtracted Delta log|det J| is invariant under curvature-independent linear changes of constraint and connection coordinates.',
  'Modulo Euler/topological and EH equation-of-motion field redefinitions, the local parity-even curvature-squared pure-vacuum bulk quotient has dimension zero.',
  'Any positive coarea factor common to all 24 history labels at fixed geometry cancels exactly from normalized conditional history probabilities.'
 ],
 'c6_fixed':False,
 'claim_lock':'G2 does not establish a global/projective coarea measure, BRST anomaly freedom, or a coherent c6 phase. The local G1 Jacobian effect remains valid in its scoped symmetric-cell average, but naive local products are not an authorized continuum gluing rule.',
 'next_gate':'QGR-ITER011-G3-FULL_SHARED_VARIABLE_COAREA_PUSHFORWARD_AND_BRST_JACOBIAN_CLOSURE'
}
open('iter011-g2-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
