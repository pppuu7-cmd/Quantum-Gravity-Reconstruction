#!/usr/bin/env python3
import json

# Existing normalized history loss: Delta_hist ~ C_prep * Gamma^2 * (ell_Q^2 R_eff)^2.
# G3 local six-derivative correction: Delta/local-response amplitude receives
# c6 * Gamma^2 * (ell_Q^2 R_eff)^2 times an observable-dependent local response functional.
# Therefore both are the same formal h^4/Gamma^2 order; an unfixed c6 cannot be dropped
# in a claimed complete leading beyond-GR prediction.

history_h_order = 4
local_h_order = 4
assert history_h_order == local_h_order

out = {
    "gate": "ITER009-G3-ORDER-COMPETITION",
    "history_scaling": "C_prep * Gamma^2 * (ell_Q^2 R_eff)^2",
    "local_six_derivative_scaling": "c6 * F_local * Gamma^2 * (ell_Q^2 R_eff)^2",
    "same_refinement_order": True,
    "leading_complete_Oh4_continuous_parameter_set_if_c6_unfixed": ["Gamma", "c6"],
    "classification": "BLOCKED_SCOPED_COMPLETE_LEADING_OH4_PHENOMENOLOGY_IS_NOT_ONE_PARAMETER_UNLESS_C6_IS_MICROSCOPICALLY_FIXED_OR_THE_LOCAL_WEYL_CUBED_RESPONSE_IS_PROVED_IRRELEVANT_FOR_THE_SPECIFIED_OBSERVABLE",
    "guard": "The Iter008 one-parameter claim remains valid for its scoped history/two-derivative comparator, not automatically for the full O(h^4) effective theory."
}
print(json.dumps(out, sort_keys=True))
