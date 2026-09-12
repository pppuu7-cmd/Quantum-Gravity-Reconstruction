#!/usr/bin/env python3
import argparse,itertools,json,math,collections
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
PERMS=list(itertools.permutations(range(4)))
rank_rows=[]
for r in range(5):
 prefixes=collections.Counter(tuple(p[:r]) for p in PERMS)
 endpoints=collections.Counter(tuple(sorted(p[:r])) for p in PERMS)
 expected_prefix_count=math.factorial(4)//math.factorial(4-r)
 assert len(prefixes)==expected_prefix_count
 assert set(prefixes.values())=={math.factorial(4-r)}
 assert len(endpoints)==math.comb(4,r)
 assert set(endpoints.values())=={math.factorial(r)*math.factorial(4-r)}
 rank_rows.append({'rank':r,'ordered_prefixes':len(prefixes),'completion_count_per_prefix':math.factorial(4-r),'endpoints':len(endpoints),'full_histories_per_endpoint':math.factorial(r)*math.factorial(4-r),'endpoint_probability':1/math.comb(4,r)})
trans=[]
for r in range(4):
 # Given a concrete rank-r prefix/subset, each unused direction has equal number of completions.
 trans.append({'rank':r,'remaining_directions':4-r,'conditional_probability_per_next_direction':1/(4-r),'conditional_amplitude_modulus_per_next_direction':1/math.sqrt(4-r)})
out={'lane':'RANK_CONDITIONED_PREFIX_TRANSITION_LAW','history_count':24,'rank_rows':rank_rows,'transitions':trans,'classification':'PASS_SCOPED_UNIFORM_24_HISTORY_MEASURE_INDUCES_EXACT_BRANCH_SYMMETRIC_MARKOV_PREFIX_LAW_WITH_NEXT_DIRECTION_PROBABILITY_ONE_OVER_FOUR_MINUS_RANK','scientific_interpretation':'Conditioning the existing uniform 24-history measure on the intrinsic Boolean rank gives an exact sequential law. At rank r every remaining generator is equiprobable with probability 1/(4-r), ordered prefixes are uniform, and rank-r endpoints are uniform over the binomial slice. No new stochastic coefficient is introduced.','guard':'This is the branch-measure law conditioned on rank. It does not yet fix branch phases, a physical tick duration, or an autonomous Hamiltonian.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))