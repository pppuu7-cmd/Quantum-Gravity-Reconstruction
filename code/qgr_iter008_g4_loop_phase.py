#!/usr/bin/env python3
import json, math

# Suppose one tried to quantize g by requiring exp(i g Phi)=1 for every
# admissible small curvature/history loop phase Phi. The established QGR curved
# branch admits continuously variable small holonomy. On an interval around
# Phi=0, continuity forces the integer winding n(Phi)=g Phi/(2pi) to be constant.
# At Phi=0 it is zero, hence g Phi=0 throughout the interval; with any nonzero
# Phi this forces g=0. Thus such a condition cannot quantize a nonzero g unless
# the curvature flux itself is separately discretized.

phis=[0.0,1e-6,2e-6,5e-6]
for g in [0.3,1.0,7.0]:
    vals=[g*p/(2*math.pi) for p in phis]
    # nonzero small phis do not all land on integers for generic nonzero g
    assert any(abs(v-round(v))>1e-12 for v in vals[1:])

result={
    "iteration":"008-G4",
    "lane":"loop-phase",
    "success":True,
    "classification":"FAIL_SCOPED_ROOT_OF_UNITY_OR_LOOP_SINGLE_VALUEDNESS_CANNOT_QUANTIZE_NONZERO_G_WHILE_QGR_CURVATURE_HOLONOMY_VARIES_CONTINUOUSLY",
    "tested_small_fluxes":phis,
    "key_results":[
        "The established regular curved QGR sector admits continuously variable small connection/holonomy data rather than a discrete set of curvature fluxes.",
        "Requiring exp(i g Phi)=1 for every continuously variable small loop phase would force the integer winding to remain zero near Phi=0 and therefore force g=0 if any nonzero small Phi is allowed.",
        "Thus 24-history closure, path single-valuedness, or loop composition cannot be converted into a nonzero quantization rule for g without first deriving a new discrete curvature/flux spectrum.",
        "Physical branch-dependent phases are allowed observables/transport data; they are not gauge inconsistencies that must be roots of unity."
    ]
}
with open("iter008-g4-loop-phase.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
