#!/usr/bin/env python3
from __future__ import annotations

import argparse, glob, json, os
from fractions import Fraction
from pathlib import Path
import numpy as np

import qgr_iter053t_orthogonal_controls as b

GATE="ITER053T-ORTHOGONAL-CONTROLS-R1-NONAUTHORITATIVE"
MODES=("stencil","weight","wrapper","tensor")


def retag(obj, mode):
    out=dict(obj); out["gate"]=GATE; out["mode"]=mode; return out


def weight_control():
    s2=b.weight_scalar(2); s3=b.weight_scalar(3); drift=b.rel(s2,s3)
    ref2=float(Fraction(10000000000000000,45949729863572161))
    ref3=float(Fraction(104510217024160000,341107264278244321))
    refd=float(Fraction(593856122131774300241121,2049986442286836800241121))
    e2=abs(s2-ref2); e3=abs(s3-ref3); ed=abs(drift-refd)
    finite=bool(np.isfinite([s2,s3,drift,ref2,ref3,refd,e2,e3,ed]).all())
    passed=bool(finite and max(e2,e3,ed)<=5e-13)
    return {"gate":GATE,"mode":"weight","GJ2_extra_weight_suppression":s2,
            "GJ3_extra_weight_suppression":s3,"GJ2_to_GJ3_relative_drift":drift,
            "exact_reference_GJ2":ref2,"exact_reference_GJ3":ref3,"exact_reference_drift":refd,
            "GJ2_reference_abs_error":e2,"GJ3_reference_abs_error":e3,
            "drift_reference_abs_error":ed,"finite":finite,"pass":passed}


def aggregate(root):
    rows=[]
    for fn in glob.glob(os.path.join(root,"**","*.json"),recursive=True):
        try:
            with open(fn,encoding="utf-8") as f: o=json.load(f)
        except Exception: continue
        if o.get("gate")==GATE and o.get("mode") in MODES: rows.append(o)
    by={o["mode"]:o for o in rows}
    complete=set(by)==set(MODES)
    passed=bool(complete and all(bool(by[m].get("pass")) for m in MODES))
    return {"gate":GATE,"mode":"aggregate","complete":complete,"modes_found":sorted(by),
            "all_controls_pass":passed,
            "classification":"ORTHOGONAL_CONTROLS_R1_PASS" if passed else "ORTHOGONAL_CONTROLS_R1_INVALID",
            "claim_lock":"Non-authoritative exact-reference retry only; no Iter053T scientific classification or evidence pooling."}


def write(o,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(o,sort_keys=True))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--mode",choices=MODES+("aggregate",),required=True)
    ap.add_argument("--input-dir"); ap.add_argument("--out",required=True); a=ap.parse_args()
    if a.mode=="stencil": out=retag(b.stencil_control(),"stencil")
    elif a.mode=="weight": out=weight_control()
    elif a.mode=="wrapper": out=retag(b.wrapper_control(),"wrapper")
    elif a.mode=="tensor": out=retag(b.tensor_control(),"tensor")
    else:
        if not a.input_dir: raise SystemExit("aggregate requires --input-dir")
        out=aggregate(a.input_dir)
    write(out,a.out)
    if a.mode!="aggregate" and not out["pass"]: raise SystemExit(2)
    if a.mode=="aggregate" and out["classification"]!="ORTHOGONAL_CONTROLS_R1_PASS": raise SystemExit(3)

if __name__=="__main__": main()
