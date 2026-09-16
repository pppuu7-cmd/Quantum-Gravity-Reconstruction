#!/usr/bin/env python3
import csv,json,math,hashlib,argparse
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import qgr_iter057z_dodecic_einstein_seed_completion as z

ROOT=Path(__file__).resolve().parents[1]; ETA=z.ETA; K=z.K; PAIRS=z.PAIRS
PREREG='0794406a04945b6b9999361c63d9f0964519ec30'
PASS='PASS_SCOPED_ITER057AC_TETRADECIC_EINSTEIN_SEED_COMPLETION_EXACT_THROUGH_DEGREE12'
R12=ROOT/'data'/'ITER057Z_CANONICAL_R12_NORMALIZED.csv'
R12_PREREG='f1c04bbfdb7848ab79708beb902ccdb315fbd5ed'; R12_SHA='e62c84d0ad586322d588093ddbf067c0ad185478a042e3c877d24e7809122c6b'

def read_csv(path,key):
 meta={}; body=[]
 for line in path.read_text().splitlines():
  if line.startswith('# ') and '=' in line[2:]: k,v=line[2:].split('=',1);meta[k]=v
  elif line.strip() and not line.startswith('#'): body.append(line)
 rows=[]
 for r in csv.DictReader(body): rows.append({'pair':[int(r['a']),int(r['b'])],'alpha':[int(r[x]) for x in 'txyz'],key:r[key]})
 return rows,meta

def seed12():
 g,prov,*_=z.canonical_seed10(); rows,meta=read_csv(R12,'R12_over_kappa6')
 _,pure=z.add_trace_reversed_layer(g,rows,6,'R12_over_kappa6',12)
 prov=prov and pure and len(rows)==469 and meta.get('preregistration')==R12_PREREG and meta.get('scientific_payload_sha256')==R12_SHA
 return g,prov,rows,meta

def inverse(g,n):
 E=z.eta_mat(); h=z.pmat()
 for a,b in product(range(4),repeat=2):
  h[a][b]=dict(g[a][b]);
  if a==b:h[a][b]=z.sub(h[a][b],z.const(ETA[a]))
  h[a][b]=z.trunc(h[a][b],n)
 T=z.mmul(z.mmul(E,h,n),E,n); gi=z.madd(E,z.mscale(T,-1)); sign=1
 for _ in range(2,8):
  T=z.mmul(z.mmul(T,h,n),E,n); gi=z.madd(gi,z.mscale(T,sign)); sign*=-1
 for a,b in product(range(4),repeat=2):gi[a][b]=z.trunc(gi[a][b],n)
 ok=True
 for a,b in product(range(4),repeat=2):
  v={}
  for c in range(4):v=z.add(v,z.mul(g[a][c],gi[c][b],n))
  if z.trunc(z.sub(v,z.const(1 if a==b else 0)),n):ok=False
 return gi,ok

def einstein(g,n=12):
 gi,invok=inverse(g,n); C=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
 for a,b,c in product(range(4),repeat=3):
  v={}
  for d in range(4):
   u=z.add(z.add(z.deriv(g[d][c],b),z.deriv(g[d][b],c)),z.neg(z.deriv(g[b][c],d)))
   v=z.add(v,z.mul(gi[a][d],u,n+1))
  C[a][b][c]=z.scale(z.trunc(v,n+1),F(1,2))
 Ric=z.pmat()
 for b,d in product(range(4),repeat=2):
  v={}
  for a in range(4):
   v=z.add(v,z.sub(z.deriv(C[a][d][b],a),z.deriv(C[a][a][b],d)))
   for e in range(4):v=z.add(v,z.sub(z.mul(C[a][a][e],C[e][d][b],n),z.mul(C[a][d][e],C[e][a][b],n)))
  Ric[b][d]=z.trunc(v,n)
 Sc={}
 for a,b in product(range(4),repeat=2):Sc=z.add(Sc,z.mul(gi[a][b],Ric[a][b],n))
 Sc=z.trunc(Sc,n); Ein=z.pmat()
 for a,b in product(range(4),repeat=2):Ein[a][b]=z.trunc(z.add(Ric[a][b],z.scale(z.mul(g[a][b],Sc,n),-F(1,2))),n)
 return Ric,Sc,Ein,invok

