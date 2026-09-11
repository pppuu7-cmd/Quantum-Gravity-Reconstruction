#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
d=4
# q/G is dimensionless as a metric/response variable. One finite first difference obeys Dq ~ h*dq.
# The quadratic cell action has two first differences and the cell count per fixed volume scales h^-d.
difference_power=2
cell_count_power=-d
total_h_power=difference_power+cell_count_power
assert total_h_power==-2
out={
 'lane':'MICRO_CONTINUUM_SCALE_POWER_COUNT',
 'spacetime_dimension':d,
 'finite_difference_power':difference_power,
 'cell_density_power':cell_count_power,
 'continuum_kinetic_coefficient_h_power':total_h_power,
 'matching_form':'a_cont = c_geom * kappa / h^2',
 'classification':'PASS_SCOPED_DIMENSIONAL_REFINEMENT_MATCHING_FIXES_CONTINUUM_NORMALIZATION_ONLY_THROUGH_KAPPA_OVER_H2',
 'scientific_interpretation':'For the already-derived dimensionless response field, Dq~h partial q while the number of four-cells in fixed physical four-volume scales h^-4. Therefore kappa sum(Dq)^2 tends to (c_geom kappa/h^2) integral(partial q)^2. The geometric constant can in principle be fixed by the detailed cell-to-continuum convention, but the h exponent is not optional.',
 'guard':'This is a scaling theorem, not the yet-uncomputed exact c_geom normalization coefficient and not an identification h=Planck length.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))