# Iter057Q preregistration — sextic c6^0 Einstein-seed completion

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057Q-SEXTIC-EINSTEIN-SEED-COMPLETION`
Parent authority: Iter057O terminal scoped PASS `679a3d73d589fc9161bdf2209f25bb4b7c785fd6`.

## Question

Can the curvature-preserving Iter057O Einstein seed

`g_seed^(4)=g_G3+r^(4)`

be extended by an unrestricted sextic zeroth-order metric jet `r^(6)` so that the full vacuum Einstein tensor vanishes through coordinate degree four, while preserving all already-fixed metric/connection/curvature/four-jet data?

This gate is independent of `c6` and of the Iter057P Weyl3 point-source reset. It is required before any corrected-seed Weyl3 **second coordinate jet** is authoritative, because `E_W3^(2)` can depend on sixth derivatives of the metric.

## Frozen expansion

Use

`g_seed^(6)=g_G3+r^(4)+r^(6)+O(|x|^8)`

with `r^(4)` fixed to the canonical Iter057O pivot solution and `r^(6)` an unrestricted symmetric sextic polynomial.

In trace-reversed form,

`rbar^(6)_ab=(1/6!) R6_ab,cdefgh x^c x^d x^e x^f x^g x^h`,

where `(ab)` is symmetric and the six derivative indices are completely symmetric.

There are `10 * C(9,3) = 840` unrestricted normalized coefficients.

Because the new correction starts at degree six, it preserves the seed metric and all derivatives through degree five at the origin, including the Iter057O origin curvature and four-jet that controls Iter057P.

## Frozen obligations

A. **Exact degree-four residual.** Compute the full nonlinear Einstein tensor of the fixed Iter057O seed through coordinate degree four and extract its complete normalized homogeneous degree-four coefficient set. Verify that degrees zero and two remain exactly zero.

B. **Full sextic generality.** Parameterize all 840 trace-reversed sextic coefficients. No static, diagonal, conformal, spherical, plane-wave or component ansatz is allowed.

C. **Gauge system.** Impose the flat de Donder condition on `rbar^(6)` through homogeneous degree five. Verify the already-fixed G3+quartic seed satisfies the lower-degree linear de Donder conditions.

D. **Exact homogeneous polynomial complex.** Assemble the full source-independent sextic principal map:

- 4 times 56 = 224 degree-five gauge rows;
- 10 times 35 = 350 degree-four Einstein rows;
- 574 total rows against 840 unknowns.

Determine its exact rank/nullspace and its complete Bianchi left-nullspace without numerical tolerance.

E. **Compatibility and solve.** Use the exact degree-four Iter057O residual as the affine RHS. Verify every Bianchi compatibility functional exactly and construct at least one unrestricted exact particular `R6` if consistent.

F. **Independent full-metric substitution.** Substitute the chosen `r^(6)` into `g_G3+r^(4)+r^(6)` and recompute the nonlinear Einstein tensor directly. All components through coordinate degree four must vanish exactly. Reduced/principal self-consistency alone is insufficient.

G. **Jet-preservation lock.** Verify `r^(6)` and all derivatives through order five vanish at the origin. Record explicitly that Iter057P point-source data, which depend only on the seed through the four-jet, are unchanged by the sextic completion.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057Q_SEXTIC_EINSTEIN_SEED_COMPLETES_THROUGH_QUARTIC_EINSTEIN_ORDER__WEYL3_SECOND_SOURCE_JET_CAN_NOW_BE_RECOMPUTED`

iff obligations A-G pass exactly.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057Q_SEXTIC_EINSTEIN_SEED_COMPLETION_INCOMPATIBLE`

only if the full unrestricted exact affine system is inconsistent after its complete Bianchi left-nullspace is accounted for.

BLOCKED:

`BLOCKED_ITER057Q_EXACT_SEXTIC_SEED_SYSTEM_NOT_REALIZED`

if the exact degree-four residual, matrix, or full-metric substitution cannot be completed within the frozen source.

INVALID:

`INVALID_ITER057Q_RESTRICTION_CONVENTION_OR_EXACTNESS_CONTROL`

if a restricted sextic ansatz, numerical rank/zero tolerance, modified quartic seed, `c6`, or an unresolved gauge/convention mismatch is used.

## Scope ceiling

A PASS is still a finite formal vacuum-seed certificate through degree four, not an all-orders Ricci-flat neighborhood or convergence theorem. It only supplies the metric six-jet required to make a corrected-seed Weyl3 second coordinate jet well-defined at the next step.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; no experiment, physical characteristics, hyperbolicity, ghost, stability, unitarity, regulator-removal or UV-completion claim is authorized.