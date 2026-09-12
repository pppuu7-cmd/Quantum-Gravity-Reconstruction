#!/usr/bin/env python3
import json
from fractions import Fraction

# Authoritative earlier exact result:
#   S2_connection = -2 S2_QGR
# in the frozen QGR field/action convention.
# With D = h d and one fundamental four-cell per coordinate h^4,
#   kappa sum S2_QGR(Dh) -> (kappa/h^2) int S2_QGR(dh)
# while
#   a int L_conn^(2) = -2 a int S2_QGR(dh).
# Coefficient matching therefore gives a = -kappa/(2 h^2).

connection_to_qgr = Fraction(-2, 1)
# Solve 1 = connection_to_qgr * c_frozen in
# kappa/h^2 = connection_to_qgr * a and a=c_frozen*kappa/h^2.
c_frozen = Fraction(1, 1) / connection_to_qgr
assert c_frozen == Fraction(-1, 2)

# Demonstrate convention covariance under S2'_QGR = alpha S2_QGR.
# To represent the same microscopic action, kappa' = kappa/alpha.
# Connection coefficient relative to S2' is -2/alpha, hence c'=-alpha/2.
# The product c'*g' is invariant when g'=g/alpha.
alphas = [Fraction(1,2), Fraction(1), Fraction(3,2), Fraction(2), Fraction(7,3)]
checks=[]
for alpha in alphas:
    cp = -alpha/Fraction(2)
    # take g=1 for algebraic invariant test only, not a physical choice
    gp = Fraction(1,1)/alpha
    invariant = cp*gp
    assert invariant == Fraction(-1,2)
    checks.append({"alpha": str(alpha), "c_prime": str(cp), "g_prime_over_g": str(Fraction(1,1)/alpha), "c_prime_g_prime_over_g": str(invariant)})

result={
    "iteration":"008-G4",
    "lane":"frozen-normalization",
    "success":True,
    "classification":"PASS_SCOPED_FROZEN_QGR_ACTION_CONVENTION_FIXES_SIGNED_C_GEOM_MINUS_ONE_HALF__ONLY_PRODUCT_C_GEOM_G_IS_NORMALIZATION_INVARIANT",
    "authoritative_input":"S2_connection = -2 S2_QGR",
    "frozen_cell_convention":"D=h partial; one coordinate four-cell volume h^4",
    "c_geom_frozen_signed":str(c_frozen),
    "c_geom_frozen_magnitude":"1/2",
    "convention_covariance_checks":checks,
    "key_results":[
        "In the already frozen QGR quadratic convention, exact coefficient matching gives a_cont=-kappa/(2 h^2), so signed c_geom=-1/2 (up to the repository curvature/action sign convention).",
        "This removes the previously unnamed geometric conversion factor inside the frozen convention; it does not determine kappa, h or g.",
        "Under a rescaling of the quadratic basis/action normalization, c_geom and g transform inversely and only their product is invariant.",
        "Therefore the physically meaningful scale ambiguity remains one dimensionless normalization combination; no g=1 inference is authorized."
    ]
}
with open("iter008-g4-frozen-normalization.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
print(json.dumps(result,sort_keys=True))
