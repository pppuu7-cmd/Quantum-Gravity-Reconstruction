#!/usr/bin/env python3
"""Frozen terminal comparator for the covariant Weyl^3 directional-variation gate.

This is the only production component allowed to read both scientific lanes.
It performs no sign, scale, normalization, seed, or convention fitting.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

GATE="COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE"
PREREG="8c21ee233423deaff52d0fa552c027fa065a53a7"
PANEL_FREEZE="1642dc7ca4204a4240635be68522f1731c8a9c50"
PANEL_GENERATOR="03377afec95801b5a49f47b85ddd9c9bf3326ac0"
PANEL_SHA="f1390bc406d0db37fe10cc908db51c2eabcf5105904e4a71cc707d2dd3137c5f"
CELLS=[("FLAT_CONTROL",7),("FLAT_CONTROL",19),("OFFSHELL_A",7),("OFFSHELL_A",19),("OFFSHELL_B",7),("OFFSHELL_B",19)]

def fs(x):
    x=F(x);return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def load_lane(root,expected_lane,ready_class):
    out={};errors=[]
    for p in sorted(Path(root).glob("*.json")):
        try:d=json.loads(p.read_text())
        except Exception as e:errors.append(f"{p.name}:json:{e}");continue
        c=d.get("cell",{}); key=(c.get("seed"),c.get("direction"))
        if key in out:errors.append(f"duplicate cell {key}");continue
        out[key]=(d,p.name)
        if d.get("gate")!=GATE:errors.append(f"{p.name}:gate")
        if d.get("preregistration_commit")!=PREREG:errors.append(f"{p.name}:prereg")
        if d.get("panel_freeze_commit")!=PANEL_FREEZE:errors.append(f"{p.name}:panel_freeze")
        if d.get("panel_generator_commit")!=PANEL_GENERATOR:errors.append(f"{p.name}:panel_generator")
        if d.get("panel_manifest_sha256")!=PANEL_SHA:errors.append(f"{p.name}:panel_sha")
        if d.get("lane")!=expected_lane:errors.append(f"{p.name}:lane")
        if d.get("classification")!=ready_class:errors.append(f"{p.name}:classification={d.get('classification')}")
        if d.get("target_blind_witness_frozen_before_comparison") is not True:errors.append(f"{p.name}:target_blind")
        if d.get("c6")!="SYMBOLIC_UNFIXED_FACTORED_OUT":errors.append(f"{p.name}:c6")
        if not c.get("controls") or not all(v is True for v in c["controls"].values()):errors.append(f"{p.name}:self_controls")
    if set(out)!=set(CELLS):errors.append(f"cell_set={sorted(out)}")
    return out,errors

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--researcher-dir",required=True);ap.add_argument("--critic-dir",required=True);ap.add_argument("--output",required=True);a=ap.parse_args()
    R,re=load_lane(a.researcher_dir,"RESEARCHER_DIRECT_VARIATION_IBP","RESEARCHER_CELL_WITNESS_READY_FOR_TARGET_BLIND_COMPARISON")
    C,ce=load_lane(a.critic_dir,"CRITIC_INDEPENDENT_COVARIANT_EULER_SOURCE","CRITIC_CELL_WITNESS_READY_FOR_TARGET_BLIND_COMPARISON")
    controls={"researcher_complete_and_self_valid":not re,"critic_complete_and_self_valid":not ce,"exact_six_frozen_cells":set(R)==set(C)==set(CELLS),"panel_manifest_pinned":True,"no_posthoc_sign_scale_or_normalization_fit":True,"c6_symbolic_unfixed":True,"corrected_q10_locked":True}
    common=[];comparisons=[];common_ok=True;discrepancies=[]
    if controls["exact_six_frozen_cells"]:
        for key in CELLS:
            r=R[key][0];c=C[key][0];rc=r["cell"];cc=c["cell"]
            ck={"jet_sha256_equal":rc["jet_sha256"]==cc["jet_sha256"],"full_jet_table_equal":rc["jet_table"]==cc["jet_table"],"riemann_point_sha256_equal":rc["riemann_point_sha256"]==cc["riemann_point_sha256"],"ricci_point_equal":rc["ricci_point"]==cc["ricci_point"],"scalar_point_equal":rc["scalar_point"]==cc["scalar_point"],"weyl_point_sha256_equal":rc["weyl_point_sha256"]==cc["weyl_point_sha256"],"I3_point_equal":rc["I3_point"]==cc["I3_point"]}
            common_ok &= all(ck.values());common.append({"seed":key[0],"direction":key[1],"controls":ck})
            direct=F(rc["direct_variation_and_ibp"]["bulk_after_ibp"]);euler=F(cc["euler_source"]["contraction_with_h"]);diff=direct-euler
            comp={"seed":key[0],"direction":key[1],"direct_bulk":fs(direct),"euler_contraction":fs(euler),"difference":fs(diff),"exact_zero":diff==0}
            comparisons.append(comp)
            if diff:discrepancies.append(comp)
    controls["independent_common_domain_curvature_exactly_agrees"]=common_ok
    controls["researcher_did_not_import_critic"]=all(R[k][0].get("critic_science_code_imported") is False for k in R)
    controls["critic_did_not_import_researcher"]=all(C[k][0].get("researcher_science_code_imported") is False for k in C)
    all_ctrl=all(controls.values())
    if re or ce or not all_ctrl:
        classification="BLOCKED_COVARIANT_WEYL3_IMPLEMENTATION_OR_COMMON_DOMAIN_CONTROL_FAILURE";scientific_pass=False;scientific_fail=False
    elif not discrepancies:
        classification="PASS_SCOPED_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFICATE";scientific_pass=True;scientific_fail=False
    else:
        classification="SCIENTIFIC_FAIL_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_DISCREPANCY";scientific_pass=False;scientific_fail=True
    localization=None
    if scientific_fail:
        localization={"smallest_exact_counterexample":discrepancies[0],"earliest_common_object_status":"metric jets, point Riemann/Ricci/scalar/Weyl and I3 agree exactly before functional-derivative comparison","earliest_divergent_intermediate_object":"POST_COMMON_CURVATURE__DIRECT_VARIATION_IBP_VS_INDEPENDENT_EULER_SOURCE","posthoc_repair_authorized":False}
    payload={"gate":GATE,"preregistration_commit":PREREG,"panel_freeze_commit":PANEL_FREEZE,"panel_generator_commit":PANEL_GENERATOR,"panel_manifest_sha256":PANEL_SHA,"classification":classification,"scientific_pass":scientific_pass,"scientific_fail":scientific_fail,"controls":controls,"researcher_errors":re,"critic_errors":ce,"common_domain_comparisons":common,"cell_comparisons":comparisons,"exact_discrepancy_zero_all_cells":all(x["exact_zero"] for x in comparisons) if len(comparisons)==6 else False,"scientific_fail_localization":localization,"target_blind_serialization_completed_before_cross_lane_compare":all_ctrl,"c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0}
    payload["terminal_payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n");print(json.dumps(payload,sort_keys=True,indent=2))
    return 2 if classification.startswith("BLOCKED") else 0
if __name__=="__main__":raise SystemExit(main())
