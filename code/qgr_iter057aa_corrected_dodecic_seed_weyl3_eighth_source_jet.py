#!/usr/bin/env python3
"""Iter057AA exact Weyl3 Euler source through coordinate degree eight on canonical R12 seed."""
import argparse,csv,json
from fractions import Fraction as F
from itertools import permutations,product
from pathlib import Path

import qgr_iter057z_dodecic_einstein_seed_completion as z

N=z.N; K=z.K; ETA=z.ETA; ZERO=z.ZERO; PAIRS=z.PAIRS
GATE='ITER057AA-CORRECTED-DODECIC-SEED-WEYL3-EIGHTH-SOURCE-JET'
PREREG='84a6a3f060b28bace577ea76eadc0aed2c429014'
ITER057U='20256a1779a3f76c46fcabe9f95cd0dd8c082305'
ITER057X='4ab5592cfc6ef5fb69d3a96fa4433ef22d51af8b'
ITER057Z='bb4fa6ccbf21e2a063467a1b0839223744866995'
R12_DATA_COMMIT='5bfe62e887dd627c76c41080187eadc3d95e0c45'
R12_PAYLOAD_SHA='e62c84d0ad586322d588093ddbf067c0ad185478a042e3c877d24e7809122c6b'
X_PAYLOAD_SHA='7a85a8b78e6876810ecefc6e1b37efea956caa41f26d54f4f8b9dcf16ca45249'
ROOT=Path(__file__).resolve().parents[1]
R12_PATH=ROOT/'data'/'ITER057Z_CANONICAL_R12_NORMALIZED.csv'
U_PATH=ROOT/'data'/'ITER057U_CANONICAL_SOURCE_0_2_4.json'
X_PATH=ROOT/'data'/'ITER057X_CANONICAL_SOURCE_DEGREE6.csv'

const=z.const; mono=z.mono; add=z.add; neg=z.neg; sub=z.sub; scale=z.scale
mul=z.mul; deriv=z.deriv; trunc=z.trunc; pmat=z.pmat; fact=z.fact; alphas=z.alphas; fstr=z.fstr

def psign(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def read_csv_with_meta(path):
    meta={}; body=[]
    for line in path.read_text().splitlines():
        if line.startswith('# '):
            x=line[2:]
            if '=' in x:
                k,v=x.split('=',1); meta[k]=v
        elif line.strip(): body.append(line)
    return meta,list(csv.DictReader(body))

def seed_metric12():
    g,baseprov,_,_,_=z.canonical_seed10()
    meta,raw=read_csv_with_meta(R12_PATH)
    rows=[{'pair':[int(r['a']),int(r['b'])],
           'alpha':[int(r['t']),int(r['x']),int(r['y']),int(r['z'])],
           'R12_over_kappa6':r['R12_over_kappa6']} for r in raw]
    r12,pure=z.add_trace_reversed_layer(g,rows,6,'R12_over_kappa6',12)
    prov=(baseprov and pure and len(rows)==469 and all(sum(r['alpha'])==12 for r in rows)
          and meta.get('preregistration')=='f1c04bbfdb7848ab79708beb902ccdb315fbd5ed'
          and meta.get('scientific_payload_sha256')==R12_PAYLOAD_SHA
          and meta.get('rank_M')=='3436' and meta.get('rank_augmented')=='3436'
          and meta.get('compatibility_nonzero_count')=='0')
    return g,prov,rows,meta

def geometry10(g):
    gi,invok=z.inverse10(g)
    Gamma=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N),repeat=3):
        val={}
        for d in range(N):
            t=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            val=add(val,mul(gi[a][d],t,11))
        Gamma[a][b][c]=scale(trunc(val,11),F(1,2))
    Rup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val=sub(deriv(Gamma[a][d][b],c),deriv(Gamma[a][c][b],d))
        for e in range(N):
            val=add(val,sub(mul(Gamma[a][c][e],Gamma[e][d][b],10),mul(Gamma[a][d][e],Gamma[e][c][b],10)))
        Rup[a][b][c][d]=trunc(val,10)
    Rlow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e in range(N): val=add(val,mul(g[a][e],Rup[e][b][c][d],10))
        Rlow[a][b][c][d]=trunc(val,10)
    Ric=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N): val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,10)
    Scal={}
    for a,b in product(range(N),repeat=2): Scal=add(Scal,mul(gi[a][b],Ric[a][b],10))
    Scal=trunc(Scal,10)
    Ein=pmat()
    for a,b in product(range(N),repeat=2):
        Ein[a][b]=trunc(add(Ric[a][b],scale(mul(g[a][b],Scal,10),-F(1,2))),10)
    return gi,Gamma,Rlow,Ric,Scal,Ein,invok

