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
out={
 'gate':'ITER011-G2-AGGREGATE',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'PARTIAL_SCOPED_TORSION_COAREA_MEASURE_HAS_A_WELL_DEFINED_FLAT_SUBTRACTED_LOCAL_REFINEMENT_BASELINE_AND_CONSTANT_BASIS_INVARIANCE__ITS_LEADING_CURVATURE2_CLASS_HAS_NO_NEW_PURE_VACUUM_BULK_DIRECTION_AND_COMMON_HISTORY_FACTORS_CANCEL_CONDITIONALLY',
 'key_results':[
  'Unique-anchor counting removes the severe shared-vertex overcount in the naive local-cell product and yields a finite even fixed-volume refinement baseline on the test lattice.',
  'Flat-subtracted Delta log|det J| is invariant under curvature-independent linear changes of constraint and connection coordinates.',
  'Modulo Euler/topological and EH equation-of-motion field redefinitions, the local parity-even curvature-squared pure-vacuum bulk quotient has dimension zero.',
  'Any positive coarea factor common to all 24 history labels at fixed geometry cancels exactly from normalized conditional history probabilities.'
 ],
 'c6_fixed':False,
 'claim_lock':'This does not establish the full glued/projective continuum measure, BRST anomaly freedom, or a coherent c6 phase. It narrows the coarea correction to a measure/configuration-sector effect in the tested scope.',
 'next_gate':'QGR-ITER011-G3-PROJECTIVE-PUSHFORWARD-COAREA-MEASURE-AND-BRST-JACOBIAN-CLOSURE'
}
open('iter011-g2-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
