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
def mul_g_h(g,h,scale=1):
    out={}
    for kg,cg in g.items():
        for kh,ch in h.items(): addto(out,kg+"*"+kh,F(scale)*cg*ch)
    return out
def hform(a,b): return {hkey(a,b):F(1)}
def merge(dst,src,scale=1):
    for k,v in src.items(): addto(dst,k,F(scale)*v)
def hc(ci,b,ai,d,i,j):
    out={}
    for r in range(4):
        if ci==i:
            merge(out,mul_g_h(dG(j,r,b,ai),hform(r,d)),-1)
            merge(out,mul_g_h(dG(j,r,b,d),hform(ai,r)),-1)
        if b==i:
            merge(out,mul_g_h(dG(j,r,ci,ai),hform(r,d)),-1)
            merge(out,mul_g_h(dG(j,r,ci,d),hform(ai,r)),-1)
    merge(out,mul_g_h(dG(j,i,ci,b),hform(ai,d)),-1)
    return out
def R(a,b,c,d,malformed=False):
    parts=[hc(c,b,a,d,0,0),hc(d,a,b,c,0,0),hc(c,a,b,d,0,0),hc(d,b,a,c,0,0)]
    signs=[1,1,-1,-1]
    if malformed: signs[0]=-1
    out={}
    for s,p in zip(signs,parts): merge(out,p,F(s,2))
    return out
def serial(m): return [[k,fs(v)] for k,v in sorted(m.items())]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); q=ap.parse_args()
    comps=[]; bad=[]
    for idx in product(range(4),repeat=4):
        comps.append({"index":list(idx),"terms":serial(R(*idx))})
        bad.append({"index":list(idx),"terms":serial(R(*idx,malformed=True))})
    out={"gate":"COVARIANT_WEYL3_A7_CONNECTION_FORMAL_MONOMIAL_IDENTITY_ADJUDICATION","lane":"A_FORMAL_TENSOR_HESSIAN","preregistration_commit":PREREG,"basis":"canonical g2[ab|pq]*h[cd]","component_order":"lexicographic(a,b,c,d),d-fastest","components":comps,"tensor_formal_sha256":jsha(comps),"malformed_control_components":bad,"malformed_control_sha256":jsha(bad),"controls":{"no_panel_data":True,"exact_fraction":True,"all_256_components":len(comps)==256,"malformed_outer0_sign_flipped":True},"classification":"FORMAL_LANE_A_READY"}
    out["payload_sha256"]=jsha(out); Path(q.output).parent.mkdir(parents=True,exist_ok=True); Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n"); print(json.dumps(out,sort_keys=True,indent=2))
if __name__=="__main__": main()
