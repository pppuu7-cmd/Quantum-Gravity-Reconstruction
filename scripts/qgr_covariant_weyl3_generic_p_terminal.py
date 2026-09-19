#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG="a388b8fdef54742b4e6120b8f23965d604aa4e04"

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def loadmap(xs):
    return {k:F(v) for k,v in xs}

def compare(a,b,negative=False):
    keys=sorted(set(a)|set(b))
    for k in keys:
        av=a.get(k,F(0)); bv=b.get(k,F(0))
        target=-bv if negative else bv
        if av!=target:
            return False,{"monomial":k,"D":fs(av),"G":fs(bv),"difference":fs(av-target)}
    return True,None

def common_ratio(a,b):
    keys=sorted(set(a)|set(b))
    ratios=set()
    for k in keys:
        av=a.get(k,F(0)); bv=b.get(k,F(0))
        if av==0 and bv==0:
            continue
        if av==0 or bv==0:
            return None
        ratios.add(av/bv)
        if len(ratios)>1:
            return None
    if len(ratios)==1:
        return fs(next(iter(ratios)))
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--lane-d",required=True)
    ap.add_argument("--lane-g",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()

    D=json.loads(Path(a.lane_d).read_text())
    G=json.loads(Path(a.lane_g).read_text())
    dm=loadmap(D.get("terms",[]))
    gm=loadmap(G.get("terms",[]))
    bad=loadmap(G.get("malformed_terms",[]))

    controls={
        "preregistration_exact":D.get("preregistration_commit")==PREREG and G.get("preregistration_commit")==PREREG,
        "lanes_ready":D.get("classification")=="GENERIC_P_LANE_D_READY" and G.get("classification")=="GENERIC_P_LANE_G_READY",
        "basis_exact":D.get("basis")==G.get("basis")=="P[pair|pair]*g2[pair|pair]*h[pair]",
        "pair_symmetry_contract_exact":D.get("P_symmetry")==G.get("P_symmetry"),
        "serialized_maps_nonempty":bool(dm) and bool(gm),
        "c6_symbolic_unfixed":D.get("c6")==G.get("c6")=="SYMBOLIC_UNFIXED",
        "corrected_q10_locked":D.get("corrected_q10_locked") is True and G.get("corrected_q10_locked") is True
    }

    eq,eq_mismatch=compare(dm,gm,False)
    neg,neg_mismatch=compare(dm,gm,True)
    bad_eq,_=compare(dm,bad,False)
    bad_neg,_=compare(dm,bad,True)

    if not all(controls.values()):
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif eq:
        cls="GENERIC_P_DIRECT_CONVERSION_EQ_COVARIANT_GAP"
    elif neg:
        cls="GENERIC_P_DIRECT_CONVERSION_EQ_NEG_COVARIANT_GAP"
    else:
        cls="GENERIC_P_DIRECT_CONVERSION_OTHER"

    if cls=="GENERIC_P_DIRECT_CONVERSION_EQ_COVARIANT_GAP":
        malformed_rejects=not bad_eq
    elif cls=="GENERIC_P_DIRECT_CONVERSION_EQ_NEG_COVARIANT_GAP":
        malformed_rejects=not bad_neg
    else:
        malformed_rejects=True

    controls["malformed_rejects_authoritative_relation"]=malformed_rejects
    if cls!="BLOCKED_EXECUTION_OR_PROVENANCE" and not malformed_rejects:
        cls="BLOCKED_EXECUTION_OR_PROVENANCE"

    out={
        "gate":"COVARIANT_WEYL3_GENERIC_P_CONNECTION_COVARIANTIZATION_IDENTITY",
        "preregistration_commit":PREREG,
        "classification":cls,
        "controls":controls,
        "D_EQ_G":eq,
        "D_EQ_NEG_G":neg,
        "first_direct_equality_mismatch":None if eq else eq_mismatch,
        "first_exact_negative_mismatch":None if neg else neg_mismatch,
        "common_exact_ratio_D_over_G":common_ratio(dm,gm),
        "lane_d_term_count":D.get("term_count"),
        "lane_g_term_count":G.get("term_count"),
        "lane_d_formal_sha256":D.get("formal_sha256"),
        "lane_g_formal_sha256":G.get("formal_sha256"),
        "malformed_g_formal_sha256":G.get("malformed_sha256"),
        "lane_d_payload_sha256":D.get("payload_sha256"),
        "lane_g_payload_sha256":G.get("payload_sha256"),
        "malformed_D_EQ_G":bad_eq,
        "malformed_D_EQ_NEG_G":bad_neg,
        "historical_parent_reclassification_authorized":False,
        "corrected_six_cell_global_promotion_authorized":False,
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
