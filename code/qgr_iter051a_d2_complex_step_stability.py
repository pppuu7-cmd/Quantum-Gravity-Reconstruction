#!/usr/bin/env python3
import argparse, json, math
import numpy as np
from qgr_iter051a_weyl3_metric_density_variation import ETA, make_q, riemann_from_q, density, algebraic_controls, transform2, transform4, boost_x, generic_A, rel
EPS=[1e-16,1e-20,1e-24,1e-28,1e-30]
VALID_LANES={0,2,9}
def run(lane):
    if lane not in VALID_LANES: raise SystemExit(3)
    seed=4001+lane*131; rng=np.random.default_rng(seed)
    R=riemann_from_q(make_q(seed)); X=rng.normal(size=(4,4)); h=(X+X.T)*0.025; g=ETA.copy()
    alg,tr=algebraic_controls(R,g)
    vals=[]
    for e in EPS:
        vals.append(float(np.imag(density(g.astype(complex)+1j*e*h,R.astype(complex)))/e))
    med=float(np.median(vals)); spread=(max(vals)-min(vals))/max(abs(med),1e-12)
    cov=[]
    cs=vals[-1]
    for A in (boost_x(0.23),generic_A()):
        gt=transform2(g,A); ht=transform2(h,A); Rt=transform4(R,A); jac=abs(float(np.linalg.det(A)))
        cst=float(np.imag(density(gt.astype(complex)+1j*1e-30*ht,Rt.astype(complex)))/1e-30)
        cov.append(rel(cst/jac,cs,1e-12))
    valid=(alg<=1e-11 and tr<=1e-10 and all(math.isfinite(x) for x in vals))
    passed=valid and spread<=1e-10 and max(cov)<=1e-8
    out={'lane':lane,'seed':seed,'eps':EPS,'complex_step_values':vals,'relative_spread':spread,'covariance_direction_rel':cov,'algebraic_residual':alg,'weyl_trace_residual':tr,'valid':valid,'pass':passed}
    print(json.dumps(out,sort_keys=True))
    if not passed: raise SystemExit(2)
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); a=ap.parse_args(); run(a.lane)
