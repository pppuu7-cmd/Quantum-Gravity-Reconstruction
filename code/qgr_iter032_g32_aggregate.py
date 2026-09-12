#!/usr/bin/env python3
import glob
import json
import os
from collections import Counter

EXPECTED = {
    "weak-log-refinement-lift": 6,
    "lipschitz-null-bound": 6,
    "riemann-polynomial-convergence": 6,
    "quadrature-common-limit": 6,
    "local-integral-cylindrical-additivity": 6,
}
rows = []
for path in glob.glob("iter032-g32-results/**/result.json", recursive=True):
    with open(path, "r", encoding="utf-8") as f:
        rows.append(json.load(f))
counts = Counter(r.get("audit") for r in rows)
all_present = len(rows) == 30 and all(counts.get(k, 0) == v for k, v in EXPECTED.items())
all_passed = all(bool(r.get("passed")) for r in rows) if rows else False

summary = {
    "gate": "ITER032-G32-AGGREGATE",
    "lane_count": len(rows),
    "audit_counts": dict(sorted(counts.items())),
    "all_required_artifacts_present": all_present,
    "all_lane_gates_passed": all_passed,
    "conditional_refinement_limit_mechanism": "PASS_SCOPED",
    "uniform_qgr_regularity_authority_derived": False,
    "absolute_quantum_phase_normalization_fixed": False,
    "physical_weyl_active_absolute_phase_target_present": False,
    "c6_fixed": False,
    "scientific_status": "PASS_CONDITIONAL_SCOPED_RESOLVED_WEAK_CELL_REFINEMENT_PLUS_UNIFORM_REGULARITY_REMOVES_LOCAL_LOG_AND_FINITE_QUADRATURE_AMBIGUITIES_IN_THE_PROJECTIVE_LIMIT_AND_THE_LIMITING_LOCAL_ACTION_IS_CYLINDRICALLY_ADDITIVE__BLOCKED_QGR_UNIFORM_REFINEMENT_REGULARITY_AND_ABSOLUTE_PHASE_NORMALIZATION_NOT_YET_DERIVED",
    "strongest_positive": "A coherent route around the G31 finite-level no-go now exists. With resolved fine-path data and sufficiently weak subcells, local principal logs reconstruct a continuous lift; under a uniform Lipschitz bound finite-sample null directions are forced to zero as 1/N; standard local quadratures share the same limit; and the limiting local integral blocks associatively.",
    "strongest_blocker": "The convergence theorem is conditional on a uniform regularity/bounded-curvature control along the actual QGR refinement tower. Current QGR results establish local regularity near specific branches but do not yet provide a tower-wide uniform bound. The absolute quantum phase normalization, beta, and c6 also remain unfixed.",
    "decision": "PROMOTE_THE_PROJECTIVE_REFINEMENT_LIMIT_MECHANISM_ONLY_CONDITIONALLY__NEXT_DERIVE_OR_REFUTE_THE_REQUIRED_UNIFORM_QGR_REGULARITY_BOUND_FROM_DISCRETE_TORSION_JACOBIAN_CONTROL_AND_LOCAL_ACTION",
    "next_gate": "QGR-ITER033-G33-REFINEMENT-TOWER-UNIFORM-REGULARITY-AUTHORITY-FROM-TORSION-JACOBIAN-AND-LOCAL-ACTION",
    "claim_locks": [
        "uniform QGR regularity along the refinement tower is not yet derived",
        "conditional convergence is not an exact finite-cell phase theorem",
        "coarse holonomy alone still does not fix a winding sector",
        "absolute beta derived = NO",
        "absolute quantum phase normalization fixed = NO",
        "physical Weyl-active absolute phase target derived = NO",
        "c6 fixed = NO",
        "theory established = 0%",
        "KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes"
    ]
}
os.makedirs("iter032-g32-summary", exist_ok=True)
with open("iter032-g32-summary/summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, sort_keys=True)
    f.write("\n")
print(json.dumps(summary, sort_keys=True))
if not all_present or not all_passed:
    raise SystemExit(2)
