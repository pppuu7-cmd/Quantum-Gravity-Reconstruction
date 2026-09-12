#!/usr/bin/env python3
import json,numpy as np
from qgr_iter011_g3_common import AD,MAX_CLOSURE_RESIDUAL,MAX_UNIMODULAR_TRACE,haar_log_density
assert MAX_CLOSURE_RESIDUAL<5e-13,MAX_CLOSURE_RESIDUAL
assert MAX_UNIMODULAR_TRACE<5e-13,MAX_UNIMODULAR_TRACE
z0=np.array([0.31,-0.22,0.17,0.09,-0.14,0.26])
eps=np.array([0.20,0.14,0.10,0.07,0.05,0.035])
vals=[];parity=[]
for e in eps:
    lp=haar_log_density(e*z0);lm=haar_log_density(-e*z0)
    vals.append(abs(0.5*(lp+lm)));parity.append(abs(lp-lm))
p=float(np.polyfit(np.log(eps),np.log(vals),1)[0])
assert abs(p-2)<0.08,p
assert max(parity)<2e-13,max(parity)
out={
 'gate':'ITER011-G3-HAAR-LIE-ALGEBRA-AUDIT',
 'max_lie_closure_residual':MAX_CLOSURE_RESIDUAL,
 'max_adjoint_trace_abs':MAX_UNIMODULAR_TRACE,
 'small_coordinate_even_loghaar_power':p,
 'max_loghaar_z_minus_loghaar_minus_z':max(parity),
 'classification':'PASS_SCOPED_FROZEN_SIX_GENERATOR_E_LORENTZ_ALGEBRA_CLOSES_IS_UNIMODULAR_AND_ITS_EXPONENTIAL_COORDINATE_HAAR_DENSITY_HAS_THE_EXPECTED_EVEN_QUADRATIC_SMALL_CONNECTION_START',
 'guard':'This validates the local exponential-coordinate Haar factor used in the weak regular chart; it is not a global statement across exponential-map singularities.'
}
print(json.dumps(out,sort_keys=True))
