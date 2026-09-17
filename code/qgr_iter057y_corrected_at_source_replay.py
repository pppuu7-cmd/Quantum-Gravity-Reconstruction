#!/usr/bin/env python3
"""Prospectively frozen corrected Iter057Y exact replay with degree-six source = -AT."""
from __future__ import annotations
import argparse,hashlib,json,subprocess
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import qgr_iter057y_onshell_q2_q4_q6_q8_response as base

GATE='ITER057Y_CORRECTED_AT_SOURCE_Q2_Q4_Q6_Q8_REPLAY'
PREREG='a6466be9dd3b2ce47bba5be1cacbd184b2161c8f'
BJ_TERMINAL_COMMIT='eb1aafc711b78c5bf845448e7d4c0edb7bd1b0c2'
BJ_CLASS='PASS_SCOPED_ITER057BJ_Y_SOURCE_CONVENTION_MAP_MINUS_AT_INDEPENDENTLY_ESTABLISHED'
BJ_PAYLOAD='5941deed797bcdf017b4efdae60a66d1ab0c40e71b16425329b54fdb67bbebbd'
BASE_REF='98c82292885cec9a38fa400a5e08b1272104f8b8'
BASE_PATH='code/qgr_iter057y_onshell_q2_q4_q6_q8_response.py'
AT_PATH=base.ROOT/'data'/'ITER057AT_CANONICAL_SOURCE_DEGREE6.csv'
AT_FILE_SHA='1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b'
AT_VECTOR_SHA='5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b'
AT_PREREG='6039cb2ed1380b549bced3d33634362ef57345d4'
AT_PRODUCTION='c4e7ccc05ea1b8f4967379fc370812dfa99cce03'
PASS='PASS_SCOPED_ITER057Y_CORRECTED_AT_SOURCE_EXACT_Q8_RESPONSE_EXISTS'
FAIL='FAIL_SCIENTIFIC_SCOPED_ITER057Y_CORRECTED_AT_SOURCE_Q8_RESPONSE_INCOMPATIBLE'
INVALID='INVALID_IMPLEMENTATION_ITER057Y_CORRECTED_AT_SOURCE_REPLAY_CONTROL_FAILURE'

AUTH_DETAILS={}

def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()

