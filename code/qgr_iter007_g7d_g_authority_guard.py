#!/usr/bin/env python3
import argparse,json
from pathlib import Path
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
g5=Path('results/ITER003_G5_PAIR_ACTION.md').read_text()
g7a=Path('results/ITER007_G7A_MICROSCOPIC_SCALE_IDENTIFIABILITY.md').read_text()
assert 'The only free coefficient is the overall normalization `kappa`' in g5
assert 'h -> lambda h' in g7a
out={
 'lane':'DIMENSIONLESS_G_AUTHORITY_GUARD',
 'g_definition':'g=kappa/hbar',
 'authoritative_free_kappa_confirmed':True,
 'existing_rule_fixing_g_to_one_found':False,
 'classification':'BLOCKED_SCOPED_CURRENT_QGR_LEAVES_ONE_DIMENSIONLESS_MICROSCOPIC_ACTION_NORMALIZATION_G_UNFIXED',
 'scientific_interpretation':'Rewriting the scale ambiguity as g=kappa/hbar clarifies but does not remove it. The authoritative action construction explicitly retained kappa as its sole overall normalization, and the existing quantum channel/measure results do not supply a condition g=1 or any other value.',
 'guard':'Do not invoke naturalness or units hbar=1 as a physical derivation of g=1. Setting hbar=1 changes units, whereas g is dimensionless and remains a physical model parameter unless further constrained.'
}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))