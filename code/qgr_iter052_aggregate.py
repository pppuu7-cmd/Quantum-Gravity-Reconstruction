#!/usr/bin/env python3
import glob, json, os, sys

files=sorted(glob.glob('artifacts/qgr-iter052-*/*.json'))
rows=[]; parse_errors=[]
for f in files:
    try:
        with open(f,encoding='utf-8') as h: rows.append(json.load(h))
    except Exception as e:
        parse_errors.append({'file':f,'error':repr(e)})
expected=12
valid=sum(bool(r.get('control_valid')) for r in rows)
passes=sum(bool(r.get('lane_pass')) for r in rows)
fails=len(rows)-passes
counts={s:sum(r.get('stream')==s for r in rows) for s in 'ABC'}
controls_ok=(len(rows)==expected and not parse_errors and valid==expected and counts=={'A':6,'B':3,'C':3})
ok=bool(controls_ok and passes==expected)
if not controls_ok:
    cls='ITER052_IMPLEMENTATION_OR_CONTROL_INVALID'
elif ok:
    cls='PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE'
else:
    cls='SCIENTIFIC_FAIL_ITER052_WEYL3_4D_DIRECTIONAL_VARIATION_IDENTITY'
summary={
  'gate':'ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION',
  'expected_lanes':expected,'found_lanes':len(rows),'valid_lanes':valid,'passes':passes,'fails':fails,
  'stream_counts':counts,'parse_errors':parse_errors,'controls_valid':controls_ok,'classification':cls,
  'frozen_identity':'d_epsilon[sqrt(-g) W3] = H5^{ab} h_ab + partial_mu Theta^mu; H5=A+I-2 sqrt(-g) D5',
  'frozen_theta':'Theta^mu=2 sqrt(-g)[P^{mu(alpha beta)nu} nabla_nu h_ab - h_ab nabla_nu P^{mu(alpha beta)nu}]',
  'interpretation_lock':'FINITE GENUINELY-4D COMPUTATIONAL VARIATIONAL CERTIFICATE ONLY; HISTORICAL G51C/D2 FAILS UNCHANGED; C6 SYMBOLIC UNFIXED; NO GLOBAL THEOREM; THEORY_ESTABLISHED_0'
}
A=[r for r in rows if r.get('stream')=='A']; B=[r for r in rows if r.get('stream')=='B']; C=[r for r in rows if r.get('stream')=='C']
if A:
    summary['worst_A_identity_relative_residual']=max(r['identity_relative_residual'] for r in A)
    summary['worst_A_direct_step_change']=max(r['direct_final_step_change'] for r in A)
    summary['worst_A_identity_residual_step_change_abs']=max(r['identity_residual_step_change_abs'] for r in A)
if B:
    summary['worst_B_absolute_identity_mismatch']=max(r['absolute_identity_mismatch'] for r in B)
    summary['worst_B_H_norm']=max(r['H_norm'] for r in B)
    summary['worst_B_P_norm']=max(r['P_norm'] for r in B)
if C:
    summary['worst_C_base_identity_relative_residual']=max(r['base']['identity_relative_residual'] for r in C)
    summary['worst_C_transformed_identity_relative_residual']=max(r['transformed']['identity_relative_residual'] for r in C)
    summary['worst_C_direct_covariance_relative_residual']=max(r['direct_covariance_relative_residual'] for r in C)
    summary['worst_C_rhs_covariance_relative_residual']=max(r['rhs_covariance_relative_residual'] for r in C)
os.makedirs('iter052-summary',exist_ok=True)
with open('iter052-summary/summary.json','w') as h: json.dump(summary,h,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if not ok: sys.exit(2 if controls_ok else 3)
