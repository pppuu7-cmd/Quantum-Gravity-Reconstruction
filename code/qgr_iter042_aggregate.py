#!/usr/bin/env python3
from __future__ import annotations
import glob,json,math,os
EXPECTED={'A':6,'B':6,'C':4,'D':4,'E':4}
rows=[]
for p in glob.glob('iter042-results/**/result.json',recursive=True):
    try:
        with open(p,encoding='utf-8') as f: d=json.load(f)
        if d.get('gate')=='ITER042': rows.append(d)
    except Exception: pass
uniq={(r.get('stream'),int(r.get('index',-1))):r for r in rows}; rows=list(uniq.values())
counts={s:sum(r.get('stream')==s for r in rows) for s in EXPECTED}
passes={s:sum(r.get('stream')==s and r.get('lane_pass') is True for r in rows) for s in EXPECTED}
complete=len(rows)==sum(EXPECTED.values()) and all(counts[s]==EXPECTED[s] for s in EXPECTED)
controls=complete and all(r.get('control_valid') is True for r in rows)
allpass=controls and all(r.get('lane_pass') is True for r in rows)
if not complete or not controls: classification='CONTROL_INVALID_OR_INCOMPLETE_ITER042'
elif allpass: classification='PASS_SCOPED_NONSTATIC_MAGNETIC_WEYL_LORENTZ_COVARIANCE_BRIDGE'
else: classification='PARTIAL_SCOPED_NONSTATIC_MAGNETIC_WEYL_COVARIANCE'
def vals(s,k):
    return [float(r[k]) for r in rows if r.get('stream')==s and r.get(k) is not None and math.isfinite(float(r[k]))]
A=vals('A','magnetic_to_electric_ratio'); B2=vals('B','finest_w2_error'); B3=vals('B','finest_w3_error'); C=vals('C','finest_parity_error'); D3=vals('D','weyl_cubic_kappa_slope'); DB=vals('D','magnetic_kappa_slope'); E=vals('E','endpoint_growth')
summary={
 'gate':'ITER042-NONSTATIC-MAGNETIC-WEYL-LORENTZ-COVARIANCE-BRIDGE',
 'classification':classification,'expected_lanes':24,'found_unique_lanes':len(rows),'counts':counts,'passes':passes,'controls_valid':controls,
 'minimum_magnetic_to_electric_ratio':min(A) if A else None,
 'maximum_finest_w2_boost_discrepancy':max(B2) if B2 else None,
 'maximum_finest_w3_boost_discrepancy':max(B3) if B3 else None,
 'maximum_finest_boost_reversal_parity_error':max(C) if C else None,
 'boosted_weyl_cubic_kappa_slope_range':[min(D3),max(D3)] if D3 else None,
 'boosted_magnetic_kappa_slope_range':[min(DB),max(DB)] if DB else None,
 'minimum_velocity_endpoint_growth':min(E) if E else None,
 'decision':('Full PASS is a covariance/magnetic-observer bridge only. Next gate must use a genuinely independent time-dependent/radiative or magnetic-Weyl geometry; do not densify boosts.' if allpass else 'Do not weaken frozen thresholds. Localize any scientific failure by stream or repair controls only if invalid.'),
 'claim_lock':'Boosted static geometry is not a new dynamical solution. Scoped finite-cell covariance evidence only; beta/c6 remain unfixed/calibration directions; no experimental confirmation.'
}
os.makedirs('iter042-summary',exist_ok=True)
with open('iter042-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,sort_keys=True,allow_nan=False)
print(json.dumps(summary,sort_keys=True,allow_nan=False))
