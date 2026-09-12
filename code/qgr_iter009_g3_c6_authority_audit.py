#!/usr/bin/env python3
import json
from pathlib import Path

roots = [Path('iterations'), Path('results'), Path('recovery'), Path('code')]
texts = []
for root in roots:
    if root.exists():
        for p in root.rglob('*'):
            if p.is_file() and p.suffix in {'.md','.json','.py'} and p.name != 'qgr_iter009_g3_c6_authority_audit.py':
                try:
                    texts.append((str(p), p.read_text(encoding='utf-8', errors='ignore')))
                except OSError:
                    pass

positive_markers = [
    'QGR_SIX_DERIVATIVE_COEFFICIENT_FIXED',
    'WEYL_CUBED_COEFFICIENT_FIXED',
    'RIEMANN_CUBED_COEFFICIENT_FIXED',
    'EXACT_FINITE_CELL_SIX_DERIVATIVE_MATCHING_CLOSED'
]
positive = []
for path, txt in texts:
    for marker in positive_markers:
        if marker in txt:
            positive.append((path, marker))
assert not positive

related = []
for path, txt in texts:
    low = txt.lower()
    if 'six derivative' in low or 'six-derivative' in low or 'weyl' in low and 'cub' in low or 'riemann' in low and 'cub' in low:
        related.append(path)

out = {
    "gate": "ITER009-G3-C6-AUTHORITY",
    "files_scanned": len(texts),
    "positive_fixed_coefficient_markers": len(positive),
    "related_records": len(set(related)),
    "classification": "BLOCKED_SCOPED_NO_AUTHORITATIVE_QGR_MICROSCOPIC_MATCHING_CURRENTLY_FIXES_THE_UNIQUE_PARITY_EVEN_SIX_DERIVATIVE_VACUUM_COEFFICIENT_C6",
    "guard": "Repository authority audit only; the coefficient may be derivable from a future exact finite-cell action, but it is not presently frozen."
}
print(json.dumps(out, sort_keys=True))
