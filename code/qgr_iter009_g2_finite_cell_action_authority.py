#!/usr/bin/env python3
import json
from pathlib import Path

roots = [Path('iterations'), Path('results'), Path('recovery')]
texts = []
for root in roots:
    if root.exists():
        for p in root.rglob('*.md'):
            try:
                texts.append((str(p), p.read_text(encoding='utf-8', errors='ignore')))
            except OSError:
                pass

# Positive authority markers would have to state exact finite-cell/microscopic closure,
# not merely an all-orders local continuum action or a branch action evaluated in a truncation.
positive_markers = [
    'EXACT_FINITE_CELL_ACTION_CLOSED',
    'UNIQUE_EXACT_FINITE_CELL_ACTION',
    'MICROSCOPIC_FINITE_CELL_ACTION_ALL_ORDERS_CLOSED'
]
found_positive = []
for path, txt in texts:
    for marker in positive_markers:
        if marker in txt:
            found_positive.append((path, marker))

# Known scoped records that must not be misread as finite-cell closure.
scoped_hits = []
for path, txt in texts:
    if 'all-orders local' in txt.lower() or 'S_alpha' in txt or 'finite-cell action' in txt.lower():
        scoped_hits.append(path)

assert not found_positive
out = {
    "gate": "ITER009-G2-FINITE-CELL-ACTION-AUTHORITY",
    "authoritative_text_files_scanned": len(texts),
    "positive_exact_finite_cell_closure_markers": len(found_positive),
    "scoped_related_records_found": len(set(scoped_hits)),
    "classification": "BLOCKED_SCOPED_NO_AUTHORITATIVE_EXACT_FINITE_CELL_HIGHER_DERIVATIVE_ACTION_CLOSURE_FOUND_IN_CURRENT_REPOSITORY",
    "guard": "Repository authority audit only; absence of a closure record is not a mathematical no-go theorem."
}
print(json.dumps(out, sort_keys=True))
