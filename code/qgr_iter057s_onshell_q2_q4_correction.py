#!/usr/bin/env python3
"""Iter057S exact on-shell first-order Q2/Q4 correction on the canonical
quartic+sextic Einstein-completed seed.

The corrected Iter057R source is consumed exactly.  The universal Q4 principal
matrix is reused, but the affine RHS is rebuilt from the new source and the new
Q2.  A direct unreduced covariant linearized-Einstein control is then evaluated
on the full canonical Einstein seed through coordinate degree two.
"""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

import qgr_iter057m_q4_exact_constructor as mctor
import qgr_iter057m_universal_q4_matrix as uq4
import qgr_iter057p_corrected_seed_weyl3_point_source as pseed
import qgr_iter057q_sextic_einstein_seed_completion as qseed
import qgr_iter057r_corrected_seed_weyl3_second_source_jet as rsource

GATE="ITER057S-ONSHELL-FIRST-ORDER-Q2-Q4-CORRECTION"
PREREG="a59858ce6dbc08493325d8ba406229da18013d40"
ITER057R="e395d2fb4be3e6f556f893ce63ae68f3b4b51ea2"
PAIRS=uq4.PAIRS
ETA=uq4.ETA
X=sp.symbols("t x y z")
t,x,y,z=X
eta=sp.diag(-1,1,1,1)
k=sp.Rational(2,25)


def alphas(n): return uq4.alphas(n)
def mon(alpha):
    out=1
    for u,n in zip(X,alpha): out*=u**n
    return out
def fact(alpha):
    out=1
    for n in alpha: out*=sp.factorial(n)
    return out
def trunc(expr,degree):
    p=sp.Poly(sp.expand(expr),*X)
    return sp.expand(sum(c*mon(a) for a,c in p.terms() if sum(a)<=degree))
def pidx(a,b): return uq4.pair_index(a,b)


def parse_corrected_source():
    obj=rsource.compute()
    if obj.get("pass") is not True:
        raise RuntimeError("Iter057R source replay failed")
    a2=alphas(2)
    S0=[sp.Integer(0)]*10
    S2=[[sp.Integer(0)]*len(a2) for _ in range(10)]
    for p,(a,b) in enumerate(PAIRS):
        rec=obj["Shat_normalized"][f"{a}{b}"]
        if rec["order0"] is not None:
            S0[p]=sp.Rational(rec["order0"]["value"])
        for item in rec["order2"]:
            alpha=tuple(item["alpha"])
            S2[p][a2.index(alpha)]=sp.Rational(item["value"])
    return obj,S0,S2


def build_full_seed():
    # Canonical G3+Iter057O quartic+Iter057Q sextic seed in exact SymPy form.
    qdata=qseed.compute()
    if qdata.get("pass") is not True:
        raise RuntimeError("Iter057Q seed replay failed")
    q=k*(x*x+y*y-2*z*z)
    g=sp.diag(-1-q,1-q,1-q,1-q)

    rbar4=sp.MutableDenseMatrix(4,4,[0]*16)
    for (pair,alpha),coef in pseed.R4.items():
        a,b=pair; term=k**2*sp.Rational(coef.numerator,coef.denominator)*mon(alpha)/fact(alpha)
        rbar4[a,b]+=term
        if a!=b:rbar4[b,a]+=term
    tr4=sum(eta[a,b]*rbar4[a,b] for a,b in product(range(4),repeat=2))
    r4=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        r4[a,b]=sp.expand(rbar4[a,b]-sp.Rational(1,2)*eta[a,b]*tr4)

    rbar6=sp.MutableDenseMatrix(4,4,[0]*16)
    for item in qdata["particular_R6_normalized"]:
        a,b=item["pair"]; alpha=tuple(item["alpha"]); coef=sp.Rational(item["R6_over_kappa3"])
        term=k**3*coef*mon(alpha)/fact(alpha)
        rbar6[a,b]+=term
        if a!=b:rbar6[b,a]+=term
    tr6=sum(eta[a,b]*rbar6[a,b] for a,b in product(range(4),repeat=2))
    r6=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        r6[a,b]=sp.expand(rbar6[a,b]-sp.Rational(1,2)*eta[a,b]*tr6)
    return sp.MutableDenseMatrix(g+r4+r6),qdata


