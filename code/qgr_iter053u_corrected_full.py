#!/usr/bin/env python3
"""Conditional Iter053U reference implementation.

DO NOT EXECUTE AS AUTHORITATIVE SCIENCE unless the execution lock in
preregistration/ITER053U_CORRECTED_FULL_COMPACT_SUPPORT_VARIATION_CONDITIONAL.md
has been satisfied by both terminal Iter053T gates.

A/B and C-base/direct reuse the frozen Iter053R routines.  The sole scientific
correction is the transformed C weighted polynomial-source extraction.
"""
from __future__ import annotations

import argparse
import json
import math
import os

import numpy as np

import qgr_iter053r_weighted_h5_compact_support as r
import qgr_iter053_compact_support_action as g53
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c

GATE="ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION"


def retag(d):
    out=dict(d)
    out["gate"]=GATE
    out["iter053u_execution_lock"]="MUST_BE_AUTHORIZED_BY_TERMINAL_ITER053T_PRIMARY_AND_NODEWISE_PASS"
    return out


def corrected_weighted_bulk_transformed(mt, source_pert, L, Linv, order, sample=False):
    """Weighted transformed side using exactly one external support factor.

    `source_pert` is the original CompactPerturbation.  Its `.base` member is
    the unfactored polynomial tensor p(u).  The transformed polynomial is
    L^T p(u) L while geometry is evaluated at y=L^-1 u.
    """
    bulk=0.0; wrong=0.0; sig=True; inv=0.0; max_h=0.0; max_p=0.0; max_w3=0.0
    for u,wt in r.gj_tasks(order):
        y=np.asarray(Linv@u,float)
        s,iv,_=d2n.extended_controls(mt,y); sig=sig and s; inv=max(inv,iv)
        H,z=d2n.assemble_minus5(mt,y,r.HSTEP)
        p=np.asarray(source_pert.base.jets(u)[0],float)
        py=np.asarray(L.T@p@L,float)
        sg=math.sqrt(-float(np.linalg.det(z['g'])))
        Hwrong=z['A']+z['I']+2.0*sg*z['D']
        bulk+=wt*float(np.einsum('ab,ab->',H,py))
        wrong+=wt*float(np.einsum('ab,ab->',Hwrong,py))
        if sample:
            # Keep sample fields schema-compatible with Iter053R.  C lanes do
            # not use them scientifically, but deterministic zero defaults are
            # avoided by recording the same available H/P norms.
            max_h=max(max_h,float(np.linalg.norm(H)))
            max_p=max(max_p,float(np.linalg.norm(z['P'])))
    return {
        'order':order,'bulk':float(bulk),'wrong_bulk':float(wrong),
        'signature_valid':bool(sig),'max_inverse_residual':float(inv),
        'sample_max_H_norm':float(max_h),'sample_max_P_norm':float(max_p),
        'sample_max_abs_W3':float(max_w3),
        'source_extraction':'UNFACTORED_SOURCE_POLYNOMIAL_THEN_LTpL',
    }


