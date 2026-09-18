#!/usr/bin/env python3
"""Neutral exact generator for the prospectively frozen Weyl^3 covariant jet panel.

Authority: preregistration/COVARIANT_WEYL3_DIRECTIONAL_VARIATION_SEED_PANEL_FREEZE.md
This module deliberately contains no curvature, variation, IBP, or Euler-source code so
Researcher/Critic scientific implementations remain independent.
"""
from __future__ import annotations
from fractions import Fraction
from hashlib import sha256
from itertools import combinations_with_replacement
import json

DIM=4
METRIC_ORDERS=range(5)
H_ORDERS=range(3)
SEEDS={"OFFSHELL_A":11,"OFFSHELL_B":23}
DIRECTIONS=(7,19)

def pair_rank(a,b):
    return min(a,b)*4+max(a,b)

def sgn(n):
    return 1 if n%4 in (0,1) else -1

def N(s,a,b,I):
    return (s+3)*17+19*pair_rank(a,b)+sum((j+1)*(I[j]+1)*23 for j in range(len(I)))+29*len(I)+7*(a+1)*(b+1)

def M(d,a,b,I):
    return (d+5)*31+37*pair_rank(a,b)+sum((j+2)*(I[j]+1)*41 for j in range(len(I)))+43*len(I)+5*(a+2)*(b+3)

def metric_value(seed,a,b,I):
    k=len(I)
    if seed=="FLAT_CONTROL":
        if k==0: return Fraction(-1 if a==b==0 else (1 if a==b else 0))
        return Fraction(0)
    if k==0: return Fraction(-1 if a==b==0 else (1 if a==b else 0))
    if k==1: return Fraction(0)
    n=N(SEEDS[seed],a,b,I)
    return Fraction(sgn(n)*(1+n%11),13+((n//11)%17))

def h_value(d,a,b,I):
    m=M(d,a,b,I)
    return Fraction(sgn(m)*(1+m%13),17+((m//13)%19))

def fracstr(x):
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def canonical_table(seed,d):
    g=[]; h=[]
    for k in METRIC_ORDERS:
        for I in combinations_with_replacement(range(DIM),k):
            for a in range(DIM):
                for b in range(a,DIM):
                    g.append([a,b,list(I),fracstr(metric_value(seed,a,b,I))])
    for k in H_ORDERS:
        for I in combinations_with_replacement(range(DIM),k):
            for a in range(DIM):
                for b in range(a,DIM):
                    h.append([a,b,list(I),fracstr(h_value(d,a,b,I))])
    return {"seed":seed,"direction":d,"g":g,"h":h}

def canonical_bytes(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()

def panel_manifest():
    cells=[]
    for seed in ("FLAT_CONTROL","OFFSHELL_A","OFFSHELL_B"):
        for d in DIRECTIONS:
            t=canonical_table(seed,d)
            cells.append({"seed":seed,"direction":d,"jet_sha256":sha256(canonical_bytes(t)).hexdigest(),"g_entries":len(t["g"]),"h_entries":len(t["h"])})
    body={"schema":"QGR_COVARIANT_WEYL3_PANEL_V1","cells":cells}
    body["panel_sha256"]=sha256(canonical_bytes(body)).hexdigest()
    return body

if __name__=="__main__":
    print(json.dumps(panel_manifest(),sort_keys=True,indent=2))
