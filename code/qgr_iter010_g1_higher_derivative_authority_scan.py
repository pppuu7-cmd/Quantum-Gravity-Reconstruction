#!/usr/bin/env python3
import json
from pathlib import Path

# Canonical scientific authority lives in iteration/result/recovery records.  Source-code audit
# scripts are intentionally excluded because they may contain marker names as search literals.
roots=[Path('iterations'),Path('results'),Path('recovery')]
files=[]
for root in roots:
    if root.exists():
        for p in root.rglob('*'):
            if p.is_file() and p.suffix in {'.md','.json'}:
                try: files.append((str(p),p.read_text(encoding='utf-8',errors='ignore')))
                except OSError: pass
markers=[
 'EXACT_'+'FINITE_CELL_ACTION_CLOSED',
 'UNIQUE_'+'EXACT_FINITE_CELL_ACTION',
 'MICROSCOPIC_'+'FINITE_CELL_ACTION_ALL_ORDERS_CLOSED',
 'C6_'+'FIXED_BY_MICROSCOPIC_FINITE_CELL_ACTION',
 'WEYL3_'+'MICROSCOPIC_COEFFICIENT_DERIVED'
]
hits=[]
for path,txt in files:
    for m in markers:
        if m in txt: hits.append({'path':path,'marker':m})
assert hits==[],hits
related=[]
for path,txt in files:
    lo=txt.lower()
    if 'weyl^3' in lo or 'weyl3' in lo or 'finite-cell action' in lo or 'finite_cell_action' in lo:
        related.append(path)
out={
 'gate':'ITER010-G1-HIGHER-DERIVATIVE-AUTHORITY-SCAN',
 'authority_roots':['iterations','results','recovery'],
 'files_scanned':len(files),
 'positive_exact_uv_closure_markers':len(hits),
 'related_records':len(set(related)),
 'classification':'BLOCKED_SCOPED_NO_ALREADY_FROZEN_EXACT_HIGHER_DERIVATIVE_FINITE_CELL_RULE_OR_DERIVED_C6_COEFFICIENT_FOUND_IN_CURRENT_REPOSITORY_AUTHORITY',
 'guard':'This is an authority-completeness audit, not a theorem that no such microscopic rule can be derived in Iter010.'
}
print(json.dumps(out,sort_keys=True))
