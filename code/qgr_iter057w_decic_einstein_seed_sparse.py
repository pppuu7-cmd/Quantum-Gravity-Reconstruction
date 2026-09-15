#!/usr/bin/env python3
"""Iter057W sparse-Fraction reproduction of the exact unrestricted decic seed gate."""
import argparse, json, math
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import qgr_iter057p_corrected_seed_weyl3_point_source as pseed

N=4; K=F(2,25); ETA=(-1,1,1,1); ZERO=(0,0,0,0)
PAIRS=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
GATE='ITER057W-DECIC-EINSTEIN-SEED-COMPLETION'
PREREG='7e6336d195985b2059966eda64859da86c9e9d15'
R6_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057Q_CANONICAL_R6_NORMALIZED.json'
R8_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057T_CANONICAL_R8_NORMALIZED.json'
Q_COMMIT='c4f1c5c01205a6991e7215e3824111e1f36d1436'
Q_DIGEST='sha256:4f7cbdba018f9193f964e71bfe5e1843d803a1432821e40d70e5f6686d42db38'
T_COMMIT='e4d8b960b8694ee166d05aa3ff089999b843e32a'
T_DIGEST='sha256:20134b10e4cf32ecd8b3e417921545714f12b29f4d72f812f6d5121e6b461dba'

def const(c): c=F(c); return {} if c==0 else {ZERO:c}
def mono(exp,c=1): c=F(c); return {} if c==0 else {tuple(exp):c}
def add(a,b):
    out=dict(a)
    for m,c in b.items():
        v=out.get(m,F(0))+c
        if v: out[m]=v
        elif m in out: del out[m]
    return out
def neg(a): return {m:-c for m,c in a.items()}
def sub(a,b): return add(a,neg(b))
def scale(a,c):
    c=F(c); return {} if c==0 else {m:c*v for m,v in a.items() if c*v}
def trunc(a,n): return {m:c for m,c in a.items() if sum(m)<=n and c}
def homog(a,n): return {m:c for m,c in a.items() if sum(m)==n and c}
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
            e=list(m); z=e[j]; e[j]-=1; e=tuple(e); out[e]=out.get(e,F(0))+c*z
    return {m:c for m,c in out.items() if c}
def fact(alpha): return math.prod(math.factorial(x) for x in alpha)
def pmat(): return [[{} for _ in range(4)] for _ in range(4)]
def madd(A,B): return [[add(A[i][j],B[i][j]) for j in range(4)] for i in range(4)]
def mscale(A,c): return [[scale(A[i][j],c) for j in range(4)] for i in range(4)]
def mmul(A,B,n):
    C=pmat()
    for i,j in product(range(4),repeat=2):
        v={}
        for r in range(4): v=add(v,mul(A[i][r],B[r][j],n))
        C[i][j]=trunc(v,n)
    return C
def eta_mat():
    E=pmat()
    for a in range(4): E[a][a]=const(ETA[a])
    return E
def alphas(n): return sorted(a for a in product(range(n+1),repeat=4) if sum(a)==n)
def pidx(a,b):
    if a>b:a,b=b,a
    return PAIRS.index((a,b))
def qrat(v): return sp.Rational(v.numerator,v.denominator)
def fstr(v): return str(v.numerator) if v.denominator==1 else f'{v.numerator}/{v.denominator}'

def add_trace_reversed_layer(g,items,power,key,degree):
    rb=pmat()
    for item in items:
        if isinstance(item,dict) and 'pair' in item:
            a,b=item['pair']; al=tuple(item['alpha']); coef=F(item[key])
        else:
            (pair,al),coef=item; a,b=pair; coef=F(coef.numerator,coef.denominator)
        term=mono(al,K**power*coef/F(fact(al)))
        rb[a][b]=add(rb[a][b],term)
        if a!=b: rb[b][a]=add(rb[b][a],term)
    tr={}
    for a in range(4): tr=add(tr,scale(rb[a][a],ETA[a]))
    r=pmat()
    for a,b in product(range(4),repeat=2):
        r[a][b]=dict(rb[a][b])
        if a==b:r[a][b]=add(r[a][b],scale(tr,-F(ETA[a],2)))
        g[a][b]=add(g[a][b],r[a][b])
    pure=all(all(sum(m)==degree for m in r[a][b]) for a,b in product(range(4),repeat=2))
    return r,pure

