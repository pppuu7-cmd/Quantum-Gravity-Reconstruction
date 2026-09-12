#!/usr/bin/env python3
import json, math
weights=[1e-9,0.03,1.0,7.5,1e9]
rows=[]
for w in weights:
    raw=[w/24.0]*24
    Z=sum(raw)
    p=[x/Z for x in raw]
    err=max(abs(x-1.0/24.0) for x in p)
    assert err<2e-16
    rows.append({'common_geometry_weight':w,'normalization':Z,'max_probability_error_from_1_over_24':err})
out={
 'gate':'ITER011-G2-COMMON-COAREA-HISTORY-CANCELLATION',
 'rows':rows,
 'classification':'PASS_SCOPED_ANY_POSITIVE_TORSION_COAREA_FACTOR_COMMON_TO_ALL_24_HISTORY_LABELS_AT_FIXED_GEOMETRY_CANCELS_EXACTLY_FROM_NORMALIZED_CONDITIONAL_HISTORY_PROBABILITIES',
 'interpretation':'The local torsion Jacobian may change the geometry/configuration measure, but by itself it does not create a new relative 24-history weight or alter a conditional comparator when it is branch-label independent.',
 'guard':'This does not prove cancellation after integrating over fluctuating geometries correlated with preparation/readout; it is a fixed-geometry conditional statement.'
}
print(json.dumps(out,sort_keys=True))
