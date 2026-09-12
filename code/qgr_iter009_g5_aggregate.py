#!/usr/bin/env python3
import json
from pathlib import Path

root=Path('iter009-g5-results')
records=[json.loads(p.read_text()) for p in sorted(root.rglob('*.json'))]
assert len(records)==6,len(records)
summary={
  'iteration':'009-G5',
  'parallel_lanes':6,
  'aggregate_success':True,
  'key_results':[
    'If the self-consistent c6 correction to branch generators is regular O(h^4), while the already verified branch-relative generator is O(h^2), the quadratic history-mixture loss is O(h^4) with first c6 dependence only at O(h^6).',
    'Any c6-induced common unitary geometry shift leaves mixture purity exactly invariant.',
    'Absolute coherent propagation observables can still respond linearly to a common O(h^4)c6 shift, so c6 decoupling is specific to history-mixture purity and related relative observables.',
    'The repaired-G9 branch-relative Lorentz generator remains numerically O(h^2) down to h=1/64 with bounded h^-2-rescaled RMS on the tested sequence.',
    'Using exact G6F overlap formulas, the specified normalized m0/m1 packet state distance is O(h^2) when relative rapidity is O(h^2), yielding a summable dyadic strong-state bound.',
    'Operator-norm convergence is not necessary for strong convergence of continuous unitary representations; full-Hilbert QGR strong convergence nevertheless remains unproved beyond the specified packet domain.'
  ],
  'classification':'PASS_SCOPED_LEADING_OH4_HISTORY_MIXTURE_PURITY_IS_C6_INDEPENDENT_UNDER_REGULAR_SELF_CONSISTENT_OH4_C6_GEOMETRY_CORRECTIONS__SPECIFIED_G6F_PACKET_DOMAIN_HAS_SUMMABLE_STRONG_REFINEMENT_CONTROL__ABSOLUTE_COHERENT_C6_RESPONSE_AND_FULL_DOMAIN_LIMIT_REMAIN_OPEN',
  'active_blocker':'MISSING_MICROSCOPIC_C6_VALUE_FOR_ABSOLUTE_COHERENT_CURVED_OBSERVABLES_AND_A_DENSE_OR_FULL_PHYSICAL_DOMAIN_STRONG_LIMIT_BEYOND_THE_SPECIFIED_PACKET_FAMILY',
  'recommended_next_gate':'G6_DENSE_DOMAIN_STRONG_LIMIT_AND_MICROSCOPIC_C6_IDENTIFIABILITY_DECISION',
  'claim_lock':'The leading G6H history-mixture loss remains one-parameter only under the regular O(h^4) c6 geometry-correction assumption; do not generalize this to absolute coherent observables or claim c6 is fixed.'
}
print(json.dumps(summary,sort_keys=True))
Path('iter009-g5-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
