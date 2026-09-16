#!/usr/bin/env python3
"""Iter057AF complete exact R12-branch obstruction aggregation.

Frozen by preregistration 564b3c18b3cf3391a72287138007aa23ebdc37b0.
The B-map is assembled ONLY from immutable Iter057AD lanes 0..6 plus the four
Iter057AF lane-7 subshards. Canonical O0 is recomputed with the unchanged
Iter057AD evaluator as O0=L*r0. No lane science is recomputed here.
"""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import qgr_iter057ad_branch_obstruction as ad
import qgr_iter057ac_tetradecic_einstein_seed_completion as ac
import qgr_iter057z_dodecic_einstein_seed_completion as z

AF_PREREG='564b3c18b3cf3391a72287138007aa23ebdc37b0'
AD_PREREG='8f53a0679692f9655e162aa1a19e45124a8dc775'
AF_SOURCE_HEAD='57b8e0f61e1d77c19eca09a2bd34f48921ffc020'
NROWS=1456; NCOLS=1114
PASS='PASS_SCOPED_ITER057AF_COMPLETE_EXACT_R12_HOMOGENEOUS_OBSTRUCTION_MAP_ADMITS_BRANCH_LIFT__R14_REPLAY_ZERO'
FAIL='SCIENTIFIC_FAIL_ITER057AF_COMPLETE_EXACT_R12_HOMOGENEOUS_FREEDOM_CANNOT_REMOVE_R14_BIANCHI_NOETHER_OBSTRUCTION'
BLOCKED='BLOCKED_ITER057AF_COMPLETE_EXACT_AGGREGATE_OR_WITNESS_REPLAY_NOT_REALIZED'
OLD_RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973)]
AF_RANGES=[(973,1009),(1009,1044),(1044,1079),(1079,1114)]

def q(x):
    if isinstance(x,F): return sp.Rational(x.numerator,x.denominator)
    return sp.Rational(x)

def payload_hash(doc):
    d=dict(doc); got=d.pop('scientific_payload_sha256',None)
    raw=json.dumps(d,sort_keys=True,separators=(',',':')).encode()
    return got, hashlib.sha256(raw).hexdigest()

def find_json(root:Path):
    fs=sorted(root.rglob('*.json'))
    if len(fs)!=1: raise ValueError(f'{root}: expected exactly one JSON, got {len(fs)}')
    return fs[0], json.loads(fs[0].read_text())

def validate_lane(root:Path, expected, tag):
    p,o=find_json(root); got,calc=payload_hash(o)
    checks={'preregistration':o.get('preregistration')==AD_PREREG,'lane':o.get('lane')==list(expected),'M12_shape':o.get('M12_shape')==[4316,4550],'M12_rank':o.get('M12_rank')==3436,'kernel_dimension':o.get('kernel_dimension')==1114,'kernel_exact_annihilation':o.get('kernel_exact_annihilation') is True,'M14_shape':o.get('M14_shape')==[6790,6800],'L14_shape':o.get('L14_shape')==[1456,6790],'L14_annihilates_M14':o.get('L14_annihilates_M14') is True,'canonical_inverse_ok':o.get('canonical_inverse_ok') is True,'canonical_lower_authority_ok':o.get('canonical_lower_authority_ok') is True,'canonical_obstruction_nonzero_count':o.get('canonical_obstruction_nonzero_count')==223,'canonical_obstruction_replays_223':o.get('canonical_obstruction_replays_223') is True,'partial_only_classification':o.get('classification')=='PARTIAL_EXACT_LANE_ONLY__NO_ITER057AD_TERMINAL_CLASSIFICATION','payload_sha256':got==calc}
    cols=o.get('columns'); checks['columns_list']=isinstance(cols,list) and len(cols)==expected[1]-expected[0]; parsed={}
    if checks['columns_list']:
      for rec in cols:
        try:
          j=int(rec['index'])
          if not (expected[0] <= j < expected[1]) or j in parsed: raise ValueError
          if rec.get('inverse_ok') is not True or rec.get('lower_authority_ok') is not True: raise ValueError
          d={}; last=-1
          for ri,sv in rec.get('nonzero',[]):
            ri=int(ri); v=F(str(sv))
            if not (0<=ri<NROWS) or ri<=last or not v: raise ValueError
            last=ri; d[ri]=v
          parsed[j]=d
        except Exception:
          checks['column_records_exact']=False; break
      else: checks['column_records_exact']=set(parsed)==set(range(*expected))
    else: checks['column_records_exact']=False
    return {'tag':tag,'path':str(p),'checks':checks,'payload_sha256':got,'columns':parsed,'raw':o}

