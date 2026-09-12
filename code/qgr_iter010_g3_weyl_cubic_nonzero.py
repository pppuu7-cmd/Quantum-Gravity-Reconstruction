#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g3_common import curvature_proxy,weyl_proxy,weyl_cubic

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[]
for h in hs:
    _,_,R=curvature_proxy(float(h),0.08);W,_,_=weyl_proxy(R);I3=weyl_cubic(W)
    rows.append({'h':float(h),'weyl_cubic':float(I3)})
vals=np.array([r['weyl_cubic'] for r in rows])
fit=np.polyfit(hs**2,vals,1);intercept=float(fit[1])
rel_last=float(abs(vals[-1]-intercept)/abs(intercept))
assert abs(intercept)>0.04,(intercept,rows)
assert rel_last<0.02,(rel_last,intercept,rows)
out={
 'gate':'ITER010-G3-WEYL-CUBIC-NONZERO',
 'rows':rows,
 'weyl_cubic_h2_extrapolated_intercept':intercept,
 'finest_to_intercept_relative_error':rel_last,
 'classification':'PASS_SCOPED_GENERAL_TETRAD_WEAK_VACUUM_TIDAL_BACKGROUND_HAS_A_NONZERO_CONTINUUM_WEYL_CUBED_INVARIANT_AND_IS_C6_SENSITIVE_IN_PRINCIPLE',
 'guard':'Nonzero Weyl^3 makes the background suitable for sensitivity tests, but does not itself provide the absolute microscopic action normalization needed to determine c6.'
}
print(json.dumps(out,sort_keys=True))
