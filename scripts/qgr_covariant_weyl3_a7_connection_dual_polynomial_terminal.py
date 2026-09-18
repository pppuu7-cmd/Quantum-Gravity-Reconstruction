#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG="ed829c5f60f2fad6a308ec3f9c50695a6777567e"
PARENT_RESULT="267743ee78ea0ebd51fd697003cc1207a9d9032b"
LANE_A=F("-433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000")
LANE_B=F("433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000")

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--extraction",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    x=json.loads(Path(a.extraction).read_text())
    controls={
      "preregistration_exact":x.get("preregistration_commit")==PREREG,
      "parent_terminal_exact":x.get("parent_terminal_commit")==PARENT_RESULT,
      "frozen_witness_exact":(x.get("seed"),x.get("direction"),x.get("i"),x.get("j"))==("OFFSHELL_A",7,0,0),
      "extraction_ready":x.get("classification")=="DUAL_POLYNOMIAL_CONNECTION_WITNESS_READY" and all(v is True for v in x.get("controls",{}).values()),
      "target_blind_serialization":x.get("serialized_before_target_comparison") is True,
      "c6_symbolic_unfixed":x.get("c6")=="SYMBOLIC_UNFIXED",
      "corrected_q10_locked":x.get("corrected_q10_locked") is True,
    }
    v=F(x.get("connection_identity_value","0"))
    if not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif v==LANE_A:
        cls="DUAL_POLYNOMIAL_EXTRACTION_MATCHES_LANE_A"
    elif v==LANE_B:
        cls="DUAL_POLYNOMIAL_EXTRACTION_MATCHES_LANE_B"
    else:
        cls="DUAL_POLYNOMIAL_EXTRACTION_MATCHES_NEITHER"
    payload={
      "gate":"COVARIANT_WEYL3_A7_CONNECTION_DUAL_POLYNOMIAL_SIGN_ADJUDICATION",
      "preregistration_commit":PREREG,
      "parent_terminal_commit":PARENT_RESULT,
      "classification":cls,
      "controls":controls,
      "extracted_value":fs(v),
      "lane_a_frozen_value":fs(LANE_A),
      "lane_b_frozen_value":fs(LANE_B),
      "difference_from_lane_a":fs(v-LANE_A),
      "difference_from_lane_b":fs(v-LANE_B),
      "extraction_tensor_sha256":x.get("connection_tensor_sha256"),
      "extraction_payload_sha256":x.get("payload_sha256"),
      "posthoc_repair_authorized":False,
      "c6":"SYMBOLIC_UNFIXED",
      "corrected_q10_locked":True,
      "theory_established_pct":0,
    }
    payload["terminal_payload_sha256"]=jsha(payload)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print(json.dumps(payload,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0

if __name__=="__main__": raise SystemExit(main())
