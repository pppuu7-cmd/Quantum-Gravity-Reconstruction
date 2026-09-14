# QGR Weyl3 dynamical-treatment selection authority — preparatory source audit

Date: 2026-09-14

Status: **outcome-independent preparation only**. This note does not classify Iter054F and does not select exact or order-reduced dynamics.

## Question

If the current mixed Einstein + `c6 Weyl^3` evolution object is not yet sufficiently defined for a strong-hyperbolicity test, does pre-existing QGR authority already contain a physical principle that selects between:

1. exact finite-`c6` fourth-order metric dynamics, including the full exact solution space; and
2. perturbative / order-reduced effective dynamics, in which only the branch analytic in the higher-derivative coefficient is retained within a controlled expansion domain?

This audit is preparatory because selecting a treatment after seeing its stability outcome would violate the QGR constitution.

## Source 1 — construction constitution

`docs/CONSTITUTION.md` forbids hidden branch selection after observing benchmark/results and requires additional freedom to have explicit physical origin. It also requires stability/positivity or framework-appropriate consistency for a minimal dynamical ansatz.

Consequence: exact versus order-reduced treatment cannot be chosen merely because one later gives a preferred spectrum/hyperbolicity result.

## Source 2 — Iter006 quantum composition layer

`iterations/ITERATION_006.md` defines the regular-domain coherent history operators

`K_alpha = 24^(-1/2) exp(i S_alpha / hbar) U_alpha`

and establishes normalized composition/positive coarse evolution in its scoped domain.

This supplies an action-phase role for `S_alpha`, but Iter006 predates the later `Weyl^3` coefficient line and does not specify whether a later higher-derivative local term is to be interpreted as an exact finite-coupling classical generator on all of its Euler-Lagrange solutions or as an effective derivative correction within a bounded expansion.

Therefore Iter006 does not by itself select the Weyl3 dynamical treatment.

## Source 3 — Iter010 c6 identifiability

`iterations/ITERATION_010.md` records that:

- lower-order authority leaves one `c6` direction free;
- history Kraus normalization and additive/projective phase composition remain exact for arbitrary real `c6`;
- no existing normalization/phase/loop/homogeneous-refinement rule fixes the absolute `c6` value;
- a Weyl-active background is sensitive to `c6`, but a nonhomogeneous microscopic absolute target is missing.

Consequence: the existing coherent-phase/composition rules do not select a unique finite coupling or, by themselves, an exact-versus-EFT solution-space prescription.

## Source 4 — Iter047 operator activation

The prospectively frozen Iter047 Weyl3 curvature-class gate treats the QGR correction density as proportional to symbolic `c6 * W3` and explicitly limits itself to operator activation/invariants, not the full Euler-Lagrange dynamics. Its exact use of curvature invariants therefore does not constitute authority for exact nonperturbative fourth-order evolution.

## Source 5 — Iter054A regime separation

Iter054A explicitly distinguishes:

- the exact higher-derivative branch of a mixed-order characteristic polynomial; and
- a finite perturbative branch analytic in the small higher-derivative coefficient.

Its preregistration states that the singular exact root lies outside a finite Taylor ansatz around the GR root unless separately justified. The gate deliberately does not choose which solution space is physically authoritative.

This is positive evidence that QGR already recognizes the two regimes as distinct, not evidence that one is selected.

## Source 6 — Iter054E regime proxy

Iter054E terminally confirms, within its exact frozen proxy, the GR-connected root and the singular branch `z_HD=-1/(eps lambda)`. Its interpretation lock explicitly withholds physical branch weights, mode/ghost status, strong hyperbolicity and quantum claims.

Thus Iter054E also does not select the physical treatment.

## Preparatory conclusion

Under the presently inspected authority, no existing source identified in this audit supplies a derived rule of the form:

- `TAKE_EXACT_FOURTH_ORDER_SOLUTION_SPACE_AS_PHYSICAL`, or
- `TAKE_ORDER_REDUCED_ANALYTIC_BRANCH_WITH_DERIVED_CUTOFF_AS_PHYSICAL`.

Nor is there yet an identified microscopic cutoff/matching theorem that would decide whether the non-analytic high-frequency branch lies inside the valid QGR continuum domain.

This is **not** a terminal scientific classification because Iter054F is still non-terminal and a separate prospective gate is required before declaring a treatment-selection blocker.

## Candidate next gate if authorized

If Iter054F terminally returns an evolution-object definition blocker, a high-information successor would be:

`ITER054G-WEYL3-DYNAMICAL-TREATMENT-SELECTION-AUTHORITY`

with frozen source/provenance lanes asking whether any already-derived microscopic QGR rule selects exact versus order-reduced dynamics, plus exact controls demonstrating that the two solution spaces agree perturbatively on the GR branch but differ nonperturbatively through the singular branch.

A valid negative outcome would be a **dynamical-treatment underdetermination blocker**, not a failure of the candidate equations.

## Claim ceiling

No treatment is selected here. No strong-hyperbolicity, well-posedness, mode-count, ghost, unitarity, `c6`, `beta=1`, UV-completion, GR-recovery, experimental or new-physics claim is authorized. Theory established remains 0%.
