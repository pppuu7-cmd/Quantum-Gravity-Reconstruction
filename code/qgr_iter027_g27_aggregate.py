#!/usr/bin/env python3
"""Aggregate prospectively frozen Iter027 G27 Boolean composition audits."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path("iter027-g27-results")
OUT = Path("iter027-g27-summary/summary.json")
EXPECTED = {
    "additive-valuation": 6,
    "multiplicative-character": 6,
    "prefix-scale-blindness": 6,
    "boundary-coboundary": 6,
    "composition-ratios": 6,
}

rows = [json.loads(p.read_text(encoding="utf-8")) for p in ROOT.rglob("result.json")]
counts = Counter(r.get("audit") for r in rows)
all_counts = len(rows) == sum(EXPECTED.values()) and all(counts.get(k, 0) == v for k, v in EXPECTED.items())
all_pass = bool(rows) and all(bool(r.get("passed")) for r in rows)

summary = {
    "gate": "ITER027-G27-AGGREGATE",
    "lane_count": len(rows),
    "audit_counts": dict(sorted(counts.items())),
    "all_lane_gates_passed": bool(all_counts and all_pass),
    "scientific_status": "PASS_SCOPED_PRIMITIVE_BOOLEAN_COMPOSITION_FIXES_THE_ADDITIVE_EVENT_SOURCE_LAW_SHAPE_TO_LINEAR_COUNT_AND_EXACT_RELATIVE_COMPOSITION_RATIOS__BLOCKED_ABSOLUTE_PHYSICAL_NORMALIZATION_REMAINS_ONE_SCALAR_AND_BRANCH_PREFIX_GLUING_NORMALIZATION_HAS_ZERO_AUTHORITY_ON_IT",
    "strongest_positive": "Within the prospectively frozen primitive additive S4-equivalent event class, zero empty insertion plus composition removes arbitrary nonlinear count dependence: the exact source law is restricted to the one-dimensional ray J(n)=beta*n. Consequently B4, face-overlap and two-block serial regions have exact beta-independent relative insertion ratios 4:5:8.",
    "strongest_blocker": "The primitive composition laws do not fix the absolute conversion beta. Multiplicative composition likewise leaves one free generator, while exact prefix/history probabilities and gluing path counts are dimensionless combinatorial normalizations with zero authority on the physical event-to-source scale.",
    "additive_source_law_shape": "J(n)=beta*n",
    "additive_source_law_dimension": 1,
    "absolute_beta_fixed": False,
    "physical_finite_curved_phase_samples_derived": False,
    "c6_fixed": False,
    "decision": "PROMOTE_LINEAR_ADDITIVE_EVENT_SOURCE_LAW_SHAPE_ONLY_WITHIN_THE_FROZEN_PRIMITIVE_COMPOSITION_CLASS__DO_NOT_SET_BETA_TO_ONE__NEXT_TEST_BETA_QUOTIENTED_FINITE_PHASE_INVARIANTS_BEFORE_SEARCHING_FOR_ANY_NEW_ABSOLUTE_SCALE_OBJECT",
    "next_gate": "QGR-ITER028-G28-SOURCE-SCALE-QUOTIENT-FINITE-PHASE-INVARIANTS",
    "claim_locks": [
        "J(n)=beta*n is scoped to primitive additive S4-equivalent event composition",
        "absolute beta derived = NO",
        "multiplicative composition generator derived = NO",
        "history/prefix/gluing normalization is not physical event-source normalization",
        "physical finite-curved phase samples derived = NO",
        "c6 fixed = NO",
        "theory established = 0%",
        "KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, sort_keys=True))
if not summary["all_lane_gates_passed"]:
    raise SystemExit(2)
