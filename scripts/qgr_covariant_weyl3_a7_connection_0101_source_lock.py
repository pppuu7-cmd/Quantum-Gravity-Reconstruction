#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path
FORBIDDEN=("isclose(","math.isclose","numpy.isclose","np.isclose","abs(diff)")
TARGETS=("6dce9ed04c9199cf36eb2a723095f7eeba3f002844c3cd9df7da33704cbdf673","702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4","e3797c7dade7f4de601ba047be48b0ed73278333e01719e3b0d97588e783deb8")
def run(*a): return subprocess.check_output(a,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); q=ap.parse_args(); b=json.loads(Path(q.binding).read_text())
 controls={"prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,"parent_terminal_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_terminal_commit"],"HEAD"]).returncode==0}
 blobs={}; texts={}
 for name,spec in b["frozen_files"].items():
  actual=run("git","rev-parse",f"HEAD:{spec['path']}"); blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}; texts[name]=Path(spec["path"]).read_text()
 controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
 for lane in ("lane_a","lane_b","lane_c"):
  t=texts[lane]; controls[lane+"_exact_fraction"]="Fraction" in t; controls[lane+"_no_tolerance"]=not any(x in t for x in FORBIDDEN); controls[lane+"_target_blind"]=not any(x in t for x in TARGETS)
 controls["lane_independence"]=all(other not in texts[lane] for lane,others in {"lane_a":["connection_0101_lane_b","connection_0101_lane_c"],"lane_b":["connection_0101_lane_a","connection_0101_lane_c"],"lane_c":["connection_0101_lane_a","connection_0101_lane_b"]}.items() for other in others)
 controls["terminal_contains_parent_controls"]=all(x in texts["terminal"] for x in TARGETS)
 controls["no_tolerance_classifier"]=not any(x in texts["terminal"] for x in FORBIDDEN)
 out={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_COMPONENT_0101_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_COMPONENT_0101_SOURCE_LOCK"}
 out["payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
