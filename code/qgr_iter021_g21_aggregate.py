#!/usr/bin/env python3
import glob,json,os,sys
files=sorted(glob.glob('iter021-g21-results/qgr-g21-*/*.json'))
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
expected={'sym2-invariants':6,'pair-support':6,'count-response-map':6,'finite-admissibility':6}
ok=(len(rows)==24 and counts==expected and all(r.get('passed') for r in rows))
out={
 'gate':'ITER021-G21-AGGREGATE','lane_count':len(rows),'audit_counts':counts,'all_lane_gates_passed':ok,
 'scientific_status':'PARTIAL_SCOPED_B4_DISTINCT_PAIR_INCIDENCE_PLUS_S4_SELECTS_A_UNIQUE_OFF_DIAGONAL_SINGLET_EVENT_INSERTION_DIRECTION_IN_SYM2_W4_AFTER_EXCLUDING_NONPRIMITIVE_DIAGONAL_SELF_PAIR_SUPPORT__BUT_THE_COMBINATORIAL_PAIR_COUNT_TO_PHYSICAL_SECOND_MOMENT_RESPONSE_MAP_RETAINS_EXACTLY_ONE_UNFIXED_SCALAR_COEFFICIENT_BETA',
 'strongest_positive':'The missing event insertion is no longer directionally arbitrary. Sym2(W4) has exactly two S4 singlets; strict B4 rank-2 distinct-pair support removes the diagonal self-response singlet and leaves the unique off-diagonal incidence ray C=J-I.',
 'strongest_blocker':'An equivariant map from one combinatorial distinct-pair count to the selected physical second-moment response is still multiplication by one scalar beta. Multiple exact beta values preserve S4, pair support, Q13 signature, the scale-invariant kinematic measure and zero constant-flat local action. Setting beta=1 from the 0/1 adjacency convention would be a postulate, not a derivation.',
 'decision':'PROMOTE_EVENT_INSERTION_DIRECTION_C_AS_STRUCTURALLY_SELECTED_IN_THE_STRICT_PAIR_INCIDENCE_SECTOR__DO_NOT_PROMOTE_ITS_MAGNITUDE__NEXT_SEARCH_MUST_DERIVE_THE_SINGLE_COMBINATORIAL_TO_PHYSICAL_RESPONSE_COEFFICIENT_FROM_A_SAME_REALIZATION_QUANTUM_OR_COMPOSITIONAL_NORMALIZATION_OR_RECLASSIFY_IT_AS_PREPARATION_DATA',
 'next_gate':'QGR-ITER022-G22-EVENT-RESPONSE-BETA-STATUS-QUANTUM-NORMALIZATION-VS-PREPARATION-DATUM',
 'event_insertion_direction_derived':True,'event_insertion_strength_derived':False,'finite_pair_triple_coherent_amplitudes_derived':False,'c6_fixed':False,
 'claim_locks':['event insertion direction derived only in strict S4-symmetric rank-2 distinct-pair sector','event insertion strength beta derived = NO','finite pair/triple coherent amplitudes derived = NO','c6 fixed = NO','beta=1 is not authorized from binary incidence notation','KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes']
}
os.makedirs('iter021-g21-summary',exist_ok=True)
with open('iter021-g21-summary/summary.json','w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(out,sort_keys=True))
if not ok: sys.exit(2)
