# COVARIANT_WEYL3_A7_FIRST_IBP_FI_JET_CAUSAL_AUDIT — prospective preregistration

Date: 2026-09-19
Status: FROZEN BEFORE IMPLEMENTATION OR RESULT INSPECTION

## Parent authority

This gate is a causal refinement of terminal lower-order localization run `35403445578`, durable result commit `6ccfededab41dbe01b071916a5aa746491273276`.

The parent classification remains `SCIENTIFIC_FAIL_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_DISCREPANCY`; the localization result is `LOWER_ORDER_LOCALIZED_EXACT` with first divergence `FIRST_DERIVATIVE_IBP_TRANSFER`.

Frozen witness remains exactly `OFFSHELL_A / d=7`. `c6=SYMBOLIC_UNFIXED`.

## Question

Why do Researcher and Critic have identical pointwise ordered `Fi` coefficients on the frozen A7 point but different exact derivative transfer `-d_i Fi`?

## Frozen causal test

Implement two independent exact lanes. Neither lane may import the other's derivative/jet helper.

For each ordered coordinate `i=0,1,2,3`, serialize target-blind before comparison:

1. pointwise `Fi` (control; must reproduce the parent exact equality);
2. the full first jet `d_j Fi` for ordered `j=0,1,2,3`;
3. the diagonal transfer component `-d_i Fi`;
4. decomposition of each `d_j Fi` by chain-rule source into frozen background metric jets, inverse-metric jets, curvature/Weyl jets, connection jets, and perturbation jets, using each lane's independently derived lineage;
5. exact reconstruction of the parent scalar first-IBP transfer by summing the four diagonal components.

No tolerance arithmetic. Fractions/exact symbolic arithmetic only.

## Frozen ordering and terminal taxonomy

Comparator scans lexicographically `(i,j)` over the 16 `d_j Fi` slots after confirming all four pointwise `Fi` controls.

- If all 16 first jets match exactly and the scalar transfer still differs: `BLOCKED_INTERNAL_INCONSISTENCY`.
- If a first jet differs: `FI_FIRST_JET_DIVERGENCE_LOCALIZED`, recording the first `(i,j)` and its exact difference.
- If first jets match and transfer matches: `FI_JET_AND_TRANSFER_MATCH__PARENT_RECONCILIATION_REQUIRED`.
- Missing provenance, non-exact arithmetic, source-lock failure, or inability to serialize the frozen decomposition: `BLOCKED_EXECUTION_OR_PROVENANCE`.

After the first differing `(i,j)` is frozen, compare its preregistered chain-rule source classes in this order: metric jet; inverse-metric jet; curvature/Weyl jet; connection jet; perturbation jet. Record the first exact source-class divergence. Do not reorder after inspection.

## Hard locks

No change to A7 witness, parent discrepancy, sign convention, normalization, Weyl definition, index placement, dimension, perturbation direction, thresholds, or target values. No fitting, rescaling, sign flip, regrouping, or repair after result inspection. A repair requires a separate prospective preregistration.

This finite off-shell audit is not a global theorem and cannot establish QGR, quantum unitarity, UV completion, a physical value of `c6`, experimental confirmation, or new physics. `theory_established=0%`; beta matching/calibration remains unfixed and `beta=1` unauthorized; corrected Q10 remains LOCKED; KMQGB `NEW_REQUIRED` remains unauthorized.
