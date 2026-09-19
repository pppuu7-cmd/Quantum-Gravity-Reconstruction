#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
PREREG="7b9d2ffb84993f04e467c0a9ea6bf650327f6b62"; ME=1; MX=2
CLASSES=["FREE_INDEX_PLACEMENT","METRIC_INVERSE_METRIC_CONTRACTIONS","CONNECTION_FACTOR_CHANNELS","HESSIAN_CHANNELS","GAMMAGAMMA_DUMMY_CHANNELS","DUAL_POLYNOMIAL_CHANNELS","PERMUTATION_ANTISYMMETRY_FACTORS","FINAL_COMPONENT_SUM"]
def fs(x):
 x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def add(ledger,cls,key,val):
 val=F(val)
 if val: ledger[cls].append({"key":key,"value":fs(val)})
class P:
 def __init__(self,d=None): self.d={(int(e),int(x)):F(v) for (e,x),v in (d or {}).items() if v and e<=ME and x<=MX}
 @staticmethod
 def c(v): v=F(v); return P({(0,0):v}) if v else P()
 @staticmethod
 def m(e,x,v=1): v=F(v); return P({(e,x):v}) if v and e<=ME and x<=MX else P()
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
  c=self.coeff(0,0)
  if not c: raise ZeroDivisionError("nonunit pivot")
  n=self-P.c(c); out=P.c(1/c); term=P.c(1); u=(-n)*F(1,c)
  for _ in range(1,6):
   term=term*u
   if not term.d: break
   out=out+term*F(1,c)
  if (self*out-P.c(1)).d: raise ArithmeticError("inverse truncation failed")
  return out
 def dx(self):
  q={}
  for (e,x),v in self.d.items():
   if x: q[(e,x-1)]=q.get((e,x-1),F(0))+x*v
  return P(q)
