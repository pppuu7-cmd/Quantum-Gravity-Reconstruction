#!/usr/bin/env python3
"""Frozen completeness-repair precondition for 10dc35e623278c7726b3822096d289e16b1765dd.

This gate first adjudicates the pre-existing false Ricci/scalar controls.  The
preregistration explicitly requires UNRESOLVED if they represent a seed
mismatch, so no desired QF8 outcome is read or inferred here.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import qgr_iter057ap_independent_covariant_source as b
import qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet as aa

PREREG='10dc35e623278c7726b3822096d289e16b1765dd'
N=b.N

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def nz_degrees(p): return sorted({sum(a) for a,v in p.items() if F(v)})
def tensor_support(T):
    out={}
    for i,j in product(range(N),repeat=2):
        ds=nz_degrees(T[i][j])
        if ds: out[f'{i}{j}']=ds
    return out

def lane(mode,out):
    # Historical R10 semantics: seed_metric10 appends the degree-10 metric layer
    # to canonical R8.  geometry8 is the authority-era truncation used by AP;
    # geometry10 asks two curvature orders further without the later R12 layer.
    g,prov,nrows,meta=b.seed_metric10()
    gi8,G8,R8,Ric8,S8,Ein8,C8,inv8=b.geometry8(g)
    gi10,G10,R10,Ric10,S10,Ein10,inv10=aa.geometry10(g)
    if mode=='researcher':
        r8=tensor_support(Ric8); r10=tensor_support(Ric10); s8=nz_degrees(S8); s10=nz_degrees(S10)
    else:
        # Independent traversal/order and direct exact coefficient predicates.
        r8={f'{i}{j}':sorted(set(sum(a) for a,v in Ric8[i][j].items() if v!=0)) for j in range(N) for i in range(N) if any(v!=0 for v in Ric8[i][j].values())}
        r10={f'{i}{j}':sorted(set(sum(a) for a,v in Ric10[i][j].items() if v!=0)) for j in range(N) for i in range(N) if any(v!=0 for v in Ric10[i][j].values())}
        s8=sorted(set(sum(a) for a,v in S8.items() if v!=0)); s10=sorted(set(sum(a) for a,v in S10.items() if v!=0))
    ric8_zero=not r8; scal8_zero=not s8; ric10_zero=not r10; scal10_zero=not s10
    # If the same R10 seed is exact at the historical geometry8 boundary but
    # ceases to be Ricci/scalar zero only when geometry is extended to degree10,
    # this is a truncation/seed-boundary mismatch.  The frozen preregistration
    # mandates UNRESOLVED in that case.
    seed_boundary_mismatch=bool(prov and inv8 and inv10 and ric8_zero and scal8_zero and (not ric10_zero or not scal10_zero))
    cls='UNRESOLVED_QF_DEGREE_BUDGET' if seed_boundary_mismatch else 'PRECONDITION_NOT_LOCALIZED'
    payload={
      'gate':'CORRECTED_DEGREE6_QF_DEGREE_FLOW_COMPLETENESS_REPAIR',
      'preregistration_commit':PREREG,'lane':mode,'classification':cls,
      'seed_provenance_exact':bool(prov),'r10_rows':nrows,
      'historical_geometry8':{'inverse_exact':bool(inv8),'ricci_zero':ric8_zero,'scalar_zero':scal8_zero,'ricci_nonzero_degree_support':r8,'scalar_nonzero_degree_support':s8},
      'extended_geometry10':{'inverse_exact':bool(inv10),'ricci_zero':ric10_zero,'scalar_zero':scal10_zero,'ricci_nonzero_degree_support':r10,'scalar_nonzero_degree_support':s10},
      'seed_boundary_mismatch':seed_boundary_mismatch,
      'qf8_outcome_read_or_used':False,'AT_target_loaded':False,
      'c6_symbolic_unfixed':True,'corrected_Q10_locked':True,
      'note':'Frozen precondition adjudication only. If seed_boundary_mismatch=true, preregistration requires unresolved; no QF8 promotion is authorized.'}
    payload['payload_sha256']=sha(payload)
    Path(out).parent.mkdir(parents=True,exist_ok=True);Path(out).write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
    print(json.dumps(payload,sort_keys=True,indent=2))
    return 0 if seed_boundary_mismatch else 2

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['researcher','critic'],required=True);ap.add_argument('--out',required=True);a=ap.parse_args();raise SystemExit(lane(a.mode,a.out))
