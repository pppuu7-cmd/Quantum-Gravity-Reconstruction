#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
TARGETS=("6dce9ed04c9199cf36eb2a723095f7eeba3f002844c3cd9df7da33704cbdf673","702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4","89350652201/169388331840","-89350652201/169388331840")
FORBIDDEN=("isclose(","math.isclose","numpy.isclose","np.isclose","abs(diff)")
def run(*a): return subprocess.check_output(a,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); q=ap.parse_args()
    b=json.loads(Path(q.binding).read_text())
    controls={
      "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
      "parent_terminal_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_terminal_commit"],"HEAD"]).returncode==0
    }
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
    ext=texts["extraction"]; term=texts["terminal"]
    controls["targets_absent_extraction"]=not any(x in ext for x in TARGETS)
    controls["targets_present_terminal"]=TARGETS[0] in term and TARGETS[1] in term
    controls["no_parent_lane_import"]="connection_0101_lane_a" not in ext and "connection_0101_lane_b" not in ext and "connection_tensor_lane_a" not in ext and "connection_tensor_lane_b" not in ext
    controls["exact_fraction_present"]="Fraction" in ext
    controls["no_tolerance_patterns"]=not any(x in ext+term for x in FORBIDDEN)
    controls["full_coordinate_variables"]=all(x in ext for x in ('"x0"','"x1"','"x2"','"x3"'))
    controls["connection_controls_present"]="all_64_dGamma_exact" in ext and "all_64_deltaGamma_exact" in ext
    out={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_MULTICOORDINATE_NEUTRAL_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_MULTICOORDINATE_NEUTRAL_SOURCE_LOCK"}
    out["payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
