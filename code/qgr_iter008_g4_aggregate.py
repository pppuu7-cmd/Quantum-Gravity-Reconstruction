#!/usr/bin/env python3
import glob, json

expected={
    "frozen-normalization",
    "deparametrization",
    "z2-sector",
    "loop-phase",
    "clock-backreaction",
}
records={}
for path in glob.glob("iter008-g4-results/**/*.json",recursive=True):
    with open(path,"r",encoding="utf-8") as f: obj=json.load(f)
    if obj.get("lane") in expected: records[obj["lane"]]=obj
missing=sorted(expected-set(records))
if missing: raise SystemExit(f"missing lanes: {missing}")
for name,obj in records.items():
    if not obj.get("success"): raise SystemExit(f"lane failed: {name}")

summary={
    "iteration":"008-G4",
    "parallel_lanes":5,
    "aggregate_success":True,
    "classification":"PARTIAL_SCOPED_FROZEN_ACTION_MATCHING_CLOSES_C_GEOM_IN_REPOSITORY_CONVENTION_BUT_INTERACTING_CLOCK_CONSTRAINTS_RETAIN_RELATIVE_NORMALIZATION__Q13_HAS_TWO_UNSELECTED_Z2_GLOBAL_SECTORS__NO_ABSOLUTE_SCALE_FIX",
    "positive_result":{
        "frozen_signed_c_geom":"-1/2",
        "scope":"frozen QGR action/Riemann sign and unit coordinate-cell convention",
        "invariant_content":"only c_geom*g is invariant under quadratic normalization changes"
    },
    "negative_results":[
        "linear/quadratic deparametrization retains one relative clock-gravity normalization",
        "loop single-valuedness cannot quantize nonzero g with continuously variable curvature holonomy",
        "ordinary dynamical rank-clock scalar backreacts on the established zero-Lambda flat vacuum for every nonzero kinetic normalization"
    ],
    "global_quantization_delta":"Q_13~RP3 admits exactly two flat U(1) line-bundle sectors (+1,-1); current scalar L2 construction is the trivial sector, and no existing QGR rule selects it uniquely",
    "active_blocker":"MISSING_MICROSCOPIC_PRINCIPLE_SELECTING_OR_RENDERING_IRRELEVANT_THE_Z2_GLOBAL_SECTOR_AND_RELATING_ANY_CLOCK_CONSTRAINT_NORMALIZATION_TO_THE_GRAVITATIONAL_DIMENSIONLESS_COUPLING_G",
    "recommended_next_gate":"G5_ONE_PARAMETER_PREDICTIVITY_AND_Z2_SECTOR_OBSERVABILITY_AUDIT",
    "claim_lock":"Frozen c_geom=-1/2 does not imply g=1 or h=l_P. The Z2 sector is a global quantization ambiguity, not evidence for a second continuous coupling."
}
with open("iter008-g4-summary.json","w",encoding="utf-8") as f: json.dump(summary,f,indent=2)
print(json.dumps(summary,sort_keys=True))
