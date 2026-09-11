#!/usr/bin/env python3
import argparse,json
from pathlib import Path
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
g5=Path('results/ITER003_G5_PAIR_ACTION.md').read_text()
g1=Path('results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md').read_text()
assert 'The only free coefficient is the overall normalization `kappa`' in g5
assert 'overall normalization/coupling: `1` (`kappa`)' in g5
assert 'the already fixed QGR quadratic normalization fixes `a`' in g1
# "fixes a" is relative to the inherited quadratic normalization; it is not an independent microscopic scale theorem.
out={
 'lane':'NORMALIZATION_AUTHORITY_GUARD',
 'iter003_g5_confirms_free_overall_kappa':True,
 'iter007_g1_inherits_quadratic_normalization':True,
 'independent_micro_scale_fix_found_in_authoritative_chain':False,
 'classification':'BLOCKED_SCOPED_AUTHORITATIVE_QGR_CHAIN_STILL_CONTAINS_ONE_FREE_OVERALL_MICROSCOPIC_NORMALIZATION_AND_NO_DERIVED_ABSOLUTE_H_RULE',
 'scientific_interpretation':'The later all-orders Einstein-Hilbert-like action inherits the quadratic normalization; it does not remove the explicitly retained microscopic overall kappa. Therefore setting kappa=1 and simultaneously reading h as a physical Planck length would add a convention/hypothesis not derived by the current chain.',
 'guard':'A future microscopic amplitude normalization, measure theorem, matter coupling, or independent observable may fix kappa or h. This guard only forbids pretending that such a result already exists.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))