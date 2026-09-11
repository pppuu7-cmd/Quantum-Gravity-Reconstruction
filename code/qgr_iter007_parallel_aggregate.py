#!/usr/bin/env python3
import json
from pathlib import Path

rows=[]
for p in sorted(Path('iter007-parallel-results').rglob('result.json')):
    rows.append(json.loads(p.read_text()))
by={r['lane']:r for r in rows}
required={'FULL_NETWORK_RG','SEED_PHYSICAL_REPRESENTATION','COMPETING_OPERATOR_CENSUS','COHERENT_BEFORE_TRACE','PHYSICAL_SCALE_AUDIT'}
assert set(by)==required,(set(by),required)
assert by['FULL_NETWORK_RG']['classification'].startswith('PASS_SCOPED_')
assert by['SEED_PHYSICAL_REPRESENTATION']['classification'].startswith('PASS_SCOPED_')
assert by['COMPETING_OPERATOR_CENSUS']['classification'].startswith('PASS_SCOPED_')
assert by['COHERENT_BEFORE_TRACE']['classification'].startswith('PASS_SCOPED_')
assert by['PHYSICAL_SCALE_AUDIT']['classification'].startswith('PARTIAL_')

summary={
 'iteration':'007',
 'parallel_lanes':5,
 'lane_classifications':{k:by[k]['classification'] for k in sorted(by)},
 'key_results':[
   'Path-level h^3 suppression is not a full-network result: a cellwise traced O(h^4) channel is marginal under four-dimensional cell counting.',
   'Postponing the trace over independent product history registers gives exactly the same reduced channel as local tracing; no cancellation arises from delayed trace alone.',
   'The exact seed physical representation is 2 + 3 + 3prime, while ordering commutators are 3 + 3prime; a two-mode-only readout therefore requires a directional/fiber protocol or quadratic contraction.',
   'Parity-even local curvature-squared action ambiguity has two dynamical bulk directions modulo Gauss-Bonnet, but any unitary such correction preserves purity and cannot fake history-channel purity loss.',
   'The microscopic length h is not independently fixed because Newton matching leaves one dimensionless normalization kappa; nevertheless explicit h cancels in naive four-volume local-trace power counting.'
 ],
 'front_change':'The dominant uncertainty is no longer simple scale h. It is whether the physically correct projective quantum composition traces independent history registers locally over the 4D network, which would leave a marginal Lorentz-anisotropic continuum channel, or whether QGR derives a non-product cross-cell history identification that changes this scaling.',
 'claim_lock':'Do not claim a continuum decoherence prediction until the full network history composition and physical 2-mode readout map are derived. Do not insert cross-cell interference weights solely to cancel the marginal channel.',
 'recommended_next_gate':'G6A_FULL_NETWORK_HISTORY_COMPOSITION_AND_PHYSICAL_READOUT_MAP'
}
Path('iter007-parallel-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))
