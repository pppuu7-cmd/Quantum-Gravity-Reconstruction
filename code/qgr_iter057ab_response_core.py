#!/usr/bin/env python3
import argparse,json,csv,sys,hashlib
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa
z=aa.z
N=z.N
K=z.K
ETA=z.ETA
ZERO=z.ZERO
PAIRS=z.PAIRS
const=z.const
mono=z.mono
add=z.add
neg=z.neg
sub=z.sub
scale=z.scale
mul=z.mul
deriv=z.deriv
trunc=z.trunc
pmat=z.pmat
fact=z.fact
alphas=z.alphas
fstr=z.fstr
PASS='PASS_SCOPED_ITER057AB_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_Q8_Q10_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_EIGHTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN'
FAIL='SCIENTIFIC_FAIL_SCOPED_ITER057AB_UNRESTRICTED_Q10_RESPONSE_SYSTEM_INCOMPATIBLE_WITH_CORRECTED_WEYL3_SOURCE_THROUGH_DEGREE_EIGHT'
INVALID='INVALID_ITER057AB_RESTRICTED_ANSATZ_LOWER_RESPONSE_OR_SEED_MUTATION_SOURCE_SUBSTITUTION_NUMERICAL_EXACTNESS_OR_CONTROL_FAILURE'
ROOT=Path(__file__).resolve().parents[1]
S_PATH=ROOT/'data'/'ITER057S_CANONICAL_Q2_Q4_RESPONSE.json'
V_PATH=ROOT/'data'/'ITER057V_CANONICAL_Q6_RESPONSE.json'
Y_PATH=ROOT/'data'/'ITER057Y_CANONICAL_Q8_RESPONSE.json'
U_PATH=ROOT/'data'/'ITER057U_CANONICAL_SOURCE_0_2_4.json'
X_PATH=ROOT/'data'/'ITER057X_CANONICAL_SOURCE_DEGREE6.csv'
AA_PATH=ROOT/'data'/'ITER057AA_CANONICAL_SOURCE_DEGREE8.csv'
GATE='ITER057AB-ONSHELL-FIRST-ORDER-Q2-Q4-Q6-Q8-Q10-RESPONSE'
PREREG='f78b028c345faa80f1e482f6a00fb9133cb9b955'
ITER057Y='cb2758238daba9ecf9c86e01e171f6c6d31c72b9'
ITER057Z='bb4fa6ccbf21e2a063467a1b0839223744866995'
ITER057AA='2c84ddcb5dd22cfe06cd3a1a273b4a0e141b605e'
S_BLOB='a1b819ed8a618f145f350d7d3dd82daba59abfec'
V_BLOB='5f897382fe0ba21540c18a096dd54ae564505ad2'
Y_BLOB='e75125bdc4767f695173ace1046d7212d9b6c157'
UNRED_LOWER_SHA='8fac49da60cc0ac90d62117166bf95e0ca7363ea2df1333bb7d2181cf34b9f70'
def git_blob_sha(path):
    b=Path(path).read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def normalized(p,a): return p.get(tuple(a),F(0))*F(fact(a))
def qrat(v): return sp.Rational(v.numerator,v.denominator)
def pidx(a,b): return z.pidx(a,b)
def read_csv(path,key):
    meta={}; body=[]
    for line in path.read_text().splitlines():
        if line.startswith('# '):
            x=line[2:]
            if '=' in x:
                k,v=x.split('=',1);meta[k]=v
        elif line.strip():body.append(line)
    rows=[]
    for r in csv.DictReader(body):
        rows.append({'pair':[int(r['a']),int(r['b'])],'alpha':[int(r['t']),int(r['x']),int(r['y']),int(r['z'])],key:r[key]})
    return rows,meta
