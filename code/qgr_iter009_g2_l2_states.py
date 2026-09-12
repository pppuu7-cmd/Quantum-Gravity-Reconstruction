#!/usr/bin/env python3
import json, math

# Along the invariant scale orbit G=s^2 Ghat, t=log s and dmu contains dt.
# Total orbit volume is infinite, but normalized L2 states need not be constant.
a = 1.0
A = (2*a/math.pi)**0.25
norm_sq = A*A*math.sqrt(math.pi/(2*a))
assert abs(norm_sq-1.0) < 1e-14

out = {
    "gate": "ITER009-G2-L2-STATES",
    "scale_coordinate": "t=log(s)",
    "reference_orbit_measure": "dt",
    "total_reference_orbit_volume": "infinite",
    "normalized_state_example": "psi(t)=(2a/pi)^(1/4) exp(-a t^2), a>0",
    "norm_squared": norm_sq,
    "classification": "PASS_SCOPED_INFINITE_REFERENCE_MEASURE_VOLUME_DOES_NOT_PREVENT_NORMALIZED_L2_STATES",
    "guard": "This does not construct a preferred interacting vacuum state."
}
print(json.dumps(out, sort_keys=True))
