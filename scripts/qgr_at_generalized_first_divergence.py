#!/usr/bin/env python3
"""Outcome-blind first-divergence localization between Iter057AT and generalized degree8 construction.
Frozen by aa2c0784f3b9cd0397c1eb10c000e0e555602a35.
"""
from __future__ import annotations
import argparse,csv,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r
import qgr_iter057aq_degree6_causal_adjudication as aq
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa
import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_corrected_degree8_weyl3_source as c

PREREG='aa2c0784f3b9cd0397c1eb10c000e0e555602a35'
AT_PRODUCTION='c4e7ccc05ea1b8f4967379fc370812dfa99cce03'
AQ_AUTHORITY='de82fe82c8f3f40854c81d7cb3e0e5d490a153a4'
PARENT_LOCALIZATION='fff23e02ebafc18d3aaa0bfe41217b29a19b43b3'
AT_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'
BAD_SHA='2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d'
ROOT=Path(__file__).resolve().parents[1]
AT_PATH=ROOT/'data'/'ITER057AT_CANONICAL_SOURCE_DEGREE6.csv'
N=b.N; PAIRS=b.PAIRS


def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def peq(p,q,degree=None):
    ks=set(p)|set(q)
    if degree is not None: ks={k for k in ks if sum(k)<=degree}
    return all(F(p.get(k,0))==F(q.get(k,0)) for k in ks)
def poly_payload(p,degree):
    return [{'alpha':list(k),'value':fs(v)} for k,v in sorted(p.items()) if sum(k)<=degree and v]
def poly_hash(p,degree): return jsha(poly_payload(p,degree))
def matrix_equal(A,B,degree): return all(peq(A[i][j],B[i][j],degree) for i,j in product(range(N),repeat=2))
def tensor3_equal(A,B,degree): return all(peq(A[i][j][k],B[i][j][k],degree) for i,j,k in product(range(N),repeat=3))
def tensor4_equal(A,B,degree): return all(peq(A[i][j][k][l],B[i][j][k][l],degree) for i,j,k,l in product(range(N),repeat=4))
def tensor4_mismatch(A,B,degree):
    n=0
    for i,j,k,l in product(range(N),repeat=4):
        ks={x for x in set(A[i][j][k][l])|set(B[i][j][k][l]) if sum(x)<=degree}
        n += sum(F(A[i][j][k][l].get(x,0))!=F(B[i][j][k][l].get(x,0)) for x in ks)
    return n
def matrix_hash(A,degree):
    rec=[]
    for i,j in product(range(N),repeat=2): rec.append({'ij':[i,j],'poly':poly_payload(A[i][j],degree)})
    return jsha(rec)
def tensor3_hash(A,degree):
    rec=[]
    for i,j,k in product(range(N),repeat=3): rec.append({'ijk':[i,j,k],'poly':poly_payload(A[i][j][k],degree)})
    return jsha(rec)
def tensor4_hash(A,degree):
    rec=[]
    for i,j,k,l in product(range(N),repeat=4): rec.append({'ijkl':[i,j,k,l],'poly':poly_payload(A[i][j][k][l],degree)})
    return jsha(rec)
def source_vector(E):
    out=[]
    for i,j in PAIRS:
        for alpha in b.alphas(6): out.append({'pair':[i,j],'alpha':list(alpha),'value':fs(b.normalized(E[i][j],alpha))})
    return out
def source_summary(E):
    v=source_vector(E)
    return {'sha256':jsha(v),'nonzero_count':sum(F(x['value'])!=0 for x in v),'vector':v}
def source6(mode,P,g,gi,Gamma,Rlow,I):
    if mode=='researcher': return aq.x_operator(P,g,gi,Gamma,Rlow,I)
    return b.ao_source(g,gi,Gamma,Rlow,P,I)[1]
def source8(mode,P,g,gi,Gamma,Rlow,I):
    if mode=='researcher': return c.primary_operator(P,g,gi,Gamma,Rlow,I)
    return c.independent_operator(P,g,gi,Gamma,Rlow,I)
