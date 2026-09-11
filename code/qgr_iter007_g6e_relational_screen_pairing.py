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
def sym2(A):
 M=[[F(0) for _ in range(10)] for __ in range(10)]
 for col,(i,j) in enumerate(FIELDS):
  H=[[F(0) for _ in V] for __ in V];H[i][j]=1;H[j][i]=1
  if i==j:H[i][j]=1
  K=mm(mm(T(A),H),A)
  for row,(r,s) in enumerate(FIELDS):M[row][col]=K[r][s]
 return M
def arr(A):return np.array([[float(x) for x in r] for r in A],float)
def field_matrix(v):
 H=np.zeros((4,4))
 for x,(i,j) in zip(v,FIELDS):H[i,j]=x;H[j,i]=x
 return H

def screen_gram(B,k,u_raw):
 B=np.asarray(B,float);g=np.linalg.inv(B);k=np.asarray(k,float);u=np.asarray(u_raw,float)
 usq=float(u@g@u);assert usq>1e-10,usq
 u=u/np.sqrt(usq);uf=g@u
 K=B@k;omega=float(k@u);assert abs(omega)>1e-10
 n=K/omega-u;nf=g@n
 assert abs(u@g@u-1)<1e-9
 assert abs(n@g@n+1)<1e-8
 assert abs(u@g@n)<1e-8
 S=np.eye(4)-np.outer(u,uf)+np.outer(n,nf)
 qcon=B-np.outer(u,u)+np.outer(n,n)
 qcov=g-np.outer(uf,uf)+np.outer(nf,nf)
 assert np.linalg.norm(S@u)<1e-8 and np.linalg.norm(S@n)<1e-8
 TTs=[]
 for a in range(10):
  e=np.zeros(10);e[a]=1;H=field_matrix(e);Hs=S.T@H@S;tr=float(np.einsum('ab,ab',qcon,Hs));TT=Hs-0.5*qcov*tr;TTs.append(TT)
 M=np.zeros((10,10))
 for a in range(10):
  for b in range(10):M[a,b]=np.einsum('ab,cd,ac,bd',TTs[a],TTs[b],qcon,qcon)
 return M,{'u_sq':float(u@g@u),'n_sq':float(n@g@n),'u_dot_n':float(u@g@n),'omega':omega}

C=[[F(0 if i==j else 1) for j in V] for i in V]
ks=[[F(1),0,0,0],[1,1,1,-1],[1,2,3,F(-11,6)]]
u0=np.ones(4)
base=[]
for k in ks:
 H=arr(hessian(C,k));R=arr(gauge(k));N=null_space(H,rcond=1e-10);assert N.shape==(10,6)
 M,geo=screen_gram(arr(C),np.array(list(map(float,k))),u0)
 assert np.linalg.norm(M@R)<1e-7
 G=N.T@M@N;eig=np.linalg.eigvalsh(G);pos=eig[eig>1e-8]
 assert len(pos)==2,(eig,pos)
 assert np.min(pos)>0
 base.append({'k':list(map(str,k)),'physical_gram_eigenvalues':eig.tolist(),'positive_eigenvalues':pos.tolist(),'geometry':geo})

# Finite-frame covariance of the screen pairing. u transforms as the relational barycentric vector A^{-1}u.
AS=[
 [[1,F(1,5),0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
 [[F(6,5),0,F(1,8),0],[0,F(9,10),0,F(1,9)],[0,0,1,0],[0,0,0,F(11,10)]],
]
covdev=[]
for A in AS:
 A=[[F(x) for x in r] for r in A];Ai=inv(A);Af=arr(A);Aif=arr(Ai);S10=arr(sym2(A));B1=mm(mm(Ai,C),T(Ai));u1=Aif@u0
 for k in ks:
  k1=mv(T(A),k);M0,_=screen_gram(arr(C),np.array(list(map(float,k))),u0);M1,_=screen_gram(arr(B1),np.array(list(map(float,k1))),u1)
  dev=float(np.linalg.norm(M0-S10.T@M1@S10))
  covdev.append(dev)
assert max(covdev)<1e-7,max(covdev)
out={
 'lane':'RELATIONAL_SCREEN_PHYSICAL_PAIRING',
 'seed_barycentric_vector':'u_raw=(1,1,1,1), the unique S4-invariant sum of the four relational cover directions',
 'null_covectors_checked':len(ks),
 'physical_screen_rank':2,
 'base_cases':base,
 'finite_frame_covariance_cases':len(covdev),
 'max_pairing_covariance_error':max(covdev),
 'pairing_definition':'Normalize timelike u with G; for null k set K=G^{-1}k, omega=k.u, n=K/omega-u; project h to the 2D screen orthogonal to u and n, remove its screen trace, and use the positive double-screen contraction as the quotient norm.',
 'classification':'PASS_SCOPED_RELATIONAL_BARYCENTRIC_TIMELIKE_SCREEN_DEFINES_POSITIVE_GAUGE_INVARIANT_TWO_MODE_PAIRING_AND_IS_FINITE_FRAME_COVARIANT_ON_REGULAR_DOMAIN',
 'scientific_interpretation':'The positive generic local polarization pairing need not be the noncovariant Euclidean seed quotient norm. The B4 cell already supplies a unique S4-invariant relational barycentric timelike direction. Together with each null characteristic covector it defines a two-dimensional screen. The TT screen map annihilates derivative-gauge directions, has exactly rank two on the on-shell Hessian nullspace, yields two positive eigenvalues, and is invariant under simultaneous finite frame transport of G,k,u,h.',
 'guard':'This is a local regular-cell one-particle/characteristic pairing conditional on the relational barycentric vector remaining timelike and on nonzero observed frequency k.u. It is not yet a global interacting BRST Hilbert inner product, and it introduces an observer/readout structure intrinsic to the relational cell rather than proving observer-independent particle splitting on arbitrary curved backgrounds.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
