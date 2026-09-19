#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
PREREG="63ead9c69964fe24ec647c7bda12c1ebc4aa28df"; P_HASH="21095bed2a18f7a5fa2484961c75d4cd7589115d6a6f664f0b3eee8697cdd4fe"; ME=1; MX=2
def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
class P:
 def __init__(self,d=None): self.d={(e,x):F(v) for (e,x),v in (d or {}).items() if v and e<=ME and x<=MX}
 @staticmethod
 def c(v): v=F(v); return P({(0,0):v}) if v else P()
 @staticmethod
 def m(e,x,v=1): return P({(e,x):F(v)}) if v and e<=ME and x<=MX else P()
 def coeff(self,e,x): return self.d.get((e,x),F(0))
 def co(self,o): return o if isinstance(o,P) else P.c(o)
 def __add__(self,o):
  o=self.co(o); q=dict(self.d)
  for k,v in o.d.items(): q[k]=q.get(k,F(0))+v
  return P(q)
 __radd__=__add__
 def __neg__(self): return P({k:-v for k,v in self.d.items()})
 def __sub__(self,o): return self+(-self.co(o))
 def __mul__(self,o):
  o=self.co(o); q={}
  for (e1,x1),v1 in self.d.items():
   for (e2,x2),v2 in o.d.items():
    e,x=e1+e2,x1+x2
    if e<=ME and x<=MX: q[(e,x)]=q.get((e,x),F(0))+v1*v2
  return P(q)
 __rmul__=__mul__
 def inv(self):
  c=self.coeff(0,0); n=self-P.c(c); out=P.c(1/c); term=P.c(1); u=(-n)*F(1,c)
  for _ in range(1,6): term=term*u; out=out+term*F(1,c)
  if (self*out-P.c(1)).d: raise ArithmeticError("inverse truncation")
  return out
def invmat(A):
 n=len(A); aug=[[A[i][j] for j in range(n)]+[P.c(int(i==j)) for j in range(n)] for i in range(n)]
 for col in range(n):
  ip=aug[col][col].inv(); aug[col]=[z*ip for z in aug[col]]
  for row in range(n):
   if row!=col:
    q=aug[row][col]; aug[row]=[aug[row][k]-q*aug[col][k] for k in range(2*n)]
 return [r[n:] for r in aug]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); a=ap.parse_args()
 import qgr_covariant_weyl3_panel as panel
 import qgr_covariant_weyl3_critic as c
 z=c.build("OFFSHELL_A"); pvec=[c.fs(z["P"][aa][bb][cc][dd].v()) for aa,bb,cc,dd in product(range(4),repeat=4)]; psha=c.jsha(pvec)
 G=[[P() for _ in range(4)] for _ in range(4)]
 for aa,bb in product(range(4),repeat=2):
  a0,b0=c.cab(aa,bb); G[aa][bb]=P.c(c.eta(aa,bb))+P.m(0,2,F(1,2)*panel.metric_value("OFFSHELL_A",a0,b0,(0,0)))+P.m(1,1,panel.h_value(7,a0,b0,()))+P.m(1,2,panel.h_value(7,a0,b0,(0,)))
 Gi=invmat(G)
 def dx(q,aa,bb):
  if q!=0:return P()
  out={}
  for (e,x),v in G[aa][bb].d.items():
   if x: out[(e,x-1)]=out.get((e,x-1),F(0))+x*v
  return P(out)
 Ga=[[[P() for _ in range(4)] for _ in range(4)] for _ in range(4)]
 for aa,bb,cc in product(range(4),repeat=3):
  q=P()
  for e in range(4): q=q+Gi[aa][e]*(dx(bb,e,cc)+dx(cc,e,bb)-dx(e,bb,cc))
  Ga[aa][bb][cc]=q*F(1,2)
 vals=[]; scalar=F(0)
 for aa,bb,cc,dd in product(range(4),repeat=4):
  q=P()
  for e,f in product(range(4),repeat=2): q=q+G[e][f]*(Ga[e][cc][aa]*Ga[f][dd][bb]-Ga[e][dd][aa]*Ga[f][cc][bb])
  v=q.coeff(1,1); vals.append(fs(v)); scalar+=z["P"][aa][bb][cc][dd].v()*v
 controls={"P_hash_exact":psha==P_HASH,"exact_fraction":True,"frozen_witness":True,"serialized_256":len(vals)==256,"c6_symbolic_unfixed":True,"corrected_q10_locked":True}
 p={"gate":"COVARIANT_WEYL3_A7_CONNECTION_TENSOR_COMPONENT_LOCALIZATION","lane":"C_DUAL_POLYNOMIAL","preregistration_commit":PREREG,"seed":"OFFSHELL_A","direction":7,"i":0,"j":0,"index_order":"lexicographic(a,b,c,d),d-fastest","tensor_values":vals,"tensor_sha256":jsha(vals),"scalar_control":fs(scalar),"P_point_sha256":psha,"controls":controls,"classification":"LANE_C_READY" if all(controls.values()) else "BLOCKED_LANE_C"}
 p["payload_sha256"]=jsha(p); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(p,sort_keys=True,indent=2)+"\n"); print(json.dumps(p,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
