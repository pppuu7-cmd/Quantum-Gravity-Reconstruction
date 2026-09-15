#!/usr/bin/env python3
"""Iter057X exact corrected-decic-seed Weyl3 Euler source through coordinate degree six."""
import argparse, csv, json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

import qgr_iter057u_corrected_seed_weyl3_fourth_source_jet as u
import qgr_iter057w_decic_einstein_seed_sparse as w

N=w.N; K=w.K; ETA=w.ETA; ZERO=w.ZERO; PAIRS=w.PAIRS
GATE='ITER057X-CORRECTED-DECIC-SEED-WEYL3-SIXTH-SOURCE-JET'
PREREG='b5f88ced655c4fa409c4ccb9c27eb84054ecfad7'
ITER057U='20256a1779a3f76c46fcabe9f95cd0dd8c082305'
ITER057W='90b4a8d0512bffa70c488111a71e78690368c009'
R10_DATA_COMMIT='e8982c84cc3b4baa0ca40ed8ff7876164b728880'
R10_PAYLOAD_SHA='359b27d478b5b4927bc7df0c98a361f0177bba57e5550433662cd21138f75571'
R10_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057W_CANONICAL_R10_NORMALIZED.csv'
U_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057U_CANONICAL_SOURCE_0_2_4.json'

const=w.const; mono=w.mono; add=w.add; neg=w.neg; sub=w.sub
scale=w.scale; mul=w.mul; deriv=w.deriv; trunc=w.trunc
pmat=w.pmat; fact=w.fact; alphas=w.alphas; fstr=w.fstr
psign=u.psign


def read_r10():
    lines=R10_PATH.read_text().splitlines()
    meta={}; data=[]; body=[]
    for line in lines:
        if line.startswith('# '):
            z=line[2:]
            if '=' in z:
                k,v=z.split('=',1); meta[k]=v
        elif line.strip(): body.append(line)
    for row in csv.DictReader(body):
        data.append({'pair':[int(row['a']),int(row['b'])],
                     'alpha':[int(row['t']),int(row['x']),int(row['y']),int(row['z'])],
                     'R10_over_kappa5':row['R10_over_kappa5']})
    prov=(meta.get('preregistration')=='7e6336d195985b2059966eda64859da86c9e9d15' and
          meta.get('implementation')=='ad14ccd72a1a3ca75ab95acb0e294c6707b14627' and
          meta.get('scientific_payload_sha256')==R10_PAYLOAD_SHA and len(data)==283 and
          all(sum(x['alpha'])==10 for x in data))
    return data,meta,prov


def seed_metric10():
    g,baseprov,_,_=w.canonical_seed8()
    rows,meta,p10=read_r10()
    _,pure=w.add_trace_reversed_layer(g,rows,5,'R10_over_kappa5',10)
    return g,(baseprov and p10 and pure),len(rows),meta


def normalized(poly,alpha):
    return poly.get(tuple(alpha),F(0))*F(fact(alpha))


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
    for a,b,c,d in product(range(N),repeat=4):
        val=sub(deriv(Gamma[a][d][b],c),deriv(Gamma[a][c][b],d))
        for e in range(N):
            val=add(val,sub(mul(Gamma[a][c][e],Gamma[e][d][b],8),mul(Gamma[a][d][e],Gamma[e][c][b],8)))
        Rup[a][b][c][d]=trunc(val,8)
    Rlow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e in range(N): val=add(val,mul(g[a][e],Rup[e][b][c][d],8))
        Rlow[a][b][c][d]=trunc(val,8)
    Ric=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N): val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,8)
    Scal={}
    for a,b in product(range(N),repeat=2): Scal=add(Scal,mul(gi[a][b],Ric[a][b],8))
    Scal=trunc(Scal,8)
    Ein=pmat()
    for a,b in product(range(N),repeat=2):
        Ein[a][b]=trunc(sub(Ric[a][b],scale(mul(g[a][b],Scal,8),F(1,2))),8)
    return gi,Gamma,Rlow,Ric,Scal,Ein,invok


