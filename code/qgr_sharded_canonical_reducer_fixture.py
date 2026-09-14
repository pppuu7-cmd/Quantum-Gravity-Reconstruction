#!/usr/bin/env python3
from __future__ import annotations

import argparse
import glob
import json
import math
from pathlib import Path

GATE="SHARDED-CANONICAL-REDUCER-EQUIVALENCE"
IDENTITY="CANONICAL_REDUCER_FIXTURE_V1"
N=4096
NSHARDS=4


def value(i:int)->float:
    return (-1.0 if i%2 else 1.0)*(i+1)/float((i+17)*(i+17))


def shard(s:int):
    if not 0 <= s < NSHARDS:
        raise ValueError("invalid shard")
    rows=[[i,value(i)] for i in range(N) if i % NSHARDS == s]
    return {"gate":GATE,"mode":"shard","identity":IDENTITY,"nshards":NSHARDS,"shard_id":s,"rows":rows}


def verify(objs):
    if len(objs)!=NSHARDS:
        return False,"SHARD_COUNT"
    if any(o.get("gate")!=GATE or o.get("mode")!="shard" for o in objs):
        return False,"GATE"
    if any(o.get("identity")!=IDENTITY for o in objs):
        return False,"IDENTITY"
    if any(int(o.get("nshards",-1))!=NSHARDS for o in objs):
        return False,"NSHARDS"
    ids=[int(o.get("shard_id",-1)) for o in objs]
    if sorted(ids)!=list(range(NSHARDS)):
        return False,"SHARD_IDS"
    flat=[]
    for o in objs:
        flat.extend(o.get("rows",[]))
    node_ids=[int(r[0]) for r in flat]
    if len(node_ids)!=N:
        return False,"NODE_COUNT"
    if len(set(node_ids))!=N:
        return False,"DUPLICATE"
    if sorted(node_ids)!=list(range(N)):
        return False,"COVERAGE"
    for i,v in flat:
        i=int(i)
        if float(v)!=value(i):
            return False,"VALUE_IDENTITY"
    return True,"OK"


def aggregate(root:str):
    objs=[]
    for fn in glob.glob(str(Path(root)/"**"/"*.json"),recursive=True):
        try:
            o=json.loads(Path(fn).read_text(encoding="utf-8"))
        except Exception:
            continue
        if o.get("gate")==GATE and o.get("mode")=="shard":
            objs.append(o)
    ok,reason=verify(objs)
    sharded_hex=baseline_hex=None
    exact_sum=False
    missing_rejected=duplicate_rejected=mixed_rejected=False
    if ok:
        rows=[]
        for o in objs: rows.extend(o["rows"])
        rows.sort(key=lambda r:int(r[0]))
        ss=math.fsum(float(r[1]) for r in rows)
        bs=math.fsum(value(i) for i in range(N))
        sharded_hex=ss.hex(); baseline_hex=bs.hex(); exact_sum=(sharded_hex==baseline_hex)

        miss=json.loads(json.dumps(objs))
        for o in miss:
            before=len(o["rows"])
            o["rows"]=[r for r in o["rows"] if int(r[0])!=0]
            if len(o["rows"])<before: break
        missing_rejected=not verify(miss)[0]

        dup=json.loads(json.dumps(objs))
        owner=1%NSHARDS
        dup[owner]["rows"].append([1,value(1)])
        duplicate_rejected=not verify(dup)[0]

        mixed=json.loads(json.dumps(objs))
        mixed[0]["identity"]="CORRUPTED_IDENTITY"
        mixed_rejected=not verify(mixed)[0]

    passed=bool(ok and exact_sum and missing_rejected and duplicate_rejected and mixed_rejected)
    return {"gate":GATE,"mode":"aggregate","input_valid":ok,"input_reason":reason,
            "sharded_sum_hex":sharded_hex,"baseline_sum_hex":baseline_hex,
            "exact_binary64_sum_identity":exact_sum,
            "missing_node_negative_control_rejected":missing_rejected,
            "duplicate_node_negative_control_rejected":duplicate_rejected,
            "mixed_identity_negative_control_rejected":mixed_rejected,
            "classification":"SHARDED_CANONICAL_REDUCER_EQUIVALENCE_PASS" if passed else "SHARDED_CANONICAL_REDUCER_EQUIVALENCE_INVALID"}


def write(o,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(o,sort_keys=True))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--mode",choices=["shard","aggregate"],required=True)
    ap.add_argument("--shard",type=int); ap.add_argument("--input-dir"); ap.add_argument("--out",required=True); a=ap.parse_args()
    if a.mode=="shard":
        if a.shard is None: raise SystemExit("shard mode requires --shard")
        o=shard(a.shard)
    else:
        if not a.input_dir: raise SystemExit("aggregate mode requires --input-dir")
        o=aggregate(a.input_dir)
    write(o,a.out)
    if a.mode=="aggregate" and o["classification"]!="SHARDED_CANONICAL_REDUCER_EQUIVALENCE_PASS": raise SystemExit(3)

if __name__=="__main__": main()
