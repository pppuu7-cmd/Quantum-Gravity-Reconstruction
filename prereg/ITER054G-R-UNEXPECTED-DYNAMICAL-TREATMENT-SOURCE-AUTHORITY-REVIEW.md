# Iter054G-R preregistration — unexpected dynamical-treatment source authority review

Date: 2026-09-14

Gate: `ITER054G-R-UNEXPECTED-DYNAMICAL-TREATMENT-SOURCE-AUTHORITY-REVIEW`

Status at freeze: **PREREGISTERED BEFORE FULL-CONTENT REVIEW OF UNEXPECTED SOURCES**

Parent gate: `ITER054G-WEYL3-DYNAMICAL-TREATMENT-SELECTION-AUTHORITY`

Parent run: `34818484127`

Parent terminal classification: `REQUIRES_SOURCE_AUTHORITY_REVIEW_ITER054G`

Frozen source snapshot: `3398cd5a195d3d6b05fad01715ab5b79a880c4f1`

## Why this successor exists

Iter054G's frozen repo-wide S0 census found 25 treatment-keyword hits in 14 paths. Six paths were already explicitly adjudicated by the parent A0/A1 source mapping. Eight additional paths were deliberately fail-closed as unexpected candidate authorities rather than ignored.

This review asks whether any of those exact eight frozen files actually satisfies the parent gate's treatment-selector obligations. Keyword occurrence alone is not authority.

No additional source may be added after review begins.

## Frozen eight-source panel

1. `docs/KMQGB_HANDOFF.md`
2. `iterations/ITERATION_007.md`
3. `iterations/ITERATION_012.md`
4. `preregistration/ITER054B_WEYL3_PRINCIPAL_HESSIAN_AND_WELLPOSEDNESS_OBLIGATION.md`
5. `results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md`
6. `results/ITER007_G7B_G7D_SCALE_BOUNDARY.md`
7. `results/ITER032_G32_PROJECTIVE_REFINEMENT_LIMIT_ACTION_PHASE.md`
8. `results/ITER053U_TERMINAL_RESULT.md`

Each lane reads its file from the frozen snapshot using `git show`. Later edits cannot change the review.

## Frozen selector criteria inherited from Iter054G

### `EXACT_SELECTOR`

A file can be classified `EXACT_SELECTOR` only if it itself provides authoritative QGR support for **all** of:

1. finite nonzero `c6` is an exact dynamical coupling, not merely symbolic/operator/finite-order bookkeeping;
2. the complete higher-derivative Euler-Lagrange solution space is physically admissible or an explicitly equivalent exact formulation is fixed;
3. additional initial-data/state content is mapped to the QGR physical state/measure/composition structure;
4. a validity domain for exact use is stated;
5. the rule is a QGR authority rather than background methodology and is not selected post hoc from stability/spectrum outcomes.

### `ORDER_REDUCED_SELECTOR`

A file can be classified `ORDER_REDUCED_SELECTOR` only if it itself provides authoritative QGR support for **all** of:

1. a controlled small derivative/coupling/scale expansion for the Weyl3 term;
2. a QGR-derived cutoff/matching/validity domain;
3. an explicit order-reduction prescription using lower-order equations;
4. a pre-existing domain-based reason the non-analytic singular branch is excluded;
5. a mapping of the reduced equations to QGR microscopic/state/composition authority and GR limit;
6. the rule is QGR authority rather than external/background methodology and is not post-hoc.

### `NON_SELECTOR`

A file is `NON_SELECTOR` if its hit is about an unrelated cutoff, merely states a future obligation, distinguishes regimes without selecting one, labels external literature as background-only, states insufficient evidence, or otherwise fails one or more mandatory selector obligations.

### `AMBIGUOUS_SOURCE_AUTHORITY`

Use only if the file contains a potentially authoritative treatment rule whose status/scope cannot be resolved from the frozen file itself. Do not infer a selector from ambiguity.

## Frozen independent lanes

Run eight independent lanes, one per path. Each lane must report:

- exact path and source-lock commit;
- all matching treatment-related excerpts with line numbers;
- whether the file claims QGR authority or background/diagnostic/prospective status;
- exact-selector obligations 1–5 separately;
- order-reduced-selector obligations 1–6 separately;
- one classification among `EXACT_SELECTOR`, `ORDER_REDUCED_SELECTOR`, `BOTH_SELECTORS`, `NON_SELECTOR`, `AMBIGUOUS_SOURCE_AUTHORITY`, `INVALID_PROVENANCE`;
- concise reason.

No lane may use another lane's output.

## Frozen aggregate

Parent Iter054G already returned `EXACT_NOT_SELECTED` and `ORDER_REDUCED_NOT_SELECTED` on its explicitly mapped core sources with valid controls.

Combine that parent fact with all eight review lanes:

- all eight `NON_SELECTOR` -> `BLOCKED_OBJECT_DEFINITION_ITER054G_WEYL3_DYNAMICAL_TREATMENT_NOT_SELECTED_AFTER_SOURCE_REVIEW`;
- exactly one or more `EXACT_SELECTOR` and no order-reduced selector -> `ITER054G_EXACT_DYNAMICAL_TREATMENT_SELECTED_AFTER_SOURCE_REVIEW`;
- exactly one or more `ORDER_REDUCED_SELECTOR` and no exact selector -> `ITER054G_ORDER_REDUCED_DYNAMICAL_TREATMENT_SELECTED_AFTER_SOURCE_REVIEW`;
- both treatment types authorized -> `BLOCKED_OBJECT_DEFINITION_ITER054G_MULTIPLE_DYNAMICAL_TREATMENTS_AUTHORIZED_WITHOUT_SELECTION_RULE`;
- any `AMBIGUOUS_SOURCE_AUTHORITY` -> `BLOCKED_SOURCE_AUTHORITY_ITER054G_UNEXPECTED_TREATMENT_SOURCE_AMBIGUOUS`;
- missing/invalid lanes -> `INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER054G_R`.

A BLOCKED result is valid terminal progress, not candidate failure.

## Interpretation ceiling

This gate may settle only whether the pre-existing frozen repository authority selects a Weyl3 dynamical treatment. It does not construct the chosen evolution formulation, establish strong hyperbolicity/well-posedness, count physical modes, prove a ghost or positivity, fix `c6`, authorize `beta=1`, establish quantum unitarity/amplitude/measure, UV completion, full GR recovery, experimental confirmation or new physics.
