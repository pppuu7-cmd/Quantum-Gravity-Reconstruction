#!/usr/bin/env python3
"""Iter057Y exact unrestricted O(c6) Q2/Q4/Q6/Q8 response through source degree six.

Independent sparse-Fraction response implementation. Lower response/source and
background layers are consumed only from frozen terminal coefficient authorities.
"""
import argparse,csv,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import qgr_iter057w_decic_einstein_seed_sparse as w

N=w.N; K=w.K; ETA=w.ETA; ZERO=w.ZERO; PAIRS=w.PAIRS
GATE='ITER057Y-ONSHELL-FIRST-ORDER-Q2-Q4-Q6-Q8-RESPONSE'
PREREG='e372123b622bd1bb94e641b82097687a29416f65'
PASS='PASS_SCOPED_ITER057Y_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_Q8_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_SIXTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN'
FAIL='SCIENTIFIC_FAIL_SCOPED_ITER057Y_UNRESTRICTED_Q8_RESPONSE_SYSTEM_INCOMPATIBLE'
INVALID='INVALID_ITER057Y_RESTRICTED_ANSATZ_LOWER_RESPONSE_OR_SEED_CHANGE_OLD_SOURCE_REUSE_NUMERICAL_EXACTNESS_OR_CONTROL_FAILURE'
ITER057S='639b0bb33dcb5ea46d54f36b54a8d7dc733421b1'; S_DIGEST='sha256:b22aff7c02ef056aaed1df7ed06c06b181d4be601e3b05eac7b361856f7143f5'
ITER057U='20256a1779a3f76c46fcabe9f95cd0dd8c082305'; U_DIGEST='sha256:fbdd20048f8f4e77618c5829e262538c4320a572c28e7bf6b36adb116e187dad'
ITER057V='0d98273f8a1ec6071692571518f4faec1af8fa7b'; V_DIGEST='sha256:3a0767e620d7609ffe24e37db1392c5c5904eb60b2c7eb2b19eeda744d3d0685'
ITER057W='90b4a8d0512bffa70c488111a71e78690368c009'; R10_SHA='359b27d478b5b4927bc7df0c98a361f0177bba57e5550433662cd21138f75571'
ITER057X='4ab5592cfc6ef5fb69d3a96fa4433ef22d51af8b'; X_SHA='7a85a8b78e6876810ecefc6e1b37efea956caa41f26d54f4f8b9dcf16ca45249'
ROOT=Path(__file__).resolve().parents[1]
S_PATH=ROOT/'data'/'ITER057S_CANONICAL_Q2_Q4_RESPONSE.json'; V_PATH=ROOT/'data'/'ITER057V_CANONICAL_Q6_RESPONSE.json'
U_PATH=ROOT/'data'/'ITER057U_CANONICAL_SOURCE_0_2_4.json'; X_PATH=ROOT/'data'/'ITER057X_CANONICAL_SOURCE_DEGREE6.csv'
R10_PATH=ROOT/'data'/'ITER057W_CANONICAL_R10_NORMALIZED.csv'

const=w.const; mono=w.mono; add=w.add; neg=w.neg; sub=w.sub; scale=w.scale; mul=w.mul; deriv=w.deriv; trunc=w.trunc
pmat=w.pmat; fact=w.fact; alphas=w.alphas; fstr=w.fstr

def normalized(p,a):return p.get(tuple(a),F(0))*F(fact(a))
def qrat(v):return sp.Rational(v.numerator,v.denominator)
def pidx(a,b):return w.pidx(a,b)

def read_csv_authority(path,value_key):
    meta={};body=[]
    for line in path.read_text().splitlines():
        if line.startswith('# '):
            z=line[2:]
            if '=' in z:
                k,v=z.split('=',1);meta[k]=v
        elif line.strip():body.append(line)
    rows=[]
    for r in csv.DictReader(body):
        rows.append({'pair':[int(r['a']),int(r['b'])], 'alpha':[int(r['t']),int(r['x']),int(r['y']),int(r['z'])], value_key:r[value_key]})
    return rows,meta

def seed_metric10():
    g,baseprov,_,_=w.canonical_seed8(); rows,meta=read_csv_authority(R10_PATH,'R10_over_kappa5')
    pure=w.add_trace_reversed_layer(g,rows,5,'R10_over_kappa5',10)[1]
    prov=(baseprov and pure and len(rows)==283 and meta.get('preregistration')=='7e6336d195985b2059966eda64859da86c9e9d15' and meta.get('scientific_payload_sha256')==R10_SHA)
    return g,prov

