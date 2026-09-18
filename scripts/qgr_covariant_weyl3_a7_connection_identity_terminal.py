#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG="d76dea1d511d0f7fa99b057866ef44fd797a1fc6"
PARENT_RESULT="07ad77de0506a3de5e7db601e2cfc8b5edc37c5c"
RESEARCHER_TARGET=F("433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000")
CRITIC_TARGET=F(0)

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--lane-a",required=True); ap.add_argument("--lane-b",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    A=json.loads(Path(a.lane_a).read_text()); B=json.loads(Path(a.lane_b).read_text())
    controls={
      "preregistration_exact":A.get("preregistration_commit")==B.get("preregistration_commit")==PREREG,
      "parent_terminal_exact":A.get("parent_terminal_commit")==B.get("parent_terminal_commit")==PARENT_RESULT,
      "same_frozen_witness":(A.get("seed"),A.get("direction"),A.get("i"),A.get("j"))==(B.get("seed"),B.get("direction"),B.get("i"),B.get("j"))==("OFFSHELL_A",7,0,0),
      "lane_a_ready":A.get("classification")=="TENSOR_HESSIAN_CONNECTION_WITNESS_READY" and all(v is True for v in A.get("controls",{}).values()),
      "lane_b_ready":B.get("classification")=="DIRECT_GAMMAGAMMA_CONNECTION_WITNESS_READY" and all(v is True for v in B.get("controls",{}).values()),
      "same_P_hash":A.get("P_point_sha256")==B.get("P_point_sha256"),
      "same_dGamma_hash":A.get("dGamma_sha256")==B.get("dGamma_sha256"),
      "target_blind_serialization":A.get("serialized_before_target_comparison") is True and B.get("serialized_before_target_comparison") is True,
      "c6_symbolic_unfixed":A.get("c6")==B.get("c6")=="SYMBOLIC_UNFIXED",
      "corrected_q10_locked":A.get("corrected_q10_locked") is True and B.get("corrected_q10_locked") is True,
    }
    av=F(A.get("connection_identity_value","0")); bv=F(B.get("connection_identity_value","0"))
    scalar_match=av==bv
    tensor_match=A.get("connection_tensor_sha256")==B.get("connection_tensor_sha256")
    controls["lane_identity_scalar_exact"]=scalar_match
    controls["lane_identity_tensor_exact"]=tensor_match
    blocked=not all(v for k,v in controls.items() if k not in ("lane_identity_scalar_exact","lane_identity_tensor_exact"))
    if blocked:
      cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif not scalar_match or not tensor_match:
      cls="CONNECTION_IDENTITY_DERIVATIONS_DISAGREE"
    elif av==RESEARCHER_TARGET:
      cls="CONNECTION_IDENTITY_MATCHES_RESEARCHER_NONZERO"
    elif av==CRITIC_TARGET:
      cls="CONNECTION_IDENTITY_MATCHES_CRITIC_ZERO"
    else:
      cls="CONNECTION_IDENTITY_MATCHES_NEITHER_PARENT"
    payload={
      "gate":"COVARIANT_WEYL3_A7_CONNECTION_JET_IDENTITY_ADJUDICATION",
      "preregistration_commit":PREREG,
      "parent_terminal_commit":PARENT_RESULT,
      "classification":cls,
      "controls":controls,
      "lane_a_value":fs(av),
      "lane_b_value":fs(bv),
      "lane_difference":fs(av-bv),
      "lane_a_tensor_sha256":A.get("connection_tensor_sha256"),
      "lane_b_tensor_sha256":B.get("connection_tensor_sha256"),
      "researcher_frozen_target":fs(RESEARCHER_TARGET),
      "critic_frozen_target":fs(CRITIC_TARGET),
      "matches_researcher":scalar_match and tensor_match and av==RESEARCHER_TARGET,
      "matches_critic":scalar_match and tensor_match and av==CRITIC_TARGET,
      "lane_a_payload_sha256":A.get("payload_sha256"),
      "lane_b_payload_sha256":B.get("payload_sha256"),
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
