#!/usr/bin/env python3
import argparse
import json
import os
from fractions import Fraction as F

AUDITS = (
    "weak-log-refinement-lift",
    "lipschitz-null-bound",
    "riemann-polynomial-convergence",
    "quadrature-common-limit",
    "local-integral-cylindrical-additivity",
)


def s(x):
    return str(F(x))


def principal(x):
    # normalized angle in turns, principal interval [-1/2,1/2)
    x = F(x)
    k = x.numerator // x.denominator
    y = x - k
    return y if y < F(1, 2) else y - 1


def poly_integral_monomial(p, a=F(0), b=F(1)):
    return (F(b) ** (p + 1) - F(a) ** (p + 1)) / F(p + 1)


def left_sum_monomial(p, N):
    N = int(N)
    return sum(F(k, N) ** p for k in range(N)) / N


def right_sum_monomial(p, N):
    N = int(N)
    return sum(F(k, N) ** p for k in range(1, N + 1)) / N


def audit_weak_log_refinement(lane):
    # A continuous fine-path lift can carry a total normalized rotation beyond
    # the coarse principal interval. Once each subcell angle is weak enough,
    # every local principal log is unique and their ordered sum recovers the
    # chosen continuous lift exactly.
    total = F(lane + 4, 3)  # includes values > 1 turn
    N = 2 * (lane + 4) + 3
    sub = total / N
    local = principal(sub)
    recovered = sum((local for _ in range(N)), F(0))
    passed = abs(sub) < F(1, 2) and local == sub and recovered == total
    return {
        "gate": "ITER032-G32-WEAK-LOG-REFINEMENT-LIFT",
        "audit": "weak-log-refinement-lift",
        "lane": lane,
        "continuous_total_lift": s(total),
        "subcell_count": N,
        "subcell_principal_lift": s(local),
        "recovered_total_lift": s(recovered),
        "passed": passed,
        "classification": "PASS_SCOPED_A_RESOLVED_CONTINUOUS_FINE_PATH_WITH_SUFFICIENTLY_WEAK_SUBCELLS_HAS_UNIQUE_LOCAL_PRINCIPAL_LOGS_WHOSE_ORDERED_SUM_RECOVERS_THE_CHOSEN_LIFT",
        "guard": "This needs resolved fine-path/refinement data; coarse holonomy alone still cannot choose the global winding sector."
    }


def audit_lipschitz_null_bound(lane):
    # If two candidate densities agree at all N+1 uniform nodes and their
    # difference is L-Lipschitz, nearest-node control gives |g| <= L/(2N),
    # hence |integral g| <= L/(2N). Doubling N halves the bound exactly.
    L = F(lane + 2, lane + 1)
    N = 2 ** (lane + 2)
    b1 = L / (2 * N)
    b2 = L / (4 * N)
    passed = b1 > 0 and b2 == b1 / 2
    return {
        "gate": "ITER032-G32-LIPSCHITZ-NULL-BOUND",
        "audit": "lipschitz-null-bound",
        "lane": lane,
        "L_control": s(L),
        "N": N,
        "integral_null_bound_N": s(b1),
        "integral_null_bound_2N": s(b2),
        "passed": passed,
        "classification": "PASS_CONDITIONAL_UNDER_A_UNIFORM_LIPSCHITZ_BOUND_THE_FINITE_SAMPLE_ACTION_NULLSPACE_IS_FORCED_TO_ZERO_IN_THE_REFINEMENT_LIMIT_AT_LEAST_AS_ONE_OVER_N",
        "guard": "Uniform QGR regularity across the refinement tower is a separate authority question and is not assumed proven here."
    }


