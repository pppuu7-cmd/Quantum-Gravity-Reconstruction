#!/usr/bin/env python3
from __future__ import annotations
import glob,json,math,os
EXPECTED={'A':8,'B':6,'C':4,'D':6}
rows=[]
for p in glob.glob('iter042r-results/**/result.json',recursive=True):
    try:
        with open(p,encoding='utf-8') as f: d=json.load(f)
        if d.get('gate')=='ITER042R': rows.append(d)
    except Exception: pass
rows=list({(r.get('stream'),int(r.get('index',-1))):r for r in rows}.values())
counts={s:sum(r.get('stream')==s for r in rows) for s in EXPECTED}
passes={s:sum(r.get('stream')==s and r.get('lane_pass') is True for r in rows) for s in EXPECTED}
complete=len(rows)==24 and all(counts[s]==EXPECTED[s] for s in EXPECTED)
controls=complete and all(r.get('control_valid') is True for r in rows)
a_fail=any(r.get('stream')=='A' and r.get('control_valid') is True and r.get('lane_pass') is not True for r in rows)
allpass=controls and all(r.get('lane_pass') is True for r in rows)
if not complete or not controls: classification='CONTROL_INVALID_OR_INCOMPLETE_ITER042R'
elif a_fail: classification='FAIL_SCOPED_EXISTING_WEYL_SCALAR_CONTRACTION_NOT_LORENTZ_INVARIANT'
elif allpass: classification='PASS_SCOPED_G42_COVARIANCE_DEFECT_ATTRIBUTED_TO_MIXED_FRAME_RECONSTRUCTION_AND_FRAME_COMPLETION_VALIDATED'
else: classification='PARTIAL_SCOPED_G42_FRAME_COMPLETION_DIAGNOSTIC'
def vals(s,k): return [float(r[k]) for r in rows if r.get('stream')==s and r.get(k) is not None and math.isfinite(float(r[k]))]
A2=vals('A','w2_relative_change'); A3=vals('A','w3_relative_change'); B2=vals('B','finest_w2_error'); B3=vals('B','finest_w3_error'); Cmix=vals('C','mixed_finest_w3_error'); Cnew=vals('C','completed_finest_w3_error')
summary={'gate':'ITER042R-FRAME-COMPLETION-COVARIANCE-DIAGNOSTIC','classification':classification,'expected_lanes':24,'found_unique_lanes':len(rows),'counts':counts,'passes':passes,'controls_valid':controls,
         'maximum_exact_transform_w2_relative_change':max(A2) if A2 else None,
         'maximum_exact_transform_w3_relative_change':max(A3) if A3 else None,
         'maximum_completed_finest_w2_error':max(B2) if B2 else None,
         'maximum_completed_finest_w3_error':max(B3) if B3 else None,
         'mixed_finest_w3_error_range':[min(Cmix),max(Cmix)] if Cmix else None,
         'completed_finest_w3_error_range':[min(Cnew),max(Cnew)] if Cnew else None,
         'decision':('If full PASS, retain original G42 PARTIAL as the discovery record, adopt frame-completed observables for future boosted/dynamical work, and only then move to an independent radiative geometry.' if allpass else 'Do not proceed to independent radiative production until the scalar/frame diagnostic is resolved; do not weaken thresholds.'),
         'claim_lock':'Corrective diagnostic does not rewrite the original frozen G42 verdict and does not prove global QGR Lorentz covariance.'}
os.makedirs('iter042r-summary',exist_ok=True)
with open('iter042r-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,sort_keys=True,allow_nan=False)
print(json.dumps(summary,sort_keys=True,allow_nan=False))
