#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
PREREG="63ead9c69964fe24ec647c7bda12c1ebc4aa28df"
EA=F("-433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000")
EB=-EA
EC=F("6471547181136613219970862102277757857/3453429297335638404524090924141568000")
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser()
 for x in ("a","b","c","output"): ap.add_argument("--"+x,required=True)
 q=ap.parse_args(); A=json.loads(Path(q.a).read_text()); B=json.loads(Path(q.b).read_text()); C=json.loads(Path(q.c).read_text())
 lanes=[A,B,C]; vals=[x.get("tensor_values",[]) for x in lanes]
 controls={
  "preregistration_exact":all(x.get("preregistration_commit")==PREREG for x in lanes),
  "witness_exact":all((x.get("seed"),x.get("direction"),x.get("i"),x.get("j"))==("OFFSHELL_A",7,0,0) for x in lanes),
  "lane_ready":(A.get("classification"),B.get("classification"),C.get("classification"))==("LANE_A_READY","LANE_B_READY","LANE_C_READY"),
  "serialized_256":all(len(v)==256 for v in vals),
  "index_order_exact":all(x.get("index_order")=="lexicographic(a,b,c,d),d-fastest" for x in lanes),
  "scalar_controls_exact":F(A.get("scalar_control","0"))==EA and F(B.get("scalar_control","0"))==EB and F(C.get("scalar_control","0"))==EC,
  "c6_q10_locks":all(x.get("controls",{}).get("c6_symbolic_unfixed") is True and x.get("controls",{}).get("corrected_q10_locked") is True for x in lanes)
 }
 if not all(controls.values()):
  cls="BLOCKED_EXECUTION_OR_PROVENANCE"; first=None
 else:
  first=None
  for n,(va,vb,vc) in enumerate(zip(*vals)):
   if not (F(va)==F(vb)==F(vc)):
    first=list(product(range(4),repeat=4))[n]; break
  cls="CONNECTION_TENSOR_ALL_THREE_EXACT_MATCH" if first is None else "CONNECTION_TENSOR_COMPONENT_DIVERGENCE_LOCALIZED"
 rel={}
 if all(len(v)==256 for v in vals):
  rel={"A_EQ_B":all(F(a)==F(b) for a,b in zip(vals[0],vals[1])),
       "A_EQ_C":all(F(a)==F(c) for a,c in zip(vals[0],vals[2])),
       "B_EQ_C":all(F(b)==F(c) for b,c in zip(vals[1],vals[2])),
       "A_EQ_NEG_B":all(F(a)==-F(b) for a,b in zip(vals[0],vals[1])),
       "A_EQ_NEG_C":all(F(a)==-F(c) for a,c in zip(vals[0],vals[2])),
       "B_EQ_NEG_C":all(F(b)==-F(c) for b,c in zip(vals[1],vals[2]))}
 out={"gate":"COVARIANT_WEYL3_A7_CONNECTION_TENSOR_COMPONENT_LOCALIZATION","preregistration_commit":PREREG,"classification":cls,"controls":controls,"first_divergent_component":first,"pairwise_relations":rel,"lane_tensor_sha256":{"A":A.get("tensor_sha256"),"B":B.get("tensor_sha256"),"C":C.get("tensor_sha256")},"lane_payload_sha256":{"A":A.get("payload_sha256"),"B":B.get("payload_sha256"),"C":C.get("payload_sha256")},"scalar_controls":{"A":A.get("scalar_control"),"B":B.get("scalar_control"),"C":C.get("scalar_control")},"posthoc_repair_authorized":False,"c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0}
 out["terminal_payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2)); return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0
if __name__=="__main__": raise SystemExit(main())
