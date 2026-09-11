#!/usr/bin/env python3
import argparse,json
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# In pure vacuum classical gravity, multiplying the full Einstein-Hilbert action by nonzero a
# does not change the zero set of the Euler-Lagrange equations: a E[G]=0 iff E[G]=0.
coeffs=[0.1,1.0,3.0,100.0]
# Test representative equation residual values symbolically/numerically.
residuals=[-2.0,-0.3,0.0,0.7,4.0]
rows=[]
for a in coeffs:
    zero_equiv=all(((abs(a*r)<1e-15)==(abs(r)<1e-15)) for r in residuals)
    assert zero_equiv
    rows.append({'a':a,'same_vacuum_zero_set':zero_equiv})
out={
 'lane':'VACUUM_GRAVITY_NORMALIZATION_AUDIT',
 'rows':rows,
 'classification':'BLOCKED_SCOPED_PURE_CLASSICAL_VACUUM_GRAVITY_DOES_NOT_OPERATIONALLY_CALIBRATE_THE_OVERALL_EINSTEIN_HILBERT_NORMALIZATION',
 'scientific_interpretation':'For nonzero a, the vacuum equation a E[G]=0 has exactly the same solutions as E[G]=0. The overall gravitational normalization becomes operational through quantum amplitudes and, especially, through its relative coupling to matter/rods/clocks. Since QGR has not yet reconstructed a universal matter sector, treating a_cont as an internally calibrated Newton constant is stronger than the current pure-gravity result.',
 'guard':'This does not make a_cont meaningless: it controls quantum phase normalization and would control sourced equations once a matter normalization is fixed. It shows why matter/clock reconstruction is part of absolute-scale closure.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))