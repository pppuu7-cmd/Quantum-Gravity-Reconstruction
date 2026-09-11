#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# A local curvature-generated history spread starts as C_prep * (h^2 R)^2.
# With h^2=c_geom*g*ell_Q^2 this becomes C_prep*c_geom^2*g^2*(ell_Q^2 R)^2.
gs=[0.1,0.3,1.0,3.0]
rows=[]
for g in gs:
    rows.append({'g':g,'history_coefficient_relative_to_g1':g*g})
out={
 'lane':'DIMENSIONLESS_HISTORY_EFFECT_FORM',
 'generic_leading_form':'loss = C_prep * (h^2 R_eff)^2 + higher order',
 'reparameterized_form':'loss = C_prep * c_geom^2 * g^2 * (ell_Q^2 R_eff)^2 + higher order',
 'rows':rows,
 'classification':'PASS_SCOPED_THE_ABSOLUTE_H4_BROADBAND_AMPLITUDE_CAN_BE_REWRITTEN_AS_A_G_SQUARED_MULTIPLIER_OF_A_GRAVITY_NORMALIZATION_CURVATURE_INVARIANT',
 'scientific_interpretation':'The unresolved finite-history amplitude is equivalent to one dimensionless coupling g squared multiplying the already-derived curvature/refinement structure. Preparation dependence remains in C_prep. This makes future phenomenological constraints naturally constraints on g rather than an independently postulated new length.',
 'guard':'R_eff denotes the curvature combination sampled by the specified wavepacket/history comparator; this lane is scaling structure, not a universal coefficient or detector prediction.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))