def pinned_base_identity()->dict:
    current=(base.ROOT/BASE_PATH).read_bytes()
    p=subprocess.run(['git','-C',str(base.ROOT),'show',f'{BASE_REF}:{BASE_PATH}'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    return {
      'git_show_exit_zero':p.returncode==0,
      'current_equals_pinned':p.returncode==0 and current==p.stdout,
      'current_sha256':H(current),
      'pinned_sha256':H(p.stdout) if p.returncode==0 else None,
    }

def corrected_consume_authorities():
    global AUTH_DETAILS
    S=json.loads(base.S_PATH.read_text());V=json.loads(base.V_PATH.read_text());U=json.loads(base.U_PATH.read_text());atrows,atmeta=base.read_csv_authority(AT_PATH,'value')
    s_ok=(S.get('terminal_commit')==base.ITER057S and S.get('source_digest')==base.S_DIGEST and len(S.get('Q4_particular_normalized',[]))==34)
    v_ok=(V.get('terminal_commit')==base.ITER057V and V.get('source_digest')==base.V_DIGEST and len(V.get('Q6_particular_normalized',[]))==88 and V.get('rank_M')==494 and V.get('rank_augmented')==494)
    urows=U.get('Shat_normalized_sparse',[])
    u_ok=(U.get('terminal_commit')==base.ITER057U and U.get('source_digest')==base.U_DIGEST and len([r for r in urows if r['degree']==4])==64)
    at_raw=AT_PATH.read_bytes()
    at_ok=(H(at_raw)==AT_FILE_SHA and len(atrows)==140 and len({tuple(r['pair']+r['alpha']) for r in atrows})==140 and all(sum(r['alpha'])==6 for r in atrows) and atmeta.get('preregistration')==AT_PREREG and atmeta.get('production_head')==AT_PRODUCTION)
    q=base.pmat()
    for key,val in S['Q2_normalized'].items():
        a,b,c,d=(int(ch) for ch in key);e=[0,0,0,0];e[c]+=1;e[d]+=1;q[a][b]=base.add(q[a][b],base.mono(tuple(e),F(val)/2))
    for item in S['Q4_particular_normalized']:
        a,b=item['pair'];al=tuple(item['alpha']);t=base.mono(al,F(item['value'])/F(base.fact(al)));q[a][b]=base.add(q[a][b],t)
        if a!=b:q[b][a]=base.add(q[b][a],t)
    for item in V['Q6_particular_normalized']:
        a,b=item['pair'];al=tuple(item['alpha']);t=base.mono(al,F(item['value'])/F(base.fact(al)));q[a][b]=base.add(q[a][b],t)
        if a!=b:q[b][a]=base.add(q[b][a],t)
    for a,b in product(range(base.N),repeat=2):q[a][b]=base.trunc(q[a][b],6)
    source=base.pmat()
    for item in urows:
        a,b=item['pair'];al=tuple(item['alpha']);t=base.mono(al,F(item['value'])/F(base.fact(al)));source[a][b]=base.add(source[a][b],t)
        if a!=b:source[b][a]=base.add(source[b][a],t)
    # Frozen Iter057BJ MAP_MINUS convention: the corrected degree-six source loaded into
    # the historical Iter057Y equation DG-source=0 is exactly -AT.
    for item in atrows:
        a,b=item['pair'];al=tuple(item['alpha']);t=base.mono(al,-F(item['value'])/F(base.fact(al)));source[a][b]=base.add(source[a][b],t)
        if a!=b:source[b][a]=base.add(source[b][a],t)
    for a,b in product(range(base.N),repeat=2):source[a][b]=base.trunc(source[a][b],6)
    AUTH_DETAILS={'S':s_ok,'V':v_ok,'U':u_ok,'AT':at_ok,'at_file_sha256':H(at_raw),'at_metadata':atmeta,'at_nonzero_rows':len(atrows)}
    # Historical engine expects key X only as a boolean degree-six authority control.
    return q,source,(s_ok and v_ok and u_ok and at_ok),{'S':s_ok,'V':v_ok,'U':u_ok,'X':at_ok}

def compute():
    ident=pinned_base_identity()
    if not ident['current_equals_pinned']:
        return {'gate':GATE,'preregistration_commit':PREREG,'classification':INVALID,'pass':False,'reason':'pinned historical Iter057Y evaluator byte identity failed','base_identity':ident,'source_convention':'MAP_MINUS','degree6_source_expression':'-AT','c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT','theory_established_pct':0}
    old=(base.consume_authorities,base.GATE,base.PREREG,base.PASS,base.FAIL,base.INVALID)
    try:
        base.consume_authorities=corrected_consume_authorities
        base.GATE=GATE;base.PREREG=PREREG;base.PASS=PASS;base.FAIL=FAIL;base.INVALID=INVALID
        out=base.compute()
    finally:
        base.consume_authorities,base.GATE,base.PREREG,base.PASS,base.FAIL,base.INVALID=old
    controls=dict(out.get('controls',{}))
    legacy=controls.pop('B_iter057X_source_through_degree6_exact',None)
    controls['A_pinned_historical_Y_evaluator_byte_exact']=ident['current_equals_pinned']
    controls['B_corrected_AT_source_through_degree6_exact']=legacy is True and AUTH_DETAILS.get('AT') is True
    controls['B_source_convention_frozen_MAP_MINUS']=True
    controls['B_AT_file_sha_exact']=AUTH_DETAILS.get('at_file_sha256')==AT_FILE_SHA
    controls['B_AT_140_unique_degree6_rows']=AUTH_DETAILS.get('at_nonzero_rows')==140
    integrity=all(v is True for k,v in controls.items() if k.startswith(('A_','B_','C_','D_','E_','K_')))
    if not integrity:
        out['classification']=INVALID;out['pass']=False
    auth=dict(out.get('authority_subcontrols',{}));auth.pop('X',None);auth['AT']=AUTH_DETAILS.get('AT') is True
    out['controls']=controls;out['authority_subcontrols']=auth
    out.pop('iter057X_commit',None)
    out.update({
      'gate':GATE,'preregistration_commit':PREREG,'BJ_terminal_commit':BJ_TERMINAL_COMMIT,'BJ_terminal_classification':BJ_CLASS,'BJ_terminal_payload_sha256':BJ_PAYLOAD,
      'source_convention':'MAP_MINUS','degree6_source_expression':'-AT','AT_file_sha256':AT_FILE_SHA,'AT_ordered_840_vector_sha256':AT_VECTOR_SHA,
      'base_evaluator_ref':BASE_REF,'base_evaluator_identity':ident,'c6_status':'SYMBOLIC_UNFIXED_FACTORED_OUT','theory_established_pct':0,
    })
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args();out=compute();p=Path(args.out);p.parent.mkdir(parents=True,exist_ok=True);txt=json.dumps(out,indent=2,sort_keys=True)+'\n';p.write_text(txt);print(txt,end='')
    return 0

if __name__=='__main__':raise SystemExit(main())
