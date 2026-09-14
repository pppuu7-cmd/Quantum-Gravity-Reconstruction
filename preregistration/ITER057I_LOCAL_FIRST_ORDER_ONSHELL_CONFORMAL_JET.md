# Iter057I preregistration — local first-order on-shell conformal jet for Einstein+Weyl3

Date: 2026-09-15
Gate: `ITER057I-LOCAL-FIRST-ORDER-ONSHELL-CONFORMAL-JET-FOR-EINSTEIN-WEYL3`

## Motivation

Iter057H proves that the uncorrected Ricci-flat G3/H0 source is off shell for nonzero `c6` in the two-operator Einstein+Weyl3 truncation. This blocks direct physical interpretation of its mixed symbol as an exact-background characteristic operator.

The next narrow question is whether the obstruction already prevents a **formal local first-order background correction**, or whether one can construct an `O(c6)` metric jet that satisfies the truncated field equation at the frozen point while preserving the pointwise metric/Weyl data needed by the leading symbol calculation.

## Frozen equation and formal expansion

Use only

`A_E G_ab[g] + c6 E_W3_ab[g] = 0`,

with finite nonzero constant `A_E` and symbolic `c6`.

Take the formal series

`g_ab = g0_ab + c6 q_ab + O(c6^2)`,

where `g0` is the source-owned G3/H0 metric and at the frozen origin

`g0=eta`, `Gamma[g0]=0`, `G[g0]=0`.

No convergence of the formal series is assumed or claimed.

## Frozen correction ansatz

Restrict the local first-order correction to a conformal jet

`q_ab = 2 psi g0_ab`,

with

`psi(0)=0`, `partial_a psi(0)=0`,

and a freely chosen symmetric Hessian

`A_ab := partial_a partial_b psi(0)`.

Use a local quadratic representative

`psi(x)=(1/2) A_ab x^a x^b`

only as a jet realization. No claim of a global conformal solution is allowed.

## Frozen obligations

A. Derive the pointwise linearized Einstein tensor for the frozen conformal jet at the G3 origin. PASS requires an exact map

`DG_ab[q](0) = -2 A_ab + 2 eta_ab A^c_c`

in four dimensions, or the convention-equivalent form.

B. Prove/refute that the map from symmetric Hessian `A_ab` to symmetric `DG_ab` is an isomorphism at the point. If invertible, give the exact inverse for arbitrary symmetric target `S_ab`.

C. Apply the inverse to

`S_ab = - E_W3_ab[g0](0) / A_E`

to construct a unique Hessian `A_ab` that solves the total equation through `O(c6)` at the point.

D. Trace consistency: show that the constructed Hessian reproduces the Iter057H trace requirement automatically, without choosing a value of `c6`.

E. Pointwise geometry preservation:

- because `psi(0)=0`, show `q_ab(0)=0`, so the metric value is unchanged at the point;
- because `partial psi(0)=0`, show the connection is unchanged at the point;
- use four-dimensional conformal covariance of the Weyl tensor to show that the pointwise Weyl tensor/mixed Weyl endomorphism is unchanged to first order at the point.

F. Symbol consequence to first formal order:

- the principal Einstein `k2` symbol depends only on the pointwise metric and is unchanged at `O(c6)` by this correction;
- `L4_Weyl3` and `L2_Weyl3` evaluated on the corrected background differ from their `g0` values by `O(c6)`, so after multiplication by the action coefficient `c6` their change enters only at `O(c6^2)`.

Therefore the `O(c6)` derivative-symbol data of the locally corrected jet may use the source `g0` blocks.

G. Interpretation ceiling: explicitly distinguish pointwise/formal jet satisfaction from a solution in an open neighborhood. No Bianchi-integrability, constraint propagation, global solution, convergence, physical treatment selection or hyperbolicity theorem may be inferred.

## Frozen classifications

Maximum PASS:

`PASS_SCOPED_ITER057I_LOCAL_O_C6_CONFORMAL_JET_CANCELS_G3_OFFSHELL_SOURCE_AT_POINT__SOURCE_SYMBOLS_VALID_TO_FIRST_ORDER`.

Scientific FAIL if the conformal Hessian-to-Einstein map is not invertible or cannot cancel a generic symmetric source at the point:

`SCIENTIFIC_FAIL_ITER057I_LOCAL_CONFORMAL_JET_CANNOT_CANCEL_GENERIC_WEYL3_SOURCE`.

INVALID if a global solution, numerical `c6`, additional operator/source, or post-hoc nonconformal correction is introduced.

## Claim locks

This is a formal local jet construction only. It does not select exact vs order-reduced physics, establish a convergent EFT/background expansion, physical characteristics/hyperbolicity, mode/ghost content, stability, unitarity, UV completion or experiment. `c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.