def read_expected_lower():
    u=json.loads(U_PATH.read_text())
    u_ok=(u.get('pass') is True and u.get('classification')==
          'PASS_SCOPED_ITER057U_CORRECTED_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_FOURTH_EVEN_ORDER__O_C6_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED'
          and len(u.get('Shat_normalized_sparse',[]))==90)
    exp={}
    for r in u.get('Shat_normalized_sparse',[]):
        d=int(r['degree'])
        if d<=4: exp[(r['pair'][0],r['pair'][1],tuple(r['alpha']))]=F(r['value'])
    xm,xrows=read_csv_with_meta(X_PATH)
    x_ok=(xm.get('preregistration')=='b5f88ced655c4fa409c4ccb9c27eb84054ecfad7'
          and xm.get('implementation')=='920b73f8430983255081b9bcd3ec6d222b737b08'
          and xm.get('scientific_payload_sha256')==X_PAYLOAD_SHA and len(xrows)==140)
    for r in xrows:
        alpha=(int(r['t']),int(r['x']),int(r['y']),int(r['z']))
        exp[(int(r['a']),int(r['b']),alpha)]=F(r['value'])
    return exp,u_ok,x_ok

def compute():
    g,prov,r12rows,r12meta=seed_metric12()
    gi,Gamma,Rlow,Ric,Scal,Ein,invok=geometry10(g)
    ricci_zero=all(not Ric[a][b] for a,b in product(range(N),repeat=2))
    scalar_zero=not Scal
    einstein_zero=all(not Ein[a][b] for a,b in product(range(N),repeat=2))
    seed_ok=prov and invok and ricci_zero and scalar_zero and einstein_zero
    if not seed_ok:
        controls={'A_iter057Z_R12_provenance_exact':prov,'A_inverse10':invok,'A_Ricci10_zero':ricci_zero,
                  'A_scalar10_zero':scalar_zero,'A_Einstein10_zero':einstein_zero}
        return {'gate':GATE,'preregistration_commit':PREREG,'controls':controls,'pass':False,
                'classification':'INVALID_ITER057AA_SEED_MUTATION_OLD_SOURCE_REUSE_NORMALIZATION_IDENTITY_OR_EXACTNESS_CONTROL_FAILURE',
                'exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT'}
    C=Rlow
    Cup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,r,s in product(range(N),repeat=4):
        val={}
        for m,n in product(range(N),repeat=2):
            val=add(val,mul(mul(gi[r][m],gi[s][n],10),C[a][b][m][n],10))
        Cup[a][b][r][s]=trunc(val,10)
    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for r,s in product(range(N),repeat=2): val=add(val,mul(Cup[a][b][r][s],C[r][s][c][d],10))
        Q[a][b][c][d]=trunc(val,10)
    perms=list(permutations(range(4)))
    Qr=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        inds=(a,b,c,d); alt={}
        for p in perms: alt=add(alt,scale(Q[inds[p[0]]][inds[p[1]]][inds[p[2]]][inds[p[3]]],F(psign(p),24)))
        Qr[a][b][c][d]=trunc(sub(Q[a][b][c][d],alt),10)
    QRic=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a,c in product(range(N),repeat=2): val=add(val,mul(gi[a][c],Qr[a][b][c][d],10))
        QRic[b][d]=trunc(val,10)
    QSc={}
    for b,d in product(range(N),repeat=2): QSc=add(QSc,mul(gi[b][d],QRic[b][d],10))
    QSc=trunc(QSc,10)
    Plow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rt=add(sub(mul(g[a][c],QRic[d][b],10),mul(g[a][d],QRic[c][b],10)),
               add(neg(mul(g[b][c],QRic[d][a],10)),mul(g[b][d],QRic[c][a],10)))
        rt=scale(rt,F(1,2))
        gg=scale(sub(mul(g[a][c],g[d][b],10),mul(g[a][d],g[c][b],10)),F(1,2))
        Plow[a][b][c][d]=scale(trunc(add(sub(Qr[a][b][c][d],rt),scale(mul(QSc,gg,10),F(1,3))),10),3)
    T1=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,j,m,n in product(range(N),repeat=4):
        val={}
        for i in range(N): val=add(val,mul(gi[a][i],Plow[i][j][m][n],10))
        T1[a][j][m][n]=trunc(val,10)
    T2=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,m,n in product(range(N),repeat=4):
        val={}
        for j in range(N): val=add(val,mul(gi[b][j],T1[a][j][m][n],10))
        T2[a][b][m][n]=trunc(val,10)
    T3=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,n in product(range(N),repeat=4):
        val={}
        for m in range(N): val=add(val,mul(gi[c][m],T2[a][b][m][n],10))
        T3[a][b][c][n]=trunc(val,10)
    P=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for n in range(N): val=add(val,mul(gi[d][n],T3[a][b][c][n],10))
        P[a][b][c][d]=trunc(val,10)
    I3={}
    for a,b,c,d,e,f in product(range(N),repeat=6):
        I3=add(I3,mul(mul(Cup[a][b][c][d],Cup[c][d][e][f],8),Cup[e][f][a][b],8))
    I3=trunc(I3,8)
    PR={}
    for a,b,c,d in product(range(N),repeat=4): PR=add(PR,mul(P[a][b][c][d],Rlow[a][b][c][d],8))
    PR=trunc(PR,8); homogeneity=not trunc(sub(PR,scale(I3,3)),8)
    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,b,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=deriv(P[a][m][b][n],a)
            for r in range(N):
                term=add(term,mul(Gamma[a][a][r],P[r][m][b][n],9))
                term=add(term,mul(Gamma[m][a][r],P[a][r][b][n],9))
                term=add(term,mul(Gamma[b][a][r],P[a][m][r][n],9))
                term=add(term,mul(Gamma[n][a][r],P[a][m][b][r],9))
            val=add(val,term)
        FD[m][b][n]=trunc(val,9)
    D=pmat()
    for m,n in product(range(N),repeat=2):
        val={}
        for b in range(N):
            term=deriv(FD[m][b][n],b)
            for r in range(N):
                term=add(term,mul(Gamma[m][b][r],FD[r][b][n],8))
                term=add(term,mul(Gamma[b][b][r],FD[m][r][n],8))
                term=add(term,mul(Gamma[n][b][r],FD[m][b][r],8))
            val=add(val,term)
        D[m][n]=trunc(val,8)
    def bone(a,b):
        val={}
        for c,d,e,f in product(range(N),repeat=4):
            val=add(val,mul(mul(P[a][c][d][e],gi[b][f],8),Rlow[f][c][d][e],8))
        return trunc(val,8)
    B=pmat()
    for a,b in product(range(N),repeat=2): B[a][b]=scale(add(bone(a,b),bone(b,a)),F(1,2))
    Eup=pmat()
    for a,b in product(range(N),repeat=2):
        v=add(neg(B[a][b]),scale(D[a][b],-2)); v=add(v,scale(mul(gi[a][b],I3,8),F(1,2)))
        Eup[a][b]=trunc(v,8)
    Edown=pmat()
    for a,b in product(range(N),repeat=2):
        v={}
        for c,d in product(range(N),repeat=2): v=add(v,mul(mul(g[a][c],g[b][d],8),Eup[c][d],8))
        Edown[a][b]=trunc(v,8)
    sym=all(not trunc(sub(Edown[a][b],Edown[b][a]),8) for a,b in product(range(N),repeat=2))
    trace={}
    for a,b in product(range(N),repeat=2): trace=add(trace,mul(gi[a][b],Edown[a][b],8))
    trace_ward=not trunc(add(trunc(trace,8),I3),8)
    noether=[]
    for b in range(N):
        v={}
        for a in range(N):
            v=add(v,deriv(Eup[a][b],a))
            for r in range(N):
                v=add(v,mul(Gamma[a][a][r],Eup[r][b],7))
                v=add(v,mul(Gamma[b][a][r],Eup[a][r],7))
        noether.append(trunc(v,7))
    noether_ok=all(not v for v in noether)
    source_sparse=[]; source_by_key={}; odd=[]; counts={d:0 for d in range(9)}; d8=d8time=d8off=0
    for a,b in PAIRS:
        S=neg(Edown[a][b])
        for alpha,raw in sorted(S.items()):
            deg=sum(alpha)
            if deg>8: continue
            norm=raw*F(fact(alpha))
            if not norm: continue
            counts[deg]+=1; source_by_key[(a,b,alpha)]=norm
            if deg in (1,3,5,7): odd.append((a,b,alpha,norm))
            rec={'pair':[a,b],'alpha':list(alpha),'degree':deg,'value':fstr(norm)}
            if deg%2==0: rec[f'over_kappa{3+deg//2}']=fstr(norm/(K**(3+deg//2)))
            source_sparse.append(rec)
            if deg==8:
                d8+=1; d8time+=bool(alpha[0]); d8off+=(a!=b)
    expected,u_ok,x_ok=read_expected_lower(); mismatches=[]
    for deg in (0,2,4,6):
        for a,b in PAIRS:
            for alpha in alphas(deg):
                got=source_by_key.get((a,b,alpha),F(0)); exp=expected.get((a,b,alpha),F(0))
                if got!=exp: mismatches.append({'pair':[a,b],'alpha':list(alpha),'got':fstr(got),'expected':fstr(exp)})
    lower_match=u_ok and x_ok and not mismatches
    basis_by_degree={str(d):10*len(alphas(d)) for d in range(9)}; basis_total=sum(basis_by_degree.values())
    controls={
      'A_iter057Z_R12_provenance_exact':prov and len(r12rows)==469,
      'A_inverse_identity_through_degree10':invok,
      'A_seed_Ricci_through_degree10_zero':ricci_zero,
      'A_seed_scalar_through_degree10_zero':scalar_zero,
      'A_seed_Einstein_through_degree10_zero':einstein_zero,
      'B_source_computed_directly_through_degree8':True,
      'C_P_dot_R_equals_3I3_through_degree8':homogeneity,
      'D_E_W3_down_symmetric_through_degree8':sym,
      'D_trace_Ward_through_degree8':trace_ward,
      'E_Noether_divergence_through_degree7':noether_ok,
      'F_complete_Iter057U_X_degree0_2_4_6_replay':lower_match,
      'F_odd_source_degrees_1_3_5_7_zero':not odd,
      'G_degree8_complete_basis_1650':basis_by_degree['8']==1650,
      'G_full_basis_count_4950':basis_total==4950,
      'H_no_tolerance':True,
    }
    passed=all(controls.values())
    classification=('PASS_SCOPED_ITER057AA_CORRECTED_DODECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_EIGHTH_EVEN_ORDER__O_C6_Q10_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED' if passed else
                    'INVALID_ITER057AA_SEED_MUTATION_OLD_SOURCE_REUSE_NORMALIZATION_IDENTITY_OR_EXACTNESS_CONTROL_FAILURE')
    return {'gate':GATE,'preregistration_commit':PREREG,'iter057U_commit':ITER057U,'iter057X_commit':ITER057X,'iter057Z_commit':ITER057Z,
            'r12_data_commit':R12_DATA_COMMIT,'r12_payload_sha256':R12_PAYLOAD_SHA,'kappa':fstr(K),'controls':controls,'pass':passed,
            'basis_count_by_degree':basis_by_degree,'basis_total':basis_total,'source_nonzero_count_by_degree':{str(k):v for k,v in counts.items()},
            'degree8_nonzero_count':d8,'degree8_time_containing_nonzero_count':d8time,'degree8_offdiagonal_nonzero_count':d8off,
            'Shat_normalized_sparse':source_sparse,'lower_replay_mismatches':mismatches,'I3_origin_over_kappa3':fstr(I3.get(ZERO,F(0))/(K**3)),
            'classification':classification,'exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out'); args=ap.parse_args(); o=compute(); txt=json.dumps(o,indent=2,sort_keys=True)+'\n'
    if args.out:
        p=Path(args.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(txt)
    print(json.dumps({k:o[k] for k in ['pass','classification','source_nonzero_count_by_degree','degree8_nonzero_count','degree8_time_containing_nonzero_count','degree8_offdiagonal_nonzero_count','I3_origin_over_kappa3']},indent=2))
    print(json.dumps(o['controls'],indent=2,sort_keys=True))
    if not o['pass']: raise SystemExit(2)
if __name__=='__main__': main()
