#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess
from pathlib import Path

TARGETS=(
"43977684225232401744358310400305192156031283",
"433508011369185071313333891829231313950116629",
"702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4"
)
FORBIDDEN=("qgr_covariant_weyl3_a7_fi_jet_researcher","connection_formal_lane_b","connection_multicoordinate","isclose(","numpy.isclose","np.isclose")

def run(*a): return subprocess.check_output(a,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); q=ap.parse_args()
    b=json.loads(Path(q.binding).read_text())
    controls={
      "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
      "parent_fi_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_fi_result_commit"],"HEAD"]).returncode==0,
      "conversion_authority_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["conversion_authority_commit"],"HEAD"]).returncode==0
    }
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())
    src=texts["replay"]; term=texts["terminal"]
    controls["targets_absent_replay"]=not any(t in src for t in TARGETS)
    controls["targets_terminal_only"]=all(t in term for t in TARGETS)
    controls["no_researcher_or_parent_correction_helper"]=not any(x in src for x in FORBIDDEN)
    controls["base_critic_and_panel_only"]="qgr_covariant_weyl3_critic" in src and "qgr_covariant_weyl3_panel" in src
    controls["exact_fraction_present"]="Fraction" in src and "Fraction" in term
    controls["no_tolerance_classifier"]="isclose(" not in src+term
    out={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"classification":"PASS_CORRECTED_CRITIC_SLOT00_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_CORRECTED_CRITIC_SLOT00_SOURCE_LOCK"}
    out["payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