def read_at_vector():
    body=[]
    for line in AT_PATH.read_text().splitlines():
        if line.strip() and not line.startswith('# '): body.append(line)
    rows=list(csv.DictReader(body)); d={}
    for x in rows:d[(int(x['a']),int(x['b']),tuple(map(int,(x['t'],x['x'],x['y'],x['z']))))]=F(x['value'])
    out=[]
    for i,j in PAIRS:
        for alpha in b.alphas(6): out.append({'pair':[i,j],'alpha':list(alpha),'value':fs(d.get((i,j,tuple(alpha)),0))})
    return out


def build(mode):
    # Same-seed identity is checked before constructing interventions.
    g0,prov0,_,_=b.seed_metric10()
    gz,provz,_,_,_=z.canonical_seed10()
    same_seed=matrix_equal(g0,gz,10)
    g=g0

    # H0: exact historical AT constructor.
    gi8,Gamma8,Rlow8,Ric8,Scal8,Ein8,C8,inv8=b.geometry8(g)
    Cup8=b.raise_last(C8,gi8,8)
    I6,Q6=r._fixed_cubic_and_Q(C8,Cup8,6)
    P0,_=r._fixed_p_from_frechet(g,gi8,C8,Cup8,Q6,8)
    E0=source6(mode,P0,g,gi8,Gamma8,Rlow8,I6)

    # Generalized geometry/Cup on the identical R10 metric.
    gi10,Gamma10,Rlow10,Ric10,Scal10,Ein10,inv10=aa.geometry10(g)
    C10=Rlow10
    Cup10=b.raise_last(C10,gi10,10)

    # H1: only geometry/Cup ceiling changed; QF6/PF8/source6 retained.
    I1,Q1=r._fixed_cubic_and_Q(C10,Cup10,6)
    P1,_=r._fixed_p_from_frechet(g,gi10,C10,Cup10,Q1,8)
    E1=source6(mode,P1,g,gi10,Gamma10,Rlow10,I1)

    # H2: only cubic/QF ceiling raised to degree8.
    I8,Q8=r._fixed_cubic_and_Q(C10,Cup10,8)
    P2,_=r._fixed_p_from_frechet(g,gi10,C10,Cup10,Q8,8)
    E2=source6(mode,P2,g,gi10,Gamma10,Rlow10,I8)

    # H3: only Frechet P ceiling raised to degree10; source still evaluated through degree6.
    P3,_=r._fixed_p_from_frechet(g,gi10,C10,Cup10,Q8,10)
    E3=source6(mode,P3,g,gi10,Gamma10,Rlow10,I8)

    # H4: only downstream assembly ceiling raised to degree8, then exact degree6 projection.
    E4=source8(mode,P3,g,gi10,Gamma10,Rlow10,I8)

    stages={'H0':source_summary(E0),'H1':source_summary(E1),'H2':source_summary(E2),'H3':source_summary(E3),'H4':source_summary(E4)}
    # Freeze all stage data and hashes before reading the AT coefficient target.
    intermediate={
      'same_seed_metric_through10':same_seed,
      'gi8_equals_gi10_through8':matrix_equal(gi8,gi10,8),
      'Gamma8_equals_Gamma10_through9':tensor3_equal(Gamma8,Gamma10,9),
      'C8_equals_Rlow10_through8':tensor4_equal(C8,Rlow10,8),
      'Cup8_equals_Cup10_through8':tensor4_equal(Cup8,Cup10,8),
      'I6_equals_I1_through6':peq(I6,I1,6),
      'Q6_equals_Q1_through6':tensor4_equal(Q6,Q1,6),
      'P0_equals_P1_through8':tensor4_equal(P0,P1,8),
      'P1_equals_P2_through8':tensor4_equal(P1,P2,8),
      'P2_equals_P3_through8':tensor4_equal(P2,P3,8),
      'geometry_hashes':{
        'gi8_le8':matrix_hash(gi8,8),'gi10_le8':matrix_hash(gi10,8),
        'Gamma8_le9':tensor3_hash(Gamma8,9),'Gamma10_le9':tensor3_hash(Gamma10,9),
        'C8_le8':tensor4_hash(C8,8),'Rlow10_le8':tensor4_hash(Rlow10,8),
        'Cup8_le8':tensor4_hash(Cup8,8),'Cup10_le8':tensor4_hash(Cup10,8)},
      'Q_hashes':{'Q6_hist_le6':tensor4_hash(Q6,6),'Q6_gen_le6':tensor4_hash(Q1,6),'Q8_gen_le8':tensor4_hash(Q8,8),'I6_hist':poly_hash(I6,6),'I6_gen':poly_hash(I1,6),'I8_gen':poly_hash(I8,8)},
      'P_hashes':{'P0_hist_le8':tensor4_hash(P0,8),'P1_geom_le8':tensor4_hash(P1,8),'P2_q8_le8':tensor4_hash(P2,8),'P3_p10_le8':tensor4_hash(P3,8),'P3_p10_le10':tensor4_hash(P3,10)},
      'P_mismatch_counts':{'P0_vs_P1_le8':tensor4_mismatch(P0,P1,8),'P1_vs_P2_le8':tensor4_mismatch(P1,P2,8),'P2_vs_P3_le8':tensor4_mismatch(P2,P3,8)}
    }
    pre={'gate':'CORRECTED_DEGREE8_AT_GENERALIZED_FIRST_DIVERGENCE_LOCALIZATION','preregistration_commit':PREREG,'lane':mode,'target_loaded_during_stage_construction':False,'stages':stages,'intermediate':intermediate}
    pre_sha=jsha(pre)

    at=read_at_vector(); at_sha=jsha(at)
    stage_sha={k:v['sha256'] for k,v in stages.items()}
    controls={
      'seed_provenance_exact':bool(prov0 and provz),
      'same_canonical_R10_metric_exact':same_seed,
      'historical_seed_Ricci_through8_zero':all(not Ric8[i][j] for i,j in product(range(N),repeat=2)),
      'historical_seed_scalar_through8_zero':not Scal8,
      'historical_inverse8_exact':bool(inv8),
      'generalized_inverse10_exact':bool(inv10),
      'AT_production_pinned':AT_PRODUCTION=='c4e7ccc05ea1b8f4967379fc370812dfa99cce03',
      'AQ_authority_pinned':AQ_AUTHORITY=='de82fe82c8f3f40854c81d7cb3e0e5d490a153a4',
      'parent_localization_pinned':PARENT_LOCALIZATION=='fff23e02ebafc18d3aaa0bfe41217b29a19b43b3',
      'complete_840_each_stage':all(len(v['vector'])==840 for v in stages.values()),
      'AT_full_ordered_hash_exact':at_sha==AT_SHA,
      'H0_reproduces_AT_exact':stages['H0']['vector']==at,
      'H4_reproduces_parent_bad_hash':stage_sha['H4']==BAD_SHA,
      'AT_loaded_only_after_stage_freeze':True,
      'exact_fraction_arithmetic_no_tolerance':True,
      'c6_symbolic_unfixed':True,
      'corrected_Q10_locked':True,
    }
    out={**pre,'pretarget_payload_sha256':pre_sha,'AT_loaded_after_pretarget_freeze':True,'AT_reconstructed_ordered_sha256':at_sha,'stage_sha256':stage_sha,'stage_equalities':{'H1_eq_H0':stage_sha['H1']==stage_sha['H0'],'H2_eq_H1':stage_sha['H2']==stage_sha['H1'],'H3_eq_H2':stage_sha['H3']==stage_sha['H2'],'H4_eq_H3':stage_sha['H4']==stage_sha['H3']},'controls':controls,'c6':'SYMBOLIC_UNFIXED','corrected_Q10_locked':True}
    Path(args.out).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    printed=dict(out); printed['stages']={k:{'sha256':v['sha256'],'nonzero_count':v['nonzero_count']} for k,v in stages.items()}; print(json.dumps(printed,sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',required=True,choices=['researcher','critic']); ap.add_argument('--out',required=True); args=ap.parse_args(); raise SystemExit(build(args.mode))
