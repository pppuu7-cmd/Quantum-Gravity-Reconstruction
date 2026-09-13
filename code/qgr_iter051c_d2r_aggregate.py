#!/usr/bin/env python3
import glob, json, os
files=sorted(glob.glob('artifacts/qgr-iter051c-d2r-*/lane-*.json'))
rows=[]; errors=[]
for p in files:
    try:
        with open(p) as f: rows.append(json.load(f))
    except Exception as e:
        errors.append(f'{p}: {e}')
valid=[r for r in rows if r.get('control_valid')]
passes=[r for r in valid if r.get('lane_pass')]
if len(rows)!=12 or len(valid)!=12 or errors:
    cls='INVALID_G51C_D2R_MISSING_OR_INVALID_LANES'
elif len(passes)==12:
    cls='PASS_SCOPED_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION'
else:
    cls='SCIENTIFIC_FAIL_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION'
summary={
 'gate':'ITER051C-D2R-FRESH-SPHERICAL-REPLACEMENT-VALIDATION','classification':cls,
 'expected_lanes':12,'found_lanes':len(rows),'valid_lanes':len(valid),'passes':len(passes),
 'fails':len(valid)-len(passes),'parse_errors':errors,
 'worst_vector_relative_residual':max([r['vector_relative_residual'] for r in valid],default=None),
 'worst_final_step_change':max([r['final_step_change'] for r in valid],default=None),
 'worst_absolute_component_error':max([max(r['absolute_errors']) for r in valid],default=None),
 'minimum_historical_plus2_vector_residual':min([r['historical_plus2_vector_residual'] for r in valid],default=None),
 'interpretation_lock':'FRESH FINITE SPHERICAL PANEL ONLY; HISTORICAL G51C/D2 FAILS UNCHANGED; DOES NOT ESTABLISH GLOBAL OR FULL 4D EOM; THEORY_ESTABLISHED_0',
 'c6_status':'SYMBOLIC_UNFIXED'
}
os.makedirs('iter051c-d2r-summary',exist_ok=True)
with open('iter051c-d2r-summary/summary.json','w') as f: json.dump(summary,f,indent=2,sort_keys=True)
print(json.dumps(summary,sort_keys=True))
if cls.startswith('INVALID_'): raise SystemExit(3)
if cls.startswith('SCIENTIFIC_FAIL_'): raise SystemExit(2)
