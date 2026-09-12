#!/usr/bin/env python3
import argparse
import json
import os
from fractions import Fraction as F

AUDITS = (
    "global-log-branch-nonuniqueness",
    "weak-cell-principal-branch",
    "finite-sample-integral-nullspace",
    "overall-action-phase-scale",
    "finite-refinement-integral-nullspace",
)


def s(x):
    return str(F(x))


def floor_fraction(x):
    return x.numerator // x.denominator


def mod1(x):
    x = F(x)
    return x - floor_fraction(x)


def principal_mod1(x):
    y = mod1(x)
    return y if y < F(1, 2) else y - 1


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def poly_eval(p, x):
    x = F(x)
    total = F(0)
    power = F(1)
    for c in p:
        total += c * power
        power *= x
    return total


def poly_integral_01(p):
    return sum(c / F(i + 1) for i, c in enumerate(p))


def vanishing_square(nodes):
    p = [F(1)]
    for x in nodes:
        p = poly_mul(p, [-F(x), F(1)])
    return poly_mul(p, p)


def audit_global_log(lane):
    # Normalize a spatial SO(2) rotation angle by 2*pi, so holonomy is x mod Z.
    # Distinct Lie-algebra lifts x and x+1 give exactly the same group element.
    x = F(lane + 1, 2 * lane + 7)
    lift1 = x
    lift2 = x + 1
    same_holonomy_class = mod1(lift1) == mod1(lift2)
    passed = lift1 != lift2 and same_holonomy_class
    return {
        "gate": "ITER031-G31-GLOBAL-LOG-BRANCH-NONUNIQUENESS",
        "audit": "global-log-branch-nonuniqueness",
        "lane": lane,
        "normalized_rotation_lifts": [s(lift1), s(lift2)],
        "holonomy_class_mod_1": s(mod1(lift1)),
        "passed": passed,
        "classification": "BLOCKED_SCOPED_FINITE_LORENTZ_HOLONOMY_DOES_NOT_GLOBALLY_SELECT_A_UNIQUE_LIE_ALGEBRA_CURVATURE_LOG_BRANCH",
        "guard": "The exact witness uses the compact spatial SO(2) subgroup of the Lorentz group; a global finite-cell curvature log needs additional branch/refinement authority."
    }


def audit_weak_principal(lane):
    # On the normalized principal interval (-1/2,1/2), the lift is unique.
    x = F(lane + 1, 4 * lane + 12)  # 0 < x <= 1/4
    area = F(lane + 2, lane + 5)
    reps = [x + k for k in range(-3, 4) if -F(1, 2) < x + k < F(1, 2)]
    principal = principal_mod1(x)
    curvature_est = principal / area
    passed = len(reps) == 1 and reps[0] == x and principal == x and area > 0
    return {
        "gate": "ITER031-G31-WEAK-CELL-PRINCIPAL-BRANCH",
        "audit": "weak-cell-principal-branch",
        "lane": lane,
        "principal_normalized_angle": s(principal),
        "cell_area_control": s(area),
        "leading_curvature_estimate": s(curvature_est),
        "principal_representative_count_in_tested_lifts": len(reps),
        "passed": passed,
        "classification": "PASS_SCOPED_WEAK_CELL_CONTINUITY_AND_PRINCIPAL_BRANCH_SELECT_A_UNIQUE_LOCAL_CURVATURE_LIFT_BEFORE_THE_FIRST_COMPACT_ROTATION_CUT",
        "guard": "This is local weak-cell branch authority, not a global strong-curvature logarithm theorem."
    }


