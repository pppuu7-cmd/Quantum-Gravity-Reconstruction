#!/usr/bin/env python3
import json, math

# A sufficient channel-limit criterion is absolute summability in a complete operator norm,
# e.g. sum ||Phi_{n+1}-Phi_n||_diamond < infinity. For dyadic h_n=2^-n,
# a hypothetical uniform O(h_n^4) diamond bound would be summable.
partial = sum((2.0**(-n))**4 for n in range(1,40))
exact = (1/16)/(1-1/16)
assert abs(partial-exact) < 1e-12

out = {
    "gate": "ITER009-G2-INFINITE-REFINEMENT-CRITERION",
    "sufficient_norm_criterion": "sum_n ||Phi_{n+1}-Phi_n||_diamond < infinity",
    "dyadic_h4_series_sum": exact,
    "current_QGR_evidence": "O(h^4) convergence only for specified scalar/broadband comparators, not a uniform diamond/strong operator bound on the full interacting channel family",
    "classification": "BLOCKED_SCOPED_FINITE_DEPTH_CHANNELS_ARE_EXACTLY_NORMALIZED_BUT_CURRENT_OBSERVABLE_H4_SCALING_DOES_NOT_PROVE_AN_INFINITE_REFINEMENT_OPERATOR_LIMIT",
    "guard": "Scalar observable convergence cannot be promoted to channel/operator convergence without a uniform bound on a dense/full state domain."
}
print(json.dumps(out, sort_keys=True))
