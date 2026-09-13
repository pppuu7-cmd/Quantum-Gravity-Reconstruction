#!/usr/bin/env python3
import glob,json,os,sys

EXPECTED={'A':8,'B':4,'C':4,'D':4}
GATE='ITER051C-D2-VARIATIONAL-SIGN-AND-HELDOUT-VALIDATION'

files=glob.glob('artifacts/qgr-iter051c-d2-*/*.json')+glob.glob('artifacts/**/*.json',recursive=True)
rows=[]; seen=set(); parse_errors=[]
for fn in files:
    if fn.endswith('summary.json'): continue
    try:
        with open(fn) as f: z=json.load(f)
    except Exception as e:
        parse_errors.append([fn,str(e)]); continue
    if z.get('gate')!=GATE or z.get('stream') not in EXPECTED: continue
    key=(z.get('stream'),z.get('index'))
    if key in seen: continue
    seen.add(key); rows.append(z)

expected=sum(EXPECTED.values())
counts={s:sum(1 for z in rows if z.get('stream')==s) for s in EXPECTED}
controls_valid=(len(rows)==expected and all(counts[s]==EXPECTED[s] for s in EXPECTED) and all(bool(z.get('control_valid')) for z in rows) and not parse_errors)
passes=sum(bool(z.get('lane_pass')) for z in rows)

if not controls_valid:
    cls='ITER051C_D2_CONTROL_OR_IMPLEMENTATION_INVALID'
elif passes==expected:
    cls='PASS_DIAGNOSTIC_G51C_D2_INDEPENDENT_SIGN_AND_HELDOUT_VALIDATION'
else:
    cls='SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION'

def vals(stream,key):
    return [float(z[key]) for z in rows if z.get('stream')==stream and key in z]

def vmax(stream,key):
    v=vals(stream,key); return max(v) if v else None

def vmin(stream,key):
    v=vals(stream,key); return min(v) if v else None

summary={
 'gate':GATE,'classification':cls,'expected_scientific_lanes':expected,'found_scientific_lanes':len(rows),
 'stream_counts':counts,'controls_valid':controls_valid,'passes':passes,'fails':len(rows)-passes,'parse_errors':parse_errors,
 'frozen_candidate':'H_D2=A+I-2*sqrt(-g)*D; no production fitting',
 'c6_status':'SYMBOLIC_UNFIXED',
 'worst':{
   'A_corrected_max_residual':vmax('A','corrected_max_residual'),
   'A_corrected_final_step_change':vmax('A','corrected_final_step_change'),
   'A_historical_plus2_min_residual':vmin('A','historical_plus2_vector_residual'),
   'B_corrected_max_residual':vmax('B','corrected_max_residual'),
   'B_corrected_final_step_change':vmax('B','corrected_final_step_change'),
   'B_historical_plus2_min_residual':vmin('B','historical_plus2_vector_residual'),
   'C_H_symmetry':vmax('C','H_symmetry_residual'),
   'C_H_step_change':vmax('C','H_final_step_change'),
   'C_H_covariance':vmax('C','H_covariance_residual'),
   'D_I3_abs':vmax('D','I3_abs'),'D_P_norm':vmax('D','P_norm'),'D_H_norm':vmax('D','H_norm')
 },
 'frozen_thresholds':{
   'A_corrected_residual_max':5e-4,'A_step_change_max':2e-4,'A_historical_plus2_residual_min':1e-2,
   'B_corrected_residual_max':1e-3,'B_step_change_max':4e-4,'B_historical_plus2_residual_min':1e-2,
   'C_H_norm_min':1e-7,'C_H_symmetry_max':3e-7,'C_step_change_max':2e-3,'C_covariance_max':1e-3,
   'D_riemann_norm_min':1e-6,'D_I3_abs_max':2e-10,'D_P_norm_max':3e-9,'D_H_norm_max':2e-7
 },
 'interpretation_lock':'D2_DIAGNOSTIC_ONLY; DOES_NOT_REWRITE_G51C; DOES_NOT_ESTABLISH_FULL_EOM; SEPARATE_PREREGISTERED_REPLACEMENT_GATE_REQUIRED; C6_UNFIXED; THEORY_ESTABLISHED_0'
}
os.makedirs('iter051c-d2-summary',exist_ok=True)
with open('iter051c-d2-summary/summary.json','w') as f: json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if cls=='ITER051C_D2_CONTROL_OR_IMPLEMENTATION_INVALID': sys.exit(3)
if cls=='SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION': sys.exit(2)
