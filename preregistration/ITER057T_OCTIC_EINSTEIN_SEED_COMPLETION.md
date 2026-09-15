# Iter057T preregistration — unrestricted octic Einstein-seed completion

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057T-OCTIC-EINSTEIN-SEED-COMPLETION`
Parent authority: Iter057Q canonical quartic+sextic Einstein seed `c4f1c5c01205a6991e7215e3824111e1f36d1436`; Iter057S terminal first-order response `639b0bb33dcb5ea46d54f36b54a8d7dc733421b1`.

## Question

Can the canonical zeroth-order Einstein seed be extended by an unrestricted pure degree-eight metric jet so that the exact vacuum Einstein tensor vanishes through coordinate degree six, while preserving all already-fixed seed derivatives through order seven?

This gate concerns only the `c6^0` Einstein seed. It does not alter or fit `c6`, and it does not yet compute the next Weyl3 source order.

## Frozen correction space

Add a pure normalized degree-eight symmetric metric correction

`delta g_ab^(8) = sum_{|alpha|=8} U_ab[alpha] x^alpha/alpha!`,

with all 10 symmetric tensor components and all degree-eight four-variable multi-indices included. No static, diagonal, spherical, conformal, plane-wave or other restricted ansatz is allowed.

## Frozen obligations

A. Replay exactly the canonical Iter057O quartic and Iter057Q sextic seed coefficients and verify the previously established Einstein cancellation through coordinate degree four.

B. Compute the full exact degree-six Einstein residual of that fixed seed before adding the octic correction. Do not infer it from lower-order equations.

C. Assemble the unrestricted exact affine system for all octic coefficients using normalized Taylor arithmetic. Numerical rank/tolerance may not decide consistency.

D. Compute exact rank and augmented rank. Compute the complete left-null compatibility space and require every exact Bianchi compatibility contraction to vanish for PASS.

E. If consistent, construct at least one exact particular octic correction and retain/report the homogeneous nullity. No post-hoc change to the lower quartic/sextic canonical pivots is allowed.

F. Independently substitute the completed metric into the unreduced nonlinear Ricci/scalar/Einstein construction and require all ten independent Einstein components to vanish exactly through coordinate degree six.

G. Verify that the pure degree-eight correction preserves the metric/connection/curvature and all already-fixed seed derivatives at lower orders required by prior gates.

H. Record the finite-order scope ceiling explicitly.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057T_OCTIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_SIX__HIGHER_SEED_ORDERS_REMAIN_OPEN`

iff A-H pass exactly.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057T_UNRESTRICTED_OCTIC_EINSTEIN_SEED_SYSTEM_INCOMPATIBLE`

only if the complete unrestricted exact affine system is inconsistent after the full Bianchi compatibility space is accounted for.

BLOCKED:

`BLOCKED_ITER057T_EXACT_OCTIC_EINSTEIN_SYSTEM_NOT_REALIZED`

if the exact degree-six source/operator system or independent nonlinear replay cannot be realized without changing the frozen problem.

INVALID:

`INVALID_ITER057T_RESTRICTED_ANSATZ_LOWER_SEED_CHANGE_NUMERICAL_EXACTNESS_OR_CONTROL_FAILURE`

if lower canonical seed coefficients are changed post hoc, a restricted ansatz is generalized, numerical zero/rank is used, or the independent nonlinear replay fails.

## Scope ceiling

A PASS would establish only one further finite zeroth-order local Taylor coefficient layer. It would not establish an all-orders or convergent Einstein seed, an open-neighborhood/global solution, the next Weyl3 source coefficient by itself, the next `O(c6)` response layer, physical characteristics, strong hyperbolicity, ghost/stability claims, quantum unitarity, regulator removal, UV completion, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; KMQGB `NEW_REQUIRED` remains unauthorized.