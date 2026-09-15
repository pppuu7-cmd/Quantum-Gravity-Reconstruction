#!/usr/bin/env python3
"""Iter057V exact unrestricted O(c6) Q2/Q4/Q6 response through degree four."""
import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import qgr_iter057p_corrected_seed_weyl3_point_source as pseed
import qgr_iter057q_sextic_einstein_seed_completion as qseed
import qgr_iter057s_onshell_q2_q4_correction as sresp

GATE="ITER057V-ONSHELL-FIRST-ORDER-Q2-Q4-Q6-RESPONSE"
PREREG="d6f6cd791e101e6492a33c43d31e8886b2875dd9"
ITER057S="639b0bb33dcb5ea46d54f36b54a8d7dc733421b1"
ITER057T="e4d8b960b8694ee166d05aa3ff089999b843e32a"
ITER057U="20256a1779a3f76c46fcabe9f95cd0dd8c082305"
PAIRS=qseed.PAIRS
ETA=qseed.ETA
X=sresp.X
eta=sresp.eta
k=sresp.k
ROOT=Path(__file__).resolve().parents[1]
S_PATH=ROOT/"data"/"ITER057S_CANONICAL_Q2_Q4_RESPONSE.json"
U_PATH=ROOT/"data"/"ITER057U_CANONICAL_SOURCE_0_2_4.json"
R8_PATH=ROOT/"data"/"ITER057T_CANONICAL_R8_NORMALIZED.json"
S_DIGEST="sha256:b22aff7c02ef056aaed1df7ed06c06b181d4be601e3b05eac7b361856f7143f5"
T_DIGEST="sha256:20134b10e4cf32ecd8b3e417921545714f12b29f4d72f812f6d5121e6b461dba"
U_DIGEST="sha256:fbdd20048f8f4e77618c5829e262538c4320a572c28e7bf6b36adb116e187dad"


def alphas(n): return qseed.alphas(n)
def mon(alpha): return sresp.mon(alpha)
def fact(alpha): return sresp.fact(alpha)
def trunc(expr,degree): return sresp.trunc(expr,degree)
def pidx(a,b): return qseed.pidx(a,b)

def normalized_coeff(expr,alpha):
    return sp.Poly(sp.expand(expr),*X).coeff_monomial(mon(alpha))*fact(alpha)


def exact_rref(M):
    R,piv=DomainMatrix.from_Matrix(M).to_field().rref()
    return R.to_Matrix(),tuple(piv)


def consume_authorities():
    sdata=json.loads(S_PATH.read_text())
    udata=json.loads(U_PATH.read_text())
    s_ok=(sdata.get("terminal_commit")==ITER057S and sdata.get("source_digest")==S_DIGEST and
          len(sdata.get("Q4_particular_normalized",[]))==34)
    urows=udata.get("Shat_normalized_sparse",[])
    u_ok=(udata.get("terminal_commit")==ITER057U and udata.get("source_digest")==U_DIGEST and
          udata.get("basis_count_by_degree")=={"0":10,"1":40,"2":100,"3":200,"4":350} and
          sum(item.get("degree")==4 for item in urows)==64)
    Q2={}
    for key,value in sdata["Q2_normalized"].items():
        a,b,c,d=(int(ch) for ch in key)
        Q2[a,b,c,d]=sp.Rational(value)
    q4=sdata["Q4_particular_normalized"]
    source=sp.MutableDenseMatrix(4,4,[0]*16)
    for item in urows:
        a,b=item["pair"];alpha=tuple(item["alpha"]);value=sp.Rational(item["value"])
        term=value*mon(alpha)/fact(alpha)
        source[a,b]+=term
        if a!=b:source[b,a]+=term
    for a,b in product(range(4),repeat=2):source[a,b]=trunc(source[a,b],4)
    return s_ok,u_ok,Q2,q4,source


def canonical_background4():
    t,x,y,z=X
    q=k*(x*x+y*y-2*z*z)
    g=sp.MutableDenseMatrix(sp.diag(-1-q,1-q,1-q,1-q))
    rbar4=sp.MutableDenseMatrix(4,4,[0]*16)
    for (pair,alpha),coef in pseed.R4.items():
        a,b=pair;c=sp.Rational(coef.numerator,coef.denominator)
        term=k**2*c*mon(alpha)/fact(alpha)
        rbar4[a,b]+=term
        if a!=b:rbar4[b,a]+=term
    tr4=sum(eta[a,b]*rbar4[a,b] for a,b in product(range(4),repeat=2))
    for a,b in product(range(4),repeat=2):
        g[a,b]=trunc(g[a,b]+rbar4[a,b]-sp.Rational(1,2)*eta[a,b]*tr4,4)
    return g


