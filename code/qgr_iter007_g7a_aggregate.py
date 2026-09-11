#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter007-g7a-results')
items=[json.loads(p.read_text()) for p in root.rglob('result.json')]
assert len(items)==4,len(items)
by={x['lane']:x for x in items}
need={'MICRO_CONTINUUM_SCALE_POWER_COUNT','KAPPA_H_IDENTIFIABILITY','HISTORY_SCALE_REPARAMETERIZATION','NORMALIZATION_AUTHORITY_GUARD'}
assert set(by)==need,set(by)
assert by['MICRO_CONTINUUM_SCALE_POWER_COUNT']['continuum_kinetic_coefficient_h_power']==-2
assert by['KAPPA_H_IDENTIFIABILITY']['jacobian_rank']==1
assert by['NORMALIZATION_AUTHORITY_GUARD']['independent_micro_scale_fix_found_in_authoritative_chain'] is False
summary={
 'iteration':'007-G7A',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'BLOCKED_SCOPED_ABSOLUTE_MICROSCOPIC_SCALE_NOT_IDENTIFIABLE_FROM_CURRENT_QGR_NORMALIZATION_CHAIN',
 'matching':'a_cont = c_geom * kappa / h^2',
 'key_results':[
  'Four-dimensional refinement power counting fixes the continuum kinetic normalization through kappa/h^2.',
  'The continuum normalization map has rank one in the two microscopic variables (kappa,h), leaving h->lambda h and kappa->lambda^2 kappa unresolved.',
  'The leading broadband history effect changes as lambda^4 along that exact continuum-normalization degeneracy.',
  'The authoritative QGR chain still explicitly retains kappa as one free overall microscopic normalization; no later derived rule fixes the absolute physical h.'
 ],
 'active_blocker':'MISSING_DERIVED_MICROSCOPIC_NORMALIZATION_OR_SECOND_INDEPENDENT_PHYSICAL_SCALE_OBSERVABLE',
 'recommended_next_gate':'G7B_MICROSCOPIC_NORMALIZATION_PRINCIPLE_OR_MATTER_COUPLING_SECOND_SCALE',
 'claim_lock':'Do not identify h with the Planck length and do not set kappa to a physical value by convention. The current QGR predicts the dimensionless/refinement structure and h^4 order, while its absolute physical magnitude remains one-scale underdetermined.'
}
Path('iter007-g7a-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))