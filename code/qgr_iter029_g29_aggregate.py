#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
root=Path('iter029-g29-results')
files=sorted(root.glob('qgr-g29-*/*.json'))
rows=[json.loads(p.read_text()) for p in files]
counts={}
for r in rows: counts[r['audit']]=counts.get(r['audit'],0)+1
required={'source-weyl-rank':6,'conformal-null':6,'absolute-phase-positive-control':6,'nonuniqueness-witness':6}
all_present=(counts==required and len(rows)==24)
all_pass=all(r.get('passed') is True for r in rows)
summary={
 'gate':'ITER029-G29-AGGREGATE','lane_count':len(rows),'audit_counts':counts,'all_required_artifacts_present':all_present,'all_lane_gates_passed':all_pass,
 'scientific_status':('BLOCKED_SCOPED_EXISTING_QGR_HAS_WEYL_ACTIVE_C6_SENSITIVITY_BUT_CURRENT_SOURCE_SHAPE_AND_SCALE_FREE_CONFORMAL_DATA_HAVE_INSUFFICIENT_AUTHORITY_RANK_TO_FIX_C6_OR_ABSOLUTE_SOURCE_SCALE__ONE_GENUINE_NONHOMOGENEOUS_WEYL_ACTIVE_ABSOLUTE_PHASE_TARGET_WOULD_CLOSE_THE_C6_DIRECTION' if all_present and all_pass else 'FAIL_OR_INCOMPLETE_G29_FROZEN_AUTHORITY_AUDIT'),
 'c6_fixed':False,'absolute_beta_fixed':False,'physical_weyl_active_phase_target_present':False,
 'next_gate':('QGR-ITER030-G30-EXISTING-MICROSCOPIC-WEYL-ACTIVE-FINITE-CELL-PHASE-SOURCE-CENSUS' if all_present and all_pass else 'BLOCKED_PENDING_G29_FAILURE_CLASSIFICATION'),
 'claim_locks':['do not fit c6','do not set beta=1','positive-control target is not physical data','theory established = 0%','KMQGB NEW_REQUIRED unauthorized unless benchmark authority changes']
}
out=Path('iter029-g29-summary/summary.json'); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
print(json.dumps(summary,sort_keys=True))
if not (all_present and all_pass): raise SystemExit(2)
