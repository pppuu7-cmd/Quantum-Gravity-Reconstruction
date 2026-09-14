#!/usr/bin/env python3
import argparse, json, os
from pathlib import Path
import sympy as sp

GATE = "ITER054A-WEYL3-DERIVATIVE-ORDER-AND-REGIME-SEPARATION"
PASS_CLASS = "PASS_SCOPED_ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION"
PREREG = "6164dd1bbbdea45c0599334f3df5b5e66ac19121"


def euler_lagrange(L, q, t, max_order):
    out = sp.diff(L, q)
    for k in range(1, max_order + 1):
        qk = sp.diff(q, t, k)
        out += (-1)**k * sp.diff(sp.diff(L, qk), t, k)
    return sp.expand(out)


def highest_q_derivative(expr, q, t):
    m = 0
    for d in expr.atoms(sp.Derivative):
        if d.expr == q and all(v == t for v in d.variables):
            m = max(m, len(d.variables))
    return m


def stream_a0():
    t = sp.symbols('t')
    q = sp.Function('q')(t)
    q2 = sp.diff(q, t, 2)
    q3 = sp.diff(q, t, 3)
    L = q2**3
    EL = euler_lagrange(L, q, t, 2)
    coeff_q4 = sp.expand(EL).coeff(sp.diff(q,t,4))
    Lneg = q3**2
    ELneg = euler_lagrange(Lneg, q, t, 3)
    order = highest_q_derivative(EL, q, t)
    neg_order = highest_q_derivative(ELneg, q, t)
    ok = order == 4 and sp.simplify(coeff_q4) != 0 and neg_order == 6
    return {
        "stream":"A0", "gate":GATE, "pass":bool(ok),
        "primary_EL":str(sp.factor(EL)), "primary_order":order,
        "q4_coefficient":str(sp.factor(coeff_q4)),
        "negative_control_EL":str(sp.factor(ELneg)), "negative_control_order":neg_order,
        "controls_valid": True,
        "interpretation":"jet-order structural audit only"
    }


def cubic_F(i, r1, r2, r3):
    # Fixed exact-rational coefficient family, frozen by prereg/implementation.
    a = sp.Rational(i+1, i+2)
    b = sp.Rational(i+2, i+3)
    c = sp.Rational(i+3, i+4)
    d = sp.Rational(2*i+1, i+5)
    e = sp.Rational(i+4, 2*i+5)
    return sp.expand(a*r1**3 + b*r2**3 + c*r3**3 + d*r1*r2*r3 + e*r1**2*r2 + sp.Rational(1, i+2)*r2**2*r3)


def component_maps(i, q0, q1, q2):
    vals=[]
    for j in range(3):
        a=sp.Rational((i+1)*(j+2)+1, i+j+3)
        b=sp.Rational(i+j+2, 2*i+j+5)
        c=sp.Rational(j+1, i+j+4)
        vals.append(sp.expand(a*q2+b*q1+c*q0))
    return vals


def stream_a1():
    t=sp.symbols('t'); q=sp.Function('q')(t)
    q0=q; q1=sp.diff(q,t); q2=sp.diff(q,t,2); q4=sp.diff(q,t,4)
    samples=[]; nonzero=0; max_order=0
    for i in range(12):
        r1,r2,r3=component_maps(i,q0,q1,q2)
        L=cubic_F(i,r1,r2,r3)
        EL=euler_lagrange(L,q,t,2)
        order=highest_q_derivative(EL,q,t)
        coeff=sp.simplify(sp.expand(EL).coeff(q4))
        nz=coeff != 0
        nonzero += int(nz); max_order=max(max_order,order)
        samples.append({"i":i,"order":order,"q4_nonzero":bool(nz),"q4_coeff_ops":int(sp.count_ops(coeff))})
    ok=max_order <= 4 and nonzero >= 10
    return {"stream":"A1","gate":GATE,"pass":bool(ok),"samples":samples,
            "sample_count":12,"nonzero_q4_count":nonzero,"max_derivative_order":max_order,
            "controls_valid":True}


