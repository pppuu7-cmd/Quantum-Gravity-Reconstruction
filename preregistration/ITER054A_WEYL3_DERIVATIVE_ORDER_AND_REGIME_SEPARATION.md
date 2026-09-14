# Iter054A preregistration — Weyl3 derivative-order and dynamical-regime separation

Freeze date: 2026-09-14

Gate: `ITER054A-WEYL3-DERIVATIVE-ORDER-AND-REGIME-SEPARATION`

## Purpose

Establish the first QGR-specific dynamical-treatment bookkeeping layer after Iter053U. This gate does **not** count physical modes, prove ghosts, prove stability, establish hyperbolicity, or authorize quantum amplitude/measure work.

The gate asks two narrower questions prospectively:

1. For a local metric action algebraic in curvature and cubic in Weyl, is the generic metric Euler-Lagrange differential order consistent with fourth order rather than a naive sixth-order count based only on operator mass dimension?
2. When a nonzero higher-derivative principal coefficient is present on a Weyl-active background, are exact extra characteristic roots non-analytic in the small symbolic coefficient and therefore outside a finite-order perturbative/order-reduced branch unless separately justified?

## Frozen streams

### A0 — exact jet-order census

Use exact SymPy differentiation for one-dimensional jet representatives whose Lagrangian depends on `q''` but not on derivatives above `q''`.

Primary cubic representative: `L=(q'')^3`. Compute the higher-derivative Euler-Lagrange expression exactly. PASS requires:

- highest derivative of `q` in the Euler-Lagrange expression is exactly order 4;
- coefficient of `q''''` is nonzero for generic `q''`;
- negative control `L=(q''')^2` has Euler-Lagrange order 6, demonstrating the detector distinguishes curvature-algebraic from derivative-of-curvature structure.

Interpretation: structural derivative-order audit only; the scalar jet is not a replacement for the full tensor theory.

### A1 — generic curvature-component cubic ensemble

Construct at least 12 exact rational cubic polynomials `F(r1,r2,r3)` and affine curvature-component maps `ri = ai q'' + bi q' + ci q` with prospectively fixed rational coefficients/seeds. For every nondegenerate sample compute the exact higher-derivative Euler-Lagrange expression.

PASS requires:

- no sample exceeds derivative order 4;
- at least 10/12 samples have nonzero `q''''` coefficient;
- exact-zero/degenerate cases, if any, are reported rather than discarded.

### B0 — background-activation audit

For the cubic representative and ensemble, linearize the Euler-Lagrange expression about `q=q0+eta*v` and extract the coefficient multiplying `v''''` at first order in `eta`.

PASS requires:

- for the cubic representative the `v''''` coefficient is proportional to the background second-derivative/curvature variable and vanishes on the zero-curvature control;
- at least one nonzero-curvature rational background gives a nonzero coefficient;
- no claim is made that flat-background linearization constrains Weyl-active backgrounds globally.

### B1 — exact-vs-perturbative root separation

Use exact symbolic algebra on the schematic principal polynomial `P(z,eps)=z*(a0 + eps*a1*z)` with `a0 != 0`, `a1 != 0`, where `z` stands only for a squared characteristic scale after gauge/sector reduction.

PASS requires:

- roots are exactly `z=0` and `z=-a0/(eps*a1)`;
- the second root is singular/non-analytic as `eps -> 0`;
- a finite Taylor ansatz `z=sum_{n=0}^N c_n eps^n` connected to the GR root does not reproduce the singular root;
- controls with `a1=0` contain no extra root.

Interpretation: this is a regime-separation statement only. It does not assign physical norm, residue, stability, ghost status, or weight to the extra exact root.

## Frozen aggregate rule

`PASS_SCOPED_ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION` only if A0, A1, B0 and B1 all PASS with exact arithmetic/controls valid. Otherwise classify the failing scientific condition explicitly; technical exceptions are infrastructure/numerical failures and are not scientific FAIL.

## Claim locks

Even full PASS means only:

- Weyl3 is treated as a curvature-cubic local operator whose generic metric Euler-Lagrange structure should be audited as fourth-order, not called sixth-order merely from mass dimension;
- exact and perturbative/order-reduced dynamical regimes must remain distinct;
- Weyl-active principal coefficients can vanish on special backgrounds, so flat/null linearizations are insufficient for global mode claims.

It does **not** establish the complete covariant Weyl3 EOM, well-posedness, hyperbolicity, physical mode count, ghosts, unitarity, positivity, UV completion, `c6`, `beta=1`, experimental confirmation, or new physics.

No thresholds or interpretation rules may be weakened after outputs are seen.