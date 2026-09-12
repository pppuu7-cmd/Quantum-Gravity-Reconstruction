#!/usr/bin/env python3
import glob
import json
import os
from collections import Counter

EXPECTED = {
    "weyl-forward-sensitivity": 6,
    "finite-geometry-phase-nonuniqueness": 6,
    "history-phase-blindness": 6,
    "coarea-measure-phase-nonuniqueness": 6,
    "composition-absolute-scale-null": 6,
}

paths = glob.glob("iter030-g30-results/**/result.json", recursive=True)
rows = []
for path in paths:
    with open(path, "r", encoding="utf-8") as f:
        rows.append(json.load(f))

counts = Counter(r.get("audit") for r in rows)
all_present = len(rows) == 30 and all(counts.get(k, 0) == v for k, v in EXPECTED.items())
all_passed = all(bool(r.get("passed")) for r in rows) if rows else False

summary = {
    "gate": "ITER030-G30-AGGREGATE",
    "lane_count": len(rows),
    "audit_counts": dict(sorted(counts.items())),
    "all_required_artifacts_present": all_present,
    "all_lane_gates_passed": all_passed,
    "finite_curvature_geometry_present": True,
    "weyl_forward_sensitivity_present": True,
    "absolute_beta_fixed": False,
    "c6_fixed": False,
    "physical_weyl_active_absolute_phase_target_present": False,
    "scientific_status": "BLOCKED_SCOPED_EXISTING_QGR_MICROSCOPIC_OBJECTS_CONTAIN_NONTRIVIAL_FINITE_CURVATURE_GEOMETRY_AND_WEYL_ACTIVE_FORWARD_ACTION_SENSITIVITY_BUT_THE_EXISTING_GEOMETRY_HISTORY_COAREA_AND_COMPOSITION_LAYERS_DO_NOT_DERIVE_A_NONHOMOGENEOUS_ABSOLUTE_FINITE_CELL_COHERENT_PHASE_SOURCE_TARGET",
    "strongest_positive": "The finite-cell side is not empty: QGR already has nontrivial finite holonomy geometry and an action direction with nonzero c6 sensitivity on Weyl-active configurations. The missing object is therefore narrower than a missing geometry or missing operator basis.",
    "strongest_blocker": "No existing microscopic layer supplies a derived map from finite-cell geometry/event data to an absolute Lorentzian coherent action phase. History completeness fixes only modulus, coarea fixes a real measure weight, and primitive composition fixes only relative source/phase ratios while retaining the absolute beta null direction.",
    "decision": "DO_NOT_FIT_C6_OR_SET_BETA_BY_CONVENTION__NEXT_SEARCH_FOR_A_DERIVED_NONHOMOGENEOUS_FINITE_CELL_ACTION_PHASE_FUNCTIONAL_FROM_THE_EXISTING_LOCAL_ACTION_AND_DISCRETE_CURVATURE_DATA_WITHOUT_NEW_COUPLINGS",
    "next_gate": "QGR-ITER031-G31-DERIVE-FINITE-CELL-ACTION-PHASE-FROM-EXISTING-DISCRETE-CURVATURE-AND-LOCAL-ACTION-WITHOUT-NEW-COUPLINGS",
    "claim_locks": [
        "nonzero holonomy is not by itself a Weyl-cubic phase datum",
        "weyl forward sensitivity is not inverse authority for c6",
        "history branch modulus is not action phase normalization",
        "coarea measure is not coherent Lorentzian phase",
        "absolute beta derived = NO",
        "c6 fixed = NO",
        "physical Weyl-active absolute phase target derived = NO",
        "theory established = 0%",
        "KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes"
    ]
}

os.makedirs("iter030-g30-summary", exist_ok=True)
with open("iter030-g30-summary/summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, sort_keys=True)
    f.write("\n")
print(json.dumps(summary, sort_keys=True))

if not all_present or not all_passed:
    raise SystemExit(2)
