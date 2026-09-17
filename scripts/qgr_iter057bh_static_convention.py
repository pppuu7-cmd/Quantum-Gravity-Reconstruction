#!/usr/bin/env python3
from __future__ import annotations
import argparse,ast,hashlib,json,subprocess
from pathlib import Path

GATE='ITER057BH_ITER057Y_SOURCE_EQUATION_CONVENTION_ADJUDICATION'
PREREG='4317e8d2dce74178ecddab100374455c933959c4'
X_REF='920b73f8430983255081b9bcd3ec6d222b737b08';X_PATH='code/qgr_iter057x_corrected_decic_seed_weyl3_sixth_source_jet.py'
Y_REF='98c82292885cec9a38fa400a5e08b1272104f8b8';Y_PATH='code/qgr_iter057y_onshell_q2_q4_q6_q8_response.py'
AQ_REF='23435e772cf82c985ed919aa2411d59667ffb3ff';AQ_PATH='code/qgr_iter057aq_degree6_causal_adjudication.py'
AT_REF='d45c6ba67459e2702909c2b864f5a5c24f104015';AT_PATH='code/qgr_iter057at_corrected_homogeneous_degree6_source.py'


def H(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def git(repo:Path,*args:str)->bytes:
    p=subprocess.run(['git','-C',str(repo),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if p.returncode:raise RuntimeError(f"git {' '.join(args)} rc={p.returncode} stderr_sha256={H(p.stderr)}")
    return p.stdout
def show(repo:Path,ref:str,path:str)->bytes:return git(repo,'show',f'{ref}:{path}')

def function(tree:ast.AST,name:str):
    for n in ast.walk(tree):
        if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name==name:return n
    return None

def source_segment(src:str,node:ast.AST)->str:return ast.get_source_segment(src,node) or ''
def has_call(node:ast.AST,name:str)->bool:
    return any(isinstance(n,ast.Call) and ((isinstance(n.func,ast.Name) and n.func.id==name) or (isinstance(n.func,ast.Attribute) and n.func.attr==name)) for n in ast.walk(node))

def build(repo:Path)->dict:
    raw={
      'x':show(repo,X_REF,X_PATH),'y':show(repo,Y_REF,Y_PATH),'aq':show(repo,AQ_REF,AQ_PATH),'at':show(repo,AT_REF,AT_PATH)}
    src={k:v.decode('utf-8','strict') for k,v in raw.items()};trees={k:ast.parse(v) for k,v in src.items()}
    xcompute=function(trees['x'],'compute'); ycompute=function(trees['y'],'compute'); yconsume=function(trees['y'],'consume_authorities')
    aqx=function(trees['aq'],'x_operator'); atp=function(trees['at'],'construct_primary'); ati=function(trees['at'],'construct_independent')

    x_neg_assignment=False;x_shat_output=False
    for n in ast.walk(xcompute):
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='S' for t in n.targets):
            val=n.value
            if isinstance(val,ast.Call) and isinstance(val.func,ast.Name) and val.func.id=='neg' and val.args and isinstance(val.args[0],ast.Subscript):
                if isinstance(val.args[0].value,ast.Name) and val.args[0].value.id=='Edown':x_neg_assignment=True
    for n in ast.walk(xcompute):
        if isinstance(n,ast.Dict):
            keys=[k.value for k in n.keys if isinstance(k,ast.Constant) and isinstance(k.value,str)]
            if 'Shat_normalized_sparse' in keys:x_shat_output=True

    aq_returns_edown=any(isinstance(n,ast.Return) and isinstance(n.value,ast.Name) and n.value.id=='Edown' for n in aqx.body)
    at_primary_calls_aq=any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='aq' and n.func.attr=='x_operator' for n in ast.walk(atp))
    at_independent_calls_ao=any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='b' and n.func.attr=='ao_source' for n in ast.walk(ati))
    at_independent_returns_edown=any(isinstance(n,ast.Return) and isinstance(n.value,ast.Tuple) and any(isinstance(e,ast.Name) and e.id=='Edown' for e in n.value.elts) for n in ati.body)

    y_loads_x=False;y_source_population=False
    for n in ast.walk(yconsume):
        seg=source_segment(src['y'],n)
        if isinstance(n,ast.Assign) and 'read_csv_authority(X_PATH' in seg:y_loads_x=True
        if isinstance(n,ast.For) and 'for item in xrows' in seg and 'source[a][b]' in seg:y_source_population=True
    y_field_minus_source=False;y_final_minus_source=False;y_rhs_negative_residual=False
    for n in ast.walk(ycompute):
        seg=source_segment(src['y'],n)
        if isinstance(n,ast.For) and 'field0[a][b]' in seg and 'sub(DG0[a][b],source[a][b])' in seg:y_field_minus_source=True
        if isinstance(n,ast.For) and 'redres' in seg and 'sub(DGT[a][b],source[a][b])' in seg and 'sub(unred[a][b],source[a][b])' in seg:y_final_minus_source=True
        if isinstance(n,ast.For) and 'rhs.append(-qrat(normalized(field0[a][b],al)))' in seg:y_rhs_negative_residual=True

    controls={
      'x_serialized_source_is_unary_negative_edown':x_neg_assignment and x_shat_output,
      'aq_x_operator_returns_edown':aq_returns_edown,
      'at_primary_is_aq_x_operator_pf':at_primary_calls_aq,
      'at_independent_is_ao_edown':at_independent_calls_ao and at_independent_returns_edown,
      'y_loads_historical_x_csv_into_source':y_loads_x and y_source_population,
      'y_initial_field_residual_is_DG_minus_source':y_field_minus_source,
      'y_terminal_residual_is_DG_minus_source':y_final_minus_source,
      'y_rhs_is_negative_current_residual':y_rhs_negative_residual,
      'corrected_y_outcome_not_loaded':True,'historical_file_modified':False,'claim_lock_promoted':False}
    positive=all(v is True for k,v in controls.items() if k not in {'historical_file_modified','claim_lock_promoted'}) and controls['historical_file_modified'] is False and controls['claim_lock_promoted'] is False
    if positive and x_neg_assignment and aq_returns_edown and at_primary_calls_aq and at_independent_calls_ao:
        mapping='MAP_MINUS'
    elif positive and not x_neg_assignment:
        mapping='MAP_PLUS'
    else:mapping='UNRESOLVED'
    return {
      'gate':GATE,'lane':'static','preregistration_commit':PREREG,
      'evidence_sha256':{k:H(v) for k,v in raw.items()},'controls':controls,
      'historical_x_source_relation_to_legacy_edown':'NEGATIVE' if x_neg_assignment else ('SAME' if positive else 'UNRESOLVED'),
      'at_object':'EDOWN_OX_PF' if aq_returns_edown and at_primary_calls_aq and at_independent_calls_ao else 'UNRESOLVED',
      'y_field_equation':'DG_MINUS_SOURCE_EQUALS_ZERO' if y_field_minus_source and y_final_minus_source else 'UNRESOLVED',
      'corrected_source_map':mapping,
      'implied_corrected_source_expression':'-AT' if mapping=='MAP_MINUS' else ('+AT' if mapping=='MAP_PLUS' else None),
      'implied_degree6_rhs_source_contribution':'+AT' if mapping=='MAP_MINUS' and y_rhs_negative_residual else ('-AT' if mapping=='MAP_PLUS' and y_rhs_negative_residual else None),
      'all_controls_pass':positive and mapping!='UNRESOLVED','corrected_y_science_consumed':False,'theory_established_pct':0,'c6':'SYMBOLIC_UNFIXED'}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();o=build(a.repo.resolve());a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n');print(json.dumps(o,sort_keys=True,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
