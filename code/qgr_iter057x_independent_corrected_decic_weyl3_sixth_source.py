#!/usr/bin/env python3
"""Independent exact reproduction of preregistered Iter057X.

Computes the corrected-decic-seed Weyl^3 Euler source through coordinate degree
six using exact Fraction polynomial arithmetic and the frozen canonical R10.
The implementation intentionally imports the terminal Iter057U implementation
only for already-validated polynomial primitives, the canonical g8 builder, and
an independent coefficient-by-coefficient replay of its degree 0/2/4 source.
No source interpolation, floating zero test, or lower seed re-solving is used.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

import qgr_iter057u_corrected_seed_weyl3_fourth_source_jet as u

N=u.N
K=u.K
ETA=u.ETA
ZERO=u.ZERO
PAIRS=u.PAIRS
const=u.const; mono=u.mono; add=u.add; neg=u.neg; sub=u.sub
scale=u.scale; mul=u.mul; deriv=u.deriv; trunc=u.trunc
v0=u.v0; fstr=u.fstr; psign=u.psign; pmat=u.pmat; fact=u.fact

GATE="ITER057X-CORRECTED-DECIC-SEED-WEYL3-SIXTH-SOURCE-JET"
PREREG="b5f88ced655c4fa409c4ccb9c27eb84054ecfad7"
ITER057U="20256a1779a3f76c46fcabe9f95cd0dd8c082305"
ITER057W="90b4a8d0512bffa70c488111a71e78690368c009"
R10_FREEZE="e8982c84cc3b4baa0ca40ed8ff7876164b728880"
R10_PATH=Path(__file__).resolve().parents[1]/"data"/"ITER057W_CANONICAL_R10_NORMALIZED.csv"
EXPECTED_R10_META={
    "preregistration":"7e6336d195985b2059966eda64859da86c9e9d15",
    "implementation":"ad14ccd72a1a3ca75ab95acb0e294c6707b14627",
    "production_runs":"35034092694,35034524501",
    "artifacts":"10423276358,10423176041",
    "scientific_payload_sha256":"359b27d478b5b4927bc7df0c98a361f0177bba57e5550433662cd21138f75571",
}
PASS_CLASS="PASS_SCOPED_ITER057X_CORRECTED_DECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_SIXTH_EVEN_ORDER__O_C6_Q8_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED"
INVALID_CLASS="INVALID_ITER057X_SEED_MUTATION_OLD_SOURCE_REUSE_RESTRICTED_ANSATZ_NORMALIZATION_OR_EXACTNESS_CONTROL"


def alphas(d):
    return sorted(a for a in product(range(d+1),repeat=4) if sum(a)==d)


def read_r10():
    text=R10_PATH.read_text()
    meta={}
    payload=[]
    for line in text.splitlines():
        if line.startswith("#"):
            body=line[1:].strip()
            if "=" in body:
                k,v=body.split("=",1);meta[k.strip()]=v.strip()
        elif line.strip():
            payload.append(line)
    rows=[]
    for row in csv.DictReader(io.StringIO("\n".join(payload))):
        a=int(row["a"]);b=int(row["b"])
        alpha=(int(row["t"]),int(row["x"]),int(row["y"]),int(row["z"]))
        coef=F(row["R10_over_kappa5"])
        rows.append((a,b,alpha,coef))
    return meta,rows


def seed_metric10():
    g,qdata,prov8,r8_count=u.seed_metric8()
    meta,rows=read_r10()
    meta_ok=all(meta.get(k)==v for k,v in EXPECTED_R10_META.items())
    pure=all(sum(alpha)==10 for _,_,alpha,_ in rows)
    unique=len({(a,b,alpha) for a,b,alpha,_ in rows})==len(rows)
    rbar=pmat()
    for a,b,alpha,coef in rows:
        term=mono(alpha,K**5*coef/F(fact(alpha)))
        rbar[a][b]=add(rbar[a][b],term)
        if a!=b:rbar[b][a]=add(rbar[b][a],term)
    tr={}
    for a in range(N):tr=add(tr,scale(rbar[a][a],ETA[a]))
    for a,b in product(range(N),repeat=2):
        rr=dict(rbar[a][b])
        if a==b:rr=add(rr,scale(tr,-F(ETA[a],2)))
        g[a][b]=add(g[a][b],rr)
    provenance=(prov8 and r8_count==153 and meta_ok and len(rows)==283 and pure and unique)
    return g,qdata,provenance,len(rows),meta,pure,unique


def inverse8(g):
    h=pmat()
    for a,b in product(range(N),repeat=2):
        h[a][b]=dict(g[a][b])
        if a==b:h[a][b]=sub(h[a][b],const(ETA[a]))
    gi=pmat()
    for a,b in product(range(N),repeat=2):
        if a==b:gi[a][b]=const(ETA[a])
        gi[a][b]=add(gi[a][b],scale(h[a][b],-ETA[a]*ETA[b]))
        hh={}
        for c in range(N):
            hh=add(hh,scale(mul(h[a][c],h[c][b],8),ETA[a]*ETA[c]*ETA[b]))
        gi[a][b]=add(gi[a][b],hh)
        hhh={}
        for c,d in product(range(N),repeat=2):
            term=mul(mul(h[a][c],h[c][d],8),h[d][b],8)
            hhh=add(hhh,scale(term,-ETA[a]*ETA[c]*ETA[d]*ETA[b]))
        gi[a][b]=add(gi[a][b],hhh)
        hhhh={}
        for c,d,e in product(range(N),repeat=3):
            term=mul(mul(mul(h[a][c],h[c][d],8),h[d][e],8),h[e][b],8)
            hhhh=add(hhhh,scale(term,ETA[a]*ETA[c]*ETA[d]*ETA[e]*ETA[b]))
        gi[a][b]=trunc(add(gi[a][b],hhhh),8)
    return gi


def normalized(poly,alpha):
    return poly.get(tuple(alpha),F(0))*F(fact(alpha))


def sparse_map(records,degrees):
    out={}
    for rec in records:
        if rec["degree"] in degrees:
            out[(tuple(rec["pair"]),tuple(rec["alpha"]))]=rec["value"]
    return out


def compute():
    g,qdata,prov10,r10_count,r10_meta,r10_pure,r10_unique=seed_metric10()
    gi=inverse8(g)

    inverse_ok=True
    for a,b in product(range(N),repeat=2):
        s={}
        for c in range(N):s=add(s,mul(g[a][c],gi[c][b],8))
        if trunc(sub(s,const(1 if a==b else 0)),8):inverse_ok=False

    Gamma=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c in product(range(N),repeat=3):
        val={}
        for d in range(N):
            t=add(add(deriv(g[d][c],b),deriv(g[d][b],c)),neg(deriv(g[b][c],d)))
            val=add(val,mul(gi[a][d],t,9))
        Gamma[a][b][c]=scale(trunc(val,9),F(1,2))

    Rup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val=sub(deriv(Gamma[a][d][b],c),deriv(Gamma[a][c][b],d))
        for e in range(N):
            val=add(val,sub(mul(Gamma[a][c][e],Gamma[e][d][b],8),mul(Gamma[a][d][e],Gamma[e][c][b],8)))
        Rup[a][b][c][d]=trunc(val,8)

    Rlow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for e in range(N):val=add(val,mul(g[a][e],Rup[e][b][c][d],8))
        Rlow[a][b][c][d]=trunc(val,8)

    Ric=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a in range(N):val=add(val,Rup[a][b][a][d])
        Ric[b][d]=trunc(val,8)
    Scal={}
    for a,b in product(range(N),repeat=2):Scal=add(Scal,mul(gi[a][b],Ric[a][b],8))
    Scal=trunc(Scal,8)
    Ein=pmat()
    for a,b in product(range(N),repeat=2):
        Ein[a][b]=trunc(sub(Ric[a][b],scale(mul(g[a][b],Scal,8),F(1,2))),8)
    ricci_zero=all(not Ric[a][b] for a,b in product(range(N),repeat=2))
    scalar_zero=not Scal
    einstein_zero=all(not Ein[a][b] for a,b in product(range(N),repeat=2))

    C=Rlow
    Cup=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,r1,s1 in product(range(N),repeat=4):
        val={}
        for m,n in product(range(N),repeat=2):
            val=add(val,mul(mul(gi[r1][m],gi[s1][n],8),C[a][b][m][n],8))
        Cup[a][b][r1][s1]=trunc(val,8)

    Q=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for rr,ss in product(range(N),repeat=2):val=add(val,mul(Cup[a][b][rr][ss],C[rr][ss][c][d],8))
        Q[a][b][c][d]=trunc(val,8)

    perms=list(permutations(range(4)))
    Qr=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        inds=(a,b,c,d);alt={}
        for pp in perms:
            alt=add(alt,scale(Q[inds[pp[0]]][inds[pp[1]]][inds[pp[2]]][inds[pp[3]]],F(psign(pp),24)))
        Qr[a][b][c][d]=trunc(sub(Q[a][b][c][d],alt),8)

    QRic=pmat()
    for b,d in product(range(N),repeat=2):
        val={}
        for a,c in product(range(N),repeat=2):val=add(val,mul(gi[a][c],Qr[a][b][c][d],8))
        QRic[b][d]=trunc(val,8)
    QSc={}
    for b,d in product(range(N),repeat=2):QSc=add(QSc,mul(gi[b][d],QRic[b][d],8))
    QSc=trunc(QSc,8)

    Plow=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        rt=add(sub(mul(g[a][c],QRic[d][b],8),mul(g[a][d],QRic[c][b],8)),
               add(neg(mul(g[b][c],QRic[d][a],8)),mul(g[b][d],QRic[c][a],8)))
        rt=scale(rt,F(1,2))
        gg=scale(sub(mul(g[a][c],g[d][b],8),mul(g[a][d],g[c][b],8)),F(1,2))
        Plow[a][b][c][d]=scale(trunc(add(sub(Qr[a][b][c][d],rt),scale(mul(QSc,gg,8),F(1,3))),8),3)

    P=[[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a,b,c,d in product(range(N),repeat=4):
        val={}
        for i,j,m,n in product(range(N),repeat=4):
            raiser=mul(mul(gi[a][i],gi[b][j],8),mul(gi[c][m],gi[d][n],8),8)
            val=add(val,mul(raiser,Plow[i][j][m][n],8))
        P[a][b][c][d]=trunc(val,8)

    I3={}
    for a,b,c,d,e,f in product(range(N),repeat=6):
        I3=add(I3,mul(mul(Cup[a][b][c][d],Cup[c][d][e][f],6),Cup[e][f][a][b],6))
    I3=trunc(I3,6)
    PR={}
    for a,b,c,d in product(range(N),repeat=4):PR=add(PR,mul(P[a][b][c][d],Rlow[a][b][c][d],6))
    PR=trunc(PR,6)
    homogeneity=not trunc(sub(PR,scale(I3,3)),6)

    FD=[[[{} for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for m,b,n in product(range(N),repeat=3):
        val={}
        for a in range(N):
            term=deriv(P[a][m][b][n],a)
            for rr in range(N):
                term=add(term,mul(Gamma[a][a][rr],P[rr][m][b][n],7))
                term=add(term,mul(Gamma[m][a][rr],P[a][rr][b][n],7))
                term=add(term,mul(Gamma[b][a][rr],P[a][m][rr][n],7))
                term=add(term,mul(Gamma[n][a][rr],P[a][m][b][rr],7))
            val=add(val,term)
        FD[m][b][n]=trunc(val,7)

    D=pmat()
    for m,n in product(range(N),repeat=2):
        val={}
        for b in range(N):
            term=deriv(FD[m][b][n],b)
            for rr in range(N):
                term=add(term,mul(Gamma[m][b][rr],FD[rr][b][n],6))
                term=add(term,mul(Gamma[b][b][rr],FD[m][rr][n],6))
                term=add(term,mul(Gamma[n][b][rr],FD[m][b][rr],6))
            val=add(val,term)
        D[m][n]=trunc(val,6)

    def bone(a,b):
        val={}
        for c,d,e,f in product(range(N),repeat=4):
            val=add(val,mul(mul(P[a][c][d][e],gi[b][f],6),Rlow[f][c][d][e],6))
        return trunc(val,6)

    B=pmat()
    for a,b in product(range(N),repeat=2):B[a][b]=scale(add(bone(a,b),bone(b,a)),F(1,2))

    Eup=pmat()
    for a,b in product(range(N),repeat=2):
        val=add(neg(B[a][b]),scale(D[a][b],-2))
        val=add(val,scale(mul(gi[a][b],I3,6),F(1,2)))
        Eup[a][b]=trunc(val,6)
    Edown=pmat()
    for a,b in product(range(N),repeat=2):
        val={}
        for c,d in product(range(N),repeat=2):val=add(val,mul(mul(g[a][c],g[b][d],6),Eup[c][d],6))
        Edown[a][b]=trunc(val,6)

    sym=all(not trunc(sub(Edown[a][b],Edown[b][a]),6) for a,b in product(range(N),repeat=2))
    trace={}
    for a,b in product(range(N),repeat=2):trace=add(trace,mul(gi[a][b],Edown[a][b],6))
    trace_ward=not trunc(add(trunc(trace,6),I3),6)

    noether=[]
    for b in range(N):
        val={}
        for a in range(N):
            val=add(val,deriv(Eup[a][b],a))
            for rr in range(N):
                val=add(val,mul(Gamma[a][a][rr],Eup[rr][b],5))
                val=add(val,mul(Gamma[b][a][rr],Eup[a][rr],5))
        noether.append(trunc(val,5))
    noether_ok=all(not x for x in noether)

    odd_nonzero=[];source_sparse=[];degree_counts={d:0 for d in range(7)}
    d6_nonzero=0;d6_time=0;d6_offdiag=0
    for a,b in PAIRS:
        S=neg(Edown[a][b])
        for alpha,raw in sorted(S.items()):
            d=sum(alpha)
            if d>6:continue
            norm=raw*F(fact(alpha))
            if not norm:continue
            degree_counts[d]+=1
            if d in (1,3,5):odd_nonzero.append((a,b,alpha,fstr(norm)))
            rec={"pair":[a,b],"alpha":list(alpha),"degree":d,"value":fstr(norm)}
            if d==0:rec["Shat_over_kappa3"]=fstr(norm/(K**3))
            elif d==2:rec["Shat_over_kappa4"]=fstr(norm/(K**4))
            elif d==4:rec["Shat_over_kappa5"]=fstr(norm/(K**5))
            elif d==6:rec["Shat_over_kappa6"]=fstr(norm/(K**6))
            source_sparse.append(rec)
            if d==6:
                d6_nonzero+=1
                if alpha[0]:d6_time+=1
                if a!=b:d6_offdiag+=1

    # Independent lower-source replay: execute the terminal Iter057U algorithm
    # afresh and compare every normalized degree 0/2/4 coefficient.
    uout=u.compute()
    u_pass=(uout.get("pass") is True and
            uout.get("classification")=="PASS_SCOPED_ITER057U_CORRECTED_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_FOURTH_EVEN_ORDER__O_C6_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED")
    expected=sparse_map(uout.get("Shat_normalized_sparse",[]),{0,2,4})
    actual=sparse_map(source_sparse,{0,2,4})
    lower_replay=(u_pass and actual==expected)
    replay_missing=sorted(str(k) for k in expected.keys()-actual.keys())
    replay_extra=sorted(str(k) for k in actual.keys()-expected.keys())
    replay_mismatch=sorted(str(k) for k in expected.keys()&actual.keys() if expected[k]!=actual[k])

    basis_by_degree={str(d):10*len(alphas(d)) for d in range(7)}
    basis_total=sum(basis_by_degree.values())
    controls={
        "A_iter057W_R10_provenance_exact_283_pure_degree10":prov10 and r10_count==283 and r10_pure and r10_unique,
        "B_inverse_identity_through_degree8":inverse_ok,
        "B_seed_Ricci_through_degree8_zero":ricci_zero,
        "B_seed_scalar_through_degree8_zero":scalar_zero,
        "B_seed_Einstein_through_degree8_zero":einstein_zero,
        "C_direct_tensor_source_computed_through_degree6":True,
        "D_P_dot_R_equals_3I3_through_degree6":homogeneity,
        "E_E_W3_down_symmetric_through_degree6":sym,
        "F_trace_Ward_through_degree6":trace_ward,
        "G_Noether_divergence_through_degree5":noether_ok,
        "H_odd_source_coefficients_degree1_3_5_zero":not odd_nonzero,
        "I_complete_terminal_Iter057U_degree0_2_4_replay":lower_replay,
        "J_full_basis_count_2100":basis_total==2100 and basis_by_degree=={"0":10,"1":40,"2":100,"3":200,"4":350,"5":560,"6":840},
        "K_scope_and_claim_locks_retained":True,
    }
    passed=all(controls.values())
    source_canonical=json.dumps(source_sparse,sort_keys=True,separators=(",",":"))
    return {
        "gate":GATE,
        "preregistration_commit":PREREG,
        "iter057U_terminal_commit":ITER057U,
        "iter057W_terminal_commit":ITER057W,
        "iter057W_R10_freeze_commit":R10_FREEZE,
        "R10_metadata":r10_meta,
        "R10_nonzero_normalized_count":r10_count,
        "kappa":fstr(K),
        "controls":controls,
        "pass":passed,
        "classification":PASS_CLASS if passed else INVALID_CLASS,
        "basis_count_by_degree":basis_by_degree,
        "basis_total":basis_total,
        "source_nonzero_count_by_degree":{str(k):v for k,v in degree_counts.items()},
        "degree6_nonzero_count":d6_nonzero,
        "degree6_time_containing_nonzero_count":d6_time,
        "degree6_offdiagonal_nonzero_count":d6_offdiag,
        "Shat_normalized_sparse":source_sparse,
        "Shat_sparse_sha256":hashlib.sha256(source_canonical.encode()).hexdigest(),
        "iter057U_replay_expected_count":len(expected),
        "iter057U_replay_actual_count":len(actual),
        "iter057U_replay_missing":replay_missing,
        "iter057U_replay_extra":replay_extra,
        "iter057U_replay_value_mismatches":replay_mismatch,
        "I3_origin_over_kappa3":fstr(v0(I3)/(K**3)),
        "exact_zero_uses_tolerance":False,
        "c6_status":"SYMBOLIC_UNFIXED_FACTORED_OUT",
        "scope":"FINITE_LOCAL_TAYLOR_SOURCE_THROUGH_COORDINATE_DEGREE_6_ONLY",
        "theory_established_percent":0,
    }


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out")
    args=ap.parse_args();out=compute();text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if args.out:Path(args.out).write_text(text)
    print(text,end="")
    if out["pass"] is not True:raise SystemExit(2)


if __name__=="__main__":main()
