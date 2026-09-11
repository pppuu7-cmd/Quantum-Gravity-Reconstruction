#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

# Dependency-free exact polynomial verification of the nonlinear transformation
# law induced by local reparametrization/pullback of the QGR second-moment field.
# This is a transformation-algebra audit, not an action-invariance proof.

N = 4


def clean(p):
    return {e:c for e,c in p.items() if c}


def add(a,b):
    d=defaultdict(Fraction)
    for e,c in a.items(): d[e]+=c
    for e,c in b.items(): d[e]+=c
    return clean(d)


def scale(a,s):
    return clean({e:c*s for e,c in a.items()})


def mul(a,b):
    d=defaultdict(Fraction)
    for e,c in a.items():
        for f,dv in b.items():
            d[tuple(e[i]+f[i] for i in range(N))]+=c*dv
    return clean(d)


def der(a,i):
    d=defaultdict(Fraction)
    for e,c in a.items():
        if e[i]:
            ee=list(e); ee[i]-=1
            d[tuple(ee)]+=c*e[i]
    return clean(d)


ONE={(0,0,0,0):Fraction(1)}

def var(i):
    e=[0]*N; e[i]=1
    return {tuple(e):Fraction(1)}

x=[var(i) for i in range(N)]

# Deterministic nontrivial polynomial vector fields.
xi=[]; eta=[]
for i in range(N):
    xi.append(add(scale(x[(i+1)%4], Fraction(i+1)), mul(x[i],x[(i+2)%4])))
    eta.append(add(scale(x[(i+2)%4], Fraction(2-i)), mul(x[(i+1)%4],x[(i+3)%4])))

# Deterministic symmetric second-moment tensor field G_ij(x).
G=[[{} for _ in range(N)] for __ in range(N)]
for i in range(N):
    for j in range(i,N):
        p=add(scale(ONE,Fraction(1+i+j)),mul(x[(i+1)%4],x[(j+2)%4]))
        G[i][j]=p; G[j][i]=p


def lie_tensor(v,T):
    # (L_v T)_ij = v^k d_k T_ij + T_kj d_i v^k + T_ik d_j v^k
    L=[[{} for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            out={}
            for k in range(N):
                out=add(out,mul(v[k],der(T[i][j],k)))
                out=add(out,mul(T[k][j],der(v[k],i)))
                out=add(out,mul(T[i][k],der(v[k],j)))
            L[i][j]=out
    return L


def bracket(v,w):
    # [v,w]^i = v^k d_k w^i - w^k d_k v^i
    out=[]
    for i in range(N):
        p={}
        for k in range(N):
            p=add(p,mul(v[k],der(w[i],k)))
            p=add(p,scale(mul(w[k],der(v[i],k)),-1))
        out.append(p)
    return out

LxiLeta=lie_tensor(xi,lie_tensor(eta,G))
LetaLxi=lie_tensor(eta,lie_tensor(xi,G))
comm=[[add(LxiLeta[i][j],scale(LetaLxi[i][j],-1)) for j in range(N)] for i in range(N)]
Lbr=lie_tensor(bracket(xi,eta),G)
assert all(comm[i][j]==Lbr[i][j] for i in range(N) for j in range(N))

print({
    'field_origin': 'G is a symmetric second moment / Sym^2 relational-frame response',
    'finite_rule': 'local frame relabeling acts by pullback',
    'linearized_rule': 'delta0 h_ij = D_i xi_j + D_j xi_i after lowering parameter with constant background form',
    'first_nonlinear_rule': 'delta1 h_ij = xi^k D_k h_ij + h_kj D_i xi^k + h_ik D_j xi^k',
    'exact_algebra_identity': '[L_xi,L_eta]G = L_[xi,eta] G',
    'polynomial_exact_test': 'PASS',
    'classification': 'PASS_SCOPED_RELATIONAL_FRAME_PULLBACK_FIXES_DELTA1_AND_CLOSES_TRANSFORMATION_ALGEBRA',
    'guard': 'this does not yet prove cubic action invariance or nonlinear field equations',
})
