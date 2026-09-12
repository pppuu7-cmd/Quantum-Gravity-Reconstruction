#!/usr/bin/env python3
import json
from fractions import Fraction

# On a fixed macroscopic causal interval T, serial microscopic depth scales as N~T/h.
# With regular per-cell relative branch generator O(h^2), the worst-case triangle bound is
# N * C h^2 = C T h ->0.  An O(c6 h^4) per-cell correction accumulates as O(c6 T h^3).
# This is a conservative coherent accumulation bound, not relying on stochastic cancellation.
T=Fraction(1)
rows=[]
for n in [8,16,32,64,128,256]:
 h=Fraction(1,n);N=n
 lead=N*h*h
 c6=N*h**4
 rows.append({'N':N,'h':str(h),'N_h2':str(lead),'N_h4':str(c6)})
assert rows[-1]['N_h2']=='1/256'
assert rows[-1]['N_h4']=='1/16777216'
out={
 'gate':'ITER009-G6-SERIAL-ACCUMULATION',
 'fixed_interval':'T=1 convention; N=T/h',
 'rows':rows,
 'leading_relative_accumulation':'O(T h)',
 'c6_accumulation':'O(c6 T h^3)',
 'classification':'PASS_SCOPED_UNDER_UNIFORM_REGULAR_PER_CELL_BOUNDS_FIXED_MACROSCOPIC_SERIAL_REFINEMENT_OF_OH2_BRANCH_SPREAD_AND_OH4_C6_CORRECTIONS_VANISHES_STRONGLY_AS_H_TO_ZERO',
 'guard':'Requires uniform local constants along the fixed macroscopic path and excludes singular/strong-curvature cells where the local implicit branch loses regularity.'
}
print(json.dumps(out,sort_keys=True))
