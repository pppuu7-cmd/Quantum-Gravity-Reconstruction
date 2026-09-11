#!/usr/bin/env python3
"""Branch-symmetric common-target null-bundle Gram audit on the Iter006 G9 background."""
import argparse,itertools,json,math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
E=np.linalg.inv(C)
BASIS=np.array([
 [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
 [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
 [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
 [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
 [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
 [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
],float)
avec=np.array([0.22,-0.17,0.13,0.09]);Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])
I=np.eye(4);PERMS=list(itertools.permutations(range(4)));k0=np.array([1.,1.,1.,0.])
assert abs(k0@E@k0)<1e-14

def one(h):
 def Om(x):
  y=h*np.asarray(x,float);return math.exp(float(avec@y+0.5*y@Q@y))
 def L(z):return expm(np.tensordot(z,BASIS,axes=(0,0)))
 def residual(x,z):
  x=np.asarray(x,int);o=Om(x);Ls=[L(z[6*i:6*i+6]) for i in range(4)];out=[]
  for i in range(4):
   for j in range(i+1,4):
    xi=x.copy();xi[i]+=1;xj=x.copy();xj[j]+=1
    lhs=o*I[:,i]+np.linalg.solve(Ls[i],Om(xi)*I[:,j]);rhs=o*I[:,j]+np.linalg.solve(Ls[j],Om(xj)*I[:,i]);out.extend(lhs-rhs)
  return np.asarray(out)
 sols={}
 for bits in itertools.product([0,1],repeat=4):
  s=least_squares(lambda z:residual(bits,z),np.zeros(24),xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=400)
  assert np.linalg.norm(s.fun)<2e-9
  sols[bits]=[L(s.x[6*i:6*i+6]) for i in range(4)]
 def edge(x,i):
  y=list(x);y[i]+=1;y=tuple(y)
  return (Om(x)/Om(y))*sols[tuple(x)][i]
 paths=[]
 for p in PERMS:
  x=[0,0,0,0];A=np.eye(4)
  for d in p:A=edge(tuple(x),d)@A;x[d]+=1
  paths.append(A)
 # A maps source vectors to target vectors, so target covector is A^{-T} k0.
 ks=np.array([np.linalg.solve(A.T,k0) for A in paths])
 Bt=E/(Om((1,1,1,1))**2)
 nulls=np.einsum('ni,ij,nj->n',ks,Bt,ks)
 assert np.max(np.abs(nulls))<1e-9
 Gram=ks@Bt@ks.T
 off=Gram[~np.eye(24,dtype=bool)]
 # Branch mean and centered coordinate covariance are diagnostic only; Gram is frame-scalar.
 mean=ks.mean(axis=0);center=ks-mean;cov=center.T@center/24
 return {
  'h':h,
  'max_target_null_residual':float(np.max(np.abs(nulls))),
  'offdiag_gram_rms':float(np.sqrt(np.mean(off**2))),
  'offdiag_gram_mean_abs':float(np.mean(np.abs(off))),
  'offdiag_gram_max_abs':float(np.max(np.abs(off))),
  'coordinate_centered_cov_trace':float(np.trace(cov)),
 }
rows=[one(h) for h in [1.,0.5,0.25,0.125]]
logh=np.log([r['h'] for r in rows]);gr=np.array([r['offdiag_gram_rms'] for r in rows]);ct=np.array([r['coordinate_centered_cov_trace'] for r in rows])
slope_g=float(np.polyfit(logh,np.log(gr),1)[0]);slope_c=float(np.polyfit(logh,np.log(ct),1)[0])
assert 3.7<slope_g<4.3,(slope_g,rows)
assert 3.7<slope_c<4.3,(slope_c,rows)
scaled=[r['offdiag_gram_rms']/r['h']**4 for r in rows]
out={
 'lane':'CURVED_NULL_BUNDLE_GRAM',
 'source_null_covector':[1,1,1,0],
 'history_count':24,
 'rows':rows,
 'offdiag_gram_rms_log_h_slope':slope_g,
 'coordinate_cov_trace_log_h_slope':slope_c,
 'offdiag_gram_rms_over_h4':scaled,
 'classification':'NUMERICALLY_VERIFIED_SCOPED_BRANCH_SYMMETRIC_COMMON_TARGET_NULL_COVECTOR_GRAM_SPREAD_IS_NONZERO_AND_SCALES_AS_H4_ON_G9',
 'scientific_interpretation':'Each curved history transports the same source null covector to a target null covector using the same finite QGR path transport. The 24x24 matrix s_pq=k_p^T G_target^{-1} k_q is common-target frame invariant and branch-permutation covariant. Its off-diagonal RMS is nonzero and scales as h^4, providing a basis-free bundle-separation observable before choosing a two-polarization detector basis.',
 'guard':'This is a characteristic-bundle/path-transport observable, not yet the quantum two-mode density matrix or purity. The source covector normalization is inherited and fixed across branches; phenomenological frequency normalization is not fixed here.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
