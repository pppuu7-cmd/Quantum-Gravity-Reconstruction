#!/usr/bin/env python3
"""Conditional Iter053U final reference implementation.

DO NOT EXECUTE AS AUTHORITATIVE SCIENCE unless the execution lock in
preregistration/ITER053U_CORRECTED_FULL_COMPACT_SUPPORT_VARIATION_CONDITIONAL.md
has been satisfied by both terminal Iter053T gates.

Scientific contract:
- direct compact-support action paths remain the historical Iter053R object;
- all weighted H5 paths use the separately validated h=5e-4 canonical cache;
- the sole scientific object correction is transformed C weighted polynomial
  source extraction: one external support weight and L^T p(u) L.
"""
from __future__ import annotations

import argparse
import json
import math
import os

import numpy as np

import qgr_iter053r_weighted_h5_compact_support as r
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c
import qgr_iter051b1_weyl3_p_insertion as w3
import qgr_d5_validated_cache_backend as cache_backend

GATE="ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION"
CACHE_EQUIVALENCE_RUN=34793411230
CACHE_EQUIVALENCE_CLASSIFICATION="D5_CANONICAL_CACHE_EQUIVALENCE_PASS"


def cached_weighted_bulk(metric,base_pert,order,u_to_coord=None,p_transform=None,sample=False):
    """Iter053R weighted observable with only the validated H5 backend changed."""
    bulk=0.0; wrong=0.0; sig=True; inv=0.0; max_h=0.0; max_p=0.0; max_w3=0.0
    for u,wt in r.gj_tasks(order):
        x=u if u_to_coord is None else np.asarray(u_to_coord(u),float)
        s,iv,_=d2n.extended_controls(metric,x); sig=sig and s; inv=max(inv,iv)
        H,z=cache_backend.assemble_minus5_cached(metric,x,r.HSTEP)
        p=np.asarray(base_pert.base.jets(u)[0],float)
        if p_transform is not None:
            p=np.asarray(p_transform(p),float)
        sg=math.sqrt(-float(np.linalg.det(z['g'])))
        Hwrong=z['A']+z['I']+2.0*sg*z['D']
        bulk+=wt*float(np.einsum('ab,ab->',H,p))
        wrong+=wt*float(np.einsum('ab,ab->',Hwrong,p))
        if sample:
            W3=float(np.real(w3.i3_complex(z['R'],z['g'],np.linalg.inv(z['g']))))
            max_h=max(max_h,float(np.linalg.norm(H)))
            max_p=max(max_p,float(np.linalg.norm(z['P'])))
            max_w3=max(max_w3,abs(W3))
    return {
        'order':order,'bulk':float(bulk),'wrong_bulk':float(wrong),
        'signature_valid':bool(sig),'max_inverse_residual':float(inv),
        'sample_max_H_norm':float(max_h),'sample_max_P_norm':float(max_p),
        'sample_max_abs_W3':float(max_w3),
        'h5_backend':'VALIDATED_D5_CANONICAL_CACHE_H5E-4',
        'h5_backend_validation_run':CACHE_EQUIVALENCE_RUN,
        'h5_backend_validation_classification':CACHE_EQUIVALENCE_CLASSIFICATION,
    }


def corrected_weighted_bulk_transformed(mt,source_pert,L,Linv,order,sample=False):
    out=cached_weighted_bulk(
        mt,source_pert,order,
        u_to_coord=lambda u:Linv@u,
        p_transform=lambda p:L.T@p@L,
        sample=sample,
    )
    out['source_extraction']='UNFACTORED_SOURCE_POLYNOMIAL_THEN_LTpL'
    return out


def transformed_source_object_control(source_pert,transformed_pert,L):
    """Fail closed if corrected and historical wrapper objects are identical."""
    all_equal=True; finite=True; node_count=0; differing_nodes=0
    for u,_ in r.gj_tasks(3):
        corrected=np.asarray(L.T@source_pert.base.jets(u)[0]@L,float)
        legacy=np.asarray(L.T@transformed_pert.base.jets(u)[0]@L,float)
        finite=finite and bool(np.isfinite(corrected).all() and np.isfinite(legacy).all())
        same=bool(np.array_equal(corrected,legacy))
        all_equal=all_equal and same
        differing_nodes+=int(not same); node_count+=1
    passed=bool(finite and node_count==81 and not all_equal)
    return {
        'node_count':node_count,'finite':finite,
        'historical_wrapper_object_identical_to_corrected':all_equal,
        'exactly_differing_node_count':differing_nodes,
        'control_pass':passed,
        'criterion':'REJECT_ONLY_IF_ALL_FROZEN_GJ3_SOURCE_NODES_ARE_OBJECT_IDENTICAL_OR_NONFINITE',
    }


def generic_summary(metric,pert,d7,d8,g2,g3,u_to_coord=None):
    direct=np.array(d8['direct'],float)
    dstep=r.rel(direct[-1],direct[-2])
    glchange=r.rel(d7['direct'][-1],direct[-1])
    bchange=r.rel(g2['bulk'],g3['bulk'])
    resid=r.rel(direct[-1],g3['bulk'])
    cres=r.rel(d7['direct'][-1],g2['bulk'])
    qchange=abs(resid-cres)
    wrongres=r.rel(direct[-1],g3['wrong_bulk'])
    collar=r.collar_control_frame(pert,u_to_coord)
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
        'wrong_sign_relative_residual':wrongres,'collar_residual':collar,
        'control_valid':valid,'generic_pass':passed,
    }


