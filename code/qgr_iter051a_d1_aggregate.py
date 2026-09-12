#!/usr/bin/env python3
import json, glob
files=sorted(glob.glob('artifacts/qgr-iter051a-d1-lane-*/*.json'))
lanes=[]
for f in files:
    with open(f,'r',encoding='utf-8') as fh: lanes.append(json.load(fh))
ids=sorted(x['lane'] for x in lanes)
valid=(len(lanes)==12 and ids==list(range(12)) and all(x.get('valid') and x.get('covariance_ok') for x in lanes))
orig_fail=[x for x in lanes if not x.get('original_g51a_pass_recomputed')]
localized=[x for x in orig_fail if x.get('diagnostic_classification')=='ROUND_OFF_TURNOVER_LOCALIZED']
if not valid or len(orig_fail)!=7:
    classification='INVALID_DIAGNOSTIC_CONTROLS'
elif len(localized)>=6:
    classification='DIAGNOSTIC_FD_ROUNDOFF_TURNOVER_DOMINANT'
elif len(localized)>=3:
    classification='DIAGNOSTIC_MIXED_NUMERICAL_BEHAVIOR'
else:
    classification='DIAGNOSTIC_G51A_FAILURE_NOT_EXPLAINED_BY_FD_ROUNDOFF'
out={
 'classification':classification,'expected_lanes':12,'found_lanes':len(lanes),
 'recomputed_original_failures':len(orig_fail),'roundoff_localized_failures':len(localized),
 'original_failure_lane_ids':[x['lane'] for x in orig_fail],
 'localized_lane_ids':[x['lane'] for x in localized],
 'max_minimum_rel':max([x['minimum_rel'] for x in lanes],default=None),
 'max_final_abs_error':max([x['final_abs_error'] for x in lanes],default=None)
}
with open('iter051a-d1-summary.json','w',encoding='utf-8') as fh: json.dump(out,fh,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
if classification=='INVALID_DIAGNOSTIC_CONTROLS': raise SystemExit(2)
