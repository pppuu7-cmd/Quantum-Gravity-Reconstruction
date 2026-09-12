#!/usr/bin/env python3
import glob, json, os

expected = {
    "clock-geometry",
    "topology-symplectic",
    "clock-dynamics",
    "clock-matter-normalization",
    "b4-spectrum",
}

records = []
for path in glob.glob("iter008-g3-results/**/*.json", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if obj.get("lane") in expected:
        records.append(obj)

lanes = {r["lane"]: r for r in records}
missing = sorted(expected - set(lanes))
if missing:
    raise SystemExit(f"missing lanes: {missing}")
for name, rec in lanes.items():
    if not rec.get("success"):
        raise SystemExit(f"lane failed: {name}")

summary = {
    "iteration": "008-G3",
    "parallel_lanes": 5,
    "aggregate_success": True,
    "classification": "BLOCKED_SCOPED_INTRINSIC_CLOCK_AND_B4_DISCRETENESS_DO_NOT_CALIBRATE_PHYSICAL_SCALE__CURRENT_Q13_TOPOLOGY_HAS_NO_CONTINUOUS_H2_PREQUANTIZATION_CLASS__MINIMAL_CLOCK_OR_CLOCK_MATTER_DYNAMICS_INTRODUCE_A_NEW_FREE_SCALE",
    "closed_in_scope": [
        "rank tick versus proper time at the symmetric Lorentzian seed",
        "continuous topological prequantization route on Q_13",
        "minimal rank-translation-invariant clock dynamics",
        "minimal intrinsic-clock-as-matter normalization route",
        "natural B4 combinatorial Laplacian spectrum"
    ],
    "key_results": [
        "Every elementary unit-rank cover is null; the symmetric rank direction and barycentric mean step are timelike, but a nonzero proper-time tick requires a coarse/readout prescription and still carries h.",
        "Q_{1,3} has homotopy type RP^3 with H^2_deRham=0; its Z2 torsion can encode only a discrete sign/line-bundle sector, not quantize a positive real g.",
        "Minimal clock dynamics leaves one free hopping/frequency scale after removing a common phase.",
        "Using the intrinsic rank clock as a physical scalar makes its kinetic normalization a new physical free coefficient rather than fixing the gravitational g.",
        "The B4 Laplacian fixes only dimensionless eigenvalue ratios 0,2,4,6,8; physical eigenvalues retain the overall 1/h^2 scale."
    ],
    "active_blocker": "MISSING_NONTRIVIAL_SAME_REALIZATION_QUANTUM_GEOMETRIC_OR_MATTER_PRINCIPLE_THAT_RELATES_THE_CLOCK_ENERGY_SCALE_TO_G_WITHOUT_ADDING_A_NEW_FREE_NORMALIZATION",
    "recommended_next_gate": "G4_SEARCH_NONTRIVIAL_DISCRETE_GEOMETRY_OR_INTERACTING_CLOCK_GRAVITY_CONSTRAINT_RELATION",
    "claim_lock": "Do not infer a minimum length, Planck-time tick, or g=1 from B4 discreteness, the rank clock, RP3 topology, or the normalized history instrument."
}

with open("iter008-g3-summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)
print(json.dumps(summary, sort_keys=True))
