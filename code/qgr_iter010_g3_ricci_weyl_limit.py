#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g3_common import curvature_proxy,weyl_proxy

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[]
for h in hs:
    _,_,R=curvature_proxy(float(h),0.08);W,Ric,scalar=weyl_proxy(R)
    rows.append({'h':float(h),'ricci_norm':float(np.linalg.norm(Ric)),'abs_scalar':float(abs(scalar)),'weyl_norm':float(np.linalg.norm(W))})
ric=np.array([r['ricci_norm'] for r in rows]);sca=np.array([r['abs_scalar'] for r in rows]);wey=np.array([r['weyl_norm'] for r in rows])
ric_slope=float(np.polyfit(np.log(hs),np.log(ric),1)[0]);sca_slope=float(np.polyfit(np.log(hs),np.log(sca),1)[0])
# Fit Weyl norm against h^2; intercept estimates the continuum value.
coef=np.polyfit(hs**2,wey,1);wintercept=float(coef[1])
assert 1.7<ric_slope<2.3,(ric_slope,rows)
assert 1.7<sca_slope<2.3,(sca_slope,rows)
assert wintercept>0.45,(wintercept,rows)
out={
 'gate':'ITER010-G3-RICCI-WEYL-CONTINUUM',
 'rows':rows,
 'ricci_norm_h_slope':ric_slope,
 'scalar_h_slope':sca_slope,
 'weyl_norm_h2_extrapolated_intercept':wintercept,
 'classification':'PASS_SCOPED_WEAK_TIDAL_GENERAL_TETRAD_BACKGROUND_APPROACHES_RICCI_FLATNESS_AS_H2_WHILE_THE_WEYL_CURVATURE_APPROACHES_A_NONZERO_CONTINUUM_LIMIT',
 'guard':'Ricci-flatness here is a controlled weak-background continuum property of the test profile; it does not establish a nonlinear exact vacuum solution at finite curvature.'
}
print(json.dumps(out,sort_keys=True))
