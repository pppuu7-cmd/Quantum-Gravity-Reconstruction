#!/usr/bin/env python3
"""Exact preregistered pre-comparison controls for the Weyl^3 target-blind panel.

This script implements only witness/control construction.  It does not read any
historical residual and does not compare the directional and functional lanes.
All arithmetic is Fraction-exact; c6 is kept as a factored symbolic scalar and
therefore omitted from the numerical coefficient tensors P/c6 and (nabla P)/c6.
"""
from fractions import Fraction as F
from itertools import product

D=4
eta=[F(-1),F(1),F(1),F(1)]
idx=list(product(range(D), repeat=4))

def zero4(): return {q:F(0) for q in idx}
def add(*ts): return {q:sum((t[q] for t in ts),F(0)) for q in idx}
def scale(a,t): return {q:a*t[q] for q in idx}

def K(p,q):
    A={(a,b):F(0) for a,b in product(range(D),repeat=2)}
    A[p,q]=F(1); A[q,p]=F(-1)
    return {(a,b,c,d):A[a,b]*A[c,d] for a,b,c,d in idx}

def ricci(R):
    # Ric_bd = g^{ac} R_abcd for diagonal eta.
    return {(b,d):sum((eta[a]*R[a,b,a,d] for a in range(D)),F(0))
            for b,d in product(range(D),repeat=2)}

def scalar(Ric): return sum((eta[a]*Ric[a,a] for a in range(D)),F(0))

def weyl(R):
    Ric=ricci(R); S=scalar(Ric)
    C=zero4()
    for a,b,c,d in idx:
        g=lambda i,j: eta[i] if i==j else F(0)
        C[a,b,c,d]=(R[a,b,c,d]
          - F(1,2)*(g(a,c)*Ric[b,d]-g(a,d)*Ric[b,c]-g(b,c)*Ric[a,d]+g(b,d)*Ric[a,c])
          + F(1,6)*S*(g(a,c)*g(b,d)-g(a,d)*g(b,c)))
    return C

def riemann_controls(R):
    for a,b,c,d in idx:
        if R[a,b,c,d] != -R[b,a,c,d]: return False
        if R[a,b,c,d] != -R[a,b,d,c]: return False
        if R[a,b,c,d] != R[c,d,a,b]: return False
        if R[a,b,c,d]+R[a,c,d,b]+R[a,d,b,c] != 0: return False
    return True

def tracefree(C):
    # Every Ricci-type contraction vanishes; pair symmetries reduce this to one.
    for b,d in product(range(D),repeat=2):
        if sum((eta[a]*C[a,b,a,d] for a in range(D)),F(0)) != 0: return False
    return True

def nonzero(T): return any(v != 0 for v in T.values())

def compose(C,Dd):
    # (C o D)_abef = C_ab{}^cd D_cd ef.
    out=zero4()
    for a,b,e,f in idx:
        out[a,b,e,f]=sum((eta[c]*eta[d]*C[a,b,c,d]*Dd[c,d,e,f]
                          for c,d in product(range(D),repeat=2)),F(0))
    return out

def p_over_c6(C):
    # Pi is the metric-orthogonal Weyl projector, hence Pi*=Pi on this pairing.
    return scale(F(3), weyl(compose(C,C)))

def dp_over_c6(C,dC):
    return scale(F(3), weyl(add(compose(dC,C),compose(C,dC))))

W=[
 (add(scale(2,K(0,1)),scale(3,K(2,3))),
  {0:add(scale(5,K(0,1)),scale(-2,K(2,3))),1:add(K(0,2),scale(2,K(1,3))) }),
 (add(K(0,1),scale(-2,K(0,2)),scale(4,K(1,3)),scale(3,K(2,3))),
  {0:add(scale(2,K(0,3)),K(1,2)),2:add(scale(-3,K(0,1)),scale(2,K(2,3))) }),
 (add(scale(3,K(0,3)),scale(2,K(1,2)),scale(-1,K(0,1)),K(2,3)),
  {1:add(scale(4,K(0,2)),scale(-1,K(1,3))),3:add(scale(2,K(0,1)),scale(3,K(2,3))) })
]

all_C_nonzero=False; all_dC_nonzero=False
for wi,(R,jets) in enumerate(W):
    assert riemann_controls(R), f'W{wi}: Riemann/Bianchi control failed'
    C=weyl(R)
    assert tracefree(C), f'W{wi}: Weyl trace failed'
    all_C_nonzero |= nonzero(C)
    P=p_over_c6(C)
    assert riemann_controls(P) and tracefree(P), f'W{wi}: P/c6 control failed'
    for e,dR in jets.items():
        assert riemann_controls(dR), f'W{wi}: jet {e} algebraic control failed'
        dC=weyl(dR)
        assert tracefree(dC), f'W{wi}: jet {e} Weyl trace failed'
        all_dC_nonzero |= nonzero(dC)
        dP=dp_over_c6(C,dC)
        assert riemann_controls(dP) and tracefree(dP), f'W{wi}: dP/c6 control failed'
    print(f'W{wi}: controls PASS; C_nonzero={nonzero(C)}; jets={sorted(jets)}')
assert all_C_nonzero, 'panel C nonzero control failed'
assert all_dC_nonzero, 'panel nabla-C nonzero control failed'
print('TARGET_BLIND_WITNESS_CONTROLS_V1=PASS')
print('c6=SYMBOLIC_UNFIXED (P/c6 and nablaP/c6 only)')
