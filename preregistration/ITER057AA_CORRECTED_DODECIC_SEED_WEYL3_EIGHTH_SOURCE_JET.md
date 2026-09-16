# Iter057AA preregistration — corrected dodecic-seed Weyl3 eighth source jet

Status: PROSPECTIVELY FROZEN
Date: 2026-09-16
Gate: `ITER057AA-CORRECTED-DODECIC-SEED-WEYL3-EIGHTH-SOURCE-JET`
Parent seed authority: Iter057Z terminal `bb4fa6ccbf21e2a063467a1b0839223744866995`.
Canonical R12 authority: `5bfe62e887dd627c76c41080187eadc3d95e0c45`.
Parent lower-source authority: Iter057X terminal `4ab5592cfc6ef5fb69d3a96fa4433ef22d51af8b`.

## Question

What is the exact corrected Weyl-cubic Euler source on the canonical dodecic Einstein seed through coordinate degree eight, and does the new degree-eight coefficient obey all exact algebraic/diffeomorphism controls while reproducing every already-authoritative source coefficient through degree six?

This gate computes only the fixed-background Weyl3 Euler source with the overall `c6`/Einstein-normalization factor removed in the same convention as Iter057U/Iter057X. It does not solve the next `O(c6)` metric-response equation.

## Why this gate is now admissible

The Weyl-cubic Euler tensor contains a double covariant divergence of a curvature-quadratic tensor and therefore can depend on four more metric derivatives than the coordinate order of the source coefficient. Iter057Z has now supplied the canonical metric twelve-jet and exact vacuum replay through Einstein coordinate degree ten. Thus source coordinate degree eight is source-owned for the first time.

## Frozen background

Reconstruct exactly the canonical even seed

`eta + G2 + R4 + R6 + R8 + R10 + R12`

from frozen coefficient authorities. No lower seed coefficient may be refit or mutated. Before source reconstruction, require exact inverse identity and Ricci/scalar/Einstein vacuum replay through coordinate degree ten.

## Frozen source definition

Use the same authoritative four-dimensional Weyl-cubic Euler convention and sign as Iter057U/Iter057X. In particular, compute the curvature-cubic invariant `I3`, its exact Riemann derivative `P=dI3/dR`, the algebraic `P.R` insertion and the double-covariant-divergence sector, and form the lower-index Euler tensor/source in exactly the established convention.

The sign/normalization is not free: every nonzero normalized source coefficient at coordinate degrees 0, 2, 4 and 6 must reproduce the canonical Iter057U/Iter057X authority exactly before any degree-eight coefficient is accepted.

## New coefficient space

For the 10 independent symmetric tensor components, the complete coordinate-degree-eight normalized source basis has

`10*C(11,3)=10*165=1650`

possible coefficient slots.

No static, diagonal, conformal, spherical, plane-wave, parity-subselected or other restricted source ansatz is allowed. The actual number of nonzero degree-eight coefficients is not preregistered.

## Frozen obligations

A. Consume the canonical Iter057Z R12 authority exactly and replay the fixed seed through coordinate degree ten: inverse identity, Ricci tensor, scalar curvature and Einstein tensor must all satisfy the terminal Z controls.

B. Recompute the Weyl/Riemann cubic construction from the full dodecic seed, not by extrapolating Iter057X coefficients. Compute all terms needed for the Euler source through coordinate degree eight in exact rational polynomial arithmetic.

C. Verify exact homogeneity/Euler identity

`P.R = 3 I3`

through coordinate degree eight.

D. Verify exact symmetry of the lower-index Euler tensor/source through degree eight and the four-dimensional trace Ward identity

`g^{ab} E_W3,ab = -I3`

through coordinate degree eight.

E. Verify exact covariant Noether identity for the Euler tensor through coordinate degree seven.

F. Replay every canonical normalized Iter057U/Iter057X source coefficient at degrees 0, 2, 4 and 6 exactly, coefficient-by-coefficient, with zero lower-replay mismatches. Because the canonical seed is even, require all odd source degrees 1, 3, 5 and 7 to vanish exactly.

G. Extract the complete normalized coordinate-degree-eight source. Report the total nonzero count, off-diagonal nonzero count and time-containing nonzero count, and freeze every nonzero coefficient in canonical order. Do not infer the degree-eight source from Ward identities or lower-order patterns.

H. Use no floating-point rank/zero test, tolerance, finite difference or numerical fitting. Record a deterministic scientific payload hash before any supplemental production reproduction is used to interpret the result.

I. Preserve the finite-order scope ceiling and all existing physical/quantum claim locks.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057AA_CORRECTED_DODECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_EIGHTH_EVEN_ORDER__O_C6_Q10_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED`

iff A-I all pass exactly and a complete degree-eight source authority is frozen.

This is a deterministic source-reconstruction gate rather than an existence gate. A failed lower replay, Ward/Noether/homogeneity identity, seed-provenance control, normalization/sign control, parity control or exactness control is therefore classified

`INVALID_ITER057AA_SEED_MUTATION_OLD_SOURCE_REUSE_NORMALIZATION_IDENTITY_OR_EXACTNESS_CONTROL_FAILURE`

until an independent exact implementation establishes otherwise.

Technical inability to realize the complete exact construction without changing the frozen problem is

`BLOCKED_ITER057AA_EXACT_WEYL3_EIGHTH_SOURCE_NOT_TECHNICALLY_REALIZED`.

No post-hoc restriction of the coefficient space or relaxation of an exact identity is allowed.

## Consequence of PASS

Only after a PASS may the next response gate be preregistered: an unrestricted pure degree-ten trace-reversed `O(c6)` response `Q10` against the source through coordinate degree eight. Its affine consistency must be tested independently; it is not implied by this source reconstruction.

## Scope ceiling

A PASS would establish only one additional finite local source Taylor layer on one canonical finite-order Einstein seed. It would not establish an all-orders/convergent Einstein+Weyl3 solution, an open-neighborhood/global/asymptotic solution, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
