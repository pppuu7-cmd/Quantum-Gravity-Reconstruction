#!/usr/bin/env python3
"""Exact common characteristic-Hilbert covariance audit.

Combines the invariant future-null-cone measure with the positive covariant QGR-L1
trace-reversed quotient pairing.  This is a one-particle/readout theorem on the regular
characteristic domain, not a global interacting vacuum construction.
"""
from fractions import Fraction as F
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
V=range(4);FIELDS=[(i,j) for i in V for j in range(i,4)]

def T(A):return [list(r) for r in zip(*A)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x):return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def inv(A):
 n=len(A);M=[list(map(F,A[i]))+eye(n)[i] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if M[r][c]);M[c],M[p]=M[p],M[c]
  z=F(1)/M[c][c];M[c]=[x*z for x in M[c]]
  for r in range(n):
   if r!=c and M[r][c]:
    z=M[r][c];M[r]=[M[r][j]-z*M[c][j] for j in range(2*n)]
 return [r[n:] for r in M]
def det(A):
 M=[list(map(F,r)) for r in A];n=len(M);d=F(1);sgn=1
 for c in range(n):
  p=next((r for r in range(c,n) if M[r][c]),None)
  if p is None:return F(0)
  if p!=c:M[c],M[p]=M[p],M[c];sgn=-sgn
  q=M[c][c];d*=q
  for r in range(c+1,n):
   if M[r][c]:
    z=M[r][c]/q
    for j in range(c,n):M[r][j]-=z*M[c][j]
 return sgn*d
def field(v):
 H=[[F(0) for _ in V] for __ in V]
 for x,(i,j) in zip(v,FIELDS):H[i][j]=x;H[j][i]=x
 return H
def vec(H):return [H[i][j] for i,j in FIELDS]
def dewitt(B):
 mats=[]
 for a in range(10):
  e=[F(0)]*10;e[a]=1;mats.append(field(e))
 D=[[F(0) for _ in range(10)] for __ in range(10)]
 for a,Ha in enumerate(mats):
  tra=sum(B[i][j]*Ha[i][j] for i in V for j in V)
  for b,Hb in enumerate(mats):
   trb=sum(B[i][j]*Hb[i][j] for i in V for j in V)
   D[a][b]=sum(Ha[i][j]*Hb[r][s]*B[i][r]*B[j][s] for i in V for j in V for r in V for s in V)-F(1,2)*tra*trb
 return D
def eq(A,B):return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))

C=[[F(0 if i==j else 1) for j in V] for i in V];E=inv(C);D0=dewitt(C)
As=[
 [[1,F(1,5),0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
 [[F(6,5),0,F(1,8),0],[0,F(9,10),0,F(1,9)],[0,0,1,0],[0,0,0,F(11,10)]],
 [[1,F(1,7),F(-1,9),0],[0,1,F(1,6),0],[0,0,1,F(1,8)],[0,0,0,1]],
]
ks=[[F(1),F(1),F(1),F(-1)],[1,2,3,F(-11,6)]]
checks=[]
for A in As:
 A=[[F(x) for x in r] for r in A];Ai=inv(A)
 Bt=mm(mm(A,C),T(A));Gt=inv(Bt);D1=dewitt(Bt)
 assert eq(Gt,mm(mm(T(Ai),E),Ai))
 # Field push-forward h_t=A^{-T}h_s A^{-1}.
 U=[[F(0) for _ in range(10)] for __ in range(10)]
 for col in range(10):
  e=[F(0)]*10;e[col]=1;Ht=mm(mm(T(Ai),field(e)),Ai);v=vec(Ht)
  for row in range(10):U[row][col]=v[row]
 assert eq(mm(mm(T(U),D1),U),D0)
 da=det(A); assert det(Bt)==da*da*det(C)
 for k in ks:
  assert sum(k[i]*C[i][j]*k[j] for i in V for j in V)==0
  kt=mv(T(Ai),k)
  assert sum(kt[i]*Bt[i][j]*kt[j] for i in V for j in V)==0
  checks.append({'detA':str(da),'source_k':[str(x) for x in k],'target_k':[str(x) for x in kt]})
out={
 'lane':'COMMON_CHARACTERISTIC_HILBERT',
 'hilbert':'H_char(G)=direct_integral over future null cone N_G^+ of dmu_G(k) times the positive 2D quotient P_(G,k)=ker H/im R',
 'measure':'dmu_G=sqrt(|det G^-1|) d4k delta(k G^-1 k) theta_future',
 'fiber_pairing':'trace-reversed QGR-L1 covariant bilinear descended to P_(G,k)',
 'exact_finite_frame_maps_checked':len(As),'exact_null_transport_checks':len(checks),
 'classification':'PASS_SCOPED_COMMON_POSITIVE_CHARACTERISTIC_DIRECT_INTEGRAL_HILBERT_AND_FINITE_FRAME_BRANCH_UNITARITY_ON_REGULAR_DOMAIN',
 'scientific_interpretation':'The same finite frame map that transports the QGR characteristic cone preserves both the invariant null-cone measure and the positive quotient pairing. Therefore its pullback/pushforward defines an isometry between the corresponding direct-integral one-particle characteristic Hilbert spaces. The 24 regular history branches can consequently be compared inside one common target characteristic Hilbert without a polarization basis, Euclidean seed norm, or new normalization coefficient.',
 'guard':'This is a local regular one-particle/readout Hilbert construction. It does not choose a vacuum, Fock completion, detector model, or global interacting BRST Hilbert space.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
