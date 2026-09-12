#!/usr/bin/env python3
import glob,json,os,sys
files=sorted(glob.glob('iter023-g23-results/qgr-g23-*/*.json'))
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
expected={'prefix-moments':6,'phase-authority-rank':6,'coefficient-family-witness':6,'order-vs-action-cumulant':6}
ok=(len(rows)==24 and counts==expected and all(r.get('passed') for r in rows))
out={
 'gate':'ITER023-G23-AGGREGATE','lane_count':len(rows),'audit_counts':counts,'all_lane_gates_passed':ok,
 'scientific_status':'PASS_SCOPED_UNIFORM_24_HISTORY_ORDER_MEASURE_EXACTLY_FIXES_COMBINATORIAL_PREFIX_OCCUPANCY_MOMENTS_AND_CONNECTED_ORDER_CUMULANTS__BLOCKED_SCOPED_THE_SAME_NORMALIZED_ORDER_MEASURE_HAS_ZERO_AUTHORITY_RANK_ON_QUADRATIC_AND_CUBIC_ACTION_PHASE_COEFFICIENTS_AND_CANNOT_SUPPLY_G13_FINITE_PAIR_CONNECTED_TRIPLE_ACTION_DATA',
 'strongest_positive':'The normalized 24-order register does contain exact nontrivial microscopic combinatorics: all one-, pair- and triple-prefix occupancy moments and connected cumulants are fixed rational numbers by uniform permutation symmetry.',
 'strongest_blocker':'Those order cumulants are statistics of which Boolean generators have occurred, not action-phase cumulants. Completeness and every tested order statistic have exact authority rank zero on (K,A,B), and distinct beta-invariant cubic-shape families share exactly the same normalized 24-history order measure.',
 'decision':'DO_NOT_USE_UNIFORM_HISTORY_ORDER_CUMULANTS_AS_G13_PAIR_TRIPLE_ACTION_TARGETS__DERIVE_A_SAME_REALIZATION_EVENT_TO_ACTION_PHASE_MAP_ON_A_FINITE_CURVED_CELL_OR_FROM_AN_INDEPENDENT_NONHOMOGENEOUS_MICROSCOPIC_RULE',
 'next_gate':'QGR-ITER024-G24-FINITE-CURVED-EVENT-INSERTION-TO-ACTION-PHASE-AUTHORITY',
 'g13_pair_triple_action_data_derived_from_history_order_measure':False,'c6_fixed':False,
 'claim_locks':['order cumulants are not action cumulants','G13 pair/triple action data derived = NO','c6 fixed = NO','history completeness fixes branch modulus not action phase coefficients','no numerical matching of combinatorial cumulants to action coefficients without derived map']
}
os.makedirs('iter023-g23-summary',exist_ok=True)
with open('iter023-g23-summary/summary.json','w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(out,sort_keys=True))
if not ok: sys.exit(2)
