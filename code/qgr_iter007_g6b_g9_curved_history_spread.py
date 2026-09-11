#!/usr/bin/env python3
"""Curved B4 history-spread audit on the existing Iter006 G9 conformal background.

Constructs all 24 opposite-vertex path transports on a physical cell of size h,
forms reference-free pairwise relative holonomies, and uses trace(H)-4 as a
frame-gauge-conjugation invariant branch-spread diagnostic. Numerical scoped test.
"""
import argparse, itertools, json, math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()
C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
B=np.array([
    [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
    [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
    [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
    [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
    [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
    [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
],dtype=float)
assert max(np.linalg.norm(X.T@C+C@X) for X in B)<1e-12
avec=np.array([0.22,-0.17,0.13,0.09])
Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])
I=np.eye(4)
PERMS=list(itertools.permutations(range(4)))

def run_scale(h):
    def Omega(x):
        y=h*np.asarray(x,dtype=float)
        return math.exp(float(avec@y + 0.5*y@Q@y))
    def L_from(p6):
        return expm(np.tensordot(p6,B,axes=(0,0)))
    def residual(x,z):
        x=np.asarray(x,dtype=int); Om=Omega(x)
        L=[L_from(z[6*i:6*i+6]) for i in range(4)]
        out=[]
        for i in range(4):
            for j in range(i+1,4):
                xi=x.copy(); xi[i]+=1
                xj=x.copy(); xj[j]+=1
                lhs=Om*I[:,i] + np.linalg.solve(L[i],Omega(xi)*I[:,j])
                rhs=Om*I[:,j] + np.linalg.solve(L[j],Omega(xj)*I[:,i])
                out.extend(lhs-rhs)
        return np.asarray(out)
    def solve(x):
        return least_squares(lambda z:residual(x,z),np.zeros(24),xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=400)
    def Ls(sol):
        return [L_from(sol.x[6*i:6*i+6]) for i in range(4)]

    sols={}
    for bits in itertools.product([0,1],repeat=4):
        s=solve(np.array(bits,dtype=int))
        assert np.linalg.norm(s.fun)<2e-9,(h,bits,np.linalg.norm(s.fun))
        sols[bits]=s
    Lm={bits:Ls(s) for bits,s in sols.items()}

    def Aedge(x,i):
        y=list(x); y[i]+=1; y=tuple(y)
        # A_wv = F_w^-1 L_wv F_v with F=Omega I.
        return (Omega(x)/Omega(y))*Lm[tuple(x)][i]

    paths=[]
    for p in PERMS:
        x=[0,0,0,0]; A=np.eye(4)
        for d in p:
            A=Aedge(tuple(x),d)@A
            x[d]+=1
        assert tuple(x)==(1,1,1,1)
        paths.append(A)

    deltas=[]; metric_errors=[]; det_errors=[]
    for Ap in paths:
        for Aq in paths:
            H=np.linalg.inv(Aq)@Ap
            deltas.append(float(np.real(np.trace(H))-4.0))
            metric_errors.append(float(np.linalg.norm(H.T@C@H-C)))
            det_errors.append(float(abs(np.linalg.det(H)-1.0)))
    d=np.asarray(deltas)
    return {
      'h':h,
      'path_count':len(paths),
      'ordered_path_pair_count':len(deltas),
      'mean_trace_delta':float(d.mean()),
      'mean_abs_trace_delta':float(np.abs(d).mean()),
      'rms_trace_delta':float(np.sqrt(np.mean(d*d))),
      'max_abs_trace_delta':float(np.max(np.abs(d))),
      'max_relative_loop_metric_error':max(metric_errors),
      'max_relative_loop_det_error':max(det_errors),
      'max_torsion_residual':max(float(np.linalg.norm(s.fun)) for s in sols.values()),
    }

hs=[1.0,0.5,0.25,0.125]
rows=[run_scale(h) for h in hs]
logh=np.log(np.asarray(hs))
rms=np.asarray([r['rms_trace_delta'] for r in rows])
meanabs=np.asarray([r['mean_abs_trace_delta'] for r in rows])
slope_rms=float(np.polyfit(logh,np.log(rms),1)[0])
slope_abs=float(np.polyfit(logh,np.log(meanabs),1)[0])
assert 3.8<slope_rms<4.2,slope_rms
assert 3.8<slope_abs<4.2,slope_abs
assert max(r['max_relative_loop_metric_error'] for r in rows)<1e-9
assert max(r['max_relative_loop_det_error'] for r in rows)<1e-9
# Scaled coefficient should remain finite/nonzero into the refined cells.
scaled=[r['rms_trace_delta']/r['h']**4 for r in rows]
assert min(scaled)>0.03 and max(scaled)<0.07,scaled

out={
  'lane':'G9_CURVED_24_HISTORY_GAUGE_INVARIANT_SPREAD',
  'background':'Iter006 G9 deterministic conformal frame, evaluated on cells of physical size h',
  'rows':rows,
  'fitted_rms_log_h_slope':slope_rms,
  'fitted_mean_abs_log_h_slope':slope_abs,
  'rms_trace_delta_over_h4':scaled,
  'classification':'NUMERICALLY_VERIFIED_SCOPED_CURVED_B4_PAIRWISE_HISTORY_HOLONOMY_TRACE_SPREAD_IS_NONZERO_AND_SCALES_AS_H4',
  'scientific_interpretation':'All 24 opposite-vertex transports are constructed from the same already-tested G9 torsion-free connection. The reference-free ordered-pair observable tr(A_q^-1 A_p)-4 is invariant under endpoint frame conjugation. Its RMS is nonzero at finite h and scales approximately h^4 under refinement, as expected because relative holonomy starts at O(h^2) while the Lorentz-algebra generator is traceless so the trace displacement begins quadratically.',
  'consequence':'QGR now has a concrete curved-background, dimensionless, branch-permutation-symmetric history-spread diagnostic at the same h^4 order as the leading traced quantum history correction. This is not yet the two-mode purity prediction.',
  'guard':'Numerical result on the deterministic G9 regular branch only. Trace spread is a classical/path-holonomy diagnostic, not experimental decoherence and not a substitute for the physical two-mode quantum readout map.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
