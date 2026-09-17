#!/usr/bin/env python3
"""Corrected source-faithful Weyl^3 source through degree eight.

Prospectively frozen by ddf4d41be23b09e5a4709149d85d85688a533fab.
Two modes share the already-authorized Frechet P_F construction but use
independent downstream Euler-source assemblies. Neither mode loads historical
Iter057AA source coefficients.
"""
from __future__ import annotations
import argparse,csv,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa
import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r

PREREG='ddf4d41be23b09e5a4709149d85d85688a533fab'
AT_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057AT_CANONICAL_SOURCE_DEGREE6.csv'
AT_FILE_SHA='1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b'
AT_VECTOR_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'
AT_PREREG='6039cb2ed1380b549bced3d33634362ef57345d4'
AT_PRODUCTION='c4e7ccc05ea1b8f4967379fc370812dfa99cce03'
AO_AUTHORITY='3246b31fde58d061f7e35cbc6be22236d1c7b2a8'
AQ_AUTHORITY='de82fe82c8f3f40854c81d7cb3e0e5d490a153a4'
N=b.N; PAIRS=b.PAIRS


def fs(x):
    x=F(x);return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def jsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def fsha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def peq(p,q):return all(F(p.get(k,0))==F(q.get(k,0)) for k in set(p)|set(q))

def read_at():
    raw=AT_PATH.read_bytes();meta={};body=[]
    for line in raw.decode('utf-8','strict').splitlines():
        if line.startswith('# '):
            s=line[2:]
            if '=' in s:
                k,v=s.split('=',1);meta[k]=v
        elif line.strip():body.append(line)
    rows=list(csv.DictReader(body))
    return raw,meta,rows

def serialize(E,deg,sign=F(1)):
    out=[]
    for a,bb in PAIRS:
        for alpha in b.alphas(deg):
            out.append({'pair':[a,bb],'alpha':list(alpha),'value':fs(sign*b.normalized(E[a][bb],alpha))})
    return out

def p_intrinsic_controls(P,I3,Rlow):
    anti1=all(not b.trunc(b.add(P[a][bb][c][d],P[bb][a][c][d]),10) for a,bb,c,d in product(range(N),repeat=4))
    anti2=all(not b.trunc(b.add(P[a][bb][c][d],P[a][bb][d][c]),10) for a,bb,c,d in product(range(N),repeat=4))
    pair=all(not b.trunc(b.sub(P[a][bb][c][d],P[c][d][a][bb]),10) for a,bb,c,d in product(range(N),repeat=4))
    bianchi=all(not b.trunc(b.add(b.add(P[a][bb][c][d],P[a][c][d][bb]),P[a][d][bb][c]),10) for a,bb,c,d in product(range(N),repeat=4))
    pr={}
    for a,bb,c,d in product(range(N),repeat=4):pr=b.add(pr,b.mul(P[a][bb][c][d],Rlow[a][bb][c][d],8))
    hom=not b.trunc(b.sub(pr,b.scale(I3,3)),8)
    return {'P_antisym_first_through10':anti1,'P_antisym_second_through10':anti2,'P_pair_exchange_through10':pair,'P_algebraic_bianchi_through10':bianchi,'P_dot_R_equals_3I3_through8':hom}

def common_object():
    g,prov,r12rows,r12meta=aa.seed_metric12()
    gi,Gamma,Rlow,Ric,Scal,Ein,invok=aa.geometry10(g)
    seed_controls={
      'R12_seed_provenance_exact':bool(prov and len(r12rows)==469),
      'inverse_identity_through10':bool(invok),
      'Ricci_through10_zero':all(not Ric[a][bb] for a,bb in product(range(N),repeat=2)),
      'scalar_through10_zero':not Scal,
      'Einstein_through10_zero':all(not Ein[a][bb] for a,bb in product(range(N),repeat=2)),
    }
    C=Rlow
    Cup=b.raise_last(C,gi,10)
    I3,QF=r._fixed_cubic_and_Q(C,Cup,8)
    PF,_=r._fixed_p_from_frechet(g,gi,C,Cup,QF,10)
    pc=p_intrinsic_controls(PF,I3,Rlow)
    return g,gi,Gamma,Rlow,I3,PF,seed_controls,pc