def assemble(old_root:Path, af_root:Path):
    records=[]; columns={}
    for i,rng in enumerate(OLD_RANGES): records.append(validate_lane(old_root/str(i),rng,f'AD-{i}'))
    for i,rng in enumerate(AF_RANGES): records.append(validate_lane(af_root/str(i),rng,f'AF-{i}'))
    controls_ok=all(all(r['checks'].values()) for r in records); duplicate=[]
    for r in records:
      for j,c in r['columns'].items():
        if j in columns: duplicate.append(j)
        columns[j]=c
    coverage=(not duplicate and set(columns)==set(range(NCOLS)))
    return records,columns,controls_ok,coverage,duplicate

def original_lane7_match(root:Path|None, records):
    if root is None:return None
    rec=validate_lane(root,(973,1114),'AD-7-diagnostic'); af={}
    for r in records:
      if r['tag'].startswith('AF-'): af.update(r['columns'])
    mismatch=[j for j in range(973,1114) if rec['columns'].get(j)!=af.get(j)]
    return {'artifact_controls_ok':all(rec['checks'].values()),'mismatch_count':len(mismatch),'mismatch_indices':mismatch[:50],'exact_match':not mismatch}

def exact_rank_flint(columns,o0):
    from flint import fmpq,fmpq_mat
    B=fmpq_mat(NROWS,NCOLS); A=fmpq_mat(NROWS,NCOLS+1)
    for j,d in columns.items():
      for i,v in d.items():
        x=fmpq(v.numerator,v.denominator); B[i,j]=x; A[i,j]=x
    for i,x in enumerate(o0):
      x=F(str(x)); A[i,NCOLS]=fmpq(-x.numerator,x.denominator)
    return int(B.rank()),int(A.rank())

def sparse_sympy(columns):
    return sp.MutableSparseMatrix(NROWS,NCOLS,{(i,j):q(v) for j,d in columns.items() for i,v in d.items()})

def exact_hstar(columns,o0):
    B=sparse_sympy(columns); rhs=sp.Matrix([-q(x) for x in o0]); sol=sp.linsolve((B,rhs)); vec=list(next(iter(sol)))
    free=set().union(*(v.free_symbols for v in vec)); subs={s:0 for s in free}; vec=[sp.factor(v.subs(subs)) for v in vec]
    if any(x!=0 for x in B*sp.Matrix(vec)-rhs): raise ArithmeticError('h* exact residual nonzero')
    return vec

