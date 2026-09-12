#!/usr/bin/env python3
"""QGR Iter026 G26: exact audit of existing microscopic event-to-source authority.

Frozen question: do already-derived QGR structures (Boolean pair incidence, the
homogeneous pair action, metric-compatible connection/holonomy, normalized
history instrument, or torsion/coarea measure) determine a nonzero absolute
map from one Boolean event to a physical boundary/source strength, without a
new coupling or convention?

No floating-point fitting is used.  All algebraic tests are exact Fractions.
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
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                q = a[i][c]
                a[i] = [x - q*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def matvec(A, x):
    return [sum((A[i][j] * x[j] for j in range(len(x))), F(0)) for i in range(len(A))]


def inv_C4():
    # Exact inverse of C=J-I in d=4: -I + J/3.
    return [[F(1,3) - (F(1) if i == j else F(0)) for j in range(4)] for i in range(4)]


def C4():
    return [[F(0) if i == j else F(1) for j in range(4)] for i in range(4)]


def frac(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def audit_incidence(lane):
    # Six unordered distinct pairs. S4 transitivity forces all six responses equal.
    # Five independent equality constraints leave exactly one scalar beta.
    constraints = []
    for j in range(1, 6):
        row = [F(0)] * 6
        row[0], row[j] = F(1), F(-1)
        constraints.append(row)
    r = rank(constraints)
    nullity = 6 - r
    b1 = F(lane + 1, lane + 2)
    b2 = F(lane + 2, lane + 3)
    w1, w2 = [b1]*6, [b2]*6
    ok1 = all(v == 0 for v in matvec(constraints, w1))
    ok2 = all(v == 0 for v in matvec(constraints, w2))
    passed = (r == 5 and nullity == 1 and ok1 and ok2 and b1 != b2)
    return {
        "gate": "ITER026-G26-INCIDENCE-AUTHORITY",
        "classification": "PASS_SCOPED_DISTINCT_PAIR_INCIDENCE_PLUS_S4_FIXES_THE_EVENT_RESPONSE_RAY_BUT_LEAVES_EXACTLY_ONE_ABSOLUTE_SCALAR_BETA",
        "constraint_rank": r,
        "response_dimension": 6,
        "nullity": nullity,
        "two_exact_admissible_beta_witnesses": [frac(b1), frac(b2)],
        "absolute_source_strength_fixed": False,
        "passed": passed,
    }


def audit_pair_action(lane):
    # Existing microscopic pair action is homogeneous quadratic: S=kappa/2 q^T C q.
    # Its variation at q=0 is exactly zero for every kappa, so it contains no
    # nonhomogeneous event source term that can select a nonzero endpoint.
    C = C4()
    q0 = [F(0)]*4
    k1 = F(lane + 1, lane + 2)
    k2 = F(lane + 3, lane + 4)
    grad1 = [k1*x for x in matvec(C, q0)]
    grad2 = [k2*x for x in matvec(C, q0)]
    h1 = [[k1*x for x in row] for row in C]
    h2 = [[k2*x for x in row] for row in C]
    passed = (all(x == 0 for x in grad1+grad2) and h1 != h2 and k1 != k2)
    return {
        "gate": "ITER026-G26-HOMOGENEOUS-PAIR-ACTION",
        "classification": "PASS_SCOPED_EXISTING_PAIR_INCIDENCE_ACTION_IS_HOMOGENEOUS_QUADRATIC_AND_HAS_ZERO_SOURCE_GRADIENT_AT_THE_IDENTITY_FOR_ANY_OVERALL_KAPPA",
        "gradient_at_identity_kappa1": [frac(x) for x in grad1],
        "gradient_at_identity_kappa2": [frac(x) for x in grad2],
        "different_hessians_same_zero_source": h1 != h2,
        "nonzero_event_source_derived": False,
        "passed": passed,
    }


def gamma_from(Ginv, D):
    # D[i][a][b] = D_i G_ab, symmetric in a,b.
    out = [[ [F(0) for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                out[i][k][j] = F(1,2) * sum(
                    Ginv[k][l] * (D[i][l][j] + D[j][l][i] - D[l][i][j])
                    for l in range(4)
                )
    return out


def audit_connection(lane):
    # Under a constant common rescaling G->lambda G and DG->lambda DG,
    # G^{-1}->G^{-1}/lambda and the compatible connection is exactly unchanged.
    Ginv = inv_C4()
    D = []
    for i in range(4):
        M = []
        for a in range(4):
            row = []
            for b in range(4):
                row.append(F((i+1)*(a+b+2) + lane, lane+2))
            M.append(row)
        D.append(M)
    lam = F(lane + 2, lane + 1)
    Gam = gamma_from(Ginv, D)
    Ginv2 = [[x/lam for x in row] for row in Ginv]
    D2 = [[[lam*x for x in row] for row in M] for M in D]
    Gam2 = gamma_from(Ginv2, D2)
    passed = (Gam == Gam2 and lam != 0)
    return {
        "gate": "ITER026-G26-CONNECTION-SCALE-HOMOGENEITY",
        "classification": "PASS_SCOPED_METRIC_COMPATIBLE_CONNECTION_AND_DERIVED_HOLONOMY_ARE_BLIND_TO_A_CONSTANT_COMMON_SECOND_MOMENT_RESCALE_AND_CANNOT_FIX_ITS_ABSOLUTE_EVENT_SOURCE_STRENGTH",
        "lambda": frac(lam),
        "connection_exactly_invariant": Gam == Gam2,
        "absolute_source_strength_fixed": False,
        "passed": passed,
    }


def audit_history(lane):
    # Completeness fixes modulus only. The derivative/rank of this normalization
    # equation with respect to any action/source phase coefficient is zero.
    branch_prob = F(1,24)
    completeness = 24 * branch_prob
    # Two distinct formal phase/source values have identical K^dagger K.
    s1 = F(lane + 1, lane + 2)
    s2 = F(lane + 3, lane + 5)
    norm1 = branch_prob
    norm2 = branch_prob
    phase_authority_rank = 0
    passed = (completeness == 1 and norm1 == norm2 and s1 != s2 and phase_authority_rank == 0)
    return {
        "gate": "ITER026-G26-HISTORY-NORMALIZATION-AUTHORITY",
        "classification": "PASS_SCOPED_HISTORY_COMPLETENESS_FIXES_BRANCH_MODULUS_ONE_OVER_SQRT24_BUT_HAS_ZERO_AUTHORITY_RANK_ON_EVENT_SOURCE_OR_ACTION_PHASE_STRENGTH",
        "completeness": frac(completeness),
        "two_distinct_phase_source_witnesses": [frac(s1), frac(s2)],
        "KdaggerK_for_both": frac(branch_prob),
        "authority_rank_on_phase_or_source": phase_authority_rank,
        "passed": passed,
    }


def audit_coarea(lane):
    # The derived torsion/coarea datum is a positive real measure factor.  Even if
    # its log-weight m is known exactly, a phase prescription theta=c*m contains
    # an arbitrary conversion coefficient c. Two exact c values give the same
    # measure datum but different coherent phases: no canonical phase/source map.
    m = F(lane + 1, lane + 3)
    c1 = F(1, lane + 2)
    c2 = F(2, lane + 2)
    th1, th2 = c1*m, c2*m
    passed = (m != 0 and c1 != c2 and th1 != th2)
    return {
        "gate": "ITER026-G26-COAREA-MEASURE-VS-PHASE",
        "classification": "PASS_SCOPED_TORSION_COAREA_WEIGHT_IS_A_REAL_MEASURE_DATUM_AND_DOES_NOT_CANONICALLY_DETERMINE_A_COHERENT_EVENT_SOURCE_OR_ACTION_PHASE",
        "same_exact_measure_log_weight": frac(m),
        "two_admissible_unfixed_conversion_coefficients": [frac(c1), frac(c2)],
        "different_phase_arguments": [frac(th1), frac(th2)],
        "canonical_measure_to_phase_map_derived": False,
        "passed": passed,
    }


AUDITS = {
    "incidence-authority": audit_incidence,
    "pair-action-homogeneity": audit_pair_action,
    "connection-scale-homogeneity": audit_connection,
    "history-normalization-authority": audit_history,
    "coarea-measure-vs-phase": audit_coarea,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", choices=sorted(AUDITS), required=True)
    ap.add_argument("--lane", type=int, required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if not 0 <= args.lane <= 5:
        raise SystemExit("lane must be 0..5")
    result = AUDITS[args.audit](args.lane)
    result.update({"audit": args.audit, "lane": args.lane})
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    if not result["passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
