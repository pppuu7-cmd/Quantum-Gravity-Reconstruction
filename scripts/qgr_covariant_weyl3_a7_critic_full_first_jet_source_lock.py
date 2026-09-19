#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,subprocess,tempfile
from pathlib import Path

FORBIDDEN=("qgr_covariant_weyl3_a7_fi_jet_researcher","isclose(","numpy.isclose","np.isclose")

def run(*a): return subprocess.check_output(a,text=True).strip()
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--binding",required=True); ap.add_argument("--output",required=True); q=ap.parse_args()
    b=json.loads(Path(q.binding).read_text())
    controls={
      "prereg_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["preregistration_commit"],"HEAD"]).returncode==0,
      "parent_fi_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["parent_fi_result_commit"],"HEAD"]).returncode==0,
      "slot00_closure_ancestor":subprocess.run(["git","merge-base","--is-ancestor",b["slot00_closure_commit"],"HEAD"]).returncode==0
    }
    blobs={}; texts={}
    for name,spec in b["frozen_files"].items():
        actual=run("git","rev-parse",f"HEAD:{spec['path']}")
        blobs[name]={"path":spec["path"],"expected":spec["blob"],"actual":actual,"exact":actual==spec["blob"]}
        texts[name]=Path(spec["path"]).read_text()
    controls["all_frozen_blobs_exact"]=all(x["exact"] for x in blobs.values())

    old_binding=b["historical_researcher_binding_path"]
    with tempfile.TemporaryDirectory() as td:
        outp=str(Path(td)/"historical_lock.json")
        p=subprocess.run(["python","scripts/qgr_covariant_weyl3_a7_fi_jet_source_lock.py","--binding",old_binding,"--output",outp],text=True,capture_output=True)
        old=json.loads(Path(outp).read_text()) if Path(outp).exists() else {}
    controls["historical_fi_jet_source_lock_replays"]=p.returncode==0 and old.get("classification")=="PASS_FI_JET_SOURCE_PROVENANCE_LOCK"

    corrected=texts["corrected"]
    reference=texts["reference_researcher"]
    terminal=texts["terminal"]
    controls["corrected_no_researcher_import"]=not any(x in corrected for x in FORBIDDEN)
    controls["reference_is_exact_historical_researcher"]="RESEARCHER_DIRECT_METRIC_FI_FIRST_JETS" in reference
    controls["terminal_no_science_imports"]="qgr_covariant_weyl3_researcher" not in terminal and "qgr_covariant_weyl3_critic" not in terminal
    controls["exact_fraction_present"]="Fraction" in corrected and "Fraction" in reference and "Fraction" in terminal
    controls["no_tolerance_patterns"]="isclose(" not in corrected+reference+terminal
    out={"gate":b["gate"],"controls":controls,"blob_checks":blobs,"historical_source_lock":old,"classification":"PASS_FULL_CORRECTED_CRITIC_SOURCE_LOCK" if all(controls.values()) else "BLOCKED_FULL_CORRECTED_CRITIC_SOURCE_LOCK"}
    out["payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