def gauge(g):
 h=z.pmat()
 for a,b in product(range(4),repeat=2):
  h[a][b]=dict(g[a][b]);
  if a==b:h[a][b]=z.sub(h[a][b],z.const(ETA[a]))
 tr={}
 for a in range(4):tr=z.add(tr,z.scale(h[a][a],ETA[a]))
 hb=z.pmat()
 for a,b in product(range(4),repeat=2):hb[a][b]=z.add(h[a][b],z.scale(tr,-F(ETA[a],2) if a==b else 0))
 out=[]
 for b in range(4):
  v={}
  for a in range(4):v=z.add(v,z.scale(z.deriv(hb[a][b],a),ETA[a]))
  out.append(v)
 return out

def system():
 a11,a12,a13,a14=map(z.alphas,(11,12,13,14)); col={(p,a):p*len(a14)+j for p in range(10) for j,a in enumerate(a14)}; rows=[];meta=[]
 for b in range(4):
  for al in a13:
   d={}
   for a in range(4):q=list(al);q[a]+=1;j=col[(z.pidx(a,b),tuple(q))];d[j]=d.get(j,0)+sp.Integer(ETA[a])
   rows.append(d);meta.append(('G',b,al))
 for p,pair in enumerate(PAIRS):
  for al in a12:
   d={}
   for m in range(4):q=list(al);q[m]+=2;j=col[(p,tuple(q))];d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
   rows.append(d);meta.append(('F',pair,al))
 M=sp.MutableSparseMatrix(len(rows),6800,{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
 return M,rows,meta,a11,a12,a13,a14

def main(out):
 g,prov,r12,meta12=seed12(); gau=gauge(g); Ric,Sc,Ein,invok=einstein(g,12); M,rows,meta,a11,a12,a13,a14=system()
 rhs=[]
 for typ,x,al in meta:
  v=gau[x].get(al,F(0)) if typ=='G' else Ein[x[0]][x[1]].get(al,F(0)); rhs.append(-sp.Rational(v.numerator,v.denominator))
 rank=DomainMatrix.from_Matrix(M).to_field().rank(); Aug=M.row_join(sp.Matrix(rhs)); arank=DomainMatrix.from_Matrix(Aug).to_field().rank()
 ann,comps,brank=z.bianchi_controls(rows,meta,rhs,a11); cnz=sum(c!=0 for c in comps)
 sol=None; nz=[]
 if rank==arank:
  sol=sp.linsolve((M,sp.Matrix(rhs))); vec=list(next(iter(sol))); subs={s:0 for v in vec for s in v.free_symbols}; vec=[sp.factor(v.subs(subs)) for v in vec]
  for p,pair in enumerate(PAIRS):
   for j,al in enumerate(a14):
    v=vec[p*len(a14)+j]
    if v:nz.append({'pair':list(pair),'alpha':list(al),'R14_over_kappa7':str(sp.factor(v*math.prod(math.factorial(x) for x in al)/(sp.Rational(K.numerator,K.denominator)**7)))})
  z.add_trace_reversed_layer(g,nz,7,'R14_over_kappa7',14)
 gau2=gauge(g); Ric2,Sc2,Ein2,inv2=einstein(g,12)
 replay_g=sum(bool(z.trunc(v,13)) for v in gau2); replay_e=sum(bool(z.trunc(Ein2[a][b],12)) for a,b in PAIRS)
 ok=prov and invok and M.shape==(6790,6800) and rank==5334 and arank==5334 and brank==1456 and ann and cnz==0 and replay_g==0 and replay_e==0 and inv2
 classification=PASS if ok else ('SCIENTIFIC_FAIL_ITER057AC_AFFINE_INCOMPATIBILITY' if arank>rank or cnz else 'INVALID_OR_BLOCKED_ITER057AC_CONTROL_FAILURE')
 payload={'gate':'ITER057AC-TETRADECIC-EINSTEIN-SEED-COMPLETION','preregistration':PREREG,'classification':classification,'lower_authority_ok':prov,'matrix_shape':list(M.shape),'rank':rank,'augmented_rank':arank,'left_nullity':M.rows-rank,'nullity':M.cols-rank,'bianchi_rank':brank,'compatibility_nonzero_count':cnz,'R14_particular_nonzero_count':len(nz),'inverse_before_ok':invok,'inverse_after_ok':inv2,'final_full_deDonder_nonzero_count':replay_g,'final_einstein_nonzero_count':replay_e,'particular_R14_normalized':nz,'scope':'finite local Taylor certificate only; c6 symbolic/unfixed; theory established 0%'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest(); Path(out).parent.mkdir(parents=True,exist_ok=True);Path(out).write_text(json.dumps(payload,indent=2,sort_keys=True)); print(json.dumps({k:v for k,v in payload.items() if k!='particular_R14_normalized'},indent=2)); return 0 if ok else 2
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',default='artifacts/iter057ac.json');a=p.parse_args();raise SystemExit(main(a.output))
