#!/usr/bin/env python3
"""Frozen aggregate classifier for preregistered QGR Iter047."""
from __future__ import annotations
import glob, json, os
from collections import Counter

EXPECTED={'A':6,'B':6,'C':6,'D':6}
rows=[]
for path in glob.glob('iter047-results/**/result.json',recursive=True):
    with open(path,encoding='utf-8') as f:
        rows.append(json.load(f))

counts=Counter(r.get('stream') for r in rows)
valid_shape=(len(rows)==24 and all(counts.get(k,0)==v for k,v in EXPECTED.items()))
controls=valid_shape and all(r.get('control_valid') is True for r in rows)
passes=sum(r.get('lane_pass') is True for r in rows)
fails=len(rows)-passes

if not valid_shape or not controls:
    classification='ITER047_CONTROL_OR_IMPLEMENTATION_INVALID'
elif passes==24:
    classification='PASS_SCOPED_EXACT_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP'
elif passes>=12:
    classification='PARTIAL_SCOPED_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP'
else:
    classification='FAIL_SCOPED_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP'

summary={
    'gate':'ITER047-EXACT-WEYL3-CURVATURE-CLASS-ACTIVATION-MAP',
    'expected_scientific_lanes':24,
    'found_scientific_lanes':len(rows),
    'stream_counts':dict(counts),
    'controls_valid':bool(controls),
    'passes':passes,
    'fails':fails,
    'classification':classification,
    'c6_status':'SYMBOLIC_UNFIXED',
    'interpretation_lock':'OPERATOR_ACTIVATION_MAP_ONLY_NOT_SIX_DERIVATIVE_EOM_NOT_C6_DETERMINATION',
}
os.makedirs('iter047-summary',exist_ok=True)
with open('iter047-summary/summary.json','w',encoding='utf-8') as f:
    json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if classification=='ITER047_CONTROL_OR_IMPLEMENTATION_INVALID':
    raise SystemExit(2)
