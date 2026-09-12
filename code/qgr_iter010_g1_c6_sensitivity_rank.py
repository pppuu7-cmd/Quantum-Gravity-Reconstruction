#!/usr/bin/env python3
import json
from fractions import Fraction as F

# Columns are [already-fixed two-derivative normalization, c6].
# Rows encode the parameter sensitivity of frozen scoped authority:
#  - the two-derivative normalization fixes the first column;
#  - the flat Hessian has zero c6 sensitivity;
#  - the h->0 continuum limit kills h^4*c6 W^3;
#  - the leading O(h^4) history-mixture loss has zero c6 sensitivity (Iter009 G5).
A=[
 [F(1),F(0)],
 [F(2),F(0)],
 [F(0),F(0)],
 [F(0),F(0)],
]

def rank_q(M):
 M=[r[:] for r in M];m=len(M);n=len(M[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m) if M[i][c]),None)
  if p is None: continue
  M[r],M[p]=M[p],M[r];v=M[r][c];M[r]=[x/v for x in M[r]]
  for i in range(m):
   if i!=r and M[i][c]:
    q=M[i][c];M[i]=[M[i][j]-q*M[r][j] for j in range(n)]
  r+=1
 return r
rank=rank_q(A);nullity=2-rank
assert rank==1 and nullity==1
null_vector=[F(0),F(1)]
assert all(sum(row[j]*null_vector[j] for j in range(2))==0 for row in A)
out={
 'gate':'ITER010-G1-C6-SENSITIVITY-RANK',
 'parameter_columns':['two_derivative_normalization','c6'],
 'exact_rational_rank':rank,
 'nullity':nullity,
 'null_vector':['0','1'],
 'interpretation':'after the two-derivative normalization is fixed, all presently frozen flat/continuum/leading-history constraints leave the c6 direction exactly unconstrained',
 'classification':'PASS_SCOPED_EXACT_FROZEN_LOWER_ORDER_SENSITIVITY_MATRIX_HAS_ONE_DIMENSIONAL_C6_NULLSPACE',
 'guard':'The matrix summarizes only already-established scoped sensitivities; an additional absolute curved microscopic datum with nonzero c6 sensitivity can lift this null direction.'
}
print(json.dumps(out,sort_keys=True))
