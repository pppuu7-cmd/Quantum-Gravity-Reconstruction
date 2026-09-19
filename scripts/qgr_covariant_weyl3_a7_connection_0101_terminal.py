#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
PREREG="7b9d2ffb84993f04e467c0a9ea6bf650327f6b62"
CLASSES=["FREE_INDEX_PLACEMENT","METRIC_INVERSE_METRIC_CONTRACTIONS","CONNECTION_FACTOR_CHANNELS","HESSIAN_CHANNELS","GAMMAGAMMA_DUMMY_CHANNELS","DUAL_POLYNOMIAL_CHANNELS","PERMUTATION_ANTISYMMETRY_FACTORS","FINAL_COMPONENT_SUM"]
EXPECTED_HASH={"A":"6dce9ed04c9199cf36eb2a723095f7eeba3f002844c3cd9df7da33704cbdf673","B":"702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4","C":"e3797c7dade7f4de601ba047be48b0ed73278333e01719e3b0d97588e783deb8"}
EXPECTED_SCALAR={"A":F("-433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000"),"B":F("433508011369185071313333891829231313950116629/312885874482554842907489423863612273152000000"),"C":F("6471547181136613219970862102277757857/3453429297335638404524090924141568000")}
def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def cmap(x,cls): return {e["key"]:F(e["value"]) for e in x.get("classes",{}).get(cls,[])}
def first_diff(lanes,names,classes):
 for cls in classes:
  maps=[cmap(x,cls) for x in lanes]; keys=sorted(set().union(*[set(m) for m in maps]))
  for key in keys:
   vals=[m.get(key,F(0)) for m in maps]
   if len(set(vals))!=1: return {"class":cls,"key":key,"values":{n:fs(v) for n,v in zip(names,vals)}}
 return None
def first_pair(x,y,nx,ny,classes):
 for cls in classes:
  a,b=cmap(x,cls),cmap(y,cls)
  for key in sorted(set(a)|set(b)):
   va,vb=a.get(key,F(0)),b.get(key,F(0))
   if va!=vb:return {"class":cls,"key":key,"values":{nx:fs(va),ny:fs(vb)},"exact_negative":va==-vb}
 return None
def main():
 ap=argparse.ArgumentParser()
 for n in ("a","b","c","output"): ap.add_argument("--"+n,required=True)
 q=ap.parse_args(); A=json.loads(Path(q.a).read_text()); B=json.loads(Path(q.b).read_text()); C=json.loads(Path(q.c).read_text()); lanes=[A,B,C]; names=["A","B","C"]
 controls={
  "preregistration_exact":all(x.get("preregistration_commit")==PREREG for x in lanes),
  "witness_exact":all((x.get("seed"),x.get("direction"),x.get("i"),x.get("j"),x.get("component"))==("OFFSHELL_A",7,0,0,[0,1,0,1]) for x in lanes),
  "lanes_ready":(A.get("classification"),B.get("classification"),C.get("classification"))==("LANE_A_PRIMITIVE_LEDGER_READY","LANE_B_PRIMITIVE_LEDGER_READY","LANE_C_PRIMITIVE_LEDGER_READY"),
  "parent_tensor_hashes_exact":A.get("full_tensor_sha256")==EXPECTED_HASH["A"] and B.get("full_tensor_sha256")==EXPECTED_HASH["B"] and C.get("full_tensor_sha256")==EXPECTED_HASH["C"],
  "parent_scalar_controls_exact":F(A.get("scalar_control","0"))==EXPECTED_SCALAR["A"] and F(B.get("scalar_control","0"))==EXPECTED_SCALAR["B"] and F(C.get("scalar_control","0"))==EXPECTED_SCALAR["C"]
 }
 overall=first_diff(lanes,names,CLASSES)
 pairs={
  "A_B":first_pair(A,B,"A","B",CLASSES),
  "A_C":first_pair(A,C,"A","C",CLASSES),
  "B_C":first_pair(B,C,"B","C",CLASSES)
 }
 shared={k:first_pair(x,y,nx,ny,CLASSES[:3]) for k,(x,y,nx,ny) in {
  "A_B":(A,B,"A","B"),"A_C":(A,C,"A","C"),"B_C":(B,C,"B","C")}.items()}
 finals=[F(x.get("component_value","0")) for x in lanes]
 primitive_classes=CLASSES[:-1]
 primitive_diff=first_diff(lanes,names,primitive_classes)
 if not all(controls.values()): cls="BLOCKED_EXECUTION_OR_PROVENANCE"
 elif primitive_diff is None and len(set(finals))!=1: cls="COMPONENT_0101_PRIMITIVE_LEDGER_ALL_THREE_MATCH_BUT_SUM_DIVERGES"
 else: cls="COMPONENT_0101_PRIMITIVE_DIVERGENCE_LOCALIZED"
 out={"gate":"COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION","preregistration_commit":PREREG,"classification":cls,"controls":controls,"first_all_three_divergence":overall,"first_pairwise_divergence":pairs,"first_shared_input_divergence":shared,"component_values":{"A":fs(finals[0]),"B":fs(finals[1]),"C":fs(finals[2])},"full_tensor_sha256":{"A":A.get("full_tensor_sha256"),"B":B.get("full_tensor_sha256"),"C":C.get("full_tensor_sha256")},"lane_payload_sha256":{"A":A.get("payload_sha256"),"B":B.get("payload_sha256"),"C":C.get("payload_sha256")},"posthoc_repair_authorized":False,"c6":"SYMBOLIC_UNFIXED","corrected_q10_locked":True,"theory_established_pct":0}
 out["terminal_payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2)); return 2 if cls=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0
if __name__=="__main__": raise SystemExit(main())