def geometry4(g):
    h=g-eta
    gi=sp.MutableDenseMatrix(eta-eta*h*eta+eta*h*eta*h*eta)
    for a,b in product(range(4),repeat=2):gi[a,b]=trunc(gi[a,b],4)
    inv_ok=all(trunc(sum(g[a,c]*gi[c,b] for c in range(4))-(1 if a==b else 0),4)==0
               for a,b in product(range(4),repeat=2))
    Gamma={}
    for a,b,c in product(range(4),repeat=3):
        v=0
        for d in range(4):
            v+=gi[a,d]*(sp.diff(g[d,c],X[b])+sp.diff(g[d,b],X[c])-sp.diff(g[b,c],X[d]))/2
        Gamma[a,b,c]=trunc(v,3)
    Rup={};Rlow={}
    for a,b,c,d in product(range(4),repeat=4):
        v=sp.diff(Gamma[a,d,b],X[c])-sp.diff(Gamma[a,c,b],X[d])
        for e in range(4):v+=Gamma[a,c,e]*Gamma[e,d,b]-Gamma[a,d,e]*Gamma[e,c,b]
        Rup[a,b,c,d]=trunc(v,2)
    for a,b,c,d in product(range(4),repeat=4):
        Rlow[a,b,c,d]=trunc(sum(g[a,e]*Rup[e,b,c,d] for e in range(4)),2)
    return gi,Gamma,Rlow,inv_ok


def qbar_from_lower(Q2,q4):
    qbar=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        qbar[a,b]=sum(sp.Rational(1,2)*Q2.get((a,b,c,d),0)*X[c]*X[d]
                      for c,d in product(range(4),repeat=2))
    for item in q4:
        a,b=item["pair"];alpha=tuple(item["alpha"]);value=sp.Rational(item["value"])
        term=value*mon(alpha)/fact(alpha)
        qbar[a,b]+=term
        if a!=b:qbar[b,a]+=term
    for a,b in product(range(4),repeat=2):qbar[a,b]=trunc(qbar[a,b],4)
    return qbar


def add_q6(qbar,qv,a6):
    out=sp.MutableDenseMatrix(qbar)
    for idx,value in enumerate(qv):
        if value==0:continue
        p=idx//len(a6);alpha=a6[idx%len(a6)];a,b=PAIRS[p]
        term=value*mon(alpha)/fact(alpha)
        out[a,b]+=term
        if a!=b:out[b,a]+=term
    for a,b in product(range(4),repeat=2):out[a,b]=trunc(out[a,b],6)
    return out


def gauge_vector(qbar,gi,Gamma,degree):
    out=[]
    for b in range(4):
        v=0
        for a,c in product(range(4),repeat=2):
            cov=sp.diff(qbar[a,b],X[c])
            for r in range(4):cov-=Gamma[r,c,a]*qbar[r,b]+Gamma[r,c,b]*qbar[a,r]
            v+=gi[a,c]*cov
        out.append(trunc(v,degree))
    return out


def reduced_DG(qbar,gi,Gamma,Rlow,degree):
    first={}
    for c,a,b in product(range(4),repeat=3):
        v=sp.diff(qbar[a,b],X[c])
        for r in range(4):v-=Gamma[r,c,a]*qbar[r,b]+Gamma[r,c,b]*qbar[a,r]
        first[c,a,b]=trunc(v,degree+1)
    second={}
    for d,c,a,b in product(range(4),repeat=4):
        v=sp.diff(first[c,a,b],X[d])
        for r in range(4):
            v-=Gamma[r,d,c]*first[r,a,b]
            v-=Gamma[r,d,a]*first[c,r,b]
            v-=Gamma[r,d,b]*first[c,a,r]
        second[d,c,a,b]=trunc(v,degree)
    qup=sp.MutableDenseMatrix(4,4,[0]*16)
    for c,d in product(range(4),repeat=2):
        qup[c,d]=trunc(sum(gi[c,e]*gi[d,f]*qbar[e,f] for e,f in product(range(4),repeat=2)),degree)
    DG=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        box=trunc(sum(gi[c,d]*second[c,d,a,b] for c,d in product(range(4),repeat=2)),degree)
        curv=trunc(sum(Rlow[a,c,b,d]*qup[c,d] for c,d in product(range(4),repeat=2)),degree)
        DG[a,b]=trunc(-sp.Rational(1,2)*(box+2*curv),degree)
    return DG


