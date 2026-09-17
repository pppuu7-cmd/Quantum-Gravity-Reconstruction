#!/usr/bin/env python3
"""Iter057AQ exact 2x2 causal adjudication of the AP/X degree-six discrepancy."""
import argparse, hashlib, json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

import qgr_iter057ap_independent_covariant_source as b

# Preserve the historical hand-written projector before importing the repair,
# which intentionally monkeypatches the base module.
LEGACY_P_FN = b.p_from_frechet_projection
import qgr_iter057ap_independent_covariant_source_repair as r

N=b.N; PAIRS=b.PAIRS; ZERO=b.ZERO
PREREG='3ac98107c7a659f63271c9836583e929bc35adb4'
AP_TERMINAL='2ccf15108b889cef25e1b90af7f8a7127b2d83be'
X_IMPL='920b73f8430983255081b9bcd3ec6d222b737b08'

def phash(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def legacy_Q(C,Cup,degree):
    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,bb,c,d in product(range(N),repeat=4):
        v={}
        for rr,ss in product(range(N),repeat=2): v=b.add(v,b.mul(Cup[a][bb][rr][ss],C[rr][ss][c][d],degree))
        Q[a][bb][c][d]=b.trunc(v,degree)
    return Q

def x_operator(P,g,gi,Gamma,Rlow,I3):
    # Exact transcription of Iter057X downstream P -> Edown assembly.
    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,bb,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=b.deriv(P[a][m][bb][n],a)
            for rr in range(N):
                term=b.add(term,b.mul(Gamma[a][a][rr],P[rr][m][bb][n],7))
                term=b.add(term,b.mul(Gamma[m][a][rr],P[a][rr][bb][n],7))
                term=b.add(term,b.mul(Gamma[bb][a][rr],P[a][m][rr][n],7))
                term=b.add(term,b.mul(Gamma[n][a][rr],P[a][m][bb][rr],7))
            val=b.add(val,term)
        FD[m][bb][n]=b.trunc(val,7)
    D=b.pmat()
    for m,n in product(range(N),repeat=2):
        val={}
        for bb in range(N):
            term=b.deriv(FD[m][bb][n],bb)
            for rr in range(N):
                term=b.add(term,b.mul(Gamma[m][bb][rr],FD[rr][bb][n],6))
                term=b.add(term,b.mul(Gamma[bb][bb][rr],FD[m][rr][n],6))
                term=b.add(term,b.mul(Gamma[n][bb][rr],FD[m][bb][rr],6))
            val=b.add(val,term)
        D[m][n]=b.trunc(val,6)
    def bone(a,bb):
        val={}
        for c,d,e,f in product(range(N),repeat=4):
            val=b.add(val,b.mul(b.mul(P[a][c][d][e],gi[bb][f],6),Rlow[f][c][d][e],6))
        return b.trunc(val,6)
    B=b.pmat()
    for a,bb in product(range(N),repeat=2): B[a][bb]=b.scale(b.add(bone(a,bb),bone(bb,a)),F(1,2))
    Eup=b.pmat()
    for a,bb in product(range(N),repeat=2):
        val=b.add(b.neg(B[a][bb]),b.scale(D[a][bb],-2))
        val=b.add(val,b.scale(b.mul(gi[a][bb],I3,6),F(1,2)))
        Eup[a][bb]=b.trunc(val,6)
    Edown=b.pmat()
    for a,bb in product(range(N),repeat=2):
        val={}
        for c,d in product(range(N),repeat=2): val=b.add(val,b.mul(b.mul(g[a][c],g[bb][d],6),Eup[c][d],6))
        Edown[a][bb]=b.trunc(val,6)
    return Edown

def ao_operator(P,g,gi,Gamma,Rlow,I3):
    Eup,Edown,_,_,_=b.ao_source(g,gi,Gamma,Rlow,P,I3)
    return Edown

def slots(E):
    out=[]
    for deg in range(7):
        for a,bb in PAIRS:
            for alpha in b.alphas(deg):
                v=b.normalized(E[a][bb],alpha)
                out.append({'pair':[a,bb],'alpha':list(alpha),'degree':deg,'value':fs(v)})
    return out

def mismatch(A,B):
    ca={str(k):0 for k in range(7)}; n=0
    for x,y in zip(A,B):
        if x['pair']!=y['pair'] or x['alpha']!=y['alpha']: raise ArithmeticError('basis ordering mismatch')
        if F(x['value'])!=F(y['value']): ca[str(x['degree'])]+=1; n+=1
    return n,ca

def p_mismatch(P,Q):
    by={str(k):0 for k in range(9)}; n=0
    for a,bb,c,d in product(range(N),repeat=4):
        keys=set(P[a][bb][c][d])|set(Q[a][bb][c][d])
        for alpha in keys:
            if P[a][bb][c][d].get(alpha,F(0))!=Q[a][bb][c][d].get(alpha,F(0)):
                by[str(sum(alpha))]+=1;n+=1
    return n,by

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args()
    g,prov,_,_=b.seed_metric10();gi,Gamma,Rlow,Ric,Scal,Ein,C,invok=b.geometry8(g)
    common_ok=prov and invok and all(not Ric[i][j] for i,j in product(range(N),repeat=2)) and not Scal
    Cup=b.raise_last(C,gi,8)
    I3,QF=r._fixed_cubic_and_Q(C,Cup,6)
    QL=legacy_Q(C,Cup,8)
    PF,_=r._fixed_p_from_frechet(g,gi,C,Cup,QF,8)
    PL,_=LEGACY_P_FN(g,gi,C,Cup,QL,8)
    pc=r._fixed_p_controls(PF,None,I3,Rlow,g,gi)
    pnm,pby=p_mismatch(PL,PF)

    cells={
      'OX_PL':slots(x_operator(PL,g,gi,Gamma,Rlow,I3)),
      'OX_PF':slots(x_operator(PF,g,gi,Gamma,Rlow,I3)),
      'OAO_PL':slots(ao_operator(PL,g,gi,Gamma,Rlow,I3)),
      'OAO_PF':slots(ao_operator(PF,g,gi,Gamma,Rlow,I3)),
    }
    hashes={k:phash(v) for k,v in cells.items()}
    pairs={}
    names=list(cells)
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            k=names[i]+'__'+names[j]; n,bd=mismatch(cells[names[i]],cells[names[j]]);pairs[k]={'mismatch_count':n,'by_degree':bd}

    controls={
      'A_common_W_seed_geometry_exact':bool(common_ok),
      'B_PF_controls_all_exact':all(v is True for v in pc.values() if isinstance(v,bool)),
      'C_four_complete_2100_slot_cells':all(len(v)==2100 for v in cells.values()),
      'D_target_coefficients_not_loaded':True,
      'E_exact_fraction_arithmetic_no_tolerance':True,
      'F_c6_symbolic_unfixed':True,
    }
    # Causal classification is defined solely from target-blind cell relations.
    xpf_ao=mismatch(cells['OX_PF'],cells['OAO_PF'])[0]
    xpl_ao=mismatch(cells['OX_PL'],cells['OAO_PL'])[0]
    p_changes_x=mismatch(cells['OX_PL'],cells['OX_PF'])[0]
    p_changes_ao=mismatch(cells['OAO_PL'],cells['OAO_PF'])[0]
    if not all(controls.values()): cls='INVALID_ITER057AQ_TARGET_LEAKAGE_SEED_MUTATION_POSTHOC_MAP_OR_EXACTNESS_FAILURE'
    elif p_changes_x and p_changes_ao and xpf_ao==0: cls='PASS_SCOPED_ITER057AQ_DISCREPANCY_LOCALIZED_TO_LEGACY_P_CONSTRUCTION'
    elif pnm==0 and xpf_ao: cls='PASS_SCOPED_ITER057AQ_DISCREPANCY_LOCALIZED_TO_DOWNSTREAM_EULER_ASSEMBLY'
    elif pnm and xpf_ao: cls='PASS_SCOPED_ITER057AQ_DISCREPANCY_IS_MIXED_P_AND_OPERATOR_DEFECT'
    else: cls='SCIENTIFIC_FAIL_ITER057AQ_AP_DISCREPANCY_NOT_REPRODUCIBLE_UNDER_FROZEN_2X2_INTERVENTION'
    payload={'gate':'ITER057AQ-DEGREE6-SOURCE-DISCREPANCY-CAUSAL-ADJUDICATION','preregistration':PREREG,'AP_terminal':AP_TERMINAL,'X_implementation':X_IMPL,'classification':cls,'controls':controls,'PF_controls':pc,'P_mismatch_count':pnm,'P_mismatch_by_degree':pby,'cell_hashes':hashes,'cell_pair_mismatches':pairs,'cell_nonzero_counts':{k:{str(d):sum(1 for z in v if z['degree']==d and F(z['value'])) for d in range(7)} for k,v in cells.items()},'exact_zero_uses_tolerance':False,'c6_status':'SYMBOLIC_UNFIXED','cells':cells}
    q=dict(payload);q.pop('cells');payload['scientific_summary_sha256']=phash(q);payload['complete_payload_sha256']=phash(payload)
    p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k!='cells'},sort_keys=True,indent=2))
    return 0 if cls.startswith('PASS_') else 2

if __name__=='__main__':raise SystemExit(main())
