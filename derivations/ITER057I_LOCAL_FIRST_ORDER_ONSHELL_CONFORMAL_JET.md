# Iter057I derivation — local first-order on-shell conformal jet

Date: 2026-09-15
Gate: `ITER057I-LOCAL-FIRST-ORDER-ONSHELL-CONFORMAL-JET-FOR-EINSTEIN-WEYL3`
Prospective preregistration: `53bd47d2b21d25dfa212bfb46c81a681bb827969`

## 1. Formal expansion and pointwise data

Consider the frozen two-operator equation

`A_E G_ab[g] + c6 E_W3_ab[g] = 0`,

with finite nonzero `A_E` and symbolic `c6`.

At the G3/H0 origin the source metric `g0` satisfies

`g0_ab=eta_ab`, `Gamma[g0]=0`, `G_ab[g0]=0`.

Take the formal series

`g_ab = g0_ab + c6 q_ab + O(c6^2)`

with the frozen conformal jet

`q_ab = 2 psi g0_ab`,

`psi(0)=0`, `partial_a psi(0)=0`,

`A_ab := partial_a partial_b psi(0)`.

Because `q(0)=0`, all background-curvature-times-`q` terms in the pointwise linearized Einstein tensor vanish at the frozen point. Because `Gamma[g0](0)=0`, the derivative calculation reduces there to the normal-coordinate flat-form principal expression.

## 2. Linearized Einstein map for the conformal Hessian

In four dimensions, for `h_ab=2 psi eta_ab`,

`h = eta^{ab}h_ab = 8 psi`,

`h^c_b = 2 psi delta^c_b`.

At the point, with `A_ab=partial_a partial_b psi`,

`delta R_ab`

`= (1/2)[ partial_c partial_a h^c_b + partial_c partial_b h^c_a - box h_ab - partial_a partial_b h ]`

`= -2 A_ab - eta_ab A`,

where

`A := eta^{ab} A_ab`.

The scalar variation is

`delta R = -6 A`.

Therefore

**`DG_ab[q](0) = -2 A_ab + 2 eta_ab A`.**

This is the frozen map required by the preregistration.

## 3. Exact invertibility

Let an arbitrary symmetric target tensor `S_ab` be given and require

`-2 A_ab + 2 eta_ab A = S_ab`.

Taking the trace gives

`6 A = S`,

with `S=eta^{ab}S_ab`. Hence

`A=S/6`.

Substitution yields the unique inverse

**`A_ab = eta_ab S/6 - S_ab/2`.**

Thus the ten-dimensional symmetric conformal Hessian jet maps isomorphically onto the ten-dimensional symmetric pointwise Einstein response tensor.

The word “conformal” here does not mean one scalar degree of freedom at a fixed Fourier covector: the local Hessian of one scalar at a point is an arbitrary symmetric 4x4 tensor and therefore has ten independent jet components.

## 4. Cancellation of the Weyl3 source through O(c6)

Expand the total equation:

`A_E [ G[g0] + c6 DG[q] ] + c6 [ E_W3[g0] + O(c6) ] = O(c6^2)`.

Since `G[g0](0)=0`, the order-`c6` condition is

`A_E DG_ab[q](0) + E_W3_ab[g0](0) = 0`.

Set

`S_ab = -E_W3_ab[g0](0)/A_E`.

The unique Hessian is therefore

**`A_ab = E_W3_ab[g0]/(2 A_E) - eta_ab E_W3[g0]/(6 A_E)`**, 

where `E_W3[g0]=eta^{ab}E_W3_ab[g0]`.

Using Iter056X,

`E_W3[g0] = -I3[g0]`,

this can also be written

`A_ab = E_W3_ab[g0]/(2 A_E) + eta_ab I3[g0]/(6 A_E)`.

No value or sign of `c6` has been chosen; `c6` is the formal expansion parameter multiplying the already-fixed Hessian jet.

