#!/usr/bin/env python3
import json
from qgr_iter011_g1_frechet_common import stats,slope,FLAT_DET
hs=[0.25,0.20,0.16,0.125,0.10,0.08,0.0625]
k=0.08
rows=[stats(h,k) for h in hs]
ys=[r['delta_mean_logabsdet'] for r in rows]
pow_h=slope(hs,ys)
coeffs=[r['delta_mean_logabsdet']/(k*k*h**4) for r,h in zip(rows,hs)]
# Flat analytic authority from Iter006/009.
flat=stats(0.1,0.0)
assert abs(flat['mean_logabsdet']-__import__('math').log(FLAT_DET))<2e-11
assert abs(pow_h-4.0)<0.12,(pow_h,coeffs)
assert abs(coeffs[-1]+25.0/16.0)<0.03,coeffs[-1]
out={
 'gate':'ITER011-G1-FRECHET-JACOBIAN-REFINEMENT',
 'flat_det_authority':FLAT_DET,
 'rows':rows,
 'h_power':pow_h,
 'coeff_delta_mean_over_kappa2_h4':coeffs,
 'continuum_coefficient_estimate':coeffs[-1],
 'candidate_exact_rational':'-25/16',
 'classification':'PASS_SCOPED_ANALYTIC_FRECHET_TORSION_JACOBIAN_CONFIRMS_A_FIXED_EVEN_MEASURE_CORRECTION_DELTA_MEAN_LOGDET_EQUALS_MINUS_25_OVER_16_KAPPA2_H4_PLUS_HIGHER_ORDER',
 'guard':'The rational identification is an asymptotic numerical reconstruction on the specified symmetric tidal hypercube. It is not yet a covariant all-background theorem and it is a real coarea-measure statement, not a coherent action phase.'
}
print(json.dumps(out,sort_keys=True))
