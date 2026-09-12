# QGR Iter038 — principal compact refinement regularity and actual fine-to-coarse blocking

Date: 2026-09-12
Status: `PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING`

## Reproducibility

Authoritative GitHub Actions run: `34709394158`.

- head: `ae8f365ea1ad9e92cdeaed8fefa81a9f05e152d9`
- frozen scientific lanes: **29** + aggregate
- aggregate job: `103595441181`
- aggregate artifact: `10303065332`
- aggregate digest: `sha256:26bf51ad50a90cc42b8ee92ba997a237df25aa82dc0ffedeb538170d9997a432`

## Frozen aggregate result

All preregistered lanes passed:

- exact small-h certificate: **1/1**;
- finite-range compact-domain gap bridge: **8/8**;
- actual fixed-physical-path fine blocking: **8/8**;
- elementary loop/groupoid fine blocking: **12/12**.

Exact common scaled-residual h=0 torsion Jacobian:

- rank: **24**;
- determinant: **11664**;
- numerical minimum singular value: `0.3742889790499052`.

Finite-range bridge over the frozen compact domain samples:

- minimum observed principal torsion-Jacobian singular value: `0.3117043266205393`;
- maximum observed condition number: `18.83979439212241`.

Fine-to-coarse blocking:

- maximum final path contraction ratio: `0.5053863019927789`;
- maximum final loop contraction ratio: `0.5080076341318422`.

## Scientific interpretation

This gate is materially stronger than a finite numerical refinement scan. After writing the
identity-connected finite torsion root as `z=h w`, the derivative of the scaled residual with respect
to `w` at `h=0` is the same exact 24x24 matrix throughout the frozen smooth conformal realization.
Its exact nonzero determinant provides genuine finite-dimensional implicit-function-theorem authority.
Together with analyticity and compactness of `K=[0,1]^4`, this gives a **uniform sufficiently-small-h
principal identity-connected branch and positive local torsion-Jacobian gap on this frozen smooth
compact realization**.

The independently preregistered finite-range bridge then connects the numerically explored interval to
that analytic small-h regime, while the physical-path and loop streams test the actual G10B
fine-product/blocking construction rather than the earlier coordinate shrinking proxy.

Therefore the G32 projective-refinement action mechanism no longer needs an unsupported uniform-
regularity assumption **within this scoped principal smooth compact realization**. The regularity and
actual transport/groupoid blocking mechanism required for that scoped construction is now supplied by
Iter038.

## What this does not establish

- no arbitrary-background/global field-space compactness theorem;
- no optimal global `h0` bound;
- no proof that QGR is the correct quantum-gravity theory;
- no absolute quantum phase/source normalization;
- no derivation of `beta`;
- no fixation of `c6`;
- no experimental confirmation.

## Consequence for the roadmap

The principal-branch refinement/regularity blocker on the frozen smooth compact realization is closed
at scoped authority. The next main-line question should not be another regularity grid. It is whether
the remaining absolute source/action-phase scale `beta` (and any physically relevant combination with
`c6`) is internally identifiable from existing QGR primitives after refinement closure, or whether an
independent calibration/matching datum is mathematically required.

## Claim locks

- theory established remains **0%**;
- distant G35–G37 algebraic roots remain nonphysical under current frozen G10B evidence;
- no physical branch weights/measures are authorized;
- Iter038 authority is scoped to the frozen smooth compact realization;
- `beta=1` remains unauthorized;
- absolute quantum phase normalization remains unfixed;
- `c6` remains unfixed;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
