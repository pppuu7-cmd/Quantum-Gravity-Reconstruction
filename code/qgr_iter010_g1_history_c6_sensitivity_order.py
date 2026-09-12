#!/usr/bin/env python3
import json

# Structural order bookkeeping from Iter009 G5:
# Delta X = h^2 A + c6 h^4 B + ...
# Any quadratic pairwise mixture-loss functional therefore has terms
# Q(Delta X,Delta X) = h^4 QAA + 2 c6 h^6 QAB + c6^2 h^8 QBB + ...
terms=[
 {'h_power':4,'c6_power':0,'label':'QAA'},
 {'h_power':6,'c6_power':1,'label':'2QAB'},
 {'h_power':8,'c6_power':2,'label':'QBB'},
]
leading=min(t['h_power'] for t in terms)
leading_c6=min(t['h_power'] for t in terms if t['c6_power']>0)
assert leading==4 and leading_c6==6
assert all(t['c6_power']==0 for t in terms if t['h_power']==4)
out={
 'gate':'ITER010-G1-HISTORY-C6-SENSITIVITY-ORDER',
 'branch_generator':'h^2 A + c6 h^4 B + ...',
 'quadratic_loss_terms':terms,
 'leading_loss_h_power':leading,
 'first_possible_branch_dependent_c6_h_power':leading_c6,
 'leading_h4_c6_sensitivity':0,
 'classification':'PASS_SCOPED_EXISTING_LEADING_OH4_HISTORY_MIXTURE_COMPARATOR_HAS_ZERO_C6_SENSITIVITY_AND_CANNOT_IDENTIFY_C6',
 'guard':'This does not exclude c6 sensitivity at O(h^6) in the mixture or O(h^4) in absolute coherent curved observables.'
}
print(json.dumps(out,sort_keys=True))
