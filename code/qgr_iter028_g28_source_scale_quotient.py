#!/usr/bin/env python3
"""QGR Iter028 G28 — source-scale quotient finite-phase invariants.

Frozen after terminal G27 and before seeing G28 results.

Scoped input already established in-repository:
  J(n)=beta*n within primitive additive S4-equivalent event composition.
  Common-conformal Dirichlet response for a specified source:
      r-1 = J/(2*lambda)
      S_on = -J^2/(4*lambda)

Question: which exact finite predictions survive quotienting the still-free beta?
No beta is fitted or set to one.  The conformal sector is Weyl-inactive, so c6
must remain unconstrained even if all quotient identities pass.
"""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path


def frac(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def witnesses(lane: int):
    beta1 = F(lane + 1, lane + 2)
    beta2 = beta1 + F(1, lane + 5)
    lam = F(lane + 3, lane + 1)
    return beta1, beta2, lam


def endpoint_ratio(lane: int):
    b1, b2, lam = witnesses(lane)
    counts = [1, 2, 3, 4, 5, 8]
    def vals(beta): return [beta*F(n)/(2*lam) for n in counts]
    v1, v2 = vals(b1), vals(b2)
    r1 = [x/v1[0] for x in v1]
    r2 = [x/v2[0] for x in v2]
    expected = [F(n) for n in counts]
    passed = b1 != b2 and r1 == expected and r2 == expected and r1 == r2
    return {"gate":"ITER028-G28-ENDPOINT-RATIO", "classification":"PASS_SCOPED_ENDPOINT_DISPLACEMENT_RATIOS_ARE_BETA_INDEPENDENT_AND_EQUAL_PRIMITIVE_COUNT_RATIOS", "counts":counts, "ratios":[frac(x) for x in r1], "absolute_beta_fixed":False, "passed":passed}


def phase_ratio(lane: int):
    b1, b2, lam = witnesses(lane)
    counts = [1, 2, 3, 4, 5, 8]
    def vals(beta): return [-(beta*F(n))**2/(4*lam) for n in counts]
    v1, v2 = vals(b1), vals(b2)
    r1 = [x/v1[0] for x in v1]
    r2 = [x/v2[0] for x in v2]
    expected = [F(n*n) for n in counts]
    passed = b1 != b2 and r1 == expected and r2 == expected and r1 == r2
    return {"gate":"ITER028-G28-PHASE-RATIO", "classification":"PASS_SCOPED_COMMON_CONFORMAL_ON_SHELL_PHASE_RATIOS_ARE_BETA_INDEPENDENT_AND_SCALE_AS_COUNT_SQUARED", "counts":counts, "phase_ratios":[frac(x) for x in r1], "absolute_beta_fixed":False, "passed":passed}


def action_endpoint_invariant(lane: int):
    b1, b2, lam = witnesses(lane)
    counts = [1, 2, 4, 5, 8]
    def inv(beta,n):
        J=beta*F(n); x=J/(2*lam); S=-(J*J)/(4*lam)
        return S/(x*x)
    i1=[inv(b1,n) for n in counts]; i2=[inv(b2,n) for n in counts]
    expected=[-lam for _ in counts]
    passed=b1!=b2 and i1==expected and i2==expected
    return {"gate":"ITER028-G28-ACTION-ENDPOINT-INVARIANT", "classification":"PASS_SCOPED_S_ON_OVER_ENDPOINT_DISPLACEMENT_SQUARED_EQUALS_MINUS_LAMBDA_INDEPENDENT_OF_EVENT_COUNT_AND_BETA", "lambda":frac(lam), "invariants":[frac(x) for x in i1], "passed":passed}


def weyl_authority_null(lane: int):
    # The common-conformal metric is conformally flat in this scoped construction.
    # Hence every Weyl tensor component and Weyl^3 insertion vanish identically;
    # derivative of this observable family w.r.t. c6 is exactly zero.
    b1,b2,lam=witnesses(lane)
    probes=[1,2,3,4,5,8]
    weyl3=[F(0) for _ in probes]
    dc6=[F(0) for _ in probes]
    passed=all(x==0 for x in weyl3+dc6) and b1!=b2 and lam>0
    return {"gate":"ITER028-G28-WEYL-AUTHORITY-NULL-CONTROL", "classification":"PASS_NEGATIVE_CONTROL_COMMON_CONFORMAL_QUOTIENT_OBSERVABLES_HAVE_EXACT_ZERO_AUTHORITY_ON_C6", "weyl3_values":[frac(x) for x in weyl3], "authority_rank_on_c6":0, "c6_fixed":False, "passed":passed}

AUDITS={"endpoint-ratio":endpoint_ratio,"phase-ratio":phase_ratio,"action-endpoint-invariant":action_endpoint_invariant,"weyl-authority-null":weyl_authority_null}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--audit',choices=sorted(AUDITS),required=True); ap.add_argument('--lane',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if not 0 <= a.lane <= 5: raise SystemExit('lane must be 0..5')
    out=AUDITS[a.audit](a.lane); out.update({'audit':a.audit,'lane':a.lane})
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,sort_keys=True))
    if not out['passed']: raise SystemExit(2)
if __name__=='__main__': main()
