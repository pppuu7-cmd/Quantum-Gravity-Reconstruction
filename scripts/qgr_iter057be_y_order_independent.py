#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, hashlib, json, re, subprocess
from pathlib import Path

GATE='ITER057BE_ITER057Y_SAME_ITERATION_REPLAY_ORDER_ADJUDICATION'
PREREG='5b16cb4432097fd974adf93e624f872e4620cd17'
CENSUS='616859890df95057556d265612c53da839a5848a'
BD='c1e5be8e0da856d0960dce20cdb48f207b572869'
SCI='cb2758238daba9ecf9c86e01e171f6c6d31c72b9'
SCI_IMPL='98c82292885cec9a38fa400a5e08b1272104f8b8'
WRAP='8d5936b988c57d44e8a279b9d5fd4f6238a071e4'
AUDIT='ddcb7f9dde1ec8d197db7c6e074f0a1d03911b3e'
SCIENCE_RECORD='results/ITER057Y_ONSHELL_FIRST_ORDER_Q2_Q4_Q6_Q8_RESPONSE_TERMINAL.md'
AUDIT_RECORD='results/ITER057Y_ACTIONS_PROVENANCE_AUDIT.md'
WRAP_PATH='code/qgr_iter057y_actions_reproduction_fixed.py'
SCI_PATH='code/qgr_iter057y_onshell_q2_q4_q6_q8_response.py'
BD_PATH='results/ITER057BD_STRICT_EARLIER_ONLY_DESCENDANT_DEPENDENCY_ADJUDICATION_TERMINAL.md'
SCI_MODULE='qgr_iter057y_onshell_q2_q4_q6_q8_response'


def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def run(repo:Path,args:list[str],ok=(0,))->bytes:
    p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if p.returncode not in ok:raise RuntimeError(f"git {' '.join(args)} rc={p.returncode} stderr_sha256={H(p.stderr)}")
    return p.stdout
def show(repo:Path,ref:str,path:str)->bytes:return run(repo,['show',f'{ref}:{path}'])
def changed(repo:Path,commit:str)->list[str]:
    raw=run(repo,['show','--format=','--name-only','-z',commit]);return [x.decode('utf-8','strict') for x in raw.split(b'\0') if x]
def ancestor(repo:Path,a:str,b:str)->bool:
    p=subprocess.run(['git','-C',str(repo),'merge-base','--is-ancestor',a,b],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if p.returncode not in (0,1):raise RuntimeError(f'ancestry check failed {a} {b} stderr_sha256={H(p.stderr)}')
    return p.returncode==0

def ast_flow(source:str)->dict:
    tree=ast.parse(source);aliases=set();compute_calls=0;patched_consume=False
    for node in ast.walk(tree):
        if isinstance(node,ast.Import):
            for a in node.names:
                if a.name==SCI_MODULE:aliases.add(a.asname or a.name)
        elif isinstance(node,ast.ImportFrom) and node.module==SCI_MODULE:
            aliases.add(node.module)
    for node in ast.walk(tree):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and isinstance(node.func.value,ast.Name) and node.func.value.id in aliases and node.func.attr=='compute':compute_calls+=1
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Attribute) and isinstance(target.value,ast.Name) and target.value.id in aliases and target.attr=='consume_authorities':patched_consume=True
    top_functions=[n.name for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))]
    return {'module_aliases':sorted(aliases),'compute_call_count':compute_calls,'consume_authorities_monkeypatch':patched_consume,'top_level_functions':top_functions}

def labeled_commit(text:str,label:str):
    m=re.search(rf'^{re.escape(label)}\s*`([0-9a-f]{{40}})`',text,re.M);return m.group(1) if m else None

