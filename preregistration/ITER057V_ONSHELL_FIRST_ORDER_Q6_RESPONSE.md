# Iter057V preregistration — unrestricted on-shell first-order Q6 response through fourth even order

Status: PROSPECTIVELY FROZEN
Date: 2026-09-15
Gate: `ITER057V-ONSHELL-FIRST-ORDER-Q2-Q4-Q6-RESPONSE`
Parent authorities: Iter057S terminal response `639b0bb33dcb5ea46d54f36b54a8d7dc733421b1`; Iter057T canonical octic Einstein seed `e4d8b960b8694ee166d05aa3ff089999b843e32a`; Iter057U corrected-seed Weyl3 source `20256a1779a3f76c46fcabe9f95cd0dd8c082305`.

## Question

Can the already-fixed unrestricted first-order `O(c6)` response from Iter057S be extended by a completely unrestricted pure degree-six trace-reversed metric jet so that

`DG_ab[qhat] = Shat_ab`

and de Donder gauge hold exactly on the canonical Iter057T Einstein seed through coordinate degree four / gauge degree five, using the consumed Iter057U source through degrees 0,2,4?

Here `qhat_ab := A_E q_ab / c6` is the normalization-factored first-order response and `Shat_ab := A_E S_ab = -E_W3,ab`. No value or sign of `c6` or `A_E` is chosen.

## Frozen lower response and background

1. The canonical Iter057S quadratic and quartic response coefficients are fixed exactly. No homogeneous Q2/Q4 freedom may be changed post hoc.
2. The zeroth-order background is exactly the canonical Iter057T seed, including the consumed quartic, sextic and octic Einstein-completion pivots.
3. The source is exactly the consumed Iter057U degree-0/2/4 corrected-seed source. Historical off-shell G3/M source coefficients are forbidden.
4. The Iter057S degree-0/2 field equation and gauge result must replay exactly before the new degree-four solve is trusted.

## Frozen new coefficient space

Extend the trace-reversed response by

`delta qbar_ab^(6) = sum_{|alpha|=6} Q6_ab[alpha] x^alpha/alpha!`.

All 10 symmetric tensor components and all degree-six four-variable monomials are included. There are

`10 * C(9,3) = 840`

unknown normalized Q6 coefficients.

No static, diagonal, conformal, spherical, plane-wave or other symmetry restriction is authorized.

## Frozen affine system

The pure degree-six correction enters the requested orders only through the flat principal trace-reversed operator:

- de Donder degree five: `4*C(8,3)=224` equations;
- field equation degree four: `10*C(7,3)=350` equations.

Thus the complete unrestricted principal matrix has frozen shape

`574 x 840`.

The curved Iter057T background and already-fixed Iter057S Q2/Q4 response contribute only to the exact affine RHS at these requested orders; they may not be absorbed into a changed principal matrix or fitted normalization.

The canonical Bianchi/de Donder compatibility complex has 80 degree-three vector-monomial relations. Therefore the source-independent principal matrix controls are prospectively frozen as

- exact rank `494`;
- exact left-nullity `80`;
- exact nullity `346`.

These structural values do **not** preregister consistency: PASS still requires `rank([M|r])=494` and all 80 exact compatibility contractions to vanish for the actual Iter057U/Iter057T affine RHS.

## Frozen obligations

A. Consume/replay the canonical Iter057S Q2/Q4 response exactly, including its degree-0/2 source match and de Donder controls.

B. Consume/replay the canonical Iter057T background and verify the lower seed coefficients are unchanged; the pure Q6 response must not mutate zeroth-order seed data.

C. Consume the full Iter057U degree-0/2/4 source with deterministic basis accounting and require its exact Noether divergence through degree three.

D. Independently compute the exact degree-four residual of the full covariant linearized Einstein operator on the Iter057T seed with fixed Q2/Q4 **before** adding Q6. No historical affine RHS may be transplanted.

E. Assemble the complete unrestricted `574 x 840` Q6 affine system in normalized Taylor arithmetic. Numerical tolerance/rank is forbidden.

F. Verify exact `rank(M)=494`, left-nullity `80`, nullity `346`, and a complete 80-dimensional canonical Bianchi compatibility basis annihilating `M`.

G. Require `rank([M|r])=rank(M)` and every one of the 80 compatibility contractions with the actual affine RHS to vanish exactly for PASS.

H. If consistent, construct at least one exact particular Q6 solution, report its nonzero coefficient count, and verify the exact affine residual is zero. Homogeneous freedom remains unfixed and must be reported as nullity 346.

I. Independently substitute the combined canonical Q2/Q4/Q6 response into an unreduced covariant linearized Ricci/scalar/Einstein construction on the full canonical Iter057T seed and require `DG_ab[qhat]-Shat_ab=0` exactly through coordinate degree four in all ten independent components.

J. Independently evaluate the full covariant de Donder vector and require exact zero through coordinate degree five.

K. Verify that the pure Q6 extension preserves the already-established response/source match through degree two and does not change lower response derivatives.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057V_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_FOURTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN`

iff A-K pass exactly.

Scientific FAIL:

`SCIENTIFIC_FAIL_SCOPED_ITER057V_UNRESTRICTED_Q6_RESPONSE_AFFINE_SYSTEM_INCOMPATIBLE`

only if the complete unrestricted exact affine system is inconsistent after the full 80-dimensional Bianchi/Noether compatibility space is accounted for, with an exact contradiction witness (`rank([M|r])>rank(M)` and/or a nonzero exact left-null contraction).

BLOCKED:

`BLOCKED_ITER057V_EXACT_UNRESTRICTED_Q6_RESPONSE_SYSTEM_NOT_TECHNICALLY_REALIZED`

if the frozen full-background degree-four residual, complete affine system, or independent unreduced replay cannot be technically realized without weakening the problem.

INVALID:

`INVALID_ITER057V_LOWER_RESPONSE_MUTATION_OLD_SOURCE_RESTRICTED_ANSATZ_NUMERICAL_EXACTNESS_OR_CONTROL_FAILURE`

if Q2/Q4 are changed post hoc, an old source/RHS is reused, the coefficient space is restricted, a fitted normalization or numerical rank/zero is used, or a mandatory replay/control fails.

## Scope ceiling

A PASS would establish only one additional finite local first-order `O(c6)` Taylor layer through source/field degree four. It would not establish an all-orders or convergent Einstein+Weyl3 background, an open-neighborhood/global solution, boundary/asymptotic completion, a physical value or sign of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghost/stability claims, quantum unitarity, regulator removal, UV completion, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed; theory established remains `0%`.
