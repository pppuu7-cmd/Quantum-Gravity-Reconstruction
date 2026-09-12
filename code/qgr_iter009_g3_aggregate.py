#!/usr/bin/env python3
import json
from pathlib import Path

root = Path('iter009-g3-results')
records = [json.loads(p.read_text()) for p in sorted(root.rglob('*.json'))]
assert len(records) == 6, len(records)

summary = {
    "iteration": "009-G3",
    "parallel_lanes": 6,
    "aggregate_success": True,
    "key_results": [
        "In four-dimensional Ricci-flat vacuum, the algebraic curvature-cubed sector reduces to one parity-even Weyl-cubed direction (plus one parity-odd direction outside the active parity-even branch).",
        "Derivative-curvature six-derivative bulk structures reduce by vacuum EOM, integration by parts and Bianchi/Lichnerowicz identities to the same parity-even Weyl-cubed bulk class in the scoped vacuum sector.",
        "A Petrov-D-type traceless Weyl block diag(-2,1,1) gives nonzero cubic trace, so the surviving parity-even class is not identically zero.",
        "The same-realization dimensional correction scales as a_cont*c6*h^4*int(I6), hence c6*Gamma^2*(ell_Q^2 R_eff)^2 relative to the EH scale: the same formal O(h^4) / Gamma^2 order as the existing history effect.",
        "No current authoritative QGR finite-cell/microscopic record fixes c6.",
        "Therefore the complete leading O(h^4) phenomenology is not yet one-parameter unless c6 is microscopically fixed or its response is proved irrelevant for a specified observable."
    ],
    "classification": "PARTIAL_SCOPED_ON_SHELL_PARITY_EVEN_PURE_VACUUM_SIX_DERIVATIVE_OPERATOR_SHAPE_COLLAPSES_TO_ONE_WEYL_CUBED_CLASS__ITS_QGR_COEFFICIENT_C6_IS_UNFIXED_AND_COMPETES_AT_THE_SAME_OH4_ORDER_AS_THE_HISTORY_EFFECT",
    "active_blocker": "MISSING_SAME_REALIZATION_MICROSCOPIC_DERIVATION_OR_ELIMINATION_OF_C6_AND_UNIFORM_INFINITE_REFINEMENT_OPERATOR_CONTROL",
    "recommended_next_gate": "G4_MICROSCOPIC_C6_MATCHING_OR_OBSERVABLE_DECOUPLING_AND_CHANNEL_CONVERGENCE",
    "claim_lock": "Iter008 one-parameter predictivity is scoped to the constructed history/two-derivative comparator; do not promote it to the complete O(h^4) effective theory while c6 is unfixed."
}
print(json.dumps(summary, sort_keys=True))
Path('iter009-g3-summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True)+"\n")
