#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path

TARGETS=("ba7ed7b7eb2b8fa66dbc07ffd6b6a66f7f2896f242257c6830e77cb56b6f2c32","09ee351958f9f066a84b581194275fffc73c123744f24c6b8cdff26ce4693034")
FORBIDDEN=("qgr_covariant_weyl3_panel","OFFSHELL_A","isclose(","numpy","sympy","connection_formal_lane_a","connection_formal_lane_b")

def run(*a): return subprocess.check_output(a,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); q=ap.parse_args()
    b=json.loads(Path(q.binding).read_text())
    controls={
      "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
      "parent_formal_result_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_formal_result_commit"],"HEAD"]).returncode==0,
      "parent_neutral_result_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_neutral_result_commit"],"HEAD"]).returncode==0
    }
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
    ext=texts["conversion"]; term=texts["terminal"]
    controls["target_hashes_absent_conversion"]=not any(t in ext for t in TARGETS)
    controls["target_hashes_present_terminal"]=all(t in term for t in TARGETS)
    controls["no_panel_numeric_or_parent_helper"]=not any(x in ext for x in FORBIDDEN)
    controls["exact_fraction_present"]="Fraction" in ext
    controls["tensor_definition_terms_present"]="connection_action_on_derivative_index_included" in ext and "partial_partial = covariant_hessian - C_nabla" in ext
    out={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_PARTIAL_COVARIANT_CONVERSION_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_PARTIAL_COVARIANT_CONVERSION_SOURCE_LOCK"}
    out["payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
