#!/usr/bin/env python3
"""Iter057AD exact branch-obstruction evaluator.
Prospective gate frozen at 8f53a0679692f9655e162aa1a19e45124a8dc775.
This implementation does not change scientific criteria.  It reconstructs the
complete M12 kernel, replays the canonical AC obstruction, and evaluates exact
columns of the obstruction map by directional finite difference.  Column
ranges permit independent Actions lanes; aggregation is a separate step.
"""
import argparse,json,hashlib
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ac_tetradecic_einstein_seed_completion as ac

PREREG='8f53a0679692f9655e162aa1a19e45124a8dc775'
ROOT=Path(__file__).resolve().parents[1]

def kernel_data():
    M,rows,meta,a9,a10,a11,a12=z.build_system()
    R,piv=DomainMatrix.from_Matrix(M).to_field().rref(); R=R.to_Matrix()
    piv=list(piv); free=[j for j in range(M.cols) if j not in set(piv)]
    # deterministic rational right-null basis, one free coordinate per column
    basis=[]
    for f in free:
        v=[sp.Integer(0)]*M.cols; v[f]=1
        for i,p in enumerate(piv): v[p]=-R[i,f]
        basis.append(v)
    return M,rows,meta,a12,basis

def add_direction(g,v,a12):
    items=[]
    for idx,x in enumerate(v):
        if x:
            p=idx//len(a12); al=a12[idx%len(a12)]
            items.append({'pair':list(z.PAIRS[p]),'alpha':list(al),'R12_over_kappa6':str(x)})
    z.add_trace_reversed_layer(g,items,6,'R12_over_kappa6',12)

def rhs14(g):
    gau=ac.gauge(g); Ric,Sc,Ein,inv=ac.einstein(g,12)
    M14,rows14,meta14,a11,a12,a13,a14=ac.system()
    rhs=[]
    for typ,x,al in meta14:
        v=gau[x].get(al,z.F(0)) if typ=='G' else Ein[x[0]][x[1]].get(al,z.F(0))
        rhs.append(-sp.Rational(v.numerator,v.denominator))
    return M14,rows14,meta14,a11,sp.Matrix(rhs),inv

def left_controls(rows,meta,a11):
    # Explicit Bianchi/Noether left rows, same convention as Iter057AC.
    lookup={m:i for i,m in enumerate(meta)}; brows=[]
    for b in range(4):
      for beta in a11:
        br={}
        for m in range(4):
          al=list(beta);al[m]+=2;i=lookup[('G',b,tuple(al))];c=sp.Rational(z.ETA[m],2);br[i]=br.get(i,0)+c
        for a in range(4):
          al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a);i=lookup[('F',pair,tuple(al))];c=sp.Integer(z.ETA[a]);br[i]=br.get(i,0)+c
        brows.append(br)
    L=sp.MutableSparseMatrix(len(brows),len(rows),{(i,j):v for i,d in enumerate(brows) for j,v in d.items() if v})
    return L

def canonical_seed12():
    g,prov,rows,meta=ac.seed12(); return g,prov

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int,default=0);ap.add_argument('--out',required=True);a=ap.parse_args()
    M12,rows12,meta12,a12,basis=kernel_data()
    if M12.shape!=(4316,4550) or len(basis)!=1114: raise SystemExit('kernel structural mismatch')
    # exact annihilation proof for every reconstructed basis vector
    kernel_ok=all(not any(M12*sp.Matrix(v)) for v in basis)
    g0,prov=canonical_seed12(); M14,rows14,meta14,a11,r0,inv0=rhs14(g0); L=left_controls(rows14,meta14,a11)
    ann=(L*M14)==sp.zeros(L.rows,M14.cols); O0=L*r0; cnz=sum(x!=0 for x in O0)
    start=max(0,a.start); stop=min(len(basis),a.stop if a.stop else len(basis)); cols=[]
    for i in range(start,stop):
        g,prov_i=canonical_seed12(); add_direction(g,basis[i],a12)
        _,_,_,_,ri,invi=rhs14(g)
        col=L*(ri-r0)
        cols.append({'index':i,'nonzero':[[j,str(x)] for j,x in enumerate(col) if x!=0],'inverse_ok':bool(invi),'lower_authority_ok':bool(prov_i)})
    payload={'gate':'ITER057AD-R12-HOMOGENEOUS-BRANCH-R14-OBSTRUCTION-LIFT','preregistration':PREREG,'lane':[start,stop],
      'M12_shape':list(M12.shape),'M12_rank':3436,'kernel_dimension':len(basis),'kernel_exact_annihilation':kernel_ok,
      'M14_shape':list(M14.shape),'L14_shape':list(L.shape),'L14_annihilates_M14':ann,'canonical_inverse_ok':inv0,
      'canonical_lower_authority_ok':prov,'canonical_obstruction_nonzero_count':cnz,
      'canonical_obstruction_replays_223':cnz==223,'columns':cols,
      'classification':'PARTIAL_EXACT_LANE_ONLY__NO_ITER057AD_TERMINAL_CLASSIFICATION'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest()
    p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True));print(json.dumps({k:v for k,v in payload.items() if k!='columns'},indent=2))
    return 0 if kernel_ok and ann and cnz==223 and prov and inv0 else 2
if __name__=='__main__': raise SystemExit(main())