#!/usr/bin/env python3
import glob,json
fs=sorted(glob.glob('artifacts/qgr-iter051a-d2-lane-*/*.json')); lanes=[]
for f in fs:
    with open(f,'r',encoding='utf-8') as h: lanes.append(json.load(h))
ids=sorted(x['lane'] for x in lanes)
valid=(len(lanes)==3 and ids==[0,2,9] and all(x.get('valid') for x in lanes))
passes=sum(bool(x.get('pass')) for x in lanes)
if not valid: c='INVALID_DIAGNOSTIC_CONTROLS'
elif passes==3: c='DIAGNOSTIC_COMPLEX_STEP_STABLE_3_OF_3'
elif passes==0: c='DIAGNOSTIC_COMPLEX_STEP_UNSTABLE_3_OF_3'
else: c='DIAGNOSTIC_COMPLEX_STEP_INSTABILITY_PRESENT'
out={'classification':c,'found_lanes':len(lanes),'passes':passes,'lane_ids':ids,'max_relative_spread':max([x['relative_spread'] for x in lanes],default=None),'max_direction_covariance_rel':max([max(x['covariance_direction_rel']) for x in lanes],default=None)}
with open('iter051a-d2-summary.json','w',encoding='utf-8') as h: json.dump(out,h,indent=2,sort_keys=True)
print(json.dumps(out,indent=2,sort_keys=True))
if c=='INVALID_DIAGNOSTIC_CONTROLS': raise SystemExit(2)