def geometry8(g):
    gi,invok=w.inverse8(g)
    Gamma=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N),repeat=3):
        val={}
        for d in range(N):
            t=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            val=add(val,mul(gi[a][d],t,9))
        Gamma[a][b][c]=scale(trunc(val,9),F(1,2))
    Rup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    Rlow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val=sub(deriv(Gamma[a][d][b],c),deriv(Gamma[a][c][b],d))
        for e in range(N):val=add(val,sub(mul(Gamma[a][c][e],Gamma[e][d][b],8),mul(Gamma[a][d][e],Gamma[e][c][b],8)))
        Rup[a][b][c][d]=trunc(val,8)
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e in range(N):val=add(val,mul(g[a][e],Rup[e][b][c][d],8))
        Rlow[a][b][c][d]=trunc(val,8)
    Ric=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N):val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,8)
    Sc={}
    for a,b in product(range(N),repeat=2):Sc=add(Sc,mul(gi[a][b],Ric[a][b],8))
    Sc=trunc(Sc,8)
    vacuum=all(not Ric[a][b] for a,b in product(range(N),repeat=2)) and not Sc
    return gi,Gamma,Rlow,invok,vacuum

def consume_authorities():
    S=json.loads(S_PATH.read_text());V=json.loads(V_PATH.read_text());U=json.loads(U_PATH.read_text());xrows,xmeta=read_csv_authority(X_PATH,'value')
    s_ok=(S.get('terminal_commit')==ITER057S and S.get('source_digest')==S_DIGEST and len(S.get('Q4_particular_normalized',[]))==34)
    v_ok=(V.get('terminal_commit')==ITER057V and V.get('source_digest')==V_DIGEST and len(V.get('Q6_particular_normalized',[]))==88 and V.get('rank_M')==494 and V.get('rank_augmented')==494)
    urows=U.get('Shat_normalized_sparse',[])
    u_ok=(U.get('terminal_commit')==ITER057U and U.get('source_digest')==U_DIGEST and len([r for r in urows if r['degree']==4])==64)
    x_ok=(len(xrows)==140 and all(sum(r['alpha'])==6 for r in xrows) and xmeta.get('preregistration')=='b5f88ced655c4fa409c4ccb9c27eb84054ecfad7' and xmeta.get('scientific_payload_sha256')==X_SHA)
    q=pmat()
    for key,val in S['Q2_normalized'].items():
        a,b,c,d=(int(ch) for ch in key);e=[0,0,0,0];e[c]+=1;e[d]+=1;q[a][b]=add(q[a][b],mono(tuple(e),F(val)/2))
    for item in S['Q4_particular_normalized']:
        a,b=item['pair'];al=tuple(item['alpha']);t=mono(al,F(item['value'])/F(fact(al)));q[a][b]=add(q[a][b],t)
        if a!=b:q[b][a]=add(q[b][a],t)
    for item in V['Q6_particular_normalized']:
        a,b=item['pair'];al=tuple(item['alpha']);t=mono(al,F(item['value'])/F(fact(al)));q[a][b]=add(q[a][b],t)
        if a!=b:q[b][a]=add(q[b][a],t)
    for a,b in product(range(N),repeat=2):q[a][b]=trunc(q[a][b],6)
    source=pmat()
    for item in urows:
        a,b=item['pair'];al=tuple(item['alpha']);t=mono(al,F(item['value'])/F(fact(al)));source[a][b]=add(source[a][b],t)
        if a!=b:source[b][a]=add(source[b][a],t)
    for item in xrows:
        a,b=item['pair'];al=tuple(item['alpha']);t=mono(al,F(item['value'])/F(fact(al)));source[a][b]=add(source[a][b],t)
        if a!=b:source[b][a]=add(source[b][a],t)
    for a,b in product(range(N),repeat=2):source[a][b]=trunc(source[a][b],6)
    return q,source,(s_ok and v_ok and u_ok and x_ok),{'S':s_ok,'V':v_ok,'U':u_ok,'X':x_ok}

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
        for r in range(N):val=sub(val,mul(Gamma[r][c][a],q[r][b],degree+1));val=sub(val,mul(Gamma[r][c][b],q[a][r],degree+1))
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

