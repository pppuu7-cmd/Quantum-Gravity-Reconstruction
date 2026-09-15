#!/usr/bin/env python3
"""Iter057U exact corrected-seed Weyl3 Euler source through coordinate degree four.

Uses exact Fraction polynomial arithmetic. The canonical Iter057T octic pivot is
consumed from its frozen artifact-derived coefficient file; no lower homogeneous
seed freedom is re-solved or changed.
"""
import argparse
import json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

import qgr_iter057r_corrected_seed_weyl3_second_source_jet as r

N=r.N
K=r.K
ETA=r.ETA
ZERO=r.ZERO
PAIRS=r.PAIRS
GATE="ITER057U-CORRECTED-SEED-WEYL3-FOURTH-SOURCE-JET"
PREREG="72eb0c6ffdcff789d7929a766e8f237475f89aaf"
ITER057R="e395d2fb4be3e6f556f893ce63ae68f3b4b51ea2"
ITER057T="e4d8b960b8694ee166d05aa3ff089999b843e32a"
T_RUN=34995145254
T_ARTIFACT=10408050133
T_DIGEST="sha256:20134b10e4cf32ecd8b3e417921545714f12b29f4d72f812f6d5121e6b461dba"
R8_PATH=Path(__file__).resolve().parents[1]/"data"/"ITER057T_CANONICAL_R8_NORMALIZED.json"

R0={
    ((0,0),ZERO):F(240), ((1,1),ZERO):F(384),
    ((2,2),ZERO):F(384), ((3,3),ZERO):F(-432),
}
R2={
    ((0,0),(2,0,0,0)):F(-448), ((0,0),(0,2,0,0)):F(3936),
    ((0,0),(0,0,2,0)):F(3936), ((0,0),(0,0,0,2)):F(-26240),
    ((0,1),(1,1,0,0)):F(2896), ((0,2),(1,0,1,0)):F(2896),
    ((0,3),(1,0,0,1)):F(-6240),
    ((1,1),(2,0,0,0)):F(10736), ((1,1),(0,2,0,0)):F(6832),
    ((1,1),(0,0,2,0)):F(7952), ((1,1),(0,0,0,2)):F(-14960),
    ((1,2),(0,1,1,0)):F(-560), ((1,3),(0,1,0,1)):F(-3952),
    ((2,2),(2,0,0,0)):F(10736), ((2,2),(0,2,0,0)):F(7952),
    ((2,2),(0,0,2,0)):F(6832), ((2,2),(0,0,0,2)):F(-14960),
    ((2,3),(0,0,1,1)):F(-3952),
    ((3,3),(2,0,0,0)):F(-19904), ((3,3),(0,2,0,0)):F(-10272),
    ((3,3),(0,0,2,0)):F(-10272), ((3,3),(0,0,0,2)):F(2816),
}

const=r.const; mono=r.mono; add=r.add; neg=r.neg; sub=r.sub
scale=r.scale; mul=r.mul; deriv=r.deriv; trunc=r.trunc
v0=r.v0; fstr=r.fstr; psign=r.psign; pmat=r.pmat; fact=r.fact


def alphas(d):
    return sorted(a for a in product(range(d+1),repeat=4) if sum(a)==d)


def seed_metric8():
    g,qdata=r.seed_metric()
    data=json.loads(R8_PATH.read_text())
    provenance=(data.get("source_artifact")==T_ARTIFACT and
                data.get("source_digest")==T_DIGEST and
                data.get("source_run")==T_RUN and
                data.get("source_commit")==ITER057T)
    rows=data.get("particular_R8_normalized",[])
    rbar8=pmat()
    for item in rows:
        a,b=item["pair"]; alpha=tuple(item["alpha"]); coef=F(item["R8_over_kappa4"])
        term=mono(alpha,K**4*coef/F(fact(alpha)))
        rbar8[a][b]=add(rbar8[a][b],term)
        if a!=b:rbar8[b][a]=add(rbar8[b][a],term)
    tr8={}
    for a in range(N):tr8=add(tr8,scale(rbar8[a][a],ETA[a]))
    for a,b in product(range(N),repeat=2):
        rr=dict(rbar8[a][b])
        if a==b:rr=add(rr,scale(tr8,-F(ETA[a],2)))
        g[a][b]=add(g[a][b],rr)
    return g,qdata,provenance,len(rows)


