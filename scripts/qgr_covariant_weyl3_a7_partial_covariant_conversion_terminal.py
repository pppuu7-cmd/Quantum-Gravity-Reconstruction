#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

PREREG="7ef60246ae816730bb702ce0d9fd7284362b3b70"
FORMAL_A="ba7ed7b7eb2b8fa66dbc07ffd6b6a66f7f2896f242257c6830e77cb56b6f2c32"
FORMAL_B="09ee351958f9f066a84b581194275fffc73c123744f24c6b8cdff26ce4693034"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--conversion",required=True); ap.add_argument("--output",required=True); q=ap.parse_args()
    x=json.loads(Path(q.conversion).read_text())
    controls={
      "preregistration_exact":x.get("preregistration_commit")==PREREG,
      "conversion_ready":x.get("classification")=="PARTIAL_COVARIANT_CONVERSION_READY" and all(v is True for v in x.get("controls",{}).values()),
      "basis_exact":x.get("basis")=="canonical g2[ab|pq]*h[cd]",
      "malformed_rejects_A":x.get("malformed_formal_sha256")!=FORMAL_A,
      "malformed_rejects_B":x.get("malformed_formal_sha256")!=FORMAL_B
    }
    h=x.get("tensor_formal_sha256")
    nh=x.get("negated_tensor_formal_sha256")
    if not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif h==FORMAL_A:
        cls="PARTIAL_COVARIANT_CONVERSION_MATCHES_FORMAL_A"
    elif h==FORMAL_B:
        cls="PARTIAL_COVARIANT_CONVERSION_MATCHES_FORMAL_B"
    else:
        cls="PARTIAL_COVARIANT_CONVERSION_MATCHES_NEITHER"
    out={
      "gate":"COVARIANT_WEYL3_A7_PARTIAL_COVARIANT_HESSIAN_CONVERSION_SIGN_AUDIT",
      "preregistration_commit":PREREG,
      "classification":cls,
      "controls":controls,
      "conversion_formal_sha256":h,
      "negated_conversion_formal_sha256":nh,
      "formal_lane_a_sha256":FORMAL_A,
      "formal_lane_b_sha256":FORMAL_B,
      "conversion_matches_A":h==FORMAL_A,
      "conversion_matches_B":h==FORMAL_B,
      "negated_conversion_matches_A":nh==FORMAL_A,
      "negated_conversion_matches_B":nh==FORMAL_B,
      "malformed_formal_sha256":x.get("malformed_formal_sha256"),
      "conversion_payload_sha256":x.get("payload_sha256"),
      "posthoc_repair_authorized":False,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0
    }
    out["terminal_payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True)
    Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0
if __name__=="__main__": raise SystemExit(main())
