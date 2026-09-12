#!/usr/bin/env python3
import glob,json,os,sys
files=sorted(glob.glob('iter020-g20-results/qgr-g20-*/*.json'))
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
expected={'free-endpoint':6,'boundary-source':6,'s4-source-count':6,'history-normalization':6}
ok=(len(rows)==24 and counts==expected and all(r.get('passed') for r in rows))
out={
 'gate':'ITER020-G20-AGGREGATE','lane_count':len(rows),'audit_counts':counts,'all_lane_gates_passed':ok,
 'scientific_status':'PASS_SCOPED_PURE_DERIVED_COMMON_CONFORMAL_DIRICHLET_BULK_ACTION_SELECTS_ONLY_THE_IDENTITY_ENDPOINT_R_EQUALS_ONE_WHEN_THE_FINAL_ENDPOINT_IS_FREE__A_NONTRIVIAL_EVENT_REQUIRES_BOUNDARY_OR_INSERTION_AUTHORITY__S4_ALLOWS_ONE_SINGLET_SOURCE_DIRECTION_BUT_DOES_NOT_FIX_ITS_STRENGTH__HISTORY_NORMALIZATION_IS_BLIND_TO_THAT_STRENGTH',
 'strongest_positive':'The apparent free r has been reclassified: it is not a bulk coupling that the existing local action should determine. With s(0)=1 and free final endpoint, the exact stationary solution is s=1. A single S4-singlet boundary source is sufficient to generate any nontrivial endpoint while preserving the derived linear profile.',
 'strongest_blocker':'QGR does not yet derive the microscopic event insertion/boundary functional (or an equivalent source strength) from the Boolean incidence realization. S4 permits exactly one singlet source direction, but its coefficient has zero authority from the bulk action and from G8A history normalization.',
 'decision':'STOP_TRYING_TO_FIX_R_FROM_BULK_SCALE_SYMMETRY__REPLACE_R_AS_PRIMARY_UNKNOWN_BY_THE_MICROSCOPIC_EVENT_INSERTION_OR_BOUNDARY_OPERATOR_THAT_GENERATES_A_NONTRIVIAL_ENDPOINT',
 'next_gate':'QGR-ITER021-G21-BOOLEAN-EVENT-INSERTION-FROM-RANK2-PAIR-INCIDENCE-AND-SECOND-MOMENT-UPDATE',
 'r_status':'BOUNDARY_EVENT_DATUM_NOT_BULK_COUPLING_IN_SCOPED_CONFORMAL_SECTOR',
 'event_insertion_derived':False,'finite_pair_triple_coherent_amplitudes_derived':False,'c6_fixed':False,
 'claim_locks':['nontrivial event insertion derived = NO','finite pair/triple coherent amplitudes derived = NO','c6 fixed = NO','r is not fixed; G20 only reclassifies its role in the scoped conformal variational problem','no boundary source is to be added by hand','KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes']
}
os.makedirs('iter020-g20-summary',exist_ok=True)
with open('iter020-g20-summary/summary.json','w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
print(json.dumps(out,sort_keys=True))
if not ok: sys.exit(2)
