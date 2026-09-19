#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

FORBIDDEN=(
    "qgr_covariant_weyl3_panel",
    "OFFSHELL_A",
    "OFFSHELL_B",
    "FLAT_CONTROL",
    "Weyl3 panel",
    "corrected_parent",
    "qgr_covariant_weyl3_researcher",
    "qgr_covariant_weyl3_critic",
    "numpy",
    "sympy",
    "isclose("
)

def run(*args):
    return subprocess.check_output(args,text=True).strip()

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--binding",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    b=json.loads(Path(a.binding).read_text())

    controls={
        "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
        "corrected_parent_result_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["corrected_parent_result_commit"],"HEAD"]).returncode==0
    }
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())

    for lane in ("lane_d","lane_g"):
        t=texts[lane]
        controls[lane+"_no_panel_or_project_science_import"]=not any(x in t for x in FORBIDDEN)
        controls[lane+"_exact_fraction"]="Fraction" in t
        controls[lane+"_pair_symmetry_only"]="no first Bianchi" in t
        controls[lane+"_target_blind"]="eb05fa6eb0cb3a3b642f302b87c1ebf280e110c3" not in t
    controls["lane_independence"]="generic_p_lane_g" not in texts["lane_d"] and "generic_p_lane_d" not in texts["lane_g"]
    controls["malformed_control_present"]="malformed_derivative_index_term_removed_only" in texts["lane_g"]
    controls["terminal_no_science_imports"]="qgr_covariant_weyl3_" not in texts["terminal"]
    controls["terminal_exact_fraction"]="Fraction" in texts["terminal"]
    controls["no_tolerance_classifier"]="isclose(" not in texts["terminal"]

    out={
        "gate":b["gate"],
        "controls":controls,
        "blob_checks":blobs,
        "classification":"PASS_GENERIC_P_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_GENERIC_P_SOURCE_LOCK"
    }
    out["payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__":
    raise SystemExit(main())
