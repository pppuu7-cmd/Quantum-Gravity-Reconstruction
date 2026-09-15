#!/usr/bin/env python3
"""Iter057Q exact unrestricted sextic c6^0 Einstein-seed completion."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp

import qgr_iter057o_quartic_einstein_seed_completion as o

GATE="ITER057Q-SEXTIC-EINSTEIN-SEED-COMPLETION"
PREREG="afc9098e6de828e8647aad5b1d8316b29f0b61a0"
ITER057O="679a3d73d589fc9161bdf2209f25bb4b7c785fd6"
PAIRS=o.PAIRS
ETA=o.ETA
X=o.X
t,x,y,z=X
eta=o.eta
k=o.k


def alphas(n):
    return sorted(a for a in product(range(n+1),repeat=4) if sum(a)==n)

def pidx(a,b):
    if a>b:a,b=b,a
    return PAIRS.index((a,b))

def homogeneous(expr,degree):
    p=sp.Poly(sp.expand(expr),*X)
    return sp.expand(sum(c*o.mon(a) for a,c in p.terms() if sum(a)==degree))

def normalized_coeff(expr,alpha):
    return sp.Poly(sp.expand(expr),*X).coeff_monomial(o.mon(alpha))*o.fact(alpha)


def einstein_through(g,degree):
    # For degree four, inverse series through h^2 is sufficient since h starts at degree two.
    h=g-eta
    gi=sp.MutableDenseMatrix(eta - eta*h*eta + eta*h*eta*h*eta)
    for a,b in product(range(4),repeat=2): gi[a,b]=o.truncate(gi[a,b],degree)
    inv_ok=all(o.truncate(sum(g[a,c]*gi[c,b] for c in range(4))-(1 if a==b else 0),degree)==0
               for a,b in product(range(4),repeat=2))
    Gamma={}
    for a,b,c in product(range(4),repeat=3):
        v=0
        for d in range(4):
            v += gi[a,d]*(sp.diff(g[d,c],X[b])+sp.diff(g[d,b],X[c])-sp.diff(g[b,c],X[d]))/2
        Gamma[a,b,c]=o.truncate(v,degree+1)
    Ric=sp.MutableDenseMatrix(4,4,[0]*16)
    for b,d in product(range(4),repeat=2):
        v=0
        for a in range(4):
            v += sp.diff(Gamma[a,d,b],X[a])-sp.diff(Gamma[a,a,b],X[d])
            for e in range(4): v += Gamma[a,a,e]*Gamma[e,d,b]-Gamma[a,d,e]*Gamma[e,a,b]
        Ric[b,d]=o.truncate(v,degree)
    scalar=o.truncate(sum(gi[a,b]*Ric[a,b] for a,b in product(range(4),repeat=2)),degree)
    Ein=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        Ein[a,b]=o.truncate(Ric[a,b]-sp.Rational(1,2)*g[a,b]*scalar,degree)
    return gi,Ric,scalar,Ein,inv_ok


def build_system():
    a3,a4,a5,a6=alphas(3),alphas(4),alphas(5),alphas(6)
    col={(p,al):p*len(a6)+j for p in range(10) for j,al in enumerate(a6)}
    rows=[]; meta=[]
    for b in range(4):
        for al in a5:
            d={}
            for a in range(4):
                beta=list(al); beta[a]+=1; beta=tuple(beta)
                j=col[(pidx(a,b),beta)]
                d[j]=d.get(j,0)+ETA[a]
            rows.append(d); meta.append(("G",b,al))
    for p,pair in enumerate(PAIRS):
        for al in a4:
            d={}
            for m in range(4):
                beta=list(al); beta[m]+=2; beta=tuple(beta)
                j=col[(p,beta)]
                d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
            rows.append(d); meta.append(("F",pair,al))
    M=sp.MutableSparseMatrix(574,840,{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
    return M,meta,a3,a4,a5,a6


def canonical_bianchi(meta,a3):
    lookup={m:i for i,m in enumerate(meta)}
    vecs=[]
    for b in range(4):
        for beta in a3:
            v=sp.zeros(574,1)
            for m in range(4):
                al=list(beta); al[m]+=2
                v[lookup[("G",b,tuple(al))]] += sp.Rational(ETA[m],2)
            for a in range(4):
                al=list(beta); al[a]+=1
                pair=(a,b) if a<=b else (b,a)
                v[lookup[("F",pair,tuple(al))]] += ETA[a]
            vecs.append(v)
    return vecs


def compute():
    # Reconstruct the exact fixed Iter057O canonical pivot seed.
    odata=o.compute()
    if odata.get("pass") is not True:
        raise RuntimeError("Iter057O seed replay failed")
    sparse4=odata["particular_R4_normalized"]
    _,_,_,g4=o.build_corrected_metric(sparse4)
    gi4,Ric4,Sc4,Ein4,inv4=einstein_through(g4,4)

    low_zero=all(homogeneous(Ein4[a,b],0)==0 and homogeneous(Ein4[a,b],2)==0
                 for a,b in product(range(4),repeat=2))
    G4={(a,b):sp.factor(homogeneous(Ein4[a,b],4)) for a,b in PAIRS}
    nonzero_G4={f"{a}{b}":str(v) for (a,b),v in G4.items() if v!=0}

    # Exact ordinary divergence of G^(4); lower Einstein orders vanish, so this is the degree-three Bianchi coefficient.
    div4=[]
    for b in range(4):
        v=sum(eta[a,c]*sp.diff(G4.get((a,b) if a<=b else (b,a),0),X[c])
              for a,c in product(range(4),repeat=2))
        div4.append(sp.factor(v))

    M,meta,a3,a4,a5,a6=build_system()
    rhs=[sp.Integer(0)]*(4*len(a5))
    for pair in PAIRS:
        expr=sp.expand(G4[pair]/k**3)
        for al in a4: rhs.append(-sp.factor(normalized_coeff(expr,al)))
    rhs=sp.Matrix(rhs)

    rankM=M.rank(); rankAug=M.row_join(rhs).rank()
    bianchi=canonical_bianchi(meta,a3)
    Y=sp.Matrix.hstack(*bianchi).T
    compatibility=[sp.factor((v.T*rhs)[0]) for v in bianchi]

    # Exact canonical-pivot particular solution, all 346 homogeneous directions set to zero.
    _,pc=M.rref(); _,pr=M.T.rref()
    A=M.extract(list(pr),list(pc)); rr=rhs.extract(list(pr),[0]); sv=A.inv()*rr
    qv=[sp.Integer(0)]*M.cols
    for j,v in zip(pc,sv): qv[j]=sp.factor(v)
    residual=M*sp.Matrix(qv)-rhs
    sparse6=[]
    for idx,v in enumerate(qv):
        if v==0: continue
        p=idx//len(a6); al=a6[idx%len(a6)]
        sparse6.append({"pair":list(PAIRS[p]),"alpha":list(al),"R6_over_kappa3":str(v)})

    # Build trace-reversed sextic correction then undo trace reversal.
    rbar6=sp.MutableDenseMatrix(4,4,[0]*16)
    for item in sparse6:
        a,b=item["pair"]; al=tuple(item["alpha"]); v=sp.Rational(item["R6_over_kappa3"])
        term=k**3*v*o.mon(al)/o.fact(al)
        rbar6[a,b]+=term
        if a!=b:rbar6[b,a]+=term
    tr6=sum(eta[a,b]*rbar6[a,b] for a,b in product(range(4),repeat=2))
    r6=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        r6[a,b]=sp.expand(rbar6[a,b]-sp.Rational(1,2)*eta[a,b]*tr6)
    g6=sp.MutableDenseMatrix(g4+r6)

    pure_degree6=all(all(sum(alpha)==6 for alpha,c in sp.Poly(sp.expand(r6[a,b]),*X).terms())
                     for a,b in product(range(4),repeat=2))

    # Combined linear de Donder check through degree five.
    h=g6-eta; trh=sum(eta[a,b]*h[a,b] for a,b in product(range(4),repeat=2))
    hbar=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):hbar[a,b]=sp.expand(h[a,b]-sp.Rational(1,2)*eta[a,b]*trh)
    gauge=[sp.factor(sum(eta[a,c]*sp.diff(hbar[a,b],X[c]) for a,c in product(range(4),repeat=2))) for b in range(4)]

    gi6,Ric6,Sc6,Ein6,inv6=einstein_through(g6,4)
    ric_zero=all(sp.simplify(Ric6[a,b])==0 for a,b in product(range(4),repeat=2))
    ein_zero=all(sp.simplify(Ein6[a,b])==0 for a,b in product(range(4),repeat=2))

    controls={
        "iter057o_replay_pass":True,
        "iter057o_lower_Einstein_orders_zero":low_zero,
        "inverse_identity_seed4_through_degree4":inv4,
        "degree4_Bianchi_divergence_zero":all(v==0 for v in div4),
        "matrix_shape_574x840":M.rows==574 and M.cols==840,
        "matrix_rank_exact_494":rankM==494,
        "left_nullity_exact_80":M.rows-rankM==80,
        "canonical_Bianchi_count_80":len(bianchi)==80,
        "canonical_Bianchi_rank_80":Y.rank()==80,
        "canonical_Bianchi_annihilates_M":all(v.T*M==sp.zeros(1,M.cols) for v in bianchi),
        "rank_augmented_equals_rank":rankAug==rankM,
        "all_80_compatibility_zero":all(v==0 for v in compatibility),
        "exact_linear_system_residual_zero":all(v==0 for v in residual),
        "r6_pure_degree6_preserves_origin_through_fifth_derivatives":pure_degree6,
        "combined_linear_deDonder_exact":all(v==0 for v in gauge),
        "inverse_identity_corrected_seed_through_degree4":inv6,
        "full_metric_Ricci_through_degree4_zero":ric_zero,
        "full_metric_scalar_through_degree4_zero":sp.simplify(Sc6)==0,
        "full_metric_Einstein_through_degree4_zero":ein_zero,
        "iter057p_four_jet_preserved_by_sextic_correction":pure_degree6,
    }
    passed=all(controls.values())
    return {
        "gate":GATE,"preregistration_commit":PREREG,"iter057o_seed_commit":ITER057O,
        "controls":controls,"pass":passed,
        "degree4_Einstein_residual":nonzero_G4,
        "degree4_residual_nonzero_component_count":len(nonzero_G4),
        "matrix_shape":[M.rows,M.cols],"matrix_nnz":len(M.todok()),
        "rank_M":rankM,"rank_augmented":rankAug,"nullity":M.cols-rankM,"left_nullity":M.rows-rankM,
        "canonical_compatibility":[str(v) for v in compatibility],
        "particular_nonzero_count":len(sparse6),"particular_R6_normalized":sparse6,
        "combined_linear_deDonder":[str(v) for v in gauge],
        "full_metric_Einstein_components":{f"{a}{b}":str(sp.factor(Ein6[a,b])) for a,b in PAIRS},
        "classification":("PASS_SCOPED_ITER057Q_SEXTIC_EINSTEIN_SEED_COMPLETES_THROUGH_QUARTIC_EINSTEIN_ORDER__WEYL3_SECOND_SOURCE_JET_CAN_NOW_BE_RECOMPUTED" if passed else "INVALID_OR_UNRESOLVED_ITER057Q"),
        "exact_zero_uses_tolerance":False,"c6_status":"NOT_USED_ZERO_ORDER_SEED_COMPLETION",
    }


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out");args=ap.parse_args()
    out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:raise SystemExit(2)

if __name__=="__main__":main()
