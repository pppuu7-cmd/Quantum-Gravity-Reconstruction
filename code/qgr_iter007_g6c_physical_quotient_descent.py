#!/usr/bin/env python3
from fractions import Fraction as F
from collections import defaultdict
import argparse,itertools,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
V=range(4); FIELDS=[(i,j) for i in V for j in range(i,4)]; FINDEX={f:i for i,f in enumerate(FIELDS)}

def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def T(A):return [list(r) for r in zip(*A)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x):return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def inv(A):
 n=len(A);M=[list(A[i])+eye(n)[i] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if M[r][c]);M[c],M[p]=M[p],M[c]
  z=F(1)/M[c][c];M[c]=[x*z for x in M[c]]
  for r in range(n):
   if r!=c and M[r][c]:
    z=M[r][c];M[r]=[M[r][j]-z*M[c][j] for j in range(2*n)]
 return [r[n:] for r in M]
def rank(A):
 M=[list(r) for r in A];m=len(M);n=len(M[0]);rr=0
 for c in range(n):
  p=next((i for i in range(rr,m) if M[i][c]),None)
  if p is None:continue
  M[rr],M[p]=M[p],M[rr];z=F(1)/M[rr][c];M[rr]=[x*z for x in M[rr]]
  for i in range(m):
   if i!=rr and M[i][c]:
    z=M[i][c];M[i]=[M[i][j]-z*M[rr][j] for j in range(n)]
  rr+=1
 return rr
def nullspace(A):
 M=[list(r) for r in A];m=len(M);n=len(M[0]);rr=0;piv=[]
 for c in range(n):
  p=next((i for i in range(rr,m) if M[i][c]),None)
  if p is None:continue
  M[rr],M[p]=M[p],M[rr];z=F(1)/M[rr][c];M[rr]=[x*z for x in M[rr]]
  for i in range(m):
   if i!=rr and M[i][c]:
    z=M[i][c];M[i]=[M[i][j]-z*M[rr][j] for j in range(n)]
  piv.append(c);rr+=1
 free=[c for c in range(n) if c not in piv];out=[]
 for f in free:
  x=[F(0)]*n;x[f]=1
  for i,p in enumerate(piv):x[p]=-M[i][f]
  out.append(x)
 return out

C=[[F(0 if i==j else 1) for j in V] for i in V]
def gamma_terms(mu,beta,rho):
 return [(1,mu,FINDEX[tuple(sorted((beta,rho)))]),(1,beta,FINDEX[tuple(sorted((mu,rho)))]),(-1,rho,FINDEX[tuple(sorted((mu,beta)))])]
def hessian(B,k):
 coeff=defaultdict(F)
 for mu,nu,alpha,beta,rho,sigma in itertools.product(V,repeat=6):
  pref=B[mu][nu]*B[alpha][rho]*B[beta][sigma]
  if not pref:continue
  for overall,A1,A2 in ((1,gamma_terms(mu,beta,rho),gamma_terms(nu,alpha,sigma)),(-1,gamma_terms(mu,nu,rho),gamma_terms(alpha,beta,sigma))):
   for s1,i,c in A1:
    for s2,j,d in A2:coeff[(c,d,i,j)]+=F(overall*s1*s2,4)*pref
 H=[[F(0) for _ in range(10)] for __ in range(10)]
 for (c,d,i,j),co in coeff.items():
  v=-co*k[i]*k[j]
  if c==d:H[c][c]+=2*v
  else:H[c][d]+=v;H[d][c]+=v
 return H
def gauge(k):
 R=[[F(0) for _ in V] for __ in range(10)]
 for a,(i,j) in enumerate(FIELDS):R[a][j]+=k[i];R[a][i]+=k[j]
 return R
def sym2_map(A):
 M=[[F(0) for _ in range(10)] for __ in range(10)]
 for col,(i,j) in enumerate(FIELDS):
  H=[[F(0) for _ in V] for __ in V];H[i][j]=1;H[j][i]=1
  if i==j:H[i][j]=1
  K=mm(mm(T(A),H),A)
  for row,(r,s) in enumerate(FIELDS):M[row][col]=K[r][s]
 return M
def nullform(B,k):return sum(k[i]*B[i][j]*k[j] for i in V for j in V)

AS=[
 [[1,F(1,5),0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[F(1,7),1,F(1,6),0],[0,0,1,0],[0,0,0,1]],
 [[F(6,5),0,F(1,8),0],[0,F(9,10),0,F(1,9)],[0,0,1,0],[0,0,0,F(11,10)]],
]
AS=[[[F(x) for x in row] for row in A] for A in AS]
KS=[[F(1),0,0,0],[1,1,1,-1],[1,2,3,F(-11,6)]]
KS=[[F(x) for x in k] for k in KS]
checks=0
for A in AS:
 Ai=inv(A);B=mm(mm(Ai,C),T(Ai));S=sym2_map(A);AT=T(A)
 assert rank(S)==10
 for k0 in KS:
  assert nullform(C,k0)==0
  kp=mv(AT,k0); assert nullform(B,kp)==0
  H0=hessian(C,k0);Hp=hessian(B,kp);R0=gauge(k0);Rp=gauge(kp)
  assert rank(H0)==4 and rank(Hp)==4 and rank(R0)==4 and rank(Rp)==4
  assert mm(S,R0)==mm(Rp,AT)
  N0=nullspace(H0); assert len(N0)==6
  for n in N0:
   sn=mv(S,n); assert all(x==0 for x in mv(Hp,sn))
  checks+=1

out={
 'lane':'PHYSICAL_QUOTIENT_DESCENT',
 'rational_frame_maps_checked':len(AS),
 'null_covectors_per_map':len(KS),
 'exact_cases':checks,
 'old_and_new_hessian_rank_on_cone':4,
 'old_and_new_gauge_rank':4,
 'physical_quotient_dimension':2,
 'gauge_covariance_identity':'Sym2(A) R(k) = R(A^T k) A^T',
 'nullspace_covariance_verified_exactly':True,
 'classification':'PASS_SCOPED_FINITE_FRAME_PULLBACK_CANONICALLY_DESCENDS_TO_ISOMORPHISM_BETWEEN_TWO_DIMENSIONAL_QGR_L1_PHYSICAL_CHARACTERISTIC_QUOTIENT_FIBERS',
 'scientific_interpretation':'The two-mode readout need not be supplied by an arbitrary 2x2 projector. The already-derived tensor pullback on the 10-component response sends gauge directions to gauge directions and Hessian null spaces to Hessian null spaces when the background and characteristic covector are transformed together. Therefore it induces a canonical basis-independent map on ker(H)/im(R).',
 'guard':'This proves fiberwise quotient descent under finite frame changes on tested exact rational regular backgrounds. A curved history generally transports k along the branch, so comparing different histories in one common target momentum fiber still requires the wavepacket/bundle readout rule.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
