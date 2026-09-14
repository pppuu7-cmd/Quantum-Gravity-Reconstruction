#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sympy as sp
import qgr_iter054c_local_metric_principal_symbol_retry as retry

core = retry.core
retry.core.k_panel = retry.corrected_k_panel

GATE = "ITER054D-WEYL3-PRINCIPAL-ORDER-GAUGE-FIXING-CHARACTERISTIC-AUDIT"
PASS_CLASS = "PASS_SCOPED_ITER054D_WEYL3_PRINCIPAL_ORDER_GAUGE_COMPLETION_QUOTIENT_INVARIANCE_HYPERBOLICITY_NOT_AUTHORIZED"
PREREG = "b3d758c25449027d23a5879c3df135c4903c37d4"
ETA = core.ETA
ALPHAS = [sp.Integer(1), sp.Rational(7,3)]
LAM = sp.Rational(3,2)
NULL_K = [
    [sp.Integer(1),sp.Integer(1),sp.Integer(0),sp.Integer(0)],
    [sp.Integer(5),sp.Integer(3),sp.Integer(4),sp.Integer(0)],
]


def k2(k):
    return sp.simplify(sum(ETA[a,b]*k[a]*k[b] for a in range(4) for b in range(4)))


def vec_h(h):
    return sp.Matrix([h[a,b] for a,b in core.SYM_BASIS])


def gauge_matrix(k, trace_coeff=sp.Rational(1,2)):
    kup = [sum(ETA[nu,r]*k[r] for r in range(4)) for nu in range(4)]
    D = sp.zeros(4,10)
    for j in range(10):
        h = core.symmetric_h(j)
        tr = sp.simplify(sum(ETA[r,s]*h[r,s] for r in range(4) for s in range(4)))
        for mu in range(4):
            D[mu,j] = sp.simplify(sum(kup[nu]*h[mu,nu] for nu in range(4)) - trace_coeff*k[mu]*tr)
    return D


def pure_gauge_columns(k):
    K = sp.zeros(10,4)
    for r in range(4):
        xi = [sp.Integer(1) if i==r else sp.Integer(0) for i in range(4)]
        h = sp.zeros(4)
        for a in range(4):
            for b in range(4):
                h[a,b] = sp.expand(k[a]*xi[b] + k[b]*xi[a])
        K[:,r] = vec_h(h)
    return K


def completion(k, alpha, bad=False):
    D = gauge_matrix(k, sp.Rational(1,3) if bad else sp.Rational(1,2))
    return sp.simplify(alpha*k2(k)) * D.T * ETA * D


def null_basis_matrix(D):
    ns = D.nullspace()
    return sp.Matrix.hstack(*ns) if ns else sp.zeros(D.cols,0)


def stream_a0():
    rows=[]; ok=True; bad_detected=False
    for i,k in enumerate(core.k_panel()):
        D=gauge_matrix(k)
        Ds=gauge_matrix([LAM*x for x in k])
        homog_D=(Ds-LAM*D)==sp.zeros(4,10)
        K=pure_gauge_columns(k)
        expected=sp.simplify(k2(k))*sp.eye(4)
        gauge_identity=(D*K-expected)==sp.zeros(4)
        rank4=(D*K).rank()==4
        gscale=True
        for alpha in ALPHAS:
            G=completion(k,alpha)
            Gs=completion([LAM*x for x in k],alpha)
            gscale = gscale and ((Gs-LAM**4*G)==sp.zeros(10))
        Dbad=gauge_matrix(k,sp.Rational(1,3))
        bad=(Dbad*K-expected)!=sp.zeros(4)
        bad_detected = bad_detected or bad
        row={"k":i,"nonnull":bool(k2(k)!=0),"D_k1_homogeneity":bool(homog_D),"gauge_identity_exact":bool(gauge_identity),"gauge_rank4":bool(rank4),"G_k4_homogeneity":bool(gscale),"negative_control_detected":bool(bad)}
        rows.append(row)
        ok = ok and all(row[x] for x in ["nonnull","D_k1_homogeneity","gauge_identity_exact","gauge_rank4","G_k4_homogeneity"])
    ok = ok and bad_detected
    return {"stream":"A0","gate":GATE,"pass":bool(ok),"controls_valid":True,"samples":rows,
            "interpretation":"exact fourth-order principal gauge-functional algebra only"}


