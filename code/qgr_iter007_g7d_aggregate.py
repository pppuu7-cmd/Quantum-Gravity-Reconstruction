#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter007-g7d-results')
items=[json.loads(p.read_text()) for p in root.rglob('result.json')]
assert len(items)==4,len(items)
by={x['lane']:x for x in items}
need={'DIMENSIONLESS_MICRO_COUPLING_REPARAMETERIZATION','DIMENSIONLESS_HISTORY_EFFECT_FORM','VACUUM_GRAVITY_NORMALIZATION_AUDIT','DIMENSIONLESS_G_AUTHORITY_GUARD'}
assert set(by)==need,set(by)
assert 'ONE_DIMENSIONLESS' in by['DIMENSIONLESS_MICRO_COUPLING_REPARAMETERIZATION']['classification']
assert 'G_SQUARED' in by['DIMENSIONLESS_HISTORY_EFFECT_FORM']['classification']
assert 'DOES_NOT_OPERATIONALLY_CALIBRATE' in by['VACUUM_GRAVITY_NORMALIZATION_AUDIT']['classification']
assert by['DIMENSIONLESS_G_AUTHORITY_GUARD']['existing_rule_fixing_g_to_one_found'] is False
summary={
 'iteration':'007-G7D',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'PARTIAL_SCOPED_ABSOLUTE_SCALE_AMBIGUITY_REDUCED_TO_ONE_DIMENSIONLESS_MICROSCOPIC_COUPLING_G_KAPPA_OVER_HBAR__G_REMAINS_UNFIXED_AND_MATTER_CLOCK_CALIBRATION_OPEN',
 'definitions':['g=kappa/hbar','ell_Q^2=hbar/a_cont','h^2=c_geom*g*ell_Q^2'],
 'key_results':[
  'After continuum normalization, the h-kappa degeneracy is equivalent to one dimensionless microscopic action normalization g=kappa/hbar.',
  'The leading h^4 history comparator can be written as a preparation-dependent coefficient times c_geom^2 g^2 (ell_Q^2 R_eff)^2.',
  'Pure classical vacuum gravity does not operationally calibrate the overall Einstein-Hilbert coefficient because multiplying the vacuum action by a nonzero constant leaves the classical solution set unchanged.',
  'No authoritative current QGR rule fixes g to one or any other value; choosing units hbar=1 does not fix a dimensionless g.'
 ],
 'active_blocker':'MISSING_DERIVED_VALUE_OR_BOUND_FOR_G_AND_OPERATIONAL_MATTER_CLOCK_CALIBRATION',
 'recommended_next_gate':'G7E_RELATIONAL_MATTER_CLOCK_RECONSTRUCTION_OR_DISCRETE_GEOMETRIC_SPECTRUM',
 'claim_lock':'The unresolved freedom is one dimensionless microscopic coupling, not a proven new arbitrary length. Do not set g=1 by naturalness or units, and do not identify h with a Planck length until matter/clock normalization and c_geom are derived.'
}
Path('iter007-g7d-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))