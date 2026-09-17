#!/usr/bin/env python3
"""Prospective diagnostic for corrected degree-eight -> degree-six reduction mismatch.
Frozen by ffc110bfd2067d13d135577141154b2aab8626be.
Each lane freezes R10/R12 degree-six decompositions before loading AT.
"""
from __future__ import annotations
import argparse,csv,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import qgr_corrected_degree8_weyl3_source as c
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa
import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057ap_independent_covariant_source_repair as r

PREREG='ffc110bfd2067d13d135577141154b2aab8626be'
AT_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'
BAD_SHA='2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d'
AT_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057AT_CANONICAL_SOURCE_DEGREE6.csv'
N=b.N; PAIRS=b.PAIRS

def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def jsha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def madd(A,B): return [[b.add(A[i][j],B[i][j]) for j in range(N)] for i in range(N)]
def msub(A,B): return [[b.sub(A[i][j],B[i][j]) for j in range(N)] for i in range(N)]
def mscale(A,s): return [[b.scale(A[i][j],s) for j in range(N)] for i in range(N)]
def lower(U,g):
    E=b.pmat()
    for a,d in product(range(N),repeat=2):
        v={}
        for i,j in product(range(N),repeat=2): v=b.add(v,b.mul(b.mul(g[a][i],g[d][j],8),U[i][j],8))
        E[a][d]=b.trunc(v,8)
    return E

def ser(E,deg=6): return c.serialize(E,deg)
def summary(E):
    v=ser(E,6)
    return {'sha256':jsha(v),'nonzero_count':sum(F(x['value'])!=0 for x in v),'vector':v}

def common(boundary):
    if boundary=='R10':
        g,prov,_,_,_=z.canonical_seed10()
    else:
        g,prov,_,_=aa.seed_metric12()
    gi,Gamma,Rlow,Ric,Scal,Ein,invok=aa.geometry10(g)
    C=Rlow; Cup=b.raise_last(C,gi,10); I3,QF=r._fixed_cubic_and_Q(C,Cup,8); PF,_=r._fixed_p_from_frechet(g,gi,C,Cup,QF,10)
    controls={'seed_provenance':bool(prov),'inverse10':bool(invok),'Ricci10_zero':all(not Ric[i][j] for i,j in product(range(N),repeat=2)),'scalar10_zero':not Scal,'Einstein10_zero':all(not Ein[i][j] for i,j in product(range(N),repeat=2))}
    return g,gi,Gamma,Rlow,I3,PF,controls

def primary_parts(P,g,gi,Gamma,Rlow,I3):
    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,q,n in product(range(N),repeat=3):
        v={}
        for a in range(N):
            t=b.deriv(P[a][m][q][n],a)
            for s in range(N):
                t=b.add(t,b.mul(Gamma[a][a][s],P[s][m][q][n],9)); t=b.add(t,b.mul(Gamma[m][a][s],P[a][s][q][n],9)); t=b.add(t,b.mul(Gamma[q][a][s],P[a][m][s][n],9)); t=b.add(t,b.mul(Gamma[n][a][s],P[a][m][q][s],9))
            v=b.add(v,t)
        FD[m][q][n]=b.trunc(v,9)
    D=b.pmat()
    for m,n in product(range(N),repeat=2):
        v={}
        for q in range(N):
            t=b.deriv(FD[m][q][n],q)
            for s in range(N):
                t=b.add(t,b.mul(Gamma[m][q][s],FD[s][q][n],8)); t=b.add(t,b.mul(Gamma[q][q][s],FD[m][s][n],8)); t=b.add(t,b.mul(Gamma[n][q][s],FD[m][q][s],8))
            v=b.add(v,t)
        D[m][n]=b.trunc(v,8)
    def bone(a,d):
        v={}
        for q,x,y,f in product(range(N),repeat=4): v=b.add(v,b.mul(b.mul(P[a][q][x][y],gi[d][f],8),Rlow[f][q][x][y],8))
        return b.trunc(v,8)
    B=b.pmat()
    for a,d in product(range(N),repeat=2): B[a][d]=b.scale(b.add(bone(a,d),bone(d,a)),F(1,2))
    alg=mscale(B,F(-1)); div=mscale(D,F(-2)); met=b.pmat()
    for a,d in product(range(N),repeat=2): met[a][d]=b.trunc(b.scale(b.mul(gi[a][d],I3,8),F(1,2)),8)
    Eup=madd(madd(alg,div),met); E=lower(Eup,g)
    return E,{'algebraic_PR':lower(alg,g),'double_divergence':lower(div,g),'metric_I3':lower(met,g),'index_lowering_delta':msub(E,Eup)}

