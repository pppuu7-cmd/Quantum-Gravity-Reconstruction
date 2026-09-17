#!/usr/bin/env python3
"""Execution-only wrapper for Iter057AP frozen constructor.

Repairs only the missing Cup helper wiring documented in
reviews/ITER057AP_CONSTRUCTOR_CUP_WIRING_DEFECT.md.  No U/X target data are
loaded here.
"""
import qgr_iter057ap_independent_covariant_source as m

_orig = m.p_controls

def _fixed_p_controls(P,Plow,I,Rlow,g,gi):
    # Frozen constructor independently requires C == Rlow on the canonical
    # Ricci-flat seed.  Rebuild the same raised Weyl tensor solely for the
    # Frechet-control helper, then invoke the unchanged frozen helper.
    m.Cup = m.raise_last(Rlow,gi,8)
    return _orig(P,Plow,I,Rlow,g,gi)

m.p_controls = _fixed_p_controls

if __name__ == '__main__':
    raise SystemExit(m.main())