def qbar_from_jets(Q2,sparse4=None):
    a4=alphas(4)
    qbar=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        qbar[a,b]=sp.expand(sum(sp.Rational(1,2)*Q2[a,b,c,d]*X[c]*X[d]
                                for c,d in product(range(4),repeat=2)))
    if sparse4:
        for item in sparse4:
            a,b=item["pair"]; alpha=tuple(item["alpha"]); value=sp.Rational(item["value"])
            term=value*mon(alpha)/fact(alpha)
            qbar[a,b]+=term
            if a!=b:qbar[b,a]+=term
    for a,b in product(range(4),repeat=2): qbar[a,b]=sp.expand(qbar[a,b])
    return qbar


def full_seed_unreduced_control(gseed,qbar,S0,S2):
    # Through qbar degree four / DG degree two, only the seed inverse/connection
    # coefficients through degree two/one can contribute.  They are nevertheless
    # obtained by truncating the full canonical seed, not by reusing a historical RHS.
    hbg=gseed-eta
    gi2=sp.MutableDenseMatrix(eta-eta*hbg*eta)
    for a,b in product(range(4),repeat=2): gi2[a,b]=trunc(gi2[a,b],2)
    inv2=all(trunc(sum(gseed[a,c]*gi2[c,b] for c in range(4))-(1 if a==b else 0),2)==0
             for a,b in product(range(4),repeat=2))

    Gamma={}
    for a,b,c in product(range(4),repeat=3):
        v=0
        for d in range(4):
            v += gi2[a,d]*(sp.diff(gseed[d,c],X[b])+sp.diff(gseed[d,b],X[c])-sp.diff(gseed[b,c],X[d]))/2
        Gamma[a,b,c]=trunc(v,1)

    # Trace reversal is involutive in 4D.  Construct h from qbar with the full seed,
    # retaining every term that can contribute through DG degree two.
    qtrace=trunc(sum(gi2[a,b]*qbar[a,b] for a,b in product(range(4),repeat=2)),4)
    h=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        h[a,b]=trunc(qbar[a,b]-sp.Rational(1,2)*gseed[a,b]*qtrace,4)
    htrace=trunc(sum(gi2[a,b]*h[a,b] for a,b in product(range(4),repeat=2)),4)

    # Direct de Donder vector on the full seed.
    gauge=[]
    for b in range(4):
        v=0
        for a,c in product(range(4),repeat=2):
            cov=sp.diff(qbar[a,b],X[c])
            for r in range(4): cov-=Gamma[r,c,a]*qbar[r,b]+Gamma[r,c,b]*qbar[a,r]
            v+=gi2[a,c]*cov
        gauge.append(trunc(v,3))

    first={}
    for a,b,c in product(range(4),repeat=3):
        v=sp.diff(h[b,c],X[a])
        for r in range(4): v-=Gamma[r,a,b]*h[r,c]+Gamma[r,a,c]*h[b,r]
        first[a,b,c]=trunc(v,3)
    second={}
    for d,a,b,c in product(range(4),repeat=4):
        v=sp.diff(first[a,b,c],X[d])
        for r in range(4):
            v-=Gamma[r,d,a]*first[r,b,c]
            v-=Gamma[r,d,b]*first[a,r,c]
            v-=Gamma[r,d,c]*first[a,b,r]
        second[d,a,b,c]=trunc(v,2)

    hess_trace={}
    for a,b in product(range(4),repeat=2):
        v=sp.diff(sp.diff(htrace,X[a]),X[b])
        for r in range(4): v-=Gamma[r,a,b]*sp.diff(htrace,X[r])
        hess_trace[a,b]=trunc(v,2)

    dRic=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        t1=sum(gi2[c,d]*second[d,a,b,c] for c,d in product(range(4),repeat=2))
        t2=sum(gi2[c,d]*second[d,b,a,c] for c,d in product(range(4),repeat=2))
        box=sum(gi2[c,d]*second[c,d,a,b] for c,d in product(range(4),repeat=2))
        dRic[a,b]=trunc(sp.Rational(1,2)*(t1+t2-box-hess_trace[a,b]),2)
    dScalar=trunc(sum(gi2[a,b]*dRic[a,b] for a,b in product(range(4),repeat=2)),2)
    dG=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        # Background Ricci/scalar vanish through degree four by Iter057Q.
        dG[a,b]=trunc(dRic[a,b]-sp.Rational(1,2)*gseed[a,b]*dScalar,2)

    a2=alphas(2)
    residual={}; point_residual={}
    for a,b in PAIRS:
        p=pidx(a,b)
        source=S0[p]+sum(S2[p][a2.index(alpha)]*mon(alpha)/fact(alpha) for alpha in a2)
        residual[f"{a}{b}"]=sp.factor(trunc(dG[a,b]-source,2))
        point_residual[f"{a}{b}"]=sp.factor((dG[a,b]-S0[p]).subs({u:0 for u in X}))
    return {
        "inverse_identity_through_degree2":inv2,
        "gauge":[str(sp.factor(v)) for v in gauge],
        "gauge_zero_exact":all(sp.simplify(v)==0 for v in gauge),
        "point_unreduced_residual":{k:str(v) for k,v in point_residual.items()},
        "point_unreduced_zero_exact":all(v==0 for v in point_residual.values()),
        "DG_minus_S_through_degree2":{k:str(v) for k,v in residual.items()},
        "unreduced_field_zero_exact":all(v==0 for v in residual.values()),
    }


