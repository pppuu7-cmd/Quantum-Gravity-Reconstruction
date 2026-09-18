#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG="ae2024bd8179f84c7b9ef3b2412d6cad088f5748"
IMPL_BINDING="2a36bcd4c4529644f4847cd49f46e92ac5f3ac38"
PARENT_RESULT="6ccfededab41dbe01b071916a5aa746491273276"
SOURCE_ORDER=("METRIC_JET","INVERSE_METRIC_JET","CURVATURE_WEYL_JET","CONNECTION_JET","PERTURBATION_JET")

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--researcher",required=True); ap.add_argument("--critic",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    r=json.loads(Path(a.researcher).read_text()); c=json.loads(Path(a.critic).read_text())
    controls={
      "preregistration_exact":r.get("preregistration_commit")==c.get("preregistration_commit")==PREREG,
      "implementation_binding_exact":r.get("implementation_binding_commit")==c.get("implementation_binding_commit")==IMPL_BINDING,
      "parent_terminal_exact":r.get("parent_terminal_commit")==c.get("parent_terminal_commit")==PARENT_RESULT,
      "same_frozen_witness":(r.get("seed"),r.get("direction"))==(c.get("seed"),c.get("direction"))==("OFFSHELL_A",7),
      "researcher_ready":r.get("classification")=="RESEARCHER_FI_JET_WITNESS_READY" and all(v is True for v in r.get("controls",{}).values()),
      "critic_ready":c.get("classification")=="CRITIC_FI_JET_WITNESS_READY" and all(v is True for v in c.get("controls",{}).values()),
      "target_blind_serialization":r.get("target_blind_serialized_before_comparison") is True and c.get("target_blind_serialized_before_comparison") is True,
      "source_order_exact":tuple(r.get("source_order",[]))==tuple(c.get("source_order",[]))==SOURCE_ORDER,
      "c6_symbolic_unfixed":r.get("c6")==c.get("c6")=="SYMBOLIC_UNFIXED",
      "corrected_q10_locked":r.get("corrected_q10_locked") is True and c.get("corrected_q10_locked") is True,
    }
    rp=r.get("pointwise_Fi",[]); cp=c.get("pointwise_Fi",[])
    pointwise=[]
    pointwise_ok=len(rp)==len(cp)==4
    if pointwise_ok:
      for x,y in zip(rp,cp):
        same=x.get("i")==y.get("i"); d=F(x.get("value","0"))-F(y.get("value","0"))
        pointwise.append({"i":x.get("i"),"same_key":same,"researcher":x.get("value"),"critic":y.get("value"),"difference":fs(d),"exact_match":same and d==0})
      pointwise_ok=all(x["exact_match"] for x in pointwise)
    controls["pointwise_Fi_exact"]=pointwise_ok

    rs=r.get("first_jet_slots",[]); cs=c.get("first_jet_slots",[])
    slot_structure=len(rs)==len(cs)==16
    comparisons=[]; first=None
    if slot_structure:
      for x,y in zip(rs,cs):
        same=(x.get("i"),x.get("j"))==(y.get("i"),y.get("j"))
        d=F(x.get("d_j_Fi","0"))-F(y.get("d_j_Fi","0"))
        row={"i":x.get("i"),"j":x.get("j"),"same_key":same,"researcher":x.get("d_j_Fi"),"critic":y.get("d_j_Fi"),"difference":fs(d),"exact_match":same and d==0}
        comparisons.append(row)
        if first is None and (not same or d):
          first=row
    controls["sixteen_ordered_first_jets"]=slot_structure and all((x["i"],x["j"])==(i,j) for x,(i,j) in zip(comparisons,[(i,j) for i in range(4) for j in range(4)]))

    rt=F(r.get("scalar_first_ibp_transfer","0")); ct=F(c.get("scalar_first_ibp_transfer","0")); transfer_diff=rt-ct

    source_comparison=None; first_source=None; source_reconstruction_exact=True
    if first is not None and first.get("same_key"):
      idx=next(k for k,x in enumerate(rs) if x.get("i")==first["i"] and x.get("j")==first["j"])
      xr,xc=rs[idx],cs[idx]
      source_comparison=[]
      dr=F(0); dc=F(0)
      for key in SOURCE_ORDER:
        rv=F(xr.get("sources",{}).get(key,"0")); cv=F(xc.get("sources",{}).get(key,"0")); d=rv-cv
        row={"source_class":key,"researcher":fs(rv),"critic":fs(cv),"difference":fs(d),"exact_match":d==0}
        source_comparison.append(row); dr+=rv; dc+=cv
        if first_source is None and d: first_source=row
      source_reconstruction_exact=(dr==F(xr["d_j_Fi"]) and dc==F(xc["d_j_Fi"]) and dr-dc==F(first["difference"]))
    controls["first_divergence_source_reconstruction_exact"]=source_reconstruction_exact
    controls["source_divergence_present_if_first_jet_diff"]=(first is None or first_source is not None)

    blocked=not all(controls.values())
    if blocked:
      classification="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif first is not None:
      classification="FI_FIRST_JET_DIVERGENCE_LOCALIZED"
    elif transfer_diff:
      classification="BLOCKED_INTERNAL_INCONSISTENCY"
    else:
      classification="FI_JET_AND_TRANSFER_MATCH__PARENT_RECONCILIATION_REQUIRED"

    payload={
      "gate":"COVARIANT_WEYL3_A7_FIRST_IBP_FI_JET_CAUSAL_AUDIT",
      "preregistration_commit":PREREG,
      "implementation_binding_commit":IMPL_BINDING,
      "parent_terminal_commit":PARENT_RESULT,
      "classification":classification,
      "controls":controls,
      "pointwise_Fi_comparison":pointwise,
      "first_jet_comparisons":comparisons,
      "first_jet_divergence":first,
      "first_divergence_source_comparison":source_comparison,
      "first_source_class_divergence":first_source,
      "parent_transfer":{"researcher":fs(rt),"critic":fs(ct),"difference":fs(transfer_diff)},
      "researcher_payload_sha256":r.get("payload_sha256"),
      "critic_payload_sha256":c.get("payload_sha256"),
      "posthoc_repair_authorized":False,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "theory_established_pct":0,
    }
    payload["terminal_payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2))
    return 2 if classification in ("BLOCKED_EXECUTION_OR_PROVENANCE","BLOCKED_INTERNAL_INCONSISTENCY") else 0

if __name__=="__main__": raise SystemExit(main())
