#!/usr/bin/env python3
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
PREREG='b40e9949932c9698a08a099bde8cfb920eb5feff';CAND='AL-R1-3';NROWS=1456;NCOLS=1114;PRIMES=[1000003,1000033,1000037]
RANGES=[(0,139),(139,278),(278,417),(417,556),(556,695),(695,834),(834,973),(973,1114)]
def ph(d):q=dict(d);g=q.pop('scientific_payload_sha256',None);c=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return g,g==c
def load(root):
 O=[F(0)]*NROWS;cols={};baseok=False;cov=[];dup=[];recs=[]
 for f in Path(root).rglob('*.json'):
  try:d=json.loads(f.read_text())
  except:continue
  if d.get('preregistration')!=PREREG:continue
  h,ok=ph(d)
  if d.get('mode')=='baseline':
   baseok=ok and d.get('candidate')==CAND and all(d.get('controls',{}).values())
   for i,v in d.get('O0_nonzero',[]):O[int(i)]=F(v)
  elif d.get('mode')=='shard':
   lane=tuple(d.get('lane',[]));ok=ok and d.get('candidate')==CAND and lane in RANGES and d.get('column_count')==lane[1]-lane[0]
   local=set()
   for r in d.get('columns',[]):
    j=int(r['index']);vals={}
    if j in local:ok=False;break
    local.add(j)
    for i,s in r.get('nonzero',[]):vals[int(i)]=F(s)
    if j in cols:dup.append(j)
    cols[j]=vals
   ok=ok and local==set(range(*lane));cov.append(lane);recs.append({'lane':list(lane),'payload_sha256':h,'ok':bool(ok)})
 cover=sorted(cov)==sorted(RANGES) and not dup and set(cols)==set(range(NCOLS)) and len(recs)==8 and all(r['ok'] for r in recs)
 return O,cols,baseok,cover,recs
def invmod(a,p):return pow(a,p-2,p)
def rank_mod(rows,ncols,p):
 piv=0;rows=[dict(r) for r in rows]
 for c in range(ncols):
  q=next((i for i in range(piv,len(rows)) if rows[i].get(c,0)%p),None)
  if q is None:continue
  rows[piv],rows[q]=rows[q],rows[piv];iv=invmod(rows[piv][c]%p,p);rows[piv]={j:(v*iv)%p for j,v in rows[piv].items() if v%p}
  for i in range(len(rows)):
   if i==piv:continue
   a=rows[i].get(c,0)%p
   if a:
    nr=dict(rows[i])
    for j,v in rows[piv].items():nr[j]=(nr.get(j,0)-a*v)%p
    rows[i]={j:v for j,v in nr.items() if v%p}
  piv+=1
  if piv==len(rows):break
 return piv
def build_rows(O,cols,p,aug=False):
 rows=[{} for _ in range(NROWS)]
 for j,d in cols.items():
  for i,v in d.items():
   if v.denominator%p==0:raise ZeroDivisionError
   rows[i][j]=(v.numerator%p)*invmod(v.denominator%p,p)%p
 if aug:
  for i,v in enumerate(O):
   if v:
    if v.denominator%p==0:raise ZeroDivisionError
    rows[i][NCOLS]=(-v.numerator%p)*invmod(v.denominator%p,p)%p
 return rows
def main():
 a=argparse.ArgumentParser();a.add_argument('--input-root',required=True);a.add_argument('--output',required=True);x=a.parse_args();O,cols,bok,cok,recs=load(x.input_root)
 chosen=None;rb=ra=None
 for p in PRIMES:
  try: rb=rank_mod(build_rows(O,cols,p,False),NCOLS,p);ra=rank_mod(build_rows(O,cols,p,True),NCOLS+1,p);chosen=p;break
  except ZeroDivisionError:continue
 controls={'baseline_exact':bok,'complete_unique_coverage':cok,'prime_selected_by_denominator_rule':chosen is not None,'modular_rank_B_full_column':rb==1114,'modular_rank_augmented_increment_one':ra==1115,'exact_finite_field_only':True,'no_numerical_tolerance':True}
 cls='CONFIRM_SCOPED_ITER057AN_MODULAR_EXACT_CRITIC' if all(controls.values()) else 'CONTRADICTION_ITER057AN_MODULAR_EXACT_CRITIC'
 out={'gate':'ITER057AN-INDEPENDENT-MODULAR-CRITIC','preregistration':PREREG,'candidate':CAND,'classification':cls,'controls':controls,'selected_prime':chosen,'rank_B_mod_p':rb,'rank_augmented_mod_p':ra,'rational_rank_lower_bound_certificate':{'rank_B_at_least':rb,'rank_augmented_at_least':ra},'O0_nonzero_count':sum(v!=0 for v in O),'shard_payloads':recs}
 raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();Path(x.output).parent.mkdir(parents=True,exist_ok=True);Path(x.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='shard_payloads'},indent=2,sort_keys=True));return 0 if cls.startswith('CONFIRM') else 2
if __name__=='__main__':raise SystemExit(main())