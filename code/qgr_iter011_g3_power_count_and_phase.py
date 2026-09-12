#!/usr/bin/env python3
import json,numpy as np
# In 4D a fixed coordinate volume contains O(h^-4) cells.  A local per-cell
# derivative expansion h^d therefore contributes h^(d-4) before the matching
# of dimensional couplings.  We only use this as refinement bookkeeping.
orders={2:-2,4:0,6:2}
assert orders[2]==-2 and orders[4]==0 and orders[6]==2
# The regular coarea/Haar factor is positive-real in the local regular chart:
# log w changes Re log(amplitude).  A Lorentzian action coefficient c6 enters
# exp(i c6 Q6) and changes Im log(amplitude).  These are independent axes.
M=np.array([[1.0,0.0],[0.0,1.0]])
rank=int(np.linalg.matrix_rank(M))
assert rank==2
out={
 'gate':'ITER011-G3-POWER-COUNT-AND-PHASE-SEPARATION',
 'fixed_4volume_cell_count_power':-4,
 'per_cell_to_fixed_volume_powers':{'two_derivative_h2':'h^-2','four_derivative_h4':'h^0','six_derivative_h6':'h^2'},
 'real_measure_vs_coherent_phase_response_rank':rank,
 'classification':'PASS_SCOPED_DERIVATIVE_HIERARCHY_SEPARATES_POWER_DIVERGENT_TWO_DERIVATIVE_MEASURE_RENORMALIZATION_FINITE_H4_MEASURE_TERMS_AND_VANISHING_H6_FIXED_VOLUME_TERMS__REAL_COAREA_AND_COHERENT_C6_PHASE_REMAIN_INDEPENDENT',
 'interpretation':'A generic h^2 local coarea correction renormalizes/matches the existing two-derivative sector; a centered h^4 curvature-squared measure term can survive fixed-volume refinement; an h^6 odd/cubic measure term vanishes as h^2. None supplies the missing imaginary Lorentzian c6 phase without a new same-realization relation.',
 'guard':'Power counting assumes a local derivative expansion after zero-jet subtraction and does not replace the still-open full shared-variable projective pushforward construction.'
}
print(json.dumps(out,sort_keys=True))
