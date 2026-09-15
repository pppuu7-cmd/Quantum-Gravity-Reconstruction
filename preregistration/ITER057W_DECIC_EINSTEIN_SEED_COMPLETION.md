# Iter057W preregistration — unrestricted decic Einstein-seed completion

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057W-DECIC-EINSTEIN-SEED-COMPLETION`
Parent seed authority: Iter057T terminal `e4d8b960b8694ee166d05aa3ff089999b843e32a`.
Latest first-order response authority: Iter057V terminal `0d98273f8a1ec6071692571518f4faec1af8fa7b`.

## Question

Can the canonical zeroth-order Einstein seed be extended by a completely unrestricted pure degree-ten metric jet so that the exact vacuum Einstein tensor vanishes through coordinate degree eight, while preserving every already-fixed seed derivative through order nine?

This gate concerns only the `c6^0` Einstein seed. It does not alter, fit, sign-select or run `c6`, and it does not yet compute the Weyl3 source at coordinate degree six.

## Why this gate is next

The Weyl3 Euler source contains two covariant derivatives of an object quadratic in curvature. A source coefficient at coordinate degree six can therefore depend on the background metric ten-jet. Iter057T fixes the canonical seed only through the octic metric layer / Einstein degree six. The decic seed layer must be fixed before a source-degree-six reconstruction can be source-owned.

## Frozen correction space

Add a pure normalized degree-ten symmetric metric correction

`delta g_ab^(10) = sum_{|alpha|=10} U10_ab[alpha] x^alpha/alpha!`,

with all 10 symmetric tensor components and all degree-ten four-variable multi-indices included.

The unrestricted coefficient count is

`10*C(13,3) = 2860`.

No static, diagonal, conformal, spherical, plane-wave or other restricted ansatz is allowed.

## Frozen homogeneous complex

At the new target layer the pure degree-ten trace-reversed correction contributes through the flat principal polynomial complex:

- de Donder degree nine: `4*C(12,3) = 880` rows;
- Einstein degree eight: `10*C(11,3) = 1650` rows;
- total: `2530` rows;
- columns: `2860`.

The canonical Bianchi compatibility family is indexed by four vector components times degree-seven monomials:

`4*C(10,3) = 480`.

Accordingly the source-independent structural controls are prospectively frozen as

- exact rank `2050`;
- exact left-nullity `480`;
- exact nullity `810`.

These counts/ranks do not preregister affine consistency for the actual degree-eight residual.

## Frozen obligations

A. Replay exactly the canonical Iter057T quartic, sextic and octic seed coefficients and require the already-established vacuum Einstein cancellation through coordinate degree six.

B. Compute directly the full exact coordinate-degree-eight Einstein residual of that fixed seed before adding any decic correction. It may not be inferred from lower equations or a fitted model.

C. Assemble the complete unrestricted exact affine system for all 2860 degree-ten coefficients in normalized Taylor arithmetic. Numerical rank/tolerance is forbidden.

D. Verify the complete `2530 x 2860` principal matrix, exact rank `2050`, left-nullity `480`, nullity `810`, and a complete rank-480 canonical Bianchi compatibility basis annihilating the matrix.

E. Require `rank([M|r])=rank(M)=2050` and all 480 exact compatibility contractions with the actual degree-eight residual to vanish for PASS.

F. If consistent, construct at least one exact particular decic correction, report its nonzero coefficient count, retain all 810 homogeneous directions as unfixed freedom, and require the exact affine residual to vanish in every row.

G. Independently substitute the completed metric into the unreduced nonlinear Levi-Civita/Ricci/scalar/Einstein construction and require all ten independent Einstein components to vanish exactly through coordinate degree eight.

H. Verify that the pure degree-ten correction preserves all canonical seed coefficients/derivatives through order nine and therefore does not mutate the already-consumed Iter057T/Iter057U lower local data.

I. Record the finite-order scope ceiling explicitly and keep all physical/quantum claim locks unchanged.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057W_DECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_EIGHT__HIGHER_SEED_ORDERS_REMAIN_OPEN`

iff A-I pass exactly.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057W_UNRESTRICTED_DECIC_EINSTEIN_SEED_SYSTEM_INCOMPATIBLE`

only if the complete unrestricted exact affine system is inconsistent after the full 480-dimensional Bianchi compatibility space is accounted for, with an exact augmented-rank or left-null contradiction witness.

BLOCKED:

`BLOCKED_ITER057W_EXACT_DECIC_EINSTEIN_SYSTEM_NOT_TECHNICALLY_REALIZED`

if the exact degree-eight residual/system or independent nonlinear replay cannot be realized without changing the frozen problem.

INVALID:

`INVALID_ITER057W_RESTRICTED_ANSATZ_LOWER_SEED_CHANGE_NUMERICAL_EXACTNESS_OR_CONTROL_FAILURE`

if lower canonical seed coefficients are changed, a restricted ansatz is generalized, numerical zero/rank is used, or a mandatory replay/control fails.

## Scope ceiling

A PASS would establish only one further finite zeroth-order local Taylor coefficient layer. It would not establish an all-orders or convergent Einstein seed, an open-neighborhood/global/asymptotic solution, the Weyl3 source degree-six coefficient by itself, a higher `O(c6)` response layer, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed; theory established remains `0%`.
