#!/usr/bin/env python3
import glob,json,os
files=glob.glob('iter007-g6e-results/*/*.json')+glob.glob('iter007-g6e-results/*.json')
D={}
for f in files:
 try:
  x=json.load(open(f));D[x['lane']]=x
 except Exception:pass
need={'C_E_CONVENTION_BRIDGE','CONVENTION_REPAIRED_G9_HISTORY','DEWITT_PHYSICAL_PAIRING','RELATIONAL_SCREEN_PHYSICAL_PAIRING','BOUNDARY_MEASURE_DISINTEGRATION'}
missing=need-set(D)
assert not missing,missing
assert D['C_E_CONVENTION_BRIDGE']['classification'].startswith('PASS_SCOPED')
assert D['CONVENTION_REPAIRED_G9_HISTORY']['classification'].startswith('PASS_SCOPED')
assert D['DEWITT_PHYSICAL_PAIRING']['classification'].startswith('PASS_SCOPED')
assert D['RELATIONAL_SCREEN_PHYSICAL_PAIRING']['classification'].startswith('PASS_SCOPED')
assert D['BOUNDARY_MEASURE_DISINTEGRATION']['classification'].startswith('PASS_SCOPED')
out={
 'iteration':'007-G6E','parallel_lanes':5,'aggregate_success':True,
 'closed_in_scope':[
  'explicit C versus C^-1 convention bridge at continuum/index level',
  'microscopic finite-curvature rerun with covariant seed E=C^-1 and QGR-L1 inverse characteristic form C',
  'positive observer-independent covariant pairing on ker(H)/im(R)',
  'relational timelike-screen construction as a representative of the two physical modes',
  'regular finite positive-measure disintegration over the shared B3 boundary without assuming conditional independence'
 ],
 'key_results':[
  'S=I-J/6 is S4-equivariant and satisfies S^T C S=C^-1; the old G6D null vector maps to one-half of the previously tested QGR-L1 null vector (1,1,1,-1).',
  'The finite torsion/history calculation rerun with covariant seed E=C^-1 retains a regular branch; relative history trace, common-target null Gram, and branch-to-branch barycentric rapidity invariants scale approximately h^4.',
  'The trace-reversed DeWitt-type bilinear has the four derivative-gauge directions as its exact radical on the six-dimensional characteristic kernel and leaves a positive two-dimensional quotient; it is exactly finite-frame covariant.',
  'The observer-dependent TT screen is therefore a representative/readout gauge for the same positive quotient pairing rather than a new physical norm.',
  'Positive regular boundary measure disintegration exists over the shared B3 pushforward; product conditional independence is neither needed nor inferred.'
 ],
 'active_blocker':'BLOCKED_MISSING_EXPLICIT_NORMALIZED_CURVED_WAVEPACKET_PREPARATION_AND_BRANCH_OVERLAP_COMPARATOR_PLUS_ABSOLUTE_H_KAPPA_SEPARATION',
 'recommended_next_gate':'G6F_NORMALIZED_CURVED_WAVEPACKET_CHANNEL_AND_PREPARATION_DEPENDENCE',
 'claim_lock':'Do not claim a parameter-free decoherence number yet. A normalized branch-mixture purity can now be defined on the common positive characteristic Hilbert, but its value depends on the specified physical wavepacket/preparation and the still-unseparated microscopic h/kappa scale. Do not convert the h^4 geometric spread alone into an experimental decoherence rate.',
 'lane_classifications':{k:D[k]['classification'] for k in sorted(need)},
 'repaired_g9_slopes':D['CONVENTION_REPAIRED_G9_HISTORY']['log_h_slopes']
}
open('iter007-g6e-summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
