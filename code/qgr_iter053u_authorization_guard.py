#!/usr/bin/env python3
"""Fail-closed execution guard for conditional Iter053U.

The guard intentionally reads only durable repository recovery state. It does
not inspect workflow partial values or infer authorization from green CI.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PRIMARY="ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED"
COMPANION="ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED"


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--state",default="recovery/state.json")
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    state=json.loads(Path(a.state).read_text(encoding="utf-8"))
    p=state.get("iter053t_primary",{})
    q=state.get("iter053t_nodewise_companion",{})
    pc=p.get("classification")
    qc=q.get("classification")
    authorized=bool(pc==PRIMARY and qc==COMPANION)
    out={
        "gate":"ITER053U-EXECUTION-AUTHORIZATION-GUARD",
        "required_primary_classification":PRIMARY,
        "found_primary_classification":pc,
        "required_companion_classification":COMPANION,
        "found_companion_classification":qc,
        "authorized":authorized,
        "policy":"DURABLE_TERMINAL_RECOVERY_ONLY_NO_PARTIAL_ACTIONS_VALUES_NO_MAJORITY_VOTE",
    }
    pth=Path(a.out); pth.parent.mkdir(parents=True,exist_ok=True)
    pth.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    if not authorized:
        raise SystemExit(5)

if __name__=="__main__": main()
