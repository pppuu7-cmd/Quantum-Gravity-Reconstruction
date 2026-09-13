#!/usr/bin/env python3
import glob,json,sys
files=sorted(glob.glob('artifacts/**/lane-*.json',recursive=True))
rows=[]; parse_errors=[]
for path in files:
    try:
        with open(path,'r',encoding='utf-8-sig') as f: lines=f.read().strip().splitlines()
        if not lines: raise ValueError('empty artifact')
        rows.append(json.loads(lines[-1]))
    except Exception as exc:
        parse_errors.append({'path':path,'error':repr(exc)})
expected=4
complete=(len(rows)==expected and len({r.get('lane') for r in rows})==expected and not parse_errors)
valid=[r for r in rows if r.get('valid') is True]; passed=[r for r in rows if r.get('pass') is True]
if not complete: status='INFRASTRUCTURE_OR_NUMERICAL_FAIL_G51B2'
elif len(valid)==expected and len(passed)==expected: status='PASS_SCOPED_WEYL3_P_CONNECTION_RESPONSE_CERTIFICATE'
else: status='SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE'
summary={'gate':'ITER051B2-WEYL3-P-CONNECTION-RESPONSE','scientific_status':status,'expected_lanes':expected,'artifact_rows':len(rows),'valid_count':len(valid),'passed_count':len(passed),'parse_errors':parse_errors,'frozen_thresholds':{'inverse_max':1e-11,'P_jet_algebraic_max':2e-10,'D_reference_norm_min':1e-6,'D_direct_norm_min':1e-6,'zero_curvature_P_norm_max':2e-10,'P_jet_reference_convergence_max':2e-5,'direct_vs_reference_finest_max':2e-5,'direct_final_step_change_max':1e-5,'D_covariance_max':2e-7,'P0_direct_covariance_max':2e-9}}
if rows:
    summary['worst']={'max_metric_det':max(float(r['max_metric_det']) for r in rows),'max_inverse_residual':max(float(r['max_inverse_residual']) for r in rows),'P_jet_algebraic':max(max(map(float,r['P_jet_algebraic_residuals'])) for r in rows),'min_D_reference_norm':min(float(r['D_reference_norm']) for r in rows),'min_D_direct_finest_norm':min(float(r['D_direct_finest_norm']) for r in rows),'zero_curvature_P_norm':max(float(r['zero_curvature_P_norm']) for r in rows),'P_jet_reference_convergence':max(float(r['P_jet_reference_convergence']) for r in rows),'direct_vs_reference_finest':max(float(r['direct_vs_reference_residuals'][-1]) for r in rows),'direct_final_step_change':max(float(r['direct_final_step_change']) for r in rows),'D_covariance':max(max(map(float,r['D_covariance_residuals'])) for r in rows),'P0_direct_covariance':max(max(map(float,r['P0_direct_covariance_residuals'])) for r in rows)}
with open('iter051b2-summary.json','w',encoding='utf-8') as f: json.dump(summary,f,indent=2,sort_keys=True)
print(json.dumps(summary,indent=2,sort_keys=True))
if status=='INFRASTRUCTURE_OR_NUMERICAL_FAIL_G51B2': sys.exit(2)
