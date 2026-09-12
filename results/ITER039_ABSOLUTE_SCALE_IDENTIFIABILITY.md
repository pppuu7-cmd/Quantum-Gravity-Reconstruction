# QGR Iter039 — absolute source/action-phase identifiability after refinement closure

Date: 2026-09-12
Status: `PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED`

## Reproducibility

Authoritative GitHub Actions run: `34709657749`.

- head: `15cedcd3507f0223dc50827a2f72e3d0762ec901`
- frozen authority matrix: **30 lanes** + aggregate
- aggregate job: `103596064182`
- aggregate artifact: `10302389728`
- aggregate digest: `sha256:11d4f47b32e269573e491d06d188d1ee90da92a9f5000377876e498d037b23e3`

## Frozen aggregate result

All preregistered audits passed in all six lanes:

- exact homogeneous source-null audit: **6/6**;
- G38 refinement beta-blind negative-authority audit: **6/6**;
- current absolute-parameter authority-rank audit: **6/6**;
- minimal calibration-rank theorem: **6/6**;
- beta-sign authority audit: **6/6**.

Aggregate facts:

- source-scale nullity: **1**;
- current absolute authority rank on `(u=beta^2,c6)`: **0**;
- rank supplied by one genuine absolute target: **1**;
- rank supplied by independent common-conformal + Weyl-active absolute targets: **2**;
- maximum G38 output difference across dummy beta witnesses: **0.0**.

## Scientific interpretation

The remaining `beta` is not a number that can be recovered by more numerical solution of the currently
authorized QGR equations. G27's additive source law has an exact one-dimensional scale orbit
`J(n)=beta*n`; G28's quotient observables remove that scale exactly; and G38's principal refinement
regularity/blocking mechanism contains no hidden beta authority. Closing the projective refinement
regularity problem therefore does not generate a missing absolute source normalization.

For current authorized absolute data equations, the local identifiability rank over `(beta^2,c6)` is
zero. This does **not** mean the forward QGR action is independent of those parameters. It means there
is presently no genuine absolute datum/equation in the repository that can infer their values.

The exact minimal-data rank audit shows:

- one genuine common-conformal absolute phase datum can constrain the `beta^2` direction but not c6;
- one genuine Weyl-active absolute phase datum supplies only one equation in the two-dimensional
  `(beta^2,c6)` space unless beta is independently calibrated;
- one independent beta calibration plus one Weyl-active phase datum, or two independent absolute
  phase directions with nonzero determinant, supplies local rank 2;
- phase-only calibration is even in beta and can fix at most `|beta|`; a signed absolute source/endpoint
  datum with an orientation convention is required to fix the sign.

## Decision

Under the current QGR authority:

- **stop searching beta numerically** as if it were an internally missing root;
- retain beta explicitly as a matching/calibration parameter unless a genuinely new microscopic
  normalization principle is independently derived;
- do not set `beta=1` and promote that convention as physics;
- retain c6 explicitly and unfixed until a genuine independent Weyl-active absolute phase/matching
  equation exists;
- preserve G28 beta-quotiented relative predictions as valid scoped predictions.

## Claim locks

- this is a no-go under current authorized QGR inputs, not a theorem forbidding future microscopic
  normalization principles;
- hypothetical calibration rows used in the rank proof are not physical data;
- beta remains explicit and unfixed;
- c6 remains explicit and unfixed;
- theory established remains **0%**;
- no experimental confirmation;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.

## Next gate

Build a same-realization Weyl-active **parameterized prediction manifold** rather than fitting beta or
c6. Identify beta-free / calibration-free combinations, determine whether multiple Weyl-active probes
can isolate c6 relative to a source calibration, and localize the minimal experimental/matching datum
needed for an actual numerical prediction.
