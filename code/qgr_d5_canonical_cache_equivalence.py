#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path

import numpy as np

import qgr_iter053r_weighted_h5_compact_support as r
import qgr_iter051c_d2n_near_null as d2n
import qgr_iter051c_full_eom as c
import qgr_iter051b0_double_divergence_operator as b0
import qgr_iter051b1_weyl3_p_insertion as w3

GATE="D5-CANONICAL-CACHE-EQUIVALENCE"
H=5.0e-4
N=4
POINTS={
    0: np.zeros(4,dtype=float),
    1: np.array([0.04,-0.03,0.025,-0.02],dtype=float),
}


def relmat(a,b,floor=1e-30):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(a),np.linalg.norm(b),floor))


def add(q,axis,k):
    z=list(q); z[axis]+=int(k); return tuple(z)


def required_offsets():
    zero=(0,0,0,0)
    centers=[zero]
    for bb in range(N):
        for ko in (-2,-1,1,2):
            centers.append(add(zero,bb,ko))
    offsets=set(centers)
    for q in centers:
        for aa in range(N):
            for ki in (-2,-1,1,2):
                offsets.add(add(q,aa,ki))
    return tuple(sorted(offsets))


def build_cache(metric,x,h):
    offsets=required_offsets()
    cache={}
    for q in offsets:
        xx=np.asarray(x,float)+h*np.asarray(q,float)
        g,dg,ddg,gi,G,R=c.geometry(metric,xx)
        P=w3.project_algebraic_riemann(w3.complex_step_gradient(R,g,gi))
        cache[q]={"g":g,"gi":gi,"G":G,"R":R,"P":P}
    return cache


def first_div_cached(cache,q,h,p_override=None):
    data=cache[q]
    P0=data["P"] if p_override is None else p_override[q]
    dP=np.empty((N,N,N,N,N))
    for aa in range(N):
        def P(k):
            qq=add(q,aa,k)
            return cache[qq]["P"] if p_override is None else p_override[qq]
        dP[aa]=(-P(2)+8.0*P(1)-8.0*P(-1)+P(-2))/(12.0*h)
    S=b0.first_cov(P0,dP,data["G"])
    return np.einsum('aambn->mbn',S)


def reduce_cache(cache,h,p_override=None):
    zero=(0,0,0,0)
    center=cache[zero]
    R0=first_div_cached(cache,zero,h,p_override)
    D=np.zeros((N,N))
    G=center["G"]
    for bb in range(N):
        def RR(k): return first_div_cached(cache,add(zero,bb,k),h,p_override)
        dR=(-RR(2)+8.0*RR(1)-8.0*RR(-1)+RR(-2))/(12.0*h)
        D += dR[:,bb,:]
        for m in range(N):
            for n in range(N):
                for rr in range(N):
                    D[m,n]+=G[m,bb,rr]*R0[rr,bb,n]+G[bb,bb,rr]*R0[m,rr,n]+G[n,bb,rr]*R0[m,bb,rr]
    g=center["g"]; R=center["R"]
    P=center["P"] if p_override is None else p_override[zero]
    A=c.algebraic_A(R,g)
    I=c.lowering_insertion(R,g,P)
    sg=math.sqrt(-float(np.linalg.det(g)))
    Hout=A+I-2.0*sg*D
    return Hout,{"g":g,"R":R,"P":P,"A":A,"I":I,"D":D}


