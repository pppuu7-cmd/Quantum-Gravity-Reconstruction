#!/usr/bin/env python3
"""Frozen aggregate classifier for preregistered QGR Iter048."""
from __future__ import annotations
import glob,json,os
from collections import Counter

EXPECTED={'A':6,'B':6,'C':6,'D':6}
rows=[]
for path in glob.glob('iter048-results/**/result.json',recursive=True):
    with open(path,encoding='utf-8') as f:
        rows.append(json.load(f))
counts=Counter(r.get('stream') for r in rows)
shape=(len(rows)==24 and all(counts.get(k,0)==v for k,v in EXPECTED.items()))
controls=shape and all(r.get('control_valid') is True for r in rows)
passes=sum(r.get('lane_pass') is True for r in rows)
if not shape or not controls:
    cls='ITER048_CONTROL_OR_IMPLEMENTATION_INVALID'
elif passes==24:
    cls='PASS_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE'
elif passes>=12:
    cls='PARTIAL_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE'
else:
    cls='FAIL_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE'
summary={
    'gate':'ITER048-WEYL3-SYMMETRY-REDUCED-VARIATIONAL-RESPONSE',
    'expected_scientific_lanes':24,'found_scientific_lanes':len(rows),
    'stream_counts':dict(counts),'controls_valid':bool(controls),
    'passes':passes,'fails':len(rows)-passes,'classification':cls,
    'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY',
    'scope_lock':'LAPSE_RETAINING_AXISYMMETRIC_BIANCHI_I_REDUCED_VARIATION_ONLY_NOT_FULL_COVARIANT_SIX_DERIVATIVE_EOM',
}
os.makedirs('iter048-summary',exist_ok=True)
with open('iter048-summary/summary.json','w',encoding='utf-8') as f:
    json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if cls=='ITER048_CONTROL_OR_IMPLEMENTATION_INVALID':
    raise SystemExit(2)
