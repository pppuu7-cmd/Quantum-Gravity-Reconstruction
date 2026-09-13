# Iter053T — Gauss–Jacobi nodewise pushforward covariance audit

Date: 2026-09-14

## Gate

`ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`

## Motivation and prerequisite

Iter053R is permanently `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION` because its two covariance lanes failed at the integrated weighted-H5 level. Iter053S subsequently established, on its frozen finite pointwise panel, that the implemented numerical `H5=A+I-2 sqrt(-g) D5` obeys the required tensor-density transformation law. Iter053S does not establish the transformed Gauss–Jacobi integration representation.

This gate is prospectively frozen before implementation. It does not rerun or reclassify Iter053R or Iter053S.

## Frozen question

For each of the two determinant-one shears used by Iter053R, and for every tensor-product GJ3 node in the original compact-support parameter cube, does the mapped transformed-frame contraction reproduce the base-frame contraction pointwise before summation?

Let `u` denote the original support parameter, `y=L^{-1}u`, and let the perturbation polynomial factor be `p(u)`. The compared quantities are

- base: `C_base(u) = H_base(u) : p(u)`;
- transformed: `C_tr(y) = H_tr(y) : (L^T p(u) L)`.

The same GJ3 weights are used only to form an additional summed consistency control; the primary scientific predicate is nodewise covariance.

## Frozen panel

- C indices: `0,1` from Iter053R.
- GJ order: `3` in each of 4 dimensions, hence exactly `81` nodes per C index.
- coordinate/double-divergence derivative steps tested independently: `1e-3`, `5e-4`, `2.5e-4`.
- architecture: `2 x 3 = 6` independent matrix lanes, `fail-fast:false`, followed by one aggregate.
- metric/perturbation seeds, support scale, shear matrices, Weyl3/H5 implementation and tensor conventions are inherited unchanged from the already frozen Iter053R/Iter053S code.

## Frozen controls

Each lane must verify:

1. `|det(L)-1| <= 2e-12`;
2. transformed metric algebra residual <= `3e-11` on all tested nodes;
3. all base/transformed metric inverse residuals <= `3e-11`;
4. Lorentzian signature is valid at all tested nodes;
5. all numerical outputs finite;
6. a deliberately wrong congruence `L H L^T` used as the transformed contravariant-density rule must disagree on at least one nontrivial node by `>=1e-3` relative residual, preventing a vacuous covariance pass.

Control failure yields `ITER053T_IMPLEMENTATION_OR_CONTROL_INVALID`, never scientific PASS/FAIL.

## Frozen scientific predicates

For each valid lane:

- maximum nodewise relative contraction residual <= `2e-3`;
- weighted GJ3 sum covariance residual <= `2e-3`;
- at least 70/81 nodes must have `max(|C_base|,|C_tr|) >= 1e-12` so the test is not dominated by numerical zeros.

The aggregate PASS requires all 6 valid lanes to pass.

## Frozen terminal classifications

- `ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED`
- `SCIENTIFIC_FAIL_ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE`
- `ITER053T_IMPLEMENTATION_OR_CONTROL_INVALID`

No threshold may be changed after production results are observed.

## Interpretation lock

A PASS means only that the transformed weighted integrand contraction and its GJ3 pushforward agree nodewise and after the frozen discrete sum for the two tested shears. It would localize the Iter053R failure away from pointwise H5/tensor pushforward and toward some other implementation detail in the full C-lane pipeline. It is not by itself compact-support functional-variation closure.

A scientific FAIL localizes the discrepancy to the mapped quadrature-node representation (including transformation/contraction evaluation) within this finite panel. It is not a global non-covariance theorem for Weyl3.

## Claim locks

`theory established = 0%`; no experimental confirmation; `c6` remains symbolic/unfixed; `beta=1` is not authorized; finite computational panels are not global theorems; no quantum amplitude/measure, unitarity, RG/UV-completion, full-GR-recovery or new-physics promotion is allowed from this gate alone.
