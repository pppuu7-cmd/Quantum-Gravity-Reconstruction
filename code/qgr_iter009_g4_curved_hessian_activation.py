#!/usr/bin/env python3
import json
from fractions import Fraction

# Diagonal traceless Weyl-block witness. Let W(eps)=W0+eps*w with
# W0=diag(-2,1,1), w=diag(1,-1,0).  Then tr(W(eps)^3) has a nonzero eps^2 term.
W0 = [Fraction(-2), Fraction(1), Fraction(1)]
w = [Fraction(1), Fraction(-1), Fraction(0)]
# coefficients of sum_i (W0_i + eps w_i)^3
c0 = sum(x**3 for x in W0)
c1 = sum(3*W0[i]**2*w[i] for i in range(3))
c2 = sum(3*W0[i]*w[i]**2 for i in range(3))
c3 = sum(wi**3 for wi in w)
assert c0 == -6
assert c2 == -3
assert c2 != 0
second_variation = 2*c2

out = {
    "gate": "ITER009-G4-CURVED-HESSIAN-ACTIVATION",
    "background_block": [-2,1,1],
    "perturbation_block": [1,-1,0],
    "tr_W_cube_coefficients_eps_0_to_3": [str(c0),str(c1),str(c2),str(c3)],
    "second_variation_coefficient": str(second_variation),
    "classification": "PASS_SCOPED_NONZERO_BACKGROUND_WEYL_CURVATURE_GENERICALLY_ACTIVATES_A_C6_DEPENDENT_QUADRATIC_RESPONSE",
    "guard": "This algebraic witness establishes generic curved-background activation, not the numerical response of the specific G9 realization."
}
print(json.dumps(out, sort_keys=True))
