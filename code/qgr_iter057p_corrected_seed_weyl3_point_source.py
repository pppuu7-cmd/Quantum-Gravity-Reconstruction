#!/usr/bin/env python3
"""Iter057P exact Weyl3 Euler point source on the Iter057O corrected seed.

All algebra is exact Fraction polynomial arithmetic.  The corrected seed is known
through quartic coordinate order.  For E_W3(0), curvature is needed through degree
two and P=dI3/dR through degree two; this is sufficient because the only derivative
sector is the double covariant divergence of P evaluated at the origin.
"""
import argparse
import json
import math
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

N=4
MAX_METRIC=4
MAX_CURV=2
K=F(2,25)
ETA=(-1,1,1,1)
GATE="ITER057P-CORRECTED-SEED-WEYL3-POINT-SOURCE-RESET"
PREREG="4c79629d38d2de28385fa059365b1b50e8c165cf"
ITER057O="679a3d73d589fc9161bdf2209f25bb4b7c785fd6"
PAIRS=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
ZERO=(0,0,0,0)

# Canonical Iter057O trace-reversed normalized R4/kappa^2 coefficients.
R4={
 ((0,0),(0,0,0,4)):F(136),
 ((0,0),(0,0,2,2)):F(-16),
 ((0,0),(0,2,0,2)):F(-16),
 ((0,0),(2,0,0,2)):F(56),
 ((0,0),(2,0,2,0)):F(-28),
 ((0,0),(2,2,0,0)):F(-28),
 ((0,3),(1,0,0,3)):F(56),
 ((0,3),(1,0,2,1)):F(-28),
 ((0,3),(1,2,0,1)):F(-28),
 ((1,1),(0,0,0,4)):F(-64),
 ((1,1),(0,0,2,2)):F(-4),
 ((1,1),(0,2,0,2)):F(4),
 ((1,2),(0,1,1,2)):F(4),
 ((1,3),(0,1,0,3)):F(-8),
 ((2,2),(0,0,0,4)):F(-64),
 ((2,2),(0,0,2,2)):F(4),
 ((2,2),(0,2,0,2)):F(-4),
 ((2,3),(0,0,1,3)):F(-8),
 ((3,3),(0,0,0,4)):F(72),
 ((3,3),(0,0,2,2)):F(-28),
 ((3,3),(0,2,0,2)):F(-28),
}

OLD_E_DOWN_OVER_K3={(0,0):F(48),(1,1):F(-208),(2,2):F(-208),(3,3):F(368)}


def const(c):
    c=F(c); return {} if c==0 else {ZERO:c}

def mono(exp,c=1):
    c=F(c); return {} if c==0 else {tuple(exp):c}

def add(a,b):
    out=dict(a)
    for m,c in b.items():
        v=out.get(m,F(0))+c
        if v: out[m]=v
        elif m in out: del out[m]
    return out

def neg(a): return {m:-c for m,c in a.items()}
def sub(a,b): return add(a,neg(b))
def scale(a,c):
    c=F(c); return {} if c==0 else {m:c*v for m,v in a.items() if c*v}
def mul(a,b,maxdeg):
    out={}
    for m,c in a.items():
        for n,d in b.items():
            e=tuple(m[i]+n[i] for i in range(4))
            if sum(e)<=maxdeg: out[e]=out.get(e,F(0))+c*d
    return {m:c for m,c in out.items() if c}
def deriv(a,coord):
    out={}
    for m,c in a.items():
        if m[coord]:
            e=list(m); n=e[coord]; e[coord]-=1; e=tuple(e)
            out[e]=out.get(e,F(0))+c*n
    return out
def trunc(a,maxdeg): return {m:c for m,c in a.items() if sum(m)<=maxdeg and c}
def v0(a): return a.get(ZERO,F(0))
def fstr(v): return str(v.numerator) if v.denominator==1 else f"{v.numerator}/{v.denominator}"
def psign(p):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv%2 else 1

def pmat_zero(): return [[{} for _ in range(N)] for _ in range(N)]


def corrected_metric():
    # q=2 Phi = kappa(x^2+y^2-2z^2), with full 4D exponent order (t,x,y,z).
    q=add(add(mono((0,2,0,0),K),mono((0,0,2,0),K)),mono((0,0,0,2),-2*K))
    g=pmat_zero()
    for a in range(N): g[a][a]=add(const(ETA[a]),scale(q,-1))

    rbar=pmat_zero()
    for (pair,alpha),coef in R4.items():
        a,b=pair
        denom=math.prod(math.factorial(n) for n in alpha)
        term=mono(alpha,K*K*coef/F(denom))
        rbar[a][b]=add(rbar[a][b],term)
        if a!=b: rbar[b][a]=add(rbar[b][a],term)
    tr={}
    for a in range(N): tr=add(tr,scale(rbar[a][a],ETA[a]))
    r=pmat_zero()
    for a,b in product(range(N),repeat=2):
        r[a][b]=dict(rbar[a][b])
        if a==b: r[a][b]=add(r[a][b],scale(tr,-F(ETA[a],2)))
        g[a][b]=add(g[a][b],r[a][b])
    return q,g,rbar,r


