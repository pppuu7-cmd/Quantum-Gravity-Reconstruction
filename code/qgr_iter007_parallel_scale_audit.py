#!/usr/bin/env python3
import argparse, json

P=argparse.ArgumentParser(); P.add_argument('--output',required=True); args=P.parse_args()

# In natural units, the continuum Einstein-Hilbert coefficient a has dimension L^-2.
# For a cell of size h, int_cell d^4x R ~ h^4 R = h^2 * (h^2 R).
# If kappa is the dimensionless microscopic coefficient multiplying the dimensionless cell curvature h^2 R,
# then kappa = a h^2. With a = 1/(16 pi G_N), h^2 = 16 pi kappa G_N.
# QGR has fixed the relative nonlinear structure but has not independently fixed this absolute dimensionless kappa.

out={
 'lane':'PHYSICAL_SCALE_AUDIT',
 'continuum_action_coefficient_dimension':'L^-2',
 'dimensionless_cell_coupling_relation':'kappa = a h^2',
 'newton_matching_natural_units':'h^2 = 16 pi kappa G_N',
 'microscopic_h_independently_predicted':False,
 'remaining_absolute_normalization_freedom':'one dimensionless kappa unless a deeper quantum normalization fixes it',
 'path_observable_scale_dependence':'O(L h^3), therefore still depends on kappa^(3/2) after Newton matching',
 'four_volume_local_trace_power_counting':'explicit h cancels at leading O(h^4) per cell times O(h^-4) cells',
 'classification':'PARTIAL_H_NOT_INDEPENDENTLY_FIXED_FOR_PATH_OBSERVABLES_BUT_EXPLICIT_H_CANCELS_IN_NAIVE_4D_LOCAL_TRACE_DENSITY',
 'scientific_interpretation':'Newton matching alone fixes only the combination kappa/h^2. The microscopic length is not separately predicted. However, if the current local traced channel is applied cellwise across a four-volume, the leading bulk history correction is scale-marginal and its explicit h dependence cancels, making the unresolved h less relevant but the continuum anisotropic channel more serious.',
 'guard':'The exact numerical bulk coefficient still requires the physical representation/readout map and a derived rule establishing that the local channel is the correct four-volume composition.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
