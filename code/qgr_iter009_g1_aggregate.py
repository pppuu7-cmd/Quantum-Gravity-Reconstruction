#!/usr/bin/env python3
import glob, json

expected={
    "scale-measure",
    "flat-zero-mode",
    "z2-superselection",
    "four-derivative-census",
    "power-counting",
}
records={}
for path in glob.glob("iter009-g1-results/**/*.json",recursive=True):
    with open(path,"r",encoding="utf-8") as f: obj=json.load(f)
    if obj.get("lane") in expected: records[obj["lane"]]=obj
missing=sorted(expected-set(records))
if missing: raise SystemExit(f"missing lanes: {missing}")
for name,obj in records.items():
    if not obj.get("success"): raise SystemExit(f"lane failed: {name}")

summary={
    "iteration":"009-G1",
    "parallel_lanes":5,
    "aggregate_success":True,
    "classification":"BLOCKED_SCOPED_NAIVE_GLOBAL_INTERACTING_VACUUM_MEASURE_IS_NOT_NORMALIZED_ALONG_THE_FLAT_SCALE_ZERO_MODE__TWO_DERIVATIVE_LOCAL_ACTION_IS_NOT_QUANTUM_CLOSED_BY_SYMMETRY_POWER_COUNTING__Z2_SECTORS_ARE_REFINEMENT_SUPERSELECTED",
    "measure_result":"Q13 invariant measure has infinite R_+ scale-orbit Haar volume; zero-Lambda flat action phase is identically one along the uniform scale mode",
    "global_sector_result":"identity/refinement-connected maps preserve + and - flat Z2 sectors separately",
    "four_derivative_result":"two independent parity-even curvature-squared local bulk directions remain in 4D modulo Euler and total derivatives",
    "power_counting_result":"generic superficial derivative order omega=2L+2 at L loops; allowance only, not an actual divergence coefficient calculation",
    "active_blocker":"MISSING_MICROSCOPIC_FINITE_REFINEMENT_DERIVATION_OF_HIGHER_DERIVATIVE_EFFECTIVE_COEFFICIENTS_AND_A_CONTROLLED_INTERACTING_STATE_OR_OPERATOR_CONSTRUCTION_BEYOND_THE_NAIVE_GLOBAL_INVARIANT_VACUUM_WEIGHT",
    "recommended_next_gate":"G2_FINITE_REFINEMENT_EFFECTIVE_ACTION_MATCHING_AND_INTERACTING_STATE_CONSTRUCTION",
    "claim_lock":"Do not infer that QGR has no quantum completion from failure of the naive invariant vacuum weight; do not infer actual loop divergences solely from power counting."
}
with open("iter009-g1-summary.json","w",encoding="utf-8") as f: json.dump(summary,f,indent=2)
print(json.dumps(summary,sort_keys=True))