def primary_operator(P,g,gi,Gamma,Rlow,I3):
    # Prospectively generalized exact AQ/Iter057X downstream assembly: P degree10 -> source degree8.
    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,bb,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=b.deriv(P[a][m][bb][n],a)
            for rr in range(N):
                term=b.add(term,b.mul(Gamma[a][a][rr],P[rr][m][bb][n],9))
                term=b.add(term,b.mul(Gamma[m][a][rr],P[a][rr][bb][n],9))
                term=b.add(term,b.mul(Gamma[bb][a][rr],P[a][m][rr][n],9))
                term=b.add(term,b.mul(Gamma[n][a][rr],P[a][m][bb][rr],9))
            val=b.add(val,term)
        FD[m][bb][n]=b.trunc(val,9)
    D=b.pmat()
    for m,n in product(range(N),repeat=2):
        val={}
        for bb in range(N):
            term=b.deriv(FD[m][bb][n],bb)
            for rr in range(N):
                term=b.add(term,b.mul(Gamma[m][bb][rr],FD[rr][bb][n],8))
                term=b.add(term,b.mul(Gamma[bb][bb][rr],FD[m][rr][n],8))
                term=b.add(term,b.mul(Gamma[n][bb][rr],FD[m][bb][rr],8))
            val=b.add(val,term)
        D[m][n]=b.trunc(val,8)
    def bone(a,bb):
        val={}
        for c,d,e,f in product(range(N),repeat=4):val=b.add(val,b.mul(b.mul(P[a][c][d][e],gi[bb][f],8),Rlow[f][c][d][e],8))
        return b.trunc(val,8)
    B=b.pmat()
    for a,bb in product(range(N),repeat=2):B[a][bb]=b.scale(b.add(bone(a,bb),bone(bb,a)),F(1,2))
    Eup=b.pmat()
    for a,bb in product(range(N),repeat=2):
        v=b.add(b.neg(B[a][bb]),b.scale(D[a][bb],-2));v=b.add(v,b.scale(b.mul(gi[a][bb],I3,8),F(1,2)));Eup[a][bb]=b.trunc(v,8)
    E=b.pmat()
    for a,bb in product(range(N),repeat=2):
        v={}
        for c,d in product(range(N),repeat=2):v=b.add(v,b.mul(b.mul(g[a][c],g[bb][d],8),Eup[c][d],8))
        E[a][bb]=b.trunc(v,8)
    return E

def independent_operator(P,g,gi,Gamma,Rlow,I3):
    # AO direct covariant first-divergence / second-divergence construction, generalized to degree8.
    U=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,c,bb in product(range(N),repeat=3):
        val={}
        for d in range(N):
            term=b.deriv(P[a][c][d][bb],d)
            for rr in range(N):
                term=b.add(term,b.mul(Gamma[a][d][rr],P[rr][c][d][bb],9))
                term=b.add(term,b.mul(Gamma[c][d][rr],P[a][rr][d][bb],9))
                term=b.add(term,b.mul(Gamma[d][d][rr],P[a][c][rr][bb],9))
                term=b.add(term,b.mul(Gamma[bb][d][rr],P[a][c][d][rr],9))
            val=b.add(val,term)
        U[a][c][bb]=b.trunc(val,9)
    T=b.pmat()
    for a,bb in product(range(N),repeat=2):
        val={}
        for c in range(N):
            term=b.deriv(U[a][c][bb],c)
            for rr in range(N):
                term=b.add(term,b.mul(Gamma[a][c][rr],U[rr][c][bb],8))
                term=b.add(term,b.mul(Gamma[c][c][rr],U[a][rr][bb],8))
                term=b.add(term,b.mul(Gamma[bb][c][rr],U[a][c][rr],8))
            val=b.add(val,term)
        T[a][bb]=b.trunc(val,8)
    A=b.pmat()
    for a,bb in product(range(N),repeat=2):
        val={}
        for c,d,e,f in product(range(N),repeat=4):val=b.add(val,b.mul(b.mul(P[a][c][d][e],gi[bb][f],8),Rlow[f][c][d][e],8))
        A[a][bb]=b.trunc(val,8)
    Eup=b.pmat()
    for a,bb in product(range(N),repeat=2):Eup[a][bb]=b.trunc(b.add(b.add(b.neg(A[a][bb]),b.scale(T[a][bb],2)),b.scale(b.mul(gi[a][bb],I3,8),F(1,2))),8)
    E=b.pmat()
    for a,bb in product(range(N),repeat=2):
        val={}
        for c,d in product(range(N),repeat=2):val=b.add(val,b.mul(b.mul(g[a][c],g[bb][d],8),Eup[c][d],8))
        E[a][bb]=b.trunc(val,8)
    return E

