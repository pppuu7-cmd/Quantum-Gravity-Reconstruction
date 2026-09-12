#!/usr/bin/env python3
import itertools,json
import numpy as np
from scipy.linalg import logm
from qgr_iter007_g6g_common import solve_paths,to_minkowski

hs=[0.25,0.125,0.0625,0.03125,0.015625]
rows=[]
for h in hs:
    dat=solve_paths(h);Ls=dat['L_paths'];vals=[]
    for p,q in itertools.combinations(range(24),2):
        H=np.linalg.solve(Ls[q],Ls[p]);Lam=to_minkowski(H)
        X=np.real_if_close(logm(Lam),tol=1000).real
        vals.append(float(np.linalg.norm(X)))
    rms=float(np.sqrt(np.mean(np.square(vals))))
    rows.append({'h':h,'relative_generator_rms':rms,'rms_over_h2':rms/(h*h),'max_torsion_residual':dat['max_torsion_residual'],'min_jacobian_singular':dat['min_jacobian_singular']})
sl=float(np.polyfit(np.log(hs),np.log([r['relative_generator_rms'] for r in rows]),1)[0])
assert 1.8<sl<2.2,(sl,rows)
rat=[r['rms_over_h2'] for r in rows]
assert max(rat)/min(rat)<1.35,(sl,rat)
out={
  'gate':'ITER009-G5-RELATIVE-HOLONOMY-EXTENDED',
  'rows':rows,
  'log_h_slope':sl,
  'rescaled_h2_ratio_spread':max(rat)/min(rat),
  'classification':'NUMERICALLY_VERIFIED_SCOPED_REPAIRED_G9_BRANCH_RELATIVE_LORENTZ_GENERATOR_REMAINS_OH2_TO_H_1_OVER_64_WITH_BOUNDED_H_MINUS2_RESCALED_RMS',
  'guard':'Finite sampled h sequence is not a proof of a uniform all-refinement bound or an exact analytic asymptotic coefficient.'
}
print(json.dumps(out,sort_keys=True))
