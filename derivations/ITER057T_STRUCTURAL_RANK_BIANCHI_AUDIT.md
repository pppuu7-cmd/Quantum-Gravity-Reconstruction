# Iter057T structural rank/Bianchi audit

Date: 2026-09-15
Gate: `ITER057T-OCTIC-EINSTEIN-SEED-COMPLETION`
Preregistration: `0f01308e81e54f77ccb91f8a76f0c129684740ff`

This note freezes an independent structural target for the exact production calculation. It is not a terminal scientific result and does not substitute for exact production rank/augmented-rank evaluation.

## Homogeneous dimensions

For four variables, the dimension of homogeneous degree `n` polynomials is

`N_n = C(n+3,3)`.

For the unrestricted symmetric trace-reversed octic metric jet:

- symmetric tensor components: `10`;
- degree-eight monomials: `N_8=C(11,3)=165`;
- unknown octic coefficients: `10*165=1650`.

The linear de Donder condition is degree seven:

- degree-seven monomials: `N_7=C(10,3)=120`;
- four gauge components: `4*120=480` rows.

The linearized Einstein response is degree six:

- degree-six monomials: `N_6=C(9,3)=84`;
- ten symmetric field components: `10*84=840` rows.

Hence the frozen octic affine system has shape

`(480+840) x 1650 = 1320 x 1650`.

## Canonical Bianchi left-null family

The exact same differential identity used in Iter057Q promotes one degree in the homogeneous complex. At degree five there are

`N_5=C(8,3)=56`

monomials. For each free field index `b=0,1,2,3`, the linearized Bianchi identity supplies one canonical row relation per degree-five monomial, so the expected canonical family has

`4*N_5 = 224`

vectors.

In the normalized Taylor basis these are exactly the vectors implemented by

`(1/2) eta^mm G_b,beta+2 e_m + eta^aa F_ab,beta+e_a`,

summed over repeated `m` and `a`, with symmetric pair ordering on `F_ab`.

Direct substitution into the frozen matrix stencil cancels column-by-column because the two contributions differ only by the order in which the divergence and wave-operator derivatives are taken. Thus every canonical Bianchi vector lies in the exact left nullspace.

## Rank target

If the production matrix has no additional left-null relations beyond the complete canonical Bianchi family, its exact rank must be

`1320 - 224 = 1096`,

with homogeneous nullity

`1650 - 1096 = 554`.

These numbers are therefore frozen as an independent target:

- matrix shape `1320 x 1650`;
- left nullity `224`;
- exact rank `1096`;
- homogeneous nullity `554`.

The production evaluator must still compute the exact rank and augmented rank independently. Agreement with these values is a control, not an assumption.

## Consistency target

The fixed quartic+sextic Einstein seed has already been certified to make all Einstein coefficients through coordinate degree four vanish. Therefore at degree six the exact nonlinear Bianchi identity has no contamination from lower nonzero Einstein orders. The degree-five divergence of the exact degree-six residual must vanish. Consequently every canonical Bianchi contraction with the affine right-hand side is expected to be exactly zero.

Again this is a prospective structural prediction only. Iter057T PASS still requires exact production evaluation, an exact particular octic correction, and independent unreduced nonlinear replay through coordinate degree six.

## Scope

No value/sign of `c6` is used. No restricted ansatz is introduced. Lower quartic/sextic canonical pivots remain frozen. No all-orders Einstein seed, convergence, open-neighborhood/global solution, physical characteristics, hyperbolicity, ghost/stability, quantum, UV, experimental, or QGR-correctness conclusion follows from this audit.