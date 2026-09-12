#!/usr/bin/env python3
"""Aggregate the prospectively frozen Iter026 G26 exact authority lanes."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path("iter026-g26-results")
OUT = Path("iter026-g26-summary/summary.json")
EXPECTED = {
    "incidence-authority": 6,
    "pair-action-homogeneity": 6,
    "connection-scale-homogeneity": 6,
    "history-normalization-authority": 6,
    "coarea-measure-vs-phase": 6,
}

rows = []
for p in ROOT.rglob("result.json"):
    rows.append(json.loads(p.read_text(encoding="utf-8")))

counts = Counter(r.get("audit") for r in rows)
all_counts = all(counts.get(k, 0) == v for k, v in EXPECTED.items()) and len(rows) == sum(EXPECTED.values())
all_pass = all(bool(r.get("passed")) for r in rows) if rows else False

summary = {
    "gate": "ITER026-G26-AGGREGATE",
    "lane_count": len(rows),
    "audit_counts": dict(sorted(counts.items())),
    "all_lane_gates_passed": bool(all_counts and all_pass),
    "scientific_status": "PASS_SCOPED_EXISTING_QGR_MICROSCOPIC_INCIDENCE_FIXES_THE_EVENT_RESPONSE_DIRECTION_WHILE_THE_CURRENT_PAIR_ACTION_CONNECTION_HOLONOMY_HISTORY_NORMALIZATION_AND_COAREA_MEASURE_CHAIN_IS_HOMOGENEOUS_SOURCE_CONDITIONAL_OR_PHASE_BLIND_AND_HAS_NO_AUTHORITY_TO_FIX_A_NONZERO_ABSOLUTE_EVENT_TO_BOUNDARY_SOURCE_STRENGTH",
    "strongest_positive": "The existing chain is internally consistent and highly constrained: B4 distinct-pair incidence fixes the unique response ray C=J-I; the pair action, compatible connection/holonomy and normalized history instrument then propagate/evolve supplied configurations without introducing arbitrary relative history weights.",
    "strongest_blocker": "Every currently derived candidate authority for the missing scalar is either homogeneous in the field normalization, conditional on an already supplied G/source configuration, restricted to branch modulus, or a real measure factor. None supplies a nonhomogeneous same-realization rule event count -> boundary/source strength. The scalar cannot be set to one by incidence notation or imported from the coarea weight.",
    "event_response_direction_derived": True,
    "event_to_source_absolute_strength_derived": False,
    "physical_finite_curved_phase_samples_derived": False,
    "c6_fixed": False,
    "decision": "CLOSE_THE_EXISTING_MICROSCOPIC_AUTHORITY_CENSUS_AS_ZERO_AUTHORITY_ON_THE_ABSOLUTE_EVENT_SOURCE_SCALAR__DO_NOT_ADD_A_COUPLING__NEXT_SEARCH_MUST_TARGET_A_GENUINELY_NONHOMOGENEOUS_PRIMITIVE_COMPOSITION_OR_BOUNDARY_INSERTION_OBJECT_FROM_THE_SAME_BOOLEAN_REALIZATION",
    "next_gate": "QGR-ITER027-G27-PRIMITIVE-BOOLEAN-COMPOSITION-BOUNDARY-INSERTION-AUTHORITY",
    "claim_locks": [
        "event response direction derived in strict S4 distinct-pair sector = YES",
        "absolute event-to-source strength derived = NO",
        "history modulus 1/sqrt(24) is not an event-source strength",
        "torsion/coarea real measure weight is not a Lorentzian coherent phase",
        "physical finite-curved phase samples derived = NO",
        "c6 fixed = NO",
        "KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, sort_keys=True))
if not summary["all_lane_gates_passed"]:
    raise SystemExit(2)
