#!/usr/bin/env python3
import argparse, json, itertools
from pathlib import Path
import sympy as sp

GATE = "ITER054C-WEYL3-LOCAL-METRIC-PRINCIPAL-SYMBOL-AND-GAUGE-DEGENERACY"
PASS_CLASS = "PASS_SCOPED_ITER054C_WEYL3_LOCAL_METRIC_PRINCIPAL_SYMBOL_GAUGE_DEGENERACY_CONFIRMED_HYPERBOLICITY_NOT_AUTHORIZED"
PREREG = "3bc563b2aa0c691a78b57c4e7c53fd0ad9a51ba3"
ETA = sp.diag(-1, 1, 1, 1)
PAIRS = [(0,1),(0,2),(0,3),(2,3),(3,1),(1,2)]
SYM_BASIS = [(a,b) for a in range(4) for b in range(a,4)]


def symmetric_h(idx):
    a,b = SYM_BASIS[idx]
    h = sp.zeros(4)
    h[a,b] = 1
    h[b,a] = 1
    if a == b:
        h[a,b] = 1
    return h


def riemann_principal(k, h, corrupted=False):
    R = {}
    for a,b,c,d in itertools.product(range(4), repeat=4):
        if not corrupted:
            v = sp.Rational(1,2)*(k[c]*k[b]*h[a,d] + k[d]*k[a]*h[b,c] - k[d]*k[b]*h[a,c] - k[c]*k[a]*h[b,d])
        else:
            v = sp.Rational(1,2)*(k[c]*k[b]*h[a,d] + k[d]*k[a]*h[b,c] + k[d]*k[b]*h[a,c] - k[c]*k[a]*h[b,d])
        R[a,b,c,d] = sp.simplify(v)
    return R


def weyl_principal_tensor(k, h, corrupted=False):
    R = riemann_principal(k, h, corrupted)
    Ric = {}
    for b,d in itertools.product(range(4), repeat=2):
        Ric[b,d] = sp.simplify(sum(ETA[a,c]*R[a,b,c,d] for a in range(4) for c in range(4)))
    scal = sp.simplify(sum(ETA[b,d]*Ric[b,d] for b in range(4) for d in range(4)))
    C = {}
    for a,b,c,d in itertools.product(range(4), repeat=4):
        C[a,b,c,d] = sp.simplify(
            R[a,b,c,d]
            - sp.Rational(1,2)*(ETA[a,c]*Ric[d,b] - ETA[a,d]*Ric[c,b] - ETA[b,c]*Ric[d,a] + ETA[b,d]*Ric[c,a])
            + sp.Rational(1,6)*scal*(ETA[a,c]*ETA[d,b] - ETA[a,d]*ETA[c,b])
        )
    return C, R


def tensor_to_bivector_operator(C):
    M = sp.zeros(6)
    for p,(a,b) in enumerate(PAIRS):
        for q,(c,d) in enumerate(PAIRS):
            M[p,q] = sp.simplify(sum(ETA[c,e]*ETA[d,f]*C[a,b,e,f] for e in range(4) for f in range(4)))
    return M


def metric_to_weyl_operator(k, h):
    C,_ = weyl_principal_tensor(k,h)
    return tensor_to_bivector_operator(C)


def e_background(seed):
    a = sp.Rational(seed + 2, seed + 5)
    b = sp.Rational(2*seed + 3, seed + 7)
    c = sp.Rational(seed + 1, seed + 9)
    d = sp.Rational(seed + 4, seed + 11)
    e = sp.Rational(2*seed + 5, seed + 13)
    E = sp.Matrix([[a,c,d],[c,b,e],[d,e,-a-b]])
    return E


def background_weyl_tensor(E):
    C = {(a,b,c,d): sp.Integer(0) for a,b,c,d in itertools.product(range(4), repeat=4)}
    def setcomp(a,b,c,d,v):
        entries = [
            (a,b,c,d,1),(b,a,c,d,-1),(a,b,d,c,-1),(b,a,d,c,1),
            (c,d,a,b,1),(d,c,a,b,-1),(c,d,b,a,-1),(d,c,b,a,1)
        ]
        for aa,bb,cc,dd,s in entries:
            C[aa,bb,cc,dd] = sp.simplify(s*v)
    for i in range(1,4):
        for j in range(1,4):
            setcomp(0,i,0,j,E[i-1,j-1])
    eps = sp.LeviCivita
    for i,j,k,l in itertools.product(range(1,4), repeat=4):
        v = -sum(eps(i-1,j-1,m)*eps(k-1,l-1,n)*E[m,n] for m in range(3) for n in range(3))
        if v != 0:
            setcomp(i,j,k,l,sp.simplify(v))
    return C


