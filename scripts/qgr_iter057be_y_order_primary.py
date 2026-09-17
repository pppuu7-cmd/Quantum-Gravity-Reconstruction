#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

GATE='ITER057BE_ITER057Y_SAME_ITERATION_REPLAY_ORDER_ADJUDICATION'
PREREG='5b16cb4432097fd974adf93e624f872e4620cd17'
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


def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def git(repo:Path,*args:str)->bytes:
    p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if p.returncode:raise RuntimeError(f"git {' '.join(args)} rc={p.returncode} stderr_sha256={H(p.stderr)}")
    return p.stdout
def show(repo:Path,ref:str,path:str)->bytes:return git(repo,'show',f'{ref}:{path}')
def text(raw:bytes)->str:return raw.decode('utf-8','strict')
def epoch(repo:Path,commit:str)->int:return int(text(git(repo,'show','-s','--format=%ct',commit)).strip())

def build(repo:Path)->dict:
    audit_raw=show(repo,CENSUS,AUDIT_RECORD); science_raw=show(repo,CENSUS,SCIENCE_RECORD)
    wrapper_raw=show(repo,WRAPPER_COMMIT,WRAPPER_PATH); impl_raw=show(repo,SCIENCE_IMPL_COMMIT,SCIENCE_IMPL_PATH)
    bd_raw=show(repo,BD_RESULT_COMMIT,BD_RESULT_PATH)
    audit=text(audit_raw);science=text(science_raw);wrapper=text(wrapper_raw);impl=text(impl_raw);bd=text(bd_raw)
    times={k:epoch(repo,v) for k,v in {'science_terminal':SCIENCE_COMMIT,'science_implementation':SCIENCE_IMPL_COMMIT,'wrapper':WRAPPER_COMMIT,'audit':AUDIT_COMMIT}.items()}
    reverse_tokens=[AUDIT_RECORD,AUDIT_COMMIT,WRAPPER_COMMIT,'qgr_iter057y_actions_reproduction_fixed']
    reverse_found=any(tok in science or tok in impl for tok in reverse_tokens)
    controls={
      'audit_names_terminal_science_authority':f'Terminal Iter057Y authority: `{SCIENCE_COMMIT}`' in audit,
      'audit_names_corrected_wrapper':f'Corrected provenance wrapper: `{WRAPPER_COMMIT}`' in audit,
      'audit_self_identifies_supplemental_provenance':'supplemental Actions provenance audit' in audit,
      'audit_says_terminal_classification_unchanged':'terminal Iter057Y classification is unchanged' in audit,
      'audit_metadata_only_no_science_change':'changes only that metadata validation predicate' in audit and 'does not change source coefficients, response coefficients, the affine matrix, right-hand side, solve, or scientific decision rules' in audit,
      'wrapper_imports_science_module':'import qgr_iter057y_onshell_q2_q4_q6_q8_response as y' in wrapper,
      'wrapper_invokes_science_compute':'obj = y.compute()' in wrapper,
      'wrapper_metadata_only_note':'Corrected only Iter057V provenance metadata validation' in wrapper and 'scientific inputs, coefficients, affine system, solve and replay are unchanged' in wrapper,
      'science_result_freezes_q8_object':f'Implementation: `{SCIENCE_IMPL_COMMIT}`' in science and 'Canonical Q8 data:' in science and '180 nonzero normalized Q8 coefficients' in science,
      'science_terminal_precedes_wrapper_and_audit':times['science_terminal']<times['wrapper']<times['audit'],
      'science_implementation_precedes_science_terminal':times['science_implementation']<times['science_terminal'],
      'reverse_dependency_absent':not reverse_found,
      'bd_membership_contains_both_y_records':SCIENCE_RECORD in bd and AUDIT_RECORD in bd,
      'no_later_queue_item_consumed':True,
      'science_recomputed':False,
      'historical_result_modified':False,
      'claim_lock_promoted':False,
    }
    relation='SCIENCE_BEFORE_AUDIT' if all(v is True or (v is False and k in {'science_recomputed','historical_result_modified','claim_lock_promoted'}) for k,v in controls.items()) else 'UNRESOLVED'
    bundle=[SCIENCE_RECORD,AUDIT_RECORD]
    return {
      'gate':GATE,'mode':'primary','preregistration_commit':PREREG,'census_commit':CENSUS,'bd_result_commit':BD_RESULT_COMMIT,
      'implementation_path':'scripts/qgr_iter057be_y_order_primary.py','implementation_sha256':H(Path(__file__).read_bytes()),
      'evidence_sha256':{'audit_record':H(audit_raw),'science_record':H(science_raw),'wrapper_source':H(wrapper_raw),'science_implementation':H(impl_raw),'bd_result':H(bd_raw)},
      'commit_epochs':times,'science_authority_commit':SCIENCE_COMMIT,'wrapper_commit':WRAPPER_COMMIT,'audit_commit':AUDIT_COMMIT,
      'audit_to_science_reference':controls['audit_names_terminal_science_authority'],'wrapper_to_science_call':controls['wrapper_invokes_science_compute'],
      'audit_is_supplemental':controls['audit_self_identifies_supplemental_provenance'] and controls['audit_metadata_only_no_science_change'],
      'reverse_dependency_found':reverse_found,'ordering_relation':relation,'same_iteration_bundle':bundle if relation=='SCIENCE_BEFORE_AUDIT' else None,
      'execution_order':bundle if relation=='SCIENCE_BEFORE_AUDIT' else None,'atomic_replay_bundle':relation=='SCIENCE_BEFORE_AUDIT',
      'controls':controls,'all_controls_pass':relation=='SCIENCE_BEFORE_AUDIT','descendant_science_consumed':False,'theory_established_pct':0,'c6':'SYMBOLIC_UNFIXED'}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=build(a.repo.resolve());a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,sort_keys=True,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
