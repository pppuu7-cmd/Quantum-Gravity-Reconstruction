#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

PREREG="d33392623c576cb22e00ad2c49f48157cbe5729b"
FROZEN_CRITIC=F("-13469266506757221030260385050166541/4364950942592885650296098808000000")
FROZEN_RESEARCHER=F("-43977684225232401744358310400305192156031283/25865232290557867013685792372725281247232000")
FROZEN_RESEARCHER_CONNECTION=F("433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000")
FROZEN_B_TENSOR_SHA="702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4"

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--replay",required=True); ap.add_argument("--output",required=True); q=ap.parse_args()
    x=json.loads(Path(q.replay).read_text())
    original=F(x.get("original_d0_F0","0"))
    corrected=F(x.get("corrected_d0_F0","0"))
    completion=F(x.get("connection_completion","0"))
    controls={
      "preregistration_exact":x.get("preregistration_commit")==PREREG,
      "replay_ready":x.get("classification")=="CORRECTED_CRITIC_SLOT00_WITNESS_READY" and all(v is True for v in x.get("controls",{}).values()),
      "original_critic_slot_reproduced":original==FROZEN_CRITIC,
      "conversion_tensor_matches_independent_B":x.get("conversion_tensor_sha256")==FROZEN_B_TENSOR_SHA,
      "pointwise_unchanged":x.get("original_pointwise_Fi0")==x.get("corrected_pointwise_Fi0"),
      "only_connection_source_changed":x.get("controls",{}).get("only_connection_source_changed") is True
    }
    if not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif corrected==FROZEN_RESEARCHER:
        cls="CORRECTED_CRITIC_SLOT00_EXACTLY_MATCHES_RESEARCHER"
    else:
        cls="CORRECTED_CRITIC_SLOT00_REMAINS_DIFFERENT"
    out={
      "gate":"COVARIANT_WEYL3_A7_CRITIC_SLOT00_CONNECTION_COMPLETION_REPLAY",
      "preregistration_commit":PREREG,
      "classification":cls,
      "controls":controls,
      "frozen_critic_d0_F0":fs(FROZEN_CRITIC),
      "frozen_researcher_d0_F0":fs(FROZEN_RESEARCHER),
      "original_critic_d0_F0":fs(original),
      "connection_completion":fs(completion),
      "frozen_researcher_connection_jet":fs(FROZEN_RESEARCHER_CONNECTION),
      "connection_completion_matches_researcher_connection":completion==FROZEN_RESEARCHER_CONNECTION,
      "corrected_critic_d0_F0":fs(corrected),
      "corrected_minus_researcher":fs(corrected-FROZEN_RESEARCHER),
      "conversion_tensor_sha256":x.get("conversion_tensor_sha256"),
      "frozen_lane_b_tensor_sha256":FROZEN_B_TENSOR_SHA,
      "replay_payload_sha256":x.get("payload_sha256"),
      "parent_reclassification_authorized":False,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0
    }
    out["terminal_payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True)
    Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0
if __name__=="__main__": raise SystemExit(main())
