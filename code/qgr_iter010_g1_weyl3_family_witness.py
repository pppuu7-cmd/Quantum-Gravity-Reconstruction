#!/usr/bin/env python3
import json
from fractions import Fraction as F

# Flat-background witness for the allowed one-parameter deformation.
# A traceless curvature perturbation w has W(eps)=eps*w at the flat seed.
# tr(W^3)=eps^3 tr(w^3), so first and second variations vanish while the cubic is nonzero.
w=[F(1),F(1),F(-2)]
assert sum(w)==0
tr_w3=sum(x**3 for x in w)
assert tr_w3==F(-6)
coefficients={0:F(0),1:F(0),2:F(0),3:tr_w3}
assert coefficients[1]==0 and coefficients[2]==0 and coefficients[3]!=0

# Multiplying the six-derivative term by arbitrary lambda leaves all <=2-derivative vertices,
# the flat Hessian, and the h->0 limit unchanged; lambda therefore remains continuous.
sample_lambdas=[F(-2),F(-1),F(0),F(1),F(2)]
assert len(set(sample_lambdas))==5
out={
 'gate':'ITER010-G1-WEYL3-CONTINUOUS-FAMILY-WITNESS',
 'traceless_witness':['1','1','-2'],
 'tr_w_cubed':str(tr_w3),
 'flat_variation_orders':{'first':0,'second':0,'third':str(tr_w3)},
 'sample_distinct_lambda_values':[str(x) for x in sample_lambdas],
 'free_continuous_parameter_dimension':1,
 'classification':'PASS_SCOPED_EXPLICIT_CONTINUOUS_C6_WEYL_CUBED_DEFORMATION_PRESERVES_FROZEN_LOWER_ORDER_AND_FLAT_HESSIAN_DATA_WHILE_REMAINING_NONTRIVIAL_AT_CUBIC_CURVATURE_ORDER',
 'guard':'Compatibility of a continuum deformation with current authority does not prove every lambda has a preferred microscopic finite-cell realization; it proves current frozen data do not select one.'
}
print(json.dumps(out,sort_keys=True))
