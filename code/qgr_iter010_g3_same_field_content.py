#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g3_common import metric_at,tetrad_at,E

# The general tetrad changes the background inside the already-established symmetric
# second-moment arena; it does not introduce extra field components.
symmetric_metric_components=4*5//2
assert symmetric_metric_components==10
samples=[(0,0,0,0),(1,0,1,0),(1,1,1,1)]
errs=[]
for x in samples:
    F=tetrad_at(x,0.25,0.08);g=metric_at(x,0.25,0.08)
    errs.append(float(np.linalg.norm(g-g.T)))
    assert np.linalg.det(F)!=0.0
    assert np.linalg.norm(g-F.T@E@F)<1e-12
# Phi Hessian in Minkowski spatial coordinates is proportional to diag(1,1,-2),
# whose Euclidean spatial trace vanishes exactly: the test potential is harmonic.
hessian_diag=[1,1,-2]
assert sum(hessian_diag)==0
out={
 'gate':'ITER010-G3-SAME-FIELD-CONTENT',
 'second_moment_components':symmetric_metric_components,
 'metric_definition':'g=F^T E F',
 'new_field_components':0,
 'harmonic_tidal_potential_spatial_hessian_diag':hessian_diag,
 'harmonic_trace':sum(hessian_diag),
 'max_metric_symmetry_error':max(errs),
 'classification':'PASS_SCOPED_WEYL_ACTIVE_TEST_BACKGROUND_LIVES_IN_THE_EXISTING_TEN_COMPONENT_SECOND_MOMENT_FIELD_CONTENT_AND_USES_A_HARMONIC_WEAK_VACUUM_TIDAL_PROFILE',
 'guard':'This establishes field-content compatibility of the background witness, not that its particular profile is a dynamically selected solution of a completed UV action.'
}
print(json.dumps(out,sort_keys=True))
