# Iter057AO — covariant Weyl^3 directional-variation certificate

Status: **PROSPECTIVELY FROZEN — no production outcome inspected**

## Purpose

Move beyond repeated symmetry reductions/background accumulation. Test the source-level metric variation of

`S6[g] = c6 * integral d^4x sqrt(-g) C_{ab}{}^{cd} C_{cd}{}^{ef} C_{ef}{}^{ab}`

with `c6` symbolic/unfixed.

This gate does **not** assume AF/AM/AN obstruction coefficients, parity support, S3 structure, or their witness as an acceptance target.

## Frozen scientific object

For a compactly supported symmetric test direction `h_ab`, construct the first directional derivative

`D_h S6[g] = d/d eps S6[g + eps h] | eps=0`

source-faithfully from the metric, Levi-Civita connection, Riemann/Ricci/scalar curvature and Weyl definition in four dimensions. Keep `c6` symbolic. No symmetry-reduced ansatz is permitted in the derivation.

Two algebraic representations are allowed only if related by exact canonicalization/integration by parts: (A) raw directional derivative containing derivatives of `h`; (B) Euler-Lagrange form `integral sqrt(-g) E6^{ab} h_ab` plus a total divergence.

## Frozen controls

1. Exact `eps`-linearity at first order; no numerical differentiation.
2. Exact metric symmetry `h_ab=h_ba`.
3. Exact Weyl trace controls before and after variation.
4. Exact diffeomorphism/Noether control: for a compactly supported gauge direction `h_ab = nabla_a xi_b + nabla_b xi_a`, the directional derivative must reduce to a boundary/divergence term; equivalently the bulk Euler-Lagrange representative must satisfy the corresponding covariant divergence identity wherever the symbolic backend can certify it.
5. Exact constant-curvature control: Weyl=0 implies the cubic density and its first variation vanish.
6. Exact conformally-flat control on at least one nontrivial four-dimensional metric with nonconstant conformal factor: Weyl=0 and first variation of the cubic functional vanishes.
7. Exact cross-backend or independently coded replay of at least one nonzero generic directional certificate before terminal PASS.
8. No floating tolerances in scientific classification.

## Frozen nonzero test assignment

The implementation must define a deterministic generic polynomial/rational metric jet and compactly supported-formal symmetric direction from a fixed literal seed string `ITER057AO-COVARIANT-WEYL3-V1`; its manifest and SHA256 must be emitted before evaluating the Weyl^3 directional derivative. Any singular/noninvertible generated jet is skipped only by a deterministic predeclared invertibility rule, never by the scientific outcome.

At least one held-out direction must be generated from literal seed `ITER057AO-COVARIANT-WEYL3-HELDOUT-V1` and may not be used to tune canonicalization or integration-by-parts rules.

## Terminal classification

`PASS_SCOPED_ITER057AO_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED` only if all frozen exact controls pass, the generic nonzero directional derivative is independently replayed, and the held-out direction passes without refit.

`SCIENTIFIC_FAIL_ITER057AO_*` if a frozen exact identity/control is violated by a source-faithful completed computation.

`BLOCKED_ITER057AO_*` if expression growth/backend limitations prevent completion without changing the frozen scientific object. BLOCKED is not scientific FAIL.

## Claim firewall

Even PASS is a scoped covariant directional-variation certificate for the classical Weyl^3 functional. It is not by itself a proof of quantum unitarity, regulator removal, UV completion, experimental confirmation, or correctness of QGR. It does not fix `c6`, authorize `beta=1`, turn finite local panels into global theorems, or authorize KMQGB `NEW_REQUIRED`.