def analyze_corrected_transformed(metric,pert,L,Linv):
    mt=c.TransformMetric(metric,L)
    pt=it.TransformPerturbation(pert,L)
    mapper=lambda u:Linv@u

    # Direct path is intentionally the historical full transformed compact
    # perturbation path and is not replaced by the reduced polynomial source.
    d7=r.support_direct(mt,pt,7,mapper)
    d8=r.support_direct(mt,pt,8,mapper)

    # Only weighted source extraction is corrected.
    g2=corrected_weighted_bulk_transformed(mt,pert,L,Linv,2)
    g3=corrected_weighted_bulk_transformed(mt,pert,L,Linv,3)

    direct=np.array(d8['direct'],float)
    dstep=r.rel(direct[-1],direct[-2])
    glchange=r.rel(d7['direct'][-1],direct[-1])
    bchange=r.rel(g2['bulk'],g3['bulk'])
    resid=r.rel(direct[-1],g3['bulk'])
    cres=r.rel(d7['direct'][-1],g2['bulk'])
    qchange=abs(resid-cres)
    wrongres=r.rel(direct[-1],g3['wrong_bulk'])
    collar=r.collar_control_frame(pt,mapper)
    nums=[*d7['direct'],*d8['direct'],g2['bulk'],g3['bulk'],g3['wrong_bulk'],
          dstep,glchange,bchange,resid,cres,qchange,wrongres,collar]
    valid=bool(
        d7['signature_valid'] and d8['signature_valid'] and
        g2['signature_valid'] and g3['signature_valid'] and
        max(d7['max_inverse_residual'],d8['max_inverse_residual'],
            g2['max_inverse_residual'],g3['max_inverse_residual'])<=3e-11 and
        collar<=1e-13 and np.isfinite(nums).all()
    )
    passed=bool(
        valid and abs(direct[-1])>=1e-10 and dstep<=5e-4 and
        glchange<=5e-4 and bchange<=2e-3 and resid<=3e-3 and
        qchange<=3e-3 and wrongres>resid
    )
    return {
        'direct_GL7':d7,'direct_GL8':d8,'GJ2':g2,'GJ3':g3,
        'direct_final_step_change':dstep,
        'direct_GL7_to_GL8_relative_change':glchange,
        'weighted_bulk_GJ2_to_GJ3_relative_change':bchange,
        'identity_relative_residual':resid,
        'coarse_identity_relative_residual':cres,
        'coarse_to_fine_identity_residual_change_abs':qchange,
        'wrong_sign_relative_residual':wrongres,
        'collar_residual':collar,
        'control_valid':valid,'generic_pass':passed,
        'weighted_source_path':'CORRECTED_SOURCE_FAITHFUL_SINGLE_WEIGHT',
    }


def lane_a(i):
    return retag(r.lane_a(i))


def lane_b(i):
    return retag(r.lane_b(i))


def lane_c(i):
    metric,pert,mseed,pseed=r.lane_objects('C',i)
    L=it.shear(i); Linv=np.linalg.inv(L)
    mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)

    vals=[]
    for u in (np.zeros(r.N),np.array([0.08,-0.06,0.05,-0.04])):
        y=Linv@u
        g=metric.jets(u)[0]; gt=mt.jets(y)[0]
        h=pert.jets(u)[0]; ht=pt.jets(y)[0]
        vals.extend([
            float(np.max(np.abs(gt-L.T@g@L))),
            float(np.max(np.abs(ht-L.T@h@L)))
        ])
    tres=max(vals); detres=abs(float(np.linalg.det(L))-1.0)

    # Base side is the exact historical Iter053R mathematical path.
    base=r.analyze_generic(metric,pert)
    # Transformed side changes only weighted polynomial-source extraction.
    transformed=analyze_corrected_transformed(metric,pert,L,Linv)

    dcov=r.rel(base['direct_GL8']['direct'][-1],transformed['direct_GL8']['direct'][-1])
    bcov=r.rel(base['GJ3']['bulk'],transformed['GJ3']['bulk'])
    valid=bool(base['control_valid'] and transformed['control_valid'] and detres<=2e-12 and tres<=3e-11)
    passed=bool(valid and base['generic_pass'] and transformed['generic_pass'] and dcov<=2e-3 and bcov<=2e-3)

    return {
        'gate':GATE,'stream':'C','index':i,
        'metric_seed':mseed,'perturbation_seed':pseed,
        'det_L':float(np.linalg.det(L)),'transform_algebra_residual':tres,
        'base':base,'transformed':transformed,
        'direct_covariance_relative_residual':dcov,
        'bulk_covariance_relative_residual':bcov,
        'control_valid':valid,'lane_pass':passed,
        'iter053u_execution_lock':'MUST_BE_AUTHORIZED_BY_TERMINAL_ITER053T_PRIMARY_AND_NODEWISE_PASS',
        'scientific_change_scope':'ONLY_TRANSFORMED_WEIGHTED_POLYNOMIAL_SOURCE_EXTRACTION',
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=['A','B','C'],required=True)
    ap.add_argument('--index',type=int,required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    lim={'A':4,'B':2,'C':2}[a.stream]
    if not 0<=a.index<lim: raise SystemExit('index out of range')
    out={'A':lane_a,'B':lane_b,'C':lane_c}[a.stream](a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
