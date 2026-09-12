#!/usr/bin/env python3
import json
from fractions import Fraction as F

# Let a prospective six-derivative cell contribution be lambda I6(cell).  Any exact additive
# refinement statement has the form lambda*(I_parent - sum I_child)=0. It is homogeneous
# in lambda. If the geometric discretization satisfies the refinement identity, every lambda
# survives; if it does not, the only algebraic solution is lambda=0, which kills the operator
# rather than selecting a nonzero normalization. Thus additivity alone cannot determine a
# unique nonzero c6.
examples=[
 {'delta':F(0),'allowed':'all_lambda'},
 {'delta':F(1,7),'allowed':'lambda_zero_only'},
 {'delta':F(-3,5),'allowed':'lambda_zero_only'}
]
assert examples[0]['delta']==0 and all(x['delta']!=0 for x in examples[1:])
out={
 'gate':'ITER010-G4-REFINEMENT-HOMOGENEITY',
 'equation':'c6 * (I6_parent - sum I6_children) = 0',
 'cases':[{'delta':str(x['delta']),'solution':x['allowed']} for x in examples],
 'classification':'BLOCKED_SCOPED_ADDITIVE_OR_HOMOGENEOUS_REFINEMENT_CONSISTENCY_CANNOT_SELECT_A_UNIQUE_NONZERO_C6_WITHOUT_AN_INDEPENDENT_NONHOMOGENEOUS_MICROSCOPIC_TARGET',
 'guard':'A future exact finite-cell action may contain cross-order or absolute normalization data that are nonhomogeneous in c6. No such rule is assumed here.'
}
print(json.dumps(out,sort_keys=True))
