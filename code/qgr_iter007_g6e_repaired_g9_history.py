#!/usr/bin/env python3
"""Convention-repaired G9/G6D audit using covariant seed E=C^{-1}.

The QGR-L1 characteristic inverse metric is C=J-I, while the covariant flat response
is E=C^{-1}.  This script reruns the finite torsion/history calculation on that same-realization
choice rather than merely relabelling the earlier C-covariant toy.
"""
import argparse,itertools,json,math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
E=np.linalg.inv(C)
J=np.ones((4,4));S=np.eye(4)-J/6;Si=np.linalg.inv(S)
BASIS_C=np.array([
 [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
 [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
 [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
 [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
 [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
 [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
],float)
BASIS=np.array([Si@X@S for X in BASIS_C])
assert max(np.linalg.norm(X.T@E+E@X) for X in BASIS)<3e-14
avec=np.array([0.22,-0.17,0.13,0.09])
Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])
I=np.eye(4);PERMS=list(itertools.permutations(range(4)))
k0=np.array([1.,1.,1.,-1.]);u0=np.ones(4)
assert abs(k0@C@k0)<1e-14
u0sq=float(u0@E@u0);assert u0sq>0

def one(h):
 def Om(x):
  y=h*np.asarray(x,float);return math.exp(float(avec@y+0.5*y@Q@y))
 def L(z):return expm(np.tensordot(z,BASIS,axes=(0,0)))
 def residual(x,z):
  x=np.asarray(x,int);o=Om(x);Ls=[L(z[6*i:6*i+6]) for i in range(4)];out=[]
  for i in range(4):
   for j in range(i+1,4):
    xi=x.copy();xi[i]+=1;xj=x.copy();xj[j]+=1
    lhs=o*I[:,i]+np.linalg.solve(Ls[i],Om(xi)*I[:,j])
    rhs=o*I[:,j]+np.linalg.solve(Ls[j],Om(xj)*I[:,i])
    out.extend(lhs-rhs)
  return np.asarray(out)
 sols={};resnorm=[];minsv=[]
 for bits in itertools.product([0,1],repeat=4):
  s=least_squares(lambda z:residual(bits,z),np.zeros(24),xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=500)
  rn=float(np.linalg.norm(s.fun));assert rn<3e-9,(bits,rn)
  resnorm.append(rn);sv=np.linalg.svd(s.jac,compute_uv=False);minsv.append(float(sv.min()))
  Ls=[L(s.x[6*i:6*i+6]) for i in range(4)]
  assert max(np.linalg.norm(X.T@E@X-E) for X in Ls)<5e-10
  sols[bits]=Ls
 def edge(x,i):
  y=list(x);y[i]+=1;y=tuple(y)
  return (Om(x)/Om(y))*sols[tuple(x)][i]
 paths=[]
 for p in PERMS:
  x=[0,0,0,0];A=np.eye(4)
  for d in p:A=edge(tuple(x),d)@A;x[d]+=1
  paths.append(A)
 ot=Om((1,1,1,1));Gt=(ot**2)*E;Bt=C/(ot**2)
 # Exact compatibility target/source up to nonlinear-solve tolerance.
 metric_err=max(float(np.linalg.norm(A.T@Gt@A-E)) for A in paths)
 assert metric_err<2e-8,metric_err
 ks=np.array([np.linalg.solve(A.T,k0) for A in paths])
 null=np.einsum('ni,ij,nj->n',ks,Bt,ks)
 assert np.max(np.abs(null))<2e-8
 gram=ks@Bt@ks.T;mask=~np.eye(24,dtype=bool);goff=gram[mask]
 traces=[]
 for p in range(24):
  for q in range(24):
   if p!=q:traces.append(float(np.trace(np.linalg.solve(paths[q],paths[p]))-4))
 # Transport the unique S4-invariant barycentric vector.  Each branch preserves
 # its timelike norm, but need not coincide with the intrinsic target barycenter.
 us=np.array([A@u0 for A in paths])
 usq=np.einsum('ni,ij,nj->n',us,Gt,us)
 assert np.max(np.abs(usq-u0sq))<2e-8
 pair_u=[]
 for p in range(24):
  for q in range(24):
   if p!=q:
    pair_u.append(float((us[p]@Gt@us[q])/math.sqrt(usq[p]*usq[q])-1.0))
 utsq=float(u0@Gt@u0)
 intrinsic=np.array([(u@Gt@u0)/math.sqrt((u@Gt@u)*utsq)-1.0 for u in us])
 return {
  'h':h,'target_omega':ot,'max_torsion_residual':max(resnorm),'min_torsion_jacobian_singular':min(minsv),
  'max_path_metric_compatibility_error':metric_err,'max_target_null_residual':float(np.max(np.abs(null))),
  'history_relative_trace_rms':float(np.sqrt(np.mean(np.square(traces)))),
  'common_target_null_gram_rms':float(np.sqrt(np.mean(goff**2))),
  'branch_barycentric_pair_rapidity_scalar_rms':float(np.sqrt(np.mean(np.square(pair_u)))),
  'intrinsic_target_vs_transport_barycenter_scalar_rms':float(np.sqrt(np.mean(intrinsic**2))),
 }

hs=[0.5,0.25,0.125,0.0625]
rows=[one(h) for h in hs]
def slope(key):return float(np.polyfit(np.log(hs),np.log([r[key] for r in rows]),1)[0])
slopes={k:slope(k) for k in ['history_relative_trace_rms','common_target_null_gram_rms','branch_barycentric_pair_rapidity_scalar_rms','intrinsic_target_vs_transport_barycenter_scalar_rms']}
for k in ['history_relative_trace_rms','common_target_null_gram_rms','branch_barycentric_pair_rapidity_scalar_rms']:
 assert 3.7<slopes[k]<4.35,(k,slopes[k],rows)
# The common intrinsic observer differs from a parallel-transported observer already at smooth O(h)
# in vector displacement, hence its cosh-1 scalar is naturally O(h^2); it is not a history-decoherence diagnostic.
assert 1.5<slopes['intrinsic_target_vs_transport_barycenter_scalar_rms']<2.3,slopes
out={
 'lane':'CONVENTION_REPAIRED_G9_HISTORY',
 'covariant_seed':'E=C^-1',
 'characteristic_inverse_metric':'C',
 'source_qgr_l1_null_covector':[1,1,1,-1],
 'source_barycentric_vector':[1,1,1,1],
 'history_count':24,'rows':rows,'log_h_slopes':slopes,
 'classification':'PASS_SCOPED_REPAIRED_E_COVARIANT_FINITE_TORSION_BRANCH_AND_QGR_L1_NULL_HISTORY_SPREAD__HISTORY_INVARIANTS_SCALE_H4',
 'scientific_interpretation':'Rerunning the microscopic finite torsion construction with the Iter005-consistent covariant seed E=C^-1 preserves a regular finite-curvature branch. The QGR-L1 null covector remains null after every one of the 24 path transports in the common target metric. Relative holonomy trace, null-cone Gram separation, and branch-to-branch barycentric rapidity separation all scale approximately as h^4 on the refinement sequence. The intrinsic target observer differs from any transported observer at the ordinary smooth-connection level (cosh-1 about h^2), but the history-dependent branch spread is two orders higher.',
 'guard':'This repairs the C/E same-realization convention for the tested finite-curvature toy. It remains a numerical regular-branch result, not a global strong-curvature theorem or a quantum purity prediction.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
