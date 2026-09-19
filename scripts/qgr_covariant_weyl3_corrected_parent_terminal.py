#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

PREREG="1640b2fb84980c68fa1e14d146b8403b43d3fd5a"
OLD_PREREG="8c21ee233423deaff52d0fa552c027fa065a53a7"
CELLS=(("FLAT_CONTROL",7),("FLAT_CONTROL",19),("OFFSHELL_A",7),("OFFSHELL_A",19),("OFFSHELL_B",7),("OFFSHELL_B",19))

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def load_corrected(root):
    out={}; errors=[]
    for p in Path(root).glob("*.json"):
        d=json.loads(p.read_text()); key=(d.get("seed"),d.get("direction"))
        if key in out: errors.append(f"duplicate corrected {key}")
        out[key]=d
        if d.get("gate")!="COVARIANT_WEYL3_CORRECTED_PARENT_CONNECTION_GAP_SIGN_REPLAY": errors.append(f"{p.name}:gate")
        if d.get("preregistration_commit")!=PREREG: errors.append(f"{p.name}:prereg")
        if d.get("lane")!="CORRECTED_CRITIC_CONNECTION_GAP_SIGN": errors.append(f"{p.name}:lane")
        if d.get("classification")!="CORRECTED_CRITIC_PARENT_CELL_READY": errors.append(f"{p.name}:classification")
        if not d.get("controls") or not all(v is True for v in d["controls"].values()): errors.append(f"{p.name}:controls")
        if d.get("corrected_rule")!="partial_IBP - covariantization_gap": errors.append(f"{p.name}:rule")
    if set(out)!=set(CELLS): errors.append(f"corrected_cell_set={sorted(out)}")
    return out,errors

def load_researcher(root):
    out={}; errors=[]
    for p in Path(root).glob("*.json"):
        d=json.loads(p.read_text()); c=d.get("cell",{}); key=(c.get("seed"),c.get("direction"))
        if key in out: errors.append(f"duplicate researcher {key}")
        out[key]=d
        if d.get("gate")!="COVARIANT_WEYL3_DIRECTIONAL_VARIATION_FUNCTIONAL_DERIVATIVE_CERTIFICATE": errors.append(f"{p.name}:gate")
        if d.get("preregistration_commit")!=OLD_PREREG: errors.append(f"{p.name}:old_prereg")
        if d.get("lane")!="RESEARCHER_DIRECT_VARIATION_IBP": errors.append(f"{p.name}:lane")
        if d.get("classification")!="RESEARCHER_CELL_WITNESS_READY_FOR_TARGET_BLIND_COMPARISON": errors.append(f"{p.name}:classification")
        if not c.get("controls") or not all(v is True for v in c["controls"].values()): errors.append(f"{p.name}:controls")
        if d.get("critic_science_code_imported") is not False: errors.append(f"{p.name}:independence")
    if set(out)!=set(CELLS): errors.append(f"researcher_cell_set={sorted(out)}")
    return out,errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--corrected-dir",required=True); ap.add_argument("--researcher-dir",required=True); ap.add_argument("--output",required=True)
    a=ap.parse_args()
    C,ce=load_corrected(a.corrected_dir); R,re=load_researcher(a.researcher_dir)
    controls={
      "corrected_complete_and_self_valid":not ce,
      "researcher_complete_and_self_valid":not re,
      "exact_six_frozen_cells":set(C)==set(R)==set(CELLS),
      "terminal_only_cross_lane_comparison":True,
      "no_posthoc_scale_additive_or_sign_fit":True,
      "c6_symbolic_unfixed":True,
      "corrected_q10_locked":True
    }
    comps=[]; first=None
    if controls["exact_six_frozen_cells"]:
        for key in CELLS:
            c=C[key]; r=R[key]; rc=r["cell"]
            cv=F(c["corrected_euler"]); rv=F(rc["direct_variation_and_ibp"]["bulk_after_ibp"]); diff=cv-rv
            common=(c["jet_sha256"]==rc["jet_sha256"])
            row={
              "seed":key[0],"direction":key[1],
              "corrected_critic":fs(cv),
              "historical_researcher_direct_bulk":fs(rv),
              "difference":fs(diff),
              "exact_zero":diff==0,
              "jet_sha256_equal":common,
              "historical_critic_euler":c["historical_euler"],
              "partial_ibp":c["partial_ibp"],
              "covariantization_gap":c["covariantization_gap"],
              "correction_from_historical":c["correction_from_historical"]
            }
            comps.append(row)
            if first is None and (diff!=0 or not common): first=row
    all_zero=len(comps)==6 and all(x["exact_zero"] and x["jet_sha256_equal"] for x in comps)
    if not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif all_zero:
        cls="CORRECTED_PARENT_SIX_CELL_EXACT_MATCH"
    else:
        cls="CORRECTED_PARENT_RESIDUAL_DISCREPANCY"
    out={
      "gate":"COVARIANT_WEYL3_CORRECTED_PARENT_CONNECTION_GAP_SIGN_REPLAY",
      "preregistration_commit":PREREG,
      "historical_parent_preregistration_commit":OLD_PREREG,
      "classification":cls,
      "controls":controls,
      "corrected_errors":ce,
      "researcher_errors":re,
      "cell_comparisons":comps,
      "exact_zero_all_six_cells":all_zero,
      "first_residual_cell":first,
      "historical_parent_reclassification_authorized":False,
      "claim_scope":"prospectively corrected six-cell certificate only",
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "theory_established_pct":0
    }
    out["terminal_payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0

if __name__=="__main__": raise SystemExit(main())
