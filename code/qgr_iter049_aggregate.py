#!/usr/bin/env python3
"""Frozen aggregate classifier for preregistered QGR Iter049."""
from __future__ import annotations
import glob,json,os
from collections import Counter
EXPECTED={'A':6,'B':6,'C':6,'D':6}
rows=[]
for path in glob.glob('iter049-results/**/result.json',recursive=True):
    with open(path,encoding='utf-8') as f: rows.append(json.load(f))
counts=Counter(x.get('stream') for x in rows)
shape=len(rows)==24 and all(counts.get(k,0)==v for k,v in EXPECTED.items())
controls=shape and all(x.get('control_valid') is True for x in rows)
passes=sum(x.get('lane_pass') is True for x in rows)
if not shape or not controls: cls='ITER049_CONTROL_OR_IMPLEMENTATION_INVALID'
elif passes==24: cls='PASS_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE'
elif passes>=12: cls='PARTIAL_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE'
else: cls='FAIL_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE'
summary={'gate':'ITER049-WEYL3-SPHERICALLY-REDUCED-VARIATIONAL-RESPONSE','expected_scientific_lanes':24,'found_scientific_lanes':len(rows),'stream_counts':dict(counts),'controls_valid':bool(controls),'passes':passes,'fails':len(rows)-passes,'classification':cls,'c6_status':'SYMBOLIC_UNFIXED_COEFFICIENT_ONLY','scope_lock':'RADIAL_GAUGE_UNFIXED_STATIC_SPHERICAL_REDUCED_VARIATION_ONLY_NOT_FULL_4D_COVARIANT_WEYL3_EOM'}
os.makedirs('iter049-summary',exist_ok=True)
with open('iter049-summary/summary.json','w',encoding='utf-8') as f: json.dump(summary,f,sort_keys=True,indent=2)
print(json.dumps(summary,sort_keys=True))
if cls=='ITER049_CONTROL_OR_IMPLEMENTATION_INVALID': raise SystemExit(2)
