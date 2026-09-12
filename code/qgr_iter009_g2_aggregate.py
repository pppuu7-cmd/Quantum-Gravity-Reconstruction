#!/usr/bin/env python3
import json
from pathlib import Path

root = Path('iter009-g2-results')
records = []
for p in sorted(root.rglob('*.json')):
    records.append(json.loads(p.read_text()))
assert len(records) == 6, len(records)
classes = [r['classification'] for r in records]

summary = {
    "iteration": "009-G2",
    "parallel_lanes": 6,
    "aggregate_success": True,
    "key_results": [
        "Infinite invariant reference-measure volume does not prevent normalized L2 states; it only prevents treating the reference measure itself as a vacuum probability.",
        "The exact 24-history instrument composes to arbitrary finite depth with completeness preserved as 24^n * 24^-n = 1.",
        "No authoritative exact finite-cell higher-derivative action closure marker exists in the current repository; existing action authority is local/continuum plus scoped branch evaluation.",
        "In pure vacuum four-dimensional EH/QGR local branch, the two curvature-squared bulk directions are both first-order EOM-redundant under local metric field redefinitions; the exact coefficient map has rank 2.",
        "The first power-counting level not removed by that redundancy argument is six derivatives, but its complete operator census and microscopic coefficients remain open.",
        "Current O(h^4) convergence of selected observables is not a uniform diamond/strong operator bound and therefore does not establish an infinite-refinement interacting channel limit."
    ],
    "classification": "PARTIAL_SCOPED_FINITE_DEPTH_INTERACTING_OPERATOR_DYNAMICS_IS_WELL_DEFINED_WITH_NORMALIZED_L2_STATES__CURVATURE_SQUARED_VACUUM_BULK_DIRECTIONS_ARE_FIELD_REDEFINITION_REDUNDANT__SIX_DERIVATIVE_MICROSCOPIC_MATCHING_AND_INFINITE_REFINEMENT_LIMIT_REMAIN_OPEN",
    "active_blocker": "MISSING_COMPLETE_SIX_DERIVATIVE_PHYSICAL_OPERATOR_CENSUS_AND_MICROSCOPIC_COEFFICIENT_MATCHING_PLUS_UNIFORM_OPERATOR_CONVERGENCE_CONTROL_FOR_INFINITE_REFINEMENT",
    "recommended_next_gate": "G3_SIX_DERIVATIVE_PHYSICAL_OPERATOR_CENSUS_AND_FINITE_REFINEMENT_MATCHING",
    "claim_lock": "Do not call curvature-squared directions physical free parameters in pure vacuum after the rank-2 field-redefinition audit; do not claim infinite-depth completion from finite CPTP normalization."
}
print(json.dumps(summary, sort_keys=True))
Path('iter009-g2-summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True)+"\n")
