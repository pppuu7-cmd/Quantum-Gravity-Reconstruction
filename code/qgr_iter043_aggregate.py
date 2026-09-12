#!/usr/bin/env python3
from __future__ import annotations
import glob,json,os

files=sorted(glob.glob('iter043-results/**/result.json',recursive=True))
rows=[]
for p in files:
    with open(p,encoding='utf-8') as f: rows.append(json.load(f))
by={r['index']:r for r in rows}
controls_valid=(len(by)==24 and all(bool(r.get('control_valid')) for r in by.values()))
passes=sum(bool(r.get('lane_pass')) for r in by.values())
if not controls_valid:
    cls='ITER043_CONTROL_OR_IMPLEMENTATION_INVALID'
elif passes==24:
    cls='PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE'
elif passes>0:
    cls='PARTIAL_SCOPED_TT_RADIATIVE_WEYL_COVARIANCE'
else:
    cls='FAIL_SCOPED_TT_RADIATIVE_WEYL_COVARIANCE'

def mx(k):
    return max((float(r[k]) for r in by.values()),default=float('nan'))
def mn(k):
    return min((float(r[k]) for r in by.values()),default=float('nan'))
summary={
 'gate':'ITER043-INDEPENDENT-TT-RADIATIVE-WEYL-COVARIANCE',
 'classification':cls,'expected_lanes':24,'found_unique_lanes':len(by),'lane_passes':passes,
 'controls_valid':controls_valid,
 'max_tt_trace':mx('tt_trace'),'max_tt_transverse_norm':mx('tt_transverse_norm'),
 'max_ricci_ratio':mx('ricci_ratio'),'max_scalar_ratio':mx('scalar_ratio'),
 'max_weyl_reconstruction_error':mx('weyl_reconstruction_error'),'max_lorentz_error':mx('lorentz_error'),
 'max_w2_covariance_error':mx('w2_covariance_error'),'max_w3_covariance_error':mx('w3_covariance_error'),
 'max_typeN_w2_null':mx('typeN_w2_null'),'max_typeN_w3_null':mx('typeN_w3_null'),
 'min_electric_norm':mn('electric_norm'),'min_magnetic_norm':mn('magnetic_norm'),
 'max_electric_magnetic_balance_error':mx('electric_magnetic_balance_error'),
 'claim_lock':'Scoped held-out analytic linearized TT-wave tensor/observable test only; not end-to-end QGR radiation dynamics, not nonlinear theorem, no beta/c6 fixing, no experimental confirmation.'
}
os.makedirs('iter043-summary',exist_ok=True)
with open('iter043-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,sort_keys=True,allow_nan=False)
print(json.dumps(summary,sort_keys=True,allow_nan=False))
