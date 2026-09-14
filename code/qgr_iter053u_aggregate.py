#!/usr/bin/env python3
"""Frozen aggregate classifier for conditional Iter053U.

Consumes only fresh Iter053U lane artifacts. Historical Iter053R/T/T-GJ lanes
are never pooled into this aggregate.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
from pathlib import Path

GATE="ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION"
EXPECTED={("A",i) for i in range(4)}|{("B",i) for i in range(2)}|{("C",i) for i in range(2)}
PASS="PASS_SCOPED_ITER053U_CORRECTED_SOURCE_FAITHFUL_WEYL3_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE"
FAIL="SCIENTIFIC_FAIL_ITER053U_CORRECTED_SOURCE_FAITHFUL_WEYL3_COMPACT_SUPPORT_ACTION_VARIATION"
INVALID="ITER053U_IMPLEMENTATION_OR_CONTROL_INVALID"
INFRA="ITER053U_NUMERICAL_OR_INFRASTRUCTURE_FAIL"


def aggregate(root):
    rows=[]; errors=[]
    for p in glob.glob(os.path.join(root,"**","*.json"),recursive=True):
        try:
            with open(p,encoding="utf-8") as f: d=json.load(f)
        except Exception as e:
            errors.append({"path":p,"error":repr(e)}); continue
        if d.get("gate")==GATE and d.get("stream") in ("A","B","C") and isinstance(d.get("index"),int):
            rows.append(d)

    keys=[(d["stream"],d["index"]) for d in rows]
    keyset=set(keys)
    missing=sorted(EXPECTED-keyset)
    extra=sorted(keyset-EXPECTED)
    duplicate_keys=sorted(k for k in keyset if keys.count(k)>1)

    valid=[d for d in rows if d.get("control_valid") is True]
    passes=[d for d in rows if d.get("lane_pass") is True]
    Arows=[d for d in rows if d.get("stream")=="A"]
    Brows=[d for d in rows if d.get("stream")=="B"]
    Crows=[d for d in rows if d.get("stream")=="C"]

    wrong_all=bool(len(Arows)==4 and all(
        float(d.get("wrong_sign_relative_residual",-1.0))>
        float(d.get("identity_relative_residual",math.inf)) for d in Arows
    ))
    wrong_strong=bool(any(float(d.get("wrong_sign_relative_residual",0.0))>=1e-2 for d in Arows))

    c_source_ok=bool(len(Crows)==2 and all(
        d.get("transformed_source_object_control",{}).get("control_pass") is True and
        d.get("transformed",{}).get("weighted_source_path")=="CORRECTED_SOURCE_FAITHFUL_SINGLE_WEIGHT" and
        d.get("scientific_change_scope")=="ONLY_TRANSFORMED_WEIGHTED_POLYNOMIAL_SOURCE_EXTRACTION"
        for d in Crows
    ))

    complete=bool(not errors and not missing and not extra and not duplicate_keys and len(rows)==8)
    if not complete:
        cls=INFRA
    elif len(valid)!=8 or not c_source_ok:
        cls=INVALID
    elif len(passes)==8 and wrong_all and wrong_strong:
        cls=PASS
    else:
        cls=FAIL

    out={
        "gate":GATE,"classification":cls,"expected_lanes":8,"found_lanes":len(rows),
        "valid_lanes":len(valid),"passes":len(passes),"missing":missing,"extra":extra,
        "duplicate_keys":duplicate_keys,"parse_errors":errors,
        "wrong_sign_control_all_weaker_than_correct":wrong_all,
        "wrong_sign_control_at_least_one_ge_1e-2":wrong_strong,
        "corrected_C_source_object_controls_pass":c_source_ok,
        "stream_counts":{s:sum(1 for d in rows if d.get("stream")==s) for s in ("A","B","C")},
        "historical_iter053r_reclassification_allowed":False,
        "evidence_pooling_from_iter053r_t_tgj_allowed":False,
        "interpretation_lock":"FINITE GENUINELY-4D COMPACT-SUPPORT COMPUTATIONAL CERTIFICATE ONLY; C6 SYMBOLIC UNFIXED; NO GLOBAL FUNCTIONAL-DERIVATIVE THEOREM; THEORY_ESTABLISHED_0",
    }
    if Arows:
        out["worst_A_identity_relative_residual"]=max(float(d.get("identity_relative_residual",math.inf)) for d in Arows)
        out["worst_A_direct_step_change"]=max(float(d.get("direct_final_step_change",math.inf)) for d in Arows)
        out["worst_A_GL7_to_GL8_change"]=max(float(d.get("direct_GL7_to_GL8_relative_change",math.inf)) for d in Arows)
        out["worst_A_weighted_bulk_GJ2_to_GJ3_change"]=max(float(d.get("weighted_bulk_GJ2_to_GJ3_relative_change",math.inf)) for d in Arows)
        out["worst_A_identity_residual_change"]=max(float(d.get("coarse_to_fine_identity_residual_change_abs",math.inf)) for d in Arows)
        out["min_A_wrong_sign_relative_residual"]=min(float(d.get("wrong_sign_relative_residual",-math.inf)) for d in Arows)
    if Brows:
        out["worst_B_abs_direct_GL8"]=max(abs(float(d["direct_GL8"]["direct"][-1])) for d in Brows)
        out["worst_B_abs_bulk_GJ3"]=max(abs(float(d["GJ3"]["bulk"])) for d in Brows)
    if Crows:
        out["worst_C_direct_covariance_relative_residual"]=max(float(d.get("direct_covariance_relative_residual",math.inf)) for d in Crows)
        out["worst_C_bulk_covariance_relative_residual"]=max(float(d.get("bulk_covariance_relative_residual",math.inf)) for d in Crows)
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input-dir",required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
    out=aggregate(a.input_dir)
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    if out["classification"]==INFRA: raise SystemExit(4)
    if out["classification"]==INVALID: raise SystemExit(3)
    if out["classification"]==FAIL: raise SystemExit(2)

if __name__=="__main__": main()
