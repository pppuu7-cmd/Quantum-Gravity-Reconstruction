#!/usr/bin/env python3
import json, numpy as np
from qgr_iter011_g1_common import flat_subtracted

h=0.125
ks=np.array([-0.12,-0.08,-0.04,0.04,0.08,0.12],float)
rows=[flat_subtracted(h,float(k)) for k in ks]
vals={round(r['kappa'],8):r['delta_sum_logabsdet'] for r in rows}
pairs=[]
for k in (0.04,0.08,0.12):
    vp=vals[round(k,8)]; vm=vals[round(-k,8)]
    even=0.5*(vp+vm); odd=0.5*(vp-vm)
    pairs.append({'abs_kappa':k,'even_part':even,'odd_part':odd,'odd_over_even_abs':abs(odd)/(abs(even)+1e-30)})
# Polynomial diagnostic through cubic order; constant excluded by flat subtraction.
X=np.column_stack([ks,ks**2,ks**3])
y=np.array([r['delta_sum_logabsdet'] for r in rows])
coef=np.linalg.lstsq(X,y,rcond=None)[0]
out={
 'gate':'ITER011-G1-JACOBIAN-AMPLITUDE-PARITY',
 'h':h,
 'rows':[{'kappa':r['kappa'],'delta_sum_logabsdet':r['delta_sum_logabsdet'],'min_sv':r['min_sv'],'max_residual':r['max_residual']} for r in rows],
 'parity_pairs':pairs,
 'fit_coefficients_kappa_kappa2_kappa3':[float(x) for x in coef],
 'classification':'PARITY_AND_CUBIC_SENSITIVITY_NUMERIC',
 'guard':'A positive coarea/Jacobian weight is a real measure datum. Even if a cubic term is present numerically, it does not become a Lorentzian action phase without an independently derived phase relation.'
}
print(json.dumps(out,sort_keys=True))
