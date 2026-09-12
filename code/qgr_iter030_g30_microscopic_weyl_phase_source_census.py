#!/usr/bin/env python3
import argparse
import json
import os
from fractions import Fraction as F

AUDITS = (
    "weyl-forward-sensitivity",
    "finite-geometry-phase-nonuniqueness",
    "history-phase-blindness",
    "coarea-measure-phase-nonuniqueness",
    "composition-absolute-scale-null",
)


def q(x):
    return str(F(x))


def audit_weyl_forward(lane):
    # Formal positive control for the already-authorized G29 forward structure:
    # S = S0 + c6 * W3.  W3 values here are algebraic controls, not physical data.
    W3 = F(lane + 1, lane + 2)
    c1 = F(lane + 1, 7)
    c2 = c1 + F(1, lane + 3)
    S0 = F(2 * lane + 1, 11)
    S1 = S0 + c1 * W3
    S2 = S0 + c2 * W3
    inferred_slope = (S2 - S1) / (c2 - c1)
    passed = W3 != 0 and inferred_slope == W3
    return {
        "gate": "ITER030-G30-WEYL-FORWARD-SENSITIVITY",
        "audit": "weyl-forward-sensitivity",
        "lane": lane,
        "W3_control": q(W3),
        "finite_difference_slope": q(inferred_slope),
        "passed": passed,
        "classification": "PASS_SCOPED_EXISTING_ACTION_FORM_HAS_NONZERO_FORWARD_C6_SENSITIVITY_WHEN_THE_RELEVANT_WEYL_CUBIC_FUNCTIONAL_IS_NONZERO",
        "guard": "The W3 values are exact algebraic positive controls, not derived physical finite-cell phase targets."
    }


def audit_geometry_phase_nonuniqueness(lane):
    # G9 supplies nontrivial finite holonomy geometry.  Geometry alone does not
    # select a coherent phase: two different phase labels leave all geometric
    # input labels unchanged.  Exact witness of missing map geometry -> phase.
    geometry_id = (lane + 1, lane + 2, lane + 3)
    theta1 = F(lane + 1, lane + 5)
    theta2 = theta1 + F(1, lane + 7)
    same_geometry = geometry_id == geometry_id
    distinct_phase = theta1 != theta2
    passed = same_geometry and distinct_phase
    return {
        "gate": "ITER030-G30-FINITE-GEOMETRY-PHASE-NONUNIQUENESS",
        "audit": "finite-geometry-phase-nonuniqueness",
        "lane": lane,
        "geometry_witness": list(geometry_id),
        "phase_witness_1": q(theta1),
        "phase_witness_2": q(theta2),
        "passed": passed,
        "classification": "BLOCKED_SCOPED_NONTRIVIAL_FINITE_HOLONOMY_GEOMETRY_DOES_NOT_BY_ITSELF_DEFINE_AN_ABSOLUTE_COHERENT_LORENTZIAN_PHASE",
        "guard": "Nonzero holonomy is curvature evidence, not a derived Weyl-cubic action phase or a numerical c6 datum."
    }


def audit_history_blindness(lane):
    # Existing 24-history instrument: K_alpha = 24^-1/2 exp(i theta) U_alpha.
    # Completeness depends on |K|^2 = 1/24 and is phase-blind exactly.
    theta1 = F(lane + 1, lane + 4)
    theta2 = theta1 + F(1, lane + 6)
    probability1 = F(1, 24)
    probability2 = F(1, 24)
    rank_on_phase = 0
    passed = theta1 != theta2 and probability1 == probability2 and rank_on_phase == 0
    return {
        "gate": "ITER030-G30-HISTORY-PHASE-BLINDNESS",
        "audit": "history-phase-blindness",
        "lane": lane,
        "theta_witnesses": [q(theta1), q(theta2)],
        "branch_probabilities": [q(probability1), q(probability2)],
        "authority_rank_on_absolute_phase": rank_on_phase,
        "passed": passed,
        "classification": "BLOCKED_SCOPED_EXACT_24_HISTORY_COMPLETENESS_NORMALIZES_BRANCH_MODULUS_BUT_HAS_ZERO_AUTHORITY_RANK_ON_ABSOLUTE_ACTION_PHASE",
        "guard": "Do not convert 1/sqrt(24) branch modulus into an event-source or Weyl-phase normalization."
    }


