#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

PARENT_D_HASH="138c715fb96eadf5162b4442aaaeed65007f3d40ab2b7f63805fab0074d6e98c"
PARENT_G_HASH="34d9ca91b11fa47b3a7f9b77f4f833788fcdf68d9f1684dd8c375d6e4f5cc8fa"
FORBIDDEN=(
    "qgr_covariant_weyl3_panel",
    "OFFSHELL_A",
    "OFFSHELL_B",
    "FLAT_CONTROL",
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
        "parent_generic_result_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_generic_result_commit"],"HEAD"]).returncode==0
    }
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())

    weighted=texts["weighted_lane"]; terminal=texts["terminal"]
    controls["weighted_no_panel_or_project_science_import"]=not any(x in weighted for x in FORBIDDEN)
    controls["weighted_exact_fraction"]="Fraction" in weighted
    controls["weighted_pair_symmetry_only"]="no first Bianchi" in weighted
    controls["density_weight_formula_present"]="dgamma(c,r,d,r)" in weighted and ",(a,b),-2" in weighted
    controls["weighted_target_blind"]=PARENT_D_HASH not in weighted and PARENT_G_HASH not in weighted
    controls["parent_lane_d_blob_exact"]=blobs["lane_d_reference"]["exact"]
    controls["terminal_contains_parent_hash_controls"]=PARENT_D_HASH in terminal and PARENT_G_HASH in terminal
    controls["terminal_no_science_imports"]="qgr_covariant_weyl3_" not in terminal
    controls["no_tolerance_classifier"]="isclose(" not in terminal

    out={
        "gate":b["gate"],
        "controls":controls,
        "blob_checks":blobs,
        "classification":"PASS_GENERIC_P_TENSOR_DENSITY_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_GENERIC_P_TENSOR_DENSITY_SOURCE_LOCK"
    }
    out["payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__":
    raise SystemExit(main())
