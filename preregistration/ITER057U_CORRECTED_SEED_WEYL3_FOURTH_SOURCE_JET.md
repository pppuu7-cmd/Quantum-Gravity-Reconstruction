# Iter057U preregistration — corrected-seed Weyl3 fourth source jet

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057U-CORRECTED-SEED-WEYL3-FOURTH-SOURCE-JET`
Parent authority: Iter057T terminal octic Einstein-seed PASS `e4d8b960b8694ee166d05aa3ff089999b843e32a`; Iter057R corrected Weyl3 source through degree two `e395d2fb4be3e6f556f893ce63ae68f3b4b51ea2`.

## Question

What is the exact Weyl3 Euler source on the canonical Einstein-completed seed through coordinate degree four, and does it satisfy the exact algebraic/Noether controls needed before any unrestricted `O(c6)` sixth-order correction gate may be opened?

Define

`Shat_ab := A_E S_ab := -E_W3,ab[g_seed]`.

No value or sign of `c6` or `A_E` is chosen. `c6` remains symbolic/unfixed.

## Frozen source authority

Use exactly the canonical corrected seed consisting of the already-authorized lower seed plus the canonical Iter057O quartic, Iter057Q sextic, and Iter057T octic Einstein-completion corrections. No post-hoc homogeneous seed freedom may be changed.

The octic seed authority is sufficient for this gate by frozen degree counting:

`metric degree 8 -> curvature/Weyl degree 6 -> P degree 6 -> D^2 P and E_W3 degree 4`.

No historical off-shell G3 Weyl3 coefficient may be substituted for the corrected seed.

## Frozen object / unrestricted output space

Compute the full symmetric tensor source `Shat_ab` in four dimensions through coordinate degree four.

The output space is unrestricted: all ten independent symmetric tensor components and every normalized coordinate monomial of total degree 0, 1, 2, 3, and 4 are represented before exact parity/identity simplification. Time-containing, mixed and off-diagonal coefficients are mandatory if nonzero. No static, diagonal, conformal, spherical, plane-wave or other symmetry ansatz is authorized.

Because this is a source-extraction gate rather than an affine correction solve, the matrix-rank criterion is prospectively frozen as **not applicable**. Any scientific classification based on a fitted coefficient solve or numerical rank in this gate is INVALID. The next response gate must preregister its own full coefficient space and exact rank/augmented-rank/nullspace criteria.

## Frozen exact construction

Use exact rational/symbolic polynomial algebra only. Construct from the canonical seed:

1. inverse metric to the order required for source degree four;
2. connection, Riemann, Ricci, scalar curvature and Weyl tensor through the required order;
3. the authorized Weyl-cubic scalar `I3` and projected `P^{abcd}` lineage;
4. covariant double divergence and the already-authorized Euler-tensor normalization;
5. `E_W3,ab` and `Shat_ab=-E_W3,ab` through coordinate degree four.

No finite-difference, floating-point, numerical tolerance or fitted normalization may decide an exact-zero statement.

## Frozen controls / compatibility witnesses

All of the following are mandatory:

A. Replay the canonical Iter057T seed and verify exact inverse identity through the required order.

B. Verify corrected-seed Ricci, scalar and Einstein tensors vanish through coordinate degree six, matching Iter057T authority.

C. Verify the exact algebraic identity `P.R = 3 I3` through the order needed for this source extraction.

D. Verify Euler-tensor symmetry `E_W3,ab=E_W3,ba` through coordinate degree four.

E. Verify the exact trace Ward identity through coordinate degree four in the same convention used by the authorized lineage.

F. Verify exact covariant Noether divergence through coordinate degree three, which is the compatibility witness for a degree-four symmetric source.

G. Verify parity directly: all odd normalized source coefficients through degree three vanish if implied by the canonical even seed; this may not be assumed before computation.

H. Independently replay the complete Iter057R corrected source at degree zero and degree two, including all time-containing/off-diagonal coefficients. Any mismatch is INVALID, not a new scientific result.

I. Export the complete normalized degree-four source coefficients, including zeros only through a deterministic full-basis accounting or an equivalent canonical sparse representation with an explicit basis count.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057U_CORRECTED_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_FOURTH_EVEN_ORDER__O_C6_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED`

iff the complete corrected-seed source through degree four is exposed and controls A-I pass exactly.

Scientific FAIL:

No standalone scientific FAIL is authorized merely because particular source coefficients are nonzero. This gate extracts the source; it does not test existence of the next metric correction.

BLOCKED:

`BLOCKED_ITER057U_EXACT_CORRECTED_SEED_WEYL3_FOURTH_SOURCE_NOT_TECHNICALLY_REALIZED`

if the required exact source or mandatory controls cannot be realized without changing the frozen object, lineage, seed or exactness requirements.

INVALID:

`INVALID_ITER057U_OLD_SOURCE_SEED_MUTATION_RESTRICTED_ANSATZ_NORMALIZATION_OR_EXACTNESS_CONTROL`

if historical off-shell source coefficients are reused, the canonical seed is changed post hoc, a restricted ansatz is generalized, a new/fitted normalization is introduced, numerical zero/rank is used, lower-order replay fails, or any frozen control is weakened after evidence is seen.

## Interpretation ceiling

A PASS is only a finite corrected-seed Weyl3 source certificate through coordinate degree four. It does not establish that the next `O(c6)` correction exists, any higher-order series, convergence/open-neighborhood existence, global/asymptotic boundary data, physical characteristics, hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, UV completion, experiment, or QGR correctness.

Historical FAIL/BLOCKED results remain preserved. `c6` remains symbolic/unfixed. `beta=1` remains unauthorized. Finite certificate != theorem; classical != quantum; diagnostic != closure; theory established remains `0%`.
