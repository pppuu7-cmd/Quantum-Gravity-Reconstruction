#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# With only the already-derived metric G and a real scalar phi, locality and pullback covariance
# allow at two derivative order: Z G^{ab} d_a phi d_b phi, m^2 phi^2 and xi R phi^2
# (plus higher powers in the potential if admitted). Canonical field rescaling removes Z but not m or xi.
raw_couplings=['Z','m2','xi']
canonical_physical=['m2_over_Z','xi_over_Z']
principal_symbol='Z * G^{-1}'
# Any nonzero Z gives the same matter characteristic cone; Z cannot provide a second geometric scale.
out={
 'lane':'MINIMAL_SCALAR_MATTER_CENSUS',
 'assumptions':['one real scalar matter probe','local pullback covariance','only emergent G as rank-2 background','at most two derivatives in equations/action sector audited'],
 'raw_allowed_couplings':raw_couplings,
 'after_canonical_field_rescaling':canonical_physical,
 'principal_symbol':principal_symbol,
 'characteristic_cone':'k_a G^{ab} k_b = 0 for massless/high-frequency scalar, independent of nonzero Z',
 'classification':'PARTIAL_SCOPED_METRIC_ONLY_COVARIANCE_FIXES_THE_MATTER_PRINCIPAL_CONE_BUT_NOT_A_SECOND_ABSOLUTE_SCALE_OR_UNIVERSAL_SUBLEADING_COUPLINGS',
 'scientific_interpretation':'If matter is assumed to couple only through the emergent metric, covariance fixes the scalar kinetic tensor up to an overall field normalization, so its high-frequency causal cone coincides with the QGR metric cone. But the field normalization is removable, while the mass and curvature coupling are independent matter data. Consequently this minimal matter sector supplies no QGR-derived equation that separates h from kappa.',
 'guard':'This is a coupling census, not a derivation that all physical matter must obey minimal metric coupling. Universality/equivalence-principle behavior is a separate gate.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))