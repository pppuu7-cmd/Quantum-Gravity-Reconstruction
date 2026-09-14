# Iter057J preregistration — open-neighborhood first-order Einstein+Weyl3 background continuation

Date: 2026-09-15
Gate: `ITER057J-OPEN-NEIGHBORHOOD-FIRST-ORDER-BACKGROUND-CONTINUATION`

## Motivation

Iter057F3 establishes the full-tensor-normalized off-shell Weyl3 `L2` block on the source-owned G3/H0 origin. Iter057H proves the uncorrected G3/H0 background is off shell for nonzero `c6`, while Iter057I shows that a conformal Hessian jet can cancel the Weyl3 source at one point through first order in symbolic `c6`.

The next question is whether that pointwise jet is compatible with an actual first-order correction on an open neighborhood. This must be decided before promoting the mixed derivative operator to physical characteristics.

## Frozen equation

Use only the classical truncation

`A_E G_ab[g] + c6 E_W3_ab[g] = 0`,

with finite nonzero `A_E` and symbolic/unfixed `c6`, and the formal expansion

`g_ab = g0_ab + c6 q_ab + O(c6^2)`.

At first order the required equation is

`A_E DG_ab[q] + E_W3_ab[g0] = 0`.

No numerical value/sign of `c6` may be chosen.

## Frozen conformal continuation candidate

First test the exact continuation of the Iter057I source-owned ansatz

`q_ab = 2 psi g0_ab`.

On the Ricci-flat source background, the linearized Einstein response is

`DG_ab[2 psi g0] = -2 nabla_a nabla_b psi + 2 g0_ab box psi`.

Define

`S_ab := -E_W3_ab[g0]/A_E`, `S := g0^{ab} S_ab`,

and the required Hessian tensor

`H_ab := g0_ab S/6 - S_ab/2`.

A conformal continuation exists only if there is a scalar `psi` on an open neighborhood with

`nabla_a nabla_b psi = H_ab`.

## Frozen obligations

A. Verify the first-order conformal Einstein-response formula covariantly on the source background.

B. Compute/derive the Hessian integrability obstruction for `H_ab`. At minimum evaluate the covariant curl condition implied by a scalar Hessian,

`nabla_c H_ab - nabla_a H_cb = R_ca b{}^d nabla_d psi`,

and determine whether a compatible gradient one-form can exist locally. A pointwise zero-gradient specialization may be used only at the frozen origin, not as an open-neighborhood proof.

C. Use the source-owned G3/H0 local background and the already-authorized covariant Weyl3 Euler tensor; no third symmetry reduction and no fitted surrogate source is allowed.

D. If the conformal continuation fails, classify it as failure of this **conformal continuation candidate only**, not failure of all first-order background corrections. The successor would have to test the general symmetric-tensor equation `DG[q]=S` with gauge/constraint control.

E. If the conformal continuation passes, require an explicit local construction or exact compatibility certificate on an open neighborhood, not merely a pointwise Hessian match.

F. Preserve source-symbol accounting: any conclusion about the Iter057F3 operator on a corrected background is only first-order in symbolic `c6`; no all-orders physical characteristic claim is permitted.

## Frozen classifications

Maximum PASS:

`PASS_SCOPED_ITER057J_CONFORMAL_O_C6_BACKGROUND_CONTINUATION_EXISTS_LOCALLY__PHYSICAL_CHARACTERISTICS_STILL_NOT_ESTABLISHED`.

Scientific FAIL for the conformal candidate if an exact nonzero integrability obstruction is found:

`SCIENTIFIC_FAIL_SCOPED_ITER057J_CONFORMAL_FIRST_ORDER_BACKGROUND_CONTINUATION_OBSTRUCTED__GENERAL_QAB_REMAINS_OPEN`.

BLOCKED if the current source representation cannot evaluate the required covariant derivative/integrability object without introducing new unfrozen geometry.

INVALID if a numerical/fitted `c6`, post-hoc source modification, third repetitive symmetry reduction, or unpreregistered treatment selector is introduced.

## Claim locks

Theory established remains `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no physical Weyl3 treatment selector; no strong-hyperbolicity, ghost, stability, unitarity, regulator-removal or UV-completion claim; KMQGB `NEW_REQUIRED` remains unauthorized.
