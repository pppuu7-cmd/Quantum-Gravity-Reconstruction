#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter008-g1-results')
items=[json.loads(p.read_text()) for p in root.rglob('result.json')]
assert len(items)==4,len(items)
by={x['lane']:x for x in items}
need={'BOOLEAN_RANK_CLOCK_UNIQUENESS','BOOLEAN_RANK_CLOCK_CAUSALITY','BOOLEAN_RANK_CLOCK_SERIAL_COMPOSITION','BOOLEAN_RANK_CLOCK_DUAL_FREQUENCY'}
assert set(by)==need,set(by)
assert by['BOOLEAN_RANK_CLOCK_UNIQUENESS']['solution_dimension_after_f0_zero_and_disjoint_additivity']==1
assert by['BOOLEAN_RANK_CLOCK_CAUSALITY']['transverse_sum_zero_dimension']==3
assert by['BOOLEAN_RANK_CLOCK_SERIAL_COMPOSITION']['all_single_cell_rank_profiles_identical'] is True
assert 'DOES_NOT_FIX' in by['BOOLEAN_RANK_CLOCK_DUAL_FREQUENCY']['classification']
summary={
 'iteration':'008-G1',
 'parallel_lanes':4,
 'aggregate_success':True,
 'classification':'PASS_SCOPED_INTRINSIC_BOOLEAN_RANK_CLOCK_DERIVED_UNIQUELY_IN_ADDITIVE_S4_CLASS_WITH_TIMELIKE_1_PLUS_3_CAUSAL_STRUCTURE_AND_EXACT_SERIAL_COMPOSITION__PHYSICAL_TICK_SCALE_REMAINS_OPEN',
 'key_results':[
  'Within S4-invariant scalar functions, zero-at-empty plus disjoint-union additivity leaves a one-dimensional space spanned by Boolean rank; unit elementary increment fixes tau(S)=|S|.',
  'The rank gradient is the unique S4-symmetric timelike direction of the C/E seed, with a three-dimensional negative-definite sum-zero transverse sector; fixed-rank levels are antichains.',
  'All 24 maximal histories share the exact rank profile 0,1,2,3,4, and rank time adds exactly across true serial B4 cells.',
  'The serial integer clock has compact dual U(1) quasi-frequency, but conversion to physical energy still requires a tick duration; the clock does not by itself fix h or g.'
 ],
 'active_blocker':'MISSING_DYNAMICAL_OR_OPERATIONAL_CALIBRATION_OF_THE_INTRINSIC_RANK_CLOCK_AND_NO_DERIVED_NONZERO_GEOMETRIC_STOP_SCALE',
 'recommended_next_gate':'G2_RELATIONAL_CLOCK_DYNAMICS_AND_COUPLING_TO_QGR_GEOMETRY',
 'claim_lock':'The Boolean rank clock is an intrinsic dimensionless ordering clock, not yet physical proper time. Do not identify one rank tick with a Planck time or use its compact dual phase to set g by convention.'
}
Path('iter008-g1-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))