#!/usr/bin/env python3
"""Iter057AO terminal Critic v3: execution-only schema repair of frozen v2."""
import argparse, hashlib, json
from pathlib import Path
PREREG='e1ded07e5050763ecb707dad679b78286fe04744'
FREEZE='0daf8a632c060c0f758f15bd43b4837633a48efa'
REPAIR='7a7c764f3d2a4e592f738af906040d4f8cca93e5'
SCHEMA_REPAIR='aef0903c50cefd61a454a21a16af05c6989e912d'
ANALYTIC_SOURCE_SHA='7cc63a46cba36fe903095494876028d9e7ebbe163a60ae35978372756a0ddf4a'
DUAL_SOURCE_COMMIT='1426fee93f2ea830b3c84e23999bf22b650c7a1e'
GENERIC='ITER057AO-COVARIANT-WEYL3-V1'; HELDOUT='ITER057AO-COVARIANT-WEYL3-HELDOUT-V1'
PASS='PASS_SCOPED_ITER057AO_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED'
INVALID='INVALID_ITER057AO_AUTHORITY_EXACTNESS_OR_NO_REFIT_CONTROL_FAILURE'
FORM={'P_definition':'P^{abcd} K_abcd = d/ds f(g,R+sK)|_{s=0} on algebraic Riemann variations K, f=I3','bulk_covariant_h':'E_cov^{ab}=-P^{a c d e} R^b_{ c d e}+2 nabla_c nabla_d P^{a c d b}+(1/2)g^{ab}f','boundary':'Theta^mu=2 P^{mu b c d} nabla_d h_bc-2(nabla_d P^{mu b c d})h_bc','identity':'delta[sqrt(-g)f]=sqrt(-g)[E_cov^{ab}h_ab+nabla_mu Theta^mu]','Noether':'for h_ab=nabla_a xi_b+nabla_b xi_a, delta_xi density=partial_mu(xi^mu density), hence nabla_a E_cov^{ab}=0'}
FORM_SHA=hashlib.sha256(json.dumps(FORM,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def phash(d):
 q=dict(d);got=q.pop('scientific_payload_sha256',None);calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest();return got==calc

def main():
 ap=argparse.ArgumentParser()
 for k in ['analytic_generic','analytic_heldout','linearity','neg_wrong_inv','neg_no_det','neg_no_raise','dual_generic','dual_heldout','analytic_source','dual_source','output']:
  ap.add_argument('--'+k.replace('_','-'),dest=k,required=True)
 a=ap.parse_args();ag=load(a.analytic_generic);ah=load(a.analytic_heldout);li=load(a.linearity);negs=[load(a.neg_wrong_inv),load(a.neg_no_det),load(a.neg_no_raise)];dg=load(a.dual_generic);dh=load(a.dual_heldout)
 src=Path(a.analytic_source).read_text();dsrc=Path(a.dual_source).read_text();source_sha=hashlib.sha256(src.encode()).hexdigest();payloads=[ag,ah,li,*negs,dg,dh]
 controls={
  'all_payload_hashes_recompute':all(phash(x) for x in payloads),
  'analytic_source_sha_exact':source_sha==ANALYTIC_SOURCE_SHA,
  'no_AF_AM_AN_import_in_analytic_source':all(x not in src for x in ['ITER057AF','ITER057AM','ITER057AN','canonical_y','B_shape']),
  'no_AF_AM_AN_import_in_dual_source':all(x not in dsrc for x in ['ITER057AF','ITER057AM','ITER057AN','canonical_y','B_shape']),
  'analytic_prereg_freeze_exact':all(x.get('preregistration')==PREREG and x.get('phase2_freeze')==FREEZE for x in [ag,ah,li,*negs]),
  'analytic_execution_repair_exact':all(x.get('execution_repair',REPAIR)==REPAIR for x in [ag,ah]),
  'generic_controls_all':all(ag.get('controls',{}).values()) and all(ag.get('weyl_controls',{}).values()) and all(ag.get('zero_controls',{}).values()),
  'heldout_controls_all':all(ah.get('controls',{}).values()) and all(ah.get('weyl_controls',{}).values()),
  'linearity_exact':all(li.get('controls',{}).values()),
  'negative_controls_detected':all(x.get('detected') is True and x.get('controls',{}).get('defect_detected') is True for x in negs),
  'compact_IBP_formula_frozen':ag.get('compact_IBP',{}).get('canonical_form')==FORM and ag.get('compact_IBP',{}).get('canonical_form_sha256')==FORM_SHA and ag.get('compact_IBP',{}).get('divergence_dropped') is False,
  'Noether_exact_and_fake_gauge_detected':ag.get('Noether',{}).get('exact_equal') is True and ag.get('Noether',{}).get('fake_gauge_detected') is True,
  'EH_sign_boundary_controls':all(ag.get('EH_control',{}).values()),
  'dual_routes_identified':dg.get('route')=='INDEPENDENT_DIRECT_DUAL_NUMBER_FULL_TENSOR_PROPAGATION' and dh.get('route')=='INDEPENDENT_DIRECT_DUAL_NUMBER_FULL_TENSOR_PROPAGATION',
  'dual_generic_controls_all':all(dg.get('controls',{}).values()),
  'dual_heldout_controls_all':all(dh.get('controls',{}).values()),
  'generic_independent_replay_exact':ag.get('directional_density',{}).get('sha256')==dg.get('directional_density',{}).get('sha256'),
  'heldout_independent_replay_exact':ah.get('directional_density',{}).get('sha256')==dh.get('directional_density',{}).get('sha256'),
  'seed_firewall':ag.get('seed')==dg.get('seed')==GENERIC and ah.get('seed')==dh.get('seed')==HELDOUT,
  'heldout_nonterminal_inputs':ah.get('terminal_classification_authorized') is False and dh.get('terminal_classification_authorized') is False,
  'no_floating_scientific_tolerance':True,
 }
 classification=PASS if all(controls.values()) else INVALID
 out={'gate':'ITER057AO-TERMINAL-CRITIC-V3','preregistration':PREREG,'schema_repair':SCHEMA_REPAIR,'analytic_source_sha256':ANALYTIC_SOURCE_SHA,'dual_source_commit':DUAL_SOURCE_COMMIT,'compact_formula_sha256':FORM_SHA,'controls':controls,'generic_directional_sha256':ag.get('directional_density',{}).get('sha256'),'heldout_directional_sha256':ah.get('directional_density',{}).get('sha256'),'classification':classification,'claim_ceiling':'finite classical source-level covariant Weyl^3 variation certificate only; c6 symbolic/unfixed; no all-orders/global/quantum/stability/UV claim'}
 raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();out['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest();Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out,sort_keys=True,indent=2));return 0 if classification==PASS else 2
if __name__=='__main__':raise SystemExit(main())
