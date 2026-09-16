#!/usr/bin/env python3
import json, math, argparse
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix

N=4; K=F(2,25); ETA=(-1,1,1,1); ZERO=(0,0,0,0)
PAIRS=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
PASS='PASS_SCOPED_ITER057Z_DODECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_TEN__HIGHER_SEED_ORDERS_REMAIN_OPEN'
FAIL='SCIENTIFIC_FAIL_SCOPED_ITER057Z_UNRESTRICTED_DODECIC_EINSTEIN_SEED_SYSTEM_INCOMPATIBLE'
INVALID='INVALID_ITER057Z_RESTRICTED_ANSATZ_LOWER_SEED_CHANGE_NUMERICAL_EXACTNESS_OR_CONTROL_FAILURE'
PREREG='f1c04bbfdb7848ab79708beb902ccdb315fbd5ed'
ROOT=Path(__file__).resolve().parents[1]
R6_PATH=ROOT/'data'/'ITER057Q_CANONICAL_R6_NORMALIZED.json'
R8_PATH=ROOT/'data'/'ITER057T_CANONICAL_R8_NORMALIZED.json'
R10_PATH=ROOT/'data'/'ITER057W_CANONICAL_R10_NORMALIZED.csv'
Q_COMMIT='c4f1c5c01205a6991e7215e3824111e1f36d1436'; Q_DIGEST='sha256:4f7cbdba018f9193f964e71bfe5e1843d803a1432821e40d70e5f6686d42db38'
T_COMMIT='e4d8b960b8694ee166d05aa3ff089999b843e32a'; T_DIGEST='sha256:20134b10e4cf32ecd8b3e417921545714f12b29f4d72f812f6d5121e6b461dba'
R10_PREREG='7e6336d195985b2059966eda64859da86c9e9d15'; R10_SHA='359b27d478b5b4927bc7df0c98a361f0177bba57e5550433662cd21138f75571'

R4={
 ((0,0),(0,0,0,4)):F(136),
 ((0,0),(0,0,2,2)):F(-16),
 ((0,0),(0,2,0,2)):F(-16),
 ((0,0),(2,0,0,2)):F(56),
 ((0,0),(2,0,2,0)):F(-28),
 ((0,0),(2,2,0,0)):F(-28),
 ((0,3),(1,0,0,3)):F(56),
 ((0,3),(1,0,2,1)):F(-28),
 ((0,3),(1,2,0,1)):F(-28),
 ((1,1),(0,0,0,4)):F(-64),
 ((1,1),(0,0,2,2)):F(-4),
 ((1,1),(0,2,0,2)):F(4),
 ((1,2),(0,1,1,2)):F(4),
 ((1,3),(0,1,0,3)):F(-8),
 ((2,2),(0,0,0,4)):F(-64),
 ((2,2),(0,0,2,2)):F(4),
 ((2,2),(0,2,0,2)):F(-4),
 ((2,3),(0,0,1,3)):F(-8),
 ((3,3),(0,0,0,4)):F(72),
 ((3,3),(0,0,2,2)):F(-28),
 ((3,3),(0,2,0,2)):F(-28),
}

def const(c):
    c=F(c); return {} if c==0 else {ZERO:c}
def mono(exp,c=1):
    c=F(c); return {} if c==0 else {tuple(exp):c}
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
            e=list(m); z=e[j]; e[j]-=1; e=tuple(e)
            out[e]=out.get(e,F(0))+c*z
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
            (pair,al),coef=item; a,b=pair; coef=F(coef)
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

def read_r10():
    import csv
    meta={};body=[]
    for line in R10_PATH.read_text().splitlines():
        if line.startswith('# '):
            z=line[2:]
            if '=' in z:
                k,v=z.split('=',1);meta[k]=v
        elif line.strip():body.append(line)
    rows=[]
    for r in csv.DictReader(body):
        rows.append({'pair':[int(r['a']),int(r['b'])], 'alpha':[int(r['t']),int(r['x']),int(r['y']),int(r['z'])], 'R10_over_kappa5':r['R10_over_kappa5']})
    return rows,meta

