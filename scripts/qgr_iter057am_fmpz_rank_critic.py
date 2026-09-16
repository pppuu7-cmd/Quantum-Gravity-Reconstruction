#!/usr/bin/env python3
"""Fast exact ZZ rank Critic for frozen Iter057AM complete held-out map.

Each rational B column is multiplied by its own positive LCM of denominators;
the O0 augmented column is independently cleared. These invertible column
scalings preserve ranks over Q exactly. No primary aggregate result is read.
"""
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
from flint import fmpz_mat

PREREG='d555671e69d2be898c7cfdd470f072bbb810a0be'
HELDOUT='AL-R1-4';NROWS=1456;NCOLS=1114
RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973),(973,1114)]

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
 cols={};ranges=[];recs=[]
 for d in sh:
  sha,ok=phash(d);lane=tuple(d.get('lane',[]));ok=ok and lane in RANGES and d.get('heldout_candidate')==HELDOUT and d.get('direct_full_control_mismatch_count')==0
  ids=set()
  for r in d.get('columns',[]):
   j=int(r['index']);ids.add(j);cols[j]={int(i):F(v) for i,v in r.get('nonzero',[])}
  ok=ok and ids==set(range(*lane));ranges.append(lane);recs.append({'lane':list(lane),'payload_sha256':sha,'ok':bool(ok)})
 complete=bok and sorted(ranges)==sorted(RANGES) and len(recs)==8 and all(x['ok'] for x in recs) and set(cols)==set(range(NCOLS))
 return O,cols,bsha,recs,complete

def lcmden(vals):
 d=1
 for v in vals:d=math.lcm(d,v.denominator)
 return d

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();O,cols,bsha,recs,complete=parse(a.input_root)
 rb=ra=None;nnz=None
 if complete:
  B=fmpz_mat(NROWS,NCOLS);nnz=0
  for j in range(NCOLS):
   s=lcmden(cols[j].values()) if cols[j] else 1
   for i,v in cols[j].items():B[i,j]=v.numerator*(s//v.denominator);nnz+=1
  rb=int(B.rank())
  A=fmpz_mat(NROWS,NCOLS+1)
  for i in range(NROWS):
   for j in range(NCOLS):
    x=B[i,j]
    if x:A[i,j]=x
  so=lcmden([x for x in O if x]) if any(O) else 1
  for i,v in enumerate(O):
   if v:A[i,NCOLS]=-v.numerator*(so//v.denominator)
  ra=int(A.rank())
 controls={'raw_complete_and_hash_exact':complete,'B_nnz_81096':nnz==81096,'exact_fmpz_rank_realized':rb is not None,'rank_increment_at_most_one':ra in (rb,rb+1) if rb is not None else False,'no_numerical_tolerance':True,'no_primary_aggregate_consumed':True}
 cls='CONFIRM_SCOPED_ITER057AM_FMPZ_EXACT_RANK_CRITIC' if all(controls.values()) else 'CONTRADICTION_ITER057AM_FMPZ_EXACT_RANK_CRITIC'
 payload={'gate':'ITER057AM-FMPZ-EXACT-RANK-CRITIC','preregistration':PREREG,'classification':cls,'controls':controls,'baseline_payload_sha256':bsha,'shard_payloads':recs,'B_shape':[NROWS,NCOLS],'B_nnz':nnz,'rank_B':rb,'rank_augmented_B_minus_O0':ra,'kernel_dimension':NROWS-rb if rb is not None else None,'obstruction_present':(ra==rb+1 if rb is not None else None),'O0_nonzero_count':sum(x!=0 for x in O),'column_scaling':'independent positive denominator LCM per B column and O0 column; rank invariant over Q'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k!='shard_payloads'},indent=2,sort_keys=True));return 0 if cls.startswith('CONFIRM') else 2
if __name__=='__main__':raise SystemExit(main())