def consume():
    S=json.load(open(S_PATH));V=json.load(open(V_PATH));Y=json.load(open(Y_PATH));U=json.load(open(U_PATH));xr,xm=read_csv(X_PATH,'value'); ar,am=read_csv(AA_PATH,'value')
    q=pmat()
    for key,val in S['Q2_normalized'].items():
        a,b,c,d=(int(ch) for ch in key);e=[0,0,0,0];e[c]+=1;e[d]+=1;q[a][b]=add(q[a][b],mono(tuple(e),F(val)/2))
    for src in (S['Q4_particular_normalized'],V['Q6_particular_normalized'],Y['Q8_particular_normalized']):
        for item in src:
            a,b=item['pair'];al=tuple(item['alpha']);t=mono(al,F(item['value'])/F(fact(al)));q[a][b]=add(q[a][b],t)
            if a!=b:q[b][a]=add(q[b][a],t)
    for a,b in product(range(N),repeat=2):q[a][b]=trunc(q[a][b],8)
    source=pmat()
    for item in U['Shat_normalized_sparse']:
        a,b=item['pair'];al=tuple(item['alpha']);t=mono(al,F(item['value'])/F(fact(al)));source[a][b]=add(source[a][b],t)
        if a!=b:source[b][a]=add(source[b][a],t)
    for rows in (xr,ar):
        for item in rows:
            a,b=item['pair'];al=tuple(item['alpha']);t=mono(al,F(item['value'])/F(fact(al)));source[a][b]=add(source[a][b],t)
            if a!=b:source[b][a]=add(source[b][a],t)
    for a,b in product(range(N),repeat=2):source[a][b]=trunc(source[a][b],8)
    auth={
      'S':git_blob_sha(S_PATH)==S_BLOB and S.get('terminal_commit')=='639b0bb33dcb5ea46d54f36b54a8d7dc733421b1' and len(S.get('Q4_particular_normalized',[]))==34,
      'V':git_blob_sha(V_PATH)==V_BLOB and V.get('source_digest')=='sha256:3a0767e620d7609ffe24e37db1392c5c5904eb60b2c7eb2b19eeda744d3d0685' and len(V.get('Q6_particular_normalized',[]))==88 and V.get('rank_M')==494 and V.get('rank_augmented')==494,
      'Y':git_blob_sha(Y_PATH)==Y_BLOB and len(Y.get('Q8_particular_normalized',[]))==180,
      'U':U.get('terminal_commit')=='20256a1779a3f76c46fcabe9f95cd0dd8c082305' and U.get('source_digest')=='sha256:fbdd20048f8f4e77618c5829e262538c4320a572c28e7bf6b36adb116e187dad' and len(U.get('Shat_normalized_sparse',[]))==90,
      'X':len(xr)==140 and xm.get('scientific_payload_sha256')=='7a85a8b78e6876810ecefc6e1b37efea956caa41f26d54f4f8b9dcf16ca45249',
      'AA':len(ar)==260 and am.get('scientific_payload_sha256')=='908baddad1138611869582c08d6d4069d591b7e840d606bb397a34bec57719c7',
    }
    return q,source,all(auth.values()),auth
def gauge_vector(q,gi,Gamma,degree):
    out=[]
    for b in range(N):
        val={}
        for a,c in product(range(N),repeat=2):
            cov=deriv(q[a][b],c)
            for r in range(N):
                cov=sub(cov,mul(Gamma[r][c][a],q[r][b],degree));cov=sub(cov,mul(Gamma[r][c][b],q[a][r],degree))
            val=add(val,mul(gi[a][c],cov,degree))
        out.append(trunc(val,degree))
    return out
