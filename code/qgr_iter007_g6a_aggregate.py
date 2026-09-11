#!/usr/bin/env python3
import json
from pathlib import Path
rows=[json.loads(p.read_text()) for p in sorted(Path('iter007-g6a-results').rglob('result.json'))]
by={r['lane']:r for r in rows};req={'JOINT_HISTORY_LAW','POSET_COMPOSITION','SPATIAL_FACTORIZATION'}
assert set(by)==req,(set(by),req)
assert by['JOINT_HISTORY_LAW']['classification'].startswith('BLOCKED_')
assert by['POSET_COMPOSITION']['classification'].startswith('PASS_SCOPED_')
assert by['SPATIAL_FACTORIZATION']['classification'].startswith('PASS_SCOPED_')
out={
 'iteration':'007-G6A',
 'lanes':3,
 'classifications':{k:by[k]['classification'] for k in sorted(by)},
 'conclusions':[
   'Local uniform 1/24 history marginals do not determine cross-cell correlations: exact countermodels permit cancellation, product accumulation, or enhancement.',
   'Two natural Boolean completions that are already compatible with the B4 language (serial ordinal sum and disjoint B8 global order) give product-uniform local order pairs, not cancellation.',
   'The earlier h^0 four-volume counting is an extensive/global warning, not by itself a local observable theorem: in a spatial tensor-factor toy local reduced purity recovers as h^3 while global -log purity remains O(1).'
 ],
 'front_change':'Network composition is underdetermined by current local history normalization. Natural uncorrelated Boolean compositions support product local histories, but observable scaling depends on the field-support/factorization map. A local continuum Lorentz-violation claim is therefore not authorized.',
 'next_gate':'G6B_DERIVE_OVERLAPPING_CELL_GLUING_AND_FIELD_SUPPORT_FROM_CCRC',
 'claim_lock':'Do not choose anticorrelated histories to cancel noise and do not identify extensive global purity with a local experimental decoherence probability.'
}
Path('iter007-g6a-summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