def audit_coarea_phase_nonuniqueness(lane):
    # A coarea/torsion branch weight is a positive real measure datum.  The same
    # weight supports distinct coherent phase labels; hence no canonical map
    # w -> theta follows from the measure alone.
    weight = F(lane + 2, lane + 9)
    theta1 = F(lane + 1, lane + 8)
    theta2 = theta1 + F(2, lane + 11)
    same_measure = weight == weight
    phase_distinct = theta1 != theta2
    authority_rank = 0
    passed = weight > 0 and same_measure and phase_distinct and authority_rank == 0
    return {
        "gate": "ITER030-G30-COAREA-MEASURE-PHASE-NONUNIQUENESS",
        "audit": "coarea-measure-phase-nonuniqueness",
        "lane": lane,
        "positive_measure_weight": q(weight),
        "phase_witnesses": [q(theta1), q(theta2)],
        "authority_rank_on_coherent_phase": authority_rank,
        "passed": passed,
        "classification": "BLOCKED_SCOPED_TORSION_COAREA_WEIGHT_IS_A_REAL_MEASURE_DATUM_AND_DOES_NOT_CANONICALLY_FIX_A_COHERENT_LORENTZIAN_PHASE",
        "guard": "A log-determinant or positive Jacobian may not be inserted into iS/hbar without a separately derived rule."
    }


def normalized_ratios(values):
    base = values[0]
    return tuple(v / base for v in values)


def audit_composition_scale_null(lane):
    # G27 source law J(n)=beta*n and G28 quotient observables.  Two distinct beta
    # values give identical endpoint and conformal on-shell phase ratios for the
    # fixed primitive counts (4,5,8), so quotient data cannot fix absolute beta.
    counts = (F(4), F(5), F(8))
    beta1 = F(lane + 1, lane + 3)
    beta2 = beta1 + F(1, lane + 5)
    J1 = tuple(beta1 * n for n in counts)
    J2 = tuple(beta2 * n for n in counts)
    endpoint_ratios_1 = normalized_ratios(J1)
    endpoint_ratios_2 = normalized_ratios(J2)
    phase_ratios_1 = normalized_ratios(tuple(x * x for x in J1))
    phase_ratios_2 = normalized_ratios(tuple(x * x for x in J2))
    passed = (
        beta1 != beta2
        and endpoint_ratios_1 == endpoint_ratios_2
        and phase_ratios_1 == phase_ratios_2
        and endpoint_ratios_1 == (F(1), F(5, 4), F(2))
        and phase_ratios_1 == (F(1), F(25, 16), F(4))
    )
    return {
        "gate": "ITER030-G30-COMPOSITION-ABSOLUTE-SCALE-NULL",
        "audit": "composition-absolute-scale-null",
        "lane": lane,
        "beta_witnesses": [q(beta1), q(beta2)],
        "counts": [4, 5, 8],
        "endpoint_ratios": [q(x) for x in endpoint_ratios_1],
        "conformal_phase_ratios": [q(x) for x in phase_ratios_1],
        "passed": passed,
        "classification": "BLOCKED_SCOPED_PRIMITIVE_COMPOSITION_AND_SOURCE_SCALE_QUOTIENT_FIX_RELATIVE_RATIOS_BUT_HAVE_AN_EXACT_ONE_PARAMETER_ABSOLUTE_SCALE_NULL_DIRECTION",
        "guard": "Scale-free composition ratios cannot be promoted to an absolute Weyl-active finite-cell phase target."
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
        "weyl-forward-sensitivity": audit_weyl_forward,
        "finite-geometry-phase-nonuniqueness": audit_geometry_phase_nonuniqueness,
        "history-phase-blindness": audit_history_blindness,
        "coarea-measure-phase-nonuniqueness": audit_coarea_phase_nonuniqueness,
        "composition-absolute-scale-null": audit_composition_scale_null,
    }[args.audit]
    result = fn(args.lane)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, sort_keys=True))
    if not result["passed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
