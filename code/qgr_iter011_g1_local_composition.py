#!/usr/bin/env python3
import itertools,json,numpy as np
import qgr_iter010_g3_common as g3
from qgr_iter011_g1_common import flat_subtracted

# Audit whether the already-derived local Jacobian factor behaves as a simple
# cell-product weight under one dyadic subdivision.  This is deliberately a
# diagnostic, not an assumed composition law: shared-boundary factors may
# require a separate gluing/coarea treatment.
rows=[]
for h in (0.25,0.125):
    coarse=flat_subtracted(h,0.08)
    fine=[]
    for off in itertools.product([0,1],repeat=4):
        y0=g3.RMI@((h/2.0)*np.asarray(off,float))
        fine.append(flat_subtracted(h/2.0,0.08,y0))
    fine_sum=float(sum(r['delta_sum_logabsdet'] for r in fine))
    rows.append({
      'h_coarse':h,'coarse_delta_log_weight':-coarse['delta_sum_logabsdet'],
      'sum_16_fine_delta_log_weight':-fine_sum,
      'composition_defect':float((-coarse['delta_sum_logabsdet'])-(-fine_sum)),
      'relative_defect':float(abs(coarse['delta_sum_logabsdet']-fine_sum)/(abs(coarse['delta_sum_logabsdet'])+abs(fine_sum)+1e-30)),
      'min_sv_all':min([coarse['min_sv']]+[r['min_sv'] for r in fine]),
      'max_residual_all':max([coarse['max_residual']]+[r['max_residual'] for r in fine]),
    })
out={
 'gate':'ITER011-G1-LOCAL-JACOBIAN-COMPOSITION-DIAGNOSTIC',
 'rows':rows,
 'classification':'NAIVE_CELL_PRODUCT_COMPOSITION_TEST_ONLY',
 'guard':'A nonzero defect is not a scientific failure: the finite-branch coarea measure lives on glued/shared variables, so duplicated boundary Jacobians must not be assumed to factorize cellwise.'
}
print(json.dumps(out,sort_keys=True))
