#!/usr/bin/env python3
import json, numpy as np
from qgr_iter011_g1_common import flat_subtracted

hs=np.array([0.5,0.25,0.125,0.0625,0.03125],float)
rows=[flat_subtracted(float(h),0.08) for h in hs]
y=np.array([abs(r['delta_sum_logabsdet']) for r in rows])
mask=y>1e-14
slope=float(np.polyfit(np.log(hs[mask]),np.log(y[mask]),1)[0]) if mask.sum()>=3 else float('nan')
out={
 'gate':'ITER011-G1-JACOBIAN-REFINEMENT-SCALING',
 'rows':[{k:r[k] for k in ('h','kappa','delta_sum_logabsdet','delta_mean_logabsdet','max_residual','min_sv','max_omega_norm')} for r in rows],
 'flat_subtracted_abs_h_slope':slope,
 'classification':'MEASURE_SECTOR_SCALING_NUMERIC',
 'guard':'This is the torsion-Jacobian factor only. Haar-coordinate Jacobians and any coherent Lorentzian phase remain separate.'
}
print(json.dumps(out,sort_keys=True))
