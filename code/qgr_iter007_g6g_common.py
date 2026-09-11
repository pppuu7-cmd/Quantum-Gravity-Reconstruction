#!/usr/bin/env python3
"""Shared deterministic repaired-G9 finite-history helper for Iter007 G6G lanes."""
import itertools,math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
C=np.array([[0.,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])
E=np.linalg.inv(C);J=np.ones((4,4));S=np.eye(4)-J/6;Si=np.linalg.inv(S)
BC=np.array([
 [[-1,0,-1,-1],[0,1,1,1],[0,0,0,0],[0,0,0,0]],
 [[0,-1,1,0],[1,0,-1,0],[-1,1,0,0],[0,0,0,0]],
 [[-1,0,-1,-1],[-1,0,1,0],[1,0,1,1],[0,0,0,0]],
 [[-1,-1,-1,0],[1,1,1,0],[0,0,0,0],[-1,1,0,0]],
 [[-1,0,-2,0],[-1,0,1,0],[2,0,1,0],[-1,0,1,0]],
 [[1,0,2,0],[0,-1,-2,0],[-2,0,-1,0],[2,0,0,1]],
],float)
BASIS=np.array([Si@X@S for X in BC])
avec=np.array([0.22,-0.17,0.13,0.09]);Q=np.array([[0,0.05,-0.02,0.03],[0.05,0,0.04,-0.01],[-0.02,0.04,0,0.02],[0.03,-0.01,0.02,0]])
I=np.eye(4);PERMS=list(itertools.permutations(range(4)));u0=np.ones(4);u0sq=float(u0@E@u0);k0=np.array([1.,1.,1.,-1.])
# E-orthonormal Minkowski basis with source null contravariant vector along +z.
t=np.ones(4)*math.sqrt(3)/2;e1=np.array([1,-1,0,0])/math.sqrt(2);e2=np.array([1,1,-2,0])/math.sqrt(6);e3=np.array([1,1,1,-3])/math.sqrt(12)
RM=np.column_stack([t,e1,-e2,-e3]);ETA=np.diag([1.,-1.,-1.,-1.]);assert np.linalg.norm(RM.T@E@RM-ETA)<1e-12
Q0=ETA@(RM.T@k0);OMEGA0=float(Q0[0]);assert np.linalg.norm(Q0-OMEGA0*np.array([1.,0,0,1.]))<1e-12

def solve_paths(h):
 def Om(x):
  y=h*np.asarray(x,float);return math.exp(float(avec@y+0.5*y@Q@y))
 def L(z):return expm(np.tensordot(z,BASIS,axes=(0,0)))
 def residual(x,z):
  x=np.asarray(x,int);o=Om(x);Ls=[L(z[6*i:6*i+6]) for i in range(4)];out=[]
  for i in range(4):
   for j in range(i+1,4):
    xi=x.copy();xi[i]+=1;xj=x.copy();xj[j]+=1
    lhs=o*I[:,i]+np.linalg.solve(Ls[i],Om(xi)*I[:,j]);rhs=o*I[:,j]+np.linalg.solve(Ls[j],Om(xj)*I[:,i]);out.extend(lhs-rhs)
  return np.asarray(out)
 sols={};minsv=1e99;maxres=0.0
 for bits in itertools.product([0,1],repeat=4):
  s=least_squares(lambda z:residual(bits,z),np.zeros(24),xtol=1e-11,ftol=1e-11,gtol=1e-11,max_nfev=500)
  rn=float(np.linalg.norm(s.fun));assert rn<3e-9;maxres=max(maxres,rn);minsv=min(minsv,float(np.linalg.svd(s.jac,compute_uv=False).min()))
  sols[bits]=[L(s.x[6*i:6*i+6]) for i in range(4)]
 def edge(x,i):
  y=list(x);y[i]+=1;y=tuple(y);return (Om(x)/Om(y))*sols[tuple(x)][i]
 paths=[]
 for p in PERMS:
  x=[0,0,0,0];A=np.eye(4)
  for d in p:A=edge(tuple(x),d)@A;x[d]+=1
  paths.append(A)
 ot=Om((1,1,1,1));Lpaths=[ot*A for A in paths]
 assert max(np.linalg.norm(L.T@E@L-E) for L in Lpaths)<2e-8
 return {'h':h,'omega_target':ot,'A_paths':paths,'L_paths':Lpaths,'max_torsion_residual':maxres,'min_jacobian_singular':minsv}

def to_minkowski(L):
 Lam=np.linalg.inv(RM)@L@RM
 assert np.linalg.norm(Lam.T@ETA@Lam-ETA)<2e-8
 return Lam

def standard_null_map(q):
 """Canonical barycentric standard Lorentz map Q0 -> future null q."""
 w=float(q[0]);n=np.asarray(q[1:]/w,float);z=np.array([0.,0.,1.]);c=float(np.dot(z,n))
 if c>1-1e-12:R3=np.eye(3)
 elif c<-1+1e-12:R3=np.diag([1.,-1.,-1.])
 else:
  v=np.cross(z,n);s=np.linalg.norm(v);vx=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
  R3=np.eye(3)+vx+vx@vx*((1-c)/(s*s))
 Rot=np.eye(4);Rot[1:,1:]=R3
 rap=math.log(w/OMEGA0);ch,sh=math.cosh(rap),math.sinh(rap);B=np.eye(4);B[0,0]=B[3,3]=ch;B[0,3]=B[3,0]=sh
 out=Rot@B;assert np.linalg.norm(out@Q0-q)<2e-8
 return out

def branch_wigner_angles(Lpaths):
 angles=[];little=[]
 for L in Lpaths:
  Lam=to_minkowski(L);q=Lam@Q0;W=np.linalg.inv(standard_null_map(q))@Lam
  little.append(float(np.linalg.norm(W@Q0-Q0)))
  R2=W[1:3,1:3]
  theta=math.atan2(float(R2[1,0]-R2[0,1]),float(R2[0,0]+R2[1,1]))
  angles.append(theta)
 return np.asarray(angles),max(little)
