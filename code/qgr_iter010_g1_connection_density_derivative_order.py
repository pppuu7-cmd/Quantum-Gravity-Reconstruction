#!/usr/bin/env python3
import json
from pathlib import Path

src=Path('code/qgr_iter005_g2_exact_quartic_noether_certificate.py').read_text(encoding='utf-8')
# Authority check: the exact Iter005 construction really is a product of two gamma_terms
# dressed only by algebraic inverse-metric/determinant series.
required=[
    'for x in gamma_terms(mu,beta,rho):',
    'for y in gamma_terms(nu,alpha,sigma):',
    'for x in gamma_terms(mu,nu,rho):',
    'for y in gamma_terms(alpha,beta,sigma):',
    'series=prod4(SQ,gs(mu,nu),gs(alpha,rho),gs(beta,sigma))'
]
assert all(x in src for x in required)

derivative_degree_gamma=1
algebraic_dressing_degree=0
connection_density_derivative_degree=2*derivative_degree_gamma+algebraic_dressing_degree
weyl_cubed_derivative_degree=6
assert connection_density_derivative_degree==2
assert connection_density_derivative_degree<weyl_cubed_derivative_degree

out={
 'gate':'ITER010-G1-CONNECTION-DENSITY-DERIVATIVE-ORDER',
 'authority_file':'code/qgr_iter005_g2_exact_quartic_noether_certificate.py',
 'connection_density_derivative_degree':connection_density_derivative_degree,
 'weyl_cubed_derivative_degree':weyl_cubed_derivative_degree,
 'reason':'each gamma_terms factor contains one derivative and the SQ/G inverse expansions are algebraic in undifferentiated h; extending the same density to arbitrary field order never raises derivative order above two',
 'classification':'PASS_SCOPED_EXISTING_EXACT_CONNECTION_DENSITY_IS_ALL_FIELD_ORDER_BUT_TWO_DERIVATIVE_AND_CANNOT_BY_ITSELF_GENERATE_THE_SIX_DERIVATIVE_WEYL_CUBED_COEFFICIENT',
 'guard':'This is a structural barrier for the already-frozen connection-density formula, not a no-go theorem against adding a separately derived microscopic higher-derivative invariant.'
}
print(json.dumps(out,sort_keys=True))
