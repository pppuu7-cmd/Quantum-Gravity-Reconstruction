#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g2_common import curvature_proxy,weyl_proxy,weyl_cubic

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[]
for h in hs:
    dat,X,R=curvature_proxy(float(h)); W,Ric,scalar=weyl_proxy(R); I3=weyl_cubic(W)
    rows.append({
      'h':float(h),
      'weyl_proxy_norm':float(np.linalg.norm(W)),
      'abs_weyl_cubic':float(abs(I3)),
      'weyl_cubic':float(I3),
      'ricci_proxy_norm':float(np.linalg.norm(Ric)),
      'scalar_proxy':float(scalar)
    })
wn=np.array([r['weyl_proxy_norm'] for r in rows]); ci=np.array([r['abs_weyl_cubic'] for r in rows])
wslope=float(np.polyfit(np.log(hs),np.log(wn),1)[0]); cslope=float(np.polyfit(np.log(hs),np.log(ci),1)[0])
assert 0.75<wslope<1.25,(wslope,rows)
assert 2.5<cslope<3.7,(cslope,rows)
out={
 'gate':'ITER010-G2-DISCRETE-WEYL-PROXY-VANISHING',
 'rows':rows,
 'weyl_norm_h_slope':wslope,
 'weyl_cubic_h_slope':cslope,
 'classification':'PASS_SCOPED_ON_REPAIRED_G9_THE_DISCRETE_WEYL_PROXY_VANISHES_TOWARD_THE_CONFORMALLY_FLAT_CONTINUUM_AND_ITS_CUBIC_IS_ONLY_A_FINITE_H_ARTIFACT',
 'guard':'The nonzero finite-h Weyl proxy is useful as a discretization diagnostic but is not an absolute continuum Weyl^3 response from which c6 may be matched.'
}
print(json.dumps(out,sort_keys=True))
