#!/usr/bin/env python3
import glob,json,os

files=glob.glob('iter016-g14-results/**/result.json',recursive=True)
recs=[json.load(open(f)) for f in files]
expected={(a,l) for a in ('equivariant-map','quadratic-authority','history-normalization','authority-rank') for l in range(6)}
seen={(r['audit'],r['lane']) for r in recs}
assert seen==expected,(len(seen),sorted(expected-seen),sorted(seen-expected))
assert all(r.get('passed') is True for r in recs)

def pick(a): return [r for r in recs if r['audit']==a]
eq=pick('equivariant-map');qa=pick('quadratic-authority');hn=pick('history-normalization');ar=pick('authority-rank')
assert {r['constraint_rank'] for r in eq}=={36}
assert {r['equivariant_map_nullity'] for r in eq}=={4}
assert {r['explicit_equivariant_basis_rank'] for r in eq}=={4}
assert all(r['same_hessian_after_cubic_change'] for r in qa)
assert {r['common_logweight_pair_cumulant'] for r in hn}=={'0'}
assert {r['common_logweight_triple_cumulant'] for r in hn}=={'0'}
assert {r['current_authority_rank'] for r in ar}=={1}
assert {r['current_cubic_nullity'] for r in ar}=={2}
assert {r['rank_with_pair_and_connected_triple_data'] for r in ar}=={3}

out={
 'gate':'QGR-ITER016-G14-MICROSCOPIC-EVENT-TO-GEOMETRY-AMPLITUDE-BRIDGE',
 'parallel_lanes':24,
 'aggregate_success':True,
 'equivariant_event_to_G_linear_map_dimension':4,
 'current_cubic_authority_rank':1,
 'current_cubic_nullity':2,
 'g13_conditional_rank_with_pair_and_triple':3,
 'c6_fixed':False,
 'classification':'BLOCKED_SCOPED_CURRENT_QGR_AUTHORITIES_FIX_THE_QUADRATIC_EVENT_COUPLING_BUT_DO_NOT_DERIVE_A_UNIQUE_EVENT_TO_G_MAP_OR_NONHOMOGENEOUS_FINITE_PAIR_AND_CONNECTED_TRIPLE_AMPLITUDES__G13_IS_CONDITIONAL_IDENTIFIABILITY_NOT_MICROSCOPIC_PROVENANCE',
 'strongest_positive':'Exact S4 representation audit gives a four-dimensional equivariant W4-to-Sym2(W4) bridge space, while G13 proves that one finite pair datum plus one connected triple datum would raise cubic authority rank from 1 to 3 and identify the two missing directions.',
 'strongest_blocker':'No existing same-realization QGR object selects one of the four equivariant event-to-G maps and computes the required finite pair plus connected triple coherent amplitudes. History normalization supplies zero coherent phase response, and G5 is exactly blind to cubic a,b.',
 'next_gate':'QGR-ITER016-G15-CANONICAL-MICROSCOPIC-EVENT-TO-G-BRIDGE-OR-NONEXISTENCE',
 'claim_locks':['c6 fixed = NO','G13 pair/triple data are not derived QGR physics','BLOCKED is not candidate FAIL','no new-model-required inference from KMQGB']
}
os.makedirs('iter016-g14-summary',exist_ok=True)
with open('iter016-g14-summary/summary.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
print(json.dumps(out,sort_keys=True))
