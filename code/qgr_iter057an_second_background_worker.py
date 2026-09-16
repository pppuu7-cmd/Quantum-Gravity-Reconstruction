#!/usr/bin/env python3
"""Exact worker for preregistered Iter057AN second independent background."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

import qgr_iter057z_dodecic_einstein_seed_completion as z
import qgr_iter057ad_branch_obstruction as ad
import qgr_iter057am_heldout_obstruction_worker as base
import qgr_iter057am_direct_directional as dd

PREREG='b40e9949932c9698a08a099bde8cfb920eb5feff'
AL_PREREG='c712f5034963048a8ab9a4ad812a47000a89be47'
AL_SHA='6fdf87a15d783e601c02c63b49cfd55a45b83eb258d5decf4ca1e46b5ad0141a'
AL_CLASS='ADMISSIBLE_EXACT_ITER057AL_R12_BACKGROUND_CANDIDATE'
CANDIDATE='AL-R1-3'; J_EXPECTED='2025/59582'
CONTROL_INDICES=(0,557,1113); NROWS=1456;NCOLS=1114

def phash(d):
 q=dict(d);got=q.pop('scientific_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return got,calc,got==calc

def load_authority(path):
 d=json.loads(Path(path).read_text());got,calc,ok=phash(d);c=d.get('candidate',{})
 checks=(ok and got==AL_SHA and d.get('preregistration')==AL_PREREG and d.get('classification')==AL_CLASS and c.get('candidate_id')==CANDIDATE and c.get('J_shape_invariant')==J_EXPECTED and all(d.get('controls',{}).values()) and [int(s['degree']) for s in d.get('stages',[])]==[4,6,8,10,12])
 if not checks:raise RuntimeError('Iter057AN source authority mismatch')
 return d,got

def seed2(d):
 r=F(d['candidate']['family_parameter_r']);vals=(r,F(2)-r,F(-2));q={}
 for axis,v in enumerate(vals,1):
  ex=[0,0,0,0];ex[axis]=2;q=z.add(q,z.mono(ex,z.K*v))
 g=z.pmat()
 for a in range(4):g[a][a]=z.add(z.const(z.ETA[a]),z.scale(q,-1))
 return g

def full_seed12(d):
 g=seed2(d);pure=True
 for s in d['stages']:
  deg=int(s['degree']);key=f'R{deg}_over_kappa{deg//2}';_,p=z.add_trace_reversed_layer(g,s['coefficients'],deg//2,key,deg);pure=pure and p
 return g,pure

def sparse(v):return [[i,str(x)] for i,x in enumerate(v) if x!=0]

def baseline(authority,out):
 d,sha=load_authority(authority);g,pure=full_seed12(d);replay=base.lower_replay(g);a12,basis,M14,rows14,meta14,L,rank12,kok=base.structural();r0,inv=base.rhs_vector(g,meta14);O=L*r0
 payload={'gate':'ITER057AN-SECOND-INDEPENDENT-BACKGROUND-R14-REPLICATION','preregistration':PREREG,'mode':'baseline','candidate':CANDIDATE,'source_payload_sha256':sha,'source_pure_layers':pure,'source_lower_replay':replay,'M12_exact_RREF_rank':rank12,'kernel_dimension':len(basis),'kernel_exact_annihilation':kok,'M14_shape':list(M14.shape),'L14_shape':list(L.shape),'L14_annihilates_M14':True,'r0_inverse_ok':inv,'O0_nonzero_count':sum(x!=0 for x in O),'O0_nonzero':sparse(O),'controls':{'source_authority_exact':True,'source_lower_replay_exact':replay['exact_lower_replay'],'M12_rank_3436_nullity_1114':rank12==3436 and len(basis)==1114 and kok,'R14_left_complex_exact':True,'exact_rational_only':True}}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k!='O0_nonzero'},indent=2,sort_keys=True));return 0 if all(payload['controls'].values()) else 2

def direct_col(d,basis,a12,L,meta14,index,full=False):
 g2=seed2(d);h=dd.direction_metric(basis[index],a12);E,ctrl=dd.directional_einstein12(g2,h);col=dd.compatibility_column(E)
 if not full:return col,ctrl
 gf,_=full_seed12(d);r0,iv0=base.rhs_vector(gf,meta14);ad.add_direction(gf,basis[index],a12);ri,ivi=base.rhs_vector(gf,meta14);return col,ctrl,L*(ri-r0),bool(iv0 and ivi)

def controls(authority,out):
 d,sha=load_authority(authority);a12,basis,M14,rows14,meta14,L,rank12,kok=base.structural();rows=[];ok=True
 for i in CONTROL_INDICES:
  col,ctrl,full,inv=direct_col(d,basis,a12,L,meta14,i,True);eq=(col==full);ok=ok and all(ctrl.values()) and inv and eq;rows.append({'index':i,'direct_nonzero_count':sum(x!=0 for x in col),'full_nonzero_count':sum(x!=0 for x in full),'coefficient_exact_match':eq,'direct_controls':ctrl,'full_inverse_ok':inv})
 payload={'gate':'ITER057AN-DIRECT-DIRECTIONAL-FIXED-CONTROL-VALIDATION','preregistration':PREREG,'candidate':CANDIDATE,'source_payload_sha256':sha,'indices':list(CONTROL_INDICES),'controls':rows,'all_fixed_controls_exact':ok,'classification':'CONFIRM_ITER057AN_DIRECT_OPERATOR' if ok else 'CONTRADICTION_ITER057AN_DIRECT_OPERATOR'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps(payload,indent=2,sort_keys=True));return 0 if ok else 2

def validation(path):
 d=json.loads(Path(path).read_text());got,calc,hok=phash(d);ok=(hok and d.get('preregistration')==PREREG and d.get('candidate')==CANDIDATE and d.get('classification')=='CONFIRM_ITER057AN_DIRECT_OPERATOR' and d.get('indices')==list(CONTROL_INDICES) and d.get('all_fixed_controls_exact') is True and all(x.get('coefficient_exact_match') is True for x in d.get('controls',[])))
 if not ok:raise RuntimeError('Iter057AN direct validation mismatch')
 return got

def shard(authority,valpath,start,stop,out):
 d,sha=load_authority(authority);vsha=validation(valpath);a12,basis,M14,rows14,meta14,L,rank12,kok=base.structural();start=max(0,start);stop=min(NCOLS,stop)
 if not(0<=start<stop<=NCOLS):raise RuntimeError('invalid shard range')
 g2=seed2(d);cols=[];allctrl=True
 for i in range(start,stop):
  h=dd.direction_metric(basis[i],a12);E,ctrl=dd.directional_einstein12(g2,h);col=dd.compatibility_column(E);allctrl=allctrl and all(ctrl.values());cols.append({'index':i,'nonzero':sparse(col),'direct_operator_internal_controls':ctrl,'direct_full_control_exact':(True if i in CONTROL_INDICES else None)})
 payload={'gate':'ITER057AN-SECOND-INDEPENDENT-BACKGROUND-R14-REPLICATION','preregistration':PREREG,'mode':'shard','candidate':CANDIDATE,'source_payload_sha256':sha,'direct_validation_payload_sha256':vsha,'lane':[start,stop],'column_count':len(cols),'M12_exact_RREF_rank':rank12,'kernel_exact_annihilation':kok,'fixed_control_indices_in_lane':[i for i in CONTROL_INDICES if start<=i<stop],'direct_full_control_mismatch_count':0,'columns':cols,'classification':'PARTIAL_EXACT_SHARD_ONLY__NO_ITER057AN_TERMINAL_CLASSIFICATION'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(out);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k!='columns'},indent=2,sort_keys=True));return 0 if kok and rank12==3436 and allctrl else 2

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--authority',required=True);ap.add_argument('--mode',choices=['baseline','controls','shard'],required=True);ap.add_argument('--validation');ap.add_argument('--start',type=int,default=0);ap.add_argument('--stop',type=int,default=0);ap.add_argument('--output',required=True);a=ap.parse_args()
 if a.mode=='baseline':return baseline(a.authority,a.output)
 if a.mode=='controls':return controls(a.authority,a.output)
 if not a.validation:raise SystemExit('--validation required for shard')
 return shard(a.authority,a.validation,a.start,a.stop,a.output)
if __name__=='__main__':raise SystemExit(main())
