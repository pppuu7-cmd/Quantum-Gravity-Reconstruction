#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Two scalar species can share the same metric principal cone yet carry distinct allowed masses/nonminimal couplings.
species=[
 {'name':'A','Z':1.0,'m2':1.0,'xi':0.0},
 {'name':'B','Z':3.0,'m2':7.0,'xi':0.2},
]
# Canonical field rescaling removes Z but leaves distinct m2/Z and xi/Z.
for s in species:
    s['canonical_m2']=s['m2']/s['Z'];s['canonical_xi']=s['xi']/s['Z']
assert species[0]['canonical_m2']!=species[1]['canonical_m2']
assert species[0]['canonical_xi']!=species[1]['canonical_xi']
out={
 'lane':'MULTISPECIES_UNIVERSALITY_COUNTERTEST',
 'species':species,
 'shared_principal_cone':'k_a G^{ab} k_b = 0 in the massless/high-frequency limit',
 'classification':'BLOCKED_SCOPED_PULLBACK_COVARIANCE_AND_SHARED_METRIC_CONE_DO_NOT_BY_THEMSELVES_DERIVE_UNIVERSAL_MATTER_NORMALIZATION_OR_A_SECOND_QGR_SCALE_RELATION',
 'scientific_interpretation':'Two matter species can obey the same metric covariance and high-frequency causal cone while retaining different canonically meaningful mass and curvature-coupling data. Therefore the gravitational G-sector alone does not derive the universality needed to use a matter parameter as an internal second scale. A genuine matter reconstruction/equivalence-principle theorem is required.',
 'guard':'The counterexample is structural: it shows non-uniqueness under the present assumptions, not that universality is impossible after adding a new prospectively derived microscopic matter principle.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))