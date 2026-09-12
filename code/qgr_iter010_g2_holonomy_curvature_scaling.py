#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g2_common import curvature_proxy,pair_symmetry_error

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[]
for h in hs:
    dat,X,R=curvature_proxy(float(h))
    xrms=float(np.sqrt(np.mean([np.linalg.norm(M)**2 for M in X.values()])))
    rows.append({
      'h':float(h),
      'plane_log_rms':xrms,
      'plane_log_over_h2':xrms/(h*h),
      'riemann_proxy_norm':float(np.linalg.norm(R)),
      'pair_symmetry_relative_error':pair_symmetry_error(R),
      'max_torsion_residual':float(dat['max_torsion_residual'])
    })
slope=float(np.polyfit(np.log(hs),np.log([r['plane_log_rms'] for r in rows]),1)[0])
pair_slope=float(np.polyfit(np.log(hs),np.log([r['pair_symmetry_relative_error'] for r in rows]),1)[0])
assert 1.85<slope<2.15,(slope,rows)
assert 0.7<pair_slope<1.3,(pair_slope,rows)
assert max(r['max_torsion_residual'] for r in rows)<3e-9
out={
 'gate':'ITER010-G2-HOLONOMY-CURVATURE-SCALING',
 'rows':rows,
 'plane_log_h_slope':slope,
 'pair_symmetry_error_h_slope':pair_slope,
 'classification':'PASS_SCOPED_REPAIRED_G9_ADJACENT_SWAP_HOLONOMY_LOGS_SCALE_H2_AND_DEFINE_A_FINITE_CURVATURE_PROXY_WHILE_RIEMANN_PAIR_SYMMETRY_ERROR_VANISHES_LINEARLY',
 'guard':'This establishes a controlled finite-cell curvature proxy on the existing background; it does not by itself define a unique six-derivative action or c6 normalization.'
}
print(json.dumps(out,sort_keys=True))
