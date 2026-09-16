#!/usr/bin/env python3
"""Exact terminal-decision certificate for frozen Iter057AM.

The rank proof is algebraically exact, not numerical: reduce the rational
matrix modulo the first prime in the frozen certificate list for which every
denominator is invertible. If the reduced matrix has full column rank, then a
maximal minor is nonzero modulo p and therefore the corresponding rational
minor is nonzero over Q. Hence rank_Q equals the column count exactly.

A held-out dual witness is constructed independently from held-out B/O0 data
inside the pre-existing terminal-AH b=0, parity=1000 coordinate sector. AG
coefficients are not read until after that new witness has been normalized and
replayed. Sector support is not a PASS criterion; it is only a deterministic
independent witness-construction lane using authority frozen before Iter057AM.
"""
import argparse,hashlib,itertools,json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

PREREG='d555671e69d2be898c7cfdd470f072bbb810a0be'
HELDOUT='AL-R1-4';NROWS=1456;NCOLS=1114
RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973),(973,1114)]
VALIDATION_SHA='0ae32c1cdc7d003afcc516e7bf99108cf8a768b42a83806479cc837583488203'
PRIME_LIST=(1000003,1000033,1000037)
PASS='PASS_SCOPED_ITER057AM_HELDOUT_NO_REFIT_R14_OBSTRUCTION_CLASS_PERSISTS_ON_INDEPENDENT_ONSHELL_BACKGROUND'
AG_PATH=Path(__file__).resolve().parents[1]/'data'/'ITER057AG_CANONICAL_DUAL_WITNESS.json'
AG_SHA='5ecb962af9a1265a8846a6d8de4cd0885c2b53bea630a5729a8c069aae9fd9da'

