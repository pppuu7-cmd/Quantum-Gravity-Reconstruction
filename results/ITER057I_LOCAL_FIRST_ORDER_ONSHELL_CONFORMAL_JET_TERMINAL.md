# Iter057I terminal result — local first-order on-shell conformal jet

Date: 2026-09-15
Gate: `ITER057I-LOCAL-FIRST-ORDER-ONSHELL-CONFORMAL-JET-FOR-EINSTEIN-WEYL3`
Prospective preregistration: `53bd47d2b21d25dfa212bfb46c81a681bb827969`
Derivation: `a6e9663bc32fcf4fcdaaa95133c7b7bf6e3f7bdb`

## Terminal classification

**`PASS_SCOPED_ITER057I_LOCAL_O_C6_CONFORMAL_JET_CANCELS_G3_OFFSHELL_SOURCE_AT_POINT__SOURCE_SYMBOLS_VALID_TO_FIRST_ORDER`**

## Exact local construction

For the formal background series

`g=g0+c6 q+O(c6^2)`

on the frozen G3/H0 origin, choose

`q_ab=2 psi g0_ab`,

with `psi(0)=partial psi(0)=0` and arbitrary symmetric Hessian

`A_ab=partial_a partial_b psi(0)`.

At the point,

**`DG_ab[q]=-2 A_ab+2 eta_ab A`**, `A=eta^{ab}A_ab`.

This ten-dimensional symmetric Hessian-to-Einstein-response map is an isomorphism. For any symmetric target `S_ab`,

**`A_ab=eta_ab S/6-S_ab/2`.**

Taking

`S_ab=-E_W3_ab[g0]/A_E`

therefore produces a unique conformal Hessian jet satisfying

`A_E DG_ab[q]+E_W3_ab[g0]=0`

at the point through first order in symbolic `c6`.

No numerical value/sign of `c6` is used.

## Trace consistency

The construction automatically satisfies Iter057H. Since `trace E_W3=-I3`,

`A=I3/(6 A_E)`,

so

`A_E trace(DG[q])=I3`

cancels `trace(E_W3)=-I3` exactly.

Thus the earlier trace obstruction is a real obstruction to the uncorrected Ricci-flat G3 source, but it does not forbid a formal local first-order corrected jet.

## Pointwise source-symbol preservation

Using the quadratic representative `psi=(1/2)A_ab x^a x^b` gives at the origin

`q=0`, `partial q=0`.

Therefore the pointwise metric and connection are unchanged through the relevant first order. The correction is conformal, so the four-dimensional Weyl tensor at the point is unchanged in the conformal-weight sense when `psi(0)=0`; the Ricci sector changes through the Hessian and supplies the required cancellation.

Consequently:

- the Einstein principal `k2` symbol at the point is unchanged at `O(c6)`;
- changes of background-dependent Weyl3 `L4`/`L2` coefficients are `O(c6)` and enter the total operator only multiplied by the action coefficient `c6`, hence at `O(c6^2)`.

Therefore the source blocks being reconstructed by Iter057F3 are also the correct derivative-symbol coefficients for this **formal pointwise on-shell jet through first order in `c6`**.

## Interpretation ceiling

This is not a solution on an open neighborhood and not a convergence theorem for a background expansion. Higher-point compatibility, Bianchi/integrability, constraints, boundary conditions and all-orders continuation remain open.

It does not select exact versus order-reduced physics and does not establish a physical characteristic cone, hyperbolicity, modes/ghosts, stability, unitarity or UV completion.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.