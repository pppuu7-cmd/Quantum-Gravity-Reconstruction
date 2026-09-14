#!/usr/bin/env python3
"""Final cached dispatcher for the guarded 20-part conditional Iter053U graph.

Direct parts and all lane reducers are imported unchanged from the provenance-
hardened v1 kernel. Weighted parts use the separately validated h=5e-4 D5/H5
cache through qgr_iter053u_corrected_full.cached_weighted_bulk.
"""
from __future__ import annotations

import argparse

import qgr_iter053u_parallel_parts as v1
import qgr_iter053u_corrected_full as u
import qgr_iter053r_weighted_h5_compact_support as r
import qgr_iter052_4d_directional_variation as it
import qgr_iter051c_full_eom as c


def cached_weighted_part(stream,index,side,prov):
    metric0,pert0,mseed,pseed=r.lane_objects(stream,index)
    if side=="base":
        sample=(stream=="B")
        g2=u.cached_weighted_bulk(metric0,pert0,2,sample=False)
        g3=u.cached_weighted_bulk(metric0,pert0,3,sample=sample)
        source_control=None
    else:
        if stream!="C":
            raise ValueError("transformed weighted part only for C")
        L=it.shear(index); Linv=__import__('numpy').linalg.inv(L)
        mt=c.TransformMetric(metric0,L); pt=it.TransformPerturbation(pert0,L)
        g2=u.corrected_weighted_bulk_transformed(mt,pert0,L,Linv,2)
        g3=u.corrected_weighted_bulk_transformed(mt,pert0,L,Linv,3)
        source_control=u.transformed_source_object_control(pert0,pt,L)
    return {
        "gate":u.GATE,"mode":"part","kind":"weighted","stream":stream,"index":index,"side":side,
        "metric_seed":mseed,"perturbation_seed":pseed,"GJ2":g2,"GJ3":g3,
        "transformed_source_object_control":source_control,
        "implementation_split":"WEIGHTED_PART_VALIDATED_D5_CACHE_H5E-4",
        "h5_backend_validation_run":u.CACHE_EQUIVALENCE_RUN,
        "h5_backend_validation_classification":u.CACHE_EQUIVALENCE_CLASSIFICATION,
        "provenance":prov,
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["part","reduce"],required=True)
    ap.add_argument("--kind",choices=["direct","weighted"])
    ap.add_argument("--stream",choices=["A","B","C"],required=True)
    ap.add_argument("--index",type=int,required=True)
    ap.add_argument("--side",choices=["base","transformed"])
    ap.add_argument("--input-dir")
    ap.add_argument("--state",default="../recovery/state.json")
    ap.add_argument("--out",required=True)
    a=ap.parse_args()

    prov=v1.authorize(a.state)
    lim={"A":4,"B":2,"C":2}[a.stream]
    if not 0<=a.index<lim:
        raise SystemExit("index out of range")

    if a.mode=="part":
        if a.kind is None or a.side is None:
            raise SystemExit("part requires --kind and --side")
        if a.stream!="C" and a.side!="base":
            raise SystemExit("A/B have base side only")
        if a.kind=="direct":
            out=v1.direct_part(a.stream,a.index,a.side,prov)
            out["final_dispatcher"]="V2_DIRECT_REUSES_V1_HISTORICAL_PATH"
        else:
            out=cached_weighted_part(a.stream,a.index,a.side,prov)
            out["final_dispatcher"]="V2_WEIGHTED_USES_VALIDATED_D5_CACHE"
    else:
        if not a.input_dir:
            raise SystemExit("reduce requires --input-dir")
        out=v1.reduce_lane(a.stream,a.index,a.input_dir)
        out["final_dispatcher"]="V2_REDUCER_REUSES_PROVENANCE_HARDENED_V1"

    v1.write(out,a.out)
    if a.mode=="reduce" and not out.get("control_valid",False):
        raise SystemExit(3)
    if a.mode=="reduce" and not out.get("lane_pass",False):
        raise SystemExit(2)


if __name__=="__main__":
    main()
