#!/usr/bin/env python3
import glob
import json
import os
from collections import Counter

EXPECTED = {
    "global-log-branch-nonuniqueness": 6,
    "weak-cell-principal-branch": 6,
    "finite-sample-integral-nullspace": 6,
    "overall-action-phase-scale": 6,
    "finite-refinement-integral-nullspace": 6,
}

rows = []
for path in glob.glob("iter031-g31-results/**/result.json", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        rows.append(json.load(f))
counts = Counter(r.get("audit") for r in rows)
all_present = len(rows) == 30 and all(counts.get(k, 0) == v for k, v in EXPECTED.items())
all_passed = all(bool(r.get("passed")) for r in rows) if rows else False

summary = {
    "gate": "ITER031-G31-AGGREGATE",
    "lane_count": len(rows),
    "audit_counts": dict(sorted(counts.items())),
    "all_required_artifacts_present": all_present,
    "all_lane_gates_passed": all_passed,
    "weak_cell_local_curvature_lift": "PASS_SCOPED",
    "global_finite_holonomy_log_unique": False,
    "exact_finite_sample_action_integral_unique": False,
    "absolute_quantum_phase_normalization_fixed_by_stationarity": False,
    "physical_weyl_active_absolute_phase_target_present": False,
    "c6_fixed": False,
    "scientific_status": "PARTIAL_SCOPED_WEAK_CELL_CONTINUITY_SELECTS_A_UNIQUE_LOCAL_PRINCIPAL_CURVATURE_LIFT__BLOCKED_EXACT_FINITE_CELL_ACTION_PHASE_DESCENT_BECAUSE_GLOBAL_HOLONOMY_LOG_BRANCH_FINITE_SAMPLE_QUADRATURE_AND_ABSOLUTE_PHASE_NORMALIZATION_ARE_NOT_FIXED_BY_THE_EXISTING_DISCRETE_DATA",
    "strongest_positive": "A genuine constructive piece exists: before the first compact-rotation branch cut, weak-cell continuity selects a unique principal holonomy lift and therefore a local leading curvature representative. This can seed a controlled refinement-limit action construction.",
    "strongest_blocker": "The exact finite-cell phase is not yet a function of the current finite data alone. Globally the holonomy logarithm has branch ambiguity, and at every finite refinement there are local-density deformations that vanish on all sampled nodes but change the integrated action. Classical stationarity also does not by itself fix the absolute quantum phase normalization.",
    "decision": "PROMOTE_ONLY_THE_WEAK_CELL_PRINCIPAL_CURVATURE_LIFT__DO_NOT_PROMOTE_AN_EXACT_FINITE_CELL_PHASE__NEXT_TEST_A_PROJECTIVE_REFINEMENT_LIMIT_ACTION_FUNCTIONAL_WITH_CYLINDRICAL_CONSISTENCY_AND_ERROR_CONTROL",
    "next_gate": "QGR-ITER032-G32-PROJECTIVE-REFINEMENT-LIMIT-ACTION-PHASE-CYLINDRICAL-CONSISTENCY-AND-UNIQUENESS",
    "claim_locks": [
        "principal holonomy log authority is local weak-cell only",
        "finite holonomy does not globally define unique curvature log",
        "finite samples do not exactly determine a continuum action integral",
        "classical stationarity does not fix absolute quantum phase normalization",
        "physical Weyl-active absolute phase target derived = NO",
        "c6 fixed = NO",
        "theory established = 0%",
        "KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes"
    ]
}

os.makedirs("iter031-g31-summary", exist_ok=True)
with open("iter031-g31-summary/summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, sort_keys=True)
    f.write("\n")
print(json.dumps(summary, sort_keys=True))
if not all_present or not all_passed:
    raise SystemExit(2)
