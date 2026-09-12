#!/usr/bin/env python3
import glob, json

expected={
    "parameter-count",
    "relative-ratio",
    "conditional-bound",
    "local-z2-invisibility",
    "global-z2-loop",
}
records={}
for path in glob.glob("iter008-g5-results/**/*.json",recursive=True):
    with open(path,"r",encoding="utf-8") as f: obj=json.load(f)
    if obj.get("lane") in expected: records[obj["lane"]]=obj
missing=sorted(expected-set(records))
if missing: raise SystemExit(f"missing lanes: {missing}")
for name,obj in records.items():
    if not obj.get("success"): raise SystemExit(f"lane failed: {name}")

summary={
    "iteration":"008-G5",
    "parallel_lanes":5,
    "aggregate_success":True,
    "classification":"PASS_SCOPED_QGR_LOCAL_BROADBAND_SECTOR_IS_ONE_CONTINUOUS_PARAMETER_FALSIFIABLE_AND_HAS_PARAMETER_FREE_RELATIVE_PREDICTIONS__Z2_GLOBAL_SECTOR_IS_LOCALLY_INVISIBLE_BUT_GLOBALLY_DISTINGUISHABLE",
    "continuous_local_parameter_count":1,
    "invariant_parameter":"Gamma=h^2/ell_Q^2=c_geom*g",
    "parameter_free_relative_prediction":"leading m1/m0 normalized packet loss coefficient ratio = 4/3 in the specified G6F comparison",
    "conditional_bound":"Gamma <= sqrt(delta_max/C_prep)/abs(ell_Q^2 R_eff)",
    "z2_local_result":"leading refinement near E is contained in a contractible Lorentzian neighborhood and is insensitive to the flat Z2 sector",
    "z2_global_result":"explicit noncontractible loop G(s)=2v(s)v(s)^T-I with v:e0->-e0 has holonomy +1/-1 in the two sectors",
    "iteration_conclusion":"The physical-scale search does not derive Gamma internally, but the remaining freedom is completely classified in the tested scope: one continuous locally measurable parameter plus one globally detectable discrete flat sector. The local model is not rendered nonpredictive by the unfixed scale.",
    "recommended_next_stage":"ITER009_INTERACTING_QUANTUM_MEASURE_RADIATIVE_STABILITY_AND_GLOBAL_SECTOR_COMPLETION",
    "claim_lock":"One-parameter predictivity is not experimental confirmation and does not establish the absolute value of Gamma or select the Z2 sector."
}
with open("iter008-g5-summary.json","w",encoding="utf-8") as f: json.dump(summary,f,indent=2)
print(json.dumps(summary,sort_keys=True))
