#!/usr/bin/env python3
"""Decision-equivalent accelerated Iter057AG evaluator.

Each equation row is multiplied by the LCM of its rational denominators before
FLINT RREF. Nonzero row scaling preserves the exact rational RREF, pivot order,
and therefore the prospectively frozen free-variables-zero canonical witness.
"""
import math
from fractions import Fraction as F
from flint import fmpz_mat
import qgr_iter057ag_dual_obstruction_witness as ag


def canonical_y_integer_rref(cols,O0):
    A=fmpz_mat(ag.NCOLS+1,ag.NROWS+1)
    # B^T rows; RHS is zero so arbitrary nonzero row clearing is exact-equivalent.
    for j in range(ag.NCOLS):
        d=cols[j]
        den=1
        for v in d.values(): den=math.lcm(den,v.denominator)
        for i,v in d.items(): A[j,i]=v.numerator*(den//v.denominator)
    # Prospectively frozen O0^T y = 1 row: scale both coefficients and RHS.
    vals=[ag.ff(x) for x in O0]
    den=1
    for v in vals:
        if v: den=math.lcm(den,v.denominator)
    for i,v in enumerate(vals):
        if v: A[ag.NCOLS,i]=v.numerator*(den//v.denominator)
    A[ag.NCOLS,ag.NROWS]=den
    R,D,rank=A.rref()
    D=int(D); rank=int(rank)
    piv=[]
    for r in range(rank):
        p=None
        for c in range(ag.NROWS):
            if R[r,c] != 0:
                p=c; break
        if p is None:
            if R[r,ag.NROWS] != 0: raise ArithmeticError('inconsistent normalized witness system')
            continue
        piv.append((r,p))
    if len({p for _,p in piv})!=len(piv): raise ArithmeticError('duplicate RREF pivots')
    y=[F(0)]*ag.NROWS
    for r,p in piv:
        if int(R[r,p]) != D: raise ArithmeticError('nonunit rational RREF pivot')
        y[p]=F(int(R[r,ag.NROWS]),D)
    return y,rank,[p for _,p in piv]

ag.canonical_y=canonical_y_integer_rref

if __name__=='__main__':
    raise SystemExit(ag.main())
