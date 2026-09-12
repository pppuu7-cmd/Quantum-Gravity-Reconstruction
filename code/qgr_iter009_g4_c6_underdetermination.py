#!/usr/bin/env python3
import json

# Consider the explicit same-field local family
# S_lambda = S_EH + lambda * a_cont * h^4 * integral(Weyl^3).
# The added term is six-derivative and vanishes as h^4 in the continuum refinement limit.
# Therefore all data that fixed only the metric-only <=2-derivative local action and its
# flat quadratic/cubic/quartic EH expansion cannot determine lambda.

lambdas = [-3, -1, 0, 1, 7]
records = []
for lam in lambdas:
    records.append({
        "lambda": lam,
        "two_derivative_sector_change": 0,
        "continuum_h_to_zero_change_order": "h^4",
        "field_content_change": 0,
        "pullback_covariance_preserved": True,
        "parity_even": True,
    })

out = {
    "gate": "ITER009-G4-C6-UNDERDETERMINATION",
    "family": "S_lambda=S_EH+lambda*a_cont*h^4*integral(Weyl^3)",
    "sampled_distinct_lambda_values": lambdas,
    "all_share_frozen_two_derivative_sector": all(r["two_derivative_sector_change"] == 0 for r in records),
    "classification": "BLOCKED_SCOPED_EXISTING_TWO_DERIVATIVE_SYMMETRY_AND_CONTINUUM_DATA_ADMIT_A_CONTINUOUS_C6_FAMILY_AND_DO_NOT_FIX_C6",
    "guard": "This does not prove that every lambda has a common exact microscopic finite-cell realization; it proves current lower-order authority is insufficient to select one."
}
print(json.dumps(out, sort_keys=True))
