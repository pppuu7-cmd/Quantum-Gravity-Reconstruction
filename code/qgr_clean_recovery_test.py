#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def nonterminal_status(value):
    if not isinstance(value,str) or not value:
        return False
    u=value.upper()
    terminal_tokens=('TERMINAL_','PASS','FAIL','BLOCKED','INVALID')
    return not any(u==t or u.startswith(t) for t in terminal_tokens)

def run():
    m=json.loads((ROOT/'recovery/CLEAN_SESSION_RECOVERY_MANIFEST.json').read_text())
    s=json.loads((ROOT/'recovery/state.json').read_text())
    sem=json.loads((ROOT/'protocol/QGR_READINESS_SEMANTICS.json').read_text())
    sync=s['science_sync']; rec=s['recovery_sync']
    next_science=sync.get('next_preregistered_science')
    next_status=sync.get('next_preregistered_status')
    prereg_answer=next_science if next_science is not None else 'NONE'
    active_question=s.get('active_question')
    if isinstance(active_question,dict):
        next_action=active_question.get('text') or s.get('next_gate_lock') or s.get('active_blocker')
    elif isinstance(active_question,str) and active_question:
        next_action=active_question
    else:
        # A terminal BLOCKED front can intentionally have no active question/no next gate.
        # Recovery must still state the bounded admissible continuation without inventing science.
        next_action=s.get('next_gate_lock') or s.get('active_blocker') or 'NO_NEXT_SCIENTIFIC_ACTION_OPEN'
    answers={
      'project':s['project']['name'],
      'repository_infrastructure_readiness':s['readiness']['repository_infrastructure_pct'],
      'programme_infrastructure_readiness':s['readiness']['candidate_program_pct'],
      'meaning_of_100':sem['candidate_program_100_semantics'],
      'theory_readiness':s['readiness']['theory_established_pct'],
      'current_scientific_front':sync['last_terminal_science'],
      'last_terminal_result':sync['last_terminal_science'],
      'preregistered_not_run':prereg_answer,
      'forbidden_claims':[k for k,v in s['claim_locks'].items() if v is False],
      'next_scientific_action':next_action,
      'future_candidate_export':'schemas/qgr_candidate_export_v1.schema.json',
      'kmqgb_interface':'protocol/QGR_KMQGB_INTERFACE_PIN.json',
      'kmqgb_version_change':'KMQGB_INTERFACE_VERSION_DRIFT'
    }
    required=set(m['questions'])
    missing=[k for k in required if k not in answers or answers[k] in (None,'',[])]
    if next_science is None:
        prereg_state_consistent=(next_status in (None,'NONE') and rec.get('latest_active_gate') in (None,'NONE'))
    else:
        gate=str(rec.get('latest_active_gate') or '')
        active_status=rec.get('active_gate_status')
        prereg_state_consistent=(
            isinstance(next_science,str) and bool(next_science)
            and nonterminal_status(next_status)
            and next_science == gate
            and active_status==next_status
        )
    last_terminal=sync.get('last_terminal_science')
    terminal_commit=rec.get('latest_terminal_result_commit')
    terminal_state_consistent=(
        isinstance(last_terminal,str) and bool(last_terminal)
        and isinstance(terminal_commit,str) and bool(terminal_commit)
    )
    ok=(not missing and m.get('chat_memory_required') is False and prereg_state_consistent and terminal_state_consistent)
    return {
      'valid':ok,'chat_memory_used':False,'missing_answers':missing,'answers':answers,
      'preregistration_state_consistent':prereg_state_consistent,
      'terminal_state_consistent':terminal_state_consistent,
      'next_preregistered_status_observed':next_status
    }

def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--output');a=ap.parse_args(argv)
    out=run();txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 1
if __name__=='__main__':raise SystemExit(main())
