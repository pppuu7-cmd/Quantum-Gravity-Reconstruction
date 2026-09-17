#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def get_path(obj,path):
    for k in path.split('.'):obj=obj[k]
    return obj
def run():
    m=json.loads((ROOT/'recovery/CLEAN_SESSION_RECOVERY_MANIFEST.json').read_text());s=json.loads((ROOT/'recovery/state.json').read_text()); sem=json.loads((ROOT/'protocol/QGR_READINESS_SEMANTICS.json').read_text())
    next_science=s['science_sync']['next_preregistered_science']
    next_status=s['science_sync']['next_preregistered_status']
    prereg_answer=next_science if next_science is not None else 'NONE'
    answers={
      'project':s['project']['name'],'repository_infrastructure_readiness':s['readiness']['repository_infrastructure_pct'],
      'programme_infrastructure_readiness':s['readiness']['candidate_program_pct'],'meaning_of_100':sem['candidate_program_100_semantics'],
      'theory_readiness':s['readiness']['theory_established_pct'],'current_scientific_front':s['science_sync']['last_terminal_science'],
      'last_terminal_result':s['science_sync']['last_terminal_science'],'preregistered_not_run':prereg_answer,
      'forbidden_claims':[k for k,v in s['claim_locks'].items() if v is False],'next_scientific_action':s['active_question']['text'],
      'future_candidate_export':'schemas/qgr_candidate_export_v1.schema.json','kmqgb_interface':'protocol/QGR_KMQGB_INTERFACE_PIN.json','kmqgb_version_change':'KMQGB_INTERFACE_VERSION_DRIFT'}
    required=set(m['questions']);missing=[k for k in required if k not in answers or answers[k] in (None,'',[])]
    prereg_state_consistent=(next_status=='PREREGISTERED_NOT_PRODUCED' and next_science is not None) or (next_status=='NONE' and next_science is None)
    ok=not missing and m.get('chat_memory_required') is False and prereg_state_consistent
    return {'valid':ok,'chat_memory_used':False,'missing_answers':missing,'answers':answers,'preregistration_state_consistent':prereg_state_consistent}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--output');a=ap.parse_args(argv);out=run();txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 1
if __name__=='__main__':raise SystemExit(main())