def stream_b0():
    t,eta,R=sp.symbols('t eta R')
    v=sp.Function('v')(t)
    # exact EL for L=(q'')^3 is 6[(q''')^2+q''q''''].
    q2=R + eta*sp.diff(v,t,2)
    q3=eta*sp.diff(v,t,3)
    q4=eta*sp.diff(v,t,4)
    EL=6*(q3**2 + q2*q4)
    lin=sp.expand(sp.diff(EL,eta).subs(eta,0))
    coeff_v4=sp.simplify(lin.coeff(sp.diff(v,t,4)))
    zero_bg=sp.simplify(coeff_v4.subs(R,0))
    nonzero_bg=sp.simplify(coeff_v4.subs(R,sp.Rational(3,7)))
    ok=sp.simplify(coeff_v4-6*R)==0 and zero_bg==0 and nonzero_bg!=0
    return {"stream":"B0","gate":GATE,"pass":bool(ok),"linearized_EL":str(sp.factor(lin)),
            "v4_coefficient":str(coeff_v4),"zero_curvature_control":str(zero_bg),
            "nonzero_background_control":str(nonzero_bg),"controls_valid":True,
            "interpretation":"background activation only; no global tensor claim"}


def stream_b1():
    z,eps,a0,a1=sp.symbols('z eps a0 a1', nonzero=True)
    P=sp.expand(z*(a0+eps*a1*z))
    roots=[sp.Integer(0), -a0/(eps*a1)]
    singular=sp.limit(abs(roots[1]), eps, 0, dir='+') == sp.oo
    # Analytic GR-connected branch test through N=4: exact coefficients vanish recursively.
    cs=sp.symbols('c0:5')
    series=sum(cs[n]*eps**n for n in range(5))
    expanded=sp.series((series*(a0+eps*a1*series)),eps,0,5).removeO().expand()
    equations=[sp.expand(expanded).coeff(eps,n) for n in range(5)]
    sol=sp.solve(equations,cs,dict=True)
    zero_branch=any(all(s.get(c,0)==0 for c in cs) for s in sol)
    # a1=0 control: polynomial reduces to a0*z, only z=0.
    control=sp.expand(P.subs(a1,0))
    ok=(sp.simplify(P.subs(z,roots[0]))==0 and sp.simplify(P.subs(z,roots[1]))==0 and singular and zero_branch and control==a0*z)
    return {"stream":"B1","gate":GATE,"pass":bool(ok),"polynomial":str(P),
            "roots":[str(r) for r in roots],"extra_root_singular_eps0":bool(singular),
            "analytic_GR_branch_zero_through_order":4,"analytic_solution_count":len(sol),
            "a1_zero_control":str(control),"controls_valid":True,
            "interpretation":"regime separation only; no physical residue/norm/ghost claim"}


def run_stream(s):
    return {"A0":stream_a0,"A1":stream_a1,"B0":stream_b0,"B1":stream_b1}[s]()


def aggregate(inp):
    rows=[]; errors=[]
    for p in sorted(Path(inp).rglob('*.json')):
        try: rows.append(json.loads(p.read_text()))
        except Exception as e: errors.append(f"{p}:{e}")
    by={r.get('stream'):r for r in rows if r.get('stream') in {'A0','A1','B0','B1'}}
    missing=sorted({'A0','A1','B0','B1'}-set(by))
    allpass=(not missing and not errors and all(by[s].get('pass') is True and by[s].get('controls_valid') is True for s in ['A0','A1','B0','B1']))
    return {"gate":GATE,"classification":PASS_CLASS if allpass else "SCIENTIFIC_FAIL_OR_INVALID_ITER054A",
            "pass":allpass,"found_streams":sorted(by),"missing":missing,"parse_errors":errors,
            "stream_pass":{s:by[s].get('pass') for s in by},
            "interpretation_lock":"DERIVATIVE-ORDER/REGIME BOOKKEEPING ONLY; NO PHYSICAL MODE/GHOST/STABILITY CLAIM; C6 UNFIXED; THEORY_ESTABLISHED_0",
            "preregistration_commit":PREREG}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['A0','A1','B0','B1']); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True)
    a=ap.parse_args(); data=aggregate(a.aggregate) if a.aggregate else run_stream(a.stream)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(data,indent=2,sort_keys=True))
    print(json.dumps(data,sort_keys=True))
    if not data.get('pass',False): raise SystemExit(2)
if __name__=='__main__': main()
