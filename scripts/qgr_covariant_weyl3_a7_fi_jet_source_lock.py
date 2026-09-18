#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

FORBIDDEN=("abs(diff)","isclose(","math.isclose","numpy.isclose","np.isclose")

def run(*args): return subprocess.check_output(args,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    b=json.loads(Path(a.binding).read_text())
    controls={
      "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
      "implementation_binding_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["implementation_binding_commit"],"HEAD"]).returncode==0,
      "parent_terminal_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_terminal_commit"],"HEAD"]).returncode==0,
    }
    blobs={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
    rt=Path(b["frozen_files"]["researcher"]["path"]).read_text()
    ct=Path(b["frozen_files"]["critic"]["path"]).read_text()
    tt=Path(b["frozen_files"]["terminal"]["path"]).read_text()
    controls["researcher_import_boundary"]="qgr_covariant_weyl3_researcher" in rt and "qgr_covariant_weyl3_critic" not in rt
    controls["critic_import_boundary"]="qgr_covariant_weyl3_critic" in ct and "qgr_covariant_weyl3_researcher" not in ct
    controls["terminal_no_science_imports"]="qgr_covariant_weyl3_researcher" not in tt and "qgr_covariant_weyl3_critic" not in tt
    controls["no_tolerance_classifier_patterns"]=not any(x in (rt+ct+tt) for x in FORBIDDEN)
    controls["exact_fraction_present"]="Fraction" in rt and "Fraction" in ct and "Fraction" in tt
    controls["frozen_witness_exact"]='"OFFSHELL_A"' in rt and '"OFFSHELL_A"' in ct and '"direction":7' in rt and '"direction":7' in ct
    controls["c6_lock_present"]="SYMBOLIC_UNFIXED" in rt and "SYMBOLIC_UNFIXED" in ct and "SYMBOLIC_UNFIXED" in tt
    controls["q10_lock_present"]="corrected_q10_locked" in rt and "corrected_q10_locked" in ct and "corrected_q10_locked" in tt
    payload={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_FI_JET_SOURCE_PROVENANCE_LOCK" if all(controls.values()) else "BLOCKED_FI_JET_SOURCE_PROVENANCE_LOCK"}
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
