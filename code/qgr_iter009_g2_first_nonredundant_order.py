#!/usr/bin/env python3
import json

# Iter009-G1 power counting: omega=2L+2.
# G2 field-redefinition audit removes both parity-even 4-derivative vacuum bulk
# directions at first correction order. Therefore the first power-counting level
# not removed by that argument is six derivatives (L=2 allowance).
levels = []
for L in range(1,5):
    omega = 2*L + 2
    levels.append((L, omega))
assert levels[0] == (1,4)
assert levels[1] == (2,6)

out = {
    "gate": "ITER009-G2-FIRST-NONREDUNDANT-ORDER",
    "power_counting_levels": levels,
    "four_derivative_vacuum_bulk_quotient_after_local_field_redefinition": 0,
    "first_not_eliminated_by_current_redundancy_argument": "six derivatives / curvature-cubed-or-derivative-curvature class",
    "classification": "PARTIAL_SCOPED_FIRST_POTENTIALLY_PHYSICAL_LOCAL_VACUUM_CORRECTION_MOVES_TO_SIX_DERIVATIVES_BUT_COMPLETE_SIX_DERIVATIVE_CENSUS_AND_MICROSCOPIC_COEFFICIENTS_REMAIN_OPEN",
    "guard": "This is not a proof that a six-derivative coefficient is nonzero, unique, or divergent."
}
print(json.dumps(out, sort_keys=True))