def analyze_generic_cached(metric,pert,u_to_coord=None,p_transform=None):
    d7=r.support_direct(metric,pert,7,u_to_coord)
    d8=r.support_direct(metric,pert,8,u_to_coord)
    g2=cached_weighted_bulk(metric,pert,2,u_to_coord,p_transform)
    g3=cached_weighted_bulk(metric,pert,3,u_to_coord,p_transform)
    return generic_summary(metric,pert,d7,d8,g2,g3,u_to_coord)


def analyze_corrected_transformed(metric,pert,L,Linv):
    mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    mapper=lambda u:Linv@u
    d7=r.support_direct(mt,pt,7,mapper)
    d8=r.support_direct(mt,pt,8,mapper)
    g2=corrected_weighted_bulk_transformed(mt,pert,L,Linv,2)
    g3=corrected_weighted_bulk_transformed(mt,pert,L,Linv,3)
    out=generic_summary(mt,pt,d7,d8,g2,g3,mapper)
    out['weighted_source_path']='CORRECTED_SOURCE_FAITHFUL_SINGLE_WEIGHT'
    return out


def lane_a(i):
    metric,pert,mseed,pseed=r.lane_objects('A',i)
    d=analyze_generic_cached(metric,pert)
    d.update({'gate':GATE,'stream':'A','index':i,'metric_seed':mseed,'perturbation_seed':pseed})
    d['lane_pass']=bool(d['control_valid'] and d['generic_pass'])
    return d


def lane_b(i):
    metric,pert,mseed,pseed=r.lane_objects('B',i)
    d7=r.support_direct(metric,pert,7); d8=r.support_direct(metric,pert,8)
    g2=cached_weighted_bulk(metric,pert,2)
    g3=cached_weighted_bulk(metric,pert,3,sample=True)
    collar=r.collar_control_frame(pert); direct=float(d8['direct'][-1]); bulk=float(g3['bulk'])
    nums=[*d7['direct'],*d8['direct'],g2['bulk'],g3['bulk'],g3['sample_max_H_norm'],
          g3['sample_max_P_norm'],g3['sample_max_abs_W3'],collar]
    valid=bool(d7['signature_valid'] and d8['signature_valid'] and g2['signature_valid'] and g3['signature_valid'] and
               max(d7['max_inverse_residual'],d8['max_inverse_residual'],g2['max_inverse_residual'],g3['max_inverse_residual'])<=3e-11 and
               collar<=1e-13 and np.isfinite(nums).all())
    passed=bool(valid and abs(direct)<=5e-8 and abs(bulk)<=5e-8 and g3['sample_max_abs_W3']<=2e-10 and
                g3['sample_max_P_norm']<=3e-9 and g3['sample_max_H_norm']<=3e-7)
    return {
        'gate':GATE,'stream':'B','index':i,'metric_seed':mseed,'perturbation_seed':pseed,
        'direct_GL7':d7,'direct_GL8':d8,'GJ2':g2,'GJ3':g3,'collar_residual':collar,
        'control_valid':valid,'lane_pass':passed,
    }


def lane_c(i):
    metric,pert,mseed,pseed=r.lane_objects('C',i)
    L=it.shear(i); Linv=np.linalg.inv(L)
    mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    vals=[]
    for x in (np.zeros(r.N),np.array([0.08,-0.06,0.05,-0.04])):
        y=Linv@x; g=metric.jets(x)[0]; gt=mt.jets(y)[0]; h=pert.jets(x)[0]; ht=pt.jets(y)[0]
        vals.extend([float(np.max(np.abs(gt-L.T@g@L))),float(np.max(np.abs(ht-L.T@h@L)))])
    tres=max(vals); detres=abs(float(np.linalg.det(L))-1.0)
    source_object=transformed_source_object_control(pert,pt,L)
    base=analyze_generic_cached(metric,pert)
    transformed=analyze_corrected_transformed(metric,pert,L,Linv)
    dcov=r.rel(base['direct_GL8']['direct'][-1],transformed['direct_GL8']['direct'][-1])
    bcov=r.rel(base['GJ3']['bulk'],transformed['GJ3']['bulk'])
    valid=bool(base['control_valid'] and transformed['control_valid'] and detres<=2e-12 and tres<=3e-11 and source_object['control_pass'])
    passed=bool(valid and base['generic_pass'] and transformed['generic_pass'] and dcov<=2e-3 and bcov<=2e-3)
    return {
        'gate':GATE,'stream':'C','index':i,'metric_seed':mseed,'perturbation_seed':pseed,
        'det_L':float(np.linalg.det(L)),'transform_algebra_residual':tres,
        'transformed_source_object_control':source_object,'base':base,'transformed':transformed,
        'direct_covariance_relative_residual':dcov,'bulk_covariance_relative_residual':bcov,
        'control_valid':valid,'lane_pass':passed,
        'iter053u_execution_lock':'MUST_BE_AUTHORIZED_BY_TERMINAL_ITER053T_PRIMARY_AND_NODEWISE_PASS',
        'scientific_change_scope':'ONLY_TRANSFORMED_WEIGHTED_POLYNOMIAL_SOURCE_EXTRACTION',
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A','B','C'],required=True)
    ap.add_argument('--index',type=int,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    lim={'A':4,'B':2,'C':2}[a.stream]
    if not 0<=a.index<lim: raise SystemExit('index out of range')
    out={'A':lane_a,'B':lane_b,'C':lane_c}[a.stream](a.index)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out,sort_keys=True))
    if not out['control_valid']: raise SystemExit(3)
    if not out['lane_pass']: raise SystemExit(2)

if __name__=='__main__': main()