def canonical_seed10():
    q=add(add(mono((0,2,0,0),K),mono((0,0,2,0),K)),mono((0,0,0,2),-2*K))
    g=pmat()
    for a in range(4): g[a][a]=add(const(ETA[a]),scale(q,-1))
    _,p4=add_trace_reversed_layer(g,list(R4.items()),2,None,4)
    qd=json.loads(R6_PATH.read_text()); td=json.loads(R8_PATH.read_text()); r10rows,r10meta=read_r10()
    _,p6=add_trace_reversed_layer(g,qd['particular_R6_normalized'],3,'R6_over_kappa3',6)
    _,p8=add_trace_reversed_layer(g,td['particular_R8_normalized'],4,'R8_over_kappa4',8)
    _,p10=add_trace_reversed_layer(g,r10rows,5,'R10_over_kappa5',10)
    prov=(p4 and p6 and p8 and p10 and len(R4)==21 and
          qd.get('source_commit')==Q_COMMIT and qd.get('source_digest')==Q_DIGEST and len(qd.get('particular_R6_normalized',[]))==69 and
          td.get('source_commit')==T_COMMIT and td.get('source_digest')==T_DIGEST and len(td.get('particular_R8_normalized',[]))==153 and
          r10meta.get('preregistration')==R10_PREREG and r10meta.get('scientific_payload_sha256')==R10_SHA and len(r10rows)==283)
    return g,prov,qd,td,{'particular_R10_normalized':r10rows,'meta':r10meta}

def inverse10(g):
    E=eta_mat(); h=pmat()
    for a,b in product(range(4),repeat=2):
        h[a][b]=dict(g[a][b])
        if a==b:h[a][b]=sub(h[a][b],const(ETA[a]))
        h[a][b]=trunc(h[a][b],10)
    T1=mmul(mmul(E,h,10),E,10)
    T2=mmul(mmul(T1,h,10),E,10)
    T3=mmul(mmul(T2,h,10),E,10)
    T4=mmul(mmul(T3,h,10),E,10)
    T5=mmul(mmul(T4,h,10),E,10)
    gi=madd(madd(madd(madd(madd(E,mscale(T1,-1)),T2),mscale(T3,-1)),T4),mscale(T5,-1))
    for a,b in product(range(4),repeat=2):gi[a][b]=trunc(gi[a][b],10)
    ok=True
    for a,b in product(range(4),repeat=2):
        v={}
        for c in range(4):v=add(v,mul(g[a][c],gi[c][b],10))
        if trunc(sub(v,const(1 if a==b else 0)),10):ok=False
    return gi,ok

