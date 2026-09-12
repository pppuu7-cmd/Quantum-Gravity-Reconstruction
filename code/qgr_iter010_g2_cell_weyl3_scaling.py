#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g2_common import curvature_proxy,weyl_proxy,weyl_cubic

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[]
for h in hs:
    _,_,R=curvature_proxy(float(h));W,_,_=weyl_proxy(R);I3=weyl_cubic(W)
    cell=(h**4)*I3
    rows.append({'h':float(h),'weyl_cubic':float(I3),'h4_weyl_cubic_cell_proxy':float(cell),'abs_cell_proxy':float(abs(cell))})
cellabs=np.array([r['abs_cell_proxy'] for r in rows])
slope=float(np.polyfit(np.log(hs),np.log(cellabs),1)[0])
# Continuum Weyl is zero for G9, so a genuine h^4 W^3 response would have an h^4 law only on
# a Weyl-active background.  Here the extra finite-h Weyl artifact supplies ~h^3 more suppression.
assert 6.5<slope<7.8,(slope,rows)
out={
 'gate':'ITER010-G2-CELL-WEYL3-SCALING',
 'rows':rows,
 'cell_proxy_h_slope':slope,
 'target_h_power_on_nonzero_continuum_weyl_background':4,
 'classification':'BLOCKED_SCOPED_REPAIRED_G9_H4_WEYL_CUBED_CELL_PROXY_VANISHES_APPROXIMATELY_H7_RATHER_THAN_PROVIDING_A_NONZERO_H4_MATCHING_SIGNAL_BECAUSE_THE_CONTINUUM_BACKGROUND_IS_WEYL_FLAT',
 'guard':'This is a background-identifiability obstruction, not evidence that the Weyl^3 operator is absent in QGR. A same-realization non-conformally-flat microscopic background is required for an absolute c6 match.'
}
print(json.dumps(out,sort_keys=True))
