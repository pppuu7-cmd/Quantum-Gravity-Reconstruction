#!/usr/bin/env python3
"""Iter057R exact Weyl3 Euler source through coordinate degree two on the
canonical Iter057O+Iter057Q Einstein-completed seed.

The implementation uses exact Fraction polynomial arithmetic in all four
coordinates.  The seed metric is retained through degree six, curvature/Weyl
through degree four, P=3 Pi_W Pi_R[C^2] through degree four, and E_W3 through
degree two.  No numerical tolerance or symmetry projection is used.
"""
import argparse
import json
import math
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

import qgr_iter057p_corrected_seed_weyl3_point_source as pseed
import qgr_iter057q_sextic_einstein_seed_completion as qseed

N=4
K=F(2,25)
ETA=(-1,1,1,1)
ZERO=(0,0,0,0)
PAIRS=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
GATE="ITER057R-CORRECTED-SEED-WEYL3-SECOND-SOURCE-JET"
PREREG="582ff376a59458270b7074d5470dedfba85896af"
ITER057P="3c8e8d54cf7c4685945f3d30284544bbba75c338"
ITER057Q="c4f1c5c01205a6991e7215e3824111e1f36d1436"

OLD_SHAT0_OVER_K3={(0,0):F(-48),(1,1):F(208),(2,2):F(208),(3,3):F(-368)}
ITER057P_E_DOWN_OVER_K3={(0,0):F(-240),(1,1):F(-384),(2,2):F(-384),(3,3):F(432)}


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
def pmat(): return [[{} for _ in range(N)] for _ in range(N)]
def factorial_multi(alpha): return math.prod(math.factorial(n) for n in alpha)


def seed_metric():
    # G3 quadratic seed.
    q=add(add(mono((0,2,0,0),K),mono((0,0,2,0),K)),mono((0,0,0,2),-2*K))
    g=pmat()
    for a in range(N): g[a][a]=add(const(ETA[a]),scale(q,-1))

    # Canonical Iter057O trace-reversed quartic coefficients are frozen in pseed.R4.
    rbar4=pmat()
    for (pair,alpha),coef in pseed.R4.items():
        a,b=pair; term=mono(alpha,K*K*coef/F(factorial_multi(alpha)))
        rbar4[a][b]=add(rbar4[a][b],term)
        if a!=b: rbar4[b][a]=add(rbar4[b][a],term)
    tr4={}
    for a in range(N): tr4=add(tr4,scale(rbar4[a][a],ETA[a]))
    r4=pmat()
    for a,b in product(range(N),repeat=2):
        r4[a][b]=dict(rbar4[a][b])
        if a==b: r4[a][b]=add(r4[a][b],scale(tr4,-F(ETA[a],2)))
        g[a][b]=add(g[a][b],r4[a][b])

    # Replay the exact Iter057Q canonical sextic pivot solution.
    qdata=qseed.compute()
    if qdata.get("pass") is not True:
        raise RuntimeError("Iter057Q replay did not pass")
    rbar6=pmat()
    for item in qdata["particular_R6_normalized"]:
        a,b=item["pair"]; alpha=tuple(item["alpha"]); coef=F(item["R6_over_kappa3"])
        term=mono(alpha,K**3*coef/F(factorial_multi(alpha)))
        rbar6[a][b]=add(rbar6[a][b],term)
        if a!=b: rbar6[b][a]=add(rbar6[b][a],term)
    tr6={}
    for a in range(N): tr6=add(tr6,scale(rbar6[a][a],ETA[a]))
    r6=pmat()
    for a,b in product(range(N),repeat=2):
        r6[a][b]=dict(rbar6[a][b])
        if a==b: r6[a][b]=add(r6[a][b],scale(tr6,-F(ETA[a],2)))
        g[a][b]=add(g[a][b],r6[a][b])
    return g,r4,r6,qdata