def audit_finite_sample_null(lane):
    # Endpoint samples do not determine the integral. p=t(1-t) vanishes at both
    # endpoints but integrates to 1/6. Scale by a lane-dependent rational.
    q = F(lane + 1, lane + 3)
    p = [F(0), q, -q]
    samples = [poly_eval(p, F(0)), poly_eval(p, F(1))]
    integ = poly_integral_01(p)
    passed = samples == [F(0), F(0)] and integ == q / 6 and integ != 0
    return {
        "gate": "ITER031-G31-FINITE-SAMPLE-INTEGRAL-NULLSPACE",
        "audit": "finite-sample-integral-nullspace",
        "lane": lane,
        "endpoint_samples": [s(v) for v in samples],
        "integral_difference": s(integ),
        "passed": passed,
        "classification": "BLOCKED_SCOPED_FINITE_ENDPOINT_OR_VERTEX_SAMPLES_DO_NOT_UNIQUELY_DETERMINE_THE_LOCAL_ACTION_INTEGRAL_WITHOUT_INTERPOLATION_OR_QUADRATURE_AUTHORITY",
        "guard": "Two local densities can agree on all supplied samples yet differ in integrated action."
    }


def audit_action_scale(lane):
    # Multiplying a nonzero classical action functional by a nonzero constant
    # preserves its stationary zero set while changing S/hbar. This isolates the
    # quantum absolute-phase role of the already-existing overall normalization.
    I = F(lane + 2, lane + 7)
    a1 = F(lane + 1, lane + 4)
    a2 = a1 + F(1, lane + 6)
    grad_control = F(0)  # stationarity witness
    eom1 = a1 * grad_control
    eom2 = a2 * grad_control
    S1 = a1 * I
    S2 = a2 * I
    passed = a1 != a2 and eom1 == eom2 == 0 and S1 != S2
    return {
        "gate": "ITER031-G31-OVERALL-ACTION-PHASE-SCALE",
        "audit": "overall-action-phase-scale",
        "lane": lane,
        "action_normalization_witnesses": [s(a1), s(a2)],
        "same_stationarity_value": s(eom1),
        "distinct_action_values": [s(S1), s(S2)],
        "passed": passed,
        "classification": "BLOCKED_SCOPED_CLASSICAL_STATIONARITY_STRUCTURE_DOES_NOT_BY_ITSELF_FIX_THE_ABSOLUTE_QUANTUM_ACTION_PHASE_NORMALIZATION",
        "guard": "This does not assert the existing action normalization is disposable; it states that its absolute quantum-phase value needs independent microscopic or empirical authority."
    }


def audit_refinement_null(lane):
    # Even after a finite refinement, construct an exact polynomial square that
    # vanishes at every sampled node but has positive nonzero integral.
    N = lane + 2
    nodes = [F(k, N) for k in range(N + 1)]
    bump = vanishing_square(nodes)
    values = [poly_eval(bump, x) for x in nodes]
    integ = poly_integral_01(bump)
    passed = all(v == 0 for v in values) and integ > 0
    return {
        "gate": "ITER031-G31-FINITE-REFINEMENT-INTEGRAL-NULLSPACE",
        "audit": "finite-refinement-integral-nullspace",
        "lane": lane,
        "refinement_intervals": N,
        "sample_count": len(nodes),
        "all_sample_differences_zero": all(v == 0 for v in values),
        "integral_difference": s(integ),
        "passed": passed,
        "classification": "BLOCKED_SCOPED_ANY_FINITE_REFINEMENT_LEVEL_RETAINS_AN_EXACT_ACTION_INTEGRAL_NULLSPACE_UNLESS_AN_INTERPOLATION_CLASS_OR_CONVERGENT_PROJECTIVE_LIMIT_RULE_IS_DERIVED",
        "guard": "Finite sampling density alone is not an exact continuum action integral."
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", choices=AUDITS, required=True)
    ap.add_argument("--lane", type=int, required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if not 0 <= args.lane < 6:
        raise SystemExit("lane must be in 0..5")

    fn = {
        "global-log-branch-nonuniqueness": audit_global_log,
        "weak-cell-principal-branch": audit_weak_principal,
        "finite-sample-integral-nullspace": audit_finite_sample_null,
        "overall-action-phase-scale": audit_action_scale,
        "finite-refinement-integral-nullspace": audit_refinement_null,
    }[args.audit]
    out = fn(args.lane)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, sort_keys=True))
    if not out["passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
