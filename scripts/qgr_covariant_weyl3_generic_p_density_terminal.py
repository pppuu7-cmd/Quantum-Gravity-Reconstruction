#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG="7a62dd856aec084add16af8e6793d157ef32637b"
PARENT_D_HASH="138c715fb96eadf5162b4442aaaeed65007f3d40ab2b7f63805fab0074d6e98c"
PARENT_G_HASH="34d9ca91b11fa47b3a7f9b77f4f833788fcdf68d9f1684dd8c375d6e4f5cc8fa"

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def loadmap(xs):
    return {k:F(v) for k,v in xs}

def compare(a,b,negative=False):
    for k in sorted(set(a)|set(b)):
        av=a.get(k,F(0)); bv=b.get(k,F(0))
        target=-bv if negative else bv
        if av!=target:
            return False,{"monomial":k,"D":fs(av),"weighted":fs(bv),"difference":fs(av-target)}
    return True,None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lane-d",required=True)
    ap.add_argument("--weighted",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()

    D=json.loads(Path(a.lane_d).read_text())
    W=json.loads(Path(a.weighted).read_text())
    dm=loadmap(D.get("terms",[]))
    wm=loadmap(W.get("weighted_terms",[]))
    unweighted=loadmap(W.get("tensor_connection_terms",[]))

    controls={
        "preregistration_exact":W.get("preregistration_commit")==PREREG,
        "lane_d_reference_ready":D.get("classification")=="GENERIC_P_LANE_D_READY",
        "weighted_lane_ready":W.get("classification")=="GENERIC_P_WEIGHTED_LANE_READY" and all(v is True for v in W.get("controls",{}).values()),
        "basis_exact":D.get("basis")==W.get("basis")=="P[pair|pair]*g2[pair|pair]*h[pair]",
        "parent_lane_d_reproduced":D.get("formal_sha256")==PARENT_D_HASH,
        "unweighted_parent_lane_g_reproduced":W.get("tensor_connection_sha256")==PARENT_G_HASH,
        "density_weight_channel_nonzero":W.get("density_weight_term_count",0)>0,
        "c6_symbolic_unfixed":D.get("c6")==W.get("c6")=="SYMBOLIC_UNFIXED",
        "corrected_q10_locked":D.get("corrected_q10_locked") is True and W.get("corrected_q10_locked") is True
    }

    eq,eq_mismatch=compare(dm,wm,False)
    neg,neg_mismatch=compare(dm,wm,True)
    old_eq,_=compare(dm,unweighted,False)
    old_neg,_=compare(dm,unweighted,True)

    if not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif eq:
        cls="GENERIC_P_TENSOR_DENSITY_COMPLETION_EQ_DIRECT_CONVERSION"
    elif neg:
        cls="GENERIC_P_TENSOR_DENSITY_COMPLETION_EQ_NEG_DIRECT_CONVERSION"
    else:
        cls="GENERIC_P_TENSOR_DENSITY_COMPLETION_OTHER"

    if cls=="GENERIC_P_TENSOR_DENSITY_COMPLETION_EQ_DIRECT_CONVERSION":
        controls["unweighted_negative_control_rejects_authoritative_relation"]=not old_eq
    elif cls=="GENERIC_P_TENSOR_DENSITY_COMPLETION_EQ_NEG_DIRECT_CONVERSION":
        controls["unweighted_negative_control_rejects_authoritative_relation"]=not old_neg
    else:
        controls["unweighted_negative_control_rejects_authoritative_relation"]=True

    if cls!="BLOCKED_EXECUTION_OR_PROVENANCE" and not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"

    out={
        "gate":"COVARIANT_WEYL3_GENERIC_P_TENSOR_DENSITY_CONNECTION_COMPLETION",
        "preregistration_commit":PREREG,
        "classification":cls,
        "controls":controls,
        "D_EQ_G_WEIGHTED":eq,
        "D_EQ_NEG_G_WEIGHTED":neg,
        "first_direct_mismatch":None if eq else eq_mismatch,
        "first_exact_negative_mismatch":None if neg else neg_mismatch,
        "unweighted_D_EQ_G":old_eq,
        "unweighted_D_EQ_NEG_G":old_neg,
        "lane_d_formal_sha256":D.get("formal_sha256"),
        "weighted_tensor_part_sha256":W.get("tensor_connection_sha256"),
        "density_weight_sha256":W.get("density_weight_sha256"),
        "weighted_formal_sha256":W.get("weighted_sha256"),
        "lane_d_payload_sha256":D.get("payload_sha256"),
        "weighted_payload_sha256":W.get("payload_sha256"),
        "historical_parent_reclassification_authorized":False,
        "global_weyl3_promotion_authorized":False,
        "c6":"SYMBOLIC_UNFIXED",
        "corrected_q10_locked":True,
        "theory_established_pct":0
    }
    out["terminal_payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0

if __name__=="__main__":
    raise SystemExit(main())