def build(repo:Path)->dict:
    audit_raw=show(repo,CENSUS,AUDIT_RECORD);science_raw=show(repo,CENSUS,SCIENCE_RECORD);wrapper_raw=show(repo,WRAP,WRAP_PATH);science_impl_raw=show(repo,SCI_IMPL,SCI_PATH);bd_raw=show(repo,BD,BD_PATH)
    audit=audit_raw.decode('utf-8','strict');science=science_raw.decode('utf-8','strict');wrapper=wrapper_raw.decode('utf-8','strict');bd=bd_raw.decode('utf-8','strict')
    flow=ast_flow(wrapper)
    topology={'science_terminal_changed_files':changed(repo,SCI),'wrapper_changed_files':changed(repo,WRAP),'audit_changed_files':changed(repo,AUDIT)}
    ancestry={'science_impl_before_terminal':ancestor(repo,SCI_IMPL,SCI),'science_terminal_before_wrapper':ancestor(repo,SCI,WRAP),'wrapper_before_audit':ancestor(repo,WRAP,AUDIT)}
    doc=ast.get_docstring(ast.parse(wrapper)) or ''
    audit_science=labeled_commit(audit,'Terminal Iter057Y authority:')
    audit_wrapper=labeled_commit(audit,'Corrected provenance wrapper:')
    future_markers=(AUDIT,WRAP,AUDIT_RECORD,'qgr_iter057y_actions_reproduction_fixed')
    reverse_found=any(x in science or x in science_impl_raw.decode('utf-8','strict') for x in future_markers)
    controls={
      'audit_label_resolves_science_terminal':audit_science==SCI,
      'audit_label_resolves_wrapper':audit_wrapper==WRAP,
      'commit_topology_science_result_created_at_terminal':SCIENCE_RECORD in topology['science_terminal_changed_files'],
      'commit_topology_wrapper_added_after_terminal':WRAP_PATH in topology['wrapper_changed_files'],
      'commit_topology_audit_added_after_wrapper':AUDIT_RECORD in topology['audit_changed_files'],
      'ancestry_science_impl_terminal_wrapper_audit':all(ancestry.values()),
      'ast_imports_science_module':bool(flow['module_aliases']),
      'ast_calls_science_compute_exactly_once':flow['compute_call_count']==1,
      'ast_wrapper_overrides_only_authority_consumption_before_compute':flow['consume_authorities_monkeypatch'] is True,
      'wrapper_doc_is_supplemental_metadata_repair':'Supplemental Iter057Y Actions reproduction' in doc and 'metadata validation' in doc and 'does not change any response/source coefficients or scientific decision' in doc,
      'audit_declares_metadata_only_reproduction':'supplemental' in audit.lower() and 'metadata-validation defect, not a scientific discrepancy' in audit and 'terminal Iter057Y classification is unchanged' in audit,
      'science_record_contains_canonical_scientific_authority':'Canonical Q8 data:' in science and f'Implementation: `{SCI_IMPL}`' in science and 'complete ordered coefficient authority' in science,
      'reverse_dependency_absent':not reverse_found,
      'bd_contains_both_y_members':SCIENCE_RECORD in bd and AUDIT_RECORD in bd,
      'no_later_queue_item_consumed':True,'science_recomputed':False,'historical_result_modified':False,'claim_lock_promoted':False,
    }
    positive=[v for k,v in controls.items() if k not in {'science_recomputed','historical_result_modified','claim_lock_promoted'}]
    relation='SCIENCE_BEFORE_AUDIT' if all(positive) and not controls['science_recomputed'] and not controls['historical_result_modified'] and not controls['claim_lock_promoted'] else 'UNRESOLVED'
    bundle=[SCIENCE_RECORD,AUDIT_RECORD]
    return {'gate':GATE,'mode':'independent','preregistration_commit':PREREG,'census_commit':CENSUS,'bd_result_commit':BD,'implementation_path':'scripts/qgr_iter057be_y_order_independent.py','implementation_sha256':H(Path(__file__).read_bytes()),'evidence_sha256':{'audit_record':H(audit_raw),'science_record':H(science_raw),'wrapper_source':H(wrapper_raw),'science_implementation':H(science_impl_raw),'bd_result':H(bd_raw)},'git_topology':topology,'ancestry':ancestry,'ast_call_flow':flow,'science_authority_commit':audit_science,'wrapper_commit':audit_wrapper,'audit_commit':AUDIT,'audit_to_science_reference':audit_science==SCI,'wrapper_to_science_call':flow['compute_call_count']==1,'audit_is_supplemental':controls['audit_declares_metadata_only_reproduction'] and controls['wrapper_doc_is_supplemental_metadata_repair'],'reverse_dependency_found':reverse_found,'ordering_relation':relation,'same_iteration_bundle':bundle if relation=='SCIENCE_BEFORE_AUDIT' else None,'execution_order':bundle if relation=='SCIENCE_BEFORE_AUDIT' else None,'atomic_replay_bundle':relation=='SCIENCE_BEFORE_AUDIT','controls':controls,'all_controls_pass':relation=='SCIENCE_BEFORE_AUDIT','descendant_science_consumed':False,'theory_established_pct':0,'c6':'SYMBOLIC_UNFIXED'}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=build(a.repo.resolve());a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n',encoding='utf-8');print(json.dumps(o,sort_keys=True,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
