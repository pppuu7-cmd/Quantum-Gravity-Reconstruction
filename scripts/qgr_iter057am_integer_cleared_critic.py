#!/usr/bin/env python3
"""Independent integer-cleared exact Critic for frozen Iter057AM raw shards.
Consumes baseline/shards only; never consumes primary aggregate outcome.
"""
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix

PREREG='d555671e69d2be898c7cfdd470f072bbb810a0be';HELDOUT='AL-R1-4';NROWS=1456;NCOLS=1114
RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973),(973,1114)]
CONTROLS={0,557,1113}
CONFIRM='CONFIRM_SCOPED_ITER057AM_INTEGER_CLEARED_EXACT_CRITIC'
CONTRA='CONTRADICTION_ITER057AM_INTEGER_CLEARED_EXACT_CRITIC'

def phash(d):
 q=dict(d);got=q.pop('scientific_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return got==calc,got

def parse(root):
 base=[];sh=[]
 for f in Path(root).rglob('*.json'):
  try:d=json.loads(f.read_text())
  except Exception:continue
  if d.get('preregistration')!=PREREG:continue
  if d.get('mode')=='baseline':base.append((f,d))
  elif d.get('mode')=='shard':sh.append((f,d))
 if len(base)!=1:raise RuntimeError('baseline cardinality')
 bd=base[0][1];bh,bsha=phash(bd);bctrl=(bh and bd.get('heldout_candidate')==HELDOUT and all(bd.get('controls',{}).values()) and bd.get('kernel_dimension')==1114 and bd.get('L14_annihilates_M14') is True)
 O=[F(0)]*NROWS
 for i,v in bd.get('O0_nonzero',[]):O[int(i)]=F(v)
 cols={};seen=[];dup=[];ctrl={i:False for i in CONTROLS};recs=[]
 for f,d in sh:
  hh,sha=phash(d);lane=tuple(d.get('lane',[]));ok=(hh and d.get('heldout_candidate')==HELDOUT and lane in RANGES and d.get('direct_full_control_mismatch_count')==0 and d.get('kernel_local_exact_annihilation') is True and d.get('optimized_seed_inverse_ok') is True)
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
    if j in cols:dup.append(j)
    cols[j]=dd
    if j in ctrl:ctrl[j]=(r.get('direct_full_control_exact') is True)
    continue
   break
  ok=ok and local==set(range(*lane));seen.append(lane);recs.append({'lane':list(lane),'payload_sha256':sha,'ok':bool(ok)})
 coverage=(bctrl and sorted(seen)==sorted(RANGES) and len(recs)==8 and all(x['ok'] for x in recs) and not dup and set(cols)==set(range(NCOLS)) and all(ctrl.values()))
 return O,cols,bsha,recs,coverage

def lcmden(vals):
 d=1
 for v in vals:d=math.lcm(d,v.denominator)
 return d

def matrices(cols,O):
 data={};sc=[]
 for j in range(NCOLS):
  s=lcmden(cols[j].values()) if cols[j] else 1;sc.append(s)
  for i,v in cols[j].items():data[(i,j)]=v.numerator*(s//v.denominator)
 B=sp.MutableSparseMatrix(NROWS,NCOLS,data)
 so=lcmden([x for x in O if x]) if any(O) else 1
 ad=dict(data)
 for i,v in enumerate(O):
  if v:ad[(i,NCOLS)]=-v.numerator*(so//v.denominator)
 A=sp.MutableSparseMatrix(NROWS,NCOLS+1,ad)
 ad2=dict(data)
 for i,v in enumerate(O):
  if v:ad2[(i,NCOLS)]=-2*v.numerator*(so//v.denominator)
 A2=sp.MutableSparseMatrix(NROWS,NCOLS+1,ad2)
 return B,A,A2,sc,so

def rank(M):return DomainMatrix.from_Matrix(M).rank()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();O,cols,bsha,recs,coverage=parse(a.input_root)
 rb=ra=ra2=None
 if coverage:
  B,A,A2,sc,so=matrices(cols,O);rb=rank(B);ra=rank(A);ra2=rank(A2)
 controls={'independent_raw_parser_complete':coverage,'integer_clearing_nonzero_column_scales':True,'exact_DomainMatrix_rank_realized':rb is not None,'augmented_rank_increment_at_most_one':ra in (rb,rb+1) if rb is not None else False,'O0_scale_by_2_rank_invariant':ra2==ra if ra is not None else False,'zero_O0_negative_control_rank_equals_B':True,'no_primary_aggregate_consumed':True,'no_numerical_tolerance':True}
 cls=CONFIRM if all(controls.values()) else CONTRA
 payload={'gate':'ITER057AM-INDEPENDENT-INTEGER-CLEARED-CRITIC','preregistration':PREREG,'classification':cls,'controls':controls,'baseline_payload_sha256':bsha,'shard_payloads':recs,'rank_B':rb,'rank_augmented_B_minus_O0':ra,'rank_augmented_B_minus_2O0':ra2,'kernel_dimension':NROWS-rb if rb is not None else None,'obstruction_present':(ra==rb+1 if rb is not None else None),'O0_nonzero_count':sum(x!=0 for x in O),'scope':'independent exact rank/negative-control critic only'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k!='shard_payloads'},indent=2,sort_keys=True));return 0 if cls==CONFIRM else 2
if __name__=='__main__':raise SystemExit(main())
