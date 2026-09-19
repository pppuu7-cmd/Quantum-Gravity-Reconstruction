#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

PREREG="bbb4e90e46ddd1aded691a1d780e10dbe0313e51"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def cmap(comp):
    return {k:F(v) for k,v in comp.get("terms",[])}
def equal(a,b,neg=False):
    for ca,cb in zip(a,b):
        ma,mb=cmap(ca),cmap(cb)
        for k in set(ma)|set(mb):
            va,vb=ma.get(k,F(0)),mb.get(k,F(0))
            if va != (-vb if neg else vb): return False
    return True
def first_mismatch(a,b,neg=False):
    for ca,cb in zip(a,b):
        idx=ca["index"]; ma,mb=cmap(ca),cmap(cb)
        for k in sorted(set(ma)|set(mb)):
            va,vb=ma.get(k,F(0)),mb.get(k,F(0)); target=-vb if neg else vb
            if va!=target:
                def fs(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
                return {"component":idx,"monomial":k,"A":fs(va),"B":fs(vb),"relation_tested":"A_EQ_NEG_B" if neg else "A_EQ_B"}
    return None
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--a",required=True); ap.add_argument("--b",required=True); ap.add_argument("--output",required=True); q=ap.parse_args()
    A=json.loads(Path(q.a).read_text()); B=json.loads(Path(q.b).read_text())
    ac=A.get("components",[]); bc=B.get("components",[]); bad=A.get("malformed_control_components",[])
    controls={
      "preregistration_exact":A.get("preregistration_commit")==PREREG and B.get("preregistration_commit")==PREREG,
      "lanes_ready":A.get("classification")=="FORMAL_LANE_A_READY" and B.get("classification")=="FORMAL_LANE_B_READY",
      "basis_exact":A.get("basis")==B.get("basis")=="canonical g2[ab|pq]*h[cd]",
      "all_256_components":len(ac)==len(bc)==len(bad)==256,
      "malformed_control_rejects_eq":not equal(bad,bc,False),
      "malformed_control_rejects_neg":not equal(bad,bc,True)
    }
    eq=equal(ac,bc,False) if all(controls.values()) else False
    neg=equal(ac,bc,True) if all(controls.values()) else False
    if not all(controls.values()): cls="BLOCKED_EXECUTION_OR_PROVENANCE"
    elif eq: cls="FORMAL_CONNECTION_TENSOR_A_EQ_B"
    elif neg: cls="FORMAL_CONNECTION_TENSOR_A_EQ_NEG_B"
    else: cls="FORMAL_CONNECTION_TENSOR_OTHER"
    out={
      "gate":"COVARIANT_WEYL3_A7_CONNECTION_FORMAL_MONOMIAL_IDENTITY_ADJUDICATION",
      "preregistration_commit":PREREG,
      "classification":cls,
      "controls":controls,
      "A_FORMAL_EQ_B":eq,
      "A_FORMAL_EQ_NEG_B":neg,
      "first_direct_mismatch":None if eq else first_mismatch(ac,bc,False),
      "first_negative_relation_mismatch":None if neg else first_mismatch(ac,bc,True),
      "lane_a_formal_sha256":A.get("tensor_formal_sha256"),
      "lane_b_formal_sha256":B.get("tensor_formal_sha256"),
      "malformed_control_sha256":A.get("malformed_control_sha256"),
      "lane_a_payload_sha256":A.get("payload_sha256"),
      "lane_b_payload_sha256":B.get("payload_sha256"),
      "posthoc_repair_authorized":False,
      "c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0
    }
    out["terminal_payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps(out,sort_keys=True,indent=2))
    return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0
if __name__=="__main__": raise SystemExit(main())