def unreduced_DG(qbar,g,gi,Gamma,source):
    qtrace=trunc(sum(gi[a,b]*qbar[a,b] for a,b in product(range(4),repeat=2)),6)
    h=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):h[a,b]=trunc(qbar[a,b]-sp.Rational(1,2)*g[a,b]*qtrace,6)
    htrace=trunc(sum(gi[a,b]*h[a,b] for a,b in product(range(4),repeat=2)),6)
    first={}
    for c,a,b in product(range(4),repeat=3):
        v=sp.diff(h[a,b],X[c])
        for r in range(4):v-=Gamma[r,c,a]*h[r,b]+Gamma[r,c,b]*h[a,r]
        first[c,a,b]=trunc(v,5)
    second={}
    for d,c,a,b in product(range(4),repeat=4):
        v=sp.diff(first[c,a,b],X[d])
        for r in range(4):
            v-=Gamma[r,d,c]*first[r,a,b]
            v-=Gamma[r,d,a]*first[c,r,b]
            v-=Gamma[r,d,b]*first[c,a,r]
        second[d,c,a,b]=trunc(v,4)
    hess={}
    for a,b in product(range(4),repeat=2):
        v=sp.diff(sp.diff(htrace,X[a]),X[b])
        for r in range(4):v-=Gamma[r,a,b]*sp.diff(htrace,X[r])
        hess[a,b]=trunc(v,4)
    dRic=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):
        t1=trunc(sum(gi[c,d]*second[d,a,b,c] for c,d in product(range(4),repeat=2)),4)
        t2=trunc(sum(gi[c,d]*second[d,b,a,c] for c,d in product(range(4),repeat=2)),4)
        box=trunc(sum(gi[c,d]*second[c,d,a,b] for c,d in product(range(4),repeat=2)),4)
        dRic[a,b]=trunc(sp.Rational(1,2)*(t1+t2-box-hess[a,b]),4)
    dScalar=trunc(sum(gi[a,b]*dRic[a,b] for a,b in product(range(4),repeat=2)),4)
    dG=sp.MutableDenseMatrix(4,4,[0]*16);residual={}
    for a,b in product(range(4),repeat=2):dG[a,b]=trunc(dRic[a,b]-sp.Rational(1,2)*g[a,b]*dScalar,4)
    for a,b in PAIRS:residual[f"{a}{b}"]=sp.factor(trunc(dG[a,b]-source[a,b],4))
    return dG,residual


