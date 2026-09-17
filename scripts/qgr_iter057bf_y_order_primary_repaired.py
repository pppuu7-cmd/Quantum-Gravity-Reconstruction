#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, hashlib, io, json, subprocess, tokenize
from pathlib import Path

GATE='ITER057BF_ITER057Y_REPLAY_ORDER_LITERAL_EXTRACTION_REPAIR'
PREREG='f80032eb7f346d57205e858cd2a55be1eeb42649'
CENSUS='616859890df95057556d265612c53da839a5848a'
BD_RESULT_COMMIT='c1e5be8e0da856d0960dce20cdb48f207b572869'
SCIENCE_COMMIT='cb2758238daba9ecf9c86e01e171f6c6d31c72b9'
SCIENCE_IMPL_COMMIT='98c82292885cec9a38fa400a5e08b1272104f8b8'
WRAPPER_COMMIT='8d5936b988c57d44e8a279b9d5fd4f6238a071e4'
AUDIT_COMMIT='ddcb7f9dde1ec8d197db7c6e074f0a1d03911b3e'
SCIENCE_RECORD='results/ITER057Y_ONSHELL_FIRST_ORDER_Q2_Q4_Q6_Q8_RESPONSE_TERMINAL.md'
AUDIT_RECORD='results/ITER057Y_ACTIONS_PROVENANCE_AUDIT.md'
WRAPPER_PATH='code/qgr_iter057y_actions_reproduction_fixed.py'
SCIENCE_IMPL_PATH='code/qgr_iter057y_onshell_q2_q4_q6_q8_response.py'
BD_RESULT_PATH='results/ITER057BD_STRICT_EARLIER_ONLY_DESCENDANT_DEPENDENCY_ADJUDICATION_TERMINAL.md'
EXPECTED_EVIDENCE={
 'audit_record':'86e1647b9febc40395b09c380e9d188b9e0b79bdd15e44ef5eb946e6c15c2680',
 'science_record':'0f88c01bd1abe9bf4e37bff781c1dd68451c1eb7d761ce4af886291c8b2aa603',
 'wrapper_source':'274aa62fd110f5a94cdfeb1968dc69c5322b1d774520575f61675423b7f5edef',
 'science_implementation':'486e8db9855f1b387c1dfb1b9d4b21178a4463019bf32ca47b3cbd7d5f5889bb',
 'bd_result':'1d673d1ef7b18398b347bd436883fdb87e31babf5521e4650ce18f41dca8cf25'}


def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def git(repo:Path,*args:str)->bytes:
    p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if p.returncode:raise RuntimeError(f"git {' '.join(args)} rc={p.returncode} stderr_sha256={H(p.stderr)}")
    return p.stdout
def show(repo:Path,ref:str,path:str)->bytes:return git(repo,'show',f'{ref}:{path}')
def text(raw:bytes)->str:return raw.decode('utf-8','strict')
def epoch(repo:Path,commit:str)->int:return int(text(git(repo,'show','-s','--format=%ct',commit)).strip())

def semantic_supplemental_note(source:str)->tuple[str|None,list[str]]:
    toks=list(tokenize.generate_tokens(io.StringIO(source).readline))
    start=None
    for i,tok in enumerate(toks):
        if tok.type!=tokenize.STRING:continue
        try:value=ast.literal_eval(tok.string)
        except Exception:continue
        if value!='supplemental_reproduction_note':continue
        # Require the concrete source form obj['supplemental_reproduction_note'] = ...
        prev=[x for x in toks[max(0,i-3):i] if x.type not in (tokenize.NL,tokenize.INDENT,tokenize.DEDENT)]
        nxt=[x for x in toks[i+1:i+5] if x.type not in (tokenize.NL,)]
        if any(x.string=='[' for x in prev) and len(nxt)>=2 and nxt[0].string==']' and nxt[1].string=='=':
            start=toks.index(nxt[1],i+1)+1
            break
    if start is None:return None,[]
    pieces=[];depth=0
    for tok in toks[start:]:
        if tok.type==tokenize.OP and tok.string in '([{':depth+=1
        elif tok.type==tokenize.OP and tok.string in ')]}':depth=max(0,depth-1)
        elif tok.type==tokenize.STRING:
            value=ast.literal_eval(tok.string)
            if not isinstance(value,str):return None,[]
            pieces.append(value)
        elif tok.type in (tokenize.NEWLINE,tokenize.ENDMARKER) and depth==0:
            break
    return ''.join(pieces),pieces

