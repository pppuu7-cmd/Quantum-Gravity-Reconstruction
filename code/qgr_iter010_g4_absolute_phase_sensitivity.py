#!/usr/bin/env python3
import json
from qgr_iter010_g3_common import curvature_proxy,weyl_proxy,weyl_cubic

# Use the established G3 Weyl-active same-field background. In units a_cont/hbar=1,
# d Phi_abs / d c6 = h^4 * Weyl^3. This must be nonzero for a useful matching datum.
h=0.0625;kappa=0.08
_,_,R=curvature_proxy(h,kappa);W,_,_=weyl_proxy(R);I3=weyl_cubic(W)
sensitivity=(h**4)*I3
assert abs(I3)>0.04
assert abs(sensitivity)>1e-8
out={
 'gate':'ITER010-G4-ABSOLUTE-PHASE-SENSITIVITY',
 'h':h,
 'tidal_kappa':kappa,
 'weyl_cubic':float(I3),
 'd_phase_dc6_in_units_a_cont_over_hbar':float(sensitivity),
 'classification':'PASS_SCOPED_G3_WEYL_ACTIVE_BACKGROUND_HAS_NONZERO_ABSOLUTE_ACTION_PHASE_SENSITIVITY_TO_C6_AND_ONE_DERIVED_ABSOLUTE_PHASE_TARGET_WOULD_FIX_THE_SCALAR_COEFFICIENT',
 'guard':'Nonzero sensitivity is not a target value. Current QGR authority still has to derive the absolute microscopic phase/action datum rather than fit it.'
}
print(json.dumps(out,sort_keys=True))
