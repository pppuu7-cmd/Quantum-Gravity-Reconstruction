#!/usr/bin/env python3
"""Iter057W exact unrestricted decic c6^0 Einstein-seed completion."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import qgr_iter057t_octic_einstein_seed_completion as t

GATE="ITER057W-DECIC-EINSTEIN-SEED-COMPLETION"
PREREG="7e6336d195985b2059966eda64859da86c9e9d15"
ITER057T="e4d8b960b8694ee166d05aa3ff089999b843e32a"
T_ARTIFACT=10408050133
T_DIGEST="sha256:20134b10e4cf32ecd8b3e417921545714f12b29f4d72f812f6d5121e6b461dba"
R8_PATH=Path(__file__).resolve().parents[1]/"data"/"ITER057T_CANONICAL_R8_NORMALIZED.json"
o=t.o
PAIRS=t.PAIRS
ETA=t.ETA
X=t.X
eta=t.eta
k=t.k


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


def exact_rank(M):
    return DomainMatrix.from_Matrix(M).to_field().rank()


def exact_rref(M):
    R,piv=DomainMatrix.from_Matrix(M).to_field().rref()
    return R.to_Matrix(),tuple(piv)


def reconstruct_t_seed():
    g6,qdata=t.reconstruct_q_seed()
    r8data=json.loads(R8_PATH.read_text())
    provenance=(r8data.get("source_commit")==ITER057T and r8data.get("source_artifact")==T_ARTIFACT and
                r8data.get("source_digest")==T_DIGEST and len(r8data.get("particular_R8_normalized",[]))==153)
    rbar8=sp.MutableDenseMatrix(4,4,[0]*16)
    for item in r8data["particular_R8_normalized"]:
        a,b=item["pair"];al=tuple(item["alpha"]);v=sp.Rational(item["R8_over_kappa4"])
        term=k**4*v*o.mon(al)/o.fact(al)
        rbar8[a,b]+=term
        if a!=b:rbar8[b,a]+=term
    tr8=sum(eta[a,b]*rbar8[a,b] for a,b in product(range(4),repeat=2))
    r8=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        r8[a,b]=sp.expand(rbar8[a,b]-sp.Rational(1,2)*eta[a,b]*tr8)
    pure8=all(all(sum(alpha)==8 for alpha,c in sp.Poly(sp.expand(r8[a,b]),*X).terms()) for a,b in product(range(4),repeat=2))
    return sp.MutableDenseMatrix(g6+r8),qdata,r8data,provenance and pure8


def einstein_through8(g):
    h=g-eta
    gi=sp.MutableDenseMatrix(eta - eta*h*eta + eta*h*eta*h*eta - eta*h*eta*h*eta*h*eta + eta*h*eta*h*eta*h*eta*h*eta)
    for a,b in product(range(4),repeat=2):gi[a,b]=o.truncate(gi[a,b],8)
    inv_ok=all(o.truncate(sum(g[a,c]*gi[c,b] for c in range(4))-(1 if a==b else 0),8)==0 for a,b in product(range(4),repeat=2))
    Gamma={}
    for a,b,c in product(range(4),repeat=3):
        v=sum(gi[a,d]*(sp.diff(g[d,c],X[b])+sp.diff(g[d,b],X[c])-sp.diff(g[b,c],X[d]))/2 for d in range(4))
        Gamma[a,b,c]=o.truncate(v,9)
    Ric=sp.MutableDenseMatrix(4,4,[0]*16)
    for b,d in product(range(4),repeat=2):
        v=0
        for a in range(4):
            v += sp.diff(Gamma[a,d,b],X[a])-sp.diff(Gamma[a,a,b],X[d])
            for e in range(4):v += Gamma[a,a,e]*Gamma[e,d,b]-Gamma[a,d,e]*Gamma[e,a,b]
        Ric[b,d]=o.truncate(v,8)
    scalar=o.truncate(sum(gi[a,b]*Ric[a,b] for a,b in product(range(4),repeat=2)),8)
    Ein=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):Ein[a,b]=o.truncate(Ric[a,b]-sp.Rational(1,2)*g[a,b]*scalar,8)
    return gi,Ric,scalar,Ein,inv_ok


def build_system():
    a7,a8,a9,a10=alphas(7),alphas(8),alphas(9),alphas(10)
    col={(p,al):p*len(a10)+j for p in range(10) for j,al in enumerate(a10)}
    rows=[];meta=[]
    for b in range(4):
        for al in a9:
            d={}
            for a in range(4):
                beta=list(al);beta[a]+=1;beta=tuple(beta);j=col[(pidx(a,b),beta)]
                d[j]=d.get(j,0)+ETA[a]
            rows.append(d);meta.append(("G",b,al))
    for p,pair in enumerate(PAIRS):
        for al in a8:
            d={}
            for m in range(4):
                beta=list(al);beta[m]+=2;beta=tuple(beta);j=col[(p,beta)]
                d[j]=d.get(j,0)-sp.Rational(ETA[m],2)
            rows.append(d);meta.append(("F",pair,al))
    M=sp.MutableSparseMatrix(len(rows),10*len(a10),{(i,j):v for i,d in enumerate(rows) for j,v in d.items() if v})
    return M,meta,a7,a8,a9,a10


def canonical_bianchi(meta,a7):
    lookup={m:i for i,m in enumerate(meta)};vecs=[]
    for b in range(4):
        for beta in a7:
            v=sp.MutableSparseMatrix(len(meta),1,{})
            for m in range(4):
                al=list(beta);al[m]+=2;v[lookup[("G",b,tuple(al))],0]+=sp.Rational(ETA[m],2)
            for a in range(4):
                al=list(beta);al[a]+=1;pair=(a,b) if a<=b else (b,a)
                v[lookup[("F",pair,tuple(al))],0]+=ETA[a]
            vecs.append(v)
    return vecs


def flat_dedonder(g):
    h=g-eta
    trh=sum(eta[a,b]*h[a,b] for a,b in product(range(4),repeat=2))
    hbar=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):hbar[a,b]=sp.expand(h[a,b]-sp.Rational(1,2)*eta[a,b]*trh)
    return [o.truncate(sum(eta[a,c]*sp.diff(hbar[a,b],X[c]) for a,c in product(range(4),repeat=2)),9) for b in range(4)]


def compute():
    g8,qdata,r8data,t_replay=reconstruct_t_seed()
    gi8,Ric8,Sc8,Ein8,inv8=einstein_through8(g8)
    lower_zero=all(homogeneous(Ein8[a,b],d)==0 for a,b in product(range(4),repeat=2) for d in (0,2,4,6))
    G8={(a,b):sp.factor(homogeneous(Ein8[a,b],8)) for a,b in PAIRS}
    nonzero_G8={f"{a}{b}":str(v) for (a,b),v in G8.items() if v!=0}
    div8=[]
    for b in range(4):
        v=0
        for a,c in product(range(4),repeat=2):
            pair=(a,b) if a<=b else (b,a)
            v+=eta[a,c]*sp.diff(G8[pair],X[c])
        div8.append(sp.factor(v))

    M,meta,a7,a8,a9,a10=build_system()
    rhs=[sp.Integer(0)]*(4*len(a9))
    for pair in PAIRS:
        expr=sp.expand(G8[pair]/k**5)
        for al in a8:rhs.append(-sp.factor(normalized_coeff(expr,al)))
    rhs=sp.Matrix(rhs)

    rankM=exact_rank(M)
    Raug,piv_aug=exact_rref(M.row_join(rhs));rankAug=len(piv_aug)
    consistent=(rankAug==rankM and all(j<M.cols for j in piv_aug))

    bianchi=canonical_bianchi(meta,a7)
    compatibility=[sp.factor((v.T*rhs)[0]) for v in bianchi]
    bianchi_annihilate=all(v.T*M==sp.zeros(1,M.cols) for v in bianchi)
    bianchi_complete=(len(bianchi)==M.rows-rankM==480)

    qv=[sp.Integer(0)]*M.cols
    if consistent:
        for row,j in enumerate(piv_aug):
            if j<M.cols:qv[j]=sp.factor(Raug[row,M.cols])
    residual=M*sp.Matrix(qv)-rhs

    sparse10=[]
    for idx,v in enumerate(qv):
        if v==0:continue
        p=idx//len(a10);al=a10[idx%len(a10)]
        sparse10.append({"pair":list(PAIRS[p]),"alpha":list(al),"R10_over_kappa5":str(v)})
    rbar10=sp.MutableDenseMatrix(4,4,[0]*16)
    for item in sparse10:
        a,b=item["pair"];al=tuple(item["alpha"]);v=sp.Rational(item["R10_over_kappa5"])
        term=k**5*v*o.mon(al)/o.fact(al)
        rbar10[a,b]+=term
        if a!=b:rbar10[b,a]+=term
    tr10=sum(eta[a,b]*rbar10[a,b] for a,b in product(range(4),repeat=2))
    r10=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):r10[a,b]=sp.expand(rbar10[a,b]-sp.Rational(1,2)*eta[a,b]*tr10)
    pure10=all(all(sum(alpha)==10 for alpha,c in sp.Poly(sp.expand(r10[a,b]),*X).terms()) for a,b in product(range(4),repeat=2))
    g10=sp.MutableDenseMatrix(g8+r10)
    preserve_lower=all(o.truncate(g10[a,b]-g8[a,b],9)==0 for a,b in product(range(4),repeat=2))
    gauge=flat_dedonder(g10)

    gi10,Ric10,Sc10,Ein10,inv10=einstein_through8(g10)
    ric_zero=all(sp.expand(Ric10[a,b])==0 for a,b in product(range(4),repeat=2))
    scalar_zero=sp.expand(Sc10)==0
    ein_zero=all(sp.expand(Ein10[a,b])==0 for a,b in product(range(4),repeat=2))

    controls={
      "A_iter057T_canonical_R8_provenance_and_replay":t_replay,
      "A_iter057Q_replay_pass":qdata.get("pass") is True,
      "A_lower_Einstein_orders_0_2_4_6_zero":lower_zero,
      "A_seed8_inverse_identity_through_degree8":inv8,
      "B_degree8_residual_directly_computed":True,
      "B_degree8_flat_Bianchi_divergence_zero":all(v==0 for v in div8),
      "C_matrix_shape_2530x2860":M.rows==2530 and M.cols==2860,
      "D_rank_M_exact_2050":rankM==2050,
      "D_left_nullity_exact_480":M.rows-rankM==480,
      "D_nullity_exact_810":M.cols-rankM==810,
      "D_canonical_Bianchi_count_480":len(bianchi)==480,
      "D_canonical_Bianchi_complete":bianchi_complete,
      "D_canonical_Bianchi_annihilates_M":bianchi_annihilate,
      "E_rank_augmented_equals_rank_2050":consistent and rankAug==2050,
      "E_all_480_compatibility_zero":len(compatibility)==480 and all(v==0 for v in compatibility),
      "F_exact_affine_residual_zero":all(v==0 for v in residual),
      "F_homogeneous_freedom_810_retained":M.cols-rankM==810,
      "G_completed_inverse_identity_through_degree8":inv10,
      "G_full_metric_Ricci_through_degree8_zero":ric_zero,
      "G_full_metric_scalar_through_degree8_zero":scalar_zero,
      "G_full_metric_Einstein_through_degree8_zero":ein_zero,
      "G_combined_linear_deDonder_through_degree9_zero":all(v==0 for v in gauge),
      "H_R10_pure_degree10":pure10,
      "H_preserves_all_seed_terms_through_degree9":preserve_lower,
      "I_exact_zero_uses_no_tolerance":True,
    }
    passed=all(controls.values())
    if passed:
        classification="PASS_SCOPED_ITER057W_DECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_EIGHT__HIGHER_SEED_ORDERS_REMAIN_OPEN"
    elif rankAug>rankM and bianchi_complete and bianchi_annihilate and any(v!=0 for v in compatibility):
        classification="SCIENTIFIC_FAIL_SCOPED_ITER057W_UNRESTRICTED_DECIC_EINSTEIN_SEED_SYSTEM_INCOMPATIBLE"
    else:
        classification="INVALID_OR_UNRESOLVED_ITER057W"
    return {
      "gate":GATE,"preregistration_commit":PREREG,"iter057T_commit":ITER057T,
      "controls":controls,"pass":passed,"classification":classification,
      "degree8_Einstein_residual_nonzero_component_count":len(nonzero_G8),"degree8_Einstein_residual":nonzero_G8,
      "degree8_flat_Bianchi_divergence":[str(v) for v in div8],
      "matrix_shape":[M.rows,M.cols],"matrix_nnz":len(M.todok()),"rank_M":rankM,"rank_augmented":rankAug,
      "nullity":M.cols-rankM,"left_nullity":M.rows-rankM,"compatibility_nonzero_count":sum(v!=0 for v in compatibility),
      "particular_nonzero_count":len(sparse10),"particular_R10_normalized":sparse10,
      "combined_linear_deDonder":[str(v) for v in gauge],
      "full_metric_Einstein_components":{f"{a}{b}":str(sp.factor(Ein10[a,b])) for a,b in PAIRS},
      "source_R8_artifact":T_ARTIFACT,"source_R8_digest":T_DIGEST,
      "homogeneous_freedom_dimension":M.cols-rankM,"exact_zero_uses_tolerance":False,
      "c6_status":"NOT_USED_ZERO_ORDER_SEED_COMPLETION",
      "scope":"FINITE_LOCAL_TAYLOR_CERTIFICATE_ONLY",
    }


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out");args=ap.parse_args()
    out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:raise SystemExit(2)

if __name__=="__main__":main()