def invmat(A):
 n=len(A); aug=[[A[i][j] for j in range(n)]+[P.c(int(i==j)) for j in range(n)] for i in range(n)]
 for col in range(n):
  ip=aug[col][col].inv(); aug[col]=[z*ip for z in aug[col]]
  for row in range(n):
   if row==col: continue
   q=aug[row][col]; aug[row]=[aug[row][k]-q*aug[col][k] for k in range(2*n)]
 return [r[n:] for r in aug]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); q=ap.parse_args()
 import qgr_covariant_weyl3_panel as panel
 import qgr_covariant_weyl3_critic as c
 z=c.build("OFFSHELL_A"); ledger={k:[] for k in CLASSES}
 G=[[P() for _ in range(4)] for _ in range(4)]
 for a,b in product(range(4),repeat=2):
  a0,b0=c.cab(a,b)
  G[a][b]=P.c(c.eta(a,b))+P.m(0,2,F(1,2)*panel.metric_value("OFFSHELL_A",a0,b0,(0,0)))+P.m(1,1,panel.h_value(7,a0,b0,()))+P.m(1,2,panel.h_value(7,a0,b0,(0,)))
 Gi=invmat(G)
 inverse_exact=all(not (sum((G[a][r]*Gi[r][b] for r in range(4)),P())-P.c(int(a==b))).d for a,b in product(range(4),repeat=2))
 def partial(coord,a,b): return G[a][b].dx() if coord==0 else P()
 Ga=[[[P() for _ in range(4)] for _ in range(4)] for _ in range(4)]
 for up,b,ci in product(range(4),repeat=3):
  s=P()
  for e in range(4): s=s+Gi[up][e]*(partial(b,e,ci)+partial(ci,e,b)-partial(e,b,ci))
  Ga[up][b][ci]=s*F(1,2)
 def R(a,b,cc,d):
  s=P()
  for e,f in product(range(4),repeat=2): s=s+G[e][f]*(Ga[e][cc][a]*Ga[f][d][b]-Ga[e][d][a]*Ga[f][cc][b])
  return s.coeff(1,1)
 vals=[fs(R(*idx)) for idx in product(range(4),repeat=4)]
 scalar=sum((z["P"][a][b][cc][d].v()*R(a,b,cc,d) for a,b,cc,d in product(range(4),repeat=4)),F(0))
 add(ledger,"FREE_INDEX_PLACEMENT","free:0,1,0,1",1)
 for a,b in product(range(4),repeat=2):
  add(ledger,"METRIC_INVERSE_METRIC_CONTRACTIONS",f"metric_base:{a},{b}",G[a][b].coeff(0,0))
  add(ledger,"METRIC_INVERSE_METRIC_CONTRACTIONS",f"inverse_base:{a},{b}",Gi[a][b].coeff(0,0))
  add(ledger,"METRIC_INVERSE_METRIC_CONTRACTIONS",f"h:{a},{b}",G[a][b].coeff(1,1))
 for up,b,ci in product(range(4),repeat=3):
  add(ledger,"CONNECTION_FACTOR_CHANNELS",f"dGamma:0,{up},{b},{ci}",Ga[up][b][ci].coeff(0,1))
  add(ledger,"CONNECTION_FACTOR_CHANNELS",f"deltaGamma:0,{up},{b},{ci}",Ga[up][b][ci].coeff(1,0))
 a,b,cc,d=0,1,0,1
 signs=[1,1,-1,-1]
 for e,f in product(range(4),repeat=2):
  g0=G[e][f].coeff(0,0)
  terms=[Ga[e][cc][a].coeff(1,0)*Ga[f][d][b].coeff(0,1),Ga[e][cc][a].coeff(0,1)*Ga[f][d][b].coeff(1,0),Ga[e][d][a].coeff(1,0)*Ga[f][cc][b].coeff(0,1),Ga[e][d][a].coeff(0,1)*Ga[f][cc][b].coeff(1,0)]
  for ti,(sgn,v) in enumerate(zip(signs,terms)): add(ledger,"GAMMAGAMMA_DUMMY_CHANNELS",f"e{e}:f{f}:term{ti}",g0*sgn*v)
  pairs=[(1,Ga[e][cc][a],Ga[f][d][b],"prod0"),(-1,Ga[e][d][a],Ga[f][cc][b],"prod1")]
  for sgn,p1,p2,label in pairs:
   for (eg,xg),vg in sorted(G[e][f].d.items()):
    for (e1,x1),v1 in sorted(p1.d.items()):
     for (e2,x2),v2 in sorted(p2.d.items()):
      if eg+e1+e2==1 and xg+x1+x2==1:
       key=f"e{e}:f{f}:{label}:g{eg},{xg}:p{e1},{x1}:q{e2},{x2}"
       add(ledger,"DUAL_POLYNOMIAL_CHANNELS",key,sgn*vg*v1*v2)
 for ti,sgn in enumerate(signs): add(ledger,"PERMUTATION_ANTISYMMETRY_FACTORS",f"term{ti}",sgn)
 comp=R(0,1,0,1); add(ledger,"FINAL_COMPONENT_SUM","component:0,1,0,1",comp)
 for k in CLASSES: ledger[k]=sorted(ledger[k],key=lambda x:x["key"])
 gamma_sum=sum((F(x["value"]) for x in ledger["GAMMAGAMMA_DUMMY_CHANNELS"]),F(0))
 dual_sum=sum((F(x["value"]) for x in ledger["DUAL_POLYNOMIAL_CHANNELS"]),F(0))
 controls={"exact_fraction":True,"frozen_component":True,"serialized_before_comparison":True,"polynomial_inverse_exact":inverse_exact,"Gamma_point_zero":all(Ga[up][b][ci].coeff(0,0)==0 for up,b,ci in product(range(4),repeat=3)),"full_tensor_256":len(vals)==256,"gammagamma_cross_sum_equals_component":gamma_sum==comp,"dual_polynomial_sum_equals_component":dual_sum==comp}
 out={"gate":"COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION","lane":"C_DUAL_POLYNOMIAL","preregistration_commit":PREREG,"seed":"OFFSHELL_A","direction":7,"i":0,"j":0,"component":[0,1,0,1],"classes":ledger,"full_tensor_sha256":jsha(vals),"scalar_control":fs(scalar),"component_value":fs(comp),"controls":controls,"classification":"LANE_C_PRIMITIVE_LEDGER_READY" if all(controls.values()) else "BLOCKED_LANE_C"}
 out["payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2)); return 0 if all(controls.values()) else 2
if __name__=="__main__": raise SystemExit(main())