def canonical_seed8():
    q=add(add(mono((0,2,0,0),K),mono((0,0,2,0),K)),mono((0,0,0,2),-2*K))
    g=pmat()
    for a in range(4):g[a][a]=add(const(ETA[a]),scale(q,-1))
    r4,p4=add_trace_reversed_layer(g,list(pseed.R4.items()),2,None,4)
    r6d=json.loads(R6_PATH.read_text()); r8d=json.loads(R8_PATH.read_text())
    p6prov=(r6d.get('source_commit')==Q_COMMIT and r6d.get('source_digest')==Q_DIGEST and len(r6d.get('particular_R6_normalized',[]))==69)
    p8prov=(r8d.get('source_commit')==T_COMMIT and r8d.get('source_digest')==T_DIGEST and len(r8d.get('particular_R8_normalized',[]))==153)
    r6,p6=add_trace_reversed_layer(g,r6d['particular_R6_normalized'],3,'R6_over_kappa3',6)
    r8,p8=add_trace_reversed_layer(g,r8d['particular_R8_normalized'],4,'R8_over_kappa4',8)
    return g,(p4 and p6 and p8 and p6prov and p8prov),r6d,r8d

def inverse8(g):
    E=eta_mat(); h=pmat()
    for a,b in product(range(4),repeat=2):
        h[a][b]=dict(g[a][b])
        if a==b:h[a][b]=sub(h[a][b],const(ETA[a]))
        h[a][b]=trunc(h[a][b],8)
    T1=mmul(mmul(E,h,8),E,8)
    T2=mmul(mmul(T1,h,8),E,8)
    T3=mmul(mmul(T2,h,8),E,8)
    T4=mmul(mmul(T3,h,8),E,8)
    gi=madd(madd(madd(madd(E,mscale(T1,-1)),T2),mscale(T3,-1)),T4)
    for a,b in product(range(4),repeat=2):gi[a][b]=trunc(gi[a][b],8)
    ok=True
    for a,b in product(range(4),repeat=2):
        v={}
        for c in range(4):v=add(v,mul(g[a][c],gi[c][b],8))
        if trunc(sub(v,const(1 if a==b else 0)),8):ok=False
    return gi,ok

def einstein8(g):
    gi,invok=inverse8(g)
    G=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,c in product(range(4),repeat=3):
        v={}
        for d in range(4):
            u=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            v=add(v,mul(gi[a][d],u,9))
        G[a][b][c]=scale(trunc(v,9),F(1,2))
    Ric=pmat()
    for b,d in product(range(4),repeat=2):
        v={}
        for a in range(4):
            v=add(v,sub(deriv(G[a][d][b],a),deriv(G[a][a][b],d)))
            for e in range(4):
                v=add(v,sub(mul(G[a][a][e],G[e][d][b],8),mul(G[a][d][e],G[e][a][b],8)))
        Ric[b][d]=trunc(v,8)
    Sc={}
    for a,b in product(range(4),repeat=2):Sc=add(Sc,mul(gi[a][b],Ric[a][b],8))
    Sc=trunc(Sc,8)
    Ein=pmat()
    for a,b in product(range(4),repeat=2):
        Ein[a][b]=dict(Ric[a][b])
        Ein[a][b]=add(Ein[a][b],scale(mul(g[a][b],Sc,8),-F(1,2)))
        Ein[a][b]=trunc(Ein[a][b],8)
    return gi,Ric,Sc,Ein,invok