def background_operator(seed):
    return tensor_to_bivector_operator(background_weyl_tensor(e_background(seed)))


def hessian_bilinear(W,H,K):
    return sp.expand(3*sp.trace(W*(H*K + K*H)))


def q_matrix(W,k):
    maps = [metric_to_weyl_operator(k, symmetric_h(i)) for i in range(10)]
    Q = sp.zeros(10)
    for i in range(10):
        for j in range(i,10):
            v = sp.simplify(hessian_bilinear(W,maps[i],maps[j]))
            Q[i,j] = v
            Q[j,i] = v
    return Q, maps


def k_panel():
    return [
        [sp.Integer(2),sp.Integer(1),sp.Integer(3),sp.Integer(1)],
        [sp.Integer(3),sp.Integer(2),sp.Integer(1),sp.Integer(2)],
        [sp.Integer(4),sp.Integer(1),sp.Integer(2),sp.Integer(3)],
        [sp.Integer(5),sp.Integer(2),sp.Integer(3),sp.Integer(1)],
    ]


def is_nonnull(k):
    return sp.simplify(sum(ETA[a,b]*k[a]*k[b] for a in range(4) for b in range(4))) != 0


def tensor_identity_residuals(C):
    vals=[]
    for a,b,c,d in itertools.product(range(4), repeat=4):
        vals.append(sp.simplify(C[a,b,c,d] + C[b,a,c,d]))
        vals.append(sp.simplify(C[a,b,c,d] + C[a,b,d,c]))
        vals.append(sp.simplify(C[a,b,c,d] - C[c,d,a,b]))
        vals.append(sp.simplify(C[a,b,c,d] + C[a,c,d,b] + C[a,d,b,c]))
    for b,d in itertools.product(range(4), repeat=2):
        vals.append(sp.simplify(sum(ETA[a,c]*C[a,b,c,d] for a in range(4) for c in range(4))))
    return vals


def stream_a0():
    probes=[]
    lam=sp.Rational(7,5)
    bad_nonzero=False
    for idx,k in enumerate(k_panel()):
        h=symmetric_h((idx*3+2)%10)
        C,_=weyl_principal_tensor(k,h)
        good=all(v==0 for v in tensor_identity_residuals(C))
        Cop=metric_to_weyl_operator(k,h)
        Cop2=metric_to_weyl_operator([lam*x for x in k],h)
        homog=(Cop2-lam**2*Cop)==sp.zeros(6)
        Cbad,_=weyl_principal_tensor(k,h,corrupted=True)
        bad=any(v!=0 for v in tensor_identity_residuals(Cbad))
        bad_nonzero = bad_nonzero or bad
        probes.append({"i":idx,"identities_exact":bool(good),"k2_homogeneity":bool(homog),"negative_control_detected":bool(bad)})
    ok=all(p["identities_exact"] and p["k2_homogeneity"] for p in probes) and bad_nonzero and all(is_nonnull(k) for k in k_panel())
    return {"stream":"A0","gate":GATE,"pass":bool(ok),"controls_valid":True,"probes":probes,
            "interpretation":"exact local metric-to-Weyl principal map only"}


