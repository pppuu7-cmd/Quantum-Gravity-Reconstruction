#!/usr/bin/env python3
"""Normalized scalar-envelope history-mixture benchmark on the convention-repaired G9 branch.

This is NOT yet the full coherent two-polarization QGR purity because momentum-dependent
polarization/Wigner transport is not included. It is the normalized characteristic-envelope
factor for two explicit Lorentz-covariant preparation profiles.
"""
import argparse,itertools,json,math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
E=np.linalg.inv(C);J=np.ones((4,4));S=np.eye(4)-J/6;Si=np.linalg.inv(S)
BC=np.array([
 [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
 [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
 [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
 [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
 [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
 [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
],float)
BASIS=np.array([Si@X@S for X in BC])
avec=np.array([0.22,-0.17,0.13,0.09]);Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])
I=np.eye(4);PERMS=list(itertools.permutations(range(4)));u0=np.ones(4);u0sq=float(u0@E@u0);assert u0sq>0

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
  s=least_squares(lambda z:residual(bits,z),np.zeros(24),xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=500)
  assert np.linalg.norm(s.fun)<3e-9
  sols[bits]=[L(s.x[6*i:6*i+6]) for i in range(4)]
 def edge(x,i):
  y=list(x);y[i]+=1;y=tuple(y);return (Om(x)/Om(y))*sols[tuple(x)][i]
 paths=[]
 for p in PERMS:
  x=[0,0,0,0];A=np.eye(4)
  for d in p:A=edge(tuple(x),d)@A;x[d]+=1
  paths.append(A)
 Gt=(Om((1,1,1,1))**2)*E
 us=np.array([A@u0 for A in paths])
 norms=np.einsum('ni,ij,nj->n',us,Gt,us);assert np.max(np.abs(norms-u0sq))<2e-8
 gamma=(us@Gt@us.T)/u0sq
 assert np.max(np.abs(np.diag(gamma)-1))<2e-8
 assert np.min(gamma)>1-2e-8
 amp0=2/(1+gamma)
 amp1=4*(2+gamma)/(3*(1+gamma)**2)
 R0=float(np.mean(amp0**2));R1=float(np.mean(amp1**2))
 L0=1-R0;L1=1-R1
 assert 0<=L0<0.05 and 0<=L1<0.05
 return {'h':h,'envelope_retention_m0':R0,'envelope_loss_m0':L0,'envelope_retention_m1':R1,'envelope_loss_m1':L1,'loss_ratio_m1_over_m0':L1/L0,'gamma_minus_one_rms':float(np.sqrt(np.mean((gamma-1)**2))),'gamma_minus_one_mean':float(np.mean(gamma-1))}

hs=[0.5,0.25,0.125,0.0625,0.03125];rows=[one(h) for h in hs]
def slope(key):return float(np.polyfit(np.log(hs),np.log([r[key] for r in rows]),1)[0])
s0=slope('envelope_loss_m0');s1=slope('envelope_loss_m1');sg=slope('gamma_minus_one_rms')
assert 3.7<s0<4.35 and 3.7<s1<4.35 and 3.7<sg<4.35,(s0,s1,sg)
ratio=rows[-1]['loss_ratio_m1_over_m0'];assert abs(ratio-4/3)<2e-5,ratio
out={
 'lane':'REPAIRED_G9_ENVELOPE_PURITY',
 'history_count':24,'rows':rows,
 'log_h_slopes':{'m0_loss':s0,'m1_loss':s1,'gamma_minus_one_rms':sg},
 'asymptotic_profile_loss_ratio_m1_over_m0':ratio,
 'm0_loss_over_h4':[r['envelope_loss_m0']/r['h']**4 for r in rows],
 'm1_loss_over_h4':[r['envelope_loss_m1']/r['h']**4 for r in rows],
 'classification':'NUMERICALLY_VERIFIED_SCOPED_REPAIRED_G9_NORMALIZED_CHARACTERISTIC_ENVELOPE_HISTORY_IMPURITY_SCALES_H4_WITH_PREPARATION_DEPENDENT_COEFFICIENT',
 'scientific_interpretation':'On the convention-repaired finite-curvature branch, the 24 history-transported timelike preparation labels have pairwise gamma-1 of order h^4. For two fully normalized Lorentz-covariant null-envelope families, the equal-history mixture loses envelope purity with the same fitted h^4 order. The asymptotic m1/m0 loss ratio tends to the analytic 4/3 profile coefficient. This is evidence that the refinement order is structural while the numerical coefficient is preparation dependent.',
 'guard':'This is the scalar characteristic-envelope contribution to a normalized history-mixture comparator, not yet the full coherent QGR two-polarization purity. Momentum-dependent physical polarization/Wigner holonomy and a concrete detector preparation remain open. Absolute physical h is also not fixed because kappa/h^2, not h alone, is currently matched to Newton coupling.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
