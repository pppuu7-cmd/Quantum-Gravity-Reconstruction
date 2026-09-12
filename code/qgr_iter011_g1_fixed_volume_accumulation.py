#!/usr/bin/env python3
import json
from qgr_iter011_g1_frechet_common import parity,slope
hs=[0.25,0.20,0.16,0.125,0.10,0.08]
k=0.04
rows=[]
for h in hs:
    p=parity(h,k)
    # In four dimensions a fixed coordinate four-volume contains O(h^-4) cells.
    rows.append({
      'h':h,
      'even_per_cell':p['even'],
      'odd_per_cell':p['odd'],
      'fixed_volume_even_proxy':p['even']/h**4,
      'fixed_volume_odd_proxy':p['odd']/h**4,
    })
even=[r['fixed_volume_even_proxy'] for r in rows]
odd=[r['fixed_volume_odd_proxy'] for r in rows]
# even tends to finite nonzero; odd must vanish ~h^2.
p_odd=slope(hs,odd)
assert abs(even[-1])>1e-5
assert abs(even[-1]-even[-2])<0.12*abs(even[-1])
assert abs(p_odd-2.0)<0.45,p_odd
assert abs(odd[-1])<0.2*abs(odd[0]),odd
out={
 'gate':'ITER011-G1-FIXED-VOLUME-ACCUMULATION',
 'rows':rows,
 'fixed_volume_odd_h_power':p_odd,
 'classification':'PASS_SCOPED_ON_THE_TEST_HYPERCUBE_THE_EVEN_TORSION_JACOBIAN_MEASURE_CORRECTION_HAS_A_FINITE_FIXED_VOLUME_LIMIT_WHILE_THE_ODD_CUBIC_PART_VANISHES_AS_H2',
 'interpretation':'The coarea determinant supplies a genuine continuum-surviving even real measure correction in this scoped family, whereas its odd/cubic curvature contribution is refinement-irrelevant at fixed four-volume and cannot provide the required finite Weyl^3 c6 target.',
 'guard':'Cell-count accumulation is a scaling audit, not yet a theorem for the correctly glued global coarea measure on shared variables.'
}
print(json.dumps(out,sort_keys=True))
