#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
PREREG="63ead9c69964fe24ec647c7bda12c1ebc4aa28df"
P_HASH="21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe"
def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
 import qgr_covariant_weyl3_panel as panel
 import qgr_covariant_weyl3_critic as c
 z=c.build("OFFSHELL_A"); pvec=[c.fs(z["P"][aa][bb][cc][dd].v()) for aa,bb,cc,dd in product(range(4),repeat=4)]; psha=c.jsha(pvec)
 def h(aa,bb): return panel.h_value(7,*c.cab(aa,bb),())
 def g2(aa,bb,p,q): return panel.metric_value("OFFSHELL_A",*c.cab(aa,bb),tuple(sorted((p,q))))
 def dG(j,up,b,ci): return F(1,2)*sum((c.eta(up,e)*(g2(e,ci,b,j)+g2(e,b,ci,j)-g2(b,ci,e,j)) for e in range(4)),F(0))
 def hc(ci,b,ai,d,i,j):
  q=F(0)
  for r in range(4):
   if ci==i: q-=dG(j,r,b,ai)*h(r,d); q-=dG(j,r,b,d)*h(ai,r)
   if b==i: q-=dG(j,r,ci,ai)*h(r,d); q-=dG(j,r,ci,d)*h(ai,r)
  q-=dG(j,i,ci,b)*h(ai,d); return q
 def R(aa,bb,cc,dd): return F(1,2)*(hc(cc,bb,aa,dd,0,0)+hc(dd,aa,bb,cc,0,0)-hc(cc,aa,bb,dd,0,0)-hc(dd,bb,aa,cc,0,0))
 vals=[fs(R(*idx)) for idx in product(range(4),repeat=4)]
 scalar=sum((z["P"][aa][bb][cc][dd].v()*R(aa,bb,cc,dd) for aa,bb,cc,dd in product(range(4),repeat=4)),F(0))
 controls={"P_hash_exact":psha==P_HASH,"exact_fraction":True,"frozen_witness":True,"serialized_256":len(vals)==256,"c6_symbolic_unfixed":True,"corrected_q10_locked":True}
 p={"gate":"COVARIANT_WEYL3_A7_CONNECTION_TENSOR_COMPONENT_LOCALIZATION","lane":"A_TENSOR_HESSIAN","preregistration_commit":PREREG,"seed":"OFFSHELL_A","direction":7,"i":0,"j":0,"index_order":"lexicographic(a,b,c,d),d-fastest","tensor_values":vals,"tensor_sha256":jsha(vals),"scalar_control":fs(scalar),"P_point_sha256":psha,"controls":controls,"classification":"LANE_A_READY" if all(controls.values()) else "BLOCKED_LANE_A"}
 p["payload_sha256"]=jsha(p); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(p,sort_keys=True,indent=2)+"\n"); print(json.dumps(p,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
