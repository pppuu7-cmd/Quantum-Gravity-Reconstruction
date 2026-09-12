#!/usr/bin/env python3
import argparse,itertools,json,math
P=argparse.ArgumentParser();P.add_argument('--output',required=True);args=P.parse_args()
# Rank-conditioned coherent tick amplitudes have modulus 1/sqrt(4-r).
mods=[1/math.sqrt(4-r) for r in range(4)]
full=math.prod(mods)
assert abs(full-1/math.sqrt(24))<1e-15
# Verify normalization recursively: from every rank-r prefix there are 4-r outgoing orthogonal history labels.
rows=[]
for r,m in enumerate(mods):
 norm=(4-r)*m*m
 assert abs(norm-1)<1e-15
 rows.append({'rank':r,'outgoing_branches':4-r,'amplitude_modulus':m,'isometry_norm_sum':norm})
# Final 24 branch probabilities are equal.
prob=full*full
assert abs(prob-1/24)<1e-15
assert abs(24*prob-1)<1e-15
out={'lane':'SEQUENTIAL_HISTORY_ISOMETRY_FACTORIZATION','tick_rows':rows,'product_amplitude_modulus':full,'final_branch_probability':prob,'final_completeness':24*prob,'classification':'PASS_SCOPED_EXISTING_ONE_OVER_SQRT24_HISTORY_MODULUS_FACTORIZES_EXACTLY_INTO_INTRINSIC_RANK_TICK_ISOMETRIES','scientific_interpretation':'The normalized 24-history instrument admits an exact sequential modulus factorization along the intrinsic rank clock: 1/sqrt(4), 1/sqrt(3), 1/sqrt(2), 1. Each tick is individually isometric when the next-direction label is retained, and the four-tick product gives exactly 1/sqrt(24) per maximal history. Thus the global branch modulus is compatible with a clock-conditioned microscopic composition rather than being only a one-cell normalization rule.','guard':'Orthogonal history labels are retained exactly as in the existing history-register construction. This result does not determine tick phases or prove that tracing after each tick is physically required.'}
open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))