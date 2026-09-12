#!/usr/bin/env python3
import json,math

# G3 establishes a continuously tunable weak tidal amplitude kappa with Weyl^3 ~ kappa^3.
# Therefore the six-derivative loop/action phase Phi6 can take arbitrarily small continuous
# nonzero values near zero. Requiring exp(i c6 Phi6)=1 for every such physical phase makes
# n(Phi)=c6 Phi/(2pi) an integer-valued continuous function, hence n=0 near zero and forces
# c6=0 if any nonzero Phi is allowed. This is not a mechanism for selecting a nonzero c6.
phis=[0.0,1e-9,8e-9,27e-9,64e-9]
for c6 in [0.2,1.0,7.0,math.pi]:
    vals=[c6*p/(2*math.pi) for p in phis]
    assert any(abs(v-round(v))>1e-15 for v in vals[1:])
out={
 'gate':'ITER010-G4-CONTINUOUS-LOOP-C6-NOQUANTIZATION',
 'continuous_small_phase_samples':phis,
 'classification':'FAIL_SCOPED_ROOT_OF_UNITY_OR_LOOP_SINGLE_VALUEDNESS_CANNOT_SELECT_A_NONZERO_C6_ON_THE_CONTINUOUS_WEYL_ACTIVE_BACKGROUND',
 'reason':'continuity of physical small Weyl-active phases near zero would force any integer winding to remain zero, so imposing unity for every loop would force c6=0 rather than quantize a nonzero value',
 'guard':'Physical branch/loop phases need not be unity. A future independently derived discrete curvature/flux spectrum could change this conclusion, but no such spectrum is current authority.'
}
print(json.dumps(out,sort_keys=True))
