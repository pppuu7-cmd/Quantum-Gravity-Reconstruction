#!/usr/bin/env python3
"""Fast exact Iter057AF obstruction-rank decision.

This is a decision-preserving fast path for the frozen Iter057AF gate. It does
not reconstruct M12's kernel: each consumed lane payload has already reproduced
and serialized the prospectively frozen kernel controls. The script validates
all eleven immutable/AF payloads, assembles the complete 1456x1114 B, recomputes
only canonical O0=L*r0 with the unchanged Iter057AD evaluator, and computes
exact rational ranks with python-flint.

A rank increase authorizes the preregistered FAIL. Equal ranks are deliberately
nonterminal here because h* plus unrestricted R14/nonlinear replay remain needed
for PASS.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
import qgr_iter057ad_branch_obstruction as ad

AF_PREREG='564b3c18b3cf3391a72287138007aa23ebdc37b0'
AD_PREREG='8f53a0679692f9655e162aa1a19e45124a8dc775'
AF_SOURCE_HEAD='57b8e0f61e1d77c19eca09a2bd34f48921ffc020'
NROWS=1456; NCOLS=1114
FAIL='SCIENTIFIC_FAIL_ITER057AF_COMPLETE_EXACT_R12_HOMOGENEOUS_FREEDOM_CANNOT_REMOVE_R14_BIANCHI_NOETHER_OBSTRUCTION'
CONSISTENT='CONSISTENT_ITER057AF_EXACT_RANKS__HSTAR_AND_R14_REPLAY_STILL_REQUIRED_FOR_PASS'
BLOCKED='BLOCKED_ITER057AF_EXACT_RANK_ONLY_AGGREGATE_NOT_REALIZED'
OLD_RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973)]
AF_RANGES=[(973,1009),(1009,1044),(1044,1079),(1079,1114)]

def payload_hash(doc):
    d=dict(doc); got=d.pop('scientific_payload_sha256',None)
    return got,hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def one_json(root):
    fs=sorted(Path(root).rglob('*.json'))
    if len(fs)!=1: raise ValueError(f'{root}: expected exactly one json, got {len(fs)}')
    return fs[0],json.loads(fs[0].read_text())

def consume(root,rng,tag):
    p,o=one_json(root); got,calc=payload_hash(o)
    checks={
      'preregistration':o.get('preregistration')==AD_PREREG,
      'lane':o.get('lane')==list(rng),
      'M12_shape':o.get('M12_shape')==[4316,4550],
      'M12_rank':o.get('M12_rank')==3436,
      'kernel_dimension':o.get('kernel_dimension')==1114,
      'kernel_exact_annihilation':o.get('kernel_exact_annihilation') is True,
      'M14_shape':o.get('M14_shape')==[6790,6800],
      'L14_shape':o.get('L14_shape')==[1456,6790],
      'L14_annihilates_M14':o.get('L14_annihilates_M14') is True,
      'canonical_inverse_ok':o.get('canonical_inverse_ok') is True,
      'canonical_lower_authority_ok':o.get('canonical_lower_authority_ok') is True,
      'canonical_obstruction_nonzero_count':o.get('canonical_obstruction_nonzero_count')==223,
      'canonical_obstruction_replays_223':o.get('canonical_obstruction_replays_223') is True,
      'partial_only':o.get('classification')=='PARTIAL_EXACT_LANE_ONLY__NO_ITER057AD_TERMINAL_CLASSIFICATION',
      'payload_hash':got==calc,
    }
    cols={}
    for rec in o.get('columns',[]):
      j=int(rec['index'])
      if not (rng[0]<=j<rng[1]) or j in cols or rec.get('inverse_ok') is not True or rec.get('lower_authority_ok') is not True:
        checks['column_records']=False; break
      d={}; last=-1
      for i,s in rec.get('nonzero',[]):
        i=int(i); v=F(str(s))
        if i<=last or not (0<=i<NROWS) or not v: checks['column_records']=False; break
        last=i; d[i]=v
      else:
        cols[j]=d; continue
      break
    else:
      checks['column_records']=set(cols)==set(range(*rng))
    return {'tag':tag,'file':str(p),'checks':checks,'payload_sha256':got,'columns':cols}

def exact_ranks(columns,o0):
    from flint import fmpq,fmpq_mat
    B=fmpq_mat(NROWS,NCOLS); A=fmpq_mat(NROWS,NCOLS+1)
    for j,d in columns.items():
      for i,v in d.items():
        x=fmpq(v.numerator,v.denominator); B[i,j]=x; A[i,j]=x
    for i,x in enumerate(o0):
      n=int(x.p); d=int(x.q); A[i,NCOLS]=fmpq(-n,d)
    return int(B.rank()),int(A.rank())

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--source-run',type=int,required=True);ap.add_argument('--source-head',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    recs=[]; cols={}; dup=[]
    for i,r in enumerate(OLD_RANGES): recs.append(consume(Path(a.old_root)/str(i),r,f'AD-{i}'))
    for i,r in enumerate(AF_RANGES): recs.append(consume(Path(a.af_root)/str(i),r,f'AF-{i}'))
    controls=all(all(r['checks'].values()) for r in recs)
    for r in recs:
      for j,d in r['columns'].items():
        if j in cols: dup.append(j)
        cols[j]=d
    coverage=(not dup and set(cols)==set(range(NCOLS)))
    g0,prov=ad.canonical_seed12(); M14,rows14,meta14,a11,r0,inv=ad.rhs14(g0); L=ad.left_controls(rows14,meta14,a11); ann=(L*M14).is_zero_matrix
    O0=L*r0; o0nz=sum(x!=0 for x in O0)
    structural=(M14.shape==(6790,6800) and L.shape==(1456,6790) and ann and bool(prov) and bool(inv) and o0nz==223)
    rb=ra=None
    if controls and coverage and structural and a.source_head==AF_SOURCE_HEAD: rb,ra=exact_ranks(cols,O0)
    if rb is not None and ra is not None and ra>rb: cls=FAIL
    elif rb is not None and ra==rb: cls=CONSISTENT
    else: cls=BLOCKED
    payload={'gate':'ITER057AF-LANE7-EXACT-PAYLOAD-COMPLETION-AND-FULL-OBSTRUCTION-RANK-DECISION','preregistration':AF_PREREG,'source_run':a.source_run,'source_head':a.source_head,'expected_source_head':AF_SOURCE_HEAD,'classification':cls,'lane_payload_controls_ok':controls,'complete_unique_coverage':coverage,'duplicate_indices':dup,'B_shape':[NROWS,NCOLS],'B_nnz':sum(len(d) for d in cols.values()),'canonical_lower_authority_ok':bool(prov),'canonical_inverse_ok':bool(inv),'M14_shape':list(M14.shape),'L14_shape':list(L.shape),'L14_annihilates_M14':bool(ann),'canonical_obstruction_nonzero_count':o0nz,'rank_B':rb,'rank_augmented_B_minus_O0':ra,'terminal_authority':bool(ra is not None and rb is not None and ra>rb),'lane_records':[{'tag':r['tag'],'file':r['file'],'payload_sha256':r['payload_sha256'],'checks':r['checks'],'column_count':len(r['columns'])} for r in recs],'scope':'finite local exact obstruction-rank certificate only; equal ranks require h* and unrestricted R14 replay; c6 symbolic/unfixed; theory established 0%'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k!='lane_records'},indent=2,sort_keys=True)); return 0 if cls in (FAIL,CONSISTENT) else 2
if __name__=='__main__': raise SystemExit(main())