def einstein10(g):
    gi,invok=inverse10(g)
    G=[[[{} for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,c in product(range(4),repeat=3):
        v={}
        for d in range(4):
            u=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            v=add(v,mul(gi[a][d],u,11))
        G[a][b][c]=scale(trunc(v,11),F(1,2))
    Ric=pmat()
    for b,d in product(range(4),repeat=2):
        v={}
        for a in range(4):
            v=add(v,sub(deriv(G[a][d][b],a),deriv(G[a][a][b],d)))
            for e in range(4):
                v=add(v,sub(mul(G[a][a][e],G[e][d][b],10),mul(G[a][d][e],G[e][a][b],10)))
        Ric[b][d]=trunc(v,10)
    Sc={}
    for a,b in product(range(4),repeat=2):Sc=add(Sc,mul(gi[a][b],Ric[a][b],10))
    Sc=trunc(Sc,10)
    Ein=pmat()
    for a,b in product(range(4),repeat=2):Ein[a][b]=trunc(add(Ric[a][b],scale(mul(g[a][b],Sc,10),-F(1,2))),10)
    return gi,Ric,Sc,Ein,invok

def build_system():
    a9,a10,a11,a12=alphas(9),alphas(10),alphas(11),alphas(12)
    col={(p,al):p*len(a12)+j for p in range(10) for j,al in enumerate(a12)}
    rows=[];meta=[]
    for b in range(4):
        for al in a11:
            d={}
            for a in range(4):
                be=list(al);be[a]+=1;be=tuple(be);j=col[(pidx(a,b),be)];d[j]=d.get(j,0)+sp.Integer(ETA[a])
            rows.append(d);meta.append(('G',b,al))
    for p,pair in enumerate(PAIRS):
        for al in a10:
            d={}
            for m in range(4):
                be=list(al);be[m]+=2;be=tuple(be);j=col[(p,be)];d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
            rows.append(d);meta.append(('F',pair,al))
    M=sp.MutableSparseMatrix(len(rows),10*len(a12),{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
    return M,rows,meta,a9,a10,a11,a12

def bianchi_controls(rows,meta,rhs,a9):
    lookup={m:i for i,m in enumerate(meta)}; comps=[]; ann=True; brows=[]
    for b in range(4):
        for beta in a9:
            combo={}; val=sp.Integer(0); br={}
            for m in range(4):
                al=list(beta);al[m]+=2;i=lookup[('G',b,tuple(al))];c=sp.Rational(ETA[m],2);val+=c*rhs[i];br[i]=br.get(i,0)+c
                for j,x in rows[i].items():combo[j]=combo.get(j,0)+c*x
            for a in range(4):
                al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a);i=lookup[('F',pair,tuple(al))];c=sp.Integer(ETA[a]);val+=c*rhs[i];br[i]=br.get(i,0)+c
                for j,x in rows[i].items():combo[j]=combo.get(j,0)+c*x
            if any(x!=0 for x in combo.values()):ann=False
            comps.append(sp.factor(val)); brows.append(br)
    B=sp.MutableSparseMatrix(len(brows),len(rows),{(i,j):v for i,d in enumerate(brows) for j,v in d.items() if v})
    brank=DomainMatrix.from_Matrix(B).to_field().rank()
    return ann,comps,brank

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
        out.append(trunc(v,11))
    return out

def compute():
    g10,prov,qd,td,wd=canonical_seed10()
    gi0,Ric0,Sc0,Ein0,inv0=einstein10(g10)
    lower=all(not homog(Ein0[a][b],d) for a,b in product(range(4),repeat=2) for d in (0,2,4,6,8))
    E10={(a,b):homog(Ein0[a][b],10) for a,b in PAIRS}
    nonzero={f'{a}{b}':{str(m):fstr(c) for m,c in sorted(v.items())} for (a,b),v in E10.items() if v}
    M,rows,meta,a9,a10,a11,a12=build_system()
    rhs=[sp.Integer(0)]*(4*len(a11))
    for pair in PAIRS:
        p=E10[pair]
        for al in a10:
            raw=p.get(al,F(0));rhs.append(-qrat(raw*F(fact(al))/(K**6)))
    rhs=sp.Matrix(rhs)
    DM=DomainMatrix.from_Matrix(M).to_field();rankM=DM.rank()
    ann,compat,brank=bianchi_controls(rows,meta,rhs,a9)
    R,piv=DomainMatrix.from_Matrix(M.row_join(rhs)).to_field().rref();rankA=len(piv);consistent=(rankA==rankM and all(j<M.cols for j in piv));R=R.to_Matrix()
    qv=[sp.Integer(0)]*M.cols
    if consistent:
        for i,j in enumerate(piv):qv[j]=sp.factor(R[i,M.cols])
    linres=[]
    for i,row in enumerate(rows):linres.append(sp.factor(sum(v*qv[j] for j,v in row.items())-rhs[i]))
    sparse=[]
    for idx,v in enumerate(qv):
        if v==0:continue
        p=idx//len(a12);al=a12[idx%len(a12)];sparse.append({'pair':list(PAIRS[p]),'alpha':list(al),'R12_over_kappa6':str(v)})
    g12=[[dict(g10[a][b]) for b in range(4)] for a in range(4)]
    r12,pure=add_trace_reversed_layer(g12,sparse,6,'R12_over_kappa6',12)
    preserve=all(not trunc(r12[a][b],11) for a,b in product(range(4),repeat=2))
    gauge=flat_gauge(g12)
    gi1,Ric1,Sc1,Ein1,inv1=einstein10(g12)
    riczero=all(not Ric1[a][b] for a,b in product(range(4),repeat=2));sczero=not Sc1;einzero=all(not Ein1[a][b] for a,b in product(range(4),repeat=2))
    controls={
      'A_frozen_R4_R6_R8_R10_provenance':prov,
      'A_seed_inverse_through_degree10':inv0,
      'A_lower_Einstein_0_2_4_6_8_zero':lower,
      'B_degree10_direct_nonlinear_residual_computed':True,
      'C_shape_4316x4550':M.shape==(4316,4550),
      'D_rank_3436':rankM==3436,
      'D_left_nullity_880':M.rows-rankM==880,
      'D_nullity_1114':M.cols-rankM==1114,
      'D_Bianchi_count_880':len(compat)==880,
      'D_Bianchi_rank_880':brank==880,
      'D_Bianchi_annihilates_M':ann,
      'E_augmented_rank_3436':consistent and rankA==3436,
      'E_compatibility_880_zero':all(v==0 for v in compat),
      'F_affine_residual_zero':all(v==0 for v in linres),
      'F_homogeneous_1114':M.cols-rankM==1114,
      'G_completed_inverse10':inv1,
      'G_Ricci10_zero':riczero,
      'G_scalar10_zero':sczero,
      'G_Einstein10_zero':einzero,
      'G_flat_deDonder11_zero':all(not v for v in gauge),
      'H_R12_pure12':pure,
      'H_preserve_through11':preserve,
      'I_no_tolerance':True,
    }
    passed=all(controls.values())
    classification=PASS if passed else (FAIL if rankA>rankM and ann and any(v!=0 for v in compat) else INVALID)
    return {
      'gate':'ITER057Z-DODECIC-EINSTEIN-SEED-COMPLETION','preregistration_commit':PREREG,'execution_lineage':'REPO_NATIVE_SPARSE_FRACTION_CANONICAL_R4_R6_R8_R10_AUTHORITIES',
      'controls':controls,'pass':passed,'classification':classification,
      'degree10_Einstein_residual_nonzero_component_count':len(nonzero),'degree10_Einstein_residual_sparse':nonzero,
      'matrix_shape':[M.rows,M.cols],'matrix_nnz':len(M.todok()),'rank_M':rankM,'rank_augmented':rankA,
      'left_nullity':M.rows-rankM,'nullity':M.cols-rankM,'bianchi_rank':brank,'compatibility_nonzero_count':sum(v!=0 for v in compat),
      'particular_nonzero_count':len(sparse),'particular_R12_normalized':sparse,
      'combined_linear_deDonder_nonzero_component_count':sum(bool(v) for v in gauge),
      'full_metric_Ricci_nonzero_component_count':sum(bool(Ric1[a][b]) for a,b in PAIRS),
      'full_metric_Einstein_nonzero_component_count':sum(bool(Ein1[a][b]) for a,b in PAIRS),
      'exact_zero_uses_tolerance':False,'c6_status':'NOT_USED_ZERO_ORDER_SEED_COMPLETION'
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out');a=ap.parse_args();o=compute();txt=json.dumps(o,indent=2,sort_keys=True)+'\n'
    if a.out:
        p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(txt)
    print(json.dumps({k:o[k] for k in ['pass','classification','matrix_shape','matrix_nnz','rank_M','rank_augmented','left_nullity','nullity','bianchi_rank','compatibility_nonzero_count','degree10_Einstein_residual_nonzero_component_count','particular_nonzero_count','combined_linear_deDonder_nonzero_component_count','full_metric_Ricci_nonzero_component_count','full_metric_Einstein_nonzero_component_count']},indent=2))
    if not o['pass']: raise SystemExit(2)
if __name__=='__main__':main()
