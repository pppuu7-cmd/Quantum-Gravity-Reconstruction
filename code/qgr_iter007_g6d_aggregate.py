#!/usr/bin/env python3
from pathlib import Path
import json
rows=[json.loads(p.read_text()) for p in sorted(Path('iter007-g6d-results').rglob('result.json'))]
by={r['lane']:r for r in rows}
required={'CURVED_NULL_BUNDLE_GRAM','NULL_CONE_MEASURE','SEED_EUCLIDEAN_QUOTIENT_NORM_COVARIANCE','CONDITIONAL_HISTORY_MIXTURE_PURITY_IDENTITY'}
assert set(by)==required,(set(by),required)
assert 3.7<by['CURVED_NULL_BUNDLE_GRAM']['offdiag_gram_rms_log_h_slope']<4.3
assert by['NULL_CONE_MEASURE']['exact_null_transport_checks']>=3
assert by['SEED_EUCLIDEAN_QUOTIENT_NORM_COVARIANCE']['classification'].startswith('FAIL_SCOPED_')
assert by['CONDITIONAL_HISTORY_MIXTURE_PURITY_IDENTITY']['branch_permutation_invariant'] is True
summary={
 'iteration':'007-G6D',
 'parallel_lanes':len(rows),
 'lane_classifications':{k:v['classification'] for k,v in sorted(by.items())},
 'key_results':[
  'The 24 curved G9 histories send one source null covector to 24 null covectors in the same target Lorentzian cone. The branch-symmetric common-target Gram scalar k_p^T G_target^-1 k_q is frame invariant, nonzero, and scales approximately h^4 (four-scale fit exponent about 3.85).',
  'The exact null-pair identity k_p B k_q = -1/2 (k_p-k_q) B (k_p-k_q) explains why the first invariant branch-separation scalar is quadratic in the O(h^2) momentum-fiber separation.',
  'The target null cone has a canonical invariant integration density sqrt(|det G^-1|) d4k delta(k^T G^-1 k) theta_future, with the metric determinant factor cancelling the finite-frame momentum Jacobian.',
  'The simple positive Euclidean quotient norm used on the symmetric seed is not covariant under generic finite QGR frame pullback. It cannot be silently promoted to the curved physical one-particle norm.',
  'If a common positive curved physical pairing is later derived, equal 1/24 history weights imply the exact basis-free purity identity P=24^-2 sum_pq |<psi_p|psi_q>|^2 with no new decoherence coefficient.'
 ],
 'closed_in_scope':[
  'common-target branch-symmetric characteristic null-bundle geometry',
  'invariant null-cone integration density',
  'scoped rejection of the seed Euclidean quotient norm as a generic covariant physical norm',
  'conditional exact branch-overlap purity formula'
 ],
 'still_open':[
  'positive covariant generic curved physical pairing/one-particle norm on the 2D quotient fibers',
  'construction of branch wavepackets as states or positive functionals with detector/preparation normalization',
  'numerical local two-mode purity on G9',
  'analytic interacting boundary-relative measure disintegration for overlapping regions',
  'absolute microscopic h/kappa separation for phenomenology',
  'independent KMQGB pass'
 ],
 'active_blocker':'BLOCKED_MISSING_POSITIVE_COVARIANT_CURVED_PHYSICAL_PAIRING_AND_INTERACTING_BOUNDARY_MEASURE_DISINTEGRATION',
 'recommended_next_gate':'G6E_CURVED_PHYSICAL_PAIRING_OR_OPERATIONAL_PURITY_WITHOUT_VECTOR_INNER_PRODUCT',
 'claim_lock':'Do not use the seed Euclidean quotient norm as the curved physical norm, do not report the conditional branch-overlap identity as a numerical QGR prediction, and do not call null-bundle Gram spread decoherence.'
}
Path('iter007-g6d-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,sort_keys=True))