def build_system():
    a7,a8,a9,a10=alphas(7),alphas(8),alphas(9),alphas(10)
    col={(p,al):p*len(a10)+j for p in range(10) for j,al in enumerate(a10)}
    rows=[];meta=[]
    for b in range(4):
        for al in a9:
            d={}
            for a in range(4):
                be=list(al);be[a]+=1;be=tuple(be);j=col[(pidx(a,b),be)];d[j]=d.get(j,0)+sp.Integer(ETA[a])
            rows.append(d);meta.append(('G',b,al))
    for p,pair in enumerate(PAIRS):
        for al in a8:
            d={}
            for m in range(4):
                be=list(al);be[m]+=2;be=tuple(be);j=col[(p,be)];d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
            rows.append(d);meta.append(('F',pair,al))
    M=sp.MutableSparseMatrix(len(rows),10*len(a10),{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
    return M,rows,meta,a7,a8,a9,a10

def bianchi_controls(rows,meta,rhs,a7):
    lookup={m:i for i,m in enumerate(meta)}; comps=[]; ann=True
    for b in range(4):
        for beta in a7:
            combo={}; val=sp.Integer(0)
            for m in range(4):
                al=list(beta);al[m]+=2;i=lookup[('G',b,tuple(al))];c=sp.Rational(ETA[m],2);val+=c*rhs[i]
                for j,x in rows[i].items():combo[j]=combo.get(j,0)+c*x
            for a in range(4):
                al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a);i=lookup[('F',pair,tuple(al))];c=sp.Integer(ETA[a]);val+=c*rhs[i]
                for j,x in rows[i].items():combo[j]=combo.get(j,0)+c*x
            if any(x!=0 for x in combo.values()):ann=False
            comps.append(sp.factor(val))
    return ann,comps

def flat_gauge(g):
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
        out.append(trunc(v,9))
    return out

def compute():
    g8,prov,r6d,r8d=canonical_seed8(); gi8,Ric8,Sc8,Ein8,inv8=einstein8(g8)
    lower=all(not homog(Ein8[a][b],d) for a,b in product(range(4),repeat=2) for d in (0,2,4,6))
    E8={(a,b):homog(Ein8[a][b],8) for a,b in PAIRS}
    nonzero={f'{a}{b}':{str(m):fstr(c) for m,c in sorted(v.items())} for (a,b),v in E8.items() if v}
    div=[]
    for b in range(4):
        v={}
        for a in range(4):
            pair=(a,b) if a<=b else (b,a);v=add(v,scale(deriv(E8[pair],a),ETA[a]))
        div.append(v)
    M,rows,meta,a7,a8,a9,a10=build_system(); rhs=[sp.Integer(0)]*(4*len(a9))
    for pair in PAIRS:
        p=E8[pair]
        for al in a8:
            raw=p.get(al,F(0)); rhs.append(-qrat(raw*F(fact(al))/(K**5)))
    rhs=sp.Matrix(rhs)
    DM=DomainMatrix.from_Matrix(M).to_field(); rankM=DM.rank()
    R,piv=DomainMatrix.from_Matrix(M.row_join(rhs)).to_field().rref(); rankA=len(piv); consistent=(rankA==rankM and all(j<M.cols for j in piv)); R=R.to_Matrix()
    ann,compat=bianchi_controls(rows,meta,rhs,a7)
    qv=[sp.Integer(0)]*M.cols
    if consistent:
        for i,j in enumerate(piv):qv[j]=sp.factor(R[i,M.cols])
    linres=[]
    for i,row in enumerate(rows):linres.append(sp.factor(sum(v*qv[j] for j,v in row.items())-rhs[i]))
    sparse=[]
    for idx,v in enumerate(qv):
        if v==0:continue
        p=idx//len(a10);al=a10[idx%len(a10)];sparse.append({'pair':list(PAIRS[p]),'alpha':list(al),'R10_over_kappa5':str(v)})
    g10=[[dict(g8[a][b]) for b in range(4)] for a in range(4)]; rb=pmat()
    for item in sparse:
        a,b=item['pair'];al=tuple(item['alpha']);v=F(item['R10_over_kappa5']);term=mono(al,K**5*v/F(fact(al)));rb[a][b]=add(rb[a][b],term)
        if a!=b:rb[b][a]=add(rb[b][a],term)
    tr={}
    for a in range(4):tr=add(tr,scale(rb[a][a],ETA[a]))
    r10=pmat()
    for a,b in product(range(4),repeat=2):
        r10[a][b]=dict(rb[a][b])
        if a==b:r10[a][b]=add(r10[a][b],scale(tr,-F(ETA[a],2)))
        g10[a][b]=add(g10[a][b],r10[a][b])
    pure=all(all(sum(m)==10 for m in r10[a][b]) for a,b in product(range(4),repeat=2)); preserve=all(not trunc(r10[a][b],9) for a,b in product(range(4),repeat=2))
    gauge=flat_gauge(g10); gi10,Ric10,Sc10,Ein10,inv10=einstein8(g10)
    riczero=all(not Ric10[a][b] for a,b in product(range(4),repeat=2)); sczero=not Sc10; einzero=all(not Ein10[a][b] for a,b in product(range(4),repeat=2))
    controls={'A_frozen_R6_R8_provenance':prov,'A_lower_Einstein_0_2_4_6_zero':lower,'A_seed_inverse8':inv8,'B_degree8_direct':True,'B_degree8_Bianchi_zero':all(not v for v in div),
      'C_shape_2530x2860':M.shape==(2530,2860),'D_rank_2050':rankM==2050,'D_left_nullity_480':M.rows-rankM==480,'D_nullity_810':M.cols-rankM==810,'D_Bianchi_count_480':len(compat)==480,'D_Bianchi_annihilates_M':ann,
      'E_augmented_rank_2050':consistent and rankA==2050,'E_compatibility_480_zero':all(v==0 for v in compat),'F_affine_residual_zero':all(v==0 for v in linres),'F_homogeneous_810':M.cols-rankM==810,
      'G_completed_inverse8':inv10,'G_Ricci8_zero':riczero,'G_scalar8_zero':sczero,'G_Einstein8_zero':einzero,'G_flat_deDonder9_zero':all(not v for v in gauge),'H_R10_pure10':pure,'H_preserve_through9':preserve,'I_no_tolerance':True}
    passed=all(controls.values())
    return {'gate':GATE,'preregistration_commit':PREREG,'execution_lineage':'SPARSE_FRACTION_FROZEN_R6_R8','controls':controls,'pass':passed,'classification':('PASS_SCOPED_ITER057W_DECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_EIGHT__HIGHER_SEED_ORDERS_REMAIN_OPEN' if passed else ('SCIENTIFIC_FAIL_SCOPED_ITER057W_UNRESTRICTED_DECIC_EINSTEIN_SEED_SYSTEM_INCOMPATIBLE' if rankA>rankM and ann and any(v!=0 for v in compat) else 'INVALID_OR_UNRESOLVED_ITER057W')),
      'degree8_Einstein_residual_nonzero_component_count':len(nonzero),'degree8_Einstein_residual_sparse':nonzero,'matrix_shape':[M.rows,M.cols],'matrix_nnz':len(M.todok()),'rank_M':rankM,'rank_augmented':rankA,'left_nullity':M.rows-rankM,'nullity':M.cols-rankM,'compatibility_nonzero_count':sum(v!=0 for v in compat),'particular_nonzero_count':len(sparse),'particular_R10_normalized':sparse,'combined_linear_deDonder_nonzero_component_count':sum(bool(v) for v in gauge),'full_metric_Einstein_nonzero_component_count':sum(bool(Ein10[a][b]) for a,b in PAIRS),'exact_zero_uses_tolerance':False,'c6_status':'NOT_USED_ZERO_ORDER_SEED_COMPLETION'}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out');a=ap.parse_args();o=compute();txt=json.dumps(o,indent=2,sort_keys=True)+'\n';
    if a.out:Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(txt)
    print(txt,end='')
    if not o['pass']:raise SystemExit(2)
if __name__=='__main__':main()
