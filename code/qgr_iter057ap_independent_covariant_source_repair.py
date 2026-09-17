#!/usr/bin/env python3
"""Target-blind source-faithful repair wrapper for Iter057AP constructor.

Repairs only defects documented before any U/X target comparison:
1. missing Cup helper wiring;
2. cubic Weyl contraction accidentally using one all-lowered C factor;
3. invalid hand-written algebraic projector for P=dI3/dR, replaced by the
   prospectively frozen 20-dimensional algebraic-Riemann Frechet solve.
No U/X target data are loaded here.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
import qgr_iter057ap_independent_covariant_source as m

_orig_p_controls = m.p_controls


def _fixed_cubic_and_Q(C,Cup,degree):
    # Frozen AO functional: I3 = C_ab^{cd} C_cd^{ef} C_ef^{ab}.
    Q=[[[[{} for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)]
    for a,b,c,d in product(range(m.N),repeat=4):
        val={}
        for e,f in product(range(m.N),repeat=2):
            val=m.add(val,m.mul(Cup[c][d][e][f],Cup[e][f][a][b],degree))
        Q[a][b][c][d]=m.trunc(val,degree)
    I={}
    for a,b,c,d in product(range(m.N),repeat=4):
        I=m.add(I,m.mul(Cup[a][b][c][d],Q[a][b][c][d],degree))
    return m.trunc(I,degree),Q


_BIVS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
_ENTRIES=[x for x in combinations_with_replacement(range(6),2) if x!=(2,3)]


def _biv_index_sign(a,b):
    if a==b:return None,0
    if a<b:return _BIVS.index((a,b)),1
    return _BIVS.index((b,a)),-1


def _basis_tensor(entry):
    S=[[F(0) for _ in range(6)] for __ in range(6)]
    i,j=entry;S[i][j]=S[j][i]=F(1)
    # frozen first-Bianchi relation S05-S14+S23=0
    S[2][3]=S[3][2]=-S[0][5]+S[1][4]
    B=[[[[F(0) for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)]
    for a,b,c,d in product(range(m.N),repeat=4):
        i,s1=_biv_index_sign(a,b);j,s2=_biv_index_sign(c,d)
        if s1 and s2:B[a][b][c][d]=F(s1*s2)*S[i][j]
    return B


_BASIS=[_basis_tensor(e) for e in _ENTRIES]


def _invert_fraction(A):
    n=len(A);aug=[list(map(F,A[i]))+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next((r for r in range(c,n) if aug[r][c]),None)
        if p is None:raise ArithmeticError('singular algebraic-Riemann Gram matrix')
        if p!=c:aug[c],aug[p]=aug[p],aug[c]
        pv=aug[c][c];aug[c]=[x/pv for x in aug[c]]
        for r in range(n):
            if r==c:continue
            z=aug[r][c]
            if z:aug[r]=[aug[r][j]-z*aug[c][j] for j in range(2*n)]
    return [row[n:] for row in aug]


_GRAM=[[sum((_BASIS[i][a][b][c][d]*_BASIS[j][a][b][c][d] for a,b,c,d in product(range(m.N),repeat=4)),F(0)) for j in range(20)] for i in range(20)]
_GRAM_INV=_invert_fraction(_GRAM)


def _frechet_on_basis(g,gi,Q,K4,degree):
    # Direct fixed-metric Frechet derivative of I3 under algebraic Riemann K.
    RicK=m.pmat()
    for b,d in product(range(m.N),repeat=2):
        val={}
        for a,c in product(range(m.N),repeat=2):
            k=K4[a][b][c][d]
            if k:val=m.add(val,m.scale(gi[a][c],k))
        RicK[b][d]=m.trunc(val,degree)
    ScK={}
    for b,d in product(range(m.N),repeat=2):ScK=m.add(ScK,m.mul(gi[b][d],RicK[b][d],degree))
    ScK=m.trunc(ScK,degree)
    CK=[[[[{} for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)]
    for a,b,c,d in product(range(m.N),repeat=4):
        val=m.const(K4[a][b][c][d])
        rt=m.add(m.sub(m.mul(g[a][c],RicK[d][b],degree),m.mul(g[a][d],RicK[c][b],degree)),
                 m.add(m.neg(m.mul(g[b][c],RicK[d][a],degree)),m.mul(g[b][d],RicK[c][a],degree)))
        gg=m.sub(m.mul(g[a][c],g[d][b],degree),m.mul(g[a][d],g[c][b],degree))
        CK[a][b][c][d]=m.trunc(m.add(m.sub(val,m.scale(rt,F(1,2))),m.scale(m.mul(ScK,gg,degree),F(1,6))),degree)
    CKup=[[[[{} for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)]
    for a,b,c,d in product(range(m.N),repeat=4):
        val={}
        for e,f in product(range(m.N),repeat=2):
            val=m.add(val,m.mul(m.mul(gi[c][e],gi[d][f],degree),CK[a][b][e][f],degree))
        CKup[a][b][c][d]=m.trunc(val,degree)
    out={}
    for a,b,c,d in product(range(m.N),repeat=4):out=m.add(out,m.mul(CKup[a][b][c][d],Q[a][b][c][d],degree))
    return m.scale(m.trunc(out,degree),3)


def _fixed_p_from_frechet(g,gi,C,Cup,Q,degree):
    dvec=[_frechet_on_basis(g,gi,Q,B,degree) for B in _BASIS]
    coeff=[]
    for j in range(20):
        val={}
        for i in range(20):
            if _GRAM_INV[j][i]:val=m.add(val,m.scale(dvec[i],_GRAM_INV[j][i]))
        coeff.append(m.trunc(val,degree))
    P=[[[[{} for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)] for _ in range(m.N)]
    for a,b,c,d in product(range(m.N),repeat=4):
        val={}
        for j,B in enumerate(_BASIS):
            z=B[a][b][c][d]
            if z:val=m.add(val,m.scale(coeff[j],z))
        P[a][b][c][d]=m.trunc(val,degree)
    # Plow is not used by the frozen control or AO source; retain interface.
    return P,None


def _fixed_p_controls(P,Plow,I,Rlow,g,gi):
    # Frozen constructor independently requires C == Rlow on the canonical
    # Ricci-flat seed. Rebuild Cup solely for the unchanged Frechet helper.
    m.Cup=m.raise_last(Rlow,gi,8)
    return _orig_p_controls(P,Plow,I,Rlow,g,gi)


m.cubic_and_Q=_fixed_cubic_and_Q
m.p_from_frechet_projection=_fixed_p_from_frechet
m.p_controls=_fixed_p_controls

if __name__=='__main__':
    raise SystemExit(m.main())
