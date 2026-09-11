#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter007-g7c-results')
items=[json.loads(p.read_text()) for p in root.rglob('result.json')]
assert len(items)==4,len(items)
by={x['lane']:x for x in items}
need={'REGULATOR_VERSUS_PHYSICAL_SCALE_FORK','CONTINUOUS_GEOMETRY_SCALE_AUDIT','COTANGENT_PREQUANTIZATION_NOFIX','B4_COMBINATORIAL_SCALE_AUDIT'}
assert set(by)==need,set(by)
assert 'VANISHES_AS_H4' in by['REGULATOR_VERSUS_PHYSICAL_SCALE_FORK']['classification']
assert 'NO_DERIVED_MINIMUM' in by['CONTINUOUS_GEOMETRY_SCALE_AUDIT']['classification']
assert 'CANNOT_QUANTIZE_KAPPA' in by['COTANGENT_PREQUANTIZATION_NOFIX']['classification']
assert 'NOT_AN_ABSOLUTE_PHYSICAL_CELL_LENGTH' in by['B4_COMBINATORIAL_SCALE_AUDIT']['classification']
summary={
 'iteration':'007-G7C',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'BLOCKED_SCOPED_CURRENT_CCRC_QGR_HAS_NO_DERIVED_NONZERO_STOP_SCALE__H_IS_EITHER_REMOVED_REGULATOR_WITH_VANISHING_H4_EFFECT_OR_REQUIRES_A_NEW_PHYSICAL_DISCRETENESS_PRINCIPLE',
 'key_results':[
  'Keeping the continuum GR normalization fixed while h->0 forces kappa~h^2 and makes the normalized history correction vanish as h^4.',
  'The current Lorentzian configuration space is continuous and its invariant measure has no minimum nonzero geometric scale.',
  'The naive canonical cotangent prequantization route cannot quantize kappa because the canonical symplectic form is exact.',
  'B4 incidence, history counts and S4 combinatorics are dimensionless and unchanged under a global physical rescaling of h.'
 ],
 'physical_fork':{
  'regulator_interpretation':'h->0; local finite-history effect vanishes; scoped local continuum is GR',
  'physical_discreteness_interpretation':'h>0; requires a prospectively derived stopping/spectrum/clock/amplitude principle not yet present'
 },
 'active_blocker':'MISSING_DERIVED_PHYSICAL_DISCRETENESS_OR_RELATIONAL_CLOCK_MATTER_SCALE_PRINCIPLE',
 'recommended_next_gate':'G7D_DISCRETE_GEOMETRY_SPECTRUM_OR_RELATIONAL_CLOCK_MATTER_RECONSTRUCTION',
 'claim_lock':'Do not describe h as a fundamental minimum length in the current QGR. No nonzero stop scale has been derived; if h is only a regulator the h^4 beyond-GR effect disappears in the continuum.'
}
Path('iter007-g7c-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))