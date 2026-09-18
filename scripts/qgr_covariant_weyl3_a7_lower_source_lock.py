#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

FORBIDDEN_TOLERANCE=("abs(diff)","isclose(","math.isclose","numpy.isclose","np.isclose")

def sha(x): return hashlib.sha256(x.encode()).hexdigest()
def run(*args): return subprocess.check_output(args,text=True).strip()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
 b=json.loads(Path(a.binding).read_text())
 controls={}
 controls["prereg_ancestor"]=subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0
 controls["decomposition_binding_ancestor"]=subprocess.run(["git","merge-base","--is-ancestor",b["decomposition_binding_commit"],"HEAD"]).returncode==0
 controls["a7_terminal_ancestor"]=subprocess.run(["git","merge-base","--is-ancestor",b["a7_terminal_commit"],"HEAD"]).returncode==0
 blob_checks={}
 for name,spec in b["frozen_files"].items():
  actual=run("git","rev-parse",f"HEAD:{spec['path']}")
  blob_checks[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
 controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blob_checks.values())
 r=Path(b["frozen_files"]["researcher"]["path"]).read_text()
 c=Path(b["frozen_files"]["critic"]["path"]).read_text()
 t=Path(b["frozen_files"]["terminal"]["path"]).read_text()
 controls["researcher_import_boundary"]="qgr_covariant_weyl3_researcher" in r and "qgr_covariant_weyl3_critic" not in r
 controls["critic_import_boundary"]="qgr_covariant_weyl3_critic" in c and "qgr_covariant_weyl3_researcher" not in c
 controls["terminal_no_science_imports"]="qgr_covariant_weyl3_researcher" not in t and "qgr_covariant_weyl3_critic" not in t
 controls["no_tolerance_classifier_patterns"]=not any(x in (r+c+t) for x in FORBIDDEN_TOLERANCE)
 controls["exact_fraction_present"]="Fraction" in r and "Fraction" in c and "Fraction" in t
 controls["same_frozen_counterexample"]='"OFFSHELL_A"' in r and '"OFFSHELL_A"' in c and '"direction":7' in r and '"direction":7' in c
 controls["c6_lock_present"]="SYMBOLIC_UNFIXED" in r and "SYMBOLIC_UNFIXED" in c and "SYMBOLIC_UNFIXED" in t
 controls["q10_lock_present"]="corrected_q10_locked" in r and "corrected_q10_locked" in c and "corrected_q10_locked" in t
 payload={"gate":b["gate"],"binding_commit":b["binding_commit"],"controls":controls,"blob_checks":blob_checks,"classification":"PASS_LOWER_ORDER_SOURCE_PROVENANCE_LOCK" if all(controls.values()) else "BLOCKED_LOWER_ORDER_SOURCE_PROVENANCE_LOCK"}
 payload["payload_sha256"]=sha(json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=True))
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
 print(json.dumps(payload,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
