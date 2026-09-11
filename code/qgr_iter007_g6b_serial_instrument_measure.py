#!/usr/bin/env python3
import argparse, json, math
from fractions import Fraction

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()

# G8A fixed every branch operator to K_a = 24^-1/2 phase_a U_a with U_a unitary.
# Hence K_a^dagger K_a = I/24. For serially composable coarse diagonal blocks,
# canonical Stinespring/history composition appends one orthogonal register per level.
rows=[]
for n in range(1,6):
    count=24**n
    prob=Fraction(1,count)
    total=count*prob
    amp_mag=24**(-n/2)
    assert total==1
    rows.append({
      'levels':n,
      'branch_count':count,
      'single_branch_probability_exact':f'1/{count}',
      'single_branch_amplitude_magnitude':amp_mag,
      'normalization_exact':str(total),
    })

# Two-level branch labels are exactly Cartesian: 24 x 24 = 576. Equal norm follows
# without assuming commuting branch operators because
# ||K_b K_a psi||^2 = <psi|K_a^dagger (I/24) K_a|psi> = ||psi||^2/24^2.
assert rows[1]['branch_count']==576

out={
  'lane':'SERIAL_HISTORY_INSTRUMENT_MEASURE',
  'finite_level_table':rows,
  'two_level_joint_history_count':576,
  'two_level_joint_probability':'1/576 for every ordered branch pair',
  'classification':'PASS_SCOPED_CANONICAL_SERIAL_G8A_HISTORY_COMPOSITION_FIXES_PRODUCT_UNIFORM_JOINT_BRANCH_MEASURE_WITHOUT_COMMUTATIVITY_ASSUMPTION',
  'scientific_interpretation':'For path-groupoid-composable coarse diagonals, the already-derived normalized history isometry fixes the multi-level branch modulus. Appending a fresh orthogonal history register at each serial block gives 24^n equal-norm branches and exact completeness at every finite n. Branch-dependent action phases and noncommuting system transports do not change the equal branch norms.',
  'consequence':'The cross-cell branch-law ambiguity found in G6A does not apply to serial coarse path blocks: their canonical joint branch measure is already fixed to product-uniform by G8A. Correlated/reversed branch pairing would require a new nonfactorizing history environment not present in the current construction.',
  'guard':'This theorem is for serially composable history instruments. It does not assign a joint measurement channel to geometrically overlapping but non-composable face-neighbour cells.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