def stream_a1():
    rows=[]; ok=True; bad_any=False
    for seed in range(12):
        W=core.background_operator(seed)
        for ki,k in enumerate(core.k_panel()):
            Q,_=core.q_matrix(W,k)
            D=gauge_matrix(k)
            K=pure_gauge_columns(k)
            N=null_basis_matrix(D)
            qgauge=(Q*K)==sp.zeros(10,4)
            quotient=sp.simplify(N.T*Q*N)
            rankQ=Q.rank()
            alpha_rows=[]
            alpha_quot=[]
            case_ok=qgauge and N.cols==6
            for alpha in ALPHAS:
                Qa=sp.simplify(Q+completion(k,alpha))
                lifted=(Qa*K).rank()==4
                rank_increment=(Qa.rank()==rankQ+4)
                qinv=(sp.simplify(N.T*Qa*N-quotient)==sp.zeros(N.cols))
                alpha_rows.append({"alpha":str(alpha),"gauge_lift_rank4":bool(lifted),"rank_increment4":bool(rank_increment),"quotient_invariant":bool(qinv),"rank_Q":int(rankQ),"rank_Qa":int(Qa.rank())})
                alpha_quot.append(sp.simplify(N.T*Qa*N))
                case_ok = case_ok and lifted and rank_increment and qinv
            cross=(alpha_quot[0]-alpha_quot[1])==sp.zeros(N.cols)
            Gbad=completion(k,sp.Integer(1),bad=True)
            badq=(sp.simplify(N.T*Gbad*N)!=sp.zeros(N.cols))
            bad_any=bad_any or badq
            case_ok=case_ok and cross and badq
            rows.append({"seed":seed,"k":ki,"Q_gauge_null_exact":bool(qgauge),"quotient_dim6":bool(N.cols==6),"alpha_tests":alpha_rows,"cross_alpha_quotient_exact":bool(cross),"bad_completion_detected":bool(badq),"pass":bool(case_ok)})
            ok = ok and case_ok
    ok = ok and bad_any and len(rows)==48
    return {"stream":"A1","gate":GATE,"pass":bool(ok),"controls_valid":True,"case_count":len(rows),"cases":rows,
            "interpretation":"finite exact gauge-null lifting and quotient-invariance certificate"}


def stream_b0():
    rows=[]; ok=True
    for ni,k in enumerate(NULL_K):
        null_exact=(k2(k)==0)
        for alpha in ALPHAS:
            gzero=(completion(k,alpha)==sp.zeros(10))
            ok = ok and null_exact and gzero
        ranks=[]
        for seed in range(12):
            W=core.background_operator(seed)
            Q,_=core.q_matrix(W,k)
            ranks.append({"seed":seed,"rank":int(Q.rank()),"nullity":int(10-Q.rank())})
        rows.append({"null_k":ni,"k2_exact_zero":bool(null_exact),"completion_zero_both_alpha":bool(all(completion(k,a)==sp.zeros(10) for a in ALPHAS)),"correction_symbol_ranks_diagnostic_only":ranks})
    return {"stream":"B0","gate":GATE,"pass":bool(ok),"controls_valid":True,"null_covector_diagnostics":rows,
            "full_system_characteristic_claim_authorized":False,
            "interpretation":"null-covector diagnostic retained; correction-only rank is not a full-system characteristic theorem"}


def stream_b1():
    missing=[
        "full_gauge_fixed_mixed_order_einstein_plus_weyl3_principal_system",
        "full_system_characteristic_polynomial",
        "open_region_real_characteristic_audit",
        "strong_hyperbolicity_diagonalizability_or_symmetrizer",
        "gauge_constraint_propagation",
        "energy_estimate",
        "physical_mode_residue_ghost_interpretation",
    ]
    cls="PRINCIPAL_ORDER_GAUGE_COMPLETION_FINITE_EXACT_QUOTIENT_CERTIFICATE_HYPERBOLICITY_NOT_YET_AUTHORIZED"
    return {"stream":"B1","gate":GATE,"pass":True,"controls_valid":True,"actual_classification":cls,"missing_obligations":missing,
            "strong_hyperbolicity_authorized":False,"well_posedness_authorized":False,"physical_spectrum_authorized":False,
            "interpretation":"fail-closed authority boundary after finite exact gauge-completion audit"}


def run_stream(s):
    return {"A0":stream_a0,"A1":stream_a1,"B0":stream_b0,"B1":stream_b1}[s]()


def aggregate(inp):
    rows=[]; errors=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try: rows.append(json.loads(p.read_text()))
        except Exception as e: errors.append(f"{p}:{e}")
    by={r.get('stream'):r for r in rows if r.get('stream') in {'A0','A1','B0','B1'}}
    missing=sorted({'A0','A1','B0','B1'}-set(by))
    allpass=not missing and not errors and all(by[s].get('pass') is True and by[s].get('controls_valid') is True for s in ['A0','A1','B0','B1'])
    return {"gate":GATE,"classification":PASS_CLASS if allpass else "SCIENTIFIC_FAIL_OR_INVALID_ITER054D","pass":allpass,
            "found_streams":sorted(by),"missing":missing,"parse_errors":errors,"stream_pass":{s:by[s].get('pass') for s in by},
            "preregistration_commit":PREREG,
            "interpretation_lock":"FINITE EXACT FOURTH-ORDER PRINCIPAL GAUGE-COMPLETION/QUOTIENT CERTIFICATE ONLY; NULL-COVECTOR RANKS DIAGNOSTIC; FULL MIXED-ORDER CHARACTERISTICS/STRONG HYPERBOLICITY/ENERGY/CONSTRAINT PROPAGATION/PHYSICAL SPECTRUM NOT ESTABLISHED; C6 UNFIXED; THEORY_ESTABLISHED_0"}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A0','A1','B0','B1']); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True)
    a=ap.parse_args(); data=aggregate(a.aggregate) if a.aggregate else run_stream(a.stream)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(data,indent=2,sort_keys=True)); print(json.dumps(data,sort_keys=True))
    if not data.get('pass',False): raise SystemExit(2)

if __name__=='__main__': main()
