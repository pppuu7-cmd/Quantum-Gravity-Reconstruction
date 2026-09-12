#!/usr/bin/env python3
import json
from fractions import Fraction

# In d=4 vacuum EH, to first order under
# delta g^{mu nu} = a R^{mu nu} + b g^{mu nu} R,
# delta S_EH is proportional to G_{mu nu} delta g^{mu nu}.
# Coefficients in basis (Ricci^2, R^2):
# (a, -(a/2+b)).
M = [[Fraction(1), Fraction(0)], [Fraction(-1,2), Fraction(-1)]]
det = M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert det == -1
rank = 2

out = {
    "gate": "ITER009-G2-CURVATURE-SQUARED-REDUNDANCY",
    "field_redefinition": "delta g^munu = a R^munu + b g^munu R",
    "map_to_basis_Ricci2_R2": [[str(x) for x in row] for row in M],
    "determinant": str(det),
    "rank": rank,
    "vacuum_four_derivative_physical_quotient_dimension_at_first_order": 0,
    "classification": "PASS_SCOPED_BOTH_PARITY_EVEN_CURVATURE_SQUARED_BULK_DIRECTIONS_ARE_EOM_REDUNDANT_FOR_PURE_VACUUM_EH_BRANCH_AT_FIRST_CORRECTION_ORDER",
    "guard": "Off-shell effective actions, matter couplings, boundaries, topology and measure Jacobians are not eliminated by this scoped on-shell vacuum field-redefinition result."
}
print(json.dumps(out, sort_keys=True))
