#!/usr/bin/env python3
"""Independent QGR readiness Critic. It never imports the primary readiness validator and never uses candidate_program_pct as evidence."""
from __future__ import annotations
import argparse,json,tempfile
from pathlib import Path
from qgr_candidate_export_validator import validate_candidate
from qgr_kmqgb_drift_detector import check as drift_check
from qgr_lineage_dag_validator import validate as lineage_validate
from qgr_synthetic_handshake import run as handshake_run
from qgr_negative_controls import run_controls,registry_ok,stale_current_marker
from build_qgr_programme_bundle import build
from qgr_clean_recovery_test import run as recovery_run
ROOT=Path(__file__).resolve().parents[1]; SEM='Research-program / roadmap infrastructure readiness only; not probability of correctness, not theory completion, and not fraction of quantum gravity solved.'
BUNDLE_REQUIRED={'protocol/QGR_PROGRAMME_READINESS_100_CONTRACT.json','protocol/QGR_GATE_REGISTRY.json','schemas/qgr_candidate_export_v1.schema.json','code/qgr_candidate_export_validator.py','code/qgr_kmqgb_adapter.py','code/qgr_programme_readiness_validator.py','code/qgr_programme_readiness_critic.py','recovery/state.json','recovery/CURRENT_FRONT.md','protocol/QGR_KMQGB_INTERFACE_PIN.json'}
def j(p):return json.loads((ROOT/p).read_text())
def critique(kroot:Path):
    state=j('recovery/state.json');sem=j('protocol/QGR_READINESS_SEMANTICS.json');reg=j('protocol/QGR_GATE_REGISTRY.json');dt=j('protocol/QGR_POST_CANDIDATE_DECISION_TREE.json');q=j('protocol/QGR_QUANTUM_COMPLETION_CONTRACT.json');sr=j('protocol/QGR_SAME_REALIZATION_CONTRACT.json')
    o={}
    o['A']=sem['candidate_program_100_semantics']==SEM and state['readiness']['theory_established_pct']==0 and all(v is False for v in state['claim_locks'].values())
    o['B']=not stale_current_marker((ROOT/'README.md').read_text()) and not stale_current_marker((ROOT/'docs/ROADMAP.md').read_text()) and state['science_sync']=={'last_terminal_science':'ITER057AQ','next_preregistered_science':'ITER057AR','next_preregistered_status':'PREREGISTERED_NOT_PRODUCED'}
    o['C']=registry_ok(reg) and all(s.get('protocol_ready') for s in reg['stages'])
    o['D']=validate_candidate(j('synthetic/qgr_synthetic_blocked_candidate_v1.json'))['valid'] and (ROOT/'code/qgr_candidate_export_validator.py').exists()
    o['E']=q['objects'][2]=='amplitude_generator_or_measure' and q['heavy_compute_on_structural_blocker'] is False
    o['F']=len(sr['required_identity_chain'])==9 and sr['forbid_downstream_realization_substitution'] is True
    o['G']='same_realization_id' in j('schemas/qgr_gr_recovery_v1.schema.json')['required'];o['H']='normalization' in j('schemas/qgr_normalized_observable_v1.schema.json')['required']
    o['I']=len(dt['nodes'])==18 and len(dt['edges'])==17 and dt['nodes'][0]=='covariant_source_consistency' and dt['nodes'][-1]=='prediction_discrimination'
    o['J']=lineage_validate(j('protocol/QGR_SCIENTIFIC_LINEAGE_DAG.json'),verify_git=True)['valid'];o['K']=drift_check(kroot)['valid']
    with tempfile.TemporaryDirectory() as td:o['L']=handshake_run(ROOT/'synthetic/qgr_synthetic_blocked_candidate_v1.json',kroot,Path(td)/'adapted.json')['valid']
    with tempfile.TemporaryDirectory() as td:
      a=Path(td)/'a';b=Path(td)/'b';mf=j('release/QGR_PROGRAMME_BUNDLE_CONTENTS.json');o['M']=BUNDLE_REQUIRED<=set(mf['files']) and 'validators' in mf.get('required_classes',[]) and build(a)==build(b) and a.read_bytes()==b.read_bytes()
    o['N']=(ROOT/'code/qgr_programme_readiness_validator.py').exists() and j('protocol/QGR_PROGRAMME_READINESS_100_CONTRACT.json')['readiness_rule']=='ALL_A_THROUGH_P_PASS_AND_INDEPENDENT_CRITIC_TRUE';o['O']=run_controls(kroot)['valid'];o['P']=recovery_run()['valid']
    failed=[k for k in 'ABCDEFGHIJKLMNOP' if not o.get(k)];ready=not failed
    return {'mandatory_obligation_count':16,'passed_obligation_count':sum(o.values()),'failed_obligations':failed,'invalid_obligations':[],'readiness_100_boolean':ready,'obligations':o,'candidate_program_pct_was_not_used':True,'classification':'QGR_PROGRAMME_INFRASTRUCTURE_100_PASS' if ready else 'QGR_PROGRAMME_INFRASTRUCTURE_INCOMPLETE'}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--kmqgb-root',required=True);ap.add_argument('--output');a=ap.parse_args(argv);out=critique(Path(a.kmqgb_root));txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['readiness_100_boolean'] else 2
if __name__=='__main__':raise SystemExit(main())
