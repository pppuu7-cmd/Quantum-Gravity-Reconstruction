# Iter057N preregistration — G3/H0 zeroth-order Einstein-seed neighborhood audit

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057N-G3-ZERO-ORDER-EINSTEIN-SEED-NEIGHBORHOOD-AUDIT`
Parent authority: Iter057M terminal scoped PASS `f947efac35e5093ec536ee9da52e86de23325d72`.

## Motivation

Iter057L and Iter057M establish exact source-compatible first-order `c6` correction jets at the frozen G3/H0 origin through the first two even source orders. Both results explicitly stop short of an open-neighborhood solution.

Before spending compute on a Q6/higher-`c6` correction jet, audit a more basic perturbative requirement: the seed `g0` in

`g = g0 + c6 q + O(c6^2)`

must satisfy the `c6^0` Einstein equation on the same local neighborhood/order being claimed. The G3/H0 metric was constructed as a weak static tidal source and is exactly Ricci-flat at the origin, but nonlinear inverse/connection effects can generate Ricci/Einstein coefficients away from the origin even though the potential is harmonic and quadratic.

An `O(c6)` correction cannot cancel an `O(c6^0)` Einstein residual without introducing inverse powers of `c6`, which are outside the frozen formal expansion.

## Frozen source

Use only the exact source-owned G3/H0 metric

`Phi=(kappa/2)(x^2+y^2-2z^2)`,

in either globally equivalent signature presentation, with symbolic nonzero `kappa` and no added matter/cosmological/operator term.

No continuum replacement, fitted coefficient, or new symmetry reduction is allowed.

## Frozen obligations

A. Compute the exact Levi-Civita Ricci tensor, scalar curvature and Einstein tensor of the exact G3/H0 metric through coordinate degree two about the frozen origin.

B. Verify the already-authorized origin statements exactly: `R_ab(0)=0`, `R(0)=0`, `G_ab(0)=0`.

C. Extract all normalized quadratic coefficients of `G_ab[g0]` and verify the contracted Bianchi identity through the corresponding first nontrivial order.

D. Independently cross-check at least one nonzero/zero coefficient family either by a second symbolic implementation, direct exact expansion of the full rational metric, or an exact invariant/contraction identity. Numerical finite differences may not decide exact zero.

E. State the perturbative consequence correctly. A nonzero `c6^0` coefficient obstructs interpreting `g0+c6 q+...` as an open-neighborhood solution with the **fixed G3 seed**, but it does not invalidate the local operator/source probes, the pointwise/finite-jet Iter057L/M certificates, or the existence of some separately corrected Einstein seed.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057N_FIXED_G3_SEED_EINSTEIN_THROUGH_QUADRATIC_ORDER__HIGHER_SEED_ORDERS_REMAIN_OPEN`

iff every exact quadratic Einstein coefficient vanishes and all controls pass.

Scientific FAIL of the fixed-seed neighborhood programme:

`SCIENTIFIC_FAIL_SCOPED_ITER057N_FIXED_G3_SEED_HAS_NONZERO_C6_ZERO_ORDER_EINSTEIN_RESIDUAL__SEED_CORRECTION_REQUIRED_BEFORE_OPEN_NEIGHBORHOOD_C6_SERIES`

iff any exact quadratic coefficient of `G_ab[g0]` is nonzero after controls.

BLOCKED:

`BLOCKED_ITER057N_EXACT_G3_EINSTEIN_SECOND_JET_NOT_REALIZED`

if the exact second jet cannot be evaluated without changing the frozen source.

INVALID:

`INVALID_ITER057N_SOURCE_CONVENTION_OR_EXACTNESS_CONTROL`

if a fitted/numerical zero test, modified source, fixed `c6`, added matter/operator, or unresolved curvature convention is used to decide the gate.

## Scope ceiling

A FAIL would concern only the **fixed G3/H0 seed as the `c6^0` neighborhood background**. It would not say that no nearby Ricci-flat/Einstein seed exists, nor that Einstein+Weyl3 is inconsistent. It would instead force the next constructor programme to separate a zeroth-order Einstein-seed completion from the later `O(c6)` Weyl3 correction.

A PASS through quadratic order would still be a finite local certificate, not a full neighborhood theorem.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; no experimental, hyperbolicity, ghost, stability, unitarity, regulator-removal or UV-completion claim is authorized.