#!/usr/bin/env python3
"""Exact audit of the C versus C^{-1} convention bridge.

This does NOT silently declare the microscopic B4 torsion construction invariant under a
continuous generator mixing.  It separates the continuum congruence statement from the
microscopic rerun requirement.
"""
from fractions import Fraction as F
import itertools,json,argparse
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
N=4

def T(A): return [list(r) for r in zip(*A)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x): return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def inv(A):
 n=len(A);M=[list(map(F,A[i]))+eye(n)[i] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if M[r][c]);M[c],M[p]=M[p],M[c]
  z=F(1)/M[c][c];M[c]=[x*z for x in M[c]]
  for r in range(n):
   if r!=c and M[r][c]:
    z=M[r][c];M[r]=[M[r][j]-z*M[c][j] for j in range(2*n)]
 return [r[n:] for r in M]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def det(A):
 A=[list(map(F,r)) for r in A];n=len(A);out=F(1);sgn=1
 for c in range(n):
  p=next((r for r in range(c,n) if A[r][c]),None)
  if p is None:return F(0)
  if p!=c:A[c],A[p]=A[p],A[c];sgn=-sgn
  z=A[c][c];out*=z
  for j in range(c,n):A[c][j]/=z
  for r in range(c+1,n):
   if A[r][c]:
    q=A[r][c]
    for j in range(c,n):A[r][j]-=q*A[c][j]
 return sgn*out

J=[[F(1) for _ in range(N)] for __ in range(N)]
C=[[F(0 if i==j else 1) for j in range(N)] for i in range(N)]
E=inv(C)
S=[[F(int(i==j))-F(1,6) for j in range(N)] for i in range(N)]
Si=inv(S)
assert eq(mm(mm(T(S),C),S),E)
assert eq(mm(mm(Si,E),T(Si)),C)

# S is S4-equivariant: it commutes with every permutation representation.
def perm_matrix(p):
 M=[[F(0) for _ in range(N)] for __ in range(N)]
 for j in range(N):M[p[j]][j]=1
 return M
commuting=0
for p in itertools.permutations(range(N)):
 Pm=perm_matrix(p)
 assert eq(mm(S,Pm),mm(Pm,S));commuting+=1

k_old=[F(1),F(1),F(1),F(0)]
k_new=mv(T(S),k_old)
q_old=sum(k_old[i]*E[i][j]*k_old[j] for i in range(N) for j in range(N))
q_new=sum(k_new[i]*C[i][j]*k_new[j] for i in range(N) for j in range(N))
assert q_old==q_new==0
assert k_new==[F(1,2),F(1,2),F(1,2),F(-1,2)]

# The old and repaired continuum quadratic forms/Gram scalars are exactly congruent.
# This is a coordinate statement only; the microscopic torsion equations must still be rerun.
xs=[
 [F(1),F(2),F(-1),F(3)],
 [F(2),F(-1),F(4),F(1)],
]
congruence_checks=[]
for x in xs:
 y=mv(T(S),x)
 qo=sum(x[i]*E[i][j]*x[j] for i in range(N) for j in range(N))
 qn=sum(y[i]*C[i][j]*y[j] for i in range(N) for j in range(N))
 assert qo==qn
 congruence_checks.append(str(qo))

# Conjugating the known o(C) basis gives an exact o(E) basis.  The linearized
# discrete torsion map remains full rank 24 with the same determinant 11664.
BC=[
 [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
 [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
 [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
 [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
 [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
 [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
]
BC=[[[F(z) for z in r] for r in X] for X in BC]
BE=[mm(mm(Si,X),S) for X in BC]
Z=[[F(0) for _ in range(N)] for __ in range(N)]
for X in BE:
 lhs=[[mm(T(X),E)[i][j]+mm(E,X)[i][j] for j in range(N)] for i in range(N)]
 assert eq(lhs,Z)
rows=[]
for i in range(N):
 for j in range(i+1,N):
  for a in range(N):
   row=[]
   for d in range(N):
    for X in BE:
     z=F(0)
     if d==i:z+=X[a][j]
     if d==j:z-=X[a][i]
     row.append(z)
   rows.append(row)
D=det(rows)
assert D==11664

out={
 'lane':'C_E_CONVENTION_BRIDGE',
 'C':'J-I',
 'E':'C^-1=-I+J/3',
 'S':'I-J/6',
 'identity':'S^T C S = E and S^-1 E S^-T = C',
 'S4_commuting_permutations':commuting,
 'old_g6d_null_covector':['1','1','1','0'],
 'mapped_qgr_l1_null_covector':[str(x) for x in k_new],
 'old_and_new_null_forms':str(q_old),
 'oE_basis_dimension':6,
 'repaired_linear_torsion_map_rank':24,
 'repaired_linear_torsion_determinant':str(D),
 'classification':'PASS_SCOPED_CONTINUUM_C_E_CONGRUENCE_AND_LINEAR_TORSION_RANK_SURVIVE__MICROSCOPIC_FINITE_CURVATURE_RERUN_REQUIRED',
 'scientific_interpretation':'The Iter005 characteristic convention G_down=E=C^-1 and the later C-based Lorentzian frame convention are related by a fixed S4-equivariant congruence. This explains why the old G6D null cone is not unrelated to QGR-L1. However S mixes the four microscopic B4 directions continuously and is not a Boolean-poset automorphism, so this algebraic bridge alone cannot certify the finite torsion/history calculations. Those must be rerun with covariant seed E and inverse characteristic form C.',
 'claim_guard':'Do not use this congruence to relabel the old microscopic G9 run as repaired. It validates only the continuum/index bridge and the exact linear torsion rank certificate.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
