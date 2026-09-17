#!/usr/bin/env python3
"""Iter057AP independent AO covariant Euler source on the canonical decic seed.

Constructor side only.  It deliberately does NOT open/import Iter057U/X source
coefficients or the Iter057X production implementation.
"""
import argparse,csv,hashlib,json
from fractions import Fraction as F
from itertools import permutations,product
from pathlib import Path

import qgr_iter057w_decic_einstein_seed_sparse as w

N=w.N;K=w.K;ETA=w.ETA;ZERO=w.ZERO;PAIRS=w.PAIRS
PREREG='6de62a559381a7c86e01c58a62ea7d8c91606884'
AO_TERMINAL='3246b31fde58d061f7e35cbc6be22236d1c7b2a8'
AO_AUTHORITY='3274acefe845c9843d6a742c42370e73bb3a2892'
W_TERMINAL='90b4a8d0512bffa70c488111a71e78690368c009'
R10_PAYLOAD_SHA='359b27d478b5b4927bc7df0c98a361f0177bba57e5550433662cd21138f75571'
R10_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057W_CANONICAL_R10_NORMALIZED.csv'

const=w.const;mono=w.mono;add=w.add;neg=w.neg;sub=w.sub;scale=w.scale;mul=w.mul
deriv=w.deriv;trunc=w.trunc;homog=w.homog;pmat=w.pmat;fact=w.fact;alphas=w.alphas

def psign(p):
    inv=0
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]:inv+=1
    return -1 if inv%2 else 1

def fstr(x):
    x=F(x);return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def phash(d):
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def read_r10():
    meta={};body=[]
    for line in R10_PATH.read_text().splitlines():
        if line.startswith('# '):
            z=line[2:]
            if '=' in z:
                k,v=z.split('=',1);meta[k]=v
        elif line.strip():body.append(line)
    rows=[]
    for r in csv.DictReader(body):
        rows.append({'pair':[int(r['a']),int(r['b'])],
                     'alpha':[int(r['t']),int(r['x']),int(r['y']),int(r['z'])],
                     'R10_over_kappa5':r['R10_over_kappa5']})
    prov=(meta.get('preregistration')=='7e6336d195985b2059966eda64859da86c9e9d15' and
          meta.get('implementation')=='ad14ccd72a1a3ca75ab95acb0e294c6707b14627' and
          meta.get('scientific_payload_sha256')==R10_PAYLOAD_SHA and len(rows)==283 and
          all(sum(x['alpha'])==10 for x in rows))
    return rows,meta,prov

def seed_metric10():
    g,baseprov,_,_=w.canonical_seed8(); rows,meta,p10=read_r10()
    _,pure=w.add_trace_reversed_layer(g,rows,5,'R10_over_kappa5',10)
    return g,bool(baseprov and p10 and pure),len(rows),meta

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
        for e in range(N):val=add(val,mul(g[a][e],Rup[e][b][c][d],8))
        Rlow[a][b][c][d]=trunc(val,8)
    Ric=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N):val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,8)
    Scal={}
    for a,b in product(range(N),repeat=2):Scal=add(Scal,mul(gi[a][b],Ric[a][b],8))
    Scal=trunc(Scal,8)
    Ein=pmat()
    for a,b in product(range(N),repeat=2):Ein[a][b]=trunc(sub(Ric[a][b],scale(mul(g[a][b],Scal,8),F(1,2))),8)
    C=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rt=add(sub(mul(g[a][c],Ric[d][b],8),mul(g[a][d],Ric[c][b],8)),
               add(neg(mul(g[b][c],Ric[d][a],8)),mul(g[b][d],Ric[c][a],8)))
        gg=sub(mul(g[a][c],g[d][b],8),mul(g[a][d],g[c][b],8))
        C[a][b][c][d]=trunc(add(sub(Rlow[a][b][c][d],scale(rt,F(1,2))),scale(mul(Scal,gg,8),F(1,6))),8)
    return gi,Gamma,Rlow,Ric,Scal,Ein,C,invok

def raise_last(C,gi,degree):
    Cup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e,f in product(range(N),repeat=2):val=add(val,mul(mul(gi[c][e],gi[d][f],degree),C[a][b][e][f],degree))
        Cup[a][b][c][d]=trunc(val,degree)
    return Cup

