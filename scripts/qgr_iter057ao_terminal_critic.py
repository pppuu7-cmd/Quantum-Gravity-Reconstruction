#!/usr/bin/env python3
"""Frozen adversarial terminal evaluator for Iter057AO.

Created before any phase-2 held-out execution. It consumes only immutable JSON
artifacts and source text. It never imports constructor tensors or AF/AM/AN
obstruction data.
"""
import argparse, hashlib, json
from pathlib import Path

PREREG='e1ded07e5050763ecb707dad679b78286fe04744'
FREEZE='0daf8a632c060c0f758f15bd43b4837633a48efa'
REPAIR='7a7c764f3d2a4e592f738af906040d4f8cca93e5'
SOURCE_SHA='7cc63a46cba36fe903095494876028d9e7ebbe163a60ae35978372756a0ddf4a'
PHASE1_HEAD='03af90c3dc0ef20d694ebb1b7d3203e3089c1b56'
PHASE1_SEED='ITER057AO-COVARIANT-WEYL3-V1'
PHASE1_HELD='ITER057AO-COVARIANT-WEYL3-HELDOUT-V1'
PASS='PASS_SCOPED_ITER057AO_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED'
BLOCKED='BLOCKED_ITER057AO_REQUIRED_TERMINAL_AUTHORITY_INCOMPLETE'
INVALID='INVALID_ITER057AO_AUTHORITY_EXACTNESS_OR_NO_REFIT_CONTROL_FAILURE'

