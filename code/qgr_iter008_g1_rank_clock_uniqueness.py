#!/usr/bin/env python3
import argparse,itertools,json
from fractions import Fraction as F
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# S4-invariant scalar f on B4 depends only on subset rank r=0..4.
# Impose f(empty)=0 and additivity f(r+s)=f(r)+f(s) whenever disjoint subsets of sizes r,s exist.
# Build exact linear system on f0..f4.
rows=[]
row=[F(0)]*5;row[0]=1;rows.append(row)
for r in range(5):
  for s in range(5-r):
    row=[F(0)]*5;row[r+s]+=1;row[r]-=1;row[s]-=1
    rows.append(row)

def rref(A):
 A=[x[:] for x in A if any(x)];m=len(A);n=5;i=0;piv=[]
 for j in range(n):
  p=next((k for k in range(i,m) if A[k][j]),None)
  if p is None:continue
  A[i],A[p]=A[p],A[i];q=A[i][j];A[i]=[x/q for x in A[i]]
  for k in range(m):
   if k!=i and A[k][j]:
    q=A[k][j];A[k]=[A[k][l]-q*A[i][l] for l in range(n)]
  piv.append(j);i+=1
 return A,piv
R,piv=rref(rows);null_dim=5-len(piv)
assert null_dim==1,(piv,null_dim)
# rank vector must solve all constraints and span the nullspace.
rank=[F(r) for r in range(5)]
assert all(sum(a*b for a,b in zip(row,rank))==0 for row in rows)
# Unit elementary increment fixes the remaining scale.
normalized=[0,1,2,3,4]
out={
 'lane':'BOOLEAN_RANK_CLOCK_UNIQUENESS',
 'S4_invariant_scalar_dimension_before_additivity':5,
 'additivity_constraint_rank':len(piv),
 'solution_dimension_after_f0_zero_and_disjoint_additivity':null_dim,
 'normalized_clock_values_by_rank':normalized,
 'classification':'PASS_SCOPED_BOOLEAN_RANK_IS_THE_UNIQUE_UNIT_INCREMENT_S4_INVARIANT_DISJOINT_ADDITIVE_SCALAR_CLOCK_ON_B4',
 'scientific_interpretation':'S4 invariance reduces any scalar on B4 to five rank values. Requiring zero at the empty event and additivity under disjoint union leaves exactly one degree of freedom, spanned by rank. Fixing one elementary cover to one clock tick gives tau(S)=|S|. This clock is derived from the existing ontology rather than inserted as a matter field.',
 'guard':'Uniqueness is within the stated S4-invariant additive scalar class. It does not yet make one rank tick a physical second or prove that this clock must be used by all matter.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))