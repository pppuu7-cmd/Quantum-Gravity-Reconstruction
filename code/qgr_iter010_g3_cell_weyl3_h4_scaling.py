#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g3_common import curvature_proxy,weyl_proxy,weyl_cubic

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[]
for h in hs:
    _,_,R=curvature_proxy(float(h),0.08);W,_,_=weyl_proxy(R);I3=weyl_cubic(W);cell=(h**4)*I3
    rows.append({'h':float(h),'weyl_cubic':float(I3),'h4_weyl_cubic_cell_proxy':float(cell),'abs_cell_proxy':float(abs(cell))})
vals=np.array([r['abs_cell_proxy'] for r in rows])
slope=float(np.polyfit(np.log(hs),np.log(vals),1)[0])
assert 3.7<slope<4.3,(slope,rows)
out={
 'gate':'ITER010-G3-WEYL-ACTIVE-CELL-H4-SCALING',
 'rows':rows,
 'cell_proxy_h_slope':slope,
 'classification':'PASS_SCOPED_ON_THE_WEYL_ACTIVE_SAME_FIELD_BACKGROUND_H4_TIMES_THE_FINITE_CELL_WEYL_CUBED_PROXY_HAS_THE_REQUIRED_NONZERO_H4_CONTINUUM_SCALING',
 'guard':'Correct scaling and nonzero sensitivity are necessary for c6 matching but do not determine the absolute coefficient without a microscopic action/phase/refinement normalization rule.'
}
print(json.dumps(out,sort_keys=True))
