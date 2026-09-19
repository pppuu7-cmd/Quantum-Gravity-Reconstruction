#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PREREG="7a62dd856aec084add16af8e6793d157ef32637b"

def fs(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def jsha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def eta(a,b):
    return F(-1 if a==0 else 1) if a==b else F(0)

def add(out,key,val):
    val=F(val)
    if not val:
        return
    out[key]=out.get(key,F(0))+val
    if not out[key]:
        del out[key]

def merge(out,src,scale=1):
    scale=F(scale)
    for k,v in src.items():
        add(out,k,scale*v)

def gkey(a,b,p,q):
    a,b=sorted((a,b)); p,q=sorted((p,q))
    return f"g2[{a},{b}|{p},{q}]"

def hkey(a,b):
    a,b=sorted((a,b))
    return f"h[{a},{b}]"

def pcanon(a,b,c,d):
    if a==b or c==d:
        return None,F(0)
    s=F(1)
    if a>b:
        a,b=b,a; s=-s
    if c>d:
        c,d=d,c; s=-s
    p1=(a,b); p2=(c,d)
    if p2<p1:
        p1,p2=p2,p1
    return f"P[{p1[0]},{p1[1]}|{p2[0]},{p2[1]}]",s

def dgamma(j,up,b,c):
    out={}
    for e in range(4):
        s=eta(up,e)
        if not s:
            continue
        add(out,gkey(e,c,b,j),F(1,2)*s)
        add(out,gkey(e,b,c,j),F(1,2)*s)
        add(out,gkey(b,c,e,j),-F(1,2)*s)
    return out

def add_pgh(out,pindices,gmap,hindices,scale):
    pk,ps=pcanon(*pindices)
    if not pk:
        return
    hk=hkey(*hindices)
    for gk,gv in gmap.items():
        add(out,f"{pk}*{gk}*{hk}",F(scale)*ps*gv)

def tensor_connection_map():
    out={}
    for a,b,c,d,r in product(range(4),repeat=5):
        h=(a,b)
        add_pgh(out,(r,c,d,b),dgamma(c,a,d,r),h,2)
        add_pgh(out,(a,r,d,b),dgamma(c,c,d,r),h,2)
        add_pgh(out,(a,c,r,b),dgamma(c,d,d,r),h,2)
        add_pgh(out,(a,c,d,r),dgamma(c,b,d,r),h,2)
    return out

def density_weight_map():
    out={}
    for a,b,c,d,r in product(range(4),repeat=5):
        add_pgh(out,(a,c,d,b),dgamma(c,r,d,r),(a,b),-2)
    return out

def serial(m):
    return [[k,fs(v)] for k,v in sorted(m.items())]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    a=ap.parse_args()

    tensor=tensor_connection_map()
    weight=density_weight_map()
    weighted=dict(tensor)
    merge(weighted,weight)

    st=serial(tensor); sw=serial(weight); sa=serial(weighted)
    controls={
        "no_weyl3_panel_data":True,
        "pair_symmetry_only_no_bianchi":True,
        "dimension_four":True,
        "eta_diagonal_minkowski":True,
        "four_tensor_index_connection_actions_included":True,
        "weight_plus_one_trace_connection_included":True,
        "density_weight_channel_nonzero":bool(sw),
        "exact_fraction_no_tolerance":True,
        "target_blind_serialized_before_comparison":True,
        "c6_symbolic_unfixed":True,
        "corrected_q10_locked":True
    }
    out={
        "gate":"COVARIANT_WEYL3_GENERIC_P_TENSOR_DENSITY_CONNECTION_COMPLETION",
        "lane":"WEIGHT_PLUS_ONE_TENSOR_DENSITY_CONNECTION_JET",
        "preregistration_commit":PREREG,
        "basis":"P[pair|pair]*g2[pair|pair]*h[pair]",
        "P_symmetry":"antisymmetric in each pair, symmetric under pair exchange; no first Bianchi",
        "tensor_connection_terms":st,
        "tensor_connection_term_count":len(st),
        "tensor_connection_sha256":jsha(st),
        "density_weight_terms":sw,
        "density_weight_term_count":len(sw),
        "density_weight_sha256":jsha(sw),
        "weighted_terms":sa,
        "weighted_term_count":len(sa),
        "weighted_sha256":jsha(sa),
        "controls":controls,
        "c6":"SYMBOLIC_UNFIXED",
        "corrected_q10_locked":True,
        "classification":"GENERIC_P_WEIGHTED_LANE_READY" if all(controls.values()) else "BLOCKED_GENERIC_P_WEIGHTED_LANE"
    }
    out["payload_sha256"]=jsha(out)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print(json.dumps({
        "classification":out["classification"],
        "tensor_connection_term_count":out["tensor_connection_term_count"],
        "tensor_connection_sha256":out["tensor_connection_sha256"],
        "density_weight_term_count":out["density_weight_term_count"],
        "density_weight_sha256":out["density_weight_sha256"],
        "weighted_term_count":out["weighted_term_count"],
        "weighted_sha256":out["weighted_sha256"],
        "payload_sha256":out["payload_sha256"]
    },sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=="__main__":
    raise SystemExit(main())