def branch_r14_replay(h,basis,a12,g0,L):
    combo=[sp.Integer(0)]*len(basis[0])
    for i,c in enumerate(h):
      if c:
        for j,x in enumerate(basis[i]):
          if x: combo[j]+=c*x
    g=[[dict(g0[a][b]) for b in range(4)] for a in range(4)]; ad.add_direction(g,combo,a12)
    M14,rows14,meta14,a11,rhs,inv_before=ad.rhs14(g); compat=L*rhs; compat_nz=sum(x!=0 for x in compat)
    rank=DomainMatrix.from_Matrix(M14).to_field().rank(); arank=DomainMatrix.from_Matrix(M14.row_join(rhs)).to_field().rank()
    out={'inverse_before_ok':bool(inv_before),'M14_rank':rank,'M14_augmented_rank':arank,'compatibility_nonzero_count':compat_nz}
    if rank!=arank or compat_nz: out['solved']=False; return out,[],g
    sol=sp.linsolve((M14,rhs)); vec=list(next(iter(sol))); free=set().union(*(v.free_symbols for v in vec)); subs={s:0 for s in free};vec=[sp.factor(v.subs(subs)) for v in vec]
    _,_,_,_,_,_,a14=ac.system(); nz=[]; Kr=sp.Rational(z.K.numerator,z.K.denominator)
    for p,pair in enumerate(z.PAIRS):
      for j,al in enumerate(a14):
        v=vec[p*len(a14)+j]
        if v:
          norm=sp.factor(v*math.prod(math.factorial(x) for x in al)/(Kr**7)); nz.append({'pair':list(pair),'alpha':list(al),'R14_over_kappa7':str(norm)})
    z.add_trace_reversed_layer(g,nz,7,'R14_over_kappa7',14); gau=ac.gauge(g); Ric,Sc,Ein,inv_after=ac.einstein(g,12)
    replay_g=sum(bool(z.trunc(v,13)) for v in gau); replay_e=sum(bool(z.trunc(Ein[a][b],12)) for a,b in z.PAIRS)
    out.update({'solved':True,'R14_particular_nonzero_count':len(nz),'inverse_after_ok':bool(inv_after),'full_deDonder_nonzero_component_count':replay_g,'einstein_nonzero_component_count':replay_e})
    return out,nz,g

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--old-root',required=True);ap.add_argument('--af-root',required=True);ap.add_argument('--original-lane7-root');ap.add_argument('--source-run',type=int,required=True);ap.add_argument('--source-head',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
    records,columns,lane_controls,coverage,duplicate=assemble(Path(args.old_root),Path(args.af_root)); cross=original_lane7_match(Path(args.original_lane7_root) if args.original_lane7_root else None,records)
    M12,rows12,meta12,a12,basis=ad.kernel_data(); kernel_ok=all(not any(M12*sp.Matrix(v)) for v in basis)
    g0,prov=ad.canonical_seed12(); M14,rows14,meta14,a11,r0,inv0=ad.rhs14(g0); L=ad.left_controls(rows14,meta14,a11)
    left_ann=(L*M14)==sp.zeros(L.rows,M14.cols); O0=L*r0; o0_nz=sum(x!=0 for x in O0)
    structural=(M12.shape==(4316,4550) and len(basis)==1114 and kernel_ok and M14.shape==(6790,6800) and L.shape==(1456,6790) and left_ann and bool(prov) and bool(inv0) and o0_nz==223)
    rankB=rankA=None; h=[]; replay={};r14=[]
    if lane_controls and coverage and structural:
      rankB,rankA=exact_rank_flint(columns,O0)
      if rankB==rankA: h=exact_hstar(columns,O0); replay,r14,_=branch_r14_replay(h,basis,a12,g0,L)
    source_ok=(args.source_head==AF_SOURCE_HEAD)
    if not (lane_controls and coverage and structural and source_ok): classification=BLOCKED
    elif rankA is not None and rankB is not None and rankA>rankB: classification=FAIL
    elif rankA==rankB and replay.get('solved') and replay.get('compatibility_nonzero_count')==0 and replay.get('M14_rank')==5334 and replay.get('M14_augmented_rank')==5334 and replay.get('inverse_before_ok') and replay.get('inverse_after_ok') and replay.get('full_deDonder_nonzero_component_count')==0 and replay.get('einstein_nonzero_component_count')==0: classification=PASS
    else: classification=BLOCKED
    h_sparse=[{'basis_index':i,'value':str(v)} for i,v in enumerate(h) if v]
    summary_records=[{'tag':r['tag'],'path':r['path'],'checks':r['checks'],'payload_sha256':r['payload_sha256'],'column_count':len(r['columns']),'range':r['raw'].get('lane')} for r in records]
    payload={'gate':'ITER057AF-LANE7-EXACT-PAYLOAD-COMPLETION-AND-FULL-OBSTRUCTION-AGGREGATE','preregistration':AF_PREREG,'source_run':args.source_run,'source_head':args.source_head,'expected_source_head':AF_SOURCE_HEAD,'classification':classification,'lane_payload_controls_ok':lane_controls,'complete_unique_coverage':coverage,'duplicate_indices':duplicate,'lane_records':summary_records,'original_lane7_diagnostic_match':cross,'M12_shape':list(M12.shape),'M12_rank':M12.cols-len(basis),'kernel_dimension':len(basis),'kernel_exact_annihilation':kernel_ok,'M14_shape':list(M14.shape),'L14_shape':list(L.shape),'L14_annihilates_M14':left_ann,'canonical_lower_authority_ok':bool(prov),'canonical_inverse_ok':bool(inv0),'canonical_obstruction_nonzero_count':o0_nz,'B_shape':[NROWS,NCOLS],'rank_B':rankB,'rank_augmented_B_minus_O0':rankA,'hstar_nonzero_count':len(h_sparse),'hstar':h_sparse,'branch_R14_replay':replay,'R14_particular_normalized':r14,'scope':'finite local exact Taylor/jet branch certificate only; c6 symbolic/unfixed; beta=1 unauthorized; theory established 0%'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k not in ('hstar','R14_particular_normalized','lane_records')},indent=2,sort_keys=True)); return 0 if classification in (PASS,FAIL) else 2
if __name__=='__main__': raise SystemExit(main())