def lane(stream,index,point_id):
    metric,_,mseed,_=r.lane_objects(stream,index)
    x=POINTS[point_id].copy()
    sig,inv,_=d2n.extended_controls(metric,x)
    Hhist,zhist=d2n.assemble_minus5(metric,x,H)
    cache=build_cache(metric,x,H)
    Hcache,zcache=reduce_cache(cache,H)

    dres=relmat(zcache["D"],zhist["D"])
    hres=relmat(Hcache,Hhist)
    ares=relmat(zcache["A"],zhist["A"])
    ires=relmat(zcache["I"],zhist["I"])
    pres=relmat(zcache["P"],zhist["P"])

    pbad={q:v["P"].copy() for q,v in cache.items()}
    corrupt=(2,0,0,0)
    pbad[corrupt]*=1.01
    Hbad,zbad=reduce_cache(cache,H,pbad)
    bad_d=relmat(zbad["D"],zcache["D"])
    bad_h=relmat(Hbad,Hcache)
    negative=bool(max(bad_d,bad_h)>=1e-6)

    nums=[dres,hres,ares,ires,pres,bad_d,bad_h,inv,*Hhist.ravel(),*Hcache.ravel()]
    finite=bool(np.isfinite(nums).all())
    offset_count=len(cache)
    unique_offsets=(offset_count==len(set(cache)))
    valid=bool(sig and inv<=3e-11 and finite and offset_count==129 and unique_offsets and (0,0,0,0) in cache)
    passed=bool(valid and dres<=1e-9 and hres<=1e-9 and ares<=1e-13 and ires<=1e-13 and pres<=1e-13 and negative)
    return {
        "gate":GATE,"stream":stream,"index":index,"point_id":point_id,"point":x.tolist(),
        "metric_seed":mseed,"h":H,"cached_unique_P_evaluation_count":offset_count,
        "signature_valid":bool(sig),"max_inverse_residual":float(inv),"finite":finite,
        "D_relative_residual":dres,"H_relative_residual":hres,
        "A_relative_residual":ares,"I_relative_residual":ires,"P_relative_residual":pres,
        "corrupted_D_relative_difference":bad_d,"corrupted_H_relative_difference":bad_h,
        "negative_control_pass":negative,"control_valid":valid,"lane_pass":passed,
        "claim_lock":"Implementation equivalence only; no QGR scientific authority."
    }


def aggregate(root):
    rows=[]
    for p in Path(root).rglob("*.json"):
        try: o=json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        if o.get("gate")==GATE and o.get("mode")!="aggregate": rows.append(o)
    expected={("A",i,p) for i in range(4) for p in range(2)}|{("B",i,p) for i in range(2) for p in range(2)}|{("C",i,p) for i in range(2) for p in range(2)}
    keys={(o.get("stream"),o.get("index"),o.get("point_id")) for o in rows}
    complete=(len(rows)==16 and keys==expected)
    valid=bool(complete and all(o.get("control_valid") is True for o in rows))
    passed=bool(valid and all(o.get("lane_pass") is True for o in rows))
    return {
        "gate":GATE,"mode":"aggregate","expected_lanes":16,"found_lanes":len(rows),
        "complete":complete,"all_valid":valid,"all_pass":passed,
        "worst_D_relative_residual":max((float(o.get("D_relative_residual",math.inf)) for o in rows),default=None),
        "worst_H_relative_residual":max((float(o.get("H_relative_residual",math.inf)) for o in rows),default=None),
        "minimum_negative_control_difference":min((max(float(o.get("corrupted_D_relative_difference",0)),float(o.get("corrupted_H_relative_difference",0))) for o in rows),default=None),
        "classification":"D5_CANONICAL_CACHE_EQUIVALENCE_PASS" if passed else "D5_CANONICAL_CACHE_EQUIVALENCE_INVALID",
        "claim_lock":"Implementation equivalence only; no active or future scientific gate is classified by this result."
    }


def write(o,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(o,sort_keys=True))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["lane","aggregate"],required=True)
    ap.add_argument("--stream",choices=["A","B","C"])
    ap.add_argument("--index",type=int)
    ap.add_argument("--point",type=int)
    ap.add_argument("--input-dir")
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    if a.mode=="lane":
        if a.stream is None or a.index is None or a.point not in POINTS: raise SystemExit("lane args invalid")
        lim={"A":4,"B":2,"C":2}[a.stream]
        if not 0<=a.index<lim: raise SystemExit("lane index invalid")
        o=lane(a.stream,a.index,a.point)
    else:
        if not a.input_dir: raise SystemExit("aggregate requires --input-dir")
        o=aggregate(a.input_dir)
    write(o,a.out)
    if a.mode=="lane" and not o["control_valid"]: raise SystemExit(3)
    if a.mode=="lane" and not o["lane_pass"]: raise SystemExit(2)
    if a.mode=="aggregate" and o["classification"]!="D5_CANONICAL_CACHE_EQUIVALENCE_PASS": raise SystemExit(3)

if __name__=="__main__": main()
