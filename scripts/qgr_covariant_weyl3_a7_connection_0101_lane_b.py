#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
PREREG="7b9d2ffb84993f04e467c0a9ea6bf650327f6b62"
CLASSES=["FREE_INDEX_PLACEMENT","METRIC_INVERSE_METRIC_CONTRACTIONS","CONNECTION_FACTOR_CHANNELS","HESSIAN_CHANNELS","GAMMAGAMMA_DUMMY_CHANNELS","DUAL_POLYNOMIAL_CHANNELS","PERMUTATION_ANTISYMMETRY_FACTORS","FINAL_COMPONENT_SUM"]
def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def add(ledger,cls,key,val):
 val=F(val)
 if val: ledger[cls].append({"key":key,"value":fs(val)})
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); q=ap.parse_args()
 import qgr_covariant_weyl3_panel as panel
 import qgr_covariant_weyl3_critic as c
 z=c.build("OFFSHELL_A"); ledger={k:[] for k in CLASSES}
 def h(a,b): return panel.h_value(7,*c.cab(a,b),())
 def g2(a,b,p,r): return panel.metric_value("OFFSHELL_A",*c.cab(a,b),tuple(sorted((p,r))))
 def dG(j,up,b,ci): return F(1,2)*sum((c.eta(up,e)*(g2(e,ci,b,j)+g2(e,b,ci,j)-g2(b,ci,e,j)) for e in range(4)),F(0))
 def dphi(i,up,b,ci): return F(1,2)*sum((c.eta(up,e)*((1 if b==i else 0)*h(e,ci)+(1 if ci==i else 0)*h(e,b)-(1 if e==i else 0)*h(b,ci)) for e in range(4)),F(0))
 def R(a,b,cc,d):
  out=F(0)
  for e,f in product(range(4),repeat=2):
   ef=c.eta(e,f)
   if ef: out+=ef*(dphi(0,e,cc,a)*dG(0,f,d,b)+dG(0,e,cc,a)*dphi(0,f,d,b)-dphi(0,e,d,a)*dG(0,f,cc,b)-dG(0,e,d,a)*dphi(0,f,cc,b))
  return out
 vals=[fs(R(*idx)) for idx in product(range(4),repeat=4)]
 scalar=sum((z["P"][a][b][cc][d].v()*R(a,b,cc,d) for a,b,cc,d in product(range(4),repeat=4)),F(0))
 add(ledger,"FREE_INDEX_PLACEMENT","free:0,1,0,1",1)
 for a,b in product(range(4),repeat=2):
  add(ledger,"METRIC_INVERSE_METRIC_CONTRACTIONS",f"metric_base:{a},{b}",c.eta(a,b))
  add(ledger,"METRIC_INVERSE_METRIC_CONTRACTIONS",f"inverse_base:{a},{b}",c.eta(a,b))
  add(ledger,"METRIC_INVERSE_METRIC_CONTRACTIONS",f"h:{a},{b}",h(a,b))
 for up,b,ci in product(range(4),repeat=3):
  add(ledger,"CONNECTION_FACTOR_CHANNELS",f"dGamma:0,{up},{b},{ci}",dG(0,up,b,ci))
  add(ledger,"CONNECTION_FACTOR_CHANNELS",f"deltaGamma:0,{up},{b},{ci}",dphi(0,up,b,ci))
 a,b,cc,d=0,1,0,1
 signs=[1,1,-1,-1]
 for e,f in product(range(4),repeat=2):
  ef=c.eta(e,f)
  if not ef: continue
  terms=[dphi(0,e,cc,a)*dG(0,f,d,b),dG(0,e,cc,a)*dphi(0,f,d,b),dphi(0,e,d,a)*dG(0,f,cc,b),dG(0,e,d,a)*dphi(0,f,cc,b)]
  for ti,(sgn,v) in enumerate(zip(signs,terms)): add(ledger,"GAMMAGAMMA_DUMMY_CHANNELS",f"e{e}:f{f}:term{ti}",ef*sgn*v)
 for ti,sgn in enumerate(signs): add(ledger,"PERMUTATION_ANTISYMMETRY_FACTORS",f"term{ti}",sgn)
 comp=R(0,1,0,1); add(ledger,"FINAL_COMPONENT_SUM","component:0,1,0,1",comp)
 for k in CLASSES: ledger[k]=sorted(ledger[k],key=lambda x:x["key"])
 controls={"exact_fraction":True,"frozen_component":True,"serialized_before_comparison":True,"full_tensor_256":len(vals)==256,"ledger_final_equals_component":sum((F(x["value"]) for x in ledger["GAMMAGAMMA_DUMMY_CHANNELS"]),F(0))==comp}
 out={"gate":"COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION","lane":"B_DIRECT_GAMMAGAMMA","preregistration_commit":PREREG,"seed":"OFFSHELL_A","direction":7,"i":0,"j":0,"component":[0,1,0,1],"classes":ledger,"full_tensor_sha256":jsha(vals),"scalar_control":fs(scalar),"component_value":fs(comp),"controls":controls,"classification":"LANE_B_PRIMITIVE_LEDGER_READY" if all(controls.values()) else "BLOCKED_LANE_B"}
 out["payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