## 5. Trace consistency with Iter057H

From the inverse map,

`A = S/6 = -E_W3[g0]/(6 A_E) = I3[g0]/(6 A_E)`.

The trace of the order-`c6` Einstein correction is

`A_E * eta^{ab}DG_ab = A_E * 6A = I3[g0]`.

The Weyl3 trace is

`eta^{ab}E_W3_ab = -I3[g0]`.

Hence they cancel exactly:

`A_E trace(DG[q]) + trace(E_W3[g0]) = I3 - I3 = 0`.

So the construction satisfies the exact Iter057H trace obstruction automatically rather than evading it by a coefficient choice.

## 6. Pointwise metric, connection and Weyl preservation

Choose the local quadratic representative

`psi(x)=(1/2) A_ab x^a x^b`.

Then at the origin

`psi=0`, `partial psi=0`.

Therefore

`q_ab(0)=0`,

`partial_c q_ab(0)=0`.

Thus the corrected metric and its connection agree pointwise with the source metric through first order in `c6`:

`g_corr(0)=g0(0)`,

`Gamma[g_corr](0)=Gamma[g0](0)=0`.

Moreover the correction is precisely the first-order form of a conformal rescaling

`g_corr = exp(2 c6 psi) g0 + O(c6^2)`.

In four dimensions the Weyl tensor with one index raised is conformally invariant. At the frozen point `psi(0)=0`, so the all-lowered/mixed representations also have the same pointwise value through `O(c6)`:

**`C[g_corr](0) = C[g0](0) + O(c6^2)` pointwise in the conformal-weight sense relevant to the frozen value.**

The Ricci sector changes because it depends on the Hessian of the conformal factor; this is exactly what cancels the Weyl3 Euler source.

## 7. First-order derivative-symbol consequence

The Einstein principal `k2` symbol at a point depends on the pointwise inverse metric, not on the background curvature. Since `q(0)=0`,

`M2_E[g_corr](0,k) = M2_E[g0](0,k) + O(c6^2)`

at the order relevant to the formal `c6` expansion.

The Weyl3 blocks `L4_W3` and `L2_W3` are background-dependent coefficients. The correction changes their background curvature/coefficient jets by `O(c6)`. Since the action multiplies the entire Weyl3 Euler operator by `c6`,

`c6 Lm_W3[g_corr] = c6 Lm_W3[g0] + O(c6^2)`

for `m=4,2`.

Therefore the derivative-symbol data through first formal order in `c6` are exactly the source-block data being reconstructed in Iter057F3:

`M_deriv = M2_E[g0] + c6 [L2_W3[g0] + L4_W3[g0]] + O(c6^2)`

with the understood powers of the wave covector attached to each homogeneous block.

This is a first-order formal statement only; it is not an all-orders background solution or treatment selection.

## 8. What remains unsolved

The construction satisfies the field equation at **one point through first order**. It does not establish:

- a solution in an open neighborhood;
- compatibility of the chosen Hessian jet with higher-point equations;
- Bianchi/integrability or constraint propagation for a completed local solution;
- convergence of the formal `c6` series;
- a global/physical asymptotic or boundary condition;
- an exact-vs-order-reduced physical treatment choice;
- hyperbolicity, mode/ghost content, stability, unitarity or UV completion.

The pointwise existence result is nevertheless sufficient to show that the Iter057H trace obstruction does not by itself prevent a formal local `O(c6)` on-shell jet.

## Frozen obligation disposition

- A conformal Einstein map: **SATISFIED**.
- B invertibility and exact inverse: **SATISFIED**.
- C cancellation of arbitrary symmetric Weyl3 source tensor at point: **SATISFIED**.
- D trace consistency: **SATISFIED**.
- E pointwise metric/connection/Weyl preservation: **SATISFIED through first formal order**.
- F source derivative-symbol validity through O(c6): **SATISFIED**.
- G local/formal interpretation ceiling: **PRESERVED**.