def compute():
    robj,S0,S2=parse_corrected_source()
    Q2=mctor.q2_from_source(S0)
    rhs,_=mctor.assemble_affine_rhs(S0,S2,Q2)
    M,meta,a4=uq4.assemble()
    canonical,labels=uq4.canonical_bianchi_basis(meta)
    compatibility=[sp.factor((v.T*rhs)[0]) for v in canonical]
    rankM=M.rank(); rankAug=M.row_join(rhs).rank()

    _,pc=M.rref(); _,pr=M.T.rref()
    A=M.extract(list(pr),list(pc)); rr=rhs.extract(list(pr),[0]); sv=A.inv()*rr
    qv=[sp.Integer(0)]*M.cols
    for j,v in zip(pc,sv): qv[j]=sp.factor(v)
    residual=M*sp.Matrix(qv)-rhs
    sparse=[]
    for idx,v in enumerate(qv):
        if v==0: continue
        p=idx//len(a4); alpha=a4[idx%len(a4)]
        sparse.append({"pair":list(PAIRS[p]),"alpha":list(alpha),"value":str(v),"over_kappa4":str(sp.factor(v/k**4))})

    gseed,qdata=build_full_seed()
    qbar=qbar_from_jets(Q2,sparse)
    direct=full_seed_unreduced_control(gseed,qbar,S0,S2)

    controls={
        "iter057R_source_replay_pass":robj.get("pass") is True,
        "iter057Q_seed_replay_pass":qdata.get("pass") is True,
        "source_Noether_through_degree1":robj.get("controls",{}).get("Noether_divergence_through_degree1") is True,
        "matrix_shape_180x350":M.rows==180 and M.cols==350,
        "rank_M_exact_164":rankM==164,
        "rank_augmented_equals_rank":rankAug==rankM,
        "all_16_Bianchi_compatibility_zero":len(compatibility)==16 and all(v==0 for v in compatibility),
        "exact_linear_system_residual_zero":all(v==0 for v in residual),
        "full_seed_inverse_control":direct["inverse_identity_through_degree2"],
        "full_seed_Q2_point_unreduced_zero":direct["point_unreduced_zero_exact"],
        "full_seed_deDonder_through_degree3_zero":direct["gauge_zero_exact"],
        "full_seed_unreduced_DG_minus_S_through_degree2_zero":direct["unreduced_field_zero_exact"],
    }
    passed=all(controls.values())
    return {
        "gate":GATE,"preregistration_commit":PREREG,"iter057R_commit":ITER057R,
        "controls":controls,"pass":passed,
        "matrix_shape":[M.rows,M.cols],"rank_M":rankM,"rank_augmented":rankAug,
        "nullity":M.cols-rankM,"left_nullity":M.rows-rankM,
        "canonical_compatibility":[str(v) for v in compatibility],
        "Q2_normalized":{f"{a}{b}{c}{d}":str(Q2[a,b,c,d]) for a,b,c,d in product(range(4),repeat=4) if Q2[a,b,c,d]!=0},
        "Q4_particular_nonzero_count":len(sparse),"Q4_particular_normalized":sparse,
        "direct_unreduced_control":direct,
        "classification":("PASS_SCOPED_ITER057S_ONSHELL_FIRST_ORDER_Q2_Q4_CORRECTION_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_SECOND_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN" if passed else "INVALID_OR_UNRESOLVED_ITER057S"),
        "exact_zero_uses_tolerance":False,"c6_status":"SYMBOLIC_UNFIXED_FACTORED_OUT",
    }


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out");args=ap.parse_args()
    out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:raise SystemExit(2)

if __name__=="__main__":main()
