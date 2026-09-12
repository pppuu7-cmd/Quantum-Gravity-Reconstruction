#!/usr/bin/env python3
import json, glob, os

files=sorted(glob.glob('artifacts/qgr-iter051a-lane-*/*.json'))
lanes=[]
for f in files:
    with open(f,'r',encoding='utf-8') as fh: lanes.append(json.load(fh))
ids=sorted(x['lane'] for x in lanes)
valid=(len(lanes)==12 and ids==list(range(12)))
classification='INVALID_G51A_METRIC_OR_ALGEBRAIC_CONTROL'
if valid:
    if all(x.get('valid') for x in lanes):
        if all(x.get('pass') for x in lanes) and sum(bool(x.get('nonzero_calibration')) for x in lanes)>=10:
            classification='PASS_SCOPED_G51A_WEYL3_ALGEBRAIC_METRIC_DENSITY_VARIATION'
        else:
            classification='SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION'
out={
 'classification':classification,
 'expected_lanes':12,'found_lanes':len(lanes),'passes':sum(bool(x.get('pass')) for x in lanes),
 'nonzero_calibration_lanes':sum(bool(x.get('nonzero_calibration')) for x in lanes),
 'max_algebraic_residual':max([x['algebraic_residual'] for x in lanes],default=None),
 'max_weyl_trace_residual':max([x['weyl_trace_residual'] for x in lanes],default=None),
 'max_finest_rel':max([x['finest_rel'] for x in lanes],default=None),
 'max_density_covariance_rel':max([max(c['density_rel'] for c in x['covariance']) for x in lanes],default=None),
 'max_direction_covariance_rel':max([max(c['direction_rel'] for c in x['covariance']) for x in lanes],default=None)
}
with open('iter051a-summary.json','w',encoding='utf-8') as fh: json.dump(out,fh,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
if classification!='PASS_SCOPED_G51A_WEYL3_ALGEBRAIC_METRIC_DENSITY_VARIATION': raise SystemExit(2)