def inverse6(g):
    h=pmat()
    for a,b in product(range(N),repeat=2):
        h[a][b]=dict(g[a][b])
        if a==b:h[a][b]=sub(h[a][b],const(ETA[a]))
    gi=pmat()
    for a,b in product(range(N),repeat=2):
        if a==b:gi[a][b]=const(ETA[a])
        gi[a][b]=add(gi[a][b],scale(h[a][b],-ETA[a]*ETA[b]))
        hh={}
        for c in range(N):hh=add(hh,scale(mul(h[a][c],h[c][b],6),ETA[a]*ETA[c]*ETA[b]))
        gi[a][b]=add(gi[a][b],hh)
        hhh={}
        for c,d in product(range(N),repeat=2):
            term=mul(mul(h[a][c],h[c][d],6),h[d][b],6)
            hhh=add(hhh,scale(term,-ETA[a]*ETA[c]*ETA[d]*ETA[b]))
        gi[a][b]=trunc(add(gi[a][b],hhh),6)
    return gi


def normalized(poly,alpha):
    return poly.get(tuple(alpha),F(0))*F(fact(alpha))


def compute():
    g,qdata,prov_ok,r8_count=seed_metric8(); gi=inverse6(g)
    inverse_ok=True
    for a,b in product(range(N),repeat=2):
        s={}
        for c in range(N):s=add(s,mul(g[a][c],gi[c][b],6))
        if trunc(sub(s,const(1 if a==b else 0)),6):inverse_ok=False

    Gamma=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N),repeat=3):
        val={}
        for d in range(N):
            t=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            val=add(val,mul(gi[a][d],t,7))
        Gamma[a][b][c]=scale(trunc(val,7),F(1,2))

    Rup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val=sub(deriv(Gamma[a][d][b],c),deriv(Gamma[a][c][b],d))
        for e in range(N):
            val=add(val,sub(mul(Gamma[a][c][e],Gamma[e][d][b],6),mul(Gamma[a][d][e],Gamma[e][c][b],6)))
        Rup[a][b][c][d]=trunc(val,6)
    Rlow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e in range(N):val=add(val,mul(g[a][e],Rup[e][b][c][d],6))
        Rlow[a][b][c][d]=trunc(val,6)

    Ric=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N):val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,6)
    Scal={}
    for a,b in product(range(N),repeat=2):Scal=add(Scal,mul(gi[a][b],Ric[a][b],6))
    Scal=trunc(Scal,6)
    Ein=pmat()
    for a,b in product(range(N),repeat=2):Ein[a][b]=trunc(sub(Ric[a][b],scale(mul(g[a][b],Scal,6),F(1,2))),6)
    ricci_zero=all(not Ric[a][b] for a,b in product(range(N),repeat=2))
    scalar_zero=not Scal
    einstein_zero=all(not Ein[a][b] for a,b in product(range(N),repeat=2))
    lower_seed_ok=(qdata.get("pass") is True and prov_ok and r8_count==153 and inverse_ok and ricci_zero and scalar_zero and einstein_zero)
    if not lower_seed_ok:
        controls={
            "A_iter057T_R8_provenance_exact":prov_ok and r8_count==153,
            "A_inverse_identity_through_degree6":inverse_ok,
            "B_seed_Ricci_through_degree6_zero":ricci_zero,
            "B_seed_scalar_through_degree6_zero":scalar_zero,
            "B_seed_Einstein_through_degree6_zero":einstein_zero,
        }
        return {"gate":GATE,"preregistration_commit":PREREG,"iter057R_commit":ITER057R,"iter057T_commit":ITER057T,
                "controls":controls,"pass":False,"classification":"INVALID_ITER057U_OLD_SOURCE_SEED_MUTATION_RESTRICTED_ANSATZ_NORMALIZATION_OR_EXACTNESS_CONTROL",
                "exact_zero_uses_tolerance":False,"c6_status":"SYMBOLIC_UNFIXED_FACTORED_OUT"}

    C=Rlow
    Cup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,r1,s1 in product(range(N),repeat=4):
        val={}
        for m,n in product(range(N),repeat=2):val=add(val,mul(mul(gi[r1][m],gi[s1][n],6),C[a][b][m][n],6))
        Cup[a][b][r1][s1]=trunc(val,6)

    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for rr,ss in product(range(N),repeat=2):val=add(val,mul(Cup[a][b][rr][ss],C[rr][ss][c][d],6))
        Q[a][b][c][d]=trunc(val,6)

    perms=list(permutations(range(4)))
    Qr=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        inds=(a,b,c,d);alt={}
        for pp in perms:alt=add(alt,scale(Q[inds[pp[0]]][inds[pp[1]]][inds[pp[2]]][inds[pp[3]]],F(psign(pp),24)))
        Qr[a][b][c][d]=trunc(sub(Q[a][b][c][d],alt),6)

    QRic=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a,c in product(range(N),repeat=2):val=add(val,mul(gi[a][c],Qr[a][b][c][d],6))
        QRic[b][d]=trunc(val,6)
    QSc={}
    for b,d in product(range(N),repeat=2):QSc=add(QSc,mul(gi[b][d],QRic[b][d],6))
    QSc=trunc(QSc,6)

    Plow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rt=add(sub(mul(g[a][c],QRic[d][b],6),mul(g[a][d],QRic[c][b],6)),add(neg(mul(g[b][c],QRic[d][a],6)),mul(g[b][d],QRic[c][a],6)))
        rt=scale(rt,F(1,2));gg=scale(sub(mul(g[a][c],g[d][b],6),mul(g[a][d],g[c][b],6)),F(1,2))
        Plow[a][b][c][d]=scale(trunc(add(sub(Qr[a][b][c][d],rt),scale(mul(QSc,gg,6),F(1,3))),6),3)

    P=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for i,j,m,n in product(range(N),repeat=4):
            raiser=mul(mul(gi[a][i],gi[b][j],6),mul(gi[c][m],gi[d][n],6),6)
            val=add(val,mul(raiser,Plow[i][j][m][n],6))
        P[a][b][c][d]=trunc(val,6)

    I3={}
    for a,b,c,d,e,f in product(range(N),repeat=6):I3=add(I3,mul(mul(Cup[a][b][c][d],Cup[c][d][e][f],4),Cup[e][f][a][b],4))
    I3=trunc(I3,4)
    PR={}
    for a,b,c,d in product(range(N),repeat=4):PR=add(PR,mul(P[a][b][c][d],Rlow[a][b][c][d],4))
    PR=trunc(PR,4);homogeneity=not trunc(sub(PR,scale(I3,3)),4)

    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,b,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=deriv(P[a][m][b][n],a)
            for rr in range(N):
                term=add(term,mul(Gamma[a][a][rr],P[rr][m][b][n],5));term=add(term,mul(Gamma[m][a][rr],P[a][rr][b][n],5))
                term=add(term,mul(Gamma[b][a][rr],P[a][m][rr][n],5));term=add(term,mul(Gamma[n][a][rr],P[a][m][b][rr],5))
            val=add(val,term)
        FD[m][b][n]=trunc(val,5)
    D=pmat()
    for m,n in product(range(N),repeat=2):
        val={}
        for b in range(N):
            term=deriv(FD[m][b][n],b)
            for rr in range(N):
                term=add(term,mul(Gamma[m][b][rr],FD[rr][b][n],4));term=add(term,mul(Gamma[b][b][rr],FD[m][rr][n],4));term=add(term,mul(Gamma[n][b][rr],FD[m][b][rr],4))
            val=add(val,term)
        D[m][n]=trunc(val,4)

    def bone(a,b):
        val={}
        for c,d,e,f in product(range(N),repeat=4):val=add(val,mul(mul(P[a][c][d][e],gi[b][f],4),Rlow[f][c][d][e],4))
        return trunc(val,4)
    B=pmat()
    for a,b in product(range(N),repeat=2):B[a][b]=scale(add(bone(a,b),bone(b,a)),F(1,2))

    Eup=pmat()
    for a,b in product(range(N),repeat=2):
        val=add(neg(B[a][b]),scale(D[a][b],-2));val=add(val,scale(mul(gi[a][b],I3,4),F(1,2)));Eup[a][b]=trunc(val,4)
    Edown=pmat()
    for a,b in product(range(N),repeat=2):
        val={}
        for c,d in product(range(N),repeat=2):val=add(val,mul(mul(g[a][c],g[b][d],4),Eup[c][d],4))
        Edown[a][b]=trunc(val,4)

    sym=all(not trunc(sub(Edown[a][b],Edown[b][a]),4) for a,b in product(range(N),repeat=2))
    trace={}
    for a,b in product(range(N),repeat=2):trace=add(trace,mul(gi[a][b],Edown[a][b],4))
    trace_ward=not trunc(add(trunc(trace,4),I3),4)
    noether=[]
    for b in range(N):
        val={}
        for a in range(N):
            val=add(val,deriv(Eup[a][b],a))
            for rr in range(N):val=add(val,mul(Gamma[a][a][rr],Eup[rr][b],3));val=add(val,mul(Gamma[b][a][rr],Eup[a][rr],3))
        noether.append(trunc(val,3))
    noether_ok=all(not x for x in noether)

    odd_nonzero=[];source_sparse=[];degree_counts={d:0 for d in range(5)};d4_nonzero=0;d4_time=0;d4_offdiag=0
    for a,b in PAIRS:
        S=neg(Edown[a][b])
        for alpha,raw in sorted(S.items()):
            d=sum(alpha)
            if d>4:continue
            norm=raw*F(fact(alpha))
            if not norm:continue
            degree_counts[d]+=1
            if d in (1,3):odd_nonzero.append((a,b,alpha,norm))
            rec={"pair":[a,b],"alpha":list(alpha),"degree":d,"value":fstr(norm)}
            if d==0:rec["over_kappa3"]=fstr(norm/(K**3))
            elif d==2:rec["over_kappa4"]=fstr(norm/(K**4))
            elif d==4:rec["over_kappa5"]=fstr(norm/(K**5))
            source_sparse.append(rec)
            if d==4:
                d4_nonzero+=1
                if alpha[0]:d4_time+=1
                if a!=b:d4_offdiag+=1

    lower_match=True;mismatches=[]
    for a,b in PAIRS:
        S=neg(Edown[a][b]);got0=normalized(S,ZERO)/(K**3);exp0=R0.get(((a,b),ZERO),F(0))
        if got0!=exp0:mismatches.append([a,b,list(ZERO),fstr(got0),fstr(exp0)]);lower_match=False
        for alpha in alphas(2):
            got=normalized(S,alpha)/(K**4);exp=R2.get(((a,b),alpha),F(0))
            if got!=exp:mismatches.append([a,b,list(alpha),fstr(got),fstr(exp)]);lower_match=False

    basis_by_degree={str(d):10*len(alphas(d)) for d in range(5)};basis_total=sum(basis_by_degree.values())
    controls={
        "A_iter057T_R8_provenance_exact":prov_ok and r8_count==153,"A_inverse_identity_through_degree6":inverse_ok,
        "B_seed_Ricci_through_degree6_zero":ricci_zero,"B_seed_scalar_through_degree6_zero":scalar_zero,"B_seed_Einstein_through_degree6_zero":einstein_zero,
        "C_P_dot_R_equals_3I3_through_degree4":homogeneity,"D_E_W3_down_symmetric_through_degree4":sym,
        "E_trace_Ward_through_degree4":trace_ward,"F_Noether_divergence_through_degree3":noether_ok,
        "G_odd_source_coefficients_through_degree3_zero":not odd_nonzero,"H_complete_Iter057R_degree0_degree2_replay":lower_match,
        "I_full_basis_count_700":basis_total==700 and basis_by_degree=={"0":10,"1":40,"2":100,"3":200,"4":350},
    }
    passed=all(controls.values())
    classification=("PASS_SCOPED_ITER057U_CORRECTED_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_FOURTH_EVEN_ORDER__O_C6_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED" if passed else "INVALID_ITER057U_OLD_SOURCE_SEED_MUTATION_RESTRICTED_ANSATZ_NORMALIZATION_OR_EXACTNESS_CONTROL")
    return {"gate":GATE,"preregistration_commit":PREREG,"iter057R_commit":ITER057R,"iter057T_commit":ITER057T,"iter057T_artifact":T_ARTIFACT,"iter057T_artifact_digest":T_DIGEST,
        "kappa":fstr(K),"controls":controls,"pass":passed,"basis_count_by_degree":basis_by_degree,"basis_total":basis_total,
        "source_nonzero_count_by_degree":{str(k):v for k,v in degree_counts.items()},"degree4_nonzero_count":d4_nonzero,
        "degree4_time_containing_nonzero_count":d4_time,"degree4_offdiagonal_nonzero_count":d4_offdiag,"Shat_normalized_sparse":source_sparse,
        "iter057R_replay_mismatches":mismatches,"I3_origin_over_kappa3":fstr(v0(I3)/(K**3)),"classification":classification,
        "exact_zero_uses_tolerance":False,"c6_status":"SYMBOLIC_UNFIXED_FACTORED_OUT"}


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out");args=ap.parse_args();out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:Path(args.out).parent.mkdir(parents=True,exist_ok=True);Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:raise SystemExit(2)

if __name__=="__main__":main()