def reduced_DG(q,gi,Gamma,Rlow,degree):
    first=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for c,a,b in product(range(N),repeat=3):
        val=deriv(q[a][b],c)
        for r in range(N):
            val=sub(val,mul(Gamma[r][c][a],q[r][b],degree+1));val=sub(val,mul(Gamma[r][c][b],q[a][r],degree+1))
        first[c][a][b]=trunc(val,degree+1)
    second=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for d,c,a,b in product(range(N),repeat=4):
        val=deriv(first[c][a][b],d)
        for r in range(N):
            val=sub(val,mul(Gamma[r][d][c],first[r][a][b],degree));val=sub(val,mul(Gamma[r][d][a],first[c][r][b],degree));val=sub(val,mul(Gamma[r][d][b],first[c][a][r],degree))
        second[d][c][a][b]=trunc(val,degree)
    qup=pmat()
    for c,d in product(range(N),repeat=2):
        val={}
        for e,f in product(range(N),repeat=2):val=add(val,mul(mul(gi[c][e],gi[d][f],degree),q[e][f],degree))
        qup[c][d]=trunc(val,degree)
    DG=pmat()
    for a,b in product(range(N),repeat=2):
        box={};curv={}
        for c,d in product(range(N),repeat=2):
            box=add(box,mul(gi[c][d],second[c][d][a][b],degree));curv=add(curv,mul(Rlow[a][c][b][d],qup[c][d],degree))
        DG[a][b]=trunc(scale(add(box,scale(curv,2)),-F(1,2)),degree)
    return DG
def unreduced_DG(q,g,gi,Gamma,degree=8):
    hdeg=degree+2;qtrace={}
    for a,b in product(range(N),repeat=2):qtrace=add(qtrace,mul(gi[a][b],q[a][b],hdeg))
    qtrace=trunc(qtrace,hdeg);h=pmat()
    for a,b in product(range(N),repeat=2):h[a][b]=trunc(sub(q[a][b],scale(mul(g[a][b],qtrace,hdeg),F(1,2))),hdeg)
    htrace={}
    for a,b in product(range(N),repeat=2):htrace=add(htrace,mul(gi[a][b],h[a][b],hdeg))
    htrace=trunc(htrace,hdeg);first=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for c,a,b in product(range(N),repeat=3):
        val=deriv(h[a][b],c)
        for r in range(N):
            val=sub(val,mul(Gamma[r][c][a],h[r][b],degree+1));val=sub(val,mul(Gamma[r][c][b],h[a][r],degree+1))
        first[c][a][b]=trunc(val,degree+1)
    second=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for d,c,a,b in product(range(N),repeat=4):
        val=deriv(first[c][a][b],d)
        for r in range(N):
            val=sub(val,mul(Gamma[r][d][c],first[r][a][b],degree));val=sub(val,mul(Gamma[r][d][a],first[c][r][b],degree));val=sub(val,mul(Gamma[r][d][b],first[c][a][r],degree))
        second[d][c][a][b]=trunc(val,degree)
    hess=pmat()
    for a,b in product(range(N),repeat=2):
        val=deriv(deriv(htrace,a),b)
        for r in range(N):val=sub(val,mul(Gamma[r][a][b],deriv(htrace,r),degree))
        hess[a][b]=trunc(val,degree)
    dRic=pmat()
    for a,b in product(range(N),repeat=2):
        t1={};t2={};box={}
        for c,d in product(range(N),repeat=2):
            t1=add(t1,mul(gi[c][d],second[d][a][b][c],degree));t2=add(t2,mul(gi[c][d],second[d][b][a][c],degree));box=add(box,mul(gi[c][d],second[c][d][a][b],degree))
        dRic[a][b]=trunc(scale(sub(add(t1,t2),add(box,hess[a][b])),F(1,2)),degree)
    dScalar={}
    for a,b in product(range(N),repeat=2):dScalar=add(dScalar,mul(gi[a][b],dRic[a][b],degree))
    dScalar=trunc(dScalar,degree);dG=pmat()
    for a,b in product(range(N),repeat=2):dG[a][b]=trunc(sub(dRic[a][b],scale(mul(g[a][b],dScalar,degree),F(1,2))),degree)
    return dG
def flat_reduced_q10(q10):
    out=pmat()
    for a,b in product(range(N),repeat=2):
        box={}
        for m in range(N): box=add(box,scale(deriv(deriv(q10[a][b],m),m),ETA[m]))
        out[a][b]=scale(box,-F(1,2))
    return out