def phash(d):
 q=dict(d);got=q.pop('scientific_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return got,got==calc

def parse(root):
 base=[];sh=[]
 for f in Path(root).rglob('*.json'):
  try:d=json.loads(f.read_text())
  except Exception:continue
  if d.get('preregistration')!=PREREG:continue
  if d.get('mode')=='baseline':base.append(d)
  elif d.get('mode')=='shard':sh.append(d)
 if len(base)!=1:raise RuntimeError('baseline cardinality')
 bd=base[0];bsha,bok=phash(bd);bok=bok and bd.get('heldout_candidate')==HELDOUT and all(bd.get('controls',{}).values())
 O=[F(0)]*NROWS
 for i,v in bd.get('O0_nonzero',[]):O[int(i)]=F(v)
 cols={};ranges=[];recs=[];dups=[];control_seen={0:False,557:False,1113:False}
 for d in sh:
  sha,ok=phash(d);lane=tuple(d.get('lane',[]));ok=ok and lane in RANGES and d.get('heldout_candidate')==HELDOUT and d.get('direct_validation_payload_sha256')==VALIDATION_SHA and d.get('direct_full_control_mismatch_count')==0 and d.get('kernel_local_exact_annihilation') is True
  local=set()
  for r in d.get('columns',[]):
   j=int(r['index']);dd={};last=-1
   if not(lane[0]<=j<lane[1]) or j in local:ok=False;break
   local.add(j)
   for i,s in r.get('nonzero',[]):
    i=int(i);v=F(s)
    if not(0<=i<NROWS) or i<=last or not v:ok=False;break
    last=i;dd[i]=v
   else:
    if j in cols:dups.append(j)
    cols[j]=dd
    if j in control_seen:control_seen[j]=(r.get('direct_full_control_exact') is True)
    continue
   break
  ok=ok and local==set(range(*lane));ranges.append(lane);recs.append({'lane':list(lane),'payload_sha256':sha,'ok':bool(ok)})
 complete=(bok and sorted(ranges)==sorted(RANGES) and len(recs)==8 and all(x['ok'] for x in recs) and not dups and set(cols)==set(range(NCOLS)) and all(control_seen.values()))
 return bd,O,cols,bsha,sorted(recs,key=lambda x:x['lane'][0]),complete

def first_good_prime(cols,O):
 dens=[]
 for d in cols.values():dens.extend(v.denominator for v in d.values())
 dens.extend(v.denominator for v in O if v)
 for p in PRIME_LIST:
  if all(d%p for d in dens):return p
 raise RuntimeError('no frozen certificate prime avoids denominators')

def modcol(d,p,sign=1):return {i:(sign*v.numerator*pow(v.denominator,-1,p))%p for i,v in d.items() if v}

def sparse_column_rank(columns,p,nrows):
 piv={};pivrows=[]
 for v0 in columns:
  v={i:x%p for i,x in v0.items() if x%p}
  while v:
   r=min(v)
   if r not in piv:
    inv=pow(v[r],p-2,p);v={i:(x*inv)%p for i,x in v.items() if (x*inv)%p};piv[r]=v;pivrows.append(r);break
   c=v[r];q=piv[r]
   for i,x in q.items():
    nv=(v.get(i,0)-c*x)%p
    if nv:v[i]=nv
    elif i in v:del v[i]
 return len(piv),pivrows

def degree11_alphas():return sorted(a for a in itertools.product(range(12),repeat=4) if sum(a)==11)

def fresh_sector_witness(cols,O):
 A=degree11_alphas();ids=[j for j,a in enumerate(A) if tuple(x%2 for x in a)==(1,0,0,0)]
 if len(ids)!=56:raise RuntimeError('AH sector cardinality drift')
 lookup={i:k for k,i in enumerate(ids)};C=sp.MutableSparseMatrix(NCOLS,len(ids),{})
 for j,d in cols.items():
  for i,v in d.items():
   if i in lookup:C[j,lookup[i]]=sp.Rational(v.numerator,v.denominator)
 ns=C.nullspace()
 if len(ns)!=1:raise RuntimeError(f'fresh held-out AH-sector nullity={len(ns)}, expected 1 for this witness-construction lane')
 v=ns[0];pair=sp.Rational(0)
 for k,i in enumerate(ids):pair+=sp.Rational(O[i].numerator,O[i].denominator)*v[k]
 if pair==0:raise RuntimeError('fresh held-out sector witness has zero O0 pairing')
 y=[sp.Rational(0)]*NROWS
 for k,i in enumerate(ids):y[i]=sp.factor(v[k]/pair)
 btnz=0
 for j,d in cols.items():
  s=sp.Rational(0)
  for i,x in d.items():
   if y[i]:s+=sp.Rational(x.numerator,x.denominator)*y[i]
  if s!=0:btnz+=1
 p2=sum((sp.Rational(O[i].numerator,O[i].denominator)*y[i] for i in range(NROWS)),sp.Rational(0))
 return ids,y,pair,btnz,p2,len(ids)-len(ns),len(ns)

def ag_postcheck(y,O):
 d=json.loads(AG_PATH.read_text());ref=[sp.Rational(0)]*NROWS
 for r in d.get('canonical_y',[]):ref[int(r['compatibility_index'])]=sp.Rational(r['value'])
 provenance=d.get('scientific_payload_sha256')==AG_SHA
 pair=sum((sp.Rational(O[i].numerator,O[i].denominator)*ref[i] for i in range(NROWS)),sp.Rational(0))
 norm=[sp.factor(q/pair) for q in ref] if pair else ref
 return provenance,pair,norm==y

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();bd,O,cols,bsha,recs,complete=parse(a.input_root)
 p=first_good_prime(cols,O) if complete else None;rb=ra=None;pivB=[];pivA=[]
 if complete:
  bcols=[modcol(cols[j],p) for j in range(NCOLS)];rb,pivB=sparse_column_rank(bcols,p,NROWS)
  od={i:v for i,v in enumerate(O) if v};ra,pivA=sparse_column_rank(bcols+[modcol(od,p,sign=-1)],p,NROWS)
 ids=y=pair=None;btnz=None;p2=None;srank=snull=None;agprov=False;agpair=None;agmatch=False
 if complete:
  ids,y,pair,btnz,p2,srank,snull=fresh_sector_witness(cols,O);agprov,agpair,agmatch=ag_postcheck(y,O)
 rank_Q_B=(rb if rb==NCOLS else None);rank_Q_A=(ra if ra==NCOLS+1 else None)
 kernel=(NROWS-rank_Q_B if rank_Q_B is not None else None);cap=(kernel-1 if kernel is not None and rank_Q_A==rank_Q_B+1 else None);quot=(kernel-cap if cap is not None else None)
 controls={'complete_raw_authority_and_hashes':complete,'first_frozen_prime_used':p==PRIME_LIST[0],'B_full_column_rank_mod_p':rb==NCOLS,'augmented_full_column_rank_mod_p':ra==NCOLS+1,'rational_rank_B_certified_by_nonzero_modular_maximal_minor':rank_Q_B==NCOLS,'rational_rank_augmented_certified_by_nonzero_modular_maximal_minor':rank_Q_A==NCOLS+1,'fresh_AH_sector_witness_constructed_without_AG_coefficients':snull==1 and srank==55,'fresh_witness_BT_y_zero_exact':btnz==0,'fresh_witness_O0T_y_one_exact':p2==1,'obstruction_quotient_dimension_one':quot==1,'AG_loaded_only_postconstruction_and_provenance_exact':agprov,'no_numerical_tolerance':True}
 classification=PASS if all(controls.values()) else 'INVALID_OR_CONTRADICTED_ITER057AM_EXACT_MODULAR_CERTIFICATE'
 payload={'gate':'ITER057AM-EXACT-MODULAR-FULL-RANK-AND-FRESH-WITNESS-CERTIFICATE','preregistration':PREREG,'classification':classification,'heldout_candidate':HELDOUT,'controls':controls,'certificate_prime':p,'certificate_prime_rule':'first prime in frozen ordered list [1000003,1000033,1000037] for which every rational denominator is invertible; no rank-dependent prime selection','B_shape':[NROWS,NCOLS],'B_nnz':sum(len(d) for d in cols.values()),'rank_B':rank_Q_B,'rank_augmented_B_minus_O0':rank_Q_A,'kernel_dimension':kernel,'kernel_O0_perp_dimension':cap,'obstruction_quotient_dimension':quot,'O0_nonzero_count':sum(v!=0 for v in O),'mod_p_B_pivot_row_count':len(pivB),'mod_p_augmented_pivot_row_count':len(pivA),'fresh_witness_sector':'pre-existing terminal-AH b=0 parity=1000 sector; not a PASS criterion','fresh_witness_pre_normalization_pairing':str(pair) if pair is not None else None,'fresh_witness_nonzero_count':sum(q!=0 for q in y) if y else None,'fresh_witness_BT_y_nonzero_count':btnz,'fresh_witness_O0T_y':str(p2) if p2 is not None else None,'fresh_normalized_witness':[[i,str(q)] for i,q in enumerate(y) if q] if y else None,'postconstruction_AG_transport_pairing':str(agpair) if agpair is not None else None,'postconstruction_fresh_witness_matches_normalized_AG':agmatch,'baseline_payload_sha256':bsha,'shard_payloads':recs,'scope':'one prospectively held-out independent finite local R12 background; exact finite-field maximal-minor rank certificate plus exact rational dual witness'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k not in ('fresh_normalized_witness','shard_payloads')},indent=2,sort_keys=True));return 0 if classification==PASS else 2
if __name__=='__main__':raise SystemExit(main())
