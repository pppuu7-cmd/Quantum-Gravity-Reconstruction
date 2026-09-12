#!/usr/bin/env python3
import json
from qgr_iter011_g1_frechet_common import parity,slope
hs=[0.25,0.20,0.16,0.125,0.10,0.08]
k=0.04
rows=[parity(h,k) for h in hs]
even=[r['even'] for r in rows];odd=[r['odd'] for r in rows]
p_even=slope(hs,even);p_odd=slope(hs,odd)
ce=[r['even']/(k*k*h**4) for r,h in zip(rows,hs)]
co=[r['odd']/(k**3*h**6) for r,h in zip(rows,hs)]
assert abs(p_even-4.0)<0.15,p_even
assert abs(p_odd-6.0)<0.45,p_odd
# Exclude an h^4 Weyl^3-like odd contribution: odd/(k^3 h^4) must decay ~h^2.
odd_h4=[r['odd']/(k**3*h**4) for r,h in zip(rows,hs)]
assert abs(odd_h4[-1]) < 0.2*abs(odd_h4[0]),odd_h4
out={
 'gate':'ITER011-G1-ODD-CUBIC-H-SCALING',
 'rows':rows,
 'even_h_power':p_even,
 'odd_h_power':p_odd,
 'even_coeff_over_kappa2_h4':ce,
 'odd_coeff_over_kappa3_h6':co,
 'odd_over_kappa3_h4':odd_h4,
 'classification':'PASS_SCOPED_TORSION_JACOBIAN_EVEN_CURVATURE_RESPONSE_STARTS_AT_KAPPA2_H4_WHILE_THE_ODD_CUBIC_RESPONSE_STARTS_AT_KAPPA3_H6_NOT_KAPPA3_H4',
 'guard':'On this Weyl-active weak tidal family, the odd/cubic Jacobian contribution is two refinement powers too suppressed to be the required cell h^4 Weyl^3 phase datum.'
}
print(json.dumps(out,sort_keys=True))