def flat_unreduced_q10(q10):
    qtrace={}
    for a in range(N): qtrace=add(qtrace,scale(q10[a][a],ETA[a]))
    h=pmat()
    for a,b in product(range(N),repeat=2):
        h[a][b]=dict(q10[a][b])
        if a==b: h[a][b]=sub(h[a][b],scale(qtrace,F(ETA[a],2)))
    htrace={}
    for a in range(N): htrace=add(htrace,scale(h[a][a],ETA[a]))
    dRic=pmat()
    for a,b in product(range(N),repeat=2):
        t1={};t2={};box={}
        for c in range(N):
            t1=add(t1,scale(deriv(deriv(h[b][c],a),c),ETA[c]))
            t2=add(t2,scale(deriv(deriv(h[a][c],b),c),ETA[c]))
            box=add(box,scale(deriv(deriv(h[a][b],c),c),ETA[c]))
        hess=deriv(deriv(htrace,a),b)
        dRic[a][b]=scale(sub(add(t1,t2),add(box,hess)),F(1,2))
    dScalar={}
    for a in range(N): dScalar=add(dScalar,scale(dRic[a][a],ETA[a]))
    dG=pmat()
    for a,b in product(range(N),repeat=2):
        dG[a][b]=dict(dRic[a][b])
        if a==b:dG[a][b]=sub(dG[a][b],scale(dScalar,F(ETA[a],2)))
    return dG
def load_unreduced_lower(path):
    obj=json.load(open(path));out=pmat()
    for a,b in PAIRS:
        p={}
        for r in obj['unreduced_lower'][f'{a}{b}']:
            p[tuple(r['alpha'])]=F(r['n'],r['d'])
        out[a][b]=p
        if a!=b:out[b][a]=dict(p)
    return out,obj
def build_system():
    a7,a8,a9,a10=alphas(7),alphas(8),alphas(9),alphas(10);col={(p,al):p*len(a10)+j for p in range(10) for j,al in enumerate(a10)};rows=[];meta=[]
    for b in range(N):
        for al in a9:
            d={}
            for a in range(N):
                be=list(al);be[a]+=1;be=tuple(be);j=col[(pidx(a,b),be)];d[j]=d.get(j,0)+sp.Integer(ETA[a])
            rows.append(d);meta.append(('G',b,al))
    for pair in PAIRS:
        for al in a8:
            d={}
            for m in range(N):
                be=list(al);be[m]+=2;be=tuple(be);j=col[(pidx(*pair),be)];d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
            rows.append(d);meta.append(('F',pair,al))
    M=sp.MutableSparseMatrix(len(rows),10*len(a10),{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
    return M,rows,meta,a7,a8,a9,a10
def bianchi_matrix(meta,a7):
    lookup={m:i for i,m in enumerate(meta)};entries={};rr=0
    for b in range(N):
        for beta in a7:
            for m in range(N):
                al=list(beta);al[m]+=2;i=lookup[('G',b,tuple(al))];entries[(rr,i)]=entries.get((rr,i),0)+sp.Rational(ETA[m],2)
            for a in range(N):
                al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a);i=lookup[('F',pair,tuple(al))];entries[(rr,i)]=entries.get((rr,i),0)+sp.Integer(ETA[a])
            rr+=1
    return sp.MutableSparseMatrix(rr,2530,entries)
def add_q10(q,qv,a10):
    out=[[dict(q[a][b]) for b in range(N)] for a in range(N)]
    for idx,value in enumerate(qv):
        if value==0:continue
        p=idx//len(a10);al=a10[idx%len(a10)];a,b=PAIRS[p];fv=F(int(value.p),int(value.q));term=mono(al,fv/F(fact(al)));out[a][b]=add(out[a][b],term)
        if a!=b:out[b][a]=add(out[b][a],term)
    for a,b in product(range(N),repeat=2):out[a][b]=trunc(out[a][b],10)
    return out
