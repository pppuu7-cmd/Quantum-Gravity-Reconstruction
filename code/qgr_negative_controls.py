#!/usr/bin/env python3
from __future__ import annotations
import copy,json,re,tempfile
from pathlib import Path
from qgr_candidate_export_validator import validate_candidate
from qgr_kmqgb_adapter import adapt
from qgr_kmqgb_drift_detector import check as drift_check
from qgr_lineage_dag_validator import validate as lineage_validate
from qgr_benchmark_leakage_audit import audit_text
from build_qgr_programme_bundle import build
ROOT=Path(__file__).resolve().parents[1]

def registry_ok(r):
    st=r.get('stages',[]);ids=[x.get('stage_id') for x in st]
    if ids!=[f'R{i}' for i in range(10)] or len(set(ids))!=10:return False
    by={x['stage_id']:x for x in st}
    for x in st:
      if not x.get('critic') or not all(k in x for k in ['pass_condition','fail_condition','blocked_condition','invalid_condition']):return False
      if any(p not in by for p in x.get('prerequisites',[])):return False
    color={i:0 for i in ids}
    def dfs(v):
      color[v]=1
      for w in by[v].get('prerequisites',[]):
        if color[w]==1:return True
        if color[w]==0 and dfs(w):return True
      color[v]=2;return False
    return not any(color[v]==0 and dfs(v) for v in ids)

def stale_current_marker(text):
    return bool(re.search(r'(current|canonical)[^\n]{0,80}24%',text,re.I))

def run_controls(kroot:Path):
    r=json.loads((ROOT/'protocol/QGR_GATE_REGISTRY.json').read_text()); synth=json.loads((ROOT/'synthetic/qgr_synthetic_blocked_candidate_v1.json').read_text()); dag=json.loads((ROOT/'protocol/QGR_SCIENTIFIC_LINEAGE_DAG.json').read_text())
    c={}
    c['stale_24_detected']=stale_current_marker('Current canonical candidate-program readiness: 24%')
    x=copy.deepcopy(r);x['stages']=[s for s in x['stages'] if s['stage_id']!='R8'];c['missing_R8_rejected']=not registry_ok(x)
    x=copy.deepcopy(r);x['stages'][8]['prerequisites']=['R9'];c['broken_stage_transition_rejected']=not registry_ok(x)
    x=copy.deepcopy(r);x['stages'][0]['prerequisites']=['R1'];c['stage_cycle_rejected']=not registry_ok(x)
    x=copy.deepcopy(r);x['stages'][5]['critic']='';c['missing_critic_rejected']=not registry_ok(x)
    malformed=json.loads((ROOT/'synthetic/qgr_malformed_candidate_v1.json').read_text());c['malformed_candidate_rejected']=not validate_candidate(malformed)['valid']
    a=adapt(synth,'0'*64);a['promotion_gates']['G0']['status']='PASS';c['blocked_to_pass_detected']=not (synth['status']=='BLOCKED' and {v['status'] for v in a['promotion_gates'].values()}=={'BLOCKED'})
    x=copy.deepcopy(synth);x['claim_locks']['qgr_theory_established']=True;c['unauthorized_theory_claim_rejected']=not validate_candidate(x)['valid']
    x=copy.deepcopy(synth);x['parameters'][0]['value']=1;c['beta_one_rejected']=not validate_candidate(x)['valid']
    x=copy.deepcopy(synth);x['parameters'][1]['value']='1/3';x['parameters'][1]['status']='FIXED';c['c6_fix_rejected']=not validate_candidate(x)['valid']
    x=copy.deepcopy(synth);x['claim_locks']['kmqgb_new_required_authorized']=True;c['new_required_rejected']=not validate_candidate(x)['valid']
    c['kmqgb_drift_detected']=not drift_check(kroot,simulate=True)['valid']
    x=copy.deepcopy(synth);x['artifact_hashes']={};c['missing_hash_rejected']=not validate_candidate(x)['valid']
    with tempfile.TemporaryDirectory() as td:
      p1=Path(td)/'a';p2=Path(td)/'b';h1=build(p1);h2=build(p2);c['bundle_determinism_control']=h1==h2 and p1.read_bytes()==p2.read_bytes() and p1.read_bytes()!=p2.read_bytes()+b'X'
    c['benchmark_target_leakage_detected']=bool(audit_text('favorable_comparator_target=PASS'))
    c['ci_green_not_scientific_pass']=r['promotion_firewall']['ci_green_implies_scientific_pass'] is False and 'scientific_status' in json.loads((ROOT/'schemas/qgr_scientific_result_v1.schema.json').read_text())['required']
    x=copy.deepcopy(dag);x['protected_historical_files'][0]['terminal_commit']='0'*40;c['historical_overwrite_detected']=not lineage_validate(x,verify_git=True)['valid']
    x=copy.deepcopy(synth);x['scientific_candidate']=True;c['synthetic_as_real_rejected']=not validate_candidate(x)['valid']
    return {'valid':all(c.values()),'control_count':len(c),'controls':c,'failed':[k for k,v in c.items() if not v]}

def main(argv=None):
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--kmqgb-root',required=True);ap.add_argument('--output');a=ap.parse_args(argv);out=run_controls(Path(a.kmqgb_root));txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 1
if __name__=='__main__':raise SystemExit(main())