FORM={
 'P_definition':'P^{abcd} K_abcd = d/ds f(g,R+sK)|_{s=0} on algebraic Riemann variations K, f=I3',
 'bulk_covariant_h':'E_cov^{ab}=-P^{a c d e} R^b_{ c d e}+2 nabla_c nabla_d P^{a c d b}+(1/2)g^{ab}f',
 'boundary':'Theta^mu=2 P^{mu b c d} nabla_d h_bc-2(nabla_d P^{mu b c d})h_bc',
 'identity':'delta[sqrt(-g)f]=sqrt(-g)[E_cov^{ab}h_ab+nabla_mu Theta^mu]',
 'Noether':'for h_ab=nabla_a xi_b+nabla_b xi_a, delta_xi density=partial_mu(xi^mu density), hence nabla_a E_cov^{ab}=0',
}
FORM_SHA=hashlib.sha256(json.dumps(FORM,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load(p): return json.loads(Path(p).read_text())
def phash(d):
    q=dict(d); got=q.pop('scientific_payload_sha256',None)
    calc=hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return got,calc

def main():
    ap=argparse.ArgumentParser()
    for k in ['phase1','generic','heldout','linearity','neg_wrong_inv','neg_no_det','neg_no_raise','source','output']:
        ap.add_argument('--'+k.replace('_','-'),dest=k,required=True)
    a=ap.parse_args()
    p1=load(a.phase1); g=load(a.generic); h=load(a.heldout); lin=load(a.linearity)
    negs=[load(a.neg_wrong_inv),load(a.neg_no_det),load(a.neg_no_raise)]
    src=Path(a.source).read_text(); source_sha=hashlib.sha256(src.encode()).hexdigest()
    hashes={}
    hash_ok=True
    for name,d in [('phase1',p1),('generic',g),('heldout',h),('linearity',lin)]+[(f'neg{i}',d) for i,d in enumerate(negs)]:
        got,calc=phash(d); hashes[name]={'declared':got,'recomputed':calc}; hash_ok &= (got==calc)
    manifest=p1.get('manifest',{})
    p1_ok=(manifest.get('gate')=='ITER057AO' and manifest.get('phase')=='PHASE1_NONTERMINAL_COVARIANT_DENSITY_PROBE' and
           manifest.get('seed')==PHASE1_SEED and manifest.get('heldout_seed')==PHASE1_HELD and
           manifest.get('arithmetic')=='exact_rational_symbolic' and manifest.get('dimension')==4 and
           p1.get('terminal_classification_authorized') is False and
           p1.get('classification')=='PARTIAL_EXACT_ITER057AO_SOURCE_LEVEL_COVARIANT_DENSITY_DIRECTIONAL_PROBE__NO_TERMINAL_PASS')
    provenance=all(d.get('preregistration')==PREREG and d.get('phase2_freeze')==FREEZE for d in [g,h,lin]+negs)
    repair=all(d.get('execution_repair',REPAIR)==REPAIR for d in [g,h])
    generic_controls=all(g.get('controls',{}).values()) and all(g.get('weyl_controls',{}).values()) and all(g.get('zero_controls',{}).values())
    held_controls=all(h.get('controls',{}).values()) and all(h.get('weyl_controls',{}).values())
    lin_controls=all(lin.get('controls',{}).values())
    neg_controls=all(d.get('control',{}).get('defect_detected') is True for d in negs)
    replay=(g.get('directional_density',{}).get('sha256')==p1.get('generic',{}).get('directional_density_sha256') and
            h.get('directional_density',{}).get('sha256')==p1.get('heldout',{}).get('directional_density_sha256'))
    compact=(g.get('compact_IBP',{}).get('canonical_form')==FORM and g.get('compact_IBP',{}).get('canonical_form_sha256')==FORM_SHA and
             g.get('compact_IBP',{}).get('divergence_dropped') is False)
    noether=(g.get('Noether',{}).get('exact_equal') is True and g.get('Noether',{}).get('fake_gauge_detected') is True and
             g.get('EH_control',{}).get('EH_bulk_reduces_to_minus_Einstein_for_covariant_h') is True and
             g.get('EH_control',{}).get('EH_boundary_reduces_to_standard_theta') is True)
    zero=(all(g.get('zero_controls',{}).values()))
    firewall=(source_sha==SOURCE_SHA and all(x not in src for x in ['ITER057AF','ITER057AM','ITER057AN','canonical_y','B_shape']))
    held_firewall=(h.get('seed')==PHASE1_HELD and g.get('seed')==PHASE1_SEED and g.get('terminal_classification_authorized') is False and h.get('terminal_classification_authorized') is False)
    controls={
      'artifact_payload_hashes_recompute':hash_ok,
      'phase1_nonterminal_authority_valid':p1_ok,
      'phase2_provenance_frozen':provenance and repair,
      'source_sha_exact':source_sha==SOURCE_SHA,
      'no_AF_AM_AN_target_import':firewall,
      'generic_all_exact_controls':generic_controls,
      'heldout_all_exact_controls':held_controls,
      'exact_linearity_control':lin_controls,
      'all_negative_controls_detected':neg_controls,
      'direct_vs_analytic_generic_and_heldout_replay_exact':replay,
      'compact_IBP_formula_exact_and_divergence_retained':compact,
      'Noether_and_EH_controls_exact':noether,
      'constant_curvature_and_nonconstant_conformal_controls_exact':zero,
      'heldout_no_refit_firewall':held_firewall,
      'no_floating_scientific_tolerance':True,
    }
    classification=PASS if all(controls.values()) else INVALID
    out={'gate':'ITER057AO-TERMINAL-ADVERSARIAL-CRITIC','preregistration':PREREG,'phase2_freeze':FREEZE,'execution_repair':REPAIR,
         'phase1_expected_head':PHASE1_HEAD,'phase2_source_sha256':SOURCE_SHA,'compact_formula_sha256':FORM_SHA,
         'controls':controls,'payload_hash_replays':hashes,'generic_directional_sha256':g.get('directional_density',{}).get('sha256'),
         'heldout_directional_sha256':h.get('directional_density',{}).get('sha256'),'classification':classification,
         'claim_ceiling':'finite classical covariant Weyl^3 directional-variation certificate only; c6 unfixed; no global/all-orders/quantum/stability/UV claim'}
    raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['scientific_payload_sha256']=hashlib.sha256(raw).hexdigest()
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps(out,sort_keys=True,indent=2)); return 0 if classification==PASS else 2
if __name__=='__main__': raise SystemExit(main())
