#!/usr/bin/env python3
import json,re
from pathlib import Path

roots=[Path('iterations'),Path('results'),Path('recovery')]
files=[]
for root in roots:
    if root.exists():
        for p in root.rglob('*'):
            if p.is_file() and p.suffix in {'.md','.json'}:
                try: files.append((str(p),p.read_text(encoding='utf-8',errors='ignore')))
                except OSError: pass
# These markers would constitute an authoritative nonhomogeneous c6 match if present.
markers=[
 'C6_ABSOLUTE_MICROSCOPIC_MATCH_CLOSED',
 'C6_FIXED_BY_ABSOLUTE_BRANCH_PHASE',
 'C6_FIXED_BY_EXACT_REFINEMENT_TARGET',
 'WEYL3_COEFFICIENT_DERIVED_FROM_FINITE_CELL_ACTION',
 'NONHOMOGENEOUS_C6_MATCHING_CLOSED'
]
hits=[]
for path,txt in files:
    for marker in markers:
        if marker in txt:hits.append({'path':path,'marker':marker})
assert hits==[],hits
# Record known negative/partial authority that bears directly on the route.
known=[]
needles=['overall kappa','does not fix kappa','no authoritative exact finite-cell','absolute scale still open','c6` is not','c6 is not']
for path,txt in files:
    lo=txt.lower()
    if any(n.lower() in lo for n in needles):known.append(path)
out={
 'gate':'ITER010-G4-NONHOMOGENEOUS-AUTHORITY-SCAN',
 'files_scanned':len(files),
 'positive_nonhomogeneous_c6_match_markers':len(hits),
 'related_negative_or_open_records':len(set(known)),
 'classification':'BLOCKED_SCOPED_NO_CANONICAL_QGR_RECORD_SUPPLIES_A_NONHOMOGENEOUS_ABSOLUTE_MICROSCOPIC_ACTION_PHASE_OR_REFINEMENT_TARGET_THAT_FIXES_C6',
 'guard':'Repository authority audit only. It identifies the missing input; it is not a theorem that a future microscopic derivation cannot supply it.'
}
print(json.dumps(out,sort_keys=True))
