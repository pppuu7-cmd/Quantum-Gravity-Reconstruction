# Iteration 039 — absolute source/action-phase identifiability after principal refinement closure

Date: 2026-09-12
Status: `PREREGISTERED / READY FOR PRODUCTION`

## Motivation

Iter038 closed the previously conditional G32/G33 principal-refinement regularity mechanism on the
frozen smooth compact realization: the common scaled-residual h=0 torsion Jacobian has exact rank 24
and determinant 11664, all eight finite-range gap bridges passed, and every frozen physical-path and
loop blocking lane passed.

The next blocker is therefore no longer local log choice, finite quadrature, branch regularity, or
fine-to-coarse transport. The unresolved authority is **absolute source/action-phase normalization**.

Already-established inputs are frozen:

- G27: additive primitive event source law has one-dimensional solution space `J(n)=beta*n`; beta is
  not fixed by Boolean composition, path/history normalization, or overlap/serial ratios.
- G28: common-conformal endpoint and on-shell phase ratios are exactly beta-independent; the Weyl^3
  column is exactly zero in that sector.
- G29/G30: QGR has a Weyl-active forward `c6` direction, but no existing microscopic object supplies a
  nonhomogeneous same-realization absolute phase target.
- G31: classical stationarity does not fix an overall quantum action-phase scale.
- G32+G38: the projective local action/refinement mechanism is now regular and constructible on the
  frozen principal compact realization, but no new external datum was introduced.

Iter039 asks whether this remaining normalization can be derived internally from the **existing**
QGR authority, or whether at least one independent absolute matching/calibration datum is
mathematically unavoidable. It also determines the minimal independent datum structure needed to
identify beta and c6 without fitting synthetic controls.

No new physical target, coupling, measured number, or convention is introduced by this gate.

## Frozen unknown coordinates

For phase-identifiability rank calculations use

- `u = beta^2` for the magnitude-sensitive common-conformal on-shell phase sector;
- `c6` for the Weyl-cubic coefficient.

The sign of beta is audited separately because a phase-only datum is even in beta while a signed
absolute source/endpoint datum is linear in beta.

## Audit A — exact homogeneous source-law null direction

Rebuild the G27 additive composition constraint matrix for `J_1...J_8` using exact rational arithmetic.
Add all homogeneous equal-increment/rank-shell constraints and exact scale-free ratio identities used
by G27/G28. PASS requires:

- exact source constraint nullity = 1;
- canonical null ray proportional to `[1,2,...,8]`;
- two distinct nonzero rational beta witnesses satisfy every frozen homogeneous constraint and produce
  identical G28 quotient observables.

Scientific consequence: existing homogeneous source/composition authority fixes the law shape but has
an exact multiplicative scale orbit.

## Audit B — principal refinement/blocking has zero beta authority

Within the frozen G10B/G38 principal conformal realization, the finite torsion residual, principal
connection solve, Jacobian certificate and relational transport blocking depend on the geometry
`Omega`, `C`, and the fixed Lorentz generator basis, not on the primitive source conversion beta.

For six frozen rational beta witnesses per lane, recompute representative G38 principal origin/path
quantities and require numerical equality to a beta-independent reference within `1e-12`.

This is a negative-authority audit only: it tests that the newly closed refinement mechanism did not
silently introduce an absolute event-source normalization.

## Audit C — current absolute-parameter authority rank

Use exact symbolic/rational rank over unknown coordinates `(u,c6)`.

Current authority-bearing data after G38 are frozen as:

- beta-quotiented conformal observables: zero derivative with respect to u and c6 after quotienting;
- principal geometry/refinement controls: zero derivative with respect to u and c6 as absolute phase
  parameters;
- Weyl-active geometry/sensitivity without an absolute target: sensitivity direction exists but adds
  no observation equation.

PASS requires current absolute authority rank = 0 over `(u,c6)`.

This rank statement does not say the forward action is independent of the parameters; it says the
currently authorized **absolute data equations** do not identify them.

## Audit D — minimal calibration-rank theorem

Construct only hypothetical Jacobian rows to determine what *kind* of future genuine datum would be
sufficient. Hypothetical rows are identifiability controls and are not promoted as QGR data.

Frozen target types:

1. one genuine common-conformal absolute phase target:
   `Phi_C = -u*n^2/(4*lambda)`, giving a nonzero u column and zero c6 column;
2. one genuine Weyl-active same-realization absolute phase target with nonzero Weyl-cubic functional
   `W3`, giving a row `[A, W3]` for some finite source-response coefficient A and `W3 != 0`.

PASS requires exact ranks:

- no absolute targets: rank 0;
- conformal absolute target only: rank 1;
- Weyl-active absolute target only: rank 1;
- one conformal + one independent Weyl-active absolute target: rank 2 for `(u,c6)` whenever the frozen
  nonzero coefficients satisfy the preregistered determinant condition.

Scientific consequence if PASS: without some independent absolute normalization datum, neither beta
magnitude nor c6 is internally identifiable from the existing scale-free authority; two independent
absolute phase-equation directions (or one beta calibration plus one Weyl-active phase datum) are the
minimal local rank needed to identify both u and c6.

## Audit E — beta sign authority

Exact controls compare:

- common-conformal phase `S_on = -(beta*n)^2/(4*lambda)`, invariant under `beta -> -beta`;
- signed endpoint/source response `r-1 = beta*n/(2*lambda)`, odd under `beta -> -beta`.

PASS requires exact demonstration that phase-only absolute calibration can at most fix `|beta|`, while
one genuine signed absolute source/endpoint datum with known orientation would fix the sign as well.
Again, this is a minimal-data theorem, not a claim that such a datum has already been derived.

## Production matrix

Five independent audit classes x six frozen rational lanes = **30 exact/numerical authority lanes**,
fail-fast disabled, plus aggregate.

## Terminal classifications

`PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED`
requires all 30 lanes and all frozen rank/nullspace/sign controls to pass.

If PASS, the repository should stop treating beta as an open numerical-computation target. Instead:

- beta remains an explicit calibration/matching parameter unless a new microscopic normalization
  principle is independently derived;
- c6 remains unfixed until a genuine Weyl-active absolute phase datum or equivalent independent
  matching equation exists;
- beta must not be set to 1 and promoted as physics;
- relative beta-quotiented predictions remain valid.

`PARTIAL_OR_CONTROL_INVALID_ABSOLUTE_SCALE_IDENTIFIABILITY_AUDIT`
if any frozen control fails or the exact authority rank differs from the preregistered structure.

## Claim locks

- hypothetical calibration controls are not physical QGR data;
- a no-go under current authority does not prove no future microscopic principle can derive beta;
- beta remains explicit, not silently gauge-fixed to 1;
- c6 remains explicit and unfixed;
- Iter038 principal refinement PASS remains scoped to the frozen smooth compact realization;
- no experimental confirmation;
- theory established remains 0%;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
