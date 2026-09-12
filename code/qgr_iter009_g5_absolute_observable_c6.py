#!/usr/bin/env python3
import json, math

# Purity is invariant under a common unitary, but an absolute coherent observable need not be.
# Qubit witness: rho=|0><0|, O=sigma_x, V(eps)=exp(-i eps sigma_y/2).
# Then <sigma_x> = sin(eps), so the first derivative at eps=0 is 1.
for eps in [1e-2,1e-3,1e-4]:
    ratio=math.sin(eps)/eps
    assert abs(ratio-1.0)<eps*eps

out={
    "gate":"ITER009-G5-ABSOLUTE-OBSERVABLE-C6",
    "witness":"rho=|0><0|, O=sigma_x, V=exp(-i eps sigma_y/2)",
    "expectation":"<O>_eps=sin(eps)",
    "linear_response_at_zero":1,
    "classification":"PASS_SCOPED_COMMON_OH4_C6_GEOMETRY_SHIFTS_CAN_AFFECT_ABSOLUTE_COHERENT_PROPAGATION_OBSERVABLES_AT_OH4_EVEN_WHEN_HISTORY_MIXTURE_PURITY_IS_UNCHANGED",
    "guard":"Leading c6 decoupling is observable-specific; it must not be generalized from purity loss to all propagation observables."
}
print(json.dumps(out,sort_keys=True))
