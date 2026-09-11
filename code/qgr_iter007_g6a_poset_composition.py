#!/usr/bin/env python3
import argparse,json,itertools,math
from collections import Counter
P=argparse.ArgumentParser();P.add_argument('--output',required=True);a=P.parse_args()
P4=list(itertools.permutations(range(4)))
# Serial ordinal-sum of two B4 cells: all four first-cell generator additions precede all four second-cell additions.
serial=24*24
assert serial==576
# Concurrent disjoint refinement represented by B8: 8! maximal chains. Restriction to each four-label subset.
all8=itertools.permutations(range(8))
counts=Counter()
for p in all8:
 left=tuple(x for x in p if x<4)
 right=tuple(x-4 for x in p if x>=4)
 counts[(left,right)]+=1
assert len(counts)==24*24
assert set(counts.values())=={math.comb(8,4)}
concurrent=math.factorial(8)
assert concurrent==40320 and math.comb(8,4)==70
# The restrictions to the two local B4 cells are exactly product-uniform despite a single global ordering.
out={
 'lane':'POSET_COMPOSITION',
 'single_B4_maximal_chains':24,
 'two_cell_serial_ordinal_sum_maximal_chains':serial,
 'two_disjoint_B4_as_B8_global_maximal_chains':concurrent,
 'B8_interleavings_per_pair_of_local_orders':70,
 'distinct_pairs_of_local_orders':len(counts),
 'local_order_pair_distribution_under_uniform_B8_global_chain':'exact product-uniform',
 'classification':'PASS_SCOPED_NATURAL_SERIAL_AND_DISJOINT_BOOLEAN_COMPOSITIONS_DO_NOT_GENERATE_CANCELLING_LOCAL_ORDER_CORRELATIONS',
 'scientific_interpretation':'For an ordinal-sum causal chain the two local orders are freely chosen (24^2). For a disjoint concurrent B8 completion a single global order adds 70 interleavings for every local-order pair, so the local restrictions are still independent uniform permutations. Merely promoting to a larger global Boolean order therefore does not create the anticorrelation needed to cancel the local history covariance.',
 'guard':'Adjacent overlapping cells with shared microscopic events are not fixed by the current local B4 specification and require a separate gluing rule.'
}
open(a.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