def inverse_through4(g):
    # g=eta+h with h starting at degree two:
    # g^{-1}=eta-eta h eta+eta h eta h eta + O(x^6).
    h=pmat()
    for a,b in product(range(N),repeat=2):
        h[a][b]=dict(g[a][b])
        if a==b: h[a][b]=sub(h[a][b],const(ETA[a]))
    gi=pmat()
    for a,b in product(range(N),repeat=2):
        if a==b: gi[a][b]=const(ETA[a])
        gi[a][b]=add(gi[a][b],scale(h[a][b],-ETA[a]*ETA[b]))
        hh={}
        for c in range(N): hh=add(hh,scale(mul(h[a][c],h[c][b],4),ETA[a]*ETA[c]*ETA[b]))
        gi[a][b]=trunc(add(gi[a][b],hh),4)
    return gi


def compute():
    g,r4,r6,qdata=seed_metric()
    gi=inverse_through4(g)

    inverse4=True
    for a,b in product(range(N),repeat=2):
        s={}
        for c in range(N): s=add(s,mul(g[a][c],gi[c][b],4))
        s=sub(s,const(1 if a==b else 0))
        if trunc(s,4): inverse4=False

    # Christoffel through degree five and curvature through degree four.
    Gamma=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N),repeat=3):
        val={}
        for d in range(N):
            t=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            val=add(val,mul(gi[a][d],t,5))
        Gamma[a][b][c]=scale(trunc(val,5),F(1,2))

    Rup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val=sub(deriv(Gamma[a][d][b],c),deriv(Gamma[a][c][b],d))
        for e in range(N):
            val=add(val,sub(mul(Gamma[a][c][e],Gamma[e][d][b],4),mul(Gamma[a][d][e],Gamma[e][c][b],4)))
        Rup[a][b][c][d]=trunc(val,4)
    Rlow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e in range(N): val=add(val,mul(g[a][e],Rup[e][b][c][d],4))
        Rlow[a][b][c][d]=trunc(val,4)

    Ric=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N): val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,4)
    Scal={}
    for a,b in product(range(N),repeat=2): Scal=add(Scal,mul(gi[a][b],Ric[a][b],4))
    Scal=trunc(Scal,4)
    seed_ricci4_zero=all(not Ric[a][b] for a,b in product(range(N),repeat=2))
    seed_scalar4_zero=not Scal

    C=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rp={}
        for i,j,sgn in ((a,c,1),(a,d,-1),(b,c,-1),(b,d,1)):
            # terms g_{i,j} R_{other}; explicit cases avoid an extra four-index object.
            if (i,j)==(a,c):
                for e in range(N): rp=add(rp,scale(mul(g[a][c],Ric[d][b],4),1))
            elif (i,j)==(a,d):
                rp=sub(rp,mul(g[a][d],Ric[c][b],4))
            elif (i,j)==(b,c):
                rp=sub(rp,mul(g[b][c],Ric[d][a],4))
            else:
                rp=add(rp,mul(g[b][d],Ric[c][a],4))
        rp=scale(rp,F(1,2))
        gg=sub(mul(g[a][c],g[d][b],4),mul(g[a][d],g[c][b],4))
        C[a][b][c][d]=trunc(add(sub(Rlow[a][b][c][d],rp),scale(mul(Scal,gg,4),F(1,6))),4)

    # C_ab{}^{rs}.
    Cup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,r,s in product(range(N),repeat=4):
        val={}
        for m,n in product(range(N),repeat=2):
            val=add(val,mul(mul(gi[r][m],gi[s][n],4),C[a][b][m][n],4))
        Cup[a][b][r][s]=trunc(val,4)

    # Q_abcd=C_ab{}^{rs} C_rs cd.
    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for r,s in product(range(N),repeat=2): val=add(val,mul(Cup[a][b][r][s],C[r][s][c][d],4))
        Q[a][b][c][d]=trunc(val,4)

    perms=list(permutations(range(4)))
    Qr=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        inds=(a,b,c,d); alt={}
        for pp in perms: alt=add(alt,scale(Q[inds[pp[0]]][inds[pp[1]]][inds[pp[2]]][inds[pp[3]]],F(psign(pp),24)))
        Qr[a][b][c][d]=sub(Q[a][b][c][d],alt)

    QRic=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a,c in product(range(N),repeat=2): val=add(val,mul(gi[a][c],Qr[a][b][c][d],4))
        QRic[b][d]=trunc(val,4)
    QSc={}
    for b,d in product(range(N),repeat=2): QSc=add(QSc,mul(gi[b][d],QRic[b][d],4))
    QSc=trunc(QSc,4)

    Plow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        t=add(sub(mul(g[a][c],QRic[d][b],4),mul(g[a][d],QRic[c][b],4)),
              add(neg(mul(g[b][c],QRic[d][a],4)),mul(g[b][d],QRic[c][a],4)))
        t=scale(t,F(1,2))
        gg=scale(sub(mul(g[a][c],g[d][b],4),mul(g[a][d],g[c][b],4)),F(1,2))
        Plow[a][b][c][d]=scale(trunc(add(sub(Qr[a][b][c][d],t),scale(mul(QSc,gg,4),F(1,3))),4),3)

    P=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for i,j,m,n in product(range(N),repeat=4):
            term=mul(mul(gi[a][i],gi[b][j],4),mul(gi[c][m],gi[d][n],4),4)
            val=add(val,mul(term,Plow[i][j][m][n],4))
        P[a][b][c][d]=trunc(val,4)

    # I3=Q_abcd C^{cdab} through degree four.
    I3={}
    for a,b,c,d in product(range(N),repeat=4):
        call={}
        for i,j,m,n in product(range(N),repeat=4):
            term=mul(mul(gi[c][i],gi[d][j],4),mul(gi[a][m],gi[b][n],4),4)
            call=add(call,mul(term,C[i][j][m][n],4))
        I3=add(I3,mul(Q[a][b][c][d],call,4))
    I3=trunc(I3,4)

    PR={}
    for a,b,c,d in product(range(N),repeat=4): PR=add(PR,mul(P[a][b][c][d],Rlow[a][b][c][d],4))
    PR=trunc(PR,4)
    homogeneity=not trunc(sub(PR,scale(I3,3)),4)

    # First divergence through degree three; second divergence through degree two.
    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,b,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=deriv(P[a][m][b][n],a)
            for r in range(N):
                term=add(term,mul(Gamma[a][a][r],P[r][m][b][n],3))
                term=add(term,mul(Gamma[m][a][r],P[a][r][b][n],3))
                term=add(term,mul(Gamma[b][a][r],P[a][m][r][n],3))
                term=add(term,mul(Gamma[n][a][r],P[a][m][b][r],3))
            val=add(val,term)
        FD[m][b][n]=trunc(val,3)
    D=pmat()
    for m,n in product(range(N),repeat=2):
        val={}
        for b in range(N):
            term=deriv(FD[m][b][n],b)
            for r in range(N):
                term=add(term,mul(Gamma[m][b][r],FD[r][b][n],2))
                term=add(term,mul(Gamma[b][b][r],FD[m][r][n],2))
                term=add(term,mul(Gamma[n][b][r],FD[m][b][r],2))
            val=add(val,term)
        D[m][n]=trunc(val,2)

    # Algebraic insertion B^{ab}=P^{(a|cde|} R^{b)}_cde through degree two.
    def bone(a,b):
        val={}
        for c,d,e,f in product(range(N),repeat=4):
            val=add(val,mul(mul(P[a][c][d][e],gi[b][f],2),Rlow[f][c][d][e],2))
        return trunc(val,2)
    B=pmat()
    for a,b in product(range(N),repeat=2): B[a][b]=scale(add(bone(a,b),bone(b,a)),F(1,2))

    Eup=pmat()
    for a,b in product(range(N),repeat=2):
        val=add(neg(B[a][b]),scale(D[a][b],-2))
        val=add(val,scale(mul(gi[a][b],I3,2),F(1,2)))
        Eup[a][b]=trunc(val,2)
    Edown=pmat()
    for a,b in product(range(N),repeat=2):
        val={}
        for c,d in product(range(N),repeat=2): val=add(val,mul(mul(g[a][c],g[b][d],2),Eup[c][d],2))
        Edown[a][b]=trunc(val,2)

    sym=all(not trunc(sub(Edown[a][b],Edown[b][a]),2) for a,b in product(range(N),repeat=2))
    trace={}
    for a,b in product(range(N),repeat=2): trace=add(trace,mul(gi[a][b],Edown[a][b],2))
    trace=trunc(trace,2)
    trace_ward=not trunc(add(trace,trunc(I3,2)),2)

    noether=[]
    for b in range(N):
        val={}
        for a in range(N):
            val=add(val,deriv(Eup[a][b],a))
            for r in range(N):
                val=add(val,mul(Gamma[a][a][r],Eup[r][b],1))
                val=add(val,mul(Gamma[b][a][r],Eup[a][r],1))
        noether.append(trunc(val,1))
    noether_ok=all(not v for v in noether)

    even_seed=all(all(sum(alpha)%2==0 for alpha in g[a][b]) for a,b in product(range(N),repeat=2))
    first_zero=all(not trunc(deriv(Edown[a][b],c),0) for a,b,c in product(range(N),repeat=3))

    point_match=True
    for a,b in PAIRS:
        expected=ITER057P_E_DOWN_OVER_K3.get((a,b),F(0))*K**3
        if v0(Edown[a][b])!=expected: point_match=False

    # Export Shat=-E_down normalized order-0 and degree-2 coefficients.
    source={}
    corrected_s2_nonzero=0
    for a,b in PAIRS:
        S=neg(Edown[a][b]); rec={"order0":None,"order2":[]}
        s0=v0(S)
        if s0:
            rec["order0"]={"value":fstr(s0),"over_kappa3":fstr(s0/(K**3))}
        for alpha,raw in sorted(S.items()):
            if sum(alpha)!=2: continue
            norm=raw*F(factorial_multi(alpha))
            if norm:
                corrected_s2_nonzero+=1
                rec["order2"].append({"alpha":list(alpha),"value":fstr(norm),"over_kappa4":fstr(norm/(K**4))})
        source[f"{a}{b}"]=rec

    controls={
        "iter057Q_replay_pass":qdata.get("pass") is True,
        "inverse_identity_through_degree4":inverse4,
        "seed_Ricci_through_degree4_zero":seed_ricci4_zero,
        "seed_scalar_through_degree4_zero":seed_scalar4_zero,
        "P_dot_R_equals_3I3_through_degree4":homogeneity,
        "E_W3_down_symmetric_through_degree2":sym,
        "trace_Ward_through_degree2":trace_ward,
        "Noether_divergence_through_degree1":noether_ok,
        "seed_even_parity":even_seed,
        "first_partial_derivatives_E_origin_zero":first_zero,
        "point_source_matches_terminal_Iter057P":point_match,
    }
    passed=all(controls.values())
    return {
        "gate":GATE,"preregistration_commit":PREREG,"iter057P_commit":ITER057P,"iter057Q_commit":ITER057Q,
        "kappa":fstr(K),"controls":controls,"pass":passed,
        "I3_origin":fstr(v0(I3)),"I3_origin_over_kappa3":fstr(v0(I3)/(K**3)),
        "E_W3_down_origin_over_kappa3":{f"{a}{b}":fstr(v0(Edown[a][b])/(K**3)) for a,b in PAIRS},
        "Shat_normalized":source,"corrected_source_degree2_nonzero_count":corrected_s2_nonzero,
        "classification":("PASS_SCOPED_ITER057R_CORRECTED_EINSTEIN_SEED_WEYL3_SECOND_SOURCE_JET_EXACTLY_EXPOSED__ONSHELL_O_C6_Q2_Q4_RECONSTRUCTION_CAN_RESTART" if passed else "INVALID_OR_UNRESOLVED_ITER057R"),
        "exact_zero_uses_tolerance":False,"c6_status":"SYMBOLIC_UNFIXED_FACTORED_OUT",
    }


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out");args=ap.parse_args()
    out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True: raise SystemExit(2)

if __name__=="__main__":main()
