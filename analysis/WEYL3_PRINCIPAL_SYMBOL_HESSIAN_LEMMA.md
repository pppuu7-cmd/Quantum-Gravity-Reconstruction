# Analytic lemma — principal high-frequency structure of the Weyl^3 correction

Date: 2026-09-14

Status: analytic dependency/control lemma. Not a scientific gate and not a claim that the full QGR corrected equations are established.

## Scope

This note concerns only the **highest-derivative part of the linearization** of a metric action term

`S6 = c6 ∫ sqrt(-g) I3(C)`,

where locally the cubic Weyl invariant can be viewed schematically as

`I3(C) = Tr(C^3)`

on the appropriate bivector/Weyl-operator representation. `c6` remains symbolic.

It assumes a future authoritative full metric variation has established the exact lower-index conventions and complete field equation. This lemma does not replace that dependency.

## 1. EFT derivative counting versus PDE differential order

`C` contains two derivatives of the metric. The local scalar `C^3` is therefore a six-derivative EFT operator in the usual derivative-counting sense.

However, the metric Euler-Lagrange equation of a curvature-only Lagrangian `L(g,Riemann)` has the schematic form

`E_ab = algebraic(P*R)_ab - 1/2 g_ab L - 2 nabla nabla P |_ab`,

where

`P = ∂L/∂Riemann`.

For `L ~ C^3`, `P ~ C^2`. Since curvature already contains second metric derivatives, `nabla nabla P` generically contains up to **four derivatives of the metric**. Thus the corrected PDE is generically fourth order, not sixth order, even though the action operator is called six-derivative in EFT counting.

A future characteristic analysis should therefore look for a quartic-in-covector high-frequency correction to the two-derivative symbol.

## 2. Curvature Hessian of the cubic invariant

At fixed background metric, regard `C` as an endomorphism on the Weyl/bivector space and let `D` be a curvature-direction perturbation. Then

`I3(C+tD) = Tr(C^3) + 3 t Tr(C^2 D) + 3 t^2 Tr(C D^2) + t^3 Tr(D^3)`.

Hence

`d I3[C](D) = 3 Tr(C^2 D)`,

and

`d^2 I3[C](D,D) = 6 Tr(C D^2)`.

For two independent directions,

`d^2 I3[C](D1,D2) = 3 Tr(C(D1 D2 + D2 D1))`.

The key structural fact is that the curvature Hessian is **linear in the background Weyl tensor/operator C**, not in the scalar value `Tr(C^3)`.

## 3. Consequence for the principal quadratic action

For a high-frequency metric perturbation `h_ab ~ exp(i k·x)`, the derivative-carrying part of the linearized Weyl tensor scales schematically as

`delta C_principal ~ Projector(gbar) · (k k h)`.

The four-derivative part of the quadratic action from `C^3` is therefore schematically

`delta^2 S6 |_k4 ~ c6 sqrt(-gbar) Tr(Cbar · delta C_principal · delta C_principal)`.

Equivalently, the corrected linearized Euler-Lagrange principal symbol receives a quartic contribution

`P4(k; gbar, Cbar) ~ c6 * Cbar * k^4`

with the precise tensor projector/gauge structure to be derived from the authoritative full field equation.

Metric/measure/projector variations with no derivatives on one perturbation can generate lower-order `k^0` or `k^2` pieces, but they do not replace this curvature-Hessian `k^4` structure.

## 4. Safe and unsafe null inferences

### Conformally flat background

If `Cbar = 0`, the curvature Hessian above vanishes. Therefore the cubic Weyl term has no `k^4` contribution arising from this Hessian on an exactly conformally-flat background. This is the structurally clean null control for the future highest-derivative symbol.

### Type-N / pp-wave background

A type-N background may have

`Tr(Cbar^2)=0`, `Tr(Cbar^3)=0`

while `Cbar != 0`.

Therefore scalar-invariant blindness (`W2=W3=0`) does **not** imply

`d^2 I3[Cbar] = 0`.

The bilinear form `Tr(Cbar D^2)` can be nonzero for suitable perturbation directions even when the background scalar `I3(Cbar)` vanishes. Consequently a type-N pp-wave must **not** be preregistered as a null control for the corrected principal symbol solely from Iter047's scalar `W3=0` result.

Instead it is a valuable algebraic-class probe whose exact symbol may be degenerate, nonzero, or direction-dependent and must be computed.

### Petrov-D Schwarzschild and Kasner

Their nonzero background Weyl makes them natural Weyl-active principal-symbol witnesses. Nonzero background `W3` is sufficient to show the cubic scalar is active, but the principal-symbol criterion itself is the background Weyl/Hessian, not the scalar `W3` value.

## 5. Future gate implications

After, and only after, an authoritative full corrected metric equation exists, a prospective characteristic gate should:

1. formulate the full gauge-reduced symbol as a polynomial containing the known two-derivative part plus the quartic `c6` correction;
2. keep `c6` symbolic and test rank/branch structure rather than choosing a preferred numerical sign/value post hoc;
3. use conformally-flat `Cbar=0` as the clean high-derivative null control;
4. treat Schwarzschild/Petrov-D, Kasner and type-N as distinct nonzero-Weyl algebraic classes;
5. explicitly search for covectors/polarizations where the quartic piece changes rank or creates extra physical branches;
6. distinguish a finite-background certificate from a theorem of global hyperbolicity.

## 6. Scientific consequence of the lemma

The post-Iter053 stability question is sharper than “does Weyl^3 activate where W3 != 0?”. It is:

**what is the gauge-reduced quartic principal symbol generated by the curvature Hessian of the cubic Weyl operator on nonzero-Weyl backgrounds, and does it introduce physically unacceptable characteristic branches or hyperbolicity defects?**

This is a future dependency, not a current PASS/FAIL.

## Claim ceiling

No functional-variation closure, stability PASS, unitarity claim, value/sign of `c6`, quantum transition, GR recovery or experimental claim follows from this analytic lemma. `theory established=0%`.