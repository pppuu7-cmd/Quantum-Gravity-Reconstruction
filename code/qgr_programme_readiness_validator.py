#!/usr/bin/env python3
"""Primary fail-closed QGR programme-infrastructure readiness validator. Does not trust candidate_program_pct."""
from __future__ import annotations
import argparse,json,tempfile,traceback
from pathlib import Path
from qgr_candidate_export_validator import validate_candidate
from qgr_kmqgb_drift_detector import check as drift_check
from qgr_lineage_dag_validator import validate as lineage_validate
from qgr_synthetic_handshake import run as handshake_run
from qgr_negative_controls import run_controls,registry_ok,stale_current_marker
from build_qgr_programme_bundle import build
from qgr_clean_recovery_test import run as recovery_run
ROOT=Path(__file__).resolve().parents[1]
SEM='Research-program / roadmap infrastructure readiness only; not probability of correctness, not theory completion, and not fraction of quantum gravity solved.'

def j(rel):return json.loads((ROOT/rel).read_text())
def evaluate(kroot:Path):
    passed={}; invalid={}; detail={}
    def chk(letter,fn):
      try:
        v=fn();passed[letter]=bool(v);detail[letter]=v
      except Exception as e:
        passed[letter]=False;invalid[letter]=f'{type(e).__name__}: {e}';detail[letter]=traceback.format_exc()
    state=j('recovery/state.json')
    chk('A',lambda: j('protocol/QGR_READINESS_SEMANTICS.json')['candidate_program_100_semantics']==SEM and state['readiness']['candidate_program_pct_semantics']==SEM and state['readiness']['repository_infrastructure_pct']==100 and state['readiness']['theory_established_pct']==0 and state['readiness']['experimental_confirmation'] is False and all(v is False for v in state['claim_locks'].values()))
    def b():
      rd=(ROOT/'README.md').read_text();rm=(ROOT/'docs/ROADMAP.md').read_text();ss=state['science_sync'];front=(ROOT/'recovery/CURRENT_FRONT.md').read_text()
      return not stale_current_marker(rd) and not stale_current_marker(rm) and ss['last_terminal_science']=='ITER057AQ' and ss['next_preregistered_science']=='ITER057AR' and ss['next_preregistered_status']=='PREREGISTERED_NOT_PRODUCED' and 'ITER057AR' in front and 'PREREGISTERED_NOT_PRODUCED' in front
    chk('B',b)
    chk('C',lambda: registry_ok(j('protocol/QGR_GATE_REGISTRY.json')) and all(x.get('protocol_ready') is True for x in j('protocol/QGR_GATE_REGISTRY.json')['stages']))
    chk('D',lambda: validate_candidate(j('synthetic/qgr_synthetic_blocked_candidate_v1.json'))['valid'] and (ROOT/'schemas/qgr_candidate_export_v1.schema.json').exists() and (ROOT/'templates/qgr_candidate_export_v1.template.json').exists())
    chk('E',lambda: len(j('protocol/QGR_QUANTUM_COMPLETION_CONTRACT.json')['objects'])==10 and j('protocol/QGR_QUANTUM_COMPLETION_CONTRACT.json')['invent_missing_quantum_theory'] is False)
    chk('F',lambda: len(j('protocol/QGR_SAME_REALIZATION_CONTRACT.json')['required_identity_chain'])==9 and j('protocol/QGR_SAME_REALIZATION_CONTRACT.json')['forbid_downstream_realization_substitution'] is True)
    chk('G',lambda: set(j('schemas/qgr_gr_recovery_v1.schema.json')['required'])>={'lorentzian_4d_domain','effective_equations_or_action','newton_sector_map','leading_corrections','remainder_error_control','domain_of_validity','same_realization_id'})
    chk('H',lambda: set(j('schemas/qgr_normalized_observable_v1.schema.json')['required'])>={'uv_definition','normalization','ir_operational_definition','common_domain','parameter_identity','uncertainty_propagation','comparator_representation','falsifiable_statement'})
    chk('I',lambda: len(j('protocol/QGR_POST_CANDIDATE_DECISION_TREE.json')['nodes'])==18 and len(j('protocol/QGR_POST_CANDIDATE_DECISION_TREE.json')['edges'])==17)
    chk('J',lambda: lineage_validate(j('protocol/QGR_SCIENTIFIC_LINEAGE_DAG.json'),verify_git=True)['valid'] and (ROOT/'protocol/QGR_DEPENDENCY_SUPERSESSION_PROTOCOL.md').exists())
    chk('K',lambda: drift_check(kroot)['valid'] and j('protocol/QGR_KMQGB_INTERFACE_PIN.json')['rqir_core_version']=='1.0')
    def l():
      with tempfile.TemporaryDirectory() as td:return handshake_run(ROOT/'synthetic/qgr_synthetic_blocked_candidate_v1.json',kroot,Path(td)/'adapted.json')['valid']
    chk('L',l)
    def m():
      with tempfile.TemporaryDirectory() as td:
        a=Path(td)/'a';b=Path(td)/'b';return build(a)==build(b) and a.read_bytes()==b.read_bytes()
    chk('M',m)
    chk('N',lambda: (ROOT/'code/qgr_programme_readiness_validator.py').exists() and set(j('protocol/QGR_PROGRAMME_READINESS_100_CONTRACT.json')['mandatory_obligations'])==set('ABCDEFGHIJKLMNOP'))
    chk('O',lambda: run_controls(kroot)['valid'])
    chk('P',lambda: recovery_run()['valid'])
    failed=[k for k in 'ABCDEFGHIJKLMNOP' if not passed.get(k,False)];readiness=not failed and not invalid
    classification='QGR_PROGRAMME_INFRASTRUCTURE_100_PASS' if readiness else ('QGR_PROGRAMME_INFRASTRUCTURE_INVALID' if invalid else 'QGR_PROGRAMME_INFRASTRUCTURE_INCOMPLETE')
    return {'classification':classification,'mandatory_obligation_count':16,'passed_obligation_count':sum(passed.values()),'failed_obligations':failed,'invalid_obligations':invalid,'obligations':passed,'readiness_100_boolean':readiness,'declared_candidate_program_pct_ignored_for_decision':True,'detail':detail}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--kmqgb-root',required=True);ap.add_argument('--require-100',action='store_true');ap.add_argument('--output');a=ap.parse_args(argv);out=evaluate(Path(a.kmqgb_root));txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if (out['readiness_100_boolean'] or not a.require_100) else 2
if __name__=='__main__':raise SystemExit(main())
