#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('iter009-g4-results')
records=[json.loads(p.read_text()) for p in sorted(root.rglob('*.json'))]
assert len(records)==6,len(records)
summary={
  "iteration":"009-G4",
  "parallel_lanes":6,
  "aggregate_success":True,
  "key_results":[
    "Current frozen two-derivative/symmetry/continuum data admit an explicit continuous S_EH+lambda h^4 Weyl^3 family and therefore do not determine c6.",
    "Because Weyl^3 is homogeneous cubic in curvature and the flat seed has W0=0, its first and second variations vanish at the flat seed; c6 does not alter the flat linearized Hessian or characteristic cone.",
    "A nonzero-Weyl background generically activates a c6-dependent quadratic response; an explicit traceless diagonal witness has a nonzero epsilon^2 coefficient.",
    "Scalar branch action phases cancel exactly from each Kraus sandwich in the traced history-mixture channel.",
    "The existing G6H implementation is a fixed-geometry transport/overlap comparator with no explicit action-phase or c6 input and does not recompute c6-corrected equations of motion.",
    "A sufficient diamond-norm convergence criterion can be written in terms of uniform branch operator differences, but current QGR O(h^4) evidence is scalar/RMS rather than a uniform operator bound."
  ],
  "classification":"PARTIAL_SCOPED_C6_IS_NOT_FIXED_BY_CURRENT_LOWER_ORDER_DATA_BUT_DECOUPLES_FROM_FLAT_LINEARIZED_PROPAGATION_AND_FROM_THE_EXISTING_FIXED_GEOMETRY_TRACED_G6H_CHANNEL_AS_A_SCALAR_PHASE__SELF_CONSISTENT_CURVED_C6_DYNAMICS_AND_INFINITE_REFINEMENT_REMAIN_OPEN",
  "active_blocker":"MISSING_SELF_CONSISTENT_CURVED_C6_RESPONSE_OR_MICROSCOPIC_C6_MATCHING_AND_UNIFORM_BRANCH_OPERATOR_CONVERGENCE",
  "recommended_next_gate":"G5_SELF_CONSISTENT_CURVED_C6_RESPONSE_AND_MICROSCOPIC_FINITE_CELL_MATCHING",
  "claim_lock":"Retain Iter008/G6H one-parameter predictivity only for the existing fixed-geometry comparator; do not call the full self-consistent O(h^4) theory one-parameter while c6 is unfixed."
}
print(json.dumps(summary,sort_keys=True))
Path('iter009-g4-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
