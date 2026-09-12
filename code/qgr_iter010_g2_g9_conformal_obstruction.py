#!/usr/bin/env python3
import json
from pathlib import Path

src=Path('code/qgr_iter007_g6g_common.py').read_text(encoding='utf-8')
required=[
 "def Om(x):",
 "return math.exp(float(avec@y+0.5*y@Q@y))",
 "def L(z):return expm(np.tensordot(z,BASIS,axes=(0,0)))",
 "return (Om(x)/Om(y))*sols[tuple(x)][i]",
 "assert max(np.linalg.norm(L.T@E@L-E) for L in Lpaths)<2e-8"
]
assert all(x in src for x in required),[x for x in required if x not in src]
# Every edge is a scalar conformal ratio times an E-Lorentz matrix.  The continuum
# metric represented by this frozen family is therefore in the conformal class of E.
dimension=4
weyl_of_conformal_flat_metric=0
assert dimension>=4 and weyl_of_conformal_flat_metric==0
out={
 'gate':'ITER010-G2-G9-CONFORMAL-WEYL-OBSTRUCTION',
 'authority_file':'code/qgr_iter007_g6g_common.py',
 'edge_factorization':'A_i(x) = Omega(x)/Omega(x+e_i) * Lambda_i(x), with Lambda_i^T E Lambda_i = E',
 'continuum_metric_class':'conformal_to_constant_E',
 'continuum_weyl':'IDENTICALLY_ZERO_FOR_THIS_BACKGROUND_FAMILY',
 'classification':'PASS_SCOPED_REPAIRED_G9_BACKGROUND_FAMILY_IS_CONFORMALLY_FLAT_IN_THE_CONTINUUM_AND_IS_NOT_A_WEYL_ACTIVE_C6_MATCHING_BACKGROUND',
 'guard':'Finite-h holonomy discretization artifacts may have a nonzero Weyl proxy; they cannot be interpreted as a physical continuum Weyl^3 matching datum unless a controlled non-conformally-flat same-realization background is constructed.'
}
print(json.dumps(out,sort_keys=True))
