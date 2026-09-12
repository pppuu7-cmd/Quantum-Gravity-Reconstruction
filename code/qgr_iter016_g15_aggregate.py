#!/usr/bin/env python3
import glob,json,os
files=glob.glob('iter016-g15-results/**/result.json',recursive=True)
recs=[json.load(open(f)) for f in files]
audits=('linear-bridge','nonlinear-congruence','profile-obstruction','authority-after-bridge')
expected={(a,l) for a in audits for l in range(6)}
seen={(r['audit'],r['lane']) for r in recs}
assert seen==expected,(len(seen),sorted(expected-seen),sorted(seen-expected))
assert all(r.get('passed') is True for r in recs)
lin=[r for r in recs if r['audit']=='linear-bridge']
non=[r for r in recs if r['audit']=='nonlinear-congruence']
pro=[r for r in recs if r['audit']=='profile-obstruction']
aut=[r for r in recs if r['audit']=='authority-after-bridge']
assert {r['offdiag_linear_map_rank'] for r in lin}=={4}
assert all(r['s4_covariant'] for r in lin+non)
assert all(r['exact_multiplicative_composition'] for r in non)
assert {r['constant_q_two_derivative_action'] for r in pro}=={'0'}
assert {r['rank_after_bridge_without_finite_profile_action'] for r in aut}=={1}
assert {r['cubic_nullity_after_bridge'] for r in aut}=={2}
out={
 'gate':'QGR-ITER016-G15-CANONICAL-MICROSCOPIC-EVENT-TO-G-BRIDGE-OR-NONEXISTENCE',
 'parallel_lanes':24,'aggregate_success':True,'c6_fixed':False,
 'classification':'PARTIAL_SCOPED_CANONICAL_GENERATOR_LOCAL_FRAME_RESCALE_SUBBRIDGE_EXISTS_INSIDE_EXISTING_G_EQUALS_FT_C_F_ARENA__BUT_IDENTIFYING_G13_EVENTS_WITH_THOSE_RESCALINGS_AND_DERIVING_THEIR_FINITE_PROFILE_ACTION_REMAINS_BLOCKED',
 'strongest_positive':'Using only the existing C=J-I seed and G=F^T C F frame congruence, generator-local diagonal frame rescalings give an exact S4-covariant rank-four nonlinear submanifold with linearization delta G_ij=q_i+q_j for i!=j and zero diagonal.',
 'strongest_blocker':'The all-orders verified local action is two-derivative: it vanishes for constant event coordinates and finite endpoint changes are profile/refinement dependent. The coordinate bridge therefore adds no nonhomogeneous amplitude-authority row; cubic rank stays 1 with nullity 2.',
 'next_gate':'QGR-ITER016-G16-MICROSCOPIC-FINITE-PROFILE-ACTION-FROM-BOOLEAN-CELL-COMPOSITION',
 'claim_locks':['canonical subbridge is not yet a derived identification of G13 event variables','finite pair/triple amplitudes remain absent','c6 fixed = NO','no QGR correctness or KMQGB NEW_REQUIRED claim']
}
os.makedirs('iter016-g15-summary',exist_ok=True)
with open('iter016-g15-summary/summary.json','w') as f:json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
