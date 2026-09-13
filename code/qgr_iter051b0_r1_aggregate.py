#!/usr/bin/env python3
import glob,json
files=sorted(glob.glob('artifacts/qgr-iter051b0-r1-lane-*/*.json'))
rows=[]; parse_errors=[]
for f in files:
    try:
        with open(f) as h: rows.append(json.load(h))
    except Exception as e: parse_errors.append({'file':f,'error':repr(e)})
ids=sorted(r.get('lane') for r in rows if isinstance(r.get('lane'),int))
valids=sum(bool(r.get('valid')) for r in rows); passes=sum(bool(r.get('pass')) for r in rows)
if parse_errors or len(rows)!=8 or ids!=list(range(8)):
    classification='NUMERICAL_OR_INFRASTRUCTURE_FAIL_G51B0_R1'
elif valids==8 and passes==8:
    classification='PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE'
else:
    classification='SCIENTIFIC_FAIL_REPLACEMENT_G51B0_DOUBLE_DIVERGENCE'
out={'classification':classification,'found_lanes':len(rows),'lane_ids':ids,'valids':valids,'passes':passes,'parse_errors':parse_errors}
if rows:
    out['max_finest_relative_discrepancy']=max(r['relative_errors'][-1] for r in rows)
    out['max_covariance_residual']=max(max(r['covariance_residuals']) for r in rows)
    out['max_P_transform_control_residual']=max(max(r['P_transform_control_residuals']) for r in rows)
    out['max_lorentz_metric_residual']=max(max(r['lorentz_metric_residuals']) for r in rows)
    out['max_inverse_residual']=max(r['max_inverse_residual'] for r in rows)
    out['max_P_symmetry_residual']=max(r['P_symmetry_residual'] for r in rows)
with open('iter051b0-r1-summary.json','w') as h: json.dump(out,h,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