def compute():
    s_ok,u_ok,Q2,q4,source=consume_authorities()
    r8=json.loads(R8_PATH.read_text())
    r8_ok=(r8.get("source_digest")==T_DIGEST and len(r8.get("particular_R8_normalized",[]))==153 and
           all(sum(item["alpha"])==8 for item in r8.get("particular_R8_normalized",[])))
    g=canonical_background4();gi,Gamma,Rlow,inv4=geometry4(g)
    qlower=qbar_from_lower(Q2,q4)
    gauge0=gauge_vector(qlower,gi,Gamma,5)
    DG0=reduced_DG(qlower,gi,Gamma,Rlow,4)
    field0=sp.MutableDenseMatrix(4,4,[0]*16)
    for a,b in product(range(4),repeat=2):field0[a,b]=trunc(DG0[a,b]-source[a,b],4)
    lower_gauge=all(trunc(v,3)==0 for v in gauge0)
    lower_field=all(trunc(field0[a,b],2)==0 for a,b in PAIRS)

    M,meta,a3,a4,a5,a6=qseed.build_system();rhs=[]
    for b in range(4):
        for alpha in a5:rhs.append(-sp.factor(normalized_coeff(gauge0[b],alpha)))
    for a,b in PAIRS:
        for alpha in a4:rhs.append(-sp.factor(normalized_coeff(field0[a,b],alpha)))
    rhs=sp.Matrix(rhs)
    _,pc=exact_rref(M);rankM=len(pc)
    Raug,pc_aug=exact_rref(M.row_join(rhs));rankAug=len(pc_aug)
    consistent=(rankAug==rankM and all(j<M.cols for j in pc_aug))
    bianchi=qseed.canonical_bianchi(meta,a3)
    compatibility=[sp.factor((v.T*rhs)[0]) for v in bianchi]
    bianchi_ann=all(v.T*M==sp.zeros(1,M.cols) for v in bianchi)
    bianchi_complete=(len(bianchi)==M.rows-rankM==80)
    qv=[sp.Integer(0)]*M.cols
    if consistent:
        for row,j in enumerate(pc):qv[j]=sp.factor(Raug[row,M.cols])
    linres=M*sp.Matrix(qv)-rhs
    sparse=[]
    for idx,value in enumerate(qv):
        if value==0:continue
        p=idx//len(a6);alpha=a6[idx%len(a6)]
        sparse.append({"pair":list(PAIRS[p]),"alpha":list(alpha),"value":str(value),"over_kappa5":str(sp.factor(value/k**5))})

    qtotal=add_q6(qlower,qv,a6)
    gauge_total=gauge_vector(qtotal,gi,Gamma,5)
    _,unred_res=unreduced_DG(qtotal,g,gi,Gamma,source)
    reduced_total=reduced_DG(qtotal,gi,Gamma,Rlow,4)
    red_res={f"{a}{b}":sp.factor(trunc(reduced_total[a,b]-source[a,b],4)) for a,b in PAIRS}
    preserve_lower=all(trunc(qtotal[a,b]-qlower[a,b],5)==0 for a,b in product(range(4),repeat=2))

    controls={
      "A_iter057S_artifact_provenance_exact":s_ok,
      "A_lower_Q2Q4_gauge_through_degree3_zero":lower_gauge,
      "A_lower_Q2Q4_field_through_degree2_zero":lower_field,
      "B_iter057T_R8_provenance_and_pure_degree8":r8_ok,
      "B_background_inverse_through_degree4":inv4,
      "C_iter057U_artifact_provenance_exact":u_ok,
      "C_source_Noether_through_degree3_consumed_from_terminal_Iter057U":u_ok,
      "D_fresh_curved_degree4_residual_computed":True,
      "E_matrix_shape_574x840":M.rows==574 and M.cols==840,
      "F_rank_M_exact_494":rankM==494,
      "F_left_nullity_exact_80":M.rows-rankM==80,
      "F_nullity_exact_346":M.cols-rankM==346,
      "F_canonical_Bianchi_complete":bianchi_complete,
      "F_canonical_Bianchi_annihilates_M":bianchi_ann,
      "G_rank_augmented_equals_rank":consistent,
      "G_all_80_compatibility_zero":len(compatibility)==80 and all(v==0 for v in compatibility),
      "H_exact_affine_residual_zero":all(v==0 for v in linres),
      "I_independent_unreduced_DG_minus_source_through_degree4_zero":all(v==0 for v in unred_res.values()),
      "J_full_covariant_deDonder_through_degree5_zero":all(v==0 for v in gauge_total),
      "K_Q6_preserves_response_through_degree5":preserve_lower,
      "K_reduced_DG_minus_source_through_degree4_zero":all(v==0 for v in red_res.values()),
    }
    passed=all(controls.values())
    if passed:
        classification="PASS_SCOPED_ITER057V_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_FOURTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN"
    elif rankAug>rankM or any(v!=0 for v in compatibility):
        classification="SCIENTIFIC_FAIL_SCOPED_ITER057V_UNRESTRICTED_Q6_RESPONSE_AFFINE_SYSTEM_INCOMPATIBLE"
    else:
        classification="INVALID_ITER057V_LOWER_RESPONSE_MUTATION_OLD_SOURCE_RESTRICTED_ANSATZ_NUMERICAL_EXACTNESS_OR_CONTROL_FAILURE"
    return {
      "gate":GATE,"preregistration_commit":PREREG,"iter057S_commit":ITER057S,"iter057T_commit":ITER057T,"iter057U_commit":ITER057U,
      "controls":controls,"pass":passed,"matrix_shape":[M.rows,M.cols],"rank_M":rankM,"rank_augmented":rankAug,
      "nullity":M.cols-rankM,"left_nullity":M.rows-rankM,"compatibility_nonzero_count":sum(v!=0 for v in compatibility),
      "fixed_Q2Q4_degree4_field_residual_nonzero_count":sum(normalized_coeff(field0[a,b],alpha)!=0 for a,b in PAIRS for alpha in a4),
      "fixed_Q2Q4_degree5_gauge_residual_nonzero_count":sum(normalized_coeff(gauge0[b],alpha)!=0 for b in range(4) for alpha in a5),
      "Q6_particular_nonzero_count":len(sparse),"Q6_particular_normalized":sparse,
      "full_deDonder":[str(sp.factor(v)) for v in gauge_total],"unreduced_DG_minus_source":{kk:str(v) for kk,v in unred_res.items()},
      "classification":classification,"exact_zero_uses_tolerance":False,"c6_status":"SYMBOLIC_UNFIXED_FACTORED_OUT"}


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out");args=ap.parse_args();out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:raise SystemExit(2)

if __name__=="__main__":main()
