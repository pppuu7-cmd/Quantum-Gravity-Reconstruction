#!/usr/bin/env python3
import glob,json,os,sys

files=sorted(glob.glob('artifacts/**/*.json',recursive=True))
rows=[]; parse_errors=[]
for path in files:
    try:
        with open(path,'r',encoding='utf-8-sig') as f:
            obj=json.load(f)
        if obj.get('gate')!='ITER051C-FULL-WEYL3-EOM-ASSEMBLY':
            continue
        rows.append(obj)
    except Exception as exc:
        parse_errors.append({'path':path,'error':repr(exc)})

expected={'A':4,'B':6,'C':4,'D':4}
keys=[(r.get('stream'),r.get('index')) for r in rows]
unique=set(keys)
complete=(len(rows)==18 and len(unique)==18 and not parse_errors and all(sum(1 for r in rows if r.get('stream')==s)==n for s,n in expected.items()))
valid=[r for r in rows if r.get('control_valid') is True]
passed=[r for r in rows if r.get('lane_pass') is True]
if not complete or len(valid)!=18:
    status='ITER051C_CONTROL_OR_IMPLEMENTATION_INVALID'
elif len(passed)==18:
    status='PASS_SCOPED_FULL_COVARIANT_WEYL3_EOM_ASSEMBLY_CERTIFICATE'
else:
    status='SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY'

summary={
  'gate':'ITER051C-FULL-WEYL3-EOM-ASSEMBLY',
  'classification':status,
  'expected_scientific_lanes':18,
  'found_scientific_lanes':len(rows),
  'unique_lanes':len(unique),
  'controls_valid':len(valid)==18,
  'passes':len(passed),
  'fails':18-len(passed) if complete else None,
  'stream_counts':{s:sum(1 for r in rows if r.get('stream')==s) for s in expected},
  'parse_errors':parse_errors,
  'c6_status':'SYMBOLIC_UNFIXED',
  'interpretation_lock':'FULL_EOM_ASSEMBLY_CERTIFICATE_ONLY_NOT_C6_DETERMINATION_NOT_THEORY_CORRECTNESS_NOT_GLOBAL_NUMERICAL_THEOREM'
}
if rows:
    A=[r for r in rows if r.get('stream')=='A']; B=[r for r in rows if r.get('stream')=='B']; C=[r for r in rows if r.get('stream')=='C']; D=[r for r in rows if r.get('stream')=='D']
    summary['worst']={
      'A_H_symmetry':max([float(r['H_symmetry_residual']) for r in A],default=None),
      'A_H_step_change':max([float(r['H_final_step_change']) for r in A],default=None),
      'A_riemann_algebraic':max([float(r['riemann_algebraic_residual']) for r in A],default=None),
      'A_P_algebraic':max([float(r['P_algebraic_residual']) for r in A],default=None),
      'B_exact_reduced_residual':max([max(map(float,r['relative_residuals'])) for r in B],default=None),
      'B_final_step_change':max([float(r['final_step_change']) for r in B],default=None),
      'C_I3_abs':max([float(r['I3_abs']) for r in C],default=None),
      'C_P_norm':max([float(r['P_norm']) for r in C],default=None),
      'C_H_norm':max([float(r['H_norm']) for r in C],default=None),
      'D_covariance':max([float(r['covariance_relative_residual']) for r in D],default=None),
    }
summary['frozen_thresholds']={
 'A_inverse_max':2e-11,'A_Riemann_algebraic_max':2e-9,'A_P_algebraic_max':2e-9,'A_H_symmetry_max':3e-7,'A_H_norm_min':1e-7,'A_H_step_change_max':2e-3,
 'B_exact_reduced_residual_max':3e-4,'B_step_change_max':2e-4,
 'C_I3_abs_max':2e-10,'C_P_norm_max':3e-9,'C_H_norm_max':2e-7,
 'D_covariance_max':8e-4,'D_transform_controls_max':2e-11
}
os.makedirs('iter051c-summary',exist_ok=True)
with open('iter051c-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,indent=2,sort_keys=True)
print(json.dumps(summary,sort_keys=True))
if status=='ITER051C_CONTROL_OR_IMPLEMENTATION_INVALID': sys.exit(2)