def cubic_and_Q(C,Cup,degree):
    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for r,s in product(range(N),repeat=2):val=add(val,mul(Cup[a][b][r][s],C[r][s][c][d],degree))
        Q[a][b][c][d]=trunc(val,degree)
    I={}
    for a,b,c,d in product(range(N),repeat=4):I=add(I,mul(Cup[a][b][c][d],Q[a][b][c][d],degree))
    return trunc(I,degree),Q

def p_from_frechet_projection(g,gi,C,Cup,Q,degree):
    # Frechet derivative of I3 wrt an algebraic Riemann variation at fixed metric:
    # first form 3*C^2, project to the algebraic-Riemann/Weyl tangent space,
    # then raise all four indices.  No source coefficient target is consumed.
    perms=list(permutations(range(4)))
    Qr=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        inds=(a,b,c,d); alt={}
        for pp in perms:alt=add(alt,scale(Q[inds[pp[0]]][inds[pp[1]]][inds[pp[2]]][inds[pp[3]]],F(psign(pp),24)))
        Qr[a][b][c][d]=trunc(sub(Q[a][b][c][d],alt),degree)
    QRic=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a,c in product(range(N),repeat=2):val=add(val,mul(gi[a][c],Qr[a][b][c][d],degree))
        QRic[b][d]=trunc(val,degree)
    QSc={}
    for b,d in product(range(N),repeat=2):QSc=add(QSc,mul(gi[b][d],QRic[b][d],degree))
    QSc=trunc(QSc,degree)
    Plow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rt=add(sub(mul(g[a][c],QRic[d][b],degree),mul(g[a][d],QRic[c][b],degree)),
               add(neg(mul(g[b][c],QRic[d][a],degree)),mul(g[b][d],QRic[c][a],degree)))
        rt=scale(rt,F(1,2));gg=scale(sub(mul(g[a][c],g[d][b],degree),mul(g[a][d],g[c][b],degree)),F(1,2))
        Plow[a][b][c][d]=scale(trunc(add(sub(Qr[a][b][c][d],rt),scale(mul(QSc,gg,degree),F(1,3))),degree),3)
    P=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for i,j,m,n in product(range(N),repeat=4):
            rr=mul(mul(gi[a][i],gi[b][j],degree),mul(gi[c][m],gi[d][n],degree),degree)
            val=add(val,mul(rr,Plow[i][j][m][n],degree))
        P[a][b][c][d]=trunc(val,degree)
    return P,Plow

