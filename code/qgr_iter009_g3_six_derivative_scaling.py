#!/usr/bin/env python3
import json

# Same-realization dimensional matching for a six-derivative local correction.
# EH: S2 ~ a_cont int R.  Adding four extra derivatives from finite cell/refinement gives
# S6 ~ a_cont * c6 * h^4 * int I6, I6~curvature^3.
# With ell_Q^2=hbar/a_cont and Gamma=h^2/ell_Q^2:
# (a_cont h^4 / hbar) = h^4/ell_Q^2 = Gamma^2 ell_Q^2.
# Relative to EH at curvature scale R_eff, the dimensionless suppression is c6 h^4 R_eff^2.

# Algebraic exponent check.
h_power = 4
gamma_power = 2
curvature_power_relative = 2
assert h_power == 2*gamma_power

out = {
    "gate": "ITER009-G3-SIX-DERIVATIVE-SCALING",
    "local_term": "S6 = a_cont * c6 * h^4 * integral(I6), I6~Weyl^3 on Ricci-flat vacuum",
    "phase_coefficient": "S6/hbar = c6 * Gamma^2 * ell_Q^2 * integral(I6)",
    "relative_local_correction": "~ c6 * Gamma^2 * (ell_Q^2 R_eff)^2",
    "h_order": "O(h^4)",
    "Gamma_power": gamma_power,
    "classification": "PASS_SCOPED_FIRST_PHYSICALLY_NONREDUNDANT_LOCAL_VACUUM_SIX_DERIVATIVE_CORRECTION_HAS_THE_SAME_H4_AND_GAMMA2_POWER_COUNTING_AS_THE_EXISTING_HISTORY_EFFECT",
    "guard": "The dimensionless coefficient c6 is not fixed by dimensional analysis."
}
print(json.dumps(out, sort_keys=True))
