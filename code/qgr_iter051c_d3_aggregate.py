#!/usr/bin/env python3
import glob, json, os, sys

files=sorted(glob.glob('artifacts/qgr-iter051c-d3-*/*.json'))
rows=[]; parse_errors=[]
for f in files:
    try:
        with open(f,encoding='utf-8') as h: rows.append(json.load(h))
    except Exception as e:
        parse_errors.append({'file':f,'error':repr(e)})
expected=16
valid=sum(bool(r.get('control_valid')) for r in rows)
passes=sum(bool(r.get('lane_pass')) for r in rows)
fails=len(rows)-passes
ok=(len(rows)==expected and not parse_errors and valid==expected and passes==expected)
summary={
  'gate':'ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT',
  'expected_lanes':expected,'found_lanes':len(rows),'valid_lanes':valid,'passes':passes,'fails':fails,
  'parse_errors':parse_errors,
  'classification':'PASS_SCOPED_G51C_D3_FIVEPOINT_FULL_EOM_REPLACEMENT_CERTIFICATE' if ok else 'SCIENTIFIC_FAIL_G51C_D3_FIVEPOINT_FULL_EOM_REPLACEMENT',
  'interpretation_lock':'FINITE COMPUTATIONAL CERTIFICATE ONLY; HISTORICAL G51C/D2 FAILS UNCHANGED; DOES NOT ESTABLISH GLOBAL 4D THEOREM OR QGR CORRECTNESS; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0'
}
if rows:
    b=[r for r in rows if r.get('stream')=='B']
    a=[r for r in rows if r.get('stream')=='A']
    d=[r for r in rows if r.get('stream')=='D']
    c=[r for r in rows if r.get('stream')=='C']
    if b:
        summary['worst_B_component_relative_residual']=max(max(r['component_relative_residuals']) for r in b)
        summary['worst_B_vector_relative_residual']=max(r['vector_relative_residual'] for r in b)
        summary['minimum_B_historical_plus2_residual']=min(r['historical_plus2_vector_residual'] for r in b)
    if a: summary['worst_A_final_step_change']=max(r['H_final_step_change'] for r in a)
    if d: summary['worst_D_covariance_relative_residual']=max(r['covariance_relative_residual'] for r in d)
    if c: summary['worst_C_H_norm']=max(r['H_norm'] for r in c)
os.makedirs('iter051c-d3-summary',exist_ok=True)
with open('iter051c-d3-summary/summary.json','w') as h: json.dump(summary,h,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if not ok: sys.exit(2)
