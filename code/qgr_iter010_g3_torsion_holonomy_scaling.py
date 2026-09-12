#!/usr/bin/env python3
import json
import numpy as np
from qgr_iter010_g3_common import plane_logs

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[]
for h in hs:
    dat,X=plane_logs(float(h),0.08)
    xrms=float(np.sqrt(np.mean([np.linalg.norm(M)**2 for M in X.values()])))
    rows.append({'h':float(h),'plane_log_rms':xrms,'plane_log_over_h2':xrms/(h*h),'max_torsion_residual':float(dat['max_torsion_residual']),'min_jacobian_singular':float(dat['min_jacobian_singular'])})
slope=float(np.polyfit(np.log(hs),np.log([r['plane_log_rms'] for r in rows]),1)[0])
assert 1.85<slope<2.15,(slope,rows)
assert max(r['max_torsion_residual'] for r in rows)<3e-9
assert min(r['min_jacobian_singular'] for r in rows)>0.25
out={
 'gate':'ITER010-G3-TORSION-HOLONOMY-SCALING',
 'rows':rows,
 'plane_log_h_slope':slope,
 'classification':'PASS_SCOPED_GENERAL_TETRAD_WEYL_ACTIVE_BACKGROUND_HAS_STABLE_UNIQUE_NUMERIC_TORSION_SOLVES_AND_RELATIVE_HOLONOMY_LOGS_SCALE_H2',
 'guard':'The positive Jacobian singular-value margin is numerical on the tested weak-curvature sequence; it is not a global strong-curvature uniqueness theorem.'
}
print(json.dumps(out,sort_keys=True))
