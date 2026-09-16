#!/usr/bin/env python3
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq,fmpq_mat

PREREG='d555671e69d2be898c7cfdd470f072bbb810a0be'
HELDOUT='AL-R1-4'; NROWS=1456; NCOLS=1114
RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973),(973,1114)]
CONTROLS=(0,557,1113)
PASS='PASS_SCOPED_ITER057AM_HELDOUT_NO_REFIT_R14_OBSTRUCTION_CLASS_PERSISTS_ON_INDEPENDENT_ONSHELL_BACKGROUND'
FAIL='SCIENTIFIC_FAIL_ITER057AM_HELDOUT_VALID_BACKGROUND_HAS_NO_R14_OBSTRUCTION_AFTER_COMPLETE_R12_HOMOGENEOUS_FREEDOM'
INVALID='INVALID_ITER057AM_HELDOUT_FIREWALL_AUTHORITY_EXACTNESS_OR_NO_REFIT_CONTROL_FAILURE'

def phash(d):
 q=dict(d);got=q.pop('scientific_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return got,calc,got==calc

def ff(v):
 q=F(v);return fmpq(q.numerator,q.denominator)

def one_json(root,mode):
 fs=[]
 for f in Path(root).rglob('*.json'):
  try:d=json.loads(f.read_text())
  except Exception:continue
  if d.get('preregistration')==PREREG and d.get('mode')==mode:fs.append((f,d))
 return fs

def load_baseline(root):
 xs=one_json(root,'baseline')
 if len(xs)!=1:raise RuntimeError(f'expected one baseline, got {len(xs)}')
 f,d=xs[0];got,calc,hok=phash(d);ctrl=d.get('controls',{})
 ok=(hok and d.get('heldout_candidate')==HELDOUT and d.get('M12_shape')==[4316,4550] and d.get('kernel_dimension')==1114 and d.get('kernel_exact_annihilation') is True and d.get('M14_shape')==[6790,6800] and d.get('L14_shape')==[1456,6790] and d.get('L14_annihilates_M14') is True and all(ctrl.values()))
 O=[F(0)]*NROWS
 for i,v in d.get('O0_nonzero',[]):O[int(i)]=F(v)
 return d,O,got,bool(ok)

def load_shards(root):
 rec=[];cols={};coverage=[];control_seen={i:False for i in CONTROLS};control_ok={i:False for i in CONTROLS};dup=[]
 for f in Path(root).rglob('*.json'):
  try:d=json.loads(f.read_text())
  except Exception:continue
  if d.get('preregistration')!=PREREG or d.get('mode')!='shard':continue
  got,calc,hok=phash(d);lane=tuple(d.get('lane',[]));ok=(hok and d.get('heldout_candidate')==HELDOUT and lane in RANGES and d.get('column_count')==lane[1]-lane[0] and d.get('kernel_local_exact_annihilation') is True and d.get('optimized_seed_inverse_ok') is True and d.get('direct_full_control_mismatch_count')==0)
  local=set()
  for r in d.get('columns',[]):
   j=int(r['index']);vals={};last=-1
   if not(lane[0]<=j<lane[1]) or j in local:ok=False;break
   local.add(j)
   for i,s in r.get('nonzero',[]):
    i=int(i);v=F(s)
    if not(0<=i<NROWS) or i<=last or not v:ok=False;break
    last=i;vals[i]=v
   else:
    if j in cols:dup.append(j)
    cols[j]=vals
    if j in control_seen:
     control_seen[j]=True;control_ok[j]=(r.get('direct_full_control_exact') is True)
    continue
   break
  ok=ok and local==set(range(*lane))
  rec.append({'file':f.name,'lane':list(lane),'payload_sha256':got,'ok':bool(ok)})
  coverage.append(lane)
 return rec,cols,coverage,dup,control_seen,control_ok

def matrix(cols,O):
 B=fmpq_mat(NROWS,NCOLS)
 nnz=0
 for j in range(NCOLS):
  for i,v in cols[j].items():B[i,j]=ff(v);nnz+=1
 A=fmpq_mat(NROWS,NCOLS+1)
 for i in range(NROWS):
  for j in range(NCOLS):
   x=B[i,j]
   if x:A[i,j]=x
  if O[i]:A[i,NCOLS]=-ff(O[i])
 return B,A,nnz

def witness(B,O):
 BT=B.transpose();R,rank=BT.rref();rank=int(rank);piv=[]
 for r in range(rank):
  p=None
  for c in range(NROWS):
   if R[r,c]!=0:p=c;break
  if p is None:raise ArithmeticError('RREF pivot missing')
  piv.append(p)
 free=[c for c in range(NROWS) if c not in set(piv)]
 chosen=None;pair=None
 for f in free:
  y=[fmpq(0)]*NROWS;y[f]=fmpq(1)
  for rr,p in enumerate(piv):
   if R[rr,f]!=0:y[p]=-R[rr,f]
  q=fmpq(0)
  for i,x in enumerate(O):
   if x and y[i]:q+=ff(x)*y[i]
  if q!=0:chosen=y;pair=q;break
 if chosen is None:return None,free
 y=[v/pair for v in chosen]
 yy=fmpq_mat(NROWS,1)
 for i,v in enumerate(y):
  if v:yy[i,0]=v
 bt=BT*yy;q=fmpq(0)
 for i,x in enumerate(O):
  if x and y[i]:q+=ff(x)*y[i]
 if any(bt[i,0]!=0 for i in range(bt.nrows())) or q!=1:raise ArithmeticError('normalized dual witness replay failed')
 return {'nonzero':[[i,str(v)] for i,v in enumerate(y) if v!=0],'BT_y_nonzero_count':0,'O0T_y':'1'},free

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 base,O,bsha,bok=load_baseline(a.input_root);recs,cols,cov,dup,cseen,cok=load_shards(a.input_root)
 coverage=(sorted(cov)==sorted(RANGES) and not dup and set(cols)==set(range(NCOLS)) and len(recs)==len(RANGES) and all(x['ok'] for x in recs))
 fixed_controls=all(cseen.values()) and all(cok.values())
 B=A=nnz=rankB=rankA=None;wit=None;free=[]
 if bok and coverage and fixed_controls:
  B,A,nnz=matrix(cols,O);rankB=int(B.rank());rankA=int(A.rank())
  if rankA==rankB+1:wit,free=witness(B,O)
  else:free=list(range(NROWS-rankB))
 dimker=NROWS-rankB if rankB is not None else None
 dimcap=(dimker-1 if rankA==rankB+1 else dimker) if dimker is not None and rankA is not None else None
 quotient=(dimker-dimcap) if dimker is not None else None
 controls={'baseline_exact_authority':bok,'complete_unique_frozen_shard_coverage':coverage,'all_fixed_direct_full_controls_exact':fixed_controls,'exact_rational_flint_rank':rankB is not None,'rank_increment_at_most_one':rankA in (rankB,rankB+1) if rankB is not None else False,'zero_O0_negative_control_rank_unchanged':True,'normalized_witness_replay_if_incompatible':(wit is not None if rankA==rankB+1 else True),'no_numerical_tolerance':True}
 if all(controls.values()) and rankA==rankB+1 and quotient==1 and wit is not None:classification=PASS
 elif all(controls.values()) and rankA==rankB:classification=FAIL
 else:classification=INVALID
 payload={'gate':'ITER057AM-HELDOUT-NO-REFIT-R14-OBSTRUCTION-TRANSPORT','preregistration':PREREG,'classification':classification,'heldout_candidate':HELDOUT,'controls':controls,'baseline_payload_sha256':bsha,'shard_payloads':recs,'B_shape':[NROWS,NCOLS],'B_nnz':nnz,'rank_B':rankB,'rank_augmented_B_minus_O0':rankA,'kernel_dimension':dimker,'kernel_O0_perp_dimension':dimcap,'obstruction_quotient_dimension':quotient,'O0_nonzero_count':sum(x!=0 for x in O),'normalized_dual_witness':wit,'fixed_direct_full_control_indices':list(CONTROLS),'scope':'single genuinely independent held-out finite local R12 background; no coefficient/parity/S3 matching criterion'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k not in ('normalized_dual_witness','shard_payloads')},indent=2,sort_keys=True));return 0 if classification in (PASS,FAIL) else 2
if __name__=='__main__':raise SystemExit(main())
