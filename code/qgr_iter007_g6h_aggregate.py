#!/usr/bin/env python3
import json
from pathlib import Path
root=Path('iter007-g6h-results')
items=[]
for p in root.rglob('result.json'):
    items.append(json.loads(p.read_text()))
assert len(items)==4,len(items)
by={x['lane']+(':'+x.get('profile','') if x['lane']=='BROADBAND_COHERENT_TWO_MODE_PROFILE' else ''):x for x in items}
val=next(x for x in items if x['lane']=='BROADBAND_ENVELOPE_VALIDATION')
prof=[x for x in items if x['lane']=='BROADBAND_COHERENT_TWO_MODE_PROFILE']
pol=next(x for x in items if x['lane']=='BROADBAND_POLARIZATION_PREPARATION_DEPENDENCE')
assert sorted(x['profile'] for x in prof)==['m0','m1']
assert all(3.65<x['log_h_slope']<4.35 for x in prof)
assert all(v['max_abs_error_vs_exact']<2e-6 for v in val['profile_validation'].values())
assert all(3.6<s<4.4 for s in pol['log_h_slopes'].values())
summary={
 'iteration':'007-G6H',
 'parallel_lanes':4,
 'aggregate_success':True,
 'closed_in_scope':[
  'cutoff-free broadband null-cone angular integration validated against exact G6F envelope overlaps',
  'full momentum-dependent little-group/spin-2 integration for two normalized radial packet profiles',
  'full broadband preparation-dependence audit across envelope-only, linear and helicity states'
 ],
 'profile_slopes':{x['profile']:x['log_h_slope'] for x in prof},
 'polarization_slopes':pol['log_h_slopes'],
 'key_results':[
  'The radial future-null-cone integral can be done analytically; no arbitrary UV momentum cutoff enters the normalized comparator.',
  'For every null direction and every history the momentum-dependent Wigner element is recomputed, so the G6G narrow-packet approximation is removed.',
  'Both m0 and m1 coherent two-mode broadband mixture losses scale as h^4 on repaired G9.',
  'Envelope-only, linear-polarization and helicity preparations share the h^4 refinement order but have preparation-dependent coefficients.'
 ],
 'active_blocker':'BLOCKED_ABSOLUTE_MICROSCOPIC_H_KAPPA_SCALE_AND_REAL_DETECTOR_MATTER_COUPLING_COMPARATOR',
 'recommended_next_gate':'G7A_MICROSCOPIC_SCALE_OR_MATTER_DETECTOR_COUPLING_CLOSURE',
 'claim_lock':'Do not call the broadband coefficient universal and do not convert h into a physical length/time without a derived h/kappa map. G6H closes a normalized model-side broadband comparator for specified preparations, not experimental phenomenology.'
}
Path('iter007-g6h-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))