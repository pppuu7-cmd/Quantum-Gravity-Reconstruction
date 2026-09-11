#!/usr/bin/env python3
from fractions import Fraction as F
from collections import defaultdict
import argparse,itertools,json
import numpy as np
from scipy.linalg import null_space
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
V=range(4);FIELDS=[(i,j) for i in V for j in range(i,4)];FI={f:i for i,f in enumerate(FIELDS)}

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
def gamma(mu,beta,rho):
 return [(1,mu,FI[tuple(sorted((beta,rho)))]),(1,beta,FI[tuple(sorted((mu,rho)))]),(-1,rho,FI[tuple(sorted((mu,beta)))])]
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
def sym2(A):
 M=[[F(0) for _ in range(10)] for __ in range(10)]
 for col,(i,j) in enumerate(FIELDS):
  H=[[F(0) for _ in V] for __ in V];H[i][j]=1;H[j][i]=1
  if i==j:H[i][j]=1
  K=mm(mm(T(A),H),A)
  for row,(r,s) in enumerate(FIELDS):M[row][col]=K[r][s]
 return M
def arr(A):return np.array([[float(x) for x in r] for r in A],float)
def physical_basis(H,R):
 N=null_space(H,rcond=1e-10) # 10x6
 Qg=np.linalg.qr(R)[0][:,:4]
 X=(np.eye(10)-Qg@Qg.T)@N
 U,s,_=np.linalg.svd(X,full_matrices=False)
 P=U[:,s>1e-8]
 assert P.shape==(10,2),(P.shape,s)
 assert np.linalg.norm(P.T@P-np.eye(2))<1e-10
 return P,Qg

C=[[F(0 if i==j else 1) for j in V] for i in V]
AS=[
 [[1,F(1,5),0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
 [[F(6,5),0,F(1,8),0],[0,F(9,10),0,F(1,9)],[0,0,1,0],[0,0,0,F(11,10)]],
]
KS=[[F(1),0,0,0],[1,1,1,-1]]
rows=[]
for A in AS:
 A=[[F(x) for x in r] for r in A];Ai=inv(A);B1=mm(mm(Ai,C),T(Ai));S=arr(sym2(A));AT=T(A)
 for k in KS:
  k=[F(x) for x in k];k1=mv(AT,k)
  H0=arr(hessian(C,k));R0=arr(gauge(k));H1=arr(hessian(B1,k1));R1=arr(gauge(k1))
  P0,Qg0=physical_basis(H0,R0);P1,Qg1=physical_basis(H1,R1)
  Y=S@P0
  assert np.linalg.norm(H1@Y)<1e-8
  Ymin=(np.eye(10)-Qg1@Qg1.T)@Y
  M=P1.T@Ymin
  G=M.T@M
  eig=np.linalg.eigvalsh(G)
  dev=float(np.linalg.norm(G-np.eye(2)))
  rows.append({'quotient_norm_gram_eigenvalues':eig.tolist(),'frobenius_deviation_from_isometry':dev})
assert max(r['frobenius_deviation_from_isometry'] for r in rows)>0.05
out={
 'lane':'SEED_EUCLIDEAN_QUOTIENT_NORM_COVARIANCE',
 'cases':rows,
 'maximum_deviation_from_isometry':max(r['frobenius_deviation_from_isometry'] for r in rows),
 'classification':'FAIL_SCOPED_SEED_EUCLIDEAN_MINIMAL_REPRESENTATIVE_QUOTIENT_NORM_IS_NOT_COVARIANT_UNDER_GENERIC_FINITE_QGR_FRAME_PULLBACK',
 'scientific_interpretation':'The positive Euclidean quotient norm used legitimately on the symmetric B4 seed does not transport as an isometry under generic finite frame pullbacks. Thus it cannot be promoted silently to the generic curved one-particle polarization norm. G6C gives a canonical linear isomorphism of physical quotient fibers, but not yet a canonical positive Hermitian pairing on those fibers.',
 'consequence':'A vector-Hilbert branch-overlap purity calculation on generic curved fibers remains blocked until a positive covariant physical pairing is derived. Operational positivity of physical states from G8D remains valid and is the authoritative positive-state structure meanwhile.',
 'guard':'This is a scoped failure of one candidate norm, not a no-go theorem for existence of a positive curved physical pairing.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