def stream_a1():
    lam=sp.Rational(3,2)
    rows=[]
    all_ok=True
    for seed in range(12):
        W=background_operator(seed)
        for ki,k in enumerate(k_panel()):
            Q,_=q_matrix(W,k)
            Qs,_=q_matrix(W,[lam*x for x in k])
            Q0,_=q_matrix(sp.zeros(6),k)
            sym=(Q-Q.T)==sp.zeros(10)
            scale=(Qs-lam**4*Q)==sp.zeros(10)
            flat=(Q0==sp.zeros(10))
            nz=(Q!=sp.zeros(10))
            i=(seed+ki)%10; j=(seed+2*ki+3)%10
            H=metric_to_weyl_operator(k,symmetric_h(i)); K=metric_to_weyl_operator(k,symmetric_h(j))
            s,t=sp.symbols('s t')
            direct=sp.expand(sp.trace((W+s*H+t*K)**3)).coeff(s,1).coeff(t,1)
            composed=hessian_bilinear(W,H,K)
            held=(sp.simplify(direct-composed)==0)
            row={"seed":seed,"k":ki,"symmetric":bool(sym),"k4_scaling":bool(scale),"flat_zero":bool(flat),"active_nonzero":bool(nz),"heldout_exact":bool(held)}
            rows.append(row)
            all_ok = all_ok and all(row[x] for x in ["symmetric","k4_scaling","flat_zero","active_nonzero","heldout_exact"])
    return {"stream":"A1","gate":GATE,"pass":bool(all_ok),"controls_valid":True,"case_count":len(rows),"cases":rows,
            "interpretation":"finite exact local fourth-order correction symbol panel"}


def stream_b0():
    rows=[]; ok=True
    xis=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    for seed in range(12):
        W=background_operator(seed)
        k=k_panel()[seed%4]
        Q,maps=q_matrix(W,k)
        gauge_ok=True
        for xi in xis:
            h=sp.zeros(4)
            for a in range(4):
                for b in range(4):
                    h[a,b]=k[a]*xi[b]+k[b]*xi[a]
            M=metric_to_weyl_operator(k,h)
            gauge_ok = gauge_ok and (M==sp.zeros(6))
        nongauge=symmetric_h((seed+4)%10)
        Mng=metric_to_weyl_operator(k,nongauge)
        nontriv=(Mng!=sp.zeros(6)) and any(hessian_bilinear(W,Mng,M)!=0 for M in maps)
        rows.append({"seed":seed,"four_gauge_nulls_exact":bool(gauge_ok),"nongauge_nontrivial":bool(nontriv)})
        ok = ok and gauge_ok and nontriv
    return {"stream":"B0","gate":GATE,"pass":bool(ok),"controls_valid":True,"samples":rows,
            "interpretation":"diffeomorphism principal degeneracy retained exactly"}


def stream_b1():
    cls="LOCAL_METRIC_PRINCIPAL_SYMBOL_CONSTRUCTED_GAUGE_DEGENERACY_CONFIRMED_HYPERBOLICITY_NOT_AUTHORIZED"
    missing=["justified_principal_order_gauge_fixing","characteristic_real_root_audit","strong_hyperbolicity_or_equivalent_estimate","constraint_gauge_propagation","energy_estimate_and_physical_mode_interpretation"]
    return {"stream":"B1","gate":GATE,"pass":True,"controls_valid":True,"actual_classification":cls,"missing_obligations":missing,
            "ordinary_second_order_de_donder_sufficient_for_fourth_order_hyperbolicity":False,
            "interpretation":"fail-closed authority boundary; no hyperbolicity or physical spectrum claim"}


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
    return {"gate":GATE,"classification":PASS_CLASS if allpass else "SCIENTIFIC_FAIL_OR_INVALID_ITER054C","pass":allpass,
            "found_streams":sorted(by),"missing":missing,"parse_errors":errors,"stream_pass":{s:by[s].get('pass') for s in by},
            "preregistration_commit":PREREG,
            "interpretation_lock":"LOCAL FINITE EXACT WEYL3 METRIC PRINCIPAL-SYMBOL CERTIFICATE ONLY; DIFFEOMORPHISM GAUGE DEGENERACY RETAINED; JUSTIFIED PRINCIPAL-ORDER GAUGE FIXING/HYPERBOLICITY/WELL-POSEDNESS NOT ESTABLISHED; NO PHYSICAL MODE/GHOST/STABILITY CLAIM; C6 UNFIXED; THEORY_ESTABLISHED_0"}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A0','A1','B0','B1']); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True)
    a=ap.parse_args(); data=aggregate(a.aggregate) if a.aggregate else run_stream(a.stream)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(data,indent=2,sort_keys=True)); print(json.dumps(data,sort_keys=True))
    if not data.get('pass',False): raise SystemExit(2)

if __name__=='__main__': main()
