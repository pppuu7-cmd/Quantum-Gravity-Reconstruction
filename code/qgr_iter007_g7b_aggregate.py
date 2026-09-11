#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter007-g7b-results')
items=[json.loads(p.read_text()) for p in root.rglob('result.json')]
assert len(items)==4,len(items)
by={x['lane']:x for x in items}
need={'HISTORY_PHASE_NORMALIZATION_NOFIX','KINEMATIC_MEASURE_SCALE_NOFIX','MINIMAL_SCALAR_MATTER_CENSUS','MULTISPECIES_UNIVERSALITY_COUNTERTEST'}
assert set(by)==need,set(by)
assert 'DO_NOT_FIX' in by['HISTORY_PHASE_NORMALIZATION_NOFIX']['classification']
assert 'SCALE_INVARIANT' in by['KINEMATIC_MEASURE_SCALE_NOFIX']['classification']
assert 'NOT_A_SECOND_ABSOLUTE_SCALE' in by['MINIMAL_SCALAR_MATTER_CENSUS']['classification']
assert 'DO_NOT_BY_THEMSELVES_DERIVE_UNIVERSAL' in by['MULTISPECIES_UNIVERSALITY_COUNTERTEST']['classification']
summary={
 'iteration':'007-G7B',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'BLOCKED_SCOPED_EXISTING_QGR_QUANTUM_NORMALIZATION_DOES_NOT_FIX_KAPPA_AND_METRIC_ONLY_MATTER_COVARIANCE_DOES_NOT_SUPPLY_A_DERIVED_SECOND_SCALE',
 'closed_in_scope':[
  'existing 24-history CPTP/isometry normalization is independent of the overall real action coefficient kappa',
  'existing Lorentzian configuration measure is exactly scale invariant and contains neither h nor kappa',
  'metric-only scalar covariance fixes the principal causal cone but leaves matter mass/nonminimal data independent',
  'shared metric causal cones do not by themselves derive multi-species universality or a second QGR scale relation'
 ],
 'key_results':[
  'The current quantum history normalization cannot quantize kappa: kappa enters only the real branch phase while the 1/sqrt(24) modulus fixes completeness.',
  'The kinematic measure |det G|^-5/2 d^10G has exactly zero homogeneity under G->s^2G and supplies no preferred scale.',
  'Minimal scalar matter coupling through G gives the same principal cone but field normalization is removable and mass/curvature couplings are independent data.',
  'Therefore neither of the two immediate G7B routes lifts the h-kappa degeneracy without adding a genuinely new microscopic symplectic/amplitude or matter-reconstruction principle.'
 ],
 'active_blocker':'MISSING_MICROSCOPIC_SYMPLECTIC_OR_AMPLITUDE_NORMALIZATION_AND_MATTER_RECONSTRUCTION_PRINCIPLE',
 'recommended_next_gate':'G7C_MICROSCOPIC_SYMPLECTIC_QUANTIZATION_OR_RELATIONAL_MATTER_RECONSTRUCTION',
 'claim_lock':'Do not infer kappa=hbar, h=l_P, or universal minimal matter coupling from the existing normalized history channel or configuration measure. Those structures are compatible with the current scale degeneracy.'
}
Path('iter007-g7b-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))