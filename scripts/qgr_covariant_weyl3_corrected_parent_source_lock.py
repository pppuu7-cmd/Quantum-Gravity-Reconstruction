#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path

FORBIDDEN_TARGET_PATTERNS=("86355995554365317186893343264769708206041673","141609523517262295106976925021598088976553029","36188861490208135407463132950092941670313420227")
FORBIDDEN_CORRECTED_IMPORTS=("qgr_covariant_weyl3_researcher","results/","terminal_compare")

def run(*a): return subprocess.check_output(a,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    b=json.loads(Path(a.binding).read_text())
    controls={
      "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
      "historical_parent_result_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["historical_parent_result_commit"],"HEAD"]).returncode==0,
      "full_first_jet_closure_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["full_first_jet_closure_commit"],"HEAD"]).returncode==0,
      "conversion_sign_authority_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["conversion_sign_authority_commit"],"HEAD"]).returncode==0
    }
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
    corrected=texts["corrected_critic"]; terminal=texts["terminal"]
    controls["corrected_no_researcher_import"]=not any(x in corrected for x in FORBIDDEN_CORRECTED_IMPORTS)
    controls["parent_targets_absent_corrected"]=not any(x in corrected for x in FORBIDDEN_TARGET_PATTERNS)
    controls["corrected_rule_literal_present"]='partial_IBP - covariantization_gap' in corrected
    controls["historical_researcher_blob_exact"]=blobs["historical_researcher"]["exact"]
    controls["historical_critic_blob_exact"]=blobs["historical_critic"]["exact"]
    controls["neutral_panel_blob_exact"]=blobs["panel"]["exact"]
    controls["terminal_imports_no_science_lane"]="qgr_covariant_weyl3_researcher" not in terminal and "qgr_covariant_weyl3_critic" not in terminal
    controls["exact_fraction_present"]="Fraction" in corrected and "Fraction" in terminal
    controls["no_tolerance_patterns"]="isclose(" not in corrected+terminal and "numpy" not in corrected+terminal
    out={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_CORRECTED_PARENT_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_CORRECTED_PARENT_SOURCE_LOCK"}
    out["payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
