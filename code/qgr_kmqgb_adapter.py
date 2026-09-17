#!/usr/bin/env python3
"""Frozen QGR export v1 -> KMQGB Candidate Gravity record v1.3 adapter."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha256_bytes(b:bytes)->str:return hashlib.sha256(b).hexdigest()

def adapt(q:dict, export_sha256:str)->dict:
    blocked=list(q.get('blockers',[])) or ['QGR_SCIENCE_BLOCKED']
    sr=q.get('same_realization_chain',{})
    gates={f'G{i}':{'status':'BLOCKED','evidence_refs':[],'scope':'synthetic/future candidate intake'} for i in range(11)}
    rv={k:sr.get(k) for k in ['microscopic_object_id','dynamics_id','parameter_map_id','regulator_id','continuum_map_id','IR_realization_id','GR_map_id','observable_id']}
    return {
      'record_schema_version':'1.3','candidate_id':q['candidate_id'],
      'authority':{'parent_object_ref':None},'parent_dynamics':{'object_ref':None,'declared_domain':None},
      'parameters':q.get('parameters',[]),'escape_doors':['E1'],
      'escape_claim':'QGR prospective candidate intake; physical escape claim remains BLOCKED until independently established.',
      'escape_evidence_refs':q.get('source_provenance',[]),'door_specific_blockers':blocked,
      'upstream_primitives':[{'id':'qgr_microscopic_object','selection_status':'BLOCKED','load_bearing':True,'evidence_refs':[]}],
      'primitive_selection_law':'BLOCKED: QGR scientific primitive selection not established by infrastructure handshake.',
      'primitive_freedom_audit':{'status':'BLOCKED','evidence_refs':[]},
      'functional_freedom':{'classification':'UNKNOWN','hard_basis_cutoffs':[],'FF_D':[],'remaining_parent_dimension':None,'evidence_refs':[]},
      'same_realization':{'status':'BLOCKED','realization_vector':rv,'map_refs':[],'uncertainty_refs':[]},
      'observable_blocks':[{'id':'QGR_SYNTHETIC_OR_FUTURE_OBSERVABLE','completeness':{'status':'BLOCKED'}}],
      'comparators':[],'covariance':{'matrix_ref':None,'cross_block_correlations_included':True},
      'attribution_stack':{'qgr_export_sha256':export_sha256,'qgr_source_provenance':q.get('source_provenance',[])},
      'rigidity':{'holdout':{'shared_parameter_retuning_on_holdout':False}},'promotion_gates':gates,
      'compute_authorization':{'blocker_type':'STRUCTURAL','heavy_compute_authorized':False,'question_can_change_terminal_classification':False,'frozen_input_refs':[],'threshold_refs':[],'output_artifact':None},
      'publication_trace':{'claim_status':'OPEN_BLOCKED','permitted_claim':'Structurally valid QGR intake; scientific candidate remains BLOCKED.','evidence_refs':q.get('source_provenance',[]),'forbidden_claims':['QGR theory established','NEW_REQUIRED authorized','synthetic candidate is physical']},
      'promotion':{'ansatz_promoted':False,'robust_global_residual':False,'fisher_promoted':False,'resources_promoted':False},
      'qgr_adapter_version':'1.0.0','qgr_native_status':q.get('status'),'qgr_synthetic':q.get('synthetic'),
      'qgr_scientific_candidate':q.get('scientific_candidate'),'qgr_theory_claim_authorized':q.get('theory_claim_authorized'),
      'qgr_blockers':blocked,'qgr_claim_locks':q.get('claim_locks',{}),'qgr_artifact_hashes':q.get('artifact_hashes',{}),
      'qgr_benchmark_interface_version':q.get('benchmark_interface_version')}

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('output'); a=ap.parse_args(argv)
    raw=Path(a.input).read_bytes(); q=json.loads(raw); out=adapt(q,sha256_bytes(raw))
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'candidate_id':out['candidate_id'],'qgr_status':out['qgr_native_status'],'kmqgb_gate_statuses':sorted(set(v['status'] for v in out['promotion_gates'].values())),'export_sha256':out['attribution_stack']['qgr_export_sha256']},sort_keys=True))
    return 0
if __name__=='__main__':raise SystemExit(main())
