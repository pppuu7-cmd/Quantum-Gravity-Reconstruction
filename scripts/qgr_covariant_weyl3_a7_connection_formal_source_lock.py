#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
FORBIDDEN=("qgr_covariant_weyl3_panel","OFFSHELL_A","isclose(","numpy","sympy")
def run(*a): return subprocess.check_output(a,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); q=ap.parse_args(); b=json.loads(Path(q.binding).read_text())
    controls={"prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0}
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
    for lane in ("lane_a","lane_b"):
        controls[lane+"_no_panel_or_numeric_witness"]=not any(x in texts[lane] for x in FORBIDDEN)
        controls[lane+"_exact_fraction"]="Fraction" in texts[lane]
    controls["lane_independence"]="formal_lane_b" not in texts["lane_a"] and "formal_lane_a" not in texts["lane_b"]
    controls["malformed_control_present"]="malformed=True" in texts["lane_a"] and "malformed_control" in texts["terminal"]
    out={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_FORMAL_MONOMIAL_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_FORMAL_MONOMIAL_SOURCE_LOCK"}
    out["payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
