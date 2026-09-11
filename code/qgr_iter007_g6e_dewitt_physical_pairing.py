#!/usr/bin/env python3
"""Exact covariant positive pairing on the QGR-L1 massless physical quotient.

The bilinear is the trace-reversed symmetric-tensor contraction already selected by the
QGR-L1 kinetic structure.  We test that, on the characteristic kernel, the gauge image is
exactly radical and the remaining two directions are positive.  No observer/polarization
basis is selected.
"""
from fractions import Fraction as F
from collections import defaultdict
import argparse,itertools,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
V=range(4);FIELDS=[(i,j) for i in V for j in range(i,4)];FI={f:i for i,f in enumerate(FIELDS)}

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
def rref(A,ncols=None):
 A=[list(map(F,r)) for r in A];ncols=ncols or len(A[0]);r=0;piv=[]
 for c in range(ncols):
  p=next((i for i in range(r,len(A)) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];z=A[r][c];A[r]=[x/z for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:
    z=A[i][c];A[i]=[A[i][j]-z*A[r][j] for j in range(ncols)]
  piv.append(c);r+=1
  if r==len(A):break
 return A,piv
def rank(A):return len(rref(A,len(A[0]))[1]) if A else 0
def nullspace(A):
 rr,piv=rref(A,len(A[0]));free=[c for c in range(len(A[0])) if c not in piv];out=[]
 for f in free:
  v=[F(0)]*len(A[0]);v[f]=1
  for ri,p in enumerate(piv):v[p]=-rr[ri][f]
  out.append(v)
 return out
def rank_cols(cols):return rank([list(r) for r in zip(*cols)]) if cols else 0

def gamma(mu,beta,rho):return [(1,mu,FI[tuple(sorted((beta,rho)))]),(1,beta,FI[tuple(sorted((mu,rho)))]),(-1,rho,FI[tuple(sorted((mu,beta)))])]
def hessian(B,k):
 coeff=defaultdict(F)
 for mu,nu,a,b,r,s in itertools.product(V,repeat=6):
  pref=B[mu][nu]*B[a][r]*B[b][s]
  if not pref:continue
  for ov,A1,A2 in ((1,gamma(mu,b,r),gamma(nu,a,s)),(-1,gamma(mu,nu,r),gamma(a,b,s))):
   for s1,i,c in A1:
    for s2,j,d in A2:coeff[(c,d,i,j)]+=F(ov*s1*s2,4)*pref
 H=[[F(0) for _ in range(10)] for __ in range(10)]
 for (c,d,i,j),co in coeff.items():
  z=-co*k[i]*k[j]
  if c==d:H[c][c]+=2*z
  else:H[c][d]+=z;H[d][c]+=z
 return H
def gauge(k):
 R=[[F(0) for _ in V] for __ in range(10)]
 for a,(i,j) in enumerate(FIELDS):R[a][j]+=k[i];R[a][i]+=k[j]
 return R
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
   D[a][b]=sum(Ha[i][j]*Hb[r][s]*B[i][r]*B[j][s] for i,j,r,s in itertools.product(V,repeat=4))-F(1,2)*tra*trb
 return D
def bilin(D,x,y):return sum(x[i]*D[i][j]*y[j] for i in range(10) for j in range(10))
def mat_eq(A,B):return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def matadd(A,B):return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

C=[[F(0 if i==j else 1) for j in V] for i in V]
D=dewitt(C)
samples=[[F(1),0,0,0],[1,1,1,-1],[1,2,3,F(-11,6)],[2,-1,3,F(-1,4)]]
cases=[]
for k in samples:
 assert sum(k[i]*C[i][j]*k[j] for i in V for j in V)==0
 H=hessian(C,k);N=nullspace(H);R=gauge(k);Rcols=[[R[i][j] for i in range(10)] for j in V]
 assert len(N)==6 and rank_cols(Rcols)==4
 assert all(all(sum(H[i][j]*r[j] for j in range(10))==0 for i in range(10)) for r in Rcols)
 # The gauge image is the radical of the DeWitt form restricted to ker H.
 maxcross=F(0)
 for n in N:
  for r in Rcols:maxcross=max(maxcross,abs(bilin(D,n,r)))
 assert maxcross==0
 cols=Rcols[:];phys=[]
 for n in N:
  if rank_cols(cols+[n])>rank_cols(cols):
   cols.append(n)
   if len(cols)>4:phys.append(n)
  if len(cols)==6:break
 assert len(phys)==2
 G2=[[bilin(D,x,y) for y in phys] for x in phys]
 det2=G2[0][0]*G2[1][1]-G2[0][1]*G2[1][0]
 assert G2[0][0]>0 and det2>0
 # Rank of D on the six-dimensional characteristic kernel is exactly two.
 DN=[[bilin(D,x,y) for y in N] for x in N]
 assert rank(DN)==2
 cases.append({'k':[str(x) for x in k],'kernel_dim':6,'gauge_rank':4,'restricted_pairing_rank':2,'physical_gram':[[str(z) for z in r] for r in G2],'physical_gram_det':str(det2),'gauge_radical_cross_max':str(maxcross)})

# Exact finite-frame covariance for physical pushforward:
# B_t=A B_s A^T, k_t=A^{-T}k_s, h_t=A^{-T}h_s A^{-1}.
As=[
 [[1,F(1,5),0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
 [[F(6,5),0,F(1,8),0],[0,F(9,10),0,F(1,9)],[0,0,1,0],[0,0,0,F(11,10)]],
]
cov_checks=0
for A in As:
 A=[[F(x) for x in r] for r in A];Ai=inv(A);B1=mm(mm(A,C),T(A));D1=dewitt(B1)
 # coefficient map h -> A^{-T} h A^{-1}
 U=[[F(0) for _ in range(10)] for __ in range(10)]
 for col in range(10):
  e=[F(0)]*10;e[col]=1;H=field(e);Ht=mm(mm(T(Ai),H),Ai);v=vec(Ht)
  for row in range(10):U[row][col]=v[row]
 assert mat_eq(mm(mm(T(U),D1),U),D)
 for k in samples:
  k1=mv(T(Ai),k)
  q0=sum(k[i]*C[i][j]*k[j] for i in V for j in V);q1=sum(k1[i]*B1[i][j]*k1[j] for i in V for j in V)
  assert q0==q1==0
  cov_checks+=1

out={
 'lane':'DEWITT_PHYSICAL_PAIRING',
 'pairing':'<h,hprime> = h_mn hprime_rs B^mr B^ns - (1/2) tr_B(h) tr_B(hprime)',
 'null_samples_checked':len(cases),'cases':cases,'finite_frame_covariance_checks':cov_checks,
 'classification':'PASS_SCOPED_TRACE_REVERSED_COVARIANT_BILINEAR_DESCENDS_TO_POSITIVE_TWO_DIMENSIONAL_QGR_L1_CHARACTERISTIC_QUOTIENT',
 'scientific_interpretation':'On every tested exact QGR-L1 null covector, the ten-component Hessian kernel is six-dimensional, the four derivative-gauge directions form the exact radical of the trace-reversed covariant bilinear on that kernel, and the quotient has a strictly positive rank-two Gram form. The bilinear is exactly invariant under finite metric/frame pushforward. Hence the positive curved one-particle pairing does not require extending the noncovariant Euclidean seed norm or choosing a polarization basis. A TT screen relative to a timelike observer is only a representative/gauge realization of this quotient pairing.',
 'guard':'This is a local characteristic/on-shell physical pairing. It is not by itself a global interacting BRST Hilbert theorem, a choice of quantum vacuum, or a numerical experimental prediction.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