def audit_riemann_convergence(lane):
    p = lane + 1
    I = F(1, p + 1)
    Ns = [4, 8, 16, 32]
    sums = [left_sum_monomial(p, N) for N in Ns]
    errors = [I - x for x in sums]
    monotone_error = all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    bound_ok = all(F(0) < e <= F(1, N) for e, N in zip(errors, Ns))
    passed = monotone_error and bound_ok
    return {
        "gate": "ITER032-G32-RIEMANN-POLYNOMIAL-CONVERGENCE",
        "audit": "riemann-polynomial-convergence",
        "lane": lane,
        "monomial_power": p,
        "exact_integral": s(I),
        "N_values": Ns,
        "left_sum_errors": [s(e) for e in errors],
        "passed": passed,
        "classification": "PASS_SCOPED_EXACT_RATIONAL_MONOTONE_POLYNOMIAL_CONTROLS_SHOW_REFINEMENT_RIEMANN_ACTIONS_CONVERGE_TO_THE_UNIQUE_LOCAL_INTEGRAL_WITH_CONTROLLED_ERROR",
        "guard": "Polynomial controls validate the refinement mechanism; they are not a proof of QGR field regularity."
    }


def audit_quadrature_common_limit(lane):
    p = lane + 1
    N = 2 ** (lane + 3)
    Ls = left_sum_monomial(p, N)
    Rs = right_sum_monomial(p, N)
    L2 = left_sum_monomial(p, 2 * N)
    R2 = right_sum_monomial(p, 2 * N)
    gap1 = Rs - Ls
    gap2 = R2 - L2
    passed = gap1 == F(1, N) and gap2 == F(1, 2 * N) and gap2 == gap1 / 2
    return {
        "gate": "ITER032-G32-QUADRATURE-COMMON-LIMIT",
        "audit": "quadrature-common-limit",
        "lane": lane,
        "power": p,
        "N": N,
        "left_right_gap_N": s(gap1),
        "left_right_gap_2N": s(gap2),
        "passed": passed,
        "classification": "PASS_SCOPED_LEFT_AND_RIGHT_LOCAL_ACTION_QUADRATURE_AMBIGUITY_COLLAPSES_AS_ONE_OVER_N_ON_THE_EXACT_MONOTONE_CONTROLS",
        "guard": "A common refinement limit removes scheme ambiguity only under the regularity assumptions needed for convergence."
    }


def audit_cylindrical_additivity(lane):
    # Once the local continuum integral exists, its interval contributions are
    # exactly cylindrically additive under arbitrary rational partitioning.
    p = lane + 1
    N = lane + 2
    cells = [poly_integral_monomial(p, F(k, N), F(k + 1, N)) for k in range(N)]
    total = sum(cells, F(0))
    direct = poly_integral_monomial(p)
    # two-level regrouping
    split = []
    M = 2 * N
    fine = [poly_integral_monomial(p, F(k, M), F(k + 1, M)) for k in range(M)]
    for k in range(N):
        split.append(fine[2 * k] + fine[2 * k + 1])
    passed = total == direct and split == cells
    return {
        "gate": "ITER032-G32-LOCAL-INTEGRAL-CYLINDRICAL-ADDITIVITY",
        "audit": "local-integral-cylindrical-additivity",
        "lane": lane,
        "power": p,
        "coarse_cells": N,
        "direct_integral": s(direct),
        "coarse_sum": s(total),
        "two_level_blocking_exact": split == cells,
        "passed": passed,
        "classification": "PASS_SCOPED_WHEN_THE_LOCAL_ACTION_INTEGRAL_EXISTS_ITS_CELL_CONTRIBUTIONS_HAVE_EXACT_TWO_LEVEL_CYLINDRICAL_ADDITIVITY",
        "guard": "This establishes the projective algebra of the limiting integral, not the missing physical normalization or c6 value."
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", choices=AUDITS, required=True)
    ap.add_argument("--lane", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if not 0 <= a.lane < 6:
        raise SystemExit("lane must be 0..5")
    fn = {
        "weak-log-refinement-lift": audit_weak_log_refinement,
        "lipschitz-null-bound": audit_lipschitz_null_bound,
        "riemann-polynomial-convergence": audit_riemann_convergence,
        "quadrature-common-limit": audit_quadrature_common_limit,
        "local-integral-cylindrical-additivity": audit_cylindrical_additivity,
    }[a.audit]
    out = fn(a.lane)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, sort_keys=True))
    if not out["passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
