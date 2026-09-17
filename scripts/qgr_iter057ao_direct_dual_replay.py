#!/usr/bin/env python3
import argparse, hashlib, json, itertools
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
N=4
GENERIC='ITER057AO-COVARIANT-WEYL3-V1'
HELDOUT='ITER057AO-COVARIANT-WEYL3-HELDOUT-V1'
PREREG='e1ded07e5050763ecb707dad679b78286fe04744'
SOURCE_FREEZE='c1616a7ba5d540e14c667ad49c53f873ae21a0cc'

def q(seed,*idx,mod=11):
 b=(seed+':' + ':'.join(map(str,idx))).encode(); n=int(hashlib.sha256(b).hexdigest()[:16],16); return F((n%(2*mod+1))-mod,13)
def gd(seed,a,b,ders):
 if a>b:a,b=b,a
 ds=tuple(sorted(ders)); k=len(ds)
 if k==0:
  base=F(-1 if a==0 else 1) if a==b else F(0); return base+q(seed,'g',a,b,mod=2)/20
 if k==1:return q(seed,'dg',a,b,*ds,mod=4)/7
 if k==2:return q(seed,'ddg',a,b,*ds,mod=4)/9
 raise ValueError(k)
def hd(seed,a,b,ders):
 if a>b:a,b=b,a
 ds=tuple(sorted(ders)); k=len(ds)
 if k==0:return q(seed,'h',a,b,mod=5)
 if k==1:return q(seed,'dh',a,b,*ds,mod=4)/7
 if k==2:return q(seed,'ddh',a,b,*ds,mod=4)/9
 raise ValueError(k)
class D:
 __slots__=('v','e')
 def __init__(self,v=0,e=0):self.v=F(v);self.e=F(e)
 @staticmethod
 def c(x):return x if isinstance(x,D) else D(x)
 def __add__(self,o):o=D.c(o);return D(self.v+o.v,self.e+o.e)
 __radd__=__add__
 def __neg__(self):return D(-self.v,-self.e)
 def __sub__(self,o):return self+(-D.c(o))
 def __rsub__(self,o):return D.c(o)+(-self)
 def __mul__(self,o):o=D.c(o);return D(self.v*o.v,self.e*o.v+self.v*o.e)
 __rmul__=__mul__
 def inv(self):return D(1/self.v,-self.e/(self.v*self.v))
 def __truediv__(self,o):return self*D.c(o).inv()
 def __rtruediv__(self,o):return D.c(o)*self.inv()
def invmat(A):
 n=len(A); aug=[[D(A[i][j].v,A[i][j].e) for j in range(n)]+[D(int(i==j)) for j in range(n)] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if aug[r][c].v!=0)
  if p!=c:aug[c],aug[p]=aug[p],aug[c]
  z=aug[c][c]; aug[c]=[x/z for x in aug[c]]
  for r in range(n):
   if r==c:continue
   z=aug[r][c]
   if z.v or z.e:aug[r]=[aug[r][j]-z*aug[c][j] for j in range(2*n)]
 return [r[n:] for r in aug]
def det4(A):
 out=D()
 for p in itertools.permutations(range(4)):
  inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)); t=D(-1 if inv%2 else 1)
  for i in range(4):t=t*A[i][p[i]]
  out=out+t
 return out
def build(seed):
 g=[[D(gd(seed,a,b,()),hd(seed,a,b,())) for b in range(N)] for a in range(N)]
 dg=[[[D(gd(seed,a,b,(c,)),hd(seed,a,b,(c,))) for c in range(N)] for b in range(N)] for a in range(N)]
 dd=[[[[D(gd(seed,a,b,(c,d)),hd(seed,a,b,(c,d))) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
 gi=invmat(g)
 Ga=[[[ (dg[a][b][c]+dg[a][c][b]-dg[b][c][a])/2 for c in range(N)] for b in range(N)] for a in range(N)]
 R=[[[[D() for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
 for a,b,c,d in itertools.product(range(N),repeat=4):
  x=(dd[a][d][b][c]+dd[b][c][a][d]-dd[a][c][b][d]-dd[b][d][a][c])/2
  for e,f in itertools.product(range(N),repeat=2):x+=gi[e][f]*(Ga[e][a][d]*Ga[f][b][c]-Ga[e][a][c]*Ga[f][b][d])
  R[a][b][c][d]=x
 Ric=[[D() for d in range(N)] for b in range(N)]
 for b,d in itertools.product(range(N),repeat=2):Ric[b][d]=sum((gi[a][c]*R[a][b][c][d] for a,c in itertools.product(range(N),repeat=2)),D())
 Sc=sum((gi[b][d]*Ric[b][d] for b,d in itertools.product(range(N),repeat=2)),D())
 C=[[[[D() for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
 for a,b,c,d in itertools.product(range(N),repeat=4):C[a][b][c][d]=R[a][b][c][d]-(g[a][c]*Ric[d][b]-g[a][d]*Ric[c][b]-g[b][c]*Ric[d][a]+g[b][d]*Ric[c][a])/2+Sc*(g[a][c]*g[d][b]-g[a][d]*g[c][b])/6
 Cu=[[[[D() for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
 for a,b,c,d in itertools.product(range(N),repeat=4):Cu[a][b][c][d]=sum((gi[c][e]*gi[d][f]*C[a][b][e][f] for e,f in itertools.product(range(N),repeat=2)),D())
 Q=[[[[D() for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
 for a,b,c,d in itertools.product(range(N),repeat=4):Q[a][b][c][d]=sum((Cu[c][d][e][f]*Cu[e][f][a][b] for e,f in itertools.product(range(N),repeat=2)),D())
 I=sum((Cu[a][b][c][d]*Q[a][b][c][d] for a,b,c,d in itertools.product(range(N),repeat=4)),D()); det=det4(g)
 sq=sp.sqrt(-sp.Rational(det.v.numerator,det.v.denominator)); val=sp.simplify(sq*(sp.Rational(I.e.numerator,I.e.denominator)+sp.Rational(det.e.numerator,det.e.denominator)*sp.Rational(I.v.numerator,I.v.denominator)/(2*sp.Rational(det.v.numerator,det.v.denominator))))
 txt=str(val); return {'det_g':str(det.v),'det_directional':str(det.e),'I3':str(I.v),'dI3':str(I.e),'canonical_sympy':txt,'sha256':hashlib.sha256(txt.encode()).hexdigest(),'nonzero':val!=0}
def phash(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--seed',choices=['generic','heldout'],required=True);ap.add_argument('--output',required=True);a=ap.parse_args();seed=GENERIC if a.seed=='generic' else HELDOUT;d=build(seed)
 out={'gate':'ITER057AO','route':'INDEPENDENT_DIRECT_DUAL_NUMBER_FULL_TENSOR_PROPAGATION','preregistration':PREREG,'phase2_source_freeze':SOURCE_FREEZE,'seed':seed,'directional_density':d,'controls':{'metric_invertible':F(d['det_g'])!=0,'directional_nonzero':d['nonzero'],'no_explicit_metric_variation_formulas':True,'full_g_plus_epsilon_h_first_order_propagation':True,'no_floating_tolerance':True},'terminal_classification_authorized':False}
 out['scientific_payload_sha256']=phash(out);Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out,sort_keys=True,indent=2));return 0 if all(out['controls'].values()) else 2
if __name__=='__main__':raise SystemExit(main())
