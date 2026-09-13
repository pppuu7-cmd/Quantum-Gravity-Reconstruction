#!/usr/bin/env python3
import glob,json,os
files=sorted(glob.glob('artifacts/**/lane.json',recursive=True))
rows=[]
for p in files:
    try:
        with open(p) as f: rows.append(json.load(f))
    except Exception: pass
expected=6
complete=len(rows)==expected
valid=complete and all(bool(r.get('control_valid')) for r in rows)
passes=sum(bool(r.get('lane_pass')) for r in rows)
if not valid:
    cls='ITER053T_IMPLEMENTATION_OR_CONTROL_INVALID'
elif passes==expected:
    cls='ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED'
else:
    cls='SCIENTIFIC_FAIL_ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE'
out={
 'gate':'ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT','classification':cls,
 'complete':complete,'valid':valid,'lane_count':len(rows),'passes':passes,
 'worst_nodewise_contraction_relative_residual':max([r.get('max_nodewise_contraction_relative_residual',float('inf')) for r in rows],default=None),
 'worst_weighted_GJ3_sum_covariance_relative_residual':max([r.get('weighted_GJ3_sum_covariance_relative_residual',float('inf')) for r in rows],default=None),
 'minimum_nontrivial_node_count':min([r.get('nontrivial_node_count',0) for r in rows],default=0),
 'minimum_wrong_congruence_relative_residual':min([r.get('wrong_congruence_max_relative_residual',0.0) for r in rows],default=0.0),
 'claim_lock':'Finite localization only. Iter053R remains historical scientific FAIL. theory established=0%; c6 unfixed; beta=1 unauthorized.'
}
os.makedirs('iter053t-summary',exist_ok=True)
with open('iter053t-summary/summary.json','w') as f: json.dump(out,f,sort_keys=True,indent=2)
print(json.dumps(out,sort_keys=True))
if cls=='ITER053T_IMPLEMENTATION_OR_CONTROL_INVALID': raise SystemExit(3)
if cls.startswith('SCIENTIFIC_FAIL'): raise SystemExit(2)