def compute():
    q,g,rbar,r=corrected_metric()

    # For curvature through degree two, inverse metric is needed only through degree two.
    gi=pmat_zero()
    gi[0][0]=add(const(-1),q)
    for a in (1,2,3): gi[a][a]=add(const(1),q)

    inv2=True
    for a,b in product(range(N),repeat=2):
        s={}
        for c in range(N): s=add(s,mul(g[a][c],gi[c][b],2))
        s=sub(s,const(1 if a==b else 0))
        if trunc(s,2): inv2=False

    Gamma=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N),repeat=3):
        val={}
        for d in range(N):
            t=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            val=add(val,mul(gi[a][d],t,3))
        Gamma[a][b][c]=scale(trunc(val,3),F(1,2))

    Rup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val=sub(deriv(Gamma[a][d][b],c),deriv(Gamma[a][c][b],d))
        for e in range(N):
            val=add(val,sub(mul(Gamma[a][c][e],Gamma[e][d][b],2),mul(Gamma[a][d][e],Gamma[e][c][b],2)))
        Rup[a][b][c][d]=trunc(val,2)

    Rlow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e in range(N): val=add(val,mul(g[a][e],Rup[e][b][c][d],2))
        Rlow[a][b][c][d]=trunc(val,2)

    Ric=pmat_zero()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N): val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,2)
    Scal={}
    for a,b in product(range(N),repeat=2): Scal=add(Scal,mul(gi[a][b],Ric[a][b],2))
    Scal=trunc(Scal,2)
    ricci2_zero=all(not Ric[a][b] for a,b in product(range(N),repeat=2))
    scalar2_zero=not Scal

    C=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rp={}
        if a==c: rp=add(rp,mul(g[a][a],Ric[d][b],2))
        if a==d: rp=sub(rp,mul(g[a][a],Ric[c][b],2))
        if b==c: rp=sub(rp,mul(g[b][b],Ric[d][a],2))
        if b==d: rp=add(rp,mul(g[b][b],Ric[c][a],2))
        rp=scale(rp,F(1,2))
        gg={}
        if a==c and d==b: gg=add(gg,mul(g[a][a],g[d][d],2))
        if a==d and c==b: gg=sub(gg,mul(g[a][a],g[c][c],2))
        C[a][b][c][d]=trunc(add(sub(Rlow[a][b][c][d],rp),scale(mul(Scal,gg,2),F(1,6))),2)

    # Q_abcd=C_ab{}^{rs} C_rs cd.  Raising/lowering through degree two uses diagonal gi/g only.
    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for rr,s in product(range(N),repeat=2):
            term=mul(mul(gi[rr][rr],gi[s][s],2),C[a][b][rr][s],2)
            val=add(val,mul(term,C[rr][s][c][d],2))
        Q[a][b][c][d]=trunc(val,2)

    perms=list(permutations(range(4)))
    Qr=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        inds=(a,b,c,d); alt={}
        for p in perms:
            alt=add(alt,scale(Q[inds[p[0]]][inds[p[1]]][inds[p[2]]][inds[p[3]]],F(psign(p),24)))
        Qr[a][b][c][d]=sub(Q[a][b][c][d],alt)

    QRic=pmat_zero()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N): val=add(val,mul(gi[a][a],Qr[a][b][a][d],2))
        QRic[b][d]=trunc(val,2)
    QSc={}
    for b in range(N): QSc=add(QSc,mul(gi[b][b],QRic[b][b],2))
    QSc=trunc(QSc,2)

    Plow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        t={}
        if a==c: t=add(t,mul(g[a][a],QRic[d][b],2))
        if a==d: t=sub(t,mul(g[a][a],QRic[c][b],2))
        if b==c: t=sub(t,mul(g[b][b],QRic[d][a],2))
        if b==d: t=add(t,mul(g[b][b],QRic[c][a],2))
        t=scale(t,F(1,2))
        gg={}
        if a==c and d==b: gg=add(gg,mul(g[a][a],g[d][d],2))
        if a==d and c==b: gg=sub(gg,mul(g[a][a],g[c][c],2))
        gg=scale(gg,F(1,2))
        Plow[a][b][c][d]=scale(trunc(add(sub(Qr[a][b][c][d],t),scale(mul(QSc,gg,2),F(1,3))),2),3)

    P=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        term=Plow[a][b][c][d]
        for idx in (a,b,c,d): term=mul(term,gi[idx][idx],2)
        P[a][b][c][d]=trunc(term,2)

    # I3 at origin from C_ab{}^{cd} operator.
    Cm={}
    for a,b,c,d in product(range(N),repeat=4):
        Cm[a,b,c,d]=F(ETA[c]*ETA[d])*v0(C[a][b][c][d])
    I30=F(0)
    for a,b,c,d,e,f in product(range(N),repeat=6):
        I30 += Cm[a,b,c,d]*Cm[c,d,e,f]*Cm[e,f,a,b]

    PR0=F(0)
    for a,b,c,d in product(range(N),repeat=4): PR0 += v0(P[a][b][c][d])*v0(Rlow[a][b][c][d])

    # First covariant divergence through degree one.
    FD=[[ [ {} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,b,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=deriv(P[a][m][b][n],a)
            for rr in range(N):
                term=add(term,mul(Gamma[a][a][rr],P[rr][m][b][n],1))
                term=add(term,mul(Gamma[m][a][rr],P[a][rr][b][n],1))
                term=add(term,mul(Gamma[b][a][rr],P[a][m][rr][n],1))
                term=add(term,mul(Gamma[n][a][rr],P[a][m][b][rr],1))
            val=add(val,term)
        FD[m][b][n]=trunc(val,1)

    D=pmat_zero()
    for m,n in product(range(N),repeat=2):
        val={}
        for b in range(N):
            term=deriv(FD[m][b][n],b)
            for rr in range(N):
                term=add(term,mul(Gamma[m][b][rr],FD[rr][b][n],0))
                term=add(term,mul(Gamma[b][b][rr],FD[m][rr][n],0))
                term=add(term,mul(Gamma[n][b][rr],FD[m][b][rr],0))
            val=add(val,term)
        D[m][n]=const(v0(val))

    # Algebraic insertion B^{ab}=P^{(a|cde|}R^{b)}_cde at the origin.
    def bone(a,b):
        s=F(0)
        for c,d,e in product(range(N),repeat=3):
            s += v0(P[a][c][d][e]) * F(ETA[b]) * v0(Rlow[b][c][d][e])
        return s
    B0=[[F(0) for _ in range(N)] for _ in range(N)]
    for a,b in product(range(N),repeat=2): B0[a][b]=(bone(a,b)+bone(b,a))/2

    Eup=[[F(0) for _ in range(N)] for _ in range(N)]
    for a,b in product(range(N),repeat=2):
        v=-B0[a][b]-2*v0(D[a][b])
        if a==b: v += F(ETA[a],2)*I30
        Eup[a][b]=v
    Edown=[[F(ETA[a]*ETA[b])*Eup[a][b] for b in range(N)] for a in range(N)]

    sym=all(Edown[a][b]==Edown[b][a] for a,b in product(range(N),repeat=2))
    trace=sum(F(ETA[a])*Edown[a][a] for a in range(N))
    even_seed=all(sum(exp)%2==0 for a,b in product(range(N),repeat=2) for exp in g[a][b])

    point={}
    comparison={}
    changed=[]
    for a,b in PAIRS:
        val=Edown[a][b]
        point[f"{a}{b}"]={"value":fstr(val),"over_kappa3":fstr(val/(K**3))}
        old=OLD_E_DOWN_OVER_K3.get((a,b),F(0))
        new=val/(K**3)
        comparison[f"{a}{b}"]={"old_over_kappa3":fstr(old),"new_over_kappa3":fstr(new),"delta_over_kappa3":fstr(new-old)}
        if new!=old: changed.append(f"{a}{b}")

    controls={
        "inverse_identity_through_degree2":inv2,
        "corrected_seed_Ricci_through_degree2_zero":ricci2_zero,
        "corrected_seed_scalar_through_degree2_zero":scalar2_zero,
        "P_dot_R_equals_3I3_origin":PR0==3*I30,
        "E_W3_down_symmetric":sym,
        "trace_Ward_exact":trace==-I30,
        "seed_full_inversion_even":even_seed,
        "first_covariant_derivatives_E_origin_zero_by_even_parity_and_Gamma0":even_seed and all(not Gamma[a][b][c].get(ZERO,F(0)) for a,b,c in product(range(N),repeat=3)),
    }
    passed=all(controls.values())
    return {
        "gate":GATE,
        "preregistration_commit":PREREG,
        "iter057o_seed_commit":ITER057O,
        "kappa":fstr(K),
        "I3_origin":fstr(I30),
        "I3_origin_over_kappa3":fstr(I30/(K**3)),
        "D_up_origin_over_kappa3":{f"{a}{b}":fstr(v0(D[a][b])/(K**3)) for a,b in PAIRS},
        "B_up_origin_over_kappa3":{f"{a}{b}":fstr(B0[a][b]/(K**3)) for a,b in PAIRS},
        "E_W3_down_origin":point,
        "old_vs_corrected_source":comparison,
        "changed_components":changed,
        "controls":controls,
        "pass":passed,
        "classification":("PASS_SCOPED_ITER057P_CORRECTED_EINSTEIN_SEED_WEYL3_POINT_SOURCE_EXACTLY_RESET__SECOND_SOURCE_JET_REQUIRES_SEXTIC_SEED" if passed else "INVALID_OR_UNRESOLVED_ITER057P"),
        "exact_zero_uses_tolerance":False,
        "c6_status":"SYMBOLIC_UNFIXED_COEFFICIENT_ONLY",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out"); args=ap.parse_args()
    out=compute(); text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True: raise SystemExit(2)

if __name__=="__main__": main()
