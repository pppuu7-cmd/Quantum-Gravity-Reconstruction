#!/usr/bin/env python3
import glob,json,os,sys
files=glob.glob('iter025-g25-results/*/result.json')
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
audits={}
for r in rows: audits[r['audit']]=audits.get(r['audit'],0)+1
all_structural=(len(rows)==24 and all(r.get('passed') for r in rows) and all(audits.get(k)==6 for k in ('current-bridge-rank','free-endpoint-collapse','source-map-nonuniqueness','three-probe-source-authority')))
out={
 'gate':'QGR-ITER025-G25-AGGREGATE',
 'lane_count':len(rows),'audit_counts':audits,'all_structural_gates_passed':all_structural,
 'scientific_status':('BLOCKED_SCIENTIFIC_EXISTING_QGR_ACTION_CAN_EVALUATE_AUTHORIZED_BOUNDARY_SOURCE_DATA_BUT_CURRENT_DERIVED_AUTHORITY_CHAIN_DOES_NOT_SUPPLY_A_UNIQUE_EVENT_COUNT_TO_SOURCE_MAP_AND_THEREFORE_DOES_NOT_DERIVE_THE_THREE_PHYSICAL_G24_FINITE_CURVED_PHASE_SAMPLES' if all_structural else 'NUMERICAL_OR_INFRASTRUCTURE_FAIL'),
 'strongest_positive':'The existing G19/G20 action-source response is sufficient to turn a specified source into an exact endpoint and on-shell phase; G24 gives a full-rank target basis for future microscopic data.',
 'strongest_blocker':'No derived same-realization map from the three finite event probes to boundary/source strength exists. Multiple exact S4-symmetric source laws satisfy current structural constraints while predicting different phase triples.',
 'claim_locks':['witness source laws are not candidate physics','K,A,B not physically fixed','c6 fixed = NO','theory established = 0%','KMQGB NEW_REQUIRED not authorized'],
 'next_gate':'QGR-ITER026-G26-SEEK-DERIVED-EVENT-TO-SOURCE-AUTHORITY-IN-EXISTING-MICROSCOPIC-INCIDENCE-HOLONOMY-AND-HISTORY-TRANSPORT-WITHOUT-ADDING-A-NEW-COUPLING'
}
os.makedirs('iter025-g25-summary',exist_ok=True)
with open('iter025-g25-summary/summary.json','w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(out,indent=2,sort_keys=True))
sys.exit(0 if all_structural else 2)
