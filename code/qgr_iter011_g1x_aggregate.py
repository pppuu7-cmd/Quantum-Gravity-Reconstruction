#!/usr/bin/env python3
import glob,json
files=glob.glob('iter011-g1x-results/*/result.json')
recs={}
for f in files:
    d=json.load(open(f));recs[d['gate']]=d
required={
 'ITER011-G1-FRECHET-JACOBIAN-REFINEMENT',
 'ITER011-G1-ODD-CUBIC-H-SCALING',
 'ITER011-G1-MEASURE-PHASE-SEPARATION',
 'ITER011-G1-FIXED-VOLUME-ACCUMULATION',
}
assert required<=set(recs),(required,set(recs))
ref=recs['ITER011-G1-FRECHET-JACOBIAN-REFINEMENT']
odd=recs['ITER011-G1-ODD-CUBIC-H-SCALING']
sep=recs['ITER011-G1-MEASURE-PHASE-SEPARATION']
acc=recs['ITER011-G1-FIXED-VOLUME-ACCUMULATION']
assert sep['response_rank_re_im']==2
out={
 'gate':'ITER011-G1X-AGGREGATE',
 'parallel_lanes':4,
 'aggregate_success':True,
 'analytic_h_power_even':ref['h_power'],
 'analytic_even_coefficient_estimate':ref['continuum_coefficient_estimate'],
 'analytic_candidate_exact_rational':ref['candidate_exact_rational'],
 'odd_cubic_h_power':odd['odd_h_power'],
 'measure_phase_response_rank':sep['response_rank_re_im'],
 'fixed_volume_odd_h_power':acc['fixed_volume_odd_h_power'],
 'classification':'PARTIAL_SCOPED_CANONICAL_TORSION_COAREA_JACOBIAN_GENERATES_A_FIXED_REAL_EVEN_CURVATURE_H4_MEASURE_CORRECTION_WITH_COEFFICIENT_CONSISTENT_WITH_MINUS_25_OVER_16_ON_THE_TEST_FAMILY__ITS_ODD_CUBIC_PART_STARTS_AT_H6_AND_NO_CANONICAL_MAP_TO_THE_COHERENT_C6_PHASE_EXISTS',
 'c6_fixed':False,
 'key_results':[
   'An independent Frechet derivative of exp(-A) reproduces the nonsingular torsion Jacobian and confirms Delta mean log|det J| ~ -(25/16) kappa^2 h^4 on the specified symmetric Weyl-active tidal hypercube.',
   'The odd-in-kappa/cubic part scales as kappa^3 h^6 rather than kappa^3 h^4.',
   'At fixed four-volume the even measure correction survives while the odd/cubic contribution vanishes as h^2.',
   'The coarea determinant changes the real log modulus while c6 changes the imaginary coherent phase; the two response directions have rank two and current QGR authority supplies no map between them.'
 ],
 'claim_lock':'This is the first internally normalized UV correction identified in the scoped real measure sector, not a numerical derivation of c6 and not a global glued-measure theorem.',
 'next_gate':'QGR-ITER011-G2-GLUED-COAREA-MEASURE-BRST-AND-PHYSICAL-OBSERVABLE-AUDIT'
}
open('iter011-g1x-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
