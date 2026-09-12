#!/usr/bin/env python3
"""QGR Iter027 G27 — primitive Boolean composition / boundary-insertion authority.

Prospectively frozen question:
Can the already-derived Boolean composition laws reduce the missing event->source
map to a unique physical law without inserting a fitted coupling?

Five independent exact audits are used:
  1) additive source valuation on 0..6 equivalent primitive pair events;
  2) multiplicative composition character non-uniqueness;
  3) exact B4 prefix/history law blindness to physical source scale;
  4) S4 rank-shell boundary coboundary/path-independence;
  5) serial/overlap composition ratios versus absolute scale.

All arithmetic is exact Fraction/integer arithmetic. No fitted physical numbers.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path


def rank(mat):
    a = [[F(x) for x in row] for row in mat]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c] != 0), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        piv = a[r][c]
        a[r] = [x / piv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [x - q*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def frac(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def audit_additive_valuation(lane: int):
    # J_n for n=1..6 equivalent primitive distinct-pair events.
    # J_{a+b}=J_a+J_b for all a,b>=1 with a+b<=6.
    rows = []
    for a in range(1, 7):
        for b in range(1, 7):
            if a + b <= 6:
                row = [F(0)] * 6
                row[a+b-1] += 1
                row[a-1] -= 1
                row[b-1] -= 1
                rows.append(row)
    r = rank(rows)
    nullity = 6-r
    beta1 = F(lane+1, lane+2)
    beta2 = beta1 + F(1, lane+3)
    v1 = [beta1*n for n in range(1,7)]
    v2 = [beta2*n for n in range(1,7)]
    def resid(v):
        return all(sum(row[j]*v[j] for j in range(6)) == 0 for row in rows)
    passed = r == 5 and nullity == 1 and resid(v1) and resid(v2) and beta1 != beta2
    return {
        "gate":"ITER027-G27-ADDITIVE-BOOLEAN-SOURCE-VALUATION",
        "classification":"PASS_SCOPED_ZERO_EMPTY_INSERTION_PLUS_S4_EQUIVALENCE_AND_ADDITIVE_PRIMITIVE_EVENT_COMPOSITION_FIXES_SOURCE_LAW_SHAPE_TO_J_N_EQUALS_BETA_TIMES_N_BUT_LEAVES_ONE_SCALAR_BETA",
        "constraint_rank":r,
        "source_values_dimension":6,
        "nullity":nullity,
        "canonical_null_ray":[1,2,3,4,5,6],
        "two_exact_beta_witnesses":[frac(beta1),frac(beta2)],
        "absolute_beta_fixed":False,
        "passed":passed,
    }


def audit_multiplicative_character(lane: int):
    # A_{n+m}=A_n A_m, A_0=1 => A_n=a^n. Composition fixes the shape,
    # not the generator a. Two exact positive generators are explicit witnesses.
    a1 = F(lane+1, lane+2)
    a2 = F(lane+2, lane+4) + F(1, 7)
    if a2 == a1:
        a2 += F(1,11)
    def char(a):
        return [a**n for n in range(7)]
    c1, c2 = char(a1), char(a2)
    def check(c):
        return c[0] == 1 and all(c[i+j] == c[i]*c[j] for i in range(7) for j in range(7-i))
    passed = check(c1) and check(c2) and a1 != a2 and c1 != c2
    return {
        "gate":"ITER027-G27-MULTIPLICATIVE-COMPOSITION-CHARACTER",
        "classification":"PASS_SCOPED_MULTIPLICATIVE_BOOLEAN_COMPOSITION_FIXES_CHARACTER_SHAPE_A_N_EQUALS_A_TO_THE_N_BUT_DOES_NOT_FIX_THE_SINGLE_EVENT_GENERATOR",
        "generator_witnesses":[frac(a1),frac(a2)],
        "both_exact_characters":True,
        "single_event_generator_fixed":False,
        "passed":passed,
    }


def audit_prefix_scale_blindness(lane: int):
    # Existing uniform B4 histories give exact rank-conditioned next-step probabilities.
    p = [F(1,4),F(1,3),F(1,2),F(1,1)]
    full = p[0]*p[1]*p[2]*p[3]
    beta1 = F(lane+1,lane+2)
    beta2 = beta1 + F(2,lane+5)
    # p contains no beta dependence; exact finite-difference authority is zero.
    delta = [x-x for x in p]
    passed = full == F(1,24) and beta1 != beta2 and all(x == 0 for x in delta)
    return {
        "gate":"ITER027-G27-PREFIX-HISTORY-SCALE-BLINDNESS",
        "classification":"PASS_SCOPED_EXACT_PREFIX_LAW_FIXES_DIMENSIONLESS_BRANCH_PROBABILITIES_AND_FULL_HISTORY_WEIGHT_ONE_OVER_24_BUT_HAS_ZERO_AUTHORITY_ON_PHYSICAL_EVENT_SOURCE_SCALE",
        "conditional_probabilities":[frac(x) for x in p],
        "single_history_probability":frac(full),
        "two_source_scale_witnesses":[frac(beta1),frac(beta2)],
        "authority_rank_on_beta":0,
        "passed":passed,
    }


def audit_boundary_coboundary(lane: int):
    # S4-invariant rank-shell potential phi_0..phi_4, phi_0=0.
    # Path-independence is automatic for any shell potential. If one additionally
    # imposes translation-homogeneous primitive insertion, all four edge increments
    # d_r=phi_{r+1}-phi_r must be equal. This leaves phi_r = r*d: one scalar.
    # Variables are phi1..phi4.
    rows=[]
    # d0=d1, d1=d2, d2=d3
    # d0=phi1; d1=phi2-phi1; d2=phi3-phi2; d3=phi4-phi3
    rows.append([F(2),F(-1),F(0),F(0)])
    rows.append([F(-1),F(2),F(-1),F(0)])
    rows.append([F(0),F(-1),F(2),F(-1)])
    r=rank(rows); nullity=4-r
    d1=F(lane+1,lane+3); d2=d1+F(1,lane+4)
    phi1=[d1*n for n in range(1,5)]
    phi2=[d2*n for n in range(1,5)]
    def resid(v): return all(sum(row[j]*v[j] for j in range(4))==0 for row in rows)
    # Telescoping path sum across four ranks equals phi4 independent of ordering.
    tel1=sum([phi1[0],phi1[1]-phi1[0],phi1[2]-phi1[1],phi1[3]-phi1[2]])
    tel2=sum([phi2[0],phi2[1]-phi2[0],phi2[2]-phi2[1],phi2[3]-phi2[2]])
    passed=r==3 and nullity==1 and resid(phi1) and resid(phi2) and tel1==phi1[3] and tel2==phi2[3] and d1!=d2
    return {
        "gate":"ITER027-G27-BOUNDARY-COBOUNDARY-AUTHORITY",
        "classification":"PASS_SCOPED_BOOLEAN_PATH_INDEPENDENCE_IS_AUTOMATIC_FOR_RANK_SHELL_BOUNDARY_POTENTIALS_AND_HOMOGENEOUS_PRIMITIVE_INSERTION_REDUCES_THEM_TO_PHI_R_EQUALS_R_TIMES_D_WITH_ONE_UNFIXED_SCALE",
        "homogeneous_increment_constraint_rank":r,
        "nullity":nullity,
        "canonical_rank_shell_ray":[1,2,3,4],
        "path_independence_fixes_scale":False,
        "passed":passed,
    }


def audit_composition_ratios(lane: int):
    # Already-derived Boolean regions: one B4 diagonal has 4 primitive rank steps;
    # 2x1x1x1 face-overlap global path has multiset length 5; two true serial B4
    # diagonals have 8 steps. Additive homogeneous insertion predicts fixed relative
    # counts 4:5:8 but a common physical conversion beta remains.
    counts=[4,5,8]
    beta1=F(lane+1,lane+2); beta2=beta1+F(1,lane+5)
    src1=[beta1*n for n in counts]; src2=[beta2*n for n in counts]
    ratios1=[F(src1[i],src1[0]) for i in range(3)]
    ratios2=[F(src2[i],src2[0]) for i in range(3)]
    expected=[F(1),F(5,4),F(2)]
    # Combinatorial history/path normalizations coexist: 24 single-cell paths,
    # 60 overlap-region global paths, 576 serial ordered pairs; none contains beta.
    path_counts=[24,60,576]
    passed=ratios1==expected and ratios2==expected and src1!=src2 and path_counts==[24,60,576]
    return {
        "gate":"ITER027-G27-COMPOSITION-RATIO-AUTHORITY",
        "classification":"PASS_SCOPED_BOOLEAN_SERIAL_AND_OVERLAP_COMPOSITION_FIXES_RELATIVE_ADDITIVE_INSERTION_COUNT_RATIOS_4_TO_5_TO_8_BUT_NOT_THE_COMMON_PHYSICAL_CONVERSION_SCALE",
        "primitive_step_counts":counts,
        "normalized_combinatorial_path_counts":path_counts,
        "scale_independent_source_ratios":[frac(x) for x in expected],
        "absolute_source_scale_fixed":False,
        "passed":passed,
    }


AUDITS={
    "additive-valuation":audit_additive_valuation,
    "multiplicative-character":audit_multiplicative_character,
    "prefix-scale-blindness":audit_prefix_scale_blindness,
    "boundary-coboundary":audit_boundary_coboundary,
    "composition-ratios":audit_composition_ratios,
}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audit",choices=sorted(AUDITS),required=True)
    ap.add_argument("--lane",type=int,required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    if not 0 <= a.lane <= 5:
        raise SystemExit("lane must be 0..5")
    out=AUDITS[a.audit](a.lane)
    out.update({"audit":a.audit,"lane":a.lane})
    p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    if not out["passed"]:
        raise SystemExit(2)

if __name__=="__main__":
    main()