def independent_parts(P,g,gi,Gamma,Rlow,I3):
    U=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,q,d in product(range(N),repeat=3):
        v={}
        for x in range(N):
            t=b.deriv(P[a][q][x][d],x)
            for s in range(N):
                t=b.add(t,b.mul(Gamma[a][x][s],P[s][q][x][d],9)); t=b.add(t,b.mul(Gamma[q][x][s],P[a][s][x][d],9)); t=b.add(t,b.mul(Gamma[x][x][s],P[a][q][s][d],9)); t=b.add(t,b.mul(Gamma[d][x][s],P[a][q][x][s],9))
            v=b.add(v,t)
        U[a][q][d]=b.trunc(v,9)
    T=b.pmat()
    for a,d in product(range(N),repeat=2):
        v={}
        for q in range(N):
            t=b.deriv(U[a][q][d],q)
            for s in range(N):
                t=b.add(t,b.mul(Gamma[a][q][s],U[s][q][d],8)); t=b.add(t,b.mul(Gamma[q][q][s],U[a][s][d],8)); t=b.add(t,b.mul(Gamma[d][q][s],U[a][q][s],8))
            v=b.add(v,t)
        T[a][d]=b.trunc(v,8)
    A=b.pmat()
    for a,d in product(range(N),repeat=2):
        v={}
        for q,x,y,f in product(range(N),repeat=4): v=b.add(v,b.mul(b.mul(P[a][q][x][y],gi[d][f],8),Rlow[f][q][x][y],8))
        A[a][d]=b.trunc(v,8)
    alg=mscale(A,F(-1)); div=mscale(T,F(2)); met=b.pmat()
    for a,d in product(range(N),repeat=2): met[a][d]=b.trunc(b.scale(b.mul(gi[a][d],I3,8),F(1,2)),8)
    Eup=madd(madd(alg,div),met); E=lower(Eup,g)
    return E,{'algebraic_PR':lower(alg,g),'double_divergence':lower(div,g),'metric_I3':lower(met,g),'index_lowering_delta':msub(E,Eup)}

def freeze(mode,boundary):
    g,gi,Gamma,Rlow,I3,P,controls=common(boundary)
    E,parts=(primary_parts(P,g,gi,Gamma,Rlow,I3) if mode=='primary' else independent_parts(P,g,gi,Gamma,Rlow,I3))
    pc=c.p_intrinsic_controls(P,I3,Rlow); comps={k:summary(v) for k,v in parts.items()}; fin=summary(E)
    return {'boundary':boundary,'controls':{**controls,**pc},'components':comps,'final':fin}

def read_at_full():
    body=[]
    for line in AT_PATH.read_text().splitlines():
        if line.strip() and not line.startswith('# '): body.append(line)
    rows=list(csv.DictReader(body)); D={}
    for x in rows:D[(int(x['a']),int(x['b']),tuple(map(int,(x['t'],x['x'],x['y'],x['z']))))]=F(x['value'])
    V=[]
    for a,d in PAIRS:
        for al in b.alphas(6): V.append({'pair':[a,d],'alpha':list(al),'value':fs(D.get((a,d,tuple(al)),0))})
    return V

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',required=True,choices=['primary','independent']); ap.add_argument('--out',required=True); a=ap.parse_args()
    # Outcome-blind phase: AT coefficients are not loaded until both boundaries are frozen in memory.
    r10=freeze(a.mode,'R10'); r12=freeze(a.mode,'R12')
    pre={'gate':'CORRECTED_DEGREE8_DEGREE6_REDUCTION_DISCREPANCY_LOCALIZATION','preregistration_commit':PREREG,'lane':a.mode,'target_loaded_during_decomposition':False,'R10':r10,'R12':r12}
    pre_sha=jsha(pre)
    at=read_at_full(); at_sha=jsha(at)
    controls={'all_intrinsic_controls':all(all(x['controls'].values()) for x in (r10,r12)),'AT_full_ordered_hash_exact':at_sha==AT_SHA,'R12_reproduces_parent_bad_hash':r12['final']['sha256']==BAD_SHA,'exact_no_tolerance':True}
    out={**pre,'pretarget_payload_sha256':pre_sha,'AT_loaded_after_pretarget_freeze':True,'AT_reconstructed_ordered_sha256':at_sha,'R10_equals_AT':r10['final']['vector']==at,'R12_equals_AT':r12['final']['vector']==at,'controls':controls,'c6':'SYMBOLIC_UNFIXED'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    q=dict(out); q['R10']={k:v for k,v in r10.items() if k!='final' and k!='components'}|{'final_sha256':r10['final']['sha256'],'component_sha256':{k:v['sha256'] for k,v in r10['components'].items()}}; q['R12']={k:v for k,v in r12.items() if k!='final' and k!='components'}|{'final_sha256':r12['final']['sha256'],'component_sha256':{k:v['sha256'] for k,v in r12['components'].items()}}; print(json.dumps(q,sort_keys=True,indent=2))
    return 0 if all(controls.values()) else 2
if __name__=='__main__': raise SystemExit(main())
