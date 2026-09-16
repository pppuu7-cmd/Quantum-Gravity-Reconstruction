#!/usr/bin/env python3
"""Exact generic vacuum local-series engine for frozen Iter057AL candidate seeds."""
import math,time,json,sys
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import sympy as sp
from sympy.polys.matrices import DomainMatrix

K=F(2,25); ETA=(-1,1,1,1); ZERO=(0,0,0,0)
PAIRS=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]

def const(c):
 c=F(c); return {} if not c else {ZERO:c}
def mono(exp,c=1):
 c=F(c); return {} if not c else {tuple(exp):c}
def add(a,b):
 out=dict(a)
 for m,c in b.items():
  v=out.get(m,F(0))+c
  if v: out[m]=v
  elif m in out: del out[m]
 return out
def neg(a):return {m:-c for m,c in a.items()}
def sub(a,b):return add(a,neg(b))
def scale(a,c):
 c=F(c); return {} if not c else {m:c*v for m,v in a.items() if c*v}
def trunc(a,n):return {m:c for m,c in a.items() if sum(m)<=n and c}
def homog(a,n):return {m:c for m,c in a.items() if sum(m)==n and c}
def mul(a,b,n):
 out={}
 for m,c in a.items():
  for q,d in b.items():
   e=tuple(m[i]+q[i] for i in range(4))
   if sum(e)<=n: out[e]=out.get(e,F(0))+c*d
 return {m:c for m,c in out.items() if c}
def deriv(a,j):
 out={}
 for m,c in a.items():
  if m[j]:
   e=list(m);z=e[j];e[j]-=1;e=tuple(e);out[e]=out.get(e,F(0))+c*z
 return {m:c for m,c in out.items() if c}
def fact(a):return math.prod(math.factorial(x) for x in a)
def pmat():return [[{} for _ in range(4)] for _ in range(4)]
def madd(A,B):return [[add(A[i][j],B[i][j]) for j in range(4)] for i in range(4)]
def mscale(A,c):return [[scale(A[i][j],c) for j in range(4)] for i in range(4)]
def mmul(A,B,n):
 C=pmat()
 for i,j in product(range(4),repeat=2):
  v={}
  for r in range(4):v=add(v,mul(A[i][r],B[r][j],n))
  C[i][j]=trunc(v,n)
 return C
def eta_mat():
 E=pmat()
 for i in range(4):E[i][i]=const(ETA[i])
 return E
@lru_cache(None)
def alphas(n):return tuple(sorted(a for a in product(range(n+1),repeat=4) if sum(a)==n))
def pidx(a,b):
 if a>b:a,b=b,a
 return PAIRS.index((a,b))
def qrat(v):return sp.Rational(v.numerator,v.denominator)

def seed2(r):
 r=F(r); lam=(r,F(2)-r,F(-2));q={}
 for axis,c in enumerate(lam,1):
  ex=[0,0,0,0];ex[axis]=2;q=add(q,mono(ex,K*c))
 g=pmat()
 for a in range(4):g[a][a]=add(const(ETA[a]),scale(q,-1))
 return g,lam

def inverse(g,n):
 E=eta_mat();h=pmat()
 for a,b in product(range(4),repeat=2):
  h[a][b]=dict(g[a][b])
  if a==b:h[a][b]=sub(h[a][b],const(ETA[a]))
  h[a][b]=trunc(h[a][b],n)
 gi=E;T=mmul(mmul(E,h,n),E,n);sign=-1
 for power in range(1,n//2+1):
  if power>1:T=mmul(mmul(T,h,n),E,n)
  gi=madd(gi,mscale(T,sign));sign*=-1
 for a,b in product(range(4),repeat=2):gi[a][b]=trunc(gi[a][b],n)
 ok=True
 for a,b in product(range(4),repeat=2):
  v={}
  for c in range(4):v=add(v,mul(g[a][c],gi[c][b],n))
  if trunc(sub(v,const(1 if a==b else 0)),n):ok=False
 return gi,ok

def geometry(g,n):
 gi,invok=inverse(g,n);G=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
 for a,b,c in product(range(4),repeat=3):
  v={}
  for d in range(4):
   u=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)));v=add(v,mul(gi[a][d],u,n+1))
  G[a][b][c]=scale(trunc(v,n+1),F(1,2))
 Ric=pmat()
 for b,d in product(range(4),repeat=2):
  v={}
  for a in range(4):
   v=add(v,sub(deriv(G[a][d][b],a),deriv(G[a][a][b],d)))
   for e in range(4):v=add(v,sub(mul(G[a][a][e],G[e][d][b],n),mul(G[a][d][e],G[e][a][b],n)))
  Ric[b][d]=trunc(v,n)
 Sc={}
 for a,b in product(range(4),repeat=2):Sc=add(Sc,mul(gi[a][b],Ric[a][b],n))
 Sc=trunc(Sc,n);Ein=pmat()
 for a,b in product(range(4),repeat=2):Ein[a][b]=trunc(add(Ric[a][b],scale(mul(g[a][b],Sc,n),-F(1,2))),n)
 return gi,Ric,Sc,Ein,invok