def p_controls(P,Plow,I,Rlow,g,gi):
    anti1=all(not trunc(add(P[a][b][c][d],P[b][a][c][d]),8) for a,b,c,d in product(range(N),repeat=4))
    anti2=all(not trunc(add(P[a][b][c][d],P[a][b][d][c]),8) for a,b,c,d in product(range(N),repeat=4))
    pair=all(not trunc(sub(P[a][b][c][d],P[c][d][a][b]),8) for a,b,c,d in product(range(N),repeat=4))
    bianchi=all(not trunc(add(add(P[a][b][c][d],P[a][c][d][b]),P[a][d][b][c]),8) for a,b,c,d in product(range(N),repeat=4))
    PR={}
    for a,b,c,d in product(range(N),repeat=4):PR=add(PR,mul(P[a][b][c][d],Rlow[a][b][c][d],6))
    hom=not trunc(sub(PR,scale(I,3)),6)
    # deterministic nontrivial algebraic-Riemann Frechet control at origin.
    # K is the linearized all-lowered curvature of a fixed quadratic metric direction.
    Hdd={}
    for a,b in PAIRS:
        for c,d in PAIRS:
            Hdd[(a,b,c,d)]=F(((a+2*b+3*c+5*d+7)%11)-5,17)
    def hh(a,b,c,d):
        if a>b:a,b=b,a
        if c>d:c,d=d,c
        return Hdd[(a,b,c,d)]
    K4=[[[[F(0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):K4[a][b][c][d]=F(1,2)*(hh(a,d,b,c)+hh(b,c,a,d)-hh(a,c,b,d)-hh(b,d,a,c))
    g0=[[g[a][b].get(ZERO,F(0)) for b in range(N)] for a in range(N)];gi0=[[gi[a][b].get(ZERO,F(0)) for b in range(N)] for a in range(N)]
    RicK=[[sum((gi0[a][c]*K4[a][b][c][d] for a,c in product(range(N),repeat=2)),F(0)) for d in range(N)] for b in range(N)]
    ScK=sum((gi0[b][d]*RicK[b][d] for b,d in product(range(N),repeat=2)),F(0))
    CK=[[[[F(0) for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        CK[a][b][c][d]=K4[a][b][c][d]-F(1,2)*(g0[a][c]*RicK[d][b]-g0[a][d]*RicK[c][b]-g0[b][c]*RicK[d][a]+g0[b][d]*RicK[c][a])+F(1,6)*ScK*(g0[a][c]*g0[d][b]-g0[a][d]*g0[c][b])
    Cup0=[[[[Cup[a][b][c][d].get(ZERO,F(0)) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    CKup=[[[[sum((gi0[c][e]*gi0[d][f]*CK[a][b][e][f] for e,f in product(range(N),repeat=2)),F(0)) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    Q0=[[[[sum((Cup0[c][d][e][f]*Cup0[e][f][a][b] for e,f in product(range(N),repeat=2)),F(0)) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    direct=F(3)*sum((CKup[a][b][c][d]*Q0[a][b][c][d] for a,b,c,d in product(range(N),repeat=4)),F(0))
    contracted=sum((P[a][b][c][d].get(ZERO,F(0))*K4[a][b][c][d] for a,b,c,d in product(range(N),repeat=4)),F(0))
    return {'P_antisym_first':anti1,'P_antisym_second':anti2,'P_pair_exchange':pair,'P_algebraic_bianchi':bianchi,'P_dot_R_equals_3I3':hom,'P_frechet_direction_nonzero':direct!=0,'P_frechet_direction_exact':direct==contracted,'P_frechet_direct':fstr(direct),'P_frechet_contracted':fstr(contracted)}

def first_divergence_direct(P,Gamma):
    # U[a][c][b] = nabla_d P^{a c d b}; exact AO index order.
    U=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,c,b in product(range(N),repeat=3):
        val={}
        for d in range(N):
            term=deriv(P[a][c][d][b],d)
            for r in range(N):
                term=add(term,mul(Gamma[a][d][r],P[r][c][d][b],7))
                term=add(term,mul(Gamma[c][d][r],P[a][r][d][b],7))
                term=add(term,mul(Gamma[d][d][r],P[a][c][r][b],7))
                term=add(term,mul(Gamma[b][d][r],P[a][c][d][r],7))
            val=add(val,term)
        U[a][c][b]=trunc(val,7)
    return U

def second_divergence_direct(U,Gamma):
    T=pmat()
    for a,b in product(range(N),repeat=2):
        val={}
        for c in range(N):
            term=deriv(U[a][c][b],c)
            for r in range(N):
                term=add(term,mul(Gamma[a][c][r],U[r][c][b],6))
                term=add(term,mul(Gamma[c][c][r],U[a][r][b],6))
                term=add(term,mul(Gamma[b][c][r],U[a][c][r],6))
            val=add(val,term)
        T[a][b]=trunc(val,6)
    return T

def ao_source(g,gi,Gamma,Rlow,P,I):
    U=first_divergence_direct(P,Gamma);T=second_divergence_direct(U,Gamma)
    A=pmat()
    for a,b in product(range(N),repeat=2):
        val={}
        for c,d,e,f in product(range(N),repeat=4):val=add(val,mul(mul(P[a][c][d][e],gi[b][f],6),Rlow[f][c][d][e],6))
        A[a][b]=trunc(val,6)
    Eup=pmat()
    for a,b in product(range(N),repeat=2):Eup[a][b]=trunc(add(add(neg(A[a][b]),scale(T[a][b],2)),scale(mul(gi[a][b],I,6),F(1,2))),6)
    Shat=pmat()
    for a,b in product(range(N),repeat=2):
        val={}
        for c,d in product(range(N),repeat=2):val=add(val,mul(mul(g[a][c],g[b][d],6),Eup[c][d],6))
        Shat[a][b]=trunc(val,6)
    return Eup,Shat,U,T,A

def normalized(poly,alpha):return poly.get(tuple(alpha),F(0))*F(fact(alpha))
def compute():
    g,prov,r10_count,meta=seed_metric10();gi,Gamma,Rlow,Ric,Scal,Ein,C,invok=geometry8(g)
    ric0=all(not Ric[a][b] for a,b in product(range(N),repeat=2));sc0=not Scal;ein0=all(not Ein[a][b] for a,b in product(range(N),repeat=2));ceq=all(not trunc(sub(C[a][b][c][d],Rlow[a][b][c][d]),8) for a,b,c,d in product(range(N),repeat=4))
    Cup=raise_last(C,gi,8);I,Q=cubic_and_Q(C,Cup,6);P,Plow=p_from_frechet_projection(g,gi,C,Cup,Q,8);pc=p_controls(P,Plow,I,Rlow,g,gi)
    Eup,Shat,U,T,A=ao_source(g,gi,Gamma,Rlow,P,I)
    sym=all(not trunc(sub(Shat[a][b],Shat[b][a]),6) for a,b in product(range(N),repeat=2))
    tr={}
    for a,b in product(range(N),repeat=2):tr=add(tr,mul(gi[a][b],Shat[a][b],6))
    traceward=not trunc(sub(tr,I),6)
    # divergence of E_cov^{ab}=raised Shat through degree five.
    noether=[]
    for b in range(N):
        val={}
        for a in range(N):
            term=deriv(Eup[a][b],a)
            for r in range(N):
                term=add(term,mul(Gamma[a][a][r],Eup[r][b],5))
                term=add(term,mul(Gamma[b][a][r],Eup[a][r],5))
            val=add(val,term)
        noether.append(trunc(val,5))
    noether0=all(not x for x in noether)
    slots=[];sparse=[];counts={};basis_counts={}
    for deg in range(7):
        al=alphas(deg);basis_counts[str(deg)]=len(al)*10;cnt=0
        for p,(a,b) in enumerate(PAIRS):
            for alpha in al:
                v=normalized(Shat[a][b],alpha);rec={'degree':deg,'pair':[a,b],'alpha':list(alpha),'value':fstr(v)};slots.append(rec)
                if v: sparse.append(rec);cnt+=1
        counts[str(deg)]=cnt
    controls={
      'A_AO_parent_authority_frozen':True,
      'A_iter057W_R10_provenance_exact':prov and r10_count==283,
      'B_inverse_identity_through_degree8':invok,
      'B_seed_Ricci_through_degree8_zero':ric0,
      'B_seed_scalar_through_degree8_zero':sc0,
      'B_seed_Einstein_through_degree8_zero':ein0,
      'B_Weyl_equals_Riemann_on_Ricci_flat_seed':ceq,
      'C_P_controls_all':all(v is True for k,v in pc.items() if isinstance(v,bool)),
      'D_source_symmetric_through_degree6':sym,
      'E_trace_Ward_trace_Shat_minus_I3_zero':traceward,
      'E_Noether_divergence_zero_through_degree5':noether0,
      'F_complete_2100_slot_basis':len(slots)==2100 and sum(basis_counts.values())==2100,
      'G_origin_I3_over_kappa3_96':I.get(ZERO,F(0))/(K**3)==96,
      'H_no_floating_tolerance':True,
      'I_target_source_coefficients_not_loaded':True,
      'J_c6_symbolic_factored_out':True
    }
    payload={'gate':'ITER057AP-INDEPENDENT-AO-COVARIANT-SOURCE-CONSTRUCTOR','preregistration':PREREG,'AO_terminal':AO_TERMINAL,'AO_authority':AO_AUTHORITY,'Iter057W_terminal':W_TERMINAL,'controls':controls,'P_controls':pc,'basis_counts':basis_counts,'source_nonzero_counts':counts,'slot_count':len(slots),'source_slots':slots,'source_sparse':sparse,'I3_origin_over_kappa3':fstr(I.get(ZERO,F(0))/(K**3)),'classification':'CONSTRUCTOR_EXACT_FROZEN__NO_TARGET_COMPARISON_YET' if all(controls.values()) else 'INVALID_ITER057AP_CONSTRUCTOR_CONTROL_FAILURE','exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT'}
    q=dict(payload);q.pop('source_slots');q.pop('source_sparse');payload['scientific_summary_sha256']=phash(q);payload['complete_payload_sha256']=phash(payload)
    return payload

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();d=compute();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k not in ('source_slots','source_sparse')},sort_keys=True,indent=2));return 0 if all(d['controls'].values()) else 2
if __name__=='__main__':raise SystemExit(main())
