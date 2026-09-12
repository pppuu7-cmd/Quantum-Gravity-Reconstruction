#!/usr/bin/env python3
from __future__ import annotations
import glob,json,math,os

EXPECTED={'A':6,'B':6,'C':4,'D':4,'E':4}
rows=[]
for p in glob.glob('iter041-results/**/result.json',recursive=True):
    try:
        with open(p,encoding='utf-8') as f: d=json.load(f)
        if d.get('gate')=='ITER041': rows.append(d)
    except Exception:
        pass

uniq={}
for r in rows:
    key=(r.get('stream'),int(r.get('index',-1)))
    uniq[key]=r
rows=list(uniq.values())
counts={s:sum(1 for r in rows if r.get('stream')==s) for s in EXPECTED}
passes={s:sum(1 for r in rows if r.get('stream')==s and r.get('lane_pass') is True) for s in EXPECTED}
expected_total=sum(EXPECTED.values())
complete=(len(rows)==expected_total and all(counts[s]==EXPECTED[s] for s in EXPECTED))
controls_valid=complete and all(r.get('control_valid') is True for r in rows)
all_pass=controls_valid and all(r.get('lane_pass') is True for r in rows)

if not complete or not controls_valid:
    classification='CONTROL_INVALID_OR_INCOMPLETE_ITER041'
elif all_pass:
    classification='PASS_SCOPED_HELDOUT_WEYL3_GENERALIZATION_AND_PREDICTION_CONTRACT_STRESS'
else:
    classification='PARTIAL_SCOPED_HELDOUT_WEYL3_GENERALIZATION'

def vals(stream,key):
    return [float(r[key]) for r in rows if r.get('stream')==stream and r.get(key) is not None and math.isfinite(float(r[key]))]

a_err=vals('A','relative_q_error')
b_err=vals('B','finest_relative_q_error')
c_ws=vals('C','weyl_norm_kappa_slope')
c_cs=vals('C','weyl_cubic_kappa_slope')
d_null=vals('D','finest_normalized_abs_cubic')
e_rot=vals('E','finest_relative_rotation_discrepancy')

summary={
 'gate':'ITER041-HELDOUT-WEYL3-GENERALIZATION-AND-PREDICTION-CONTRACT-STRESS',
 'classification':classification,
 'expected_lanes':expected_total,
 'found_unique_lanes':len(rows),
 'counts':counts,
 'passes':passes,
 'controls_valid':controls_valid,
 'maximum_fixed_scale_heldout_q_error':max(a_err) if a_err else None,
 'maximum_finest_refinement_heldout_q_error':max(b_err) if b_err else None,
 'weyl_norm_amplitude_slope_range':[min(c_ws),max(c_ws)] if c_ws else None,
 'weyl_cubic_amplitude_slope_range':[min(c_cs),max(c_cs)] if c_cs else None,
 'maximum_finest_rotated_null_normalized_cubic':max(d_null) if d_null else None,
 'maximum_finest_heldout_rotation_discrepancy':max(e_rot) if e_rot else None,
 'decision':(
   'If full PASS, stop densifying the weak static electric-tidal family and move to a genuinely new dynamical/magnetic-Weyl or non-static covariance sector while keeping beta/c6 explicit.'
   if all_pass else
   'Do not weaken frozen thresholds. Localize any held-out scientific failure by stream; repair only invalid controls if classification is control-invalid.'
 ),
 'claim_lock':'Scoped held-out weak static tidal-sector generalization only. Finite numerical convergence is not an arbitrary-spacetime theorem; beta and c6 remain unfixed/calibration directions; no experimental confirmation.'
}
os.makedirs('iter041-summary',exist_ok=True)
with open('iter041-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,sort_keys=True,allow_nan=False)
print(json.dumps(summary,sort_keys=True,allow_nan=False))
