#!/usr/bin/env python3
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq,fmpq_mat
PREREG='b40e9949932c9698a08a099bde8cfb920eb5feff';CAND='AL-R1-3';NROWS=1456;NCOLS=1114
RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973),(973,1114)];CTR=(0,557,1113)
PASS='PASS_SCOPED_ITER057AN_SECOND_INDEPENDENT_BACKGROUND_REPRODUCES_ONE_DIMENSIONAL_R14_OBSTRUCTION_CLASS'
FAIL='SCIENTIFIC_FAIL_ITER057AN_VALID_SECOND_BACKGROUND_HAS_NO_R14_OBSTRUCTION_AFTER_COMPLETE_R12_FREEDOM'
INVALID='INVALID_ITER057AN_NO_REFIT_AUTHORITY_OR_EXACTNESS_CONTROL_FAILURE'
def ph(d):
 q=dict(d);g=q.pop('scientific_payload_sha256',None);c=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return g,g==c
def one(root,mode):
 out=[]
 for f in Path(root).rglob('*.json'):
  try:d=json.loads(f.read_text())
  except:continue
  if d.get('preregistration')==PREREG and d.get('mode')==mode:out.append((f,d))
 return out
def base(root):
 xs=one(root,'baseline');
 if len(xs)!=1:raise RuntimeError('baseline count')
 _,d=xs[0];h,ok=ph(d);ctrl=d.get('controls',{});ok=ok and d.get('candidate')==CAND and d.get('kernel_dimension')==1114 and d.get('M14_shape')==[6790,6800] and d.get('L14_shape')==[1456,6790] and all(ctrl.values())
 O=[F(0)]*NROWS
 for i,v in d.get('O0_nonzero',[]):O[int(i)]=F(v)
 return O,h,bool(ok),d
def shards(root):
 cols={};recs=[];cov=[];dup=[];seen={i:False for i in CTR};good={i:False for i in CTR}
 for f,d in one(root,'shard'):
  h,ok=ph(d);lane=tuple(d.get('lane',[]));ok=ok and d.get('candidate')==CAND and lane in RANGES and d.get('column_count')==lane[1]-lane[0] and d.get('kernel_exact_annihilation') is True and d.get('direct_full_control_mismatch_count')==0
  loc=set()
  for r in d.get('columns',[]):
   j=int(r['index']); vals={};last=-1
   if not(lane[0]<=j<lane[1]) or j in loc:ok=False;break
   loc.add(j)
   for i,s in r.get('nonzero',[]):
    i=int(i);v=F(s)
    if i<=last or not(0<=i<NROWS) or not v:ok=False;break
    last=i;vals[i]=v
   else:
    if j in cols:dup.append(j)
    cols[j]=vals
    if j in seen:seen[j]=True;good[j]=(r.get('direct_full_control_exact') is True)
    continue
   break
  ok=ok and loc==set(range(*lane));recs.append({'file':f.name,'lane':list(lane),'payload_sha256':h,'ok':bool(ok)});cov.append(lane)
 return cols,recs,cov,dup,seen,good
def fq(x):x=F(x);return fmpq(x.numerator,x.denominator)
def witness(B,O):
 T=B.transpose();R,rank=T.rref();rank=int(rank);piv=[]
 for r in range(rank):
  for c in range(NROWS):
   if R[r,c]!=0:piv.append(c);break
 free=[c for c in range(NROWS) if c not in set(piv)]
 for f in free:
  y=[fmpq(0)]*NROWS;y[f]=1
  for rr,p in enumerate(piv):
   if R[rr,f]!=0:y[p]=-R[rr,f]
  q=fmpq(0)
  for i,x in enumerate(O):
   if x and y[i]:q+=fq(x)*y[i]
  if q:
   y=[v/q for v in y];Y=fmpq_mat(NROWS,1)
   for i,v in enumerate(y):Y[i,0]=v
   if any((T*Y)[i,0]!=0 for i in range(T.nrows())):raise RuntimeError('witness replay')
   return {'nonzero':[[i,str(v)] for i,v in enumerate(y) if v],'BT_y_nonzero_count':0,'O0T_y':'1'}
 return None
def main():
 a=argparse.ArgumentParser();a.add_argument('--input-root',required=True);a.add_argument('--output',required=True);x=a.parse_args();O,bsha,bok,bd=base(x.input_root);cols,recs,cov,dup,seen,good=shards(x.input_root)
 cover=sorted(cov)==sorted(RANGES) and not dup and set(cols)==set(range(NCOLS)) and len(recs)==8 and all(r['ok'] for r in recs);ctrl=all(seen.values()) and all(good.values())
 rb=ra=nnz=None;wit=None
 if bok and cover and ctrl:
  B=fmpq_mat(NROWS,NCOLS);A=fmpq_mat(NROWS,NCOLS+1);nnz=0
  for j in range(NCOLS):
   for i,v in cols[j].items():B[i,j]=fq(v);A[i,j]=fq(v);nnz+=1
  for i,v in enumerate(O):
   if v:A[i,NCOLS]=-fq(v)
  rb=int(B.rank());ra=int(A.rank());wit=witness(B,O) if ra==rb+1 else None
 dk=NROWS-rb if rb is not None else None;dc=(dk-1 if ra==rb+1 else dk) if dk is not None else None;q=(dk-dc) if dk is not None else None
 controls={'baseline_exact':bok,'complete_unique_coverage':cover,'fixed_direct_full_controls_exact':ctrl,'exact_rational_flint_rank':rb is not None,'rank_increment_at_most_one':ra in (rb,rb+1) if rb is not None else False,'normalized_witness_replay':wit is not None if ra==rb+1 else True,'no_numerical_tolerance':True}
 cls=PASS if all(controls.values()) and ra==rb+1 and q==1 and wit else FAIL if all(controls.values()) and ra==rb else INVALID
 p={'gate':'ITER057AN-SECOND-INDEPENDENT-BACKGROUND-R14-REPLICATION','preregistration':PREREG,'classification':cls,'candidate':CAND,'controls':controls,'baseline_payload_sha256':bsha,'shard_payloads':recs,'B_shape':[NROWS,NCOLS],'B_nnz':nnz,'rank_B':rb,'rank_augmented_B_minus_O0':ra,'kernel_dimension':dk,'kernel_O0_perp_dimension':dc,'obstruction_quotient_dimension':q,'O0_nonzero_count':sum(v!=0 for v in O),'normalized_dual_witness':wit,'fixed_control_indices':list(CTR),'scope':'second independent additional finite-local R12 background; no coefficient/parity/S3 matching criterion'}
 raw=json.dumps(p,sort_keys=True,separators=(',',':')).encode();p['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();Path(x.output).parent.mkdir(parents=True,exist_ok=True);Path(x.output).write_text(json.dumps(p,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in p.items() if k not in ('normalized_dual_witness','shard_payloads')},indent=2,sort_keys=True));return 0 if cls in (PASS,FAIL) else 2
if __name__=='__main__':raise SystemExit(main())