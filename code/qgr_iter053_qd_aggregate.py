#!/usr/bin/env python3
import glob,json,os,sys
rows=[]; errors=[]
for f in sorted(glob.glob('artifacts/qgr-iter053-qd-*/*.json')):
    try:
        with open(f,encoding='utf-8') as h: rows.append(json.load(h))
    except Exception as e: errors.append({'file':f,'error':repr(e)})
expected=8
valid=sum(bool(r.get('control_valid')) for r in rows)
confirmed=sum(bool(r.get('aliasing_confirmed')) for r in rows)
counts={s:sum(r.get('stream')==s for r in rows) for s in 'ABC'}
ok=(len(rows)==expected and not errors and valid==expected and confirmed==expected and counts=={'A':4,'B':2,'C':2})
summary={
 'gate':'ITER053-QD-COMPACT-SUPPORT-QUADRATURE-CONDITIONING',
 'expected_lanes':expected,'found_lanes':len(rows),'valid_lanes':valid,'confirmed_lanes':confirmed,
 'stream_counts':counts,'parse_errors':errors,
 'classification':'PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED' if ok else 'DIAGNOSTIC_ITER053_QUADRATURE_ALIASING_NOT_CONFIRMED',
 'interpretation_lock':'NUMERICAL QUADRATURE DIAGNOSTIC ONLY; ITER053 SCIENTIFIC CLASSIFICATION UNCHANGED; NO THRESHOLD RETUNING; C6 SYMBOLIC UNFIXED; THEORY_ESTABLISHED_0'
}
if rows:
    summary['outer_order3_nonzero_nodes']=sorted(set(r['outer']['3']['tensor_nonzero_nodes'] for r in rows))
    summary['outer_order4_nonzero_nodes']=sorted(set(r['outer']['4']['tensor_nonzero_nodes'] for r in rows))
    summary['min_pure_bump_error_improvement']=min(r['support5_vs_outer4_pure_bump_error_improvement'] for r in rows)
    summary['worst_direct_outer_3_to_4_change']=max(r['direct_outer_3_to_4_change'] for r in rows)
    summary['worst_direct_support_3_to_4_change']=max(r['direct_support_3_to_4_change'] for r in rows)
    summary['worst_direct_support_4_to_5_change']=max(r['direct_support_4_to_5_change'] for r in rows)
os.makedirs('iter053-qd-summary',exist_ok=True)
with open('iter053-qd-summary/summary.json','w') as h: json.dump(summary,h,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if not ok: sys.exit(2)