def build(mode):
    g,gi,Gamma,Rlow,I3,PF,seed,pc=common_object()
    E=primary_operator(PF,g,gi,Gamma,Rlow,I3) if mode=='primary' else independent_operator(PF,g,gi,Gamma,Rlow,I3)
    d6=serialize(E,6);d8=serialize(E,8);yd8=serialize(E,8,F(-1))
    at_raw,at_meta,at_rows=read_at()
    at_controls={
      'AT_file_sha_exact':hashlib.sha256(at_raw).hexdigest()==AT_FILE_SHA,
      'AT_metadata_exact':at_meta.get('preregistration')==AT_PREREG and at_meta.get('production_head')==AT_PRODUCTION,
      'AT_140_rows':len(at_rows)==140,
      'degree6_projection_hash_equals_AT':jsha(d6)==AT_VECTOR_SHA,
    }
    sym=all(peq(E[a][bb],E[bb][a]) for a,bb in product(range(N),repeat=2))
    controls={**seed,**pc,**at_controls,
      'standard_source_symmetric_through8':sym,
      'degree8_slot_count_1650':len(d8)==1650,
      'degree8_monomials_per_pair_165':len(tuple(b.alphas(8)))==165,
      'historical_AA_or_X_target_not_loaded':True,
      'exact_fraction_arithmetic_no_tolerance':True,
      'c6_symbolic_unfixed_factored_out':True,
      'AO_covariant_variation_authority_pinned':AO_AUTHORITY=='3246b31fde58d061f7e35cbc6be22236d1c7b2a8',
      'AQ_legacy_P_localization_authority_pinned':AQ_AUTHORITY=='de82fe82c8f3f40854c81d7cb3e0e5d490a153a4',
    }
    ok=all(controls.values())
    out={'gate':'CORRECTED_DEGREE8_WEYL3_SOURCE_RECONSTRUCTION','preregistration_commit':PREREG,'lane':mode,'classification':('READY_CORRECTED_DEGREE8_'+mode.upper() if ok else 'INVALID_CORRECTED_DEGREE8_'+mode.upper()+'_CONTROL_FAILURE'),'controls':controls,'P_controls':pc,'degree6_vector_sha256':jsha(d6),'degree8_standard_vector_sha256':jsha(d8),'degree8_y_format_minus_vector_sha256':jsha(yd8),'degree8_standard_nonzero_count':sum(F(z['value'])!=0 for z in d8),'degree8_y_format_nonzero_count':sum(F(z['value'])!=0 for z in yd8),'c6':'SYMBOLIC_UNFIXED_FACTORED_OUT','historical_target_loaded':False,'degree8_standard_vector':d8,'degree8_y_format_minus_vector':yd8}
    return out,ok

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',required=True,choices=['primary','independent']);ap.add_argument('--output',required=True);a=ap.parse_args();o,ok=build(a.mode);p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n');q=dict(o);q.pop('degree8_standard_vector');q.pop('degree8_y_format_minus_vector');print(json.dumps(q,sort_keys=True,indent=2));return 0 if ok else 2
if __name__=='__main__':raise SystemExit(main())
