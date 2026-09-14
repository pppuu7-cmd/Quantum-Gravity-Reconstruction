#!/usr/bin/env python3
"""Guarded parallel-part kernel for conditional Iter053U.

This file prepares a faster execution graph but remains unusable until durable
recovery records both exact Iter053T PASS classifications. It preserves the
same eight Iter053U scientific lane identities; direct/weighted and C side
computations are merely separated into independent execution parts.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np

import qgr_iter053r_weighted_h5_compact_support as r
import qgr_iter053u_corrected_full as u
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_full_eom as c

GATE=u.GATE
PRIMARY="ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED"
COMPANION="ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED"
PREREG="dbb306d68e6d1fc332a73eccb88f52df0cc5859a"


def authorize(state_path):
    raw=Path(state_path).read_bytes()
    state=json.loads(raw.decode("utf-8"))
    p=state.get("iter053t_primary",{}).get("classification")
    q=state.get("iter053t_nodewise_companion",{}).get("classification")
    if p!=PRIMARY or q!=COMPANION:
        raise SystemExit("ITER053U execution unauthorized by durable terminal recovery state")
    production_sha=os.environ.get("GITHUB_SHA")
    if not production_sha:
        raise SystemExit("ITER053U production parts require GITHUB_SHA provenance")
    return {
        "production_sha":production_sha,
        "authorization_state_sha256":hashlib.sha256(raw).hexdigest(),
        "preregistration_commit":PREREG,
        "required_primary_classification":PRIMARY,
        "required_companion_classification":COMPANION,
    }


def objects(stream,index,side):
    metric,pert,mseed,pseed=r.lane_objects(stream,index)
    if side=="base":
        return metric,pert,None,None,mseed,pseed
    if stream!="C" or side!="transformed":
        raise ValueError("transformed side is frozen only for C lanes")
    L=it.shear(index); Linv=np.linalg.inv(L)
    mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    return mt,pt,L,Linv,mseed,pseed


def direct_part(stream,index,side,prov):
    metric,pert,L,Linv,mseed,pseed=objects(stream,index,side)
    mapper=(lambda x:Linv@x) if side=="transformed" else None
    d7=r.support_direct(metric,pert,7,mapper)
    d8=r.support_direct(metric,pert,8,mapper)
    return {
        "gate":GATE,"mode":"part","kind":"direct","stream":stream,"index":index,"side":side,
        "metric_seed":mseed,"perturbation_seed":pseed,"GL7":d7,"GL8":d8,
        "implementation_split":"DIRECT_PART_ONLY_SAME_FROZEN_OBJECT","provenance":prov,
    }


def weighted_part(stream,index,side,prov):
    metric0,pert0,mseed,pseed=r.lane_objects(stream,index)
    if side=="base":
        sample=(stream=="B")
        g2=r.weighted_bulk(metric0,pert0,2,sample=False)
        g3=r.weighted_bulk(metric0,pert0,3,sample=sample)
        source_control=None
    else:
        if stream!="C": raise ValueError("transformed weighted part only for C")
        L=it.shear(index); Linv=np.linalg.inv(L)
        mt=c.TransformMetric(metric0,L); pt=it.TransformPerturbation(pert0,L)
        g2=u.corrected_weighted_bulk_transformed(mt,pert0,L,Linv,2)
        g3=u.corrected_weighted_bulk_transformed(mt,pert0,L,Linv,3)
        source_control=u.transformed_source_object_control(pert0,pt,L)
    return {
        "gate":GATE,"mode":"part","kind":"weighted","stream":stream,"index":index,"side":side,
        "metric_seed":mseed,"perturbation_seed":pseed,"GJ2":g2,"GJ3":g3,
        "transformed_source_object_control":source_control,
        "implementation_split":"WEIGHTED_PART_ONLY_SAME_FROZEN_OBJECT","provenance":prov,
    }


def load_parts(root,stream,index):
    out={}
    for fn in glob.glob(os.path.join(root,"**","*.json"),recursive=True):
        try:
            with open(fn,encoding="utf-8") as f: d=json.load(f)
        except Exception:
            continue
        if d.get("gate")!=GATE or d.get("mode")!="part": continue
        if d.get("stream")!=stream or d.get("index")!=index: continue
        key=(d.get("side"),d.get("kind"))
        if key in out: raise ValueError(f"duplicate part {key}")
        out[key]=d
    return out


def common_provenance(parts):
    if not parts: raise ValueError("no parts")
    vals=[d.get("provenance") for d in parts.values()]
    if any(not isinstance(v,dict) for v in vals): raise ValueError("missing part provenance")
    ref=vals[0]
    required=("production_sha","authorization_state_sha256","preregistration_commit",
              "required_primary_classification","required_companion_classification")
    if any(not ref.get(k) for k in required): raise ValueError("incomplete reference provenance")
    if ref.get("preregistration_commit")!=PREREG: raise ValueError("wrong preregistration identity")
    if ref.get("required_primary_classification")!=PRIMARY or ref.get("required_companion_classification")!=COMPANION:
        raise ValueError("wrong authorization classification identity")
    if any(v!=ref for v in vals[1:]): raise ValueError("mixed part provenance")
    return ref


def generic_summary(dpart,wpart,metric,pert,mapper=None):
    d7=dpart["GL7"]; d8=dpart["GL8"]
    g2=wpart["GJ2"]; g3=wpart["GJ3"]
    direct=np.array(d8["direct"],float)
    dstep=r.rel(direct[-1],direct[-2])
    glchange=r.rel(d7["direct"][-1],direct[-1])
    bchange=r.rel(g2["bulk"],g3["bulk"])
    resid=r.rel(direct[-1],g3["bulk"])
    cres=r.rel(d7["direct"][-1],g2["bulk"])
    qchange=abs(resid-cres)
    wrongres=r.rel(direct[-1],g3["wrong_bulk"])
    collar=r.collar_control_frame(pert,mapper)
    nums=[*d7["direct"],*d8["direct"],g2["bulk"],g3["bulk"],g3["wrong_bulk"],
          dstep,glchange,bchange,resid,cres,qchange,wrongres,collar]
    valid=bool(
        d7["signature_valid"] and d8["signature_valid"] and g2["signature_valid"] and g3["signature_valid"] and
        max(d7["max_inverse_residual"],d8["max_inverse_residual"],g2["max_inverse_residual"],g3["max_inverse_residual"])<=3e-11 and
        collar<=1e-13 and np.isfinite(nums).all()
    )
    passed=bool(valid and abs(direct[-1])>=1e-10 and dstep<=5e-4 and glchange<=5e-4 and
                bchange<=2e-3 and resid<=3e-3 and qchange<=3e-3 and wrongres>resid)
    return {
        "direct_GL7":d7,"direct_GL8":d8,"GJ2":g2,"GJ3":g3,
        "direct_final_step_change":dstep,"direct_GL7_to_GL8_relative_change":glchange,
        "weighted_bulk_GJ2_to_GJ3_relative_change":bchange,"identity_relative_residual":resid,
        "coarse_identity_relative_residual":cres,"coarse_to_fine_identity_residual_change_abs":qchange,
        "wrong_sign_relative_residual":wrongres,"collar_residual":collar,
        "control_valid":valid,"generic_pass":passed,
    }


def reduce_a(index,parts):
    need={("base","direct"),("base","weighted")}
    if set(parts)!=need: raise ValueError(f"A{index} part set mismatch {set(parts)}")
    prov=common_provenance(parts)
    metric,pert,mseed,pseed=r.lane_objects("A",index)
    if any(d.get("metric_seed")!=mseed or d.get("perturbation_seed")!=pseed for d in parts.values()): raise ValueError("A seed identity mismatch")
    d=generic_summary(parts[("base","direct")],parts[("base","weighted")],metric,pert)
    d.update({"gate":GATE,"stream":"A","index":index,"metric_seed":mseed,"perturbation_seed":pseed,"provenance":prov})
    d["lane_pass"]=bool(d["control_valid"] and d["generic_pass"])
    d["iter053u_execution_lock"]="DURABLE_TWO_PASS_AUTHORIZATION_REQUIRED"
    return d


def reduce_b(index,parts):
    need={("base","direct"),("base","weighted")}
    if set(parts)!=need: raise ValueError(f"B{index} part set mismatch {set(parts)}")
    prov=common_provenance(parts)
    metric,pert,mseed,pseed=r.lane_objects("B",index)
    if any(d.get("metric_seed")!=mseed or d.get("perturbation_seed")!=pseed for d in parts.values()): raise ValueError("B seed identity mismatch")
    dp=parts[("base","direct")]; wp=parts[("base","weighted")]
    d7=dp["GL7"]; d8=dp["GL8"]; g2=wp["GJ2"]; g3=wp["GJ3"]
    collar=r.collar_control_frame(pert)
    direct=float(d8["direct"][-1]); bulk=float(g3["bulk"])
    nums=[*d7["direct"],*d8["direct"],g2["bulk"],g3["bulk"],g3["sample_max_H_norm"],
          g3["sample_max_P_norm"],g3["sample_max_abs_W3"],collar]
    valid=bool(d7["signature_valid"] and d8["signature_valid"] and g2["signature_valid"] and g3["signature_valid"] and
               max(d7["max_inverse_residual"],d8["max_inverse_residual"],g2["max_inverse_residual"],g3["max_inverse_residual"])<=3e-11 and
               collar<=1e-13 and np.isfinite(nums).all())
    passed=bool(valid and abs(direct)<=5e-8 and abs(bulk)<=5e-8 and g3["sample_max_abs_W3"]<=2e-10 and
                g3["sample_max_P_norm"]<=3e-9 and g3["sample_max_H_norm"]<=3e-7)
    return {
        "gate":GATE,"stream":"B","index":index,"metric_seed":mseed,"perturbation_seed":pseed,
        "direct_GL7":d7,"direct_GL8":d8,"GJ2":g2,"GJ3":g3,"collar_residual":collar,
        "control_valid":valid,"lane_pass":passed,"iter053u_execution_lock":"DURABLE_TWO_PASS_AUTHORIZATION_REQUIRED",
        "provenance":prov,
    }


def reduce_c(index,parts):
    need={("base","direct"),("base","weighted"),("transformed","direct"),("transformed","weighted")}
    if set(parts)!=need: raise ValueError(f"C{index} part set mismatch {set(parts)}")
    prov=common_provenance(parts)
    metric,pert,mseed,pseed=r.lane_objects("C",index)
    if any(d.get("metric_seed")!=mseed or d.get("perturbation_seed")!=pseed for d in parts.values()): raise ValueError("C seed identity mismatch")
    L=it.shear(index); Linv=np.linalg.inv(L); mt=c.TransformMetric(metric,L); pt=it.TransformPerturbation(pert,L)
    base=generic_summary(parts[("base","direct")],parts[("base","weighted")],metric,pert)
    transformed=generic_summary(parts[("transformed","direct")],parts[("transformed","weighted")],mt,pt,lambda x:Linv@x)
    transformed["weighted_source_path"]="CORRECTED_SOURCE_FAITHFUL_SINGLE_WEIGHT"

    vals=[]
    for x in (np.zeros(r.N),np.array([0.08,-0.06,0.05,-0.04])):
        y=Linv@x
        g=metric.jets(x)[0]; gt=mt.jets(y)[0]
        h=pert.jets(x)[0]; ht=pt.jets(y)[0]
        vals.extend([float(np.max(np.abs(gt-L.T@g@L))),float(np.max(np.abs(ht-L.T@h@L)))])
    tres=max(vals); detres=abs(float(np.linalg.det(L))-1.0)
    source_control=parts[("transformed","weighted")].get("transformed_source_object_control") or {}
    dcov=r.rel(base["direct_GL8"]["direct"][-1],transformed["direct_GL8"]["direct"][-1])
    bcov=r.rel(base["GJ3"]["bulk"],transformed["GJ3"]["bulk"])
    valid=bool(base["control_valid"] and transformed["control_valid"] and detres<=2e-12 and tres<=3e-11 and source_control.get("control_pass") is True)
    passed=bool(valid and base["generic_pass"] and transformed["generic_pass"] and dcov<=2e-3 and bcov<=2e-3)
    return {
        "gate":GATE,"stream":"C","index":index,"metric_seed":mseed,"perturbation_seed":pseed,
        "det_L":float(np.linalg.det(L)),"transform_algebra_residual":tres,
        "transformed_source_object_control":source_control,"base":base,"transformed":transformed,
        "direct_covariance_relative_residual":dcov,"bulk_covariance_relative_residual":bcov,
        "control_valid":valid,"lane_pass":passed,
        "scientific_change_scope":"ONLY_TRANSFORMED_WEIGHTED_POLYNOMIAL_SOURCE_EXTRACTION",
        "iter053u_execution_lock":"DURABLE_TWO_PASS_AUTHORIZATION_REQUIRED","provenance":prov,
    }


def reduce_lane(stream,index,root):
    parts=load_parts(root,stream,index)
    if stream=="A": return reduce_a(index,parts)
    if stream=="B": return reduce_b(index,parts)
    return reduce_c(index,parts)


def write(o,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(o,sort_keys=True))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["part","reduce"],required=True)
    ap.add_argument("--kind",choices=["direct","weighted"])
    ap.add_argument("--stream",choices=["A","B","C"],required=True)
    ap.add_argument("--index",type=int,required=True)
    ap.add_argument("--side",choices=["base","transformed"])
    ap.add_argument("--input-dir")
    ap.add_argument("--state",default="../recovery/state.json")
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    prov=authorize(a.state)
    lim={"A":4,"B":2,"C":2}[a.stream]
    if not 0<=a.index<lim: raise SystemExit("index out of range")
    if a.mode=="part":
        if a.kind is None or a.side is None: raise SystemExit("part requires --kind and --side")
        if a.stream!="C" and a.side!="base": raise SystemExit("A/B have base side only")
        o=direct_part(a.stream,a.index,a.side,prov) if a.kind=="direct" else weighted_part(a.stream,a.index,a.side,prov)
    else:
        if not a.input_dir: raise SystemExit("reduce requires --input-dir")
        o=reduce_lane(a.stream,a.index,a.input_dir)
    write(o,a.out)
    if a.mode=="reduce" and not o.get("control_valid",False): raise SystemExit(3)
    if a.mode=="reduce" and not o.get("lane_pass",False): raise SystemExit(2)

if __name__=="__main__": main()
