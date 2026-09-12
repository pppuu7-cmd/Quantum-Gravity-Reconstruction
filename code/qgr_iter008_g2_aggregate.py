#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter008-g2-results')
items=[json.loads(p.read_text()) for p in root.rglob('result.json')]
assert len(items)==4,len(items)
by={x['lane']:x for x in items}
need={'RANK_CONDITIONED_PREFIX_TRANSITION_LAW','SEQUENTIAL_HISTORY_ISOMETRY_FACTORIZATION','CLOCK_CONDITIONED_EDGE_TRANSPORT_COMPOSITION','INTRINSIC_CLOCK_PHASE_FREEDOM'}
assert set(by)==need,set(by)
assert by['RANK_CONDITIONED_PREFIX_TRANSITION_LAW']['history_count']==24
assert abs(by['SEQUENTIAL_HISTORY_ISOMETRY_FACTORIZATION']['product_amplitude_modulus']-24**-0.5)<1e-14
assert by['CLOCK_CONDITIONED_EDGE_TRANSPORT_COMPOSITION']['max_prefix_suffix_composition_error']<1e-12
assert by['INTRINSIC_CLOCK_PHASE_FREEDOM']['S4_clock_only_physical_phase_dimension']==0
summary={
 'iteration':'008-G2',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'PASS_SCOPED_INTRINSIC_RANK_CLOCK_GIVES_EXACT_SEQUENTIAL_BRANCH_MEASURE_AND_ISOMETRY_FACTORIZATION_COMPATIBLE_WITH_PATH_COMPOSITION__CLOCK_ALONE_HAS_NO_NONTRIVIAL_PHYSICAL_PHASE',
 'key_results':[
  'Conditioning the uniform 24-history measure on rank gives exact next-direction probabilities 1/(4-r) and uniform binomial rank-slice endpoints.',
  'The global 1/sqrt(24) history modulus factorizes exactly into one-tick isometries 1/sqrt(4),1/sqrt(3),1/sqrt(2),1.',
  'Rank-conditioned prefixes/suffixes are exactly compatible with the established path-groupoid composition law.',
  'A clock-only S4-invariant edge phase is completely removable by rank-slice vertex rephasings; the scalar clock alone cannot supply a physical phase or fix g.'
 ],
 'active_blocker':'MISSING_NONTRIVIAL_CLOCK_GEOMETRY_OR_MATTER_DYNAMICAL_COUPLING_WITH_FIXED_NORMALIZATION',
 'recommended_next_gate':'G3_CLOCK_CONDITIONED_QGR_DYNAMICS_AND_RELATIONAL_MATTER_EXTENSION',
 'claim_lock':'The intrinsic clock refines the history instrument but does not add an autonomous Hamiltonian or set the physical tick duration/g. Nontrivial phases remain supplied by the geometric QGR action/connection sector.'
}
Path('iter008-g2-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))