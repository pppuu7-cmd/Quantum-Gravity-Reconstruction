#!/usr/bin/env python3
"""Fail-closed validator for QGR candidate export v1. Infrastructure validity != science PASS."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'schemas'/'qgr_candidate_export_v1.schema.json'
LOCKS=[
 'qgr_theory_established','experimental_confirmation','beta_set_to_one_authorized',
 'qgr_six_derivative_coefficient_fixed','c6_running_authorized','strong_hyperbolicity_established',
 'physical_ghost_claim_authorized','quantum_unitarity_established','global_interacting_measure_established',
 'regulator_removal_established','uv_complete','new_physics_found','kmqgb_new_required_authorized']
CHAIN=['microscopic_object_id','dynamics_id','parameter_map_id','regulator_id','continuum_map_id','IR_realization_id','GR_map_id','observable_id']

def validate_candidate(record:dict)->dict:
    errors=[]; warnings=[]
    schema=json.loads(SCHEMA.read_text())
    errors += [f'schema:{e.message}' for e in Draft202012Validator(schema).iter_errors(record)]
    locks=record.get('claim_locks',{})
    for k in LOCKS:
        if locks.get(k) is not False:
            errors.append(f'current QGR export v1 requires claim lock {k}=false')
    if record.get('synthetic'):
        if record.get('scientific_candidate') is not False: errors.append('synthetic candidate cannot be scientific_candidate')
        if record.get('theory_claim_authorized') is not False: errors.append('synthetic candidate cannot authorize theory claim')
    if record.get('theory_claim_authorized') and not locks.get('qgr_theory_established'):
        errors.append('theory_claim_authorized inconsistent with theory lock')
    for p in record.get('parameters',[]):
        pid=str(p.get('id','')).lower(); val=p.get('value'); status=str(p.get('status',''))
        if pid=='beta' and val==1 and not locks.get('beta_set_to_one_authorized',False): errors.append('beta=1 unauthorized')
        if pid=='c6' and (val is not None or status not in {'SYMBOLIC_UNFIXED','UNFIXED','BLOCKED','UNKNOWN'}):
            if not locks.get('qgr_six_derivative_coefficient_fixed',False): errors.append('c6 numerically/fixed without authority')
    chain=record.get('same_realization_chain',{})
    if chain.get('status')=='PASS':
        if chain.get('candidate_version')!=record.get('candidate_version'): errors.append('same-realization candidate_version mismatch')
        missing=[k for k in CHAIN if not isinstance(chain.get(k),str) or not chain.get(k)]
        if missing: errors.append(f'same-realization PASS missing identity fields: {missing}')
    hashes=record.get('artifact_hashes')
    if not isinstance(hashes,dict) or not hashes: errors.append('artifact_hashes must be nonempty')
    if not record.get('benchmark_interface_version'): errors.append('benchmark interface version absent')
    if record.get('status')=='PASS' and record.get('blockers'): errors.append('PASS export cannot retain blockers')
    return {'valid':not errors,'errors':errors,'warnings':warnings,'scientific_status':record.get('status'),'promotion_authorized':bool(record.get('theory_claim_authorized')) and not errors}

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--output'); a=ap.parse_args(argv)
    rec=json.loads(Path(a.record).read_text()); out=validate_candidate(rec)
    text=json.dumps(out,sort_keys=True,indent=2); print(text)
    if a.output: Path(a.output).write_text(text+'\n')
    return 0 if out['valid'] else 1
if __name__=='__main__': raise SystemExit(main())
