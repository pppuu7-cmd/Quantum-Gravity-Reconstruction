#!/usr/bin/env python3
import glob,json,os,math

EXPECTED={('A',i) for i in range(4)}|{('B',i) for i in range(2)}|{('C',i) for i in range(2)}
rows=[]; errors=[]
for p in glob.glob('artifacts/qgr-iter053-*/*.json'):
    try:
        with open(p) as f: d=json.load(f)
        if d.get('stream') in ('A','B','C') and isinstance(d.get('index'),int): rows.append(d)
    except Exception as e: errors.append({'path':p,'error':repr(e)})
keys={(d['stream'],d['index']) for d in rows}
missing=sorted(EXPECTED-keys); extra=sorted(keys-EXPECTED)
valid=[d for d in rows if d.get('control_valid') is True]
passes=[d for d in rows if d.get('lane_pass') is True]
A=[d for d in rows if d.get('stream')=='A']
wrong_all=bool(len(A)==4 and all(float(d.get('wrong_sign_relative_residual',-1))>float(d.get('identity_relative_residual',1e99)) for d in A))
wrong_strong=bool(any(float(d.get('wrong_sign_relative_residual',0))>=1e-2 for d in A))

if errors or missing or extra or len(rows)!=8:
    cls='ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL'
elif len(valid)!=8:
    cls='ITER053_IMPLEMENTATION_OR_CONTROL_INVALID'
elif len(passes)==8 and wrong_all and wrong_strong:
    cls='PASS_SCOPED_ITER053_WEYL3_INTEGRATED_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE'
else:
    cls='SCIENTIFIC_FAIL_ITER053_WEYL3_INTEGRATED_COMPACT_SUPPORT_ACTION_VARIATION'

summary={
 'gate':'ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION',
 'classification':cls,'expected_lanes':8,'found_lanes':len(rows),'valid_lanes':len(valid),'passes':len(passes),
 'missing':missing,'extra':extra,'parse_errors':errors,'wrong_sign_control_all_weaker_than_correct':wrong_all,
 'wrong_sign_control_at_least_one_ge_1e-2':wrong_strong,
 'stream_counts':{s:sum(1 for d in rows if d.get('stream')==s) for s in ('A','B','C')},
 'interpretation_lock':'FINITE INTEGRATED GENUINELY-4D COMPACT-SUPPORT COMPUTATIONAL CERTIFICATE ONLY; C6 SYMBOLIC UNFIXED; NO GLOBAL THEOREM; THEORY_ESTABLISHED_0'
}
# Useful extrema for terminal review.
if A:
 summary['worst_A_identity_relative_residual']=max(float(d.get('identity_relative_residual',math.inf)) for d in A)
 summary['worst_A_direct_step_change']=max(float(d.get('direct_final_step_change',math.inf)) for d in A)
 summary['worst_A_bulk_quadrature_change']=max(float(d.get('bulk_coarse_to_fine_relative_change',math.inf)) for d in A)
 summary['min_A_wrong_sign_relative_residual']=min(float(d.get('wrong_sign_relative_residual',-math.inf)) for d in A)
B=[d for d in rows if d.get('stream')=='B']
if B:
 summary['worst_B_abs_direct']=max(abs(float(d['fine']['direct'][-1])) for d in B)
 summary['worst_B_abs_bulk']=max(abs(float(d['fine']['bulk'])) for d in B)
C=[d for d in rows if d.get('stream')=='C']
if C:
 summary['worst_C_direct_covariance_relative_residual']=max(float(d.get('direct_covariance_relative_residual',math.inf)) for d in C)
 summary['worst_C_bulk_covariance_relative_residual']=max(float(d.get('bulk_covariance_relative_residual',math.inf)) for d in C)

os.makedirs('iter053-summary',exist_ok=True)
with open('iter053-summary/summary.json','w') as f: json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if cls=='ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL': raise SystemExit(4)
if cls=='ITER053_IMPLEMENTATION_OR_CONTROL_INVALID': raise SystemExit(3)
if cls.startswith('SCIENTIFIC_FAIL'): raise SystemExit(2)
