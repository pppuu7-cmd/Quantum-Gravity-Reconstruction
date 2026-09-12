#!/usr/bin/env python3
import json, numpy as np
from qgr_iter011_g1_frechet_common import stats
from qgr_iter010_g3_common import curvature_proxy,weyl_proxy,weyl_cubic
h=0.125;k=0.08
j=stats(h,k)
_,_,R=curvature_proxy(h,k);W,_,_=weyl_proxy(R);I3=float(weyl_cubic(W));q=h**4*I3
# For an amplitude A ~ |det J|^{-1/2} exp(i c6 q), the induced changes in
# (Re log A, Im log A) from the coarea factor and from c6 point in independent axes.
d_re=-0.5*j['delta_mean_logabsdet']; d_im_dc6=q
M=np.array([[d_re,0.0],[0.0,d_im_dc6]],float)
rank=int(np.linalg.matrix_rank(M,tol=1e-14))
assert abs(d_re)>1e-10 and abs(d_im_dc6)>1e-10 and rank==2,(d_re,d_im_dc6,rank)
out={
 'gate':'ITER011-G1-MEASURE-PHASE-SEPARATION',
 'h':h,'kappa':k,
 'delta_re_log_amplitude_from_coarea':d_re,
 'weyl_cubic':I3,
 'h4_weyl_cubic_phase_sensitivity':d_im_dc6,
 'response_rank_re_im':rank,
 'classification':'PASS_SCOPED_COAREA_JACOBIAN_AND_C6_ACT_IN_LINEarly_INDEPENDENT_REAL_MODULUS_AND_IMAGINARY_PHASE_DIRECTIONS_OF_THE_MICROSCOPIC_AMPLITUDE',
 'decision':'THE_FIXED_REAL_COAREA_WEIGHT_DOES_NOT_LIFT_THE_C6_COHERENT_PHASE_NULL_DIRECTION_WITHOUT_A_NEW_DERIVED_MEASURE_TO_PHASE_RELATION',
 'guard':'Writing the positive coarea factor as exp(-Delta log det) is a real measure/effective-weight representation. No Lorentzian Wick rotation or multiplication by i is authorized by current QGR authority.'
}
print(json.dumps(out,sort_keys=True))
