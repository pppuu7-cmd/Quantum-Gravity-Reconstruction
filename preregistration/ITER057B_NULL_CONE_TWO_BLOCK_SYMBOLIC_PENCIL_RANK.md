# Iter057B preregistration — symbolic null-cone two-block Einstein/Weyl3 pencil rank

Date: 2026-09-15
Gate: `ITER057B-NULL-CONE-TWO-BLOCK-EINSTEIN-WEYL3-SYMBOLIC-PENCIL-RANK`

## Motivation

Iter057A prospectively falsified the hypothesis that both non-gauge GR null classes are also Weyl3 `k4` null classes. On all 24 frozen exact cases, the quotient kernel intersection has dimension one. Therefore the two exact matrices `M2` and `M4` share the four gauge directions plus one non-gauge null direction, while one GR null class is mapped nontrivially by `M4`.

The immediate matrix-pencil question is whether

`M(lambda)=M2 + lambda M4`

has rank 5 for every nonzero symbolic multiplier `lambda` on this frozen panel, versus rank 4 at `lambda=0`.

`lambda` is only a symbolic relative multiplier for this two-block audit. It is not a fitted or normalized value of physical `c6`.

## Frozen objects and panel

Reuse exactly the Iter057A objects:

- 12 rational Weyl backgrounds `background_operator(seed)`, `seed=0,...,11`;
- null covectors `(1,1,0,0)` and `(5,3,4,0)`;
- exact Einstein `M2` from the same principal Riemann convention;
- exact Weyl3 Hessian `M4=Q(W,k)`;
- exact 4D pure-gauge matrix `K(k)`.

No background, covector, basis or normalization changes are allowed after output.

## Frozen controls

A. Reproduce all Iter057A object controls: `k^2=0`, `rank K=4`, `rank M2=4`, `rank M4=4`, both symbols annihilate `K`, and full common-kernel dimension = 5.

B. Introduce a single exact SymPy indeterminate `lambda` and construct `M(lambda)=M2+lambda M4` without assigning a sign or numerical value.

C. Generic symbolic-rank predicate: rank over the rational-function field must be exactly 5 in every case.

D. Strong all-nonzero predicate: for each case find at least one exact 5x5 minor of `M(lambda)` whose factored polynomial is a nonzero monomial `c*lambda^m`, `m>=1`, with `c != 0`. Together with the common five-dimensional kernel this proves `rank M(lambda)=5` for every `lambda != 0`, not merely generic lambda.

E. Zero control: `rank M(0)=4` exactly.

F. Common-kernel control: the frozen five-dimensional full common kernel of `M2` and `M4` is annihilated by `M(lambda)` identically, leaving at least the four gauge directions plus one non-gauge null class for every lambda.

G. If C passes but D cannot be certified, classify only a generic-lambda result; do not upgrade it to all nonzero lambda.

## Frozen classifications

Maximum PASS if A-F hold in all 24 cases:

`PASS_SCOPED_ITER057B_NULL_CONE_TWO_BLOCK_PENCIL_RANK5_FOR_ALL_NONZERO_SYMBOLIC_MULTIPLIER_ON_FROZEN_PANEL`.

Partial/generic result if A-C,E,F hold but D fails or remains unproved:

`PARTIAL_SCOPED_ITER057B_GENERIC_NONZERO_MULTIPLIER_RANK5_ALL_NONZERO_NOT_CERTIFIED`.

Scientific FAIL if controls are valid but symbolic rank is not 5 in at least one case:

`SCIENTIFIC_FAIL_ITER057B_TWO_BLOCK_RANK5_HYPOTHESIS_ON_FROZEN_PANEL`.

INVALID if any Iter057A object/provenance control is not reproduced.

## Interpretation ceiling

This gate audits only the two blocks `M2_Einstein + lambda M4_Weyl3`. The full linearized Weyl3 Euler response also contains lower-degree terms (including possible degree-two contributions on curved backgrounds), and those are **not** included here. Therefore even maximum PASS is not the full characteristic polynomial and does not authorize birefringence, cone shifting, hyperbolicity, ghost, stability, energy, or treatment claims.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.