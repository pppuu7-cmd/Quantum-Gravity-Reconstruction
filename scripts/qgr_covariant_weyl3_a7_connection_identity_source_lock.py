#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

TARGET_NUMERATOR="433508011369185071313333891829231313950116629"
FORBIDDEN_TOL=("abs(diff)","isclose(","math.isclose","numpy.isclose","np.isclose")

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
    at=Path(b["frozen_files"]["lane_a"]["path"]).read_text()
    bt=Path(b["frozen_files"]["lane_b"]["path"]).read_text()
    tt=Path(b["frozen_files"]["terminal"]["path"]).read_text()
    controls["lane_a_no_lane_b_import"]="qgr_covariant_weyl3_a7_connection_gammagamma_identity" not in at
    controls["lane_b_no_lane_a_import"]="qgr_covariant_weyl3_a7_connection_hessian_identity" not in bt
    controls["target_fraction_absent_from_identity_lanes"]=TARGET_NUMERATOR not in at and TARGET_NUMERATOR not in bt
    controls["target_fraction_present_only_terminal"]=TARGET_NUMERATOR in tt
    controls["shared_P_common_input_declared"]="qgr_covariant_weyl3_critic" in at and "qgr_covariant_weyl3_critic" in bt
    controls["neutral_panel_used"]="qgr_covariant_weyl3_panel" in at and "qgr_covariant_weyl3_panel" in bt
    controls["no_tolerance_classifier_patterns"]=not any(x in (at+bt+tt) for x in FORBIDDEN_TOL)
    controls["exact_fraction_present"]="Fraction" in at and "Fraction" in bt and "Fraction" in tt
    controls["frozen_slot_exact"]='"direction":7' in at and '"direction":7' in bt and '"i":0' in at and '"i":0' in bt and '"j":0' in at and '"j":0' in bt
    controls["c6_q10_locks"]="SYMBOLIC_UNFIXED" in at and "SYMBOLIC_UNFIXED" in bt and "corrected_q10_locked" in at and "corrected_q10_locked" in bt
    payload={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_CONNECTION_IDENTITY_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_CONNECTION_IDENTITY_SOURCE_LOCK"}
    payload["payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2

if __name__=="__main__": raise SystemExit(main())
