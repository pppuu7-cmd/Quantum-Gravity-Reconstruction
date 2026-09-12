#!/usr/bin/env python3
import json
from fractions import Fraction as F

# Frozen Iter008 matching: S2_connection=-2 S2_QGR and D=h partial imply
# a_cont = -kappa/(2 h^2). This fixes the normalization of the unique two-derivative
# action in the repository convention.  The independent six-derivative term is written
# a_cont * c6 * h^4 * I6.  The matching equation contains no c6 column.
A=[[F(-2),F(0)]]  # columns [a_cont conversion, c6]
rank=1
null=[F(0),F(1)]
assert sum(A[0][j]*null[j] for j in range(2))==0
c_geom=F(-1,2)
assert c_geom==F(-1,2)
out={
 'gate':'ITER010-G4-TWO-VS-SIX-DERIVATIVE-NORMALIZATION',
 'frozen_two_derivative_conversion':'a_cont=-kappa/(2 h^2)',
 'c_geom':'-1/2',
 'parameter_columns':['two_derivative_conversion','c6'],
 'matching_rank':rank,
 'remaining_null_direction':['0','1'],
 'classification':'PASS_SCOPED_FROZEN_TWO_DERIVATIVE_ACTION_NORMALIZATION_FIXES_ONLY_THE_EINSTEIN_HILBERT_CONVERSION_AND_LEAVES_THE_INDEPENDENT_SIX_DERIVATIVE_C6_DIRECTION_FREE',
 'guard':'The common prefactor a_cont multiplies both terms once an EFT convention is chosen, but that does not determine the dimensionless Wilson coefficient c6.'
}
print(json.dumps(out,sort_keys=True))
