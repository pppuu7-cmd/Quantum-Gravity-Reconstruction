# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter040`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD`
Active roadmap stage: `principal refinement closure -> absolute-scale no-go -> calibration-free Weyl-active predictions -> end-to-end parameterized model contract -> independent matching/validation`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter039 completion: **100%**
- Iter040 completion: **PRODUCTION ACTIVE**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Projective refinement-limit action mechanism: **PASS_SCOPED on frozen principal smooth compact realization after G38**
- Principal identity/refinement-connected connection: **PASS_SCOPED / G10B physical branch rule**
- Principal compact-domain small-h uniform regularity: **PASS_SCOPED (G38)**
- Actual principal fixed-path/loop fine-to-coarse blocking: **PASS_SCOPED (G38)**
- Finite nonlinear torsion equation multiplicity: **VERIFIED_SCOPED (G35–G37)**
- Additional physical connection branches from strongest distant roots: **NOT SUPPORTED UNDER FROZEN G10B (G37C)**
- Absolute source normalization `beta`: **EXPLICIT MATCHING/CALIBRATION PARAMETER UNDER CURRENT AUTHORITY (G39)**
- Current absolute authority rank on `(beta^2,c6)`: **0 (G39)**
- Minimal local rank for `(beta^2,c6)` identification: **2 independent absolute directions (G39)**
- Physical Weyl-active same-realization finite absolute phase target: **NOT DERIVED**
- Calibration-free Weyl^3 response manifold: **ACTIVE G40**
- `c6` fixed: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter038 terminal — principal refinement regularity and actual blocking
Authoritative run `34709394158`, head `ae8f365ea1ad9e92cdeaed8fefa81a9f05e152d9`, aggregate job `103595441181`, artifact `10303065332`, digest `sha256:26bf51ad50a90cc42b8ee92ba997a237df25aa82dc0ffedeb538170d9997a432`.

Classification: `PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING`.

All **29/29** frozen scientific lanes passed. Exact common scaled-residual h=0 torsion Jacobian has rank **24**, determinant **11664**, and numerical minimum singular value `0.3742889790499052`. Analyticity plus compactness of frozen `K=[0,1]^4` supplies a uniform sufficiently-small-h principal identity-connected IFT branch/gap on this scoped smooth realization; physical-path and loop fine-blocking streams independently passed.

Record: `results/ITER038_PRINCIPAL_REFINEMENT_REGULARITY_AND_BLOCKING.md`.

## Iter039 terminal — absolute source/action-phase identifiability
Authoritative run `34709657749`, head `15cedcd3507f0223dc50827a2f72e3d0762ec901`, aggregate job `103596064182`, artifact `10302389728`, digest `sha256:11d4f47b32e269573e491d06d188d1ee90da92a9f5000377876e498d037b23e3`.

Frozen outcome: all **30/30** authority lanes passed.

Classification: `PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED`.

Exact/scoped conclusions under current authorized QGR inputs:
- source-scale nullity = **1**;
- current absolute identifying rank on `(u=beta^2,c6)` = **0**;
- G38 principal refinement/blocking outputs are exactly beta-blind in the frozen audit (`max difference = 0.0` across dummy beta witnesses);
- one genuine absolute datum supplies rank 1;
- independent common-conformal + Weyl-active absolute directions supply rank 2;
- phase-only calibration is even in beta and can at most determine `|beta|`; a signed absolute source/endpoint datum is needed for its sign.

Decision: stop treating beta as an internally missing numerical root. Keep beta explicit as a matching/calibration parameter unless a genuinely new microscopic normalization principle is independently derived. Do not set `beta=1` and promote the convention as physics. Keep c6 explicit/unfixed until a genuine independent Weyl-active absolute phase or equivalent matching equation exists.

Record: `results/ITER039_ABSOLUTE_SCALE_IDENTIFIABILITY.md`.

## Active gate — Iter040
`QGR-ITER040-CALIBRATION-FREE-WEYL3-RESPONSE-MANIFOLD`.

Preregistered before production in `status/ITERATION_040.md`.
Production workflow: `qgr-iter040-weyl-response`.
Production run: `34709914980`, launch head `b990644250a4df7d29ddec467629c56956fd83e9`.

No beta/c6 fitting is allowed. The gate generalizes the existing G10 same-field-content weak static vacuum tidal witness to four frozen trace-free Hessian shapes and proper spatial rotations, while retaining c6 only as an overall unknown multiplier of the Weyl^3 response kernel.

Frozen response tests:
1. **A / refinement-null-sign:** four tidal shapes, including a nonzero-Weyl profile with zero cubic tidal trace and a sign-reversed pair;
2. **B / amplitude law:** three nonzero-cubic shapes, checking Weyl ~ kappa and Weyl^3 ~ kappa^3;
3. **C / shape-ratio universality:** tests whether `W3/tr(H^3)` approaches a common discretization-independent factor across nonzero shapes;
4. **D / rotational recovery:** four frozen orientations of H0, testing recovery of normalized cubic response under proper spatial rotations toward refinement;
5. **E / exact prediction table:** six exact control lanes proving c6 cancels from response ratios/nulls and beta does not enter pure Weyl^3 kernel ratios.

Total **20 scientific lanes** + aggregate. Full PASS classification is `PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED`.

## Strongest positive result
The scoped principal model now has a mathematically supported refinement mechanism and an exact characterization of what cannot be internally normalized. This cleanly separates structural predictions from matching parameters instead of hiding calibration freedom inside conventions.

## Strongest blocker
`CALIBRATION_FREE_WEYL_ACTIVE_PREDICTION_STRUCTURE_AND_THEN_END_TO_END_PARAMETERIZED_MODEL_CLOSURE`.

Even if G40 passes, absolute Weyl-active phase amplitude remains proportional to unfixed c6 and no experiment/matching datum is invented.

## Claim locks
- theory established `0%`;
- beta is explicit matching/calibration parameter under current G39 authority; `beta=1` is not physics;
- c6 remains unfixed;
- G40 response-kernel ratios are not absolute quantum phases;
- G38 authority remains scoped to the frozen smooth compact principal realization;
- G35–G37 distant algebraic roots do not authorize physical branch weights under current G10B evidence;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
