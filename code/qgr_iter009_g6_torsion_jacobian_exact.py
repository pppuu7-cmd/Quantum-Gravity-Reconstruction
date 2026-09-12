#!/usr/bin/env python3
import json
from fractions import Fraction

n=4
I=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
J=[[Fraction(1) for _ in range(n)] for _ in range(n)]
S=[[I[i][j]-J[i][j]/6 for j in range(n)] for i in range(n)]
Si=[[I[i][j]+J[i][j]/2 for j in range(n)] for i in range(n)]
BC=[
 [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
 [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
 [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
 [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
 [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
 [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
]
def mm(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
BASIS=[mm(mm(Si,[[Fraction(x) for x in r] for r in M]),S) for M in BC]
# At h=0,z=0, residual pair (i,j) linearization is -Z_i e_j + Z_j e_i.
rows=[]
for i in range(4):
 for j in range(i+1,4):
  for comp in range(4):
   row=[Fraction(0) for _ in range(24)]
   for a,B in enumerate(BASIS):
    row[6*i+a]-=B[comp][j]
    row[6*j+a]+=B[comp][i]
   rows.append(row)
def rank_q(A):
 A=[r[:] for r in A];m=len(A);n=len(A[0]);r=0
 for c in range(n):
  p=next((k for k in range(r,m) if A[k][c]),None)
  if p is None: continue
  A[r],A[p]=A[p],A[r];v=A[r][c];A[r]=[x/v for x in A[r]]
  for k in range(m):
   if k!=r and A[k][c]:
    f=A[k][c];A[k]=[A[k][q]-f*A[r][q] for q in range(n)]
  r+=1
  if r==m: break
 return r
rank=rank_q(rows)
assert len(rows)==24 and rank==24
out={
 'gate':'ITER009-G6-TORSION-JACOBIAN-EXACT',
 'jacobian_shape':[24,24],
 'exact_rational_rank':rank,
 'flat_solution':'h=0,z=0',
 'implicit_function_consequence':'the analytic torsion residual has a unique local analytic z(h) branch through the flat solution for each microscopic vertex chart',
 'classification':'PASS_SCOPED_EXACT_FULL_RANK_FLAT_TORSION_JACOBIAN_GIVES_LOCAL_UNIQUE_ANALYTIC_MICROSCOPIC_CONNECTION_BRANCH_NEAR_H0',
 'guard':'Local implicit-function control does not prove global uniqueness through strong-curvature singular points.'
}
print(json.dumps(out,sort_keys=True))
