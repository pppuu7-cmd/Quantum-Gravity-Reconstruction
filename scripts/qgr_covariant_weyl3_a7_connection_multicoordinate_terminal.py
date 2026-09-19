#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

PREREG="58284ae7f71e73db5c2d71d157bc74bd7d646030"
PARENT="199ecea77c9138c4a166d1ffc7143ce2d0de34be"
A_HASH="6dce9ed04c9199cf36eb2a723095f7eeba3f002844c3cd9df7da33704cbdf673"
B_HASH="702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4"
LEGACY_C_HASH="e3797c7dade7f4de601ba047be48b0ed73278333e01719e3b0d97588e783deb8"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--extraction",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    x=json.loads(Path(a.extraction).read_text())
    controls={
      "preregistration_exact":x.get("preregistration_commit")==PREREG,
      "parent_terminal_exact":x.get("parent_terminal_commit")==PARENT,
      "witness_exact":(x.get("seed"),x.get("direction"),x.get("i"),x.get("j"),x.get("component"))==("OFFSHELL_A",7,0,0,[0,1,0,1]),
      "extraction_ready":x.get("classification")=="MULTICOORDINATE_NEUTRAL_WITNESS_READY" and all(v is True for v in x.get("controls",{}).values()),
      "all_64_dGamma_exact":x.get("controls",{}).get("all_64_dGamma_exact") is True,
      "all_64_deltaGamma_exact":x.get("controls",{}).get("all_64_deltaGamma_exact") is True,
      "serialized_256":len(x.get("tensor_values",[]))==256,
      "c6_symbolic_unfixed":x.get("c6")=="SYMBOLIC_UNFIXED",
      "corrected_q10_locked":x.get("corrected_q10_locked") is True
    }
    h=x.get("tensor_sha256")
    if not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif h==A_HASH:
        cls="MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_A"
    elif h==B_HASH:
        cls="MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_B"
    else:
        cls="MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_NEITHER"
    out={
      "gate":"COVARIANT_WEYL3_A7_CONNECTION_MULTICOORDINATE_NEUTRAL_EXTRACTION",
      "preregistration_commit":PREREG,
      "parent_terminal_commit":PARENT,
      "classification":cls,
      "controls":controls,
      "neutral_tensor_sha256":h,
      "lane_a_tensor_sha256":A_HASH,
      "lane_b_tensor_sha256":B_HASH,
      "legacy_lane_c_tensor_sha256":LEGACY_C_HASH,
      "matches_legacy_c":h==LEGACY_C_HASH,
      "component_0101_value":x.get("component_0101_value"),
      "scalar_control":x.get("scalar_control"),
      "dGamma_poly_sha256":x.get("dGamma_poly_sha256"),
      "dGamma_reference_sha256":x.get("dGamma_reference_sha256"),
      "deltaGamma_poly_sha256":x.get("deltaGamma_poly_sha256"),
      "deltaGamma_reference_sha256":x.get("deltaGamma_reference_sha256"),
      "extraction_payload_sha256":x.get("payload_sha256"),
      "legacy_result_reclassification_authorized":False,
      "posthoc_parent_repair_authorized":False,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0
    }
    out["terminal_payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0

if __name__=="__main__": raise SystemExit(main())
