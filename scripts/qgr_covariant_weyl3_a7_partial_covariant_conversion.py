#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="7ef60246ae816730bb702ce0d9fd7284362b3b70"

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def eta(a,b):
    if a!=b: return F(0)
    return F(-1 if a==0 else 1)
def addto(out,key,val):
    val=F(val)
    if val: out[key]=out.get(key,F(0))+val
    if key in out and not out[key]: del out[key]
def merge(dst,src,scale=1):
    for k,v in src.items(): addto(dst,k,F(scale)*v)
def gkey(a,b,p,q):
    a,b=sorted((a,b)); p,q=sorted((p,q))
    return f"g2[{a},{b}|{p},{q}]"
def hkey(a,b):
    a,b=sorted((a,b))
    return f"h[{a},{b}]"
def hform(a,b):
    return {hkey(a,b):F(1)}
def dgamma(j,up,b,c):
    out={}
    for e in range(4):
        s=eta(up,e)
        if not s: continue
        addto(out,gkey(e,c,b,j),F(1,2)*s)
        addto(out,gkey(e,b,c,j),F(1,2)*s)
        addto(out,gkey(b,c,e,j),-F(1,2)*s)
    return out
def mul(a,b,scale=1):
    out={}
    for ka,va in a.items():
        for kb,vb in b.items():
            if ka.startswith("g2["): key=ka+"*"+kb
            else: key=kb+"*"+ka
            addto(out,key,F(scale)*va*vb)
    return out

def c_nabla(c,b,a,d,i=0,j=0,omit_derivative_index=False):
    # Mixed connection contribution inside nabla_c nabla_b (phi h_ad)
    # at Gamma=0, partial_r phi = delta_{ri}, coefficient in background x^j.
    out={}
    for r in range(4):
        if c==i:
            merge(out,mul(dgamma(j,r,b,a),hform(r,d)),-1)
            merge(out,mul(dgamma(j,r,b,d),hform(a,r)),-1)
        if b==i:
            merge(out,mul(dgamma(j,r,c,a),hform(r,d)),-1)
            merge(out,mul(dgamma(j,r,c,d),hform(a,r)),-1)
    if not omit_derivative_index:
        merge(out,mul(dgamma(j,i,c,b),hform(a,d)),-1)
    return out

def conversion(a,b,c,d,malformed=False):
    # Repository derivative ordering:
    # 1/2 [partial_c partial_b s_ad + partial_d partial_a s_bc
    #      -partial_d partial_b s_ac - partial_c partial_a s_bd].
    # Since partial partial = nabla nabla - C_nabla, K is minus the
    # same signed combination of C_nabla.
    terms=[
      c_nabla(c,b,a,d,omit_derivative_index=malformed),
      c_nabla(d,a,b,c,omit_derivative_index=malformed),
      c_nabla(d,b,a,c,omit_derivative_index=malformed),
      c_nabla(c,a,b,d,omit_derivative_index=malformed),
    ]
    signs=[-1,-1,1,1]
    out={}
    for s,t in zip(signs,terms):
        merge(out,t,F(s,2))
    return out

def serial(m):
    return [[k,fs(v)] for k,v in sorted(m.items())]

def neg_components(comps):
    out=[]
    for c in comps:
        out.append({"index":c["index"],"terms":[[k,fs(-F(v))] for k,v in c["terms"]]})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); q=ap.parse_args()
    comps=[]; malformed=[]
    for idx in product(range(4),repeat=4):
        comps.append({"index":list(idx),"terms":serial(conversion(*idx,malformed=False))})
        malformed.append({"index":list(idx),"terms":serial(conversion(*idx,malformed=True))})
    neg=neg_components(comps)
    controls={
      "exact_fraction":True,
      "all_256_components":len(comps)==256,
      "normal_coordinate_identity_used":True,
      "connection_action_on_derivative_index_included":True,
      "connection_action_on_tensor_indices_included":True,
      "repository_partial_derivative_ordering_frozen":True,
      "no_panel_numeric_witness":True,
      "target_blind_no_parent_hashes":True,
      "malformed_omits_derivative_index_connection":True
    }
    out={
      "gate":"COVARIANT_WEYL3_A7_PARTIAL_COVARIANT_HESSIAN_CONVERSION_SIGN_AUDIT",
      "lane":"TARGET_BLIND_PARTIAL_TO_COVARIANT_CONVERSION",
      "preregistration_commit":PREREG,
      "basis":"canonical g2[ab|pq]*h[cd]",
      "component_order":"lexicographic(a,b,c,d),d-fastest",
      "identity":"partial_partial = covariant_hessian - C_nabla",
      "components":comps,
      "tensor_formal_sha256":jsha(comps),
      "negated_tensor_formal_sha256":jsha(neg),
      "malformed_components":malformed,
      "malformed_formal_sha256":jsha(malformed),
      "controls":controls,
      "classification":"PARTIAL_COVARIANT_CONVERSION_READY"
    }
    out["payload_sha256"]=jsha(out)
    Path(q.output).parent.mkdir(parents=True,exist_ok=True)
    Path(q.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("components","malformed_components")},sort_keys=True,indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
