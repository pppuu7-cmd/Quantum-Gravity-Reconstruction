#!/usr/bin/env python3
import glob,json,os,sys
rows=[]; errors=[]
for f in sorted(glob.glob('artifacts/qgr-iter053-qd2-*/*.json')):
    try:
        with open(f,encoding='utf-8') as h: rows.append(json.load(h))
    except Exception as e: errors.append({'file':f,'error':repr(e)})
expected=8
counts={s:sum(r.get('stream')==s for r in rows) for s in 'ABC'}
valid=sum(bool(r.get('control_valid')) for r in rows)
conv=sum(bool(r.get('converged')) for r in rows)
ok=(len(rows)==expected and not errors and counts=={'A':4,'B':2,'C':2} and valid==expected and conv==expected)
summary={
 'gate':'ITER053-QD2-SUPPORT-DIRECT-QUADRATURE-CONVERGENCE','expected_lanes':expected,
 'found_lanes':len(rows),'valid_lanes':valid,'converged_lanes':conv,'stream_counts':counts,'parse_errors':errors,
 'classification':'PASS_DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_CONVERGED_BY_GL8' if ok else 'DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_NOT_CONVERGED_BY_GL8',
 'interpretation_lock':'DIRECT-ACTION QUADRATURE DIAGNOSTIC ONLY; NO H5 BULK CERTIFICATE; ITER053 SCIENTIFIC CLASSIFICATION UNCHANGED; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0'
}
if rows:
    generic=[r for r in rows if r.get('stream') in ('A','C')]
    null=[r for r in rows if r.get('stream')=='B']
    if generic:
        summary['worst_generic_6_to_7_relative']=max(r['changes']['6_to_7_relative'] for r in generic)
        summary['worst_generic_7_to_8_relative']=max(r['changes']['7_to_8_relative'] for r in generic)
    if null:
        summary['worst_null_abs_GL8']=max(abs(r['orders']['8']['value']) for r in null)
        summary['worst_null_7_to_8_absolute']=max(r['changes']['7_to_8_absolute'] for r in null)
os.makedirs('iter053-qd2-summary',exist_ok=True)
with open('iter053-qd2-summary/summary.json','w') as h: json.dump(summary,h,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if not ok: sys.exit(2)
