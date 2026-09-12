#!/usr/bin/env python3
import glob,json,sys
files=glob.glob('artifacts/**/lane-*.json',recursive=True)
rows=[]
for f in files:
    with open(f) as h: rows.append(json.load(h))
rows=sorted(rows,key=lambda x:x['lane'])
valid=len(rows)==12 and len({r['lane'] for r in rows})==12
passes=sum(bool(r.get('pass')) for r in rows)
nonzero=sum(bool(r.get('nonzero_calibration')) for r in rows)
if not valid:
    cls='INVALID_COVARIANT_CURVATURE_DATA_OR_CONTROL'
elif passes==12 and nonzero>=10:
    cls='PASS_SCOPED_COVARIANT_WEYL3_CURVATURE_DIRECTIONAL_VARIATION_PREREQUISITE'
else:
    cls='SCIENTIFIC_FAIL_WEYL3_CURVATURE_DIRECTIONAL_CERTIFICATE'
out={'classification':cls,'found_lanes':len(rows),'passes':passes,'nonzero_calibration_lanes':nonzero,'expected_lanes':12,'max_algebraic_residual':max([r['algebraic_residual'] for r in rows],default=None),'max_weyl_trace_residual':max([r['weyl_trace_residual'] for r in rows],default=None),'max_finest_rel':max([r['finest_rel'] for r in rows],default=None),'max_scalar_covariance_rel':max([max(x[0] for x in r['covariance']) for r in rows],default=None),'max_direction_covariance_rel':max([max(x[1] for x in r['covariance']) for r in rows],default=None)}
print(json.dumps(out,indent=2,sort_keys=True))
with open('iter050-summary.json','w') as f: json.dump(out,f,indent=2,sort_keys=True)
if cls!='PASS_SCOPED_COVARIANT_WEYL3_CURVATURE_DIRECTIONAL_VARIATION_PREREQUISITE': sys.exit(2)