def compute():
    g,prov,r10_count,r10meta=seed_metric10()
    gi,Gamma,Rlow,Ric,Scal,Ein,invok=geometry8(g)
    ricci_zero=all(not Ric[a][b] for a,b in product(range(N),repeat=2))
    scalar_zero=not Scal
    einstein_zero=all(not Ein[a][b] for a,b in product(range(N),repeat=2))
    seed_ok=(prov and r10_count==283 and invok and ricci_zero and scalar_zero and einstein_zero)
    if not seed_ok:
        controls={
          'A_iter057W_R10_provenance_exact':prov and r10_count==283,
          'B_inverse_identity_through_degree8':invok,
          'B_seed_Ricci_through_degree8_zero':ricci_zero,
          'B_seed_scalar_through_degree8_zero':scalar_zero,
          'B_seed_Einstein_through_degree8_zero':einstein_zero,
        }
        return {'gate':GATE,'preregistration_commit':PREREG,'iter057W_commit':ITER057W,
                'controls':controls,'pass':False,
                'classification':'INVALID_ITER057X_SEED_MUTATION_OLD_SOURCE_REUSE_RESTRICTED_ANSATZ_NORMALIZATION_OR_EXACTNESS_CONTROL',
                'exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT'}

    C=Rlow
    Cup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,r1,s1 in product(range(N),repeat=4):
        val={}
        for m,n in product(range(N),repeat=2):
            val=add(val,mul(mul(gi[r1][m],gi[s1][n],8),C[a][b][m][n],8))
        Cup[a][b][r1][s1]=trunc(val,8)

    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for rr,ss in product(range(N),repeat=2): val=add(val,mul(Cup[a][b][rr][ss],C[rr][ss][c][d],8))
        Q[a][b][c][d]=trunc(val,8)

    perms=list(permutations(range(4)))
    Qr=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        inds=(a,b,c,d); alt={}
        for pp in perms: alt=add(alt,scale(Q[inds[pp[0]]][inds[pp[1]]][inds[pp[2]]][inds[pp[3]]],F(psign(pp),24)))
        Qr[a][b][c][d]=trunc(sub(Q[a][b][c][d],alt),8)

    QRic=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a,c in product(range(N),repeat=2): val=add(val,mul(gi[a][c],Qr[a][b][c][d],8))
        QRic[b][d]=trunc(val,8)
    QSc={}
    for b,d in product(range(N),repeat=2): QSc=add(QSc,mul(gi[b][d],QRic[b][d],8))
    QSc=trunc(QSc,8)

    Plow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rt=add(sub(mul(g[a][c],QRic[d][b],8),mul(g[a][d],QRic[c][b],8)),
               add(neg(mul(g[b][c],QRic[d][a],8)),mul(g[b][d],QRic[c][a],8)))
        rt=scale(rt,F(1,2))
        gg=scale(sub(mul(g[a][c],g[d][b],8),mul(g[a][d],g[c][b],8)),F(1,2))
        Plow[a][b][c][d]=scale(trunc(add(sub(Qr[a][b][c][d],rt),scale(mul(QSc,gg,8),F(1,3))),8),3)

    P=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for i,j,m,n in product(range(N),repeat=4):
            raiser=mul(mul(gi[a][i],gi[b][j],8),mul(gi[c][m],gi[d][n],8),8)
            val=add(val,mul(raiser,Plow[i][j][m][n],8))
        P[a][b][c][d]=trunc(val,8)

    I3={}
    for a,b,c,d,e,f in product(range(N),repeat=6):
        I3=add(I3,mul(mul(Cup[a][b][c][d],Cup[c][d][e][f],6),Cup[e][f][a][b],6))
    I3=trunc(I3,6)
    PR={}
    for a,b,c,d in product(range(N),repeat=4): PR=add(PR,mul(P[a][b][c][d],Rlow[a][b][c][d],6))
    PR=trunc(PR,6)
    homogeneity=not trunc(sub(PR,scale(I3,3)),6)

    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,b,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=deriv(P[a][m][b][n],a)
            for rr in range(N):
                term=add(term,mul(Gamma[a][a][rr],P[rr][m][b][n],7))
                term=add(term,mul(Gamma[m][a][rr],P[a][rr][b][n],7))
                term=add(term,mul(Gamma[b][a][rr],P[a][m][rr][n],7))
                term=add(term,mul(Gamma[n][a][rr],P[a][m][b][rr],7))
            val=add(val,term)
        FD[m][b][n]=trunc(val,7)
    D=pmat()
    for m,n in product(range(N),repeat=2):
        val={}
        for b in range(N):
            term=deriv(FD[m][b][n],b)
            for rr in range(N):
                term=add(term,mul(Gamma[m][b][rr],FD[rr][b][n],6))
                term=add(term,mul(Gamma[b][b][rr],FD[m][rr][n],6))
                term=add(term,mul(Gamma[n][b][rr],FD[m][b][rr],6))
            val=add(val,term)
        D[m][n]=trunc(val,6)

    def bone(a,b):
        val={}
        for c,d,e,f in product(range(N),repeat=4):
            val=add(val,mul(mul(P[a][c][d][e],gi[b][f],6),Rlow[f][c][d][e],6))
        return trunc(val,6)
    B=pmat()
    for a,b in product(range(N),repeat=2): B[a][b]=scale(add(bone(a,b),bone(b,a)),F(1,2))

    Eup=pmat()
    for a,b in product(range(N),repeat=2):
        val=add(neg(B[a][b]),scale(D[a][b],-2))
        val=add(val,scale(mul(gi[a][b],I3,6),F(1,2)))
        Eup[a][b]=trunc(val,6)
    Edown=pmat()
    for a,b in product(range(N),repeat=2):
        val={}
        for c,d in product(range(N),repeat=2): val=add(val,mul(mul(g[a][c],g[b][d],6),Eup[c][d],6))
        Edown[a][b]=trunc(val,6)

    sym=all(not trunc(sub(Edown[a][b],Edown[b][a]),6) for a,b in product(range(N),repeat=2))
    trace={}
    for a,b in product(range(N),repeat=2): trace=add(trace,mul(gi[a][b],Edown[a][b],6))
    trace_ward=not trunc(add(trunc(trace,6),I3),6)
    noether=[]
    for b in range(N):
        val={}
        for a in range(N):
            val=add(val,deriv(Eup[a][b],a))
            for rr in range(N):
                val=add(val,mul(Gamma[a][a][rr],Eup[rr][b],5))
                val=add(val,mul(Gamma[b][a][rr],Eup[a][rr],5))
        noether.append(trunc(val,5))
    noether_ok=all(not x for x in noether)

    source_sparse=[]; odd=[]; counts={d:0 for d in range(7)}; d6=0; d6time=0; d6off=0
    source_by_key={}
    for a,b in PAIRS:
        S=neg(Edown[a][b])
        for alpha,raw in sorted(S.items()):
            deg=sum(alpha)
            if deg>6: continue
            norm=raw*F(fact(alpha))
            if not norm: continue
            counts[deg]+=1; source_by_key[(a,b,alpha)]=norm
            if deg in (1,3,5): odd.append((a,b,alpha,norm))
            rec={'pair':[a,b],'alpha':list(alpha),'degree':deg,'value':fstr(norm)}
            if deg==0: rec['over_kappa3']=fstr(norm/(K**3))
            elif deg==2: rec['over_kappa4']=fstr(norm/(K**4))
            elif deg==4: rec['over_kappa5']=fstr(norm/(K**5))
            elif deg==6: rec['over_kappa6']=fstr(norm/(K**6))
            source_sparse.append(rec)
            if deg==6:
                d6+=1
                if alpha[0]: d6time+=1
                if a!=b: d6off+=1

    udata=json.loads(U_PATH.read_text())
    uprov=(udata.get('terminal_commit')==ITER057U and len(udata.get('Shat_normalized_sparse',[]))==90)
    expected={}
    for item in udata.get('Shat_normalized_sparse',[]):
        deg=int(item['degree'])
        if deg<=4: expected[(item['pair'][0],item['pair'][1],tuple(item['alpha']))]=F(item['value'])
    mismatches=[]
    for deg in (0,2,4):
        for a,b in PAIRS:
            for alpha in alphas(deg):
                got=source_by_key.get((a,b,alpha),F(0)); exp=expected.get((a,b,alpha),F(0))
                if got!=exp: mismatches.append({'pair':[a,b],'alpha':list(alpha),'got':fstr(got),'expected':fstr(exp)})
    lower_match=uprov and not mismatches

    basis_by_degree={str(d):10*len(alphas(d)) for d in range(7)}
    basis_total=sum(basis_by_degree.values())
    controls={
      'A_iter057W_R10_provenance_exact':prov and r10_count==283,
      'B_inverse_identity_through_degree8':invok,
      'B_seed_Ricci_through_degree8_zero':ricci_zero,
      'B_seed_scalar_through_degree8_zero':scalar_zero,
      'B_seed_Einstein_through_degree8_zero':einstein_zero,
      'C_source_computed_directly_through_degree6':True,
      'D_P_dot_R_equals_3I3_through_degree6':homogeneity,
      'E_E_W3_down_symmetric_through_degree6':sym,
      'F_trace_Ward_through_degree6':trace_ward,
      'G_Noether_divergence_through_degree5':noether_ok,
      'H_odd_source_degrees_1_3_5_zero':not odd,
      'I_complete_Iter057U_degree0_2_4_replay':lower_match,
      'J_full_basis_count_2100':basis_total==2100 and basis_by_degree=={'0':10,'1':40,'2':100,'3':200,'4':350,'5':560,'6':840},
      'K_no_tolerance':True,
    }
    passed=all(controls.values())
    classification=('PASS_SCOPED_ITER057X_CORRECTED_DECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_SIXTH_EVEN_ORDER__O_C6_Q8_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED' if passed else
                    'INVALID_ITER057X_SEED_MUTATION_OLD_SOURCE_REUSE_RESTRICTED_ANSATZ_NORMALIZATION_OR_EXACTNESS_CONTROL')
    return {
      'gate':GATE,'preregistration_commit':PREREG,'iter057U_commit':ITER057U,'iter057W_commit':ITER057W,
      'r10_data_commit':R10_DATA_COMMIT,'r10_payload_sha256':R10_PAYLOAD_SHA,'kappa':fstr(K),
      'controls':controls,'pass':passed,'basis_count_by_degree':basis_by_degree,'basis_total':basis_total,
      'source_nonzero_count_by_degree':{str(k):v for k,v in counts.items()},
      'degree6_nonzero_count':d6,'degree6_time_containing_nonzero_count':d6time,'degree6_offdiagonal_nonzero_count':d6off,
      'Shat_normalized_sparse':source_sparse,'iter057U_replay_mismatches':mismatches,
      'I3_origin_over_kappa3':fstr(I3.get(ZERO,F(0))/(K**3)),'classification':classification,
      'exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out'); args=ap.parse_args()
    out=compute(); text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(text)
    print(text,end='')
    if out['pass'] is not True: raise SystemExit(2)

if __name__=='__main__': main()
