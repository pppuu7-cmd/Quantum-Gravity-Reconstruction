#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json
from fractions import Fraction
from pathlib import Path

GATE='ITER057BG_ITER057AT_CORRECTED_DEGREE6_DURABLE_INPUT_MATERIALIZATION'
PREREG='180be23933c9cc4f78dbf8e1fea6cb76b9c74fc8'
EXPECTED_FILE_SHA='1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b'
EXPECTED_VECTOR_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'
EXPECTED_META={
 'gate':'ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE',
 'preregistration':'6039cb2ed1380b549bced3d33634362ef57345d4',
 'production_head':'c4e7ccc05ea1b8f4967379fc370812dfa99cce03',
 'actions_run':'35198813733','primary_artifact':'10486378527',
 'primary_artifact_digest':'sha256:7e923b6b3124d3bd8a95488a8c7b184ce86bb683a0076a8fb26098424ac838e7',
 'independent_artifact':'10486998588','independent_artifact_digest':'sha256:29a01128e1561c42fa15e06989c1967089d40bd9d960935215a412c1ce226f2f',
 'terminal_artifact':'10486973737','terminal_artifact_digest':'sha256:bdb5affc949803e692d3680864746daa0c4175324d85e1ce7426d1b719621bb6',
 'ordered_840_vector_sha256':EXPECTED_VECTOR_SHA,'slot_count':'840','nonzero_count':'140','c6':'SYMBOLIC_UNFIXED_FACTORED_OUT'}

def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def J(x)->bytes:return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def canon_fraction(s:str)->str:
    f=Fraction(s);return str(f.numerator) if f.denominator==1 else f'{f.numerator}/{f.denominator}'
def read_candidate(path:Path):
    raw=path.read_bytes();lines=raw.decode('utf-8','strict').splitlines();meta={};body=[]
    for line in lines:
        if line.startswith('# '):
            k,v=line[2:].split('=',1);meta[k]=v
        elif line.strip():body.append(line)
    rows=[]
    for r in csv.DictReader(body):
        rows.append({'pair':[int(r['a']),int(r['b'])],'alpha':[int(r['t']),int(r['x']),int(r['y']),int(r['z'])],'value':r['value']})
    return raw,meta,rows
def build(candidate:Path,lane_path:Path,mode:str):
    raw,meta,rows=read_candidate(candidate);lane=json.loads(lane_path.read_text(encoding='utf-8'));fresh=lane.get('degree6_vector',[])
    sparse={};duplicate=False
    for r in rows:
        key=tuple(r['pair']+r['alpha'])
        if key in sparse:duplicate=True
        sparse[key]=r['value']
    reconstructed=[]
    for item in fresh:
        key=tuple(item['pair']+item['alpha']);reconstructed.append({'pair':item['pair'],'alpha':item['alpha'],'value':sparse.get(key,'0')})
    controls={
      'candidate_file_sha_exact':H(raw)==EXPECTED_FILE_SHA,
      'candidate_metadata_exact':all(meta.get(k)==v for k,v in EXPECTED_META.items()) and set(EXPECTED_META)<=set(meta),
      'row_count_140':len(rows)==140,
      'rows_unique':not duplicate and len(sparse)==140,
      'all_rows_total_degree_6':all(sum(r['alpha'])==6 for r in rows),
      'all_rows_nonzero_exact_canonical_rationals':all(r['value']!='0' and canon_fraction(r['value'])==r['value'] for r in rows),
      'fresh_gate_exact':lane.get('gate')=='ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE',
      'fresh_prereg_exact':lane.get('preregistration_commit')=='6039cb2ed1380b549bced3d33634362ef57345d4',
      'fresh_mode_exact':lane.get('lane')==mode,
      'fresh_slot_count_840':lane.get('slot_count')==840 and len(fresh)==840,
      'fresh_constructor_controls_all_true':bool(lane.get('controls')) and all(v is True for v in lane['controls'].values()),
      'fresh_historical_target_not_loaded':lane.get('historical_target_loaded') is False,
      'fresh_c6_symbolic_unfixed':lane.get('c6')=='SYMBOLIC_UNFIXED_FACTORED_OUT',
      'fresh_vector_hash_exact':lane.get('degree6_vector_sha256')==EXPECTED_VECTOR_SHA and H(J(fresh))==EXPECTED_VECTOR_SHA,
      'sparse_reconstruction_slot_count_840':len(reconstructed)==840,
      'sparse_reconstruction_hash_exact':H(J(reconstructed))==EXPECTED_VECTOR_SHA,
      'sparse_reconstruction_bit_for_bit_equals_fresh':reconstructed==fresh,
      'descendant_science_consumed':False,'historical_target_substitution':False,'claim_lock_promoted':False}
    positive=all(v is True for k,v in controls.items() if k not in {'descendant_science_consumed','historical_target_substitution','claim_lock_promoted'})
    valid=positive and controls['descendant_science_consumed'] is False and controls['historical_target_substitution'] is False and controls['claim_lock_promoted'] is False
    return {'gate':GATE,'mode':mode,'preregistration_commit':PREREG,'candidate_path':str(candidate),'candidate_file_sha256':H(raw),'candidate_metadata':meta,'candidate_nonzero_count':len(rows),'fresh_vector_sha256':H(J(fresh)),'reconstructed_vector_sha256':H(J(reconstructed)),'fresh_vector':fresh,'controls':controls,'all_controls_pass':valid,'descendant_science_consumed':False,'theory_established_pct':0,'c6':'SYMBOLIC_UNFIXED'}
def main():
    p=argparse.ArgumentParser();p.add_argument('--candidate',type=Path,required=True);p.add_argument('--lane-result',type=Path,required=True);p.add_argument('--mode',choices=['primary','independent'],required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=build(a.candidate,a.lane_result,a.mode);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k!='fresh_vector'},sort_keys=True,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
