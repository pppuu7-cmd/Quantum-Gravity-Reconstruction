#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

TARGET_NUMERATOR="433508011369185071313333891829231313950116629"
FORBIDDEN=("abs(diff)","isclose(","math.isclose","numpy.isclose","np.isclose")

def run(*args): return subprocess.check_output(args,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    b=json.loads(Path(a.binding).read_text())
    controls={
      "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
      "parent_terminal_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_terminal_commit"],"HEAD"]).returncode==0,
    }
    blobs={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
    et=Path(b["frozen_files"]["extraction"]["path"]).read_text()
    tt=Path(b["frozen_files"]["terminal"]["path"]).read_text()
    controls["target_absent_extraction"]=TARGET_NUMERATOR not in et
    controls["target_present_terminal_only"]=TARGET_NUMERATOR in tt
    controls["no_parent_identity_helpers"]="connection_hessian_identity" not in et and "connection_gammagamma_identity" not in et
    controls["neutral_panel_and_frozen_P_only"]="qgr_covariant_weyl3_panel" in et and "qgr_covariant_weyl3_critic" in et
    controls["exact_fraction_present"]="Fraction" in et and "Fraction" in tt
    controls["no_tolerance_classifier_patterns"]=not any(x in (et+tt) for x in FORBIDDEN)
    controls["polynomial_phi_x0_frozen"]='phi":"x0"' in et or '"phi":"x0"' in et
    controls["c6_q10_locks"]="SYMBOLIC_UNFIXED" in et and "corrected_q10_locked" in et and "corrected_q10_locked" in tt
    payload={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_DUAL_POLYNOMIAL_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_DUAL_POLYNOMIAL_SOURCE_LOCK"}
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