def build(repo:Path)->dict:
    audit_raw=show(repo,CENSUS,AUDIT_RECORD);science_raw=show(repo,CENSUS,SCIENCE_RECORD)
    wrapper_raw=show(repo,WRAPPER_COMMIT,WRAPPER_PATH);impl_raw=show(repo,SCIENCE_IMPL_COMMIT,SCIENCE_IMPL_PATH);bd_raw=show(repo,BD_RESULT_COMMIT,BD_RESULT_PATH)
    audit=text(audit_raw);science=text(science_raw);wrapper=text(wrapper_raw);impl=text(impl_raw);bd=text(bd_raw)
    evidence={'audit_record':H(audit_raw),'science_record':H(science_raw),'wrapper_source':H(wrapper_raw),'science_implementation':H(impl_raw),'bd_result':H(bd_raw)}
    note,pieces=semantic_supplemental_note(wrapper)
    times={k:epoch(repo,v) for k,v in {'science_terminal':SCIENCE_COMMIT,'science_implementation':SCIENCE_IMPL_COMMIT,'wrapper':WRAPPER_COMMIT,'audit':AUDIT_COMMIT}.items()}
    reverse_tokens=[AUDIT_RECORD,AUDIT_COMMIT,WRAPPER_COMMIT,'qgr_iter057y_actions_reproduction_fixed']
    reverse_found=any(tok in science or tok in impl for tok in reverse_tokens)
    controls={
      'evidence_hashes_exact':evidence==EXPECTED_EVIDENCE,
      'audit_names_terminal_science_authority':f'Terminal Iter057Y authority: `{SCIENCE_COMMIT}`' in audit,
      'audit_names_corrected_wrapper':f'Corrected provenance wrapper: `{WRAPPER_COMMIT}`' in audit,
      'audit_self_identifies_supplemental_provenance':'supplemental Actions provenance audit' in audit,
      'audit_says_terminal_classification_unchanged':'terminal Iter057Y classification is unchanged' in audit,
      'audit_metadata_only_no_science_change':'changes only that metadata validation predicate' in audit and 'does not change source coefficients, response coefficients, the affine matrix, right-hand side, solve, or scientific decision rules' in audit,
      'wrapper_imports_science_module':'import qgr_iter057y_onshell_q2_q4_q6_q8_response as y' in wrapper,
      'wrapper_invokes_science_compute':'obj = y.compute()' in wrapper,
      'wrapper_metadata_only_note':isinstance(note,str) and 'Corrected only Iter057V provenance metadata validation' in note and 'scientific inputs, coefficients, affine system, solve and replay are unchanged.' in note,
      'science_result_freezes_q8_object':f'Implementation: `{SCIENCE_IMPL_COMMIT}`' in science and 'Canonical Q8 data:' in science and '180 nonzero normalized Q8 coefficients' in science,
      'science_terminal_precedes_wrapper_and_audit':times['science_terminal']<times['wrapper']<times['audit'],
      'science_implementation_precedes_science_terminal':times['science_implementation']<times['science_terminal'],
      'reverse_dependency_absent':not reverse_found,
      'bd_membership_contains_both_y_records':SCIENCE_RECORD in bd and AUDIT_RECORD in bd,
      'no_later_queue_item_consumed':True,
      'science_recomputed':False,'historical_result_modified':False,'claim_lock_promoted':False,
    }
    positive=all(v is True for k,v in controls.items() if k not in {'science_recomputed','historical_result_modified','claim_lock_promoted'})
    relation='SCIENCE_BEFORE_AUDIT' if positive and not controls['science_recomputed'] and not controls['historical_result_modified'] and not controls['claim_lock_promoted'] else 'UNRESOLVED'
    bundle=[SCIENCE_RECORD,AUDIT_RECORD]
    return {'gate':GATE,'mode':'primary_repaired','preregistration_commit':PREREG,'census_commit':CENSUS,'bd_result_commit':BD_RESULT_COMMIT,'implementation_path':'scripts/qgr_iter057bf_y_order_primary_repaired.py','implementation_sha256':H(Path(__file__).read_bytes()),'evidence_sha256':evidence,'semantic_note':note,'semantic_note_literal_piece_count':len(pieces),'semantic_note_literal_piece_sha256':[H(p.encode()) for p in pieces],'commit_epochs':times,'science_authority_commit':SCIENCE_COMMIT,'wrapper_commit':WRAPPER_COMMIT,'audit_commit':AUDIT_COMMIT,'audit_to_science_reference':controls['audit_names_terminal_science_authority'],'wrapper_to_science_call':controls['wrapper_invokes_science_compute'],'audit_is_supplemental':controls['audit_self_identifies_supplemental_provenance'] and controls['audit_metadata_only_no_science_change'],'reverse_dependency_found':reverse_found,'ordering_relation':relation,'same_iteration_bundle':bundle if relation=='SCIENCE_BEFORE_AUDIT' else None,'execution_order':bundle if relation=='SCIENCE_BEFORE_AUDIT' else None,'atomic_replay_bundle':relation=='SCIENCE_BEFORE_AUDIT','controls':controls,'all_controls_pass':relation=='SCIENCE_BEFORE_AUDIT','descendant_science_consumed':False,'theory_established_pct':0,'c6':'SYMBOLIC_UNFIXED'}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=build(a.repo.resolve());a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,sort_keys=True,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
