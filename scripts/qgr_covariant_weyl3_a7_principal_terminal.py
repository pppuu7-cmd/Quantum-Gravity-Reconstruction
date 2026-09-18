#!/usr/bin/env python3
"""Frozen comparator for A7 principal-symbol causal localization."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG="5c5d6197ff15573f2110729ddd41c4e64c005e7a"
PARENT_DIFF=F("-86355995554365317186893343264769708206041673/10039118967354700841951532316479538176000000")
R_READY="RESEARCHER_A7_PRINCIPAL_WITNESS_READY"
C_READY="CRITIC_A7_PRINCIPAL_WITNESS_READY"

def fs(x):
    x=F(x);return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--researcher",required=True);ap.add_argument("--critic",required=True);ap.add_argument("--output",required=True);a=ap.parse_args()
    r=json.loads(Path(a.researcher).read_text());c=json.loads(Path(a.critic).read_text())
    controls={
      "preregistration_exact":r.get("preregistration_commit")==c.get("preregistration_commit")==PREREG,
      "same_frozen_counterexample":(r.get("seed"),r.get("direction"))==(c.get("seed"),c.get("direction"))==("OFFSHELL_A",7),
      "researcher_ready":r.get("classification")==R_READY and all(v is True for v in r.get("controls",{}).values()),
      "critic_ready":c.get("classification")==C_READY and all(v is True for v in c.get("controls",{}).values()),
      "same_parent_jet":r.get("parent_jet_sha256")==c.get("parent_jet_sha256"),
      "target_blind_lane_serialization":r.get("target_blind_no_critic_values_read") is True and c.get("target_blind_no_researcher_values_read") is True,
      "c6_symbolic_unfixed":r.get("controls",{}).get("c6_symbolic_unfixed") is True and c.get("controls",{}).get("c6_symbolic_unfixed") is True,
      "corrected_q10_locked":r.get("controls",{}).get("corrected_q10_locked") is True and c.get("controls",{}).get("corrected_q10_locked") is True,
      "exact_fraction_no_tolerance":r.get("controls",{}).get("exact_fraction_no_tolerance") is True and c.get("controls",{}).get("exact_fraction_no_tolerance") is True,
    }
    volume_diff=F(r.get("direct_volume_term","0"))-F(c.get("euler_metric_I3_term","0"))
    rv=r.get("Fij_vector",[]);cv=c.get("principal_vector",[])
    principal=[]
    if len(rv)==len(cv)==10:
        for x,y in zip(rv,cv):
            same_key=x.get("ij")==y.get("ij")
            diff=F(x.get("value","0"))-F(y.get("value","0"))
            principal.append({"ij":x.get("ij"),"same_key":same_key,"researcher_Fij":x.get("value"),"critic_P_principal":y.get("value"),"difference":fs(diff),"exact_zero":same_key and diff==0})
    controls["ten_ordered_principal_slots"]=len(principal)==10 and all(x["same_key"] for x in principal)
    direct=F(r.get("direct_bulk_parent","0"));euler=F(c.get("euler_total_parent","0"));parent_diff=direct-euler
    controls["parent_terminal_discrepancy_reproduced_exact"]=parent_diff==PARENT_DIFF
    blocked=not all(controls.values())
    if blocked:
        cls="BLOCKED_COVARIANT_WEYL3_A7_PRINCIPAL_SYMBOL_LOCALIZATION_EXECUTION_OR_PROVENANCE_FAILURE"
    elif volume_diff:
        cls="LOCALIZED_DETERMINANT_OR_METRIC_INDEX_CONVENTION_MISMATCH"
    elif not all(x["exact_zero"] for x in principal):
        cls="LOCALIZED_P_FRECHET_PRINCIPAL_SYMBOL_MISMATCH"
    elif parent_diff:
        cls="PRINCIPAL_SYMBOL_AND_VOLUME_MATCH__LOWER_ORDER_COVARIANTIZATION_OR_IBP_LOCALIZATION_REQUIRED"
    else:
        cls="SCIENTIFIC_FAIL_PARENT_DISCREPANCY_NOT_REPRODUCIBLE_UNDER_FROZEN_COUNTEREXAMPLE"
    payload={
      "gate":"COVARIANT_WEYL3_OFFSHELL_A7_PRINCIPAL_SYMBOL_CAUSAL_LOCALIZATION",
      "preregistration_commit":PREREG,
      "classification":cls,
      "controls":controls,
      "researcher_payload_sha256":r.get("payload_sha256"),
      "critic_payload_sha256":c.get("payload_sha256"),
      "researcher_Fij_sha256":r.get("Fij_vector_sha256"),
      "critic_principal_sha256":c.get("principal_vector_sha256"),
      "volume":{"direct":r.get("direct_volume_term"),"euler_metric_I3":c.get("euler_metric_I3_term"),"difference":fs(volume_diff),"exact_zero":volume_diff==0},
      "principal_slots":principal,
      "principal_exact_zero_all":len(principal)==10 and all(x["exact_zero"] for x in principal),
      "parent":{"direct_bulk":r.get("direct_bulk_parent"),"euler_total":c.get("euler_total_parent"),"difference":fs(parent_diff),"exact_parent_difference":parent_diff==PARENT_DIFF},
      "posthoc_repair_authorized":False,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "theory_established_pct":0,
    }
    payload["terminal_payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n");print(json.dumps(payload,sort_keys=True,indent=2))
    return 2 if cls.startswith("BLOCKED") else 0
if __name__=="__main__":raise SystemExit(main())
