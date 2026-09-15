#!/usr/bin/env python3
"""Iter057T exact unrestricted octic c6^0 Einstein-seed completion."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import qgr_iter057q_sextic_einstein_seed_completion as q

GATE="ITER057T-OCTIC-EINSTEIN-SEED-COMPLETION"
PREREG="0f01308e81e54f77ccb91f8a76f0c129684740ff"
ITER057Q="c4f1c5c01205a6991e7215e3824111e1f36d1436"
o=q.o
PAIRS=o.PAIRS
ETA=o.ETA
X=o.X
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


def einstein_through6(g):
    h=g-eta
    gi=sp.MutableDenseMatrix(eta - eta*h*eta + eta*h*eta*h*eta - eta*h*eta*h*eta*h*eta)
    for a,b in product(range(4),repeat=2):gi[a,b]=o.truncate(gi[a,b],6)
    inv_ok=all(o.truncate(sum(g[a,c]*gi[c,b] for c in range(4))-(1 if a==b else 0),6)==0 for a,b in product(range(4),repeat=2))
    Gamma={}
    for a,b,c in product(range(4),repeat=3):
        v=sum(gi[a,d]*(sp.diff(g[d,c],X[b])+sp.diff(g[d,b],X[c])-sp.diff(g[b,c],X[d]))/2 for d in range(4))
        Gamma[a,b,c]=o.truncate(v,7)
    Ric=sp.MutableDenseMatrix(4,4,[0]*16)
    for b,d in product(range(4),repeat=2):
        v=0
        for a in range(4):
            v += sp.diff(Gamma[a,d,b],X[a])-sp.diff(Gamma[a,a,b],X[d])
            for e in range(4):v += Gamma[a,a,e]*Gamma[e,d,b]-Gamma[a,d,e]*Gamma[e,a,b]
        Ric[b,d]=o.truncate(v,6)
    scalar=o.truncate(sum(gi[a,b]*Ric[a,b] for a,b in product(range(4),repeat=2)),6)
    Ein=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):Ein[a,b]=o.truncate(Ric[a,b]-sp.Rational(1,2)*g[a,b]*scalar,6)
    return gi,Ric,scalar,Ein,inv_ok


def build_system():
    a5,a6,a7,a8=alphas(5),alphas(6),alphas(7),alphas(8)
    col={(p,al):p*len(a8)+j for p in range(10) for j,al in enumerate(a8)}
    rows=[];meta=[]
    for b in range(4):
        for al in a7:
            d={}
            for a in range(4):
                beta=list(al);beta[a]+=1;beta=tuple(beta);j=col[(pidx(a,b),beta)]
                d[j]=d.get(j,0)+ETA[a]
            rows.append(d);meta.append(("G",b,al))
    for p,pair in enumerate(PAIRS):
        for al in a6:
            d={}
            for m in range(4):
                beta=list(al);beta[m]+=2;beta=tuple(beta);j=col[(p,beta)]
                d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
            rows.append(d);meta.append(("F",pair,al))
    M=sp.MutableSparseMatrix(len(rows),10*len(a8),{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
    return M,meta,a5,a6,a7,a8


def canonical_bianchi(meta,a5):
    lookup={m:i for i,m in enumerate(meta)};vecs=[]
    for b in range(4):
        for beta in a5:
            v=sp.MutableSparseMatrix(len(meta),1,{})
            for m in range(4):
                al=list(beta);al[m]+=2;v[lookup[("G",b,tuple(al))],0]+=sp.Rational(ETA[m],2)
            for a in range(4):
                al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a)
                v[lookup[("F",pair,tuple(al))],0]+=ETA[a]
            vecs.append(v)
    return vecs


def reconstruct_q_seed():
    qdata=q.compute()
    if qdata.get("pass") is not True:raise RuntimeError("Iter057Q replay failed")
    odata=o.compute()
    if odata.get("pass") is not True:raise RuntimeError("Iter057O replay failed")
    _,_,_,g4=o.build_corrected_metric(odata["particular_R4_normalized"])
    rbar6=sp.MutableDenseMatrix(4,4,[0]*16)
    for item in qdata["particular_R6_normalized"]:
        a,b=item["pair"];al=tuple(item["alpha"]);v=sp.Rational(item["R6_over_kappa3"]);term=k**3*v*o.mon(al)/o.fact(al)
        rbar6[a,b]+=term
        if a!=b:rbar6[b,a]+=term
    tr6=sum(eta[a,b]*rbar6[a,b] for a,b in product(range(4),repeat=2));r6=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):r6[a,b]=sp.expand(rbar6[a,b]-sp.Rational(1,2)*eta[a,b]*tr6)
    return sp.MutableDenseMatrix(g4+r6),qdata


def exact_rref(M):
    R,piv=DomainMatrix.from_Matrix(M).to_field().rref()
    return R.to_Matrix(),tuple(piv)


def compute():
    g6,qdata=reconstruct_q_seed();gi6,Ric6,Sc6,Ein6,inv6=einstein_through6(g6)
    low_zero=all(homogeneous(Ein6[a,b],d)==0 for a,b in product(range(4),repeat=2) for d in (0,2,4))
    G6={(a,b):sp.factor(homogeneous(Ein6[a,b],6)) for a,b in PAIRS};nonzero_G6={f"{a}{b}":str(v) for (a,b),v in G6.items() if v!=0}
    div6=[sp.factor(sum(eta[a,c]*sp.diff(G6.get((a,b) if a<=b else (b,a),0),X[c]) for a,c in product(range(4),repeat=2))) for b in range(4)]

    M,meta,a5,a6,a7,a8=build_system();rhs=[sp.Integer(0)]*(4*len(a7))
    for pair in PAIRS:
        expr=sp.expand(G6[pair]/k**4)
        for al in a6:rhs.append(-sp.factor(normalized_coeff(expr,al)))
    rhs=sp.Matrix(rhs)

    _,pc=exact_rref(M);rankM=len(pc)
    Raug,pc_aug=exact_rref(M.row_join(rhs));rankAug=len(pc_aug)
    consistent=(rankAug==rankM and all(j<M.cols for j in pc_aug))

    bianchi=canonical_bianchi(meta,a5);compatibility=[sp.factor((v.T*rhs)[0]) for v in bianchi]
    bianchi_annihilate=all(v.T*M==sp.zeros(1,M.cols) for v in bianchi)
    bianchi_rank_complete=(len(bianchi)==M.rows-rankM==224)

    # Canonical exact particular solution: set every free column to zero and read pivot values from augmented RREF.
    qv=[sp.Integer(0)]*M.cols
    if consistent:
        for row,j in enumerate(pc):qv[j]=sp.factor(Raug[row,M.cols])
    residual=M*sp.Matrix(qv)-rhs

    sparse8=[]
    for idx,v in enumerate(qv):
        if v==0:continue
        p=idx//len(a8);al=a8[idx%len(a8)];sparse8.append({"pair":list(PAIRS[p]),"alpha":list(al),"R8_over_kappa4":str(v)})
    rbar8=sp.MutableDenseMatrix(4,4,[0]*16)
    for item in sparse8:
        a,b=item["pair"];al=tuple(item["alpha"]);v=sp.Rational(item["R8_over_kappa4"]);term=k**4*v*o.mon(al)/o.fact(al)
        rbar8[a,b]+=term
        if a!=b:rbar8[b,a]+=term
    tr8=sum(eta[a,b]*rbar8[a,b] for a,b in product(range(4),repeat=2));r8=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):r8[a,b]=sp.expand(rbar8[a,b]-sp.Rational(1,2)*eta[a,b]*tr8)
    g8=sp.MutableDenseMatrix(g6+r8)
    pure8=all(all(sum(alpha)==8 for alpha,c in sp.Poly(sp.expand(r8[a,b]),*X).terms()) for a,b in product(range(4),repeat=2))
    h=g8-eta;trh=sum(eta[a,b]*h[a,b] for a,b in product(range(4),repeat=2));hbar=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):hbar[a,b]=sp.expand(h[a,b]-sp.Rational(1,2)*eta[a,b]*trh)
    gauge=[sp.factor(sum(eta[a,c]*sp.diff(hbar[a,b],X[c]) for a,c in product(range(4),repeat=2))) for b in range(4)]

    gi8,Ric8,Sc8,Ein8,inv8=einstein_through6(g8);ric_zero=all(sp.simplify(Ric8[a,b])==0 for a,b in product(range(4),repeat=2));ein_zero=all(sp.simplify(Ein8[a,b])==0 for a,b in product(range(4),repeat=2))
    controls={
      "iter057q_replay_pass":True,"lower_Einstein_orders_0_2_4_zero":low_zero,"inverse_identity_seed6_through_degree6":inv6,"degree6_Bianchi_divergence_zero":all(v==0 for v in div6),
      "matrix_shape_1320x1650":M.rows==1320 and M.cols==1650,"matrix_rank_exact_1096":rankM==1096,"left_nullity_exact_224":M.rows-rankM==224,"canonical_Bianchi_count_224":len(bianchi)==224,
      "canonical_Bianchi_complete":bianchi_rank_complete,"canonical_Bianchi_annihilates_M":bianchi_annihilate,"rank_augmented_equals_rank":consistent,"all_224_compatibility_zero":all(v==0 for v in compatibility),
      "exact_linear_system_residual_zero":all(v==0 for v in residual),"r8_pure_degree8_preserves_seed_through_seventh_derivatives":pure8,"combined_linear_deDonder_exact":all(v==0 for v in gauge),
      "inverse_identity_corrected_seed_through_degree6":inv8,"full_metric_Ricci_through_degree6_zero":ric_zero,"full_metric_scalar_through_degree6_zero":sp.simplify(Sc8)==0,"full_metric_Einstein_through_degree6_zero":ein_zero,
    }
    passed=all(controls.values())
    return {"gate":GATE,"preregistration_commit":PREREG,"iter057q_seed_commit":ITER057Q,"controls":controls,"pass":passed,"degree6_Einstein_residual":nonzero_G6,"degree6_residual_nonzero_component_count":len(nonzero_G6),
      "matrix_shape":[M.rows,M.cols],"matrix_nnz":len(M.todok()),"rank_M":rankM,"rank_augmented":rankAug,"nullity":M.cols-rankM,"left_nullity":M.rows-rankM,"compatibility_nonzero_count":sum(v!=0 for v in compatibility),
      "particular_nonzero_count":len(sparse8),"particular_R8_normalized":sparse8,"combined_linear_deDonder":[str(v) for v in gauge],"full_metric_Einstein_components":{f"{a}{b}":str(sp.factor(Ein8[a,b])) for a,b in PAIRS},
      "classification":("PASS_SCOPED_ITER057T_OCTIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_SIX__HIGHER_SEED_ORDERS_REMAIN_OPEN" if passed else "INVALID_OR_UNRESOLVED_ITER057T"),"exact_zero_uses_tolerance":False,"c6_status":"NOT_USED_ZERO_ORDER_SEED_COMPLETION"}


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out");args=ap.parse_args();out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:raise SystemExit(2)

if __name__=="__main__":main()
