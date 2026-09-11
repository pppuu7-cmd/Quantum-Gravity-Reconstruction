#!/usr/bin/env python3
import glob,json
files=glob.glob('iter007-g6f-results/*/*.json')+glob.glob('iter007-g6f-results/*.json')
D={}
for f in files:
 try:
  x=json.load(open(f));D[x['lane']]=x
 except Exception:pass
need={'COMMON_CHARACTERISTIC_HILBERT','NORMALIZED_PACKET_OVERLAP_IDENTITIES','REPAIRED_G9_ENVELOPE_PURITY'}
missing=need-set(D);assert not missing,missing
assert D['COMMON_CHARACTERISTIC_HILBERT']['classification'].startswith('PASS_SCOPED')
assert D['NORMALIZED_PACKET_OVERLAP_IDENTITIES']['classification'].startswith('PASS_SCOPED')
assert D['REPAIRED_G9_ENVELOPE_PURITY']['classification'].startswith('NUMERICALLY_VERIFIED_SCOPED')
out={
 'iteration':'007-G6F','parallel_lanes':3,'aggregate_success':True,
 'closed_in_scope':[
  'common positive target characteristic direct-integral Hilbert for regular one-particle/readout sector',
  'finite regular history-branch isometry on that characteristic Hilbert',
  'two analytically normalized Lorentz-covariant null-envelope preparation families with exact overlap functions',
  'convention-repaired G9 normalized characteristic-envelope impurity benchmark through five refinement scales'
 ],
 'key_results':[
  'Invariant future-null-cone measure plus the positive covariant two-mode quotient pairing define a common target characteristic Hilbert; finite QGR frame transports act isometrically.',
  'For psi~exp(-alpha u.k), normalized overlap is 2/(1+gamma); for psi~(u.k)exp(-alpha u.k), overlap is 4(2+gamma)/(3(1+gamma)^2). Alpha cancels exactly.',
  'On repaired G9, normalized envelope impurity scales h^4 for both profiles, while the asymptotic numerical coefficient differs by exactly the analytic 4/3 ratio.',
  'Therefore the h^4 order is robust across these benchmark preparations but the absolute coefficient is not a preparation-independent theory number.'
 ],
 'g9_slopes':D['REPAIRED_G9_ENVELOPE_PURITY']['log_h_slopes'],
 'profile_loss_ratio':D['REPAIRED_G9_ENVELOPE_PURITY']['asymptotic_profile_loss_ratio_m1_over_m0'],
 'active_blocker':'BLOCKED_MISSING_FULL_COHERENT_TWO_POLARIZATION_WAVEPACKET_HOLONOMY_AND_CONCRETE_DETECTOR_PREPARATION_PLUS_ABSOLUTE_H_KAPPA_SEPARATION',
 'recommended_next_gate':'G6G_PHYSICAL_POLARIZATION_WIGNER_HOLONOMY_AND_DETECTOR_COMPARATOR',
 'claim_lock':'Do not report the scalar-envelope impurity as the full QGR graviton purity/decoherence prediction. Polarization/Wigner holonomy of coherent two-mode wavepackets, detector preparation/readout, and absolute microscopic h remain open. The robust result is the h^4 refinement order and the explicit preparation dependence of its coefficient.',
 'lane_classifications':{k:D[k]['classification'] for k in sorted(need)}
}
open('iter007-g6f-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
