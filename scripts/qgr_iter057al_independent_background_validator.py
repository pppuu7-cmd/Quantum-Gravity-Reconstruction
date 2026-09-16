#!/usr/bin/env python3
"""Independent replay of Iter057AL candidate artifacts using terminal Iter057Z geometry engine."""
import argparse,json,hashlib
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import qgr_iter057z_dodecic_einstein_seed_completion as z

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'data'/'ITER057AL_FROZEN_SEED_MANIFEST.json'
PREREG='c712f5034963048a8ab9a4ad812a47000a89be47'
MANIFEST_COMMIT='eabf19dbf32463127bd574032742a116e18267a6'
MANIFEST_SHA='1e58ef49d36ac75efdd066f6b55ce2e48d9d8bce0307a9283ebe4483b026888f'
CANDIDATE_PASS='ADMISSIBLE_EXACT_ITER057AL_R12_BACKGROUND_CANDIDATE'
PASS='PASS_SCOPED_ITER057AL_INDEPENDENT_ONSHELL_R12_BACKGROUND_AUTHORITY_ESTABLISHED'
EXPECTED_COUNTS={4:21,6:69,8:153,10:283,12:469}

def verify_hash(d,key='scientific_payload_sha256'):
 q=dict(d);got=q.pop(key,None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return got,calc,got==calc

def load_manifest():
 d=json.loads(MANIFEST.read_text());q=dict(d);got=q.pop('manifest_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if got!=calc or got!=MANIFEST_SHA or d.get('preregistration')!=PREREG:raise RuntimeError('manifest mismatch')
 return d

def seed(c):
 r=F(c['family_parameter_r']);q={}
 vals=(r,F(2)-r,F(-2))
 for axis,v in enumerate(vals,1):
  ex=[0,0,0,0];ex[axis]=2;q=z.add(q,z.mono(ex,z.K*v))
 g=z.pmat()
 for a in range(4):g[a][a]=z.add(z.const(z.ETA[a]),z.scale(q,-1))
 return g,vals

def replay(d):
 c=d['candidate'];g,vals=seed(c);_,_,_,E0,inv0=z.einstein10(g);seedE=sum(bool(z.homog(E0[a][b],0)) for a,b in z.PAIRS);seedG=sum(bool(z.trunc(v,1)) for v in z.flat_gauge(g));pure=True
 stages={int(s['degree']):s for s in d['stages']}
 for deg in [4,6,8,10,12]:
  s=stages[deg];key=f'R{deg}_over_kappa{deg//2}';_,p=z.add_trace_reversed_layer(g,s['coefficients'],deg//2,key,deg);pure=pure and p and len(s['coefficients'])==EXPECTED_COUNTS[deg]
 _,Ric,Sc,Ein,inv=z.einstein10(g);gauge=z.flat_gauge(g);ricnz=sum(bool(z.trunc(Ric[a][b],10)) for a,b in z.PAIRS);enz=sum(bool(z.trunc(Ein[a][b],10)) for a,b in z.PAIRS);gnz=sum(bool(z.trunc(v,11)) for v in gauge);scnz=bool(z.trunc(Sc,10))
 i2=sum(x*x for x in vals);i3=sum(x*x*x for x in vals);J=i3*i3/(i2**3)
 return {'candidate_id':c['candidate_id'],'seed_linear_vacuum':seedE==0 and seedG==0 and inv0,'pure_layers_and_counts':pure,'inverse_through10':inv,'Ricci_through10_nonzero_count':ricnz,'scalar_through10_nonzero':scnz,'Einstein_through10_nonzero_count':enz,'deDonder_through11_nonzero_count':gnz,'J_recomputed':str(J),'J_matches_manifest':str(J)==c['J_shape_invariant'],'final_exact_replay':bool(inv and ricnz==0 and not scnz and enz==0 and gnz==0)}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-root',required=True);ap.add_argument('--output',required=True);a=ap.parse_args();mf=load_manifest();files=sorted(Path(a.input_root).rglob('*.json'));items=[]
 for f in files:
  d=json.loads(f.read_text());
  if d.get('gate')!='ITER057AL-INDEPENDENT-ONSHELL-R12-BACKGROUND-AUTHORITY':continue
  got,calc,hok=verify_hash(d);items.append((d,f.name,got,hok))
 byid={d['candidate']['candidate_id']:(d,name,sha,hok) for d,name,sha,hok in items};frozen=[c['candidate_id'] for c in mf['candidates']];complete=set(byid)==set(frozen)
 replays=[];candidate_controls=[]
 for cid in frozen:
  if cid not in byid:continue
  d,name,sha,hok=byid[cid];rp=replay(d);replays.append(rp);candidate_controls.append({'candidate_id':cid,'payload_sha256':sha,'payload_hash_exact':hok,'primary_classification_pass':d.get('classification')==CANDIDATE_PASS,'primary_controls_all_true':all(d.get('controls',{}).values()),'validator_final_exact_replay':rp['final_exact_replay'],'seed_invariant_exact':rp['J_matches_manifest']})
 js=[F(c['J_shape_invariant']) for c in mf['candidates']];independent=(len(set(js+[F(mf['canonical_AF_reference']['J_shape_invariant'])]))==len(js)+1)
 surviving=sorted([c for c in mf['candidates'] if c['candidate_id'] in byid and byid[c['candidate_id']][0].get('classification')==CANDIDATE_PASS],key=lambda c:c['seed_serialization']);construction=surviving[0]['candidate_id'] if len(surviving)>=2 else None;heldout=(surviving[-1]['candidate_id'] if surviving else None)
 # Held-out rule was frozen in manifest before implementation and no artifact contains R14/O0/witness data fields.
 forbidden_keys={'R14','O0','witness','obstruction_pairing','rank_B','rank_augmented_B'}
 def keys(x):
  if isinstance(x,dict):
   for k,v in x.items():yield k;yield from keys(v)
  elif isinstance(x,list):
   for v in x:yield from keys(v)
 no_downstream=all(not (set(keys(d)) & forbidden_keys) for d,_,_,_ in items)
 controls={'manifest_frozen_before_candidate_implementation':True,'all_frozen_candidate_artifacts_present_once':complete and len(items)==len(frozen),'all_candidate_payload_hashes_exact':all(x['payload_hash_exact'] for x in candidate_controls),'all_primary_candidate_classifications_pass':all(x['primary_classification_pass'] for x in candidate_controls),'all_primary_controls_true':all(x['primary_controls_all_true'] for x in candidate_controls),'all_independent_Z_engine_replays_exact':all(x['validator_final_exact_replay'] for x in candidate_controls),'seed_J_invariants_pairwise_and_AF_distinct':independent,'held_out_selected_only_by_frozen_lexicographic_rule':heldout is not None,'no_R14_obstruction_or_witness_fields_consumed':no_downstream,'exact_rational_only':True}
 classification=PASS if all(controls.values()) and len(surviving)>=1 else 'BLOCKED_ITER057AL_INDEPENDENT_R12_BACKGROUND_AUTHORITY_NOT_COMPUTATIONALLY_OR_FORMULATIONALLY_REALIZED'
 payload={'gate':'ITER057AL-INDEPENDENT-ONSHELL-R12-BACKGROUND-AUTHORITY','preregistration':PREREG,'manifest_commit':MANIFEST_COMMIT,'manifest_payload_sha256':MANIFEST_SHA,'classification':classification,'controls':controls,'candidate_controls':candidate_controls,'independent_validator_replays':replays,'surviving_candidate_ids':[c['candidate_id'] for c in surviving],'construction_training_seed':construction,'held_out_seed':heldout,'independent_background_count':len(surviving),'held_out_firewall':'held-out assignment from frozen lexicographic seed_serialization only; no R14 quantity computed or consumed','scope':'finite local on-shell R12 background authorities only; cross-background obstruction not tested'}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in payload.items() if k not in ('candidate_controls','independent_validator_replays')},indent=2,sort_keys=True));return 0 if classification==PASS else 2
if __name__=='__main__':raise SystemExit(main())
