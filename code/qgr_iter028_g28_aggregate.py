#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

root=Path('iter028-g28-results')
files=sorted(root.glob('qgr-g28-*/*.json'))
rows=[json.loads(p.read_text(encoding='utf-8')) for p in files]
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
required={'endpoint-ratio':6,'phase-ratio':6,'action-endpoint-invariant':6,'weyl-authority-null':6}
all_present=counts==required and len(rows)==24
all_pass=all(r.get('passed') is True for r in rows)
summary={
 'gate':'ITER028-G28-AGGREGATE',
 'lane_count':len(rows),
 'audit_counts':counts,
 'all_required_artifacts_present':all_present,
 'all_lane_gates_passed':all_pass,
 'absolute_beta_fixed':False,
 'physical_finite_curved_phase_samples_derived':False,
 'c6_fixed':False,
 'scientific_status':('PASS_SCOPED_SOURCE_SCALE_QUOTIENT_YIELDS_EXACT_BETA_INDEPENDENT_ENDPOINT_AND_COMMON_CONFORMAL_PHASE_RATIOS_AND_ACTION_ENDPOINT_INVARIANT__NEGATIVE_CONTROL_CONFIRMS_ZERO_C6_AUTHORITY' if all_present and all_pass else 'FAIL_OR_INCOMPLETE_G28_FROZEN_QUOTIENT_GATE'),
 'decision':('PROMOTE_ONLY_SCALE_FREE_COMMON_CONFORMAL_RELATIONS__DO_NOT_PROMOTE_ABSOLUTE_SOURCE_NORMALIZATION_OR_C6__NEXT_SEEK_A_WEYL_ACTIVE_SAME_REALIZATION_FINITE_PHASE_OBSERVABLE_OR_AN_INDEPENDENT_ABSOLUTE_SOURCE_AUTHORITY' if all_present and all_pass else 'DO_NOT_PROMOTE'),
 'next_gate':('QGR-ITER029-G29-WEYL-ACTIVE-SAME-REALIZATION-FINITE-PHASE-AUTHORITY-SEARCH' if all_present and all_pass else 'BLOCKED_PENDING_G28_FAILURE_CLASSIFICATION'),
 'claim_locks':['beta fixed = NO','physical same-realization finite-curved phases derived = NO','c6 fixed = NO','theory established = 0%','KMQGB NEW_REQUIRED remains unauthorized unless benchmark authority changes']
}
out=Path('iter028-g28-summary/summary.json'); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,sort_keys=True))
if not (all_present and all_pass): raise SystemExit(2)
