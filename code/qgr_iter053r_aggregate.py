#!/usr/bin/env python3
import glob,json,math,os
EXPECTED={('A',i) for i in range(4)}|{('B',i) for i in range(2)}|{('C',i) for i in range(2)}
rows=[]; errors=[]
for p in glob.glob('artifacts/qgr-iter053r-*/*.json'):
    try:
        with open(p) as f: d=json.load(f)
        if d.get('stream') in ('A','B','C') and isinstance(d.get('index'),int): rows.append(d)
    except Exception as e: errors.append({'path':p,'error':repr(e)})
keys={(d['stream'],d['index']) for d in rows}; missing=sorted(EXPECTED-keys); extra=sorted(keys-EXPECTED)
valid=[d for d in rows if d.get('control_valid') is True]; passes=[d for d in rows if d.get('lane_pass') is True]
Arows=[d for d in rows if d.get('stream')=='A']
wrong_all=bool(len(Arows)==4 and all(float(d.get('wrong_sign_relative_residual',-1))>float(d.get('identity_relative_residual',math.inf)) for d in Arows))
wrong_strong=bool(any(float(d.get('wrong_sign_relative_residual',0))>=1e-2 for d in Arows))
if errors or missing or extra or len(rows)!=8:
    cls='ITER053R_NUMERICAL_OR_INFRASTRUCTURE_FAIL'
elif len(valid)!=8:
    cls='ITER053R_IMPLEMENTATION_OR_CONTROL_INVALID'
elif len(passes)==8 and wrong_all and wrong_strong:
    cls='PASS_SCOPED_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE'
else:
    cls='SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION'
summary={'gate':'ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION','classification':cls,'expected_lanes':8,'found_lanes':len(rows),
         'valid_lanes':len(valid),'passes':len(passes),'missing':missing,'extra':extra,'parse_errors':errors,
         'wrong_sign_control_all_weaker_than_correct':wrong_all,'wrong_sign_control_at_least_one_ge_1e-2':wrong_strong,
         'stream_counts':{s:sum(1 for d in rows if d.get('stream')==s) for s in ('A','B','C')},
         'interpretation_lock':'FINITE GENUINELY-4D COMPACT-SUPPORT COMPUTATIONAL CERTIFICATE ONLY; C6 SYMBOLIC UNFIXED; NO GLOBAL FUNCTIONAL-DERIVATIVE THEOREM; THEORY_ESTABLISHED_0'}
if Arows:
    summary['worst_A_identity_relative_residual']=max(float(d.get('identity_relative_residual',math.inf)) for d in Arows)
    summary['worst_A_direct_step_change']=max(float(d.get('direct_final_step_change',math.inf)) for d in Arows)
    summary['worst_A_GL7_to_GL8_change']=max(float(d.get('direct_GL7_to_GL8_relative_change',math.inf)) for d in Arows)
    summary['worst_A_weighted_bulk_GJ2_to_GJ3_change']=max(float(d.get('weighted_bulk_GJ2_to_GJ3_relative_change',math.inf)) for d in Arows)
    summary['worst_A_identity_residual_change']=max(float(d.get('coarse_to_fine_identity_residual_change_abs',math.inf)) for d in Arows)
    summary['min_A_wrong_sign_relative_residual']=min(float(d.get('wrong_sign_relative_residual',-math.inf)) for d in Arows)
Brows=[d for d in rows if d.get('stream')=='B']
if Brows:
    summary['worst_B_abs_direct_GL8']=max(abs(float(d['direct_GL8']['direct'][-1])) for d in Brows)
    summary['worst_B_abs_bulk_GJ3']=max(abs(float(d['GJ3']['bulk'])) for d in Brows)
Crows=[d for d in rows if d.get('stream')=='C']
if Crows:
    summary['worst_C_direct_covariance_relative_residual']=max(float(d.get('direct_covariance_relative_residual',math.inf)) for d in Crows)
    summary['worst_C_bulk_covariance_relative_residual']=max(float(d.get('bulk_covariance_relative_residual',math.inf)) for d in Crows)
os.makedirs('iter053r-summary',exist_ok=True)
with open('iter053r-summary/summary.json','w') as f: json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if cls=='ITER053R_NUMERICAL_OR_INFRASTRUCTURE_FAIL': raise SystemExit(4)
if cls=='ITER053R_IMPLEMENTATION_OR_CONTROL_INVALID': raise SystemExit(3)
if cls.startswith('SCIENTIFIC_FAIL'): raise SystemExit(2)
