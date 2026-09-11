#!/usr/bin/env python3
import glob,json
files=glob.glob('iter007-g6g-results/*/*.json')+glob.glob('iter007-g6g-results/*.json')
D={}
for f in files:
 try:
  x=json.load(open(f));D[x['lane']]=x
 except Exception:pass
need={'RELATIVE_LORENTZ_HOLONOMY_INVARIANTS','CENTRAL_RAY_WIGNER_SPIN2','NARROW_PACKET_DETECTOR_COMPARATOR'}
missing=need-set(D);assert not missing,missing
assert D['RELATIVE_LORENTZ_HOLONOMY_INVARIANTS']['classification'].startswith('NUMERICALLY_VERIFIED_SCOPED')
assert D['CENTRAL_RAY_WIGNER_SPIN2']['classification'].startswith('NUMERICALLY_VERIFIED_SCOPED')
assert D['NARROW_PACKET_DETECTOR_COMPARATOR']['classification'].startswith('NUMERICALLY_VERIFIED_SCOPED')
out={
 'iteration':'007-G6G','parallel_lanes':3,'aggregate_success':True,
 'closed_in_scope':[
  'basis-invariant relative Lorentz-holonomy Lie-generator and quadratic Casimir scaling on repaired G9',
  'central-ray little-group/Wigner transport on the two physical QGR-L1 modes in a specified relational detector frame',
  'one normalized specified narrow-packet linear-polarization comparator combining envelope and polarization overlap factors'
 ],
 'key_results':[
  'Relative branch Lorentz generators are O(h^2); both quadratic Lorentz-algebra Casimirs and the finite trace defect are O(h^4).',
  'In a specified barycentric detector/standard section, branch Wigner-angle spread is O(h^2), so a fixed linear spin-2 polarization pair-overlap loss is O(h^4).',
  'A normalized exponential envelope plus fixed linear polarization in the narrow-packet approximation yields a combined history-mixture loss with h^4 scaling on repaired G9.',
  'The coefficient remains preparation/readout dependent. The robust model-side statement is the refinement order and derived finite holonomy structure, not a universal decoherence constant.'
 ],
 'holonomy_slopes':D['RELATIVE_LORENTZ_HOLONOMY_INVARIANTS']['log_h_slopes'],
 'wigner_slopes':D['CENTRAL_RAY_WIGNER_SPIN2']['log_h_slopes'],
 'comparator_slopes':D['NARROW_PACKET_DETECTOR_COMPARATOR']['log_h_slopes'],
 'active_blocker':'BLOCKED_MISSING_EXACT_BROADBAND_MOMENTUM_DEPENDENT_TWO_MODE_WIGNER_INTEGRATION_AND_ABSOLUTE_MICROSCOPIC_H_KAPPA_SEPARATION_FOR_PHENOMENOLOGY',
 'recommended_next_gate':'G6H_BROADBAND_COHERENT_TWO_MODE_INTEGRAL_OR_STOP_ITER007_AT_SCOPED_COMPARATOR',
 'claim_lock':'Do not promote the narrow-packet comparator to a universal QGR decoherence prediction. Its detector/linear-polarization choice is explicit and its Wigner angle uses a fixed standard section. The basis-invariant Lorentz Casimirs are model-side observables; the quantum comparator coefficient is preparation/readout dependent. Absolute h remains open.',
 'lane_classifications':{k:D[k]['classification'] for k in sorted(need)}
}
open('iter007-g6g-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