def flat_gauge(g,n):
 h=pmat()
 for a,b in product(range(4),repeat=2):
  h[a][b]=dict(g[a][b])
  if a==b:h[a][b]=sub(h[a][b],const(ETA[a]))
 tr={}
 for a in range(4):tr=add(tr,scale(h[a][a],ETA[a]))
 hb=pmat()
 for a,b in product(range(4),repeat=2):
  hb[a][b]=dict(h[a][b])
  if a==b:hb[a][b]=add(hb[a][b],scale(tr,-F(ETA[a],2)))
 out=[]
 for b in range(4):
  v={}
  for a in range(4):v=add(v,scale(deriv(hb[a][b],a),ETA[a]))
  out.append(trunc(v,n))
 return out

def add_rbar_layer(g,d,vec):
 p=d//2;ads=alphas(d);rb=pmat()
 for idx,v in enumerate(vec):
  if not v:continue
  a,b=PAIRS[idx//len(ads)];al=ads[idx%len(ads)];vf=F(int(v.p),int(v.q)) if isinstance(v,sp.Rational) else F(v);term=mono(al,K**p*vf/F(fact(al)))
  rb[a][b]=add(rb[a][b],term)
  if a!=b:rb[b][a]=add(rb[b][a],term)
 tr={}
 for a in range(4):tr=add(tr,scale(rb[a][a],ETA[a]))
 r=pmat()
 for a,b in product(range(4),repeat=2):
  r[a][b]=dict(rb[a][b])
  if a==b:r[a][b]=add(r[a][b],scale(tr,-F(ETA[a],2)))
  g[a][b]=add(g[a][b],r[a][b])
 return r

@lru_cache(None)
def build_system(d):
 af=alphas(d-2);ag=alphas(d-1);au=alphas(d);col={(p,a):p*len(au)+j for p in range(10) for j,a in enumerate(au)};rows=[];meta=[]
 for b in range(4):
  for al in ag:
   dd={}
   for a in range(4):
    be=list(al);be[a]+=1;be=tuple(be);j=col[(pidx(a,b),be)];dd[j]=dd.get(j,0)+sp.Integer(ETA[a])
   rows.append(dd);meta.append(('G',b,al))
 for pair in PAIRS:
  for al in af:
   dd={}
   for m in range(4):
    be=list(al);be[m]+=2;be=tuple(be);j=col[(pidx(*pair),be)];dd[j]=dd.get(j,0)-sp.Rational(ETA[m],2)
   rows.append(dd);meta.append(('F',pair,al))
 M=sp.MutableSparseMatrix(len(rows),10*len(au),{(i,j):v for i,dd in enumerate(rows) for j,v in dd.items() if v})
 return M,rows,meta,af,ag,au

def bianchi(rows,meta,rhs,d):
 ab=alphas(d-3);lookup={m:i for i,m in enumerate(meta)};comps=[];ann=True
 for b in range(4):
  for beta in ab:
   combo={};val=sp.Rational(0)
   for m in range(4):
    al=list(beta);al[m]+=2;i=lookup[('G',b,tuple(al))];c=sp.Rational(ETA[m],2);val+=c*rhs[i]
    for j,x in rows[i].items():combo[j]=combo.get(j,0)+c*x
   for a in range(4):
    al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a);i=lookup[('F',pair,tuple(al))];c=sp.Integer(ETA[a]);val+=c*rhs[i]
    for j,x in rows[i].items():combo[j]=combo.get(j,0)+c*x
   if any(x for x in combo.values()):ann=False
   comps.append(sp.factor(val))
 return ann,comps
