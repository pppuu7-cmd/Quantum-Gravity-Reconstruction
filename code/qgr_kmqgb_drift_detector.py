#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def h(p:Path):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(kroot:Path,simulate=False):
    pin=json.loads((ROOT/'protocol/QGR_KMQGB_INTERFACE_PIN.json').read_text())
    observed={
      'kmqgb_commit':subprocess.check_output(['git','-C',str(kroot),'rev-parse','HEAD'],text=True).strip(),
      'schema_sha256':h(kroot/pin['schema_path']),'template_sha256':h(kroot/pin['template_path']),
      'validator_sha256':h(kroot/pin['validator_path']),'base_validator_sha256':h(kroot/pin['base_validator_path'])}
    s=json.loads((kroot/'recovery/state.json').read_text()); observed['rqir_core_version']=str(s['rqir_core']['version']); observed['rqir_core_status']=str(s['rqir_core']['status'])
    if simulate: observed['schema_sha256']='0'*64
    expected={k:pin[k] for k in observed}
    mismatch={k:{'expected':expected[k],'observed':v} for k,v in observed.items() if expected[k]!=v}
    return {'valid':not mismatch,'classification':'KMQGB_INTERFACE_PIN_MATCH' if not mismatch else 'KMQGB_INTERFACE_VERSION_DRIFT','mismatch':mismatch,'observed':observed}
def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--kmqgb-root',required=True);ap.add_argument('--simulate-drift',action='store_true');ap.add_argument('--output');a=ap.parse_args(argv)
    out=check(Path(a.kmqgb_root),a.simulate_drift); txt=json.dumps(out,sort_keys=True,indent=2);print(txt)
    if a.output:Path(a.output).write_text(txt+'\n')
    return 0 if out['valid'] else 3
if __name__=='__main__':raise SystemExit(main())
