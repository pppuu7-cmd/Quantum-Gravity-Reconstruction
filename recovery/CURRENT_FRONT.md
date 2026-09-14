# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `Iter054H / refinement-domain conditional order-reduction derivation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 DYNAMICAL TREATMENT CONSTRUCTION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Complete mixed-order evolution reduction: **not established**.
- Pre-existing authority selecting exact vs order-reduced Weyl3 dynamics: **absent after fail-closed source review**.
- Quantum amplitude/measure transition: **not authorized**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID/BLOCKED results are immutable.

## Iter054F — TERMINAL BLOCKED

Classification: **`BLOCKED_OBJECT_DEFINITION_ITER054F_MIXED_ORDER_EVOLUTION_REDUCTION_NOT_FIXED`**.

Authoritative retry run `34817585523`; aggregate `103892887023`; summary artifact `10336467977`; digest `sha256:2ff9d546b8443080fc48c6cf27c2c0b0764b7686b72aff2e53735e7d1bb8a27f`.

All eight ingredients needed for a QGR-specific strong-hyperbolicity evolution object remained unresolved: state/reduction variables, time/spatial split, evolution formulation, principal evolution matrix, gauge evolution, constraint propagation, symmetrizer/norm/open region, and map back to mixed Einstein+Weyl3 with GR limit.

## Iter054G parent — TERMINAL SOURCE REVIEW REQUIRED

Gate: `ITER054G-WEYL3-DYNAMICAL-TREATMENT-SELECTION-AUTHORITY`.

- preregistration `b4730d02f66b9378c41313bb833e2fdedd62daae`
- frozen source snapshot `3398cd5a195d3d6b05fad01715ab5b79a880c4f1`
- run `34818484127`
- aggregate `103894668345`
- summary artifact `10337630463`
- digest `sha256:9e7cee1882ec13faddb8734a7c203f4eeb228381a3f56381c09c6a2c971e34f7`
- parent classification **`REQUIRES_SOURCE_AUTHORITY_REVIEW_ITER054G`**

The explicitly mapped core sources returned `EXACT_NOT_SELECTED` and `ORDER_REDUCED_NOT_SELECTED`. The parent stopped fail-closed because a repo-wide census found eight additional treatment-keyword paths.

Durable note: `results/ITER054G_PARENT_SOURCE_REVIEW_REQUIRED.md`.

## Iter054G-R — TERMINAL BLOCKED after 8-source review

Gate: `ITER054G-R-UNEXPECTED-DYNAMICAL-TREATMENT-SOURCE-AUTHORITY-REVIEW`.

- preregistration `f9973884ce8e994c347f0ee5412fdc25206875ee`
- implementation `41ca0a8ef7c7c7b1e8bf55a858f5bf2797fed685`
- workflow head `9195320ca9060cb7e2874ae1fd5923e4afbecc9d`
- run `34818909992`
- aggregate `103895733649`
- summary artifact `10336563789`
- summary digest `sha256:0880ebc3d1a817bddfbaca358f017aeca3dc040367f70710f27c97395f4108c5`
- classification **`BLOCKED_OBJECT_DEFINITION_ITER054G_WEYL3_DYNAMICAL_TREATMENT_NOT_SELECTED_AFTER_SOURCE_REVIEW`**

All eight unexpected frozen sources were independently reviewed and classified `NON_SELECTOR`; there were no missing, ambiguous, invalid or selector-positive lanes.

Durable note: `results/ITER054G_R_TERMINAL_RESULT.md`.

Scientific consequence: the missing treatment rule is now a genuine model-definition/construction blocker, not an incomplete repository search. Existing QGR authority does not already select exact finite-`c6` higher-derivative dynamics or perturbative/order-reduced dynamics.

## New constructive route / Iter054H

The next highest-information step is to ask whether the already-established QGR refinement hierarchy itself can derive a **conditional low-resolution/order-reduction domain**, without pretending that such a domain was pre-existing authority.

Relevant established structure:

- Iter009 operator census identifies the first nonredundant Ricci-flat parity-even local correction as
  `S6 = a_cont * c6 * h^4 * integral(Weyl^3)`;
- this correction is formally `O(h^4)` / `O(Gamma^2)`;
- no exact higher-derivative finite-cell UV action has been frozen;
- the regular weak-curvature microscopic branch and one-particle refinement limit are controlled locally;
- a regular per-cell `c6 O(h^4)` contribution accumulates as `O(c6 T h^3) -> 0` at fixed macroscopic interval;
- Iter054A proves that exact singular characteristic branches are non-analytic in the small higher-derivative coefficient and lie outside a finite Taylor branch unless separately justified.

For an Einstein `k^2` principal term plus a Weyl-active correction scaling schematically as `c6 h^4 Cbar k^4`, define the dimensionless control parameter

`chi = |c6| h^2 |Cbar|`.

On a resolved band `q=|k|h <= q_max`, the correction/Einstein principal ratio scales as `rho <= chi q_max^2`, while the singular proxy branch obeys `q_HD ~ chi^(-1/2)` up to the frozen eigenchannel normalization/sign convention.

The prospectively frozen Iter054H gate must determine exactly what follows from this scaling and what still does not:

1. derive/check the dimensionless ratio and branch/band separation algebraically;
2. include positive controls with `chi << 1` and negative controls with `chi >= 1`;
3. audit whether existing QGR refinement authority supplies a physical bound/domain on `chi`, an all-orders/remainder control, and a derived resolved-band definition sufficient to promote the conditional statement to a treatment selector;
4. if only the conditional inequality is derivable, classify it as a scoped conditional bridge while retaining treatment selection BLOCKED;
5. do not infer an order-reduced physical theory merely because the singular branch is outside a chosen toy band.

Only a later separately authorized evolution construction can reopen strong-hyperbolicity testing.
