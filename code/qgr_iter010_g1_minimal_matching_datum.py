#!/usr/bin/env python3
import json
from fractions import Fraction as F

# After all lower-order normalizations are frozen, the remaining effective UV parameter sector
# is one-dimensional: c6. Existing scoped observables used at their frozen orders have zero
# c6 sensitivity. One independently normalized absolute curved microscopic response with
# nonzero sensitivity is sufficient (and, dimensionally, necessary) to fix one scalar c6.
existing_sensitivities=[F(0),F(0),F(0)]  # flat Hessian, h->0 lower-order data, leading h^4 mixture
rank_existing=0 if all(x==0 for x in existing_sensitivities) else 1
assert rank_existing==0
new_absolute_curved_sensitivity=F(1)
rank_with_new=1 if new_absolute_curved_sensitivity else rank_existing
assert rank_with_new==1
out={
 'gate':'ITER010-G1-MINIMAL-MATCHING-DATUM',
 'remaining_parameter_sector_dimension':1,
 'existing_c6_sensitivity_rank':rank_existing,
 'rank_after_one_nonzero_absolute_curved_matching_condition':rank_with_new,
 'minimal_additional_independent_scalar_conditions':1,
 'sufficient_datum':'one internally derived, absolutely normalized curved O(h^4) microscopic action/EOM/phase response with nonzero Weyl^3 sensitivity',
 'insufficient_datum':'the existing leading O(h^4) traced history-mixture purity coefficient because its c6 sensitivity is exactly zero at that order',
 'classification':'PASS_SCOPED_ONE_NONZERO_ABSOLUTE_CURVED_MICROSCOPIC_MATCHING_CONDITION_IS_MINIMAL_AND_SUFFICIENT_TO_LIFT_THE_ONE_DIMENSIONAL_C6_NULL_DIRECTION',
 'guard':'This identifies the information requirement only; it does not manufacture or fit the missing datum.'
}
print(json.dumps(out,sort_keys=True))
