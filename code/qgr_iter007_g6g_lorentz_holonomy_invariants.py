#!/usr/bin/env python3
import argparse,itertools,json
import numpy as np
from scipy.linalg import logm
from qgr_iter007_g6g_common import solve_paths,to_minkowski
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()

def one(h):
 dat=solve_paths(h);Ls=dat['L_paths'];I1=[];I2=[];Xn=[];tr=[]
 for p,q in itertools.combinations(range(24),2):
  H=np.linalg.solve(Ls[q],Ls[p]);Lam=to_minkowski(H);X=np.real_if_close(logm(Lam),tol=1000).real
  assert np.linalg.norm(X.T@np.diag([1.,-1.,-1.,-1.])+np.diag([1.,-1.,-1.,-1.])@X)<2e-7
  b=np.array([X[0,1],X[0,2],X[0,3]])
  O=X[1:,1:];r=np.array([-O[1,2],O[0,2],-O[0,1]])
  I1.append(float(r@r-b@b));I2.append(float(r@b));Xn.append(float(np.linalg.norm(X)));tr.append(float(np.trace(Lam)-4))
 return {'h':h,'lie_generator_rms':float(np.sqrt(np.mean(np.square(Xn)))),'casimir_r2_minus_b2_rms':float(np.sqrt(np.mean(np.square(I1)))),'casimir_r_dot_b_rms':float(np.sqrt(np.mean(np.square(I2)))),'relative_trace_rms':float(np.sqrt(np.mean(np.square(tr)))),'max_torsion_residual':dat['max_torsion_residual'],'min_torsion_jacobian_singular':dat['min_jacobian_singular']}
hs=[.5,.25,.125,.0625,.03125];rows=[one(h) for h in hs]
def slope(key):return float(np.polyfit(np.log(hs),np.log([r[key] for r in rows]),1)[0])
sl={k:slope(k) for k in ['lie_generator_rms','casimir_r2_minus_b2_rms','casimir_r_dot_b_rms','relative_trace_rms']}
assert 1.8<sl['lie_generator_rms']<2.2,sl
for k in ['casimir_r2_minus_b2_rms','casimir_r_dot_b_rms','relative_trace_rms']:assert 3.7<sl[k]<4.35,(k,sl[k])
out={'lane':'RELATIVE_LORENTZ_HOLONOMY_INVARIANTS','rows':rows,'log_h_slopes':sl,'classification':'NUMERICALLY_VERIFIED_SCOPED_RELATIVE_HISTORY_LORENTZ_GENERATOR_IS_H2_WHILE_BASIS_INVARIANT_LORENTZ_CASIMIRS_ARE_H4_ON_REPAIRED_G9','scientific_interpretation':'The branch-to-branch relative finite transports are genuine Lorentz holonomies after removing the common conformal endpoint scale. Their Lie-algebra displacement is O(h^2), while the two quadratic Lorentz-algebra Casimirs and the finite trace defect are O(h^4). Thus the h^4 history signal is not an artifact of one trace diagnostic: it is also present in basis-independent boost/rotation holonomy invariants.','guard':'The Casimirs characterize relative classical/one-particle holonomy. They do not by themselves specify a prepared polarization state, detector axis, or quantum decoherence probability.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
