#!/usr/bin/env python3
import glob,json,os

files=glob.glob('artifacts/qgr-iter051a-r1-lane-*/*.json')
rows=[]
for f in files:
    with open(f,'r',encoding='utf-8') as h: rows.append(json.load(h))
rows=sorted(rows,key=lambda x:x['lane'])
expected=list(range(12))
valid_structure=(len(rows)==12 and [r['lane'] for r in rows]==expected)
if not valid_structure:
    cls='INFRASTRUCTURE_OR_NUMERICAL_FAIL'
else:
    cls='PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE' if all(r.get('pass') for r in rows) else 'SCIENTIFIC_FAIL_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE'
out={
 'classification':cls,
 'found_lanes':len(rows),
 'lane_ids':[r['lane'] for r in rows],
 'passes':sum(bool(r.get('pass')) for r in rows),
 'valids':sum(bool(r.get('valid')) for r in rows),
 'nonzero_calibrations':sum(bool(r.get('nonzero_calibration')) for r in rows),
 'max_cs_vs_rich_80':max((r['cs_vs_rich_80'] for r in rows),default=None),
 'max_cs_vs_rich_120':max((r['cs_vs_rich_120'] for r in rows),default=None),
 'max_cs_precision_change':max((r['cs_precision_change'] for r in rows),default=None),
 'max_rich_precision_change':max((r['rich_precision_change'] for r in rows),default=None),
 'max_algebraic_residual_120':max((r['algebraic_residual_120'] for r in rows),default=None),
 'max_weyl_trace_residual_120':max((r['weyl_trace_residual_120'] for r in rows),default=None),
 'max_density_covariance_rel_120':max((r['max_density_covariance_rel_120'] for r in rows),default=None),
 'max_direction_covariance_rel_120':max((r['max_direction_covariance_rel_120'] for r in rows),default=None)
}
with open('iter051a-r1-summary.json','w',encoding='utf-8') as h: json.dump(out,h,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
