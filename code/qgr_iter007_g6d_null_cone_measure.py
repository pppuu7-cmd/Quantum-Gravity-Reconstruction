#!/usr/bin/env python3
from fractions import Fraction as F
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()

def T(A):return [list(r) for r in zip(*A)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x):return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def inv(A):
 n=len(A);M=[list(A[i])+eye(n)[i] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if M[r][c]);M[c],M[p]=M[p],M[c]
  z=F(1)/M[c][c];M[c]=[x*z for x in M[c]]
  for r in range(n):
   if r!=c and M[r][c]:
    z=M[r][c];M[r]=[M[r][j]-z*M[c][j] for j in range(2*n)]
 return [r[n:] for r in M]
def det(A):
 M=[list(r) for r in A];n=len(M);d=F(1);sgn=1
 for c in range(n):
  p=next((r for r in range(c,n) if M[r][c]),None)
  if p is None:return F(0)
  if p!=c:M[c],M[p]=M[p],M[c];sgn*=-1
  q=M[c][c];d*=q
  for r in range(c+1,n):
   if M[r][c]:
    z=M[r][c]/q
    for j in range(c,n):M[r][j]-=z*M[c][j]
 return d*sgn

C=[[F(0 if i==j else 1) for j in range(4)] for i in range(4)]
B=inv(C)
AS=[
 [[F(2),0,F(1),F(1)],[0,F(1,2),F(-1,2),F(-1,2)],[0,0,1,0],[0,0,0,1]],
 [[F(3,2),F(1,4),0,0],[0,F(4,3),0,0],[0,0,F(5,4),F(1,7)],[0,0,0,F(6,5)]],
 [[1,F(1,3),0,F(1,5)],[0,1,F(1,4),0],[0,0,1,F(1,6)],[0,0,0,1]],
]
KS=[[F(1),F(1),F(1),0],[1,1,0,1],[1,0,1,1]]
checks=[]
for A in AS:
 A=[[F(x) for x in r] for r in A];Ai=inv(A)
 # vector metric relation G_s=A^T G_t A -> contravariant B_t=A B_s A^T
 Bt=mm(mm(A,B),T(A))
 da=det(A); db=det(B); dbt=det(Bt)
 assert dbt==da*da*db
 for k in KS:
  k=[F(x) for x in k]
  q=sum(k[i]*B[i][j]*k[j] for i in range(4) for j in range(4))
  if q!=0:continue
  kt=mv(T(Ai),k) # A^{-T} k
  qt=sum(kt[i]*Bt[i][j]*kt[j] for i in range(4) for j in range(4))
  assert qt==0
  checks.append({'detA':str(da),'source_null':list(map(str,k)),'target_null':list(map(str,kt))})
# Density sqrt(|det B|) d4k delta(k B k): sqrt(det Bt)=|det A|sqrt(det B),
# while d4k_t=|det A|^-1 d4k_s and the delta argument is invariant.
out={
 'lane':'NULL_CONE_MEASURE',
 'exact_frame_maps_checked':len(AS),
 'exact_null_transport_checks':len(checks),
 'determinant_identity':'det(B_target)=det(A)^2 det(B_source)',
 'measure':'dmu_G(k)=sqrt(|det G^{-1}|) d^4k delta(k^T G^{-1} k) theta_future(k)',
 'jacobian_cancellation':'sqrt(|det B_target|) contributes |det A| while d^4k_target contributes |det A|^-1; the quadratic delta argument is exactly invariant',
 'classification':'PASS_SCOPED_CANONICAL_LORENTZIAN_NULL_CONE_DENSITY_IS_INVARIANT_UNDER_QGR_FINITE_METRIC_ISOMETRY_TRANSPORT',
 'scientific_interpretation':'The target characteristic bundle has a natural frame-independent scalar integration density constructed only from the already-derived Lorentzian response metric. Thus differing branch-transported momenta can be represented in one common target null-cone measure space without choosing a polarization basis or a preferred coordinate frame.',
 'guard':'Future-cone selection uses the already existing causal orientation and is not re-derived here. This measure does not supply the missing positive generic curved polarization-fiber inner product.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
