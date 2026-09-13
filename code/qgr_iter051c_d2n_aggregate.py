#!/usr/bin/env python3
import glob,json,os,sys

GATE='ITER051C-D2N-NEAR-NULL-SPHERICAL-CONDITIONING'
EXPECTED={'A':6,'B':2}
files=glob.glob('artifacts/qgr-iter051c-d2n-*/*.json')+glob.glob('artifacts/**/*.json',recursive=True)
rows=[]; seen=set(); parse=[]
for fn in files:
    if fn.endswith('summary.json'): continue
    try:
        with open(fn) as f: z=json.load(f)
    except Exception as e:
        parse.append([fn,str(e)]); continue
    if z.get('gate')!=GATE or z.get('stream') not in EXPECTED: continue
    key=(z.get('stream'),z.get('index'))
    if key in seen: continue
    seen.add(key); rows.append(z)

expected=sum(EXPECTED.values())
counts={s:sum(1 for z in rows if z.get('stream')==s) for s in EXPECTED}
controls=(len(rows)==expected and not parse and all(counts[s]==EXPECTED[s] for s in EXPECTED) and all(bool(z.get('control_valid')) for z in rows))
passes=sum(bool(z.get('lane_pass')) for z in rows)
replay=[z for z in rows if z.get('is_D2_B3_replay')]
if not controls or len(replay)!=1:
    cls='ITER051C_D2N_CONTROL_OR_IMPLEMENTATION_INVALID'
elif passes==expected:
    cls='PASS_DIAGNOSTIC_D2N_NEAR_NULL_ERROR_COLLAPSES_UNDER_INDEPENDENT_FIVE_POINT_STENCIL'
else:
    cls='DIAGNOSTIC_FAIL_D2N_NEAR_NULL_MISMATCH_PERSISTS'

def vmax(k):
    v=[float(z[k]) for z in rows if k in z]; return max(v) if v else None

def vmin(k):
    v=[float(z[k]) for z in rows if k in z]; return min(v) if v else None

rp=replay[0] if replay else {}
summary={
 'gate':GATE,'classification':cls,'expected_scientific_lanes':expected,'found_scientific_lanes':len(rows),
 'stream_counts':counts,'controls_valid':controls,'passes':passes,'fails':len(rows)-passes,'parse_errors':parse,
 'method_lock':'M3 existing nested central vs independently implemented M5 five-point nested covariant derivative; no coefficient fitting',
 'replay':{
   'M3_angular_abs_error':(rp.get('M3_abs_errors') or [None,None,None])[2],
   'M5_angular_abs_error':(rp.get('M5_abs_errors') or [None,None,None])[2],
   'M5_over_M3_angular_abs_error_ratio':rp.get('M5_over_M3_angular_abs_error_ratio'),
   'M5_vector_relative_residual':rp.get('M5_vector_relative_residual'),
   'M5_final_step_change':rp.get('M5_final_step_change'),
   'M5_angular_sign_ok':rp.get('M5_angular_sign_ok'),
   'historical_plus2_vector_residual':rp.get('historical_plus2_vector_residual')
 },
 'panel_worst':{
   'M5_vector_relative_residual':vmax('M5_vector_relative_residual'),
   'M5_final_step_change':vmax('M5_final_step_change'),
   'historical_plus2_min_vector_residual':vmin('historical_plus2_vector_residual')
 },
 'frozen_replay_thresholds':{'M5_angular_abs_error_max':2e-9,'M5_over_M3_ratio_max':0.35,'M5_vector_relative_residual_max':5e-5,'M5_step_change_max':5e-5,'historical_plus2_residual_min':1e-2},
 'frozen_other_thresholds':{'M5_vector_relative_residual_max':1e-4,'M5_step_change_max':5e-5,'M5_max_component_abs_error_max':2e-7,'historical_plus2_residual_min':1e-2},
 'c6_status':'SYMBOLIC_UNFIXED',
 'interpretation_lock':'NUMERICAL_CONDITIONING_DIAGNOSTIC_ONLY; D2 HISTORICAL FAIL UNCHANGED; DOES_NOT ESTABLISH FULL EOM OR AUTHORIZE G51C-R1 DIRECTLY; THEORY_ESTABLISHED_0'
}
os.makedirs('iter051c-d2n-summary',exist_ok=True)
with open('iter051c-d2n-summary/summary.json','w') as f: json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if cls=='ITER051C_D2N_CONTROL_OR_IMPLEMENTATION_INVALID': sys.exit(3)
if cls=='DIAGNOSTIC_FAIL_D2N_NEAR_NULL_MISMATCH_PERSISTS': sys.exit(2)
