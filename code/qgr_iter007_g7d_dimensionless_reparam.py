#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# a_cont has units action/length^2, kappa has units action, h has units length.
# Define ell_Q^2 = hbar/a_cont and g=kappa/hbar. Then h^2=c_geom*g*ell_Q^2.
examples=[0.01,0.1,1.0,10.0,100.0]
rows=[]
for g in examples:
    h2_over_c_ell2=g
    h4_over_c2_ell4=g*g
    rows.append({'g_kappa_over_hbar':g,'h2_over_cgeom_ellQ2':h2_over_c_ell2,'h4_over_cgeom2_ellQ4':h4_over_c2_ell4})
out={
 'lane':'DIMENSIONLESS_MICRO_COUPLING_REPARAMETERIZATION',
 'definitions':['g=kappa/hbar','ell_Q^2=hbar/a_cont'],
 'matching':'h^2 = c_geom * g * ell_Q^2',
 'rows':rows,
 'classification':'PASS_SCOPED_AFTER_CONTINUUM_NORMALIZATION_THE_H_KAPPA_DEGENERACY_IS_EQUIVALENT_TO_ONE_DIMENSIONLESS_MICROSCOPIC_COUPLING_G_KAPPA_OVER_HBAR',
 'scientific_interpretation':'Once the continuum gravitational normalization and hbar are regarded as fixed physical inputs, the unresolved microscopic scale is not an independent arbitrary dimensionful length: it is equivalent to the dimensionless action normalization g=kappa/hbar. A finite physical cell size would be h=sqrt(c_geom g) ell_Q. Current QGR does not fix g.',
 'guard':'ell_Q is only a normalization-derived gravity length. Do not identify it or h with a convention-specific Planck length until matter/units and c_geom are operationally fixed.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))