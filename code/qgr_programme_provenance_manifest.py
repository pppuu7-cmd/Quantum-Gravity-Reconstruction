#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.metadata,json,os,platform,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TRACKED={
 'completion_contract':'protocol/QGR_PROGRAMME_READINESS_100_CONTRACT.json',
 'completion_preregistration':'preregistration/QGR_PROGRAMME_INFRASTRUCTURE_100_COMPLETION.md',
 'primary_validator':'code/qgr_programme_readiness_validator.py','independent_critic':'code/qgr_programme_readiness_critic.py',
 'gate_registry':'protocol/QGR_GATE_REGISTRY.json','export_schema':'schemas/qgr_candidate_export_v1.schema.json',
 'candidate_validator':'code/qgr_candidate_export_validator.py','kmqgb_adapter':'code/qgr_kmqgb_adapter.py',
 'synthetic_candidate':'synthetic/qgr_synthetic_blocked_candidate_v1.json','negative_candidate':'synthetic/qgr_malformed_candidate_v1.json',
 'recovery_manifest':'recovery/CLEAN_SESSION_RECOVERY_MANIFEST.json','bundle_manifest':'release/QGR_PROGRAMME_BUNDLE_CONTENTS.json'}
def h(p:Path):return hashlib.sha256(p.read_bytes()).hexdigest()
def build(kroot:Path,bundle:Path|None,adapted:Path|None):
    pin=json.loads((ROOT/'protocol/QGR_KMQGB_INTERFACE_PIN.json').read_text())
    out={'qgr_head':subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip(),'completion_contract_commit':'cf528fb6cd9f21611ca7f04ca5fb488fcd506359','file_sha256':{k:h(ROOT/v) for k,v in TRACKED.items()},'kmqgb_pin':pin,'python_version':platform.python_version(),'jsonschema_version':importlib.metadata.version('jsonschema'),'github_run_id':os.getenv('GITHUB_RUN_ID'),'github_run_attempt':os.getenv('GITHUB_RUN_ATTEMPT'),'github_workflow':os.getenv('GITHUB_WORKFLOW')}
    if kroot:
      out['kmqgb_observed_commit']=subprocess.check_output(['git','-C',str(kroot),'rev-parse','HEAD'],text=True).strip()
    if bundle:out['bundle_sha256']=h(bundle);out['bundle_size']=bundle.stat().st_size
    if adapted:out['adapted_package_sha256']=h(adapted)
    return out
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--kmqgb-root',required=True);ap.add_argument('--bundle');ap.add_argument('--adapted');ap.add_argument('--output',required=True);a=ap.parse_args(argv);out=build(Path(a.kmqgb_root),Path(a.bundle) if a.bundle else None,Path(a.adapted) if a.adapted else None);Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out,sort_keys=True,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
