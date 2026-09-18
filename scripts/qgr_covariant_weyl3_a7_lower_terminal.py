#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

PREREG="a8c7bd1bd5280f18aa50955b4cd847b707c178ab"
BINDING="f0081e60056106b0eac916b6f207ad03fc113233"
PARENT_DIRECT=F("141609523517262295106976925021598088976553029/33325122725952586818549169405591839744000000")
PARENT_EULER=F("36188861490208135407463132950092941670313420227/2815972870342993586167404814772510458368000000")
PARENT_DIFF=F("-86355995554365317186893343264769708206041673/10039118967354700841951532316479538176000000")
FROZEN_PRINCIPAL_SHA="fb20b1704d6e651ccae7df87591cd3961d6792a04d103a182aa712552db65896"
CLASS_KEYS=(
 "CONNECTION_VARIATION",
 "COVARIANTIZATION_GAMMA_TIMES_DH",
 "COVARIANTIZATION_DGAMMA_TIMES_H",
 "COVARIANTIZATION_GAMMA_GAMMA_TIMES_H",
 "IBP_FIRST_TRANSFER",
 "IBP_SECOND_TRANSFER",
 "ALGEBRAIC_CURVATURE_VARIATION",
 "VOLUME_CONTROL",
 "PRINCIPAL_CONTROL",
)
CONNECTION_KEYS=CLASS_KEYS[:4]

def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def jsha(x):
 return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def diff(a,b): return F(a)-F(b)

def first_vector_difference(rv,cv,key):
 if len(rv)!=len(cv): return {"slot":"LENGTH","researcher":str(len(rv)),"critic":str(len(cv)),"difference":"NONNUMERIC"}
 for x,y in zip(rv,cv):
  if x.get(key)!=y.get(key): return {"slot":f"KEY:{x.get(key)}!={y.get(key)}","researcher":x.get("value"),"critic":y.get("value"),"difference":"NONNUMERIC"}
  d=diff(x.get("value","0"),y.get("value","0"))
  if d: return {"slot":x.get(key),"researcher":x.get("value"),"critic":y.get("value"),"difference":fs(d)}
 return None

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--researcher",required=True); ap.add_argument("--critic",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
 r=json.loads(Path(a.researcher).read_text()); c=json.loads(Path(a.critic).read_text())
 controls={
  "preregistration_exact":r.get("preregistration_commit")==c.get("preregistration_commit")==PREREG,
  "binding_exact":r.get("implementation_binding_commit")==c.get("implementation_binding_commit")==BINDING,
  "same_frozen_counterexample":(r.get("seed"),r.get("direction"))==(c.get("seed"),c.get("direction"))==("OFFSHELL_A",7),
  "same_parent_jet":r.get("parent_jet_sha256")==c.get("parent_jet_sha256"),
  "researcher_ready":r.get("classification")=="RESEARCHER_LOWER_ORDER_WITNESS_READY" and all(v is True for v in r.get("controls",{}).values()),
  "critic_ready":c.get("classification")=="CRITIC_LOWER_ORDER_WITNESS_READY" and all(v is True for v in c.get("controls",{}).values()),
  "target_blind_serialization":r.get("target_blind_serialized_before_comparison") is True and c.get("target_blind_serialized_before_comparison") is True,
  "c6_symbolic_unfixed":r.get("c6")==c.get("c6")=="SYMBOLIC_UNFIXED",
  "corrected_q10_locked":r.get("corrected_q10_locked") is True and c.get("corrected_q10_locked") is True,
  "class_semantics_exact":tuple(r.get("class_order",[]))==tuple(c.get("class_order",[]))==CLASS_KEYS and set(r.get("classes",{}))==set(c.get("classes",{}))==set(CLASS_KEYS),
  "principal_hash_frozen":r.get("principal_vector_sha256")==c.get("principal_vector_sha256")==FROZEN_PRINCIPAL_SHA,
 }
 principal_first=first_vector_difference(r.get("principal_vector",[]),c.get("principal_vector",[]),"ij")
 controls["principal_slots_exact"]=principal_first is None
 controls["volume_exact"]=diff(r.get("volume","0"),c.get("volume","0"))==0

 rtotal=F(r.get("parent_total","0")); ctotal=F(c.get("parent_total","0")); fulldiff=rtotal-ctotal
 controls["parent_direct_exact"]=rtotal==PARENT_DIRECT
 controls["parent_euler_exact"]=ctotal==PARENT_EULER
 controls["parent_difference_exact"]=fulldiff==PARENT_DIFF

 rsum=sum((F(r.get("classes",{}).get(k,"0")) for k in CLASS_KEYS),F(0))
 csum=sum((F(c.get("classes",{}).get(k,"0")) for k in CLASS_KEYS),F(0))
 class_diffs=[{"class":k,"researcher":r["classes"][k],"critic":c["classes"][k],"difference":fs(F(r["classes"][k])-F(c["classes"][k]))} for k in CLASS_KEYS] if controls["class_semantics_exact"] else []
 class_diff_sum=sum((F(x["difference"]) for x in class_diffs),F(0)) if class_diffs else F(0)
 reconstruction={
  "researcher_class_sum":fs(rsum),"researcher_parent":fs(rtotal),"researcher_exact":rsum==rtotal,
  "critic_class_sum":fs(csum),"critic_parent":fs(ctotal),"critic_exact":csum==ctotal,
  "class_difference_sum":fs(class_diff_sum),"parent_difference":fs(fulldiff),"difference_exact":class_diff_sum==fulldiff,
 }

 stages=[]; first=None
 d1=diff(r.get("lower_order_curvature_before_ibp","0"),c.get("lower_order_curvature_before_ibp","0"))
 s1={"stage":"LOWER_ORDER_CURVATURE_VARIATION_BEFORE_IBP","exact_match":d1==0,"researcher":r.get("lower_order_curvature_before_ibp"),"critic":c.get("lower_order_curvature_before_ibp"),"difference":fs(d1)}; stages.append(s1)
 if d1 and first is None: first={"stage":s1["stage"],"slot":"SCALAR_F0_MINUS_VOLUME","researcher":s1["researcher"],"critic":s1["critic"],"difference":s1["difference"]}

 vf=first_vector_difference(r.get("Fi_vector",[]),c.get("Fi_vector",[]),"i")
 s2={"stage":"FIRST_DERIVATIVE_PERTURBATION_COEFFICIENTS","exact_match":vf is None,"first_difference":vf}; stages.append(s2)
 if vf is not None and first is None: first={"stage":s2["stage"],**vf}

 d3=diff(r.get("first_ibp_transfer","0"),c.get("first_ibp_transfer","0"))
 s3={"stage":"FIRST_DERIVATIVE_IBP_TRANSFER","exact_match":d3==0,"researcher":r.get("first_ibp_transfer"),"critic":c.get("first_ibp_transfer"),"difference":fs(d3)}; stages.append(s3)
 if d3 and first is None: first={"stage":s3["stage"],"slot":"SCALAR_TRANSFER","researcher":s3["researcher"],"critic":s3["critic"],"difference":s3["difference"]}

 d4=diff(r.get("second_ibp_transfer","0"),c.get("second_ibp_transfer","0"))
 s4={"stage":"SECOND_DERIVATIVE_LOWER_ORDER_IBP","exact_match":d4==0 and principal_first is None,"researcher":r.get("second_ibp_transfer"),"critic":c.get("second_ibp_transfer"),"difference":fs(d4),"principal_control_exact":principal_first is None}; stages.append(s4)
 if (d4 or principal_first is not None) and first is None:
  first={"stage":s4["stage"],"slot":"SCALAR_TRANSFER" if d4 else f"PRINCIPAL:{principal_first['slot']}","researcher":s4["researcher"] if d4 else principal_first["researcher"],"critic":s4["critic"] if d4 else principal_first["critic"],"difference":s4["difference"] if d4 else principal_first["difference"]}

 conn=[]
 for k in CONNECTION_KEYS:
  d=diff(r.get("classes",{}).get(k,"0"),c.get("classes",{}).get(k,"0"))
  conn.append({"class":k,"researcher":r.get("classes",{}).get(k),"critic":c.get("classes",{}).get(k),"difference":fs(d),"exact_match":d==0})
 s5={"stage":"COVARIANTIZATION_CONNECTION","exact_match":all(x["exact_match"] for x in conn),"classes":conn}; stages.append(s5)
 if first is None:
  for x in conn:
   if not x["exact_match"]:
    first={"stage":s5["stage"],"slot":x["class"],"researcher":x["researcher"],"critic":x["critic"],"difference":x["difference"]}; break

 s6={"stage":"ALGEBRAIC_EULER_TERM","status":"NOT_REACHED" if first is not None else ("NO_RESIDUAL_BY_RECONSTRUCTION" if fulldiff==0 else "UNACCOUNTED_RESIDUAL")}; stages.append(s6)

 blocked=not all(controls.values())
 decomposition_ok=reconstruction["researcher_exact"] and reconstruction["critic_exact"] and reconstruction["difference_exact"]
 if blocked:
  classification="BLOCKED_EXECUTION_OR_PROVENANCE"
 elif not decomposition_ok:
  classification="LOWER_ORDER_DECOMPOSITION_DISAGREES"
 elif fulldiff==0:
  classification="FULL_COVARIANT_AGREEMENT_RECOVERED"
 elif first is not None:
  classification="LOWER_ORDER_LOCALIZED_EXACT"
 else:
  classification="LOWER_ORDER_DECOMPOSITION_DISAGREES"

 payload={
  "gate":"COVARIANT_WEYL3_A7_LOWER_ORDER_COVARIANTIZATION_IBP_LOCALIZATION",
  "preregistration_commit":PREREG,
  "implementation_binding_commit":BINDING,
  "classification":classification,
  "controls":controls,
  "reconstruction":reconstruction,
  "stages":stages,
  "first_divergence":first,
  "class_differences":class_diffs,
  "parent":{"researcher_total":fs(rtotal),"critic_total":fs(ctotal),"difference":fs(fulldiff),"frozen_difference":fs(PARENT_DIFF)},
  "researcher_payload_sha256":r.get("payload_sha256"),
  "critic_payload_sha256":c.get("payload_sha256"),
  "posthoc_repair_authorized":False,
  "c6":"SYMBOLIC_UNFIXED",
  "corrected_q10_locked":True,
  "theory_established_pct":0,
 }
 payload["terminal_payload_sha256"]=jsha(payload)
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
 print(json.dumps(payload,sort_keys=True,indent=2))
 return 2 if classification=="BLOCKED_EXECUTION_OR_PROVENANCE" else 0

if __name__=="__main__": raise SystemExit(main())
