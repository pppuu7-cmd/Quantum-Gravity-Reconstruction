#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="bbb4e90e46ddd1aded691a1d780e10dbe0313e51"

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def eta(a,b):
    if a!=b:return F(0)
    return F(-1 if a==0 else 1)
def addto(out,key,val):
    val=F(val)
    if val: out[key]=out.get(key,F(0))+val
    if key in out and not out[key]: del out[key]
def gkey(a,b,p,q):
    a,b=sorted((a,b)); p,q=sorted((p,q)); return f"g2[{a},{b}|{p},{q}]"
def hkey(a,b):
    a,b=sorted((a,b)); return f"h[{a},{b}]"
def dG(j,up,b,ci):
    out={}
    for e in range(4):
        s=eta(up,e)
        if not s: continue
        addto(out,gkey(e,ci,b,j),F(1,2)*s)
        addto(out,gkey(e,b,ci,j),F(1,2)*s)
        addto(out,gkey(b,ci,e,j),-F(1,2)*s)
    return out
def dphi(i,up,b,ci):
    out={}
    for e in range(4):
        s=eta(up,e)
        if not s: continue
        if b==i: addto(out,hkey(e,ci),F(1,2)*s)
        if ci==i: addto(out,hkey(e,b),F(1,2)*s)
        if e==i: addto(out,hkey(b,ci),-F(1,2)*s)
    return out
def mul(h,g,scale=1):
    out={}
    for kh,ch in h.items():
        for kg,cg in g.items(): addto(out,kg+"*"+kh,F(scale)*ch*cg)
    return out
def merge(dst,src,scale=1):
    for k,v in src.items(): addto(dst,k,F(scale)*v)
def R(a,b,c,d):
    out={}
    for e,f in product(range(4),repeat=2):
        ef=eta(e,f)
        if not ef: continue
        merge(out,mul(dphi(0,e,c,a),dG(0,f,d,b)),ef)
        merge(out,mul(dphi(0,f,d,b),dG(0,e,c,a)),ef)
        merge(out,mul(dphi(0,e,d,a),dG(0,f,c,b)),-ef)
        merge(out,mul(dphi(0,f,c,b),dG(0,e,d,a)),-ef)
    return out
def serial(m): return [[k,fs(v)] for k,v in sorted(m.items())]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); q=ap.parse_args()
    comps=[{"index":list(idx),"terms":serial(R(*idx))} for idx in product(range(4),repeat=4)]
    out={"gate":"COVARIANT_WEYL3_A7_CONNECTION_FORMAL_MONOMIAL_IDENTITY_ADJUDICATION","lane":"B_FORMAL_GAMMAGAMMA","preregistration_commit":PREREG,"basis":"canonical g2[ab|pq]*h[cd]","component_order":"lexicographic(a,b,c,d),d-fastest","components":comps,"tensor_formal_sha256":jsha(comps),"controls":{"no_panel_data":True,"exact_fraction":True,"all_256_components":len(comps)==256},"classification":"FORMAL_LANE_B_READY"}
    out["payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2))
if __name__=="__main__": main()
