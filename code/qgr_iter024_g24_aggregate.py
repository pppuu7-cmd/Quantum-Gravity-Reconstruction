#!/usr/bin/env python3
import glob,json,os,sys
files=glob.glob('iter024-g24-results/**/result.json',recursive=True)
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
all_pass=len(rows)==24 and all(r.get('passed') for r in rows)
summary={
 'gate':'ITER024-G24-AGGREGATE','lane_count':len(rows),'audit_counts':counts,'all_lane_gates_passed':all_pass,
 'scientific_status':'PASS_SCOPED_ALGEBRAIC_PHASE_AUTHORITY_DESIGN__BLOCKED_PHYSICAL_SAME_REALIZATION_FINITE_CURVED_PHASE_DATA_NOT_YET_DERIVED',
 'strongest_positive':'Three prospectively chosen nonredundant finite event phase samples have exact rank three on (K,A,B), and beta-independent cubic/quadratic ratios can then be read out without fixing the event-unit calibration.',
 'strongest_blocker':'Current QGR derived inputs provide zero numerical finite-curved phase samples. Unit-pair plus unit-triple data alone have rank two and leave an exact K/A degeneracy.',
 'next_gate':'QGR-ITER025-G25-DERIVE-SAME-REALIZATION-FINITE-CURVED-PHASE-SAMPLES-FROM-EXISTING-QGR-ACTION-WITHOUT-RETUNING',
 'claim_locks':['synthetic positive controls are not microscopic data','K,A,B not physically fixed','c6 fixed = NO','theory established = 0%','KMQGB NEW_REQUIRED not authorized']
}
os.makedirs('iter024-g24-summary',exist_ok=True)
with open('iter024-g24-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(summary,sort_keys=True))
if not all_pass: sys.exit(2)
