#!/usr/bin/env python3
import argparse, json
import numpy as np
from qgr_iter051a_weyl3_metric_density_variation import (
    ETA, make_q, riemann_from_q, density, algebraic_controls,
    transform2, transform4, boost_x, generic_A, rel, signature_ok
)

GRID=[1.6e-3,8e-4,4e-4,2e-4,1e-4,5e-5,2.5e-5,1.25e-5]
ORIG=[2e-4,1e-4,5e-5,2.5e-5]

def eval_lane(lane):
    seed=4001+lane*131
    rng=np.random.default_rng(seed)
    R=riemann_from_q(make_q(seed))
    X=rng.normal(size=(4,4)); h=(X+X.T)*0.025
    g=ETA.copy()
    alg_res,tr_res=algebraic_controls(R,g)
    L0=density(g,R)
    cs_eps=1e-30
    cs=float(np.imag(density(g.astype(complex)+1j*cs_eps*h,R.astype(complex)))/cs_eps)

    def fd_at(e):
        gp=g+e*h; gm=g-e*h
        sig=signature_ok(gp) and signature_ok(gm)
        fd=float(np.real((density(gp,R)-density(gm,R))/(2*e)))
        return fd,sig

    fds=[]; errs=[]; sigs=[]
    for e in GRID:
        fd,sig=fd_at(e); fds.append(fd); errs.append(abs(fd-cs)); sigs.append(sig)
    min_i=int(np.argmin(errs)); min_err=float(errs[min_i]); final_err=float(errs[-1])
    min_rel=rel(fds[min_i],cs,1e-12)
    turnover=(min_i <= len(GRID)-3) and (final_err >= 1.5*max(min_err,1e-30))

    orig_fds=[]; orig_errs=[]
    for e in ORIG:
        fd,_=fd_at(e); orig_fds.append(fd); orig_errs.append(abs(fd-cs))
    orig_finest_rel=rel(orig_fds[-1],cs,1e-12)
    orig_conv=(orig_errs[-1] <= 1.05*orig_errs[-2]) and ((orig_errs[-1] < 1e-10) or (orig_errs[-2]/max(orig_errs[-1],1e-30) >= 2.5))
    orig_derivative_ok=(orig_finest_rel<=2e-6 or abs(orig_fds[-1]-cs)<=1e-9) and orig_conv

    cov=[]
    for A in (boost_x(0.23),generic_A()):
        gt=transform2(g,A); ht=transform2(h,A); Rt=transform4(R,A)
        jac=abs(float(np.linalg.det(A)))
        Lt=density(gt,Rt)
        cst=float(np.imag(density(gt.astype(complex)+1j*cs_eps*ht,Rt.astype(complex)))/cs_eps)
        cov.append({'density_rel':rel(float(np.real(Lt))/jac,float(np.real(L0)),1e-12),
                    'direction_rel':rel(cst/jac,cs,1e-12)})
    valid=all(sigs) and alg_res<=1e-11 and tr_res<=1e-10
    covariance_ok=max(x['density_rel'] for x in cov)<=1e-9 and max(x['direction_rel'] for x in cov)<=1e-8
    localized=valid and covariance_ok and (min_rel<=2e-6 or min_err<=1e-9) and turnover
    return {
      'lane':lane,'seed':seed,'grid':GRID,'fd':fds,'errors':errs,'complex_step_directional':cs,
      'minimum_index':min_i,'minimum_step':GRID[min_i],'minimum_abs_error':min_err,'minimum_rel':min_rel,
      'final_abs_error':final_err,'turnover':turnover,'algebraic_residual':alg_res,
      'weyl_trace_residual':tr_res,'covariance':cov,'valid':valid,'covariance_ok':covariance_ok,
      'original_g51a_derivative_ok':orig_derivative_ok,
      'original_g51a_pass_recomputed':bool(valid and covariance_ok and orig_derivative_ok),
      'diagnostic_classification':'ROUND_OFF_TURNOVER_LOCALIZED' if localized else 'DERIVATIVE_DISCREPANCY_NOT_LOCALIZED_AS_ROUNDOFF'
    }

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',type=int,required=True); a=ap.parse_args()
    print(json.dumps(eval_lane(a.lane),sort_keys=True))
