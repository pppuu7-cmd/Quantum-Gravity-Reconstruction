#!/usr/bin/env python3
import json

# Let the branch-relative generator difference have the same-realization expansion
# dX = h^2 A + c6 h^4 B + ... .  Any leading purity/overlap loss quadratic in dX
# has schematic Q(dX,dX).  The powers are therefore h^4, c6 h^6, c6^2 h^8.
terms = [
    {"factor":"Q(A,A)","h_power":4,"c6_power":0},
    {"factor":"2 Q(A,B)","h_power":6,"c6_power":1},
    {"factor":"Q(B,B)","h_power":8,"c6_power":2},
]
assert min(t["h_power"] for t in terms if t["c6_power"]>0)==6

out={
    "gate":"ITER009-G5-HISTORY-LOSS-C6-ORDER",
    "branch_generator_expansion":"Delta X = h^2 Delta A + c6 h^4 Delta B + ...",
    "quadratic_loss_terms":terms,
    "leading_history_loss_order":"h^4",
    "first_c6_dependent_history_loss_order":"h^6",
    "classification":"PASS_SCOPED_IF_SELF_CONSISTENT_C6_GEOMETRY_CORRECTIONS_ENTER_BRANCH_GENERATORS_AT_OH4_THE_LEADING_QUADRATIC_HISTORY_MIXTURE_LOSS_AT_OH4_IS_C6_INDEPENDENT_AND_C6_FIRST_ENTERS_AT_OH6",
    "guard":"Requires the c6-induced branch-map correction to be regular O(h^4), with no singular 1/h enhancement or change of the leading h^2 branch-spread law."
}
print(json.dumps(out,sort_keys=True))
