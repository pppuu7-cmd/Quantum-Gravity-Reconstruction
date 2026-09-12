#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g3_common import curvature_proxy,weyl_proxy,weyl_cubic

h=0.0625
kappas=np.array([0.04,0.06,0.08,0.10,0.12],float)
rows=[]
for k in kappas:
    _,_,R=curvature_proxy(h,float(k));W,Ric,scalar=weyl_proxy(R);I3=weyl_cubic(W)
    rows.append({'kappa':float(k),'weyl_norm':float(np.linalg.norm(W)),'weyl_cubic':float(I3),'abs_weyl_cubic':float(abs(I3)),'ricci_norm':float(np.linalg.norm(Ric))})
wslope=float(np.polyfit(np.log(kappas),np.log([r['weyl_norm'] for r in rows]),1)[0])
cslope=float(np.polyfit(np.log(kappas),np.log([r['abs_weyl_cubic'] for r in rows]),1)[0])
assert 0.9<wslope<1.1,(wslope,rows)
assert 2.85<cslope<3.15,(cslope,rows)
out={
 'gate':'ITER010-G3-WEYL-AMPLITUDE-SCALING',
 'h':h,
 'rows':rows,
 'weyl_norm_kappa_slope':wslope,
 'weyl_cubic_kappa_slope':cslope,
 'classification':'PASS_SCOPED_WEYL_ACTIVE_BACKGROUND_SHOWS_LINEAR_CURVATURE_AND_CUBIC_WEYL_INVARIANT_SCALING_WITH_THE_TIDAL_AMPLITUDE_AS_REQUIRED',
 'guard':'Amplitude scaling validates the intended weak-curvature interpretation of the witness; it does not select a preferred physical kappa or derive c6.'
}
print(json.dumps(out,sort_keys=True))