def unreduced_DG(q,g,gi,Gamma,degree=6):
    hdeg=degree+2;qtrace={}
    for a,b in product(range(N),repeat=2):qtrace=add(qtrace,mul(gi[a][b],q[a][b],hdeg))
    qtrace=trunc(qtrace,hdeg);h=pmat()
    for a,b in product(range(N),repeat=2):h[a][b]=trunc(sub(q[a][b],scale(mul(g[a][b],qtrace,hdeg),F(1,2))),hdeg)
    htrace={}
    for a,b in product(range(N),repeat=2):htrace=add(htrace,mul(gi[a][b],h[a][b],hdeg))
    htrace=trunc(htrace,hdeg);first=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for c,a,b in product(range(N),repeat=3):
        val=deriv(h[a][b],c)
        for r in range(N):val=sub(val,mul(Gamma[r][c][a],h[r][b],degree+1));val=sub(val,mul(Gamma[r][c][b],h[a][r],degree+1))
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

def build_system():
    a5,a6,a7,a8=alphas(5),alphas(6),alphas(7),alphas(8);col={(p,al):p*len(a8)+j for p in range(10) for j,al in enumerate(a8)};rows=[];meta=[]
    for b in range(N):
        for al in a7:
            d={}
            for a in range(N):
                be=list(al);be[a]+=1;be=tuple(be);j=col[(pidx(a,b),be)];d[j]=d.get(j,0)+sp.Integer(ETA[a])
            rows.append(d);meta.append(('G',b,al))
    for pair in PAIRS:
        for al in a6:
            d={}
            for m in range(N):
                be=list(al);be[m]+=2;be=tuple(be);j=col[(pidx(*pair),be)];d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
            rows.append(d);meta.append(('F',pair,al))
    M=sp.MutableSparseMatrix(len(rows),10*len(a8),{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
    return M,rows,meta,a5,a6,a7,a8

def bianchi_matrix(meta,a5):
    lookup={m:i for i,m in enumerate(meta)};entries={};rr=0
    for b in range(N):
        for beta in a5:
            for m in range(N):
                al=list(beta);al[m]+=2;i=lookup[('G',b,tuple(al))];entries[(rr,i)]=entries.get((rr,i),0)+sp.Rational(ETA[m],2)
            for a in range(N):
                al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a);i=lookup[('F',pair,tuple(al))];entries[(rr,i)]=entries.get((rr,i),0)+sp.Integer(ETA[a])
            rr+=1
    return sp.MutableSparseMatrix(rr,1320,entries)

def add_q8(q,qv,a8):
    out=[[dict(q[a][b]) for b in range(N)] for a in range(N)]
    for idx,value in enumerate(qv):
        if value==0:continue
        p=idx//len(a8);al=a8[idx%len(a8)];a,b=PAIRS[p];fv=F(int(value.p),int(value.q));term=mono(al,fv/F(fact(al)));out[a][b]=add(out[a][b],term)
        if a!=b:out[b][a]=add(out[b][a],term)
    for a,b in product(range(N),repeat=2):out[a][b]=trunc(out[a][b],8)
    return out

def compute():
    g,bgprov=seed_metric10();gi,Gamma,Rlow,invok,vacuum=geometry8(g);qlower,source,auth_ok,auth=consume_authorities()
    gauge0=gauge_vector(qlower,gi,Gamma,7);DG0=reduced_DG(qlower,gi,Gamma,Rlow,6);field0=pmat()
    for a,b in product(range(N),repeat=2):field0[a][b]=trunc(sub(DG0[a][b],source[a][b]),6)
    lower_gauge=all(not trunc(v,5) for v in gauge0);lower_field=all(not trunc(field0[a][b],4) for a,b in PAIRS)
    fresh_g7=sum(bool(normalized(gauge0[b],al)) for b in range(N) for al in alphas(7));fresh_f6=sum(bool(normalized(field0[a][b],al)) for a,b in PAIRS for al in alphas(6))
    M,rows,meta,a5,a6,a7,a8=build_system();rhs=[]
    for b in range(N):
        for al in a7:rhs.append(-qrat(normalized(gauge0[b],al)))
    for a,b in PAIRS:
        for al in a6:rhs.append(-qrat(normalized(field0[a][b],al)))
    rhsv=sp.Matrix(rhs);rankM=DomainMatrix.from_Matrix(M).to_field().rank();B=bianchi_matrix(meta,a5);brank=DomainMatrix.from_Matrix(B).to_field().rank();bann=(B*M==sp.zeros(224,M.cols));compat=B*rhsv;compat_nz=sum(v!=0 for v in compat)
    Raug,piv=DomainMatrix.from_Matrix(M.row_join(rhsv)).to_field().rref();piv=tuple(piv);rankAug=len(piv);Raug=Raug.to_Matrix();consistent=(rankAug==rankM and all(j<M.cols for j in piv));qv=[sp.Integer(0)]*M.cols
    if consistent:
        for row,j in enumerate(piv):qv[j]=sp.factor(Raug[row,M.cols])
    linres=[sp.factor(sum(v*qv[j] for j,v in row.items())-rhs[i]) for i,row in enumerate(rows)];q8=[]
    for idx,value in enumerate(qv):
        if value==0:continue
        p=idx//len(a8);al=a8[idx%len(a8)];q8.append({'pair':list(PAIRS[p]),'alpha':list(al),'value':str(value),'over_kappa6':str(sp.factor(value/qrat(K**6)))})
    qtotal=add_q8(qlower,qv,a8);gaugeT=gauge_vector(qtotal,gi,Gamma,7);DGT=reduced_DG(qtotal,gi,Gamma,Rlow,6);unred=unreduced_DG(qtotal,g,gi,Gamma,6)
    redres={};unres={}
    for a,b in PAIRS:redres[f'{a}{b}']=sub(DGT[a][b],source[a][b]);unres[f'{a}{b}']=sub(unred[a][b],source[a][b])
    preserve=all(not trunc(sub(qtotal[a][b],qlower[a][b]),7) for a,b in product(range(N),repeat=2))
    controls={
      'A_frozen_parent_authorities_exact':auth_ok and bgprov,'A_background_inverse_through_degree8':invok,'A_background_vacuum_through_degree8':vacuum,
      'A_lower_Q2Q4Q6_gauge_through_degree5_zero':lower_gauge,'A_lower_Q2Q4Q6_field_through_degree4_zero':lower_field,'B_iter057X_source_through_degree6_exact':auth['X'] and auth['U'],
      'C_fresh_curved_degree7_gauge_and_degree6_field_residual_computed':True,'D_matrix_shape_1320x1650':M.rows==1320 and M.cols==1650,
      'E_rank_M_exact_1096':rankM==1096,'E_left_nullity_exact_224':M.rows-rankM==224,'E_nullity_exact_554':M.cols-rankM==554,'E_canonical_Bianchi_rank_224':B.rows==224 and brank==224,'E_canonical_Bianchi_annihilates_M':bann,
      'F_rank_augmented_equals_rank_M':rankAug==rankM==1096,'F_all_224_compatibility_contractions_zero':compat_nz==0,'G_exact_affine_residual_zero':all(v==0 for v in linres),
      'H_Q8_preserves_lower_response_through_order7':preserve,'I_full_covariant_deDonder_through_degree7_zero':all(not v for v in gaugeT),
      'J_reduced_DG_minus_source_through_degree6_zero':all(not v for v in redres.values()),'J_unreduced_DG_minus_source_through_degree6_zero':all(not v for v in unres.values()),'K_exact_zero_uses_no_tolerance':True}
    passed=all(controls.values());classification=PASS if passed else (FAIL if rankM==1096 and (rankAug>rankM or compat_nz) else INVALID)
    return {'gate':GATE,'preregistration_commit':PREREG,'iter057V_commit':ITER057V,'iter057W_commit':ITER057W,'iter057X_commit':ITER057X,'pass':passed,'classification':classification,'controls':controls,'authority_subcontrols':auth,
      'matrix_shape':[M.rows,M.cols],'matrix_nnz':len(M.todok()),'rank_M':rankM,'rank_augmented':rankAug,'left_nullity':M.rows-rankM,'nullity':M.cols-rankM,'bianchi_rank':brank,'compatibility_nonzero_count':compat_nz,
      'fresh_fixed_Q2Q4Q6_degree7_gauge_residual_nonzero_count':fresh_g7,'fresh_fixed_Q2Q4Q6_degree6_field_residual_nonzero_count':fresh_f6,'Q8_particular_nonzero_count':len(q8),'Q8_particular_normalized':q8,
      'full_deDonder_nonzero_component_count':sum(bool(v) for v in gaugeT),'reduced_DG_minus_source_nonzero_component_count':sum(bool(v) for v in redres.values()),'unreduced_DG_minus_source_nonzero_component_count':sum(bool(v) for v in unres.values()),
      'exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out');args=ap.parse_args();out=compute();txt=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.out:Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(txt)
    print(txt,end='')
    if not out['pass']:raise SystemExit(2)
if __name__=='__main__':main()
