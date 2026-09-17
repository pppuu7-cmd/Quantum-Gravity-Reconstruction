#!/usr/bin/env python3
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / 'iter057ao_phase2_parts'
EXPECTED = '7cc63a46cba36fe903095494876028d9e7ebbe163a60ae35978372756a0ddf4a'
parts = sorted(PARTS.glob('part*.txt'))
if len(parts) != 6:
    raise SystemExit(f'expected 6 source parts, found {len(parts)}')
src = ''.join(p.read_text() for p in parts)
got = hashlib.sha256(src.encode()).hexdigest()
if got != EXPECTED:
    raise SystemExit(f'assembled source sha256 mismatch: {got}')
ns = {'__name__': '__main__', '__file__': str(ROOT / 'qgr_iter057ao_phase2_assembled.py')}
exec(compile(src, ns['__file__'], 'exec'), ns)
