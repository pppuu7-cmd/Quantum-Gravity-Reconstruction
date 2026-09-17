#!/usr/bin/env python3
"""Target-blind execution/source-faithful wrapper for Iter057AP constructor.

Repairs only defects documented before any U/X target comparison:
1. missing Cup helper wiring;
2. cubic Weyl contraction accidentally using one all-lowered C factor.
No U/X target data are loaded here.
"""
import qgr_iter057ap_independent_covariant_source as m

_orig_p = m.p_controls

def _fixed_cubic_and_Q(C,Cup,degree):
    # Frozen AO functional: I3 = C_ab^{cd} C_cd^{ef} C_ef^{ab}.
    Q=[[[[{} for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)]
    for a,b,c,d in m.product(range(m.N),repeat=4):
        val={}
        for e,f in m.product(range(m.N),repeat=2):
            val=m.add(val,m.mul(Cup[c][d][e][f],Cup[e][f][a][b],degree))
        Q[a][b][c][d]=m.trunc(val,degree)
    I={}
    for a,b,c,d in m.product(range(m.N),repeat=4):
        I=m.add(I,m.mul(Cup[a][b][c][d],Q[a][b][c][d],degree))
    return m.trunc(I,degree),Q

def _fixed_p_controls(P,Plow,I,Rlow,g,gi):
    # Frozen constructor independently requires C == Rlow on the canonical
    # Ricci-flat seed. Rebuild the same raised Weyl tensor solely for the
    # Frechet-control helper, then invoke the unchanged helper.
    m.Cup = m.raise_last(Rlow,gi,8)
    return _orig_p(P,Plow,I,Rlow,g,gi)

m.cubic_and_Q = _fixed_cubic_and_Q
m.p_controls = _fixed_p_controls

if __name__ == '__main__':
    raise SystemExit(m.main())
