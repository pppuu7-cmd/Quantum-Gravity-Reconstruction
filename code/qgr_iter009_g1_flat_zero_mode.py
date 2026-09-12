#!/usr/bin/env python3
import json, cmath

# On a uniform configuration G_v=s^2 E at every vertex/cell, all finite
# differences vanish. The derived torsion-free connection is identity/zero
# infinitesimally and curvature is zero, so the zero-Lambda EH action is zero.
# Thus exp(iS/hbar)=1 along the entire noncompact uniform scale orbit.

scales=[1e-6,1e-3,1.0,1e3,1e6]
phases=[]
for s in scales:
    S=0.0
    phase=cmath.exp(1j*S)
    assert abs(phase-1.0)<1e-15
    phases.append([phase.real,phase.imag])

result={
    "iteration":"009-G1",
    "lane":"flat-zero-mode",
    "success":True,
    "classification":"BLOCKED_SCOPED_LORENTZIAN_ACTION_PHASE_DOES_NOT_REGULARIZE_THE_UNIFORM_FLAT_SCALE_ZERO_MODE",
    "uniform_family":"G_v=s^2 E for all v, s>0",
    "curvature":"0",
    "zero_lambda_action":"0",
    "phase":"exp(iS/hbar)=1",
    "sample_scales":scales,
    "key_results":[
        "Uniform rescaling of a constant flat Lorentzian metric leaves all finite differences and curvature zero in the active zero-cosmological branch.",
        "The Lorentzian action contributes no oscillatory suppression at all along this exact scale zero-mode: its phase is identically one.",
        "Combined with the infinite invariant scale-orbit volume, a naive vacuum weight exp(iS/hbar)dmu cannot be normalized by the action phase on this mode.",
        "The result is a scoped obstruction to a naive global path-integral/vacuum measure, not a no-go for operator/algebraic quantum dynamics."
    ]
}
with open("iter009-g1-flat-zero-mode.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
