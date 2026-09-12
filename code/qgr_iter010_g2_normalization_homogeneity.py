#!/usr/bin/env python3
import json
from fractions import Fraction as F

# Represent a candidate six-derivative finite-cell term by one coefficient lambda.
# Existing relevant constraints at this stage are homogeneous in that term:
# S4 invariance, parity evenness, vanishing on the flat/conformally-flat continuum background,
# correct derivative/scaling class, and linear homogeneous refinement covariance.
# If I6 satisfies them, lambda*I6 does as well.  Their sensitivity rows therefore have zero
# nonhomogeneous normalization content.
homogeneous_rows=[F(0),F(0),F(0),F(0),F(0)]
assert all(x==0 for x in homogeneous_rows)
free_dimension=1
# One absolute microscopic equation A*lambda=b with A!=0 is sufficient to fix the scalar.
A=F(3,2); b=F(5,7); lam=b/A
assert A*lam==b
out={
 'gate':'ITER010-G2-NORMALIZATION-HOMOGENEITY',
 'candidate_coefficient_dimension':1,
 'existing_homogeneous_constraint_count':len(homogeneous_rows),
 'normalization_rank_from_homogeneous_constraints':0,
 'remaining_normalization_dimension':free_dimension,
 'example_nonhomogeneous_absolute_match':{'A':'3/2','b':'5/7','lambda':str(lam)},
 'classification':'BLOCKED_SCOPED_EXISTING_SYMMETRY_SCALING_AND_HOMOGENEOUS_REFINEMENT_REQUIREMENTS_CANNOT_FIX_THE_OVERALL_SIX_DERIVATIVE_FINITE_CELL_NORMALIZATION',
 'guard':'A genuine nonhomogeneous absolute microscopic action/EOM/phase normalization condition could fix the coefficient; none is supplied by this lane.'
}
print(json.dumps(out,sort_keys=True))
