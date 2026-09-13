# Iteration 052 — genuinely 4D Weyl^3 directional-variation certificate

Date: 2026-09-13
Gate: `ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION`
Status at this commit: **prospectively preregistered before implementation and production**.

## Scientific question

Does the D3 five-point tensor density reproduce the direct first variation of the full four-dimensional Weyl-cubic Lagrangian density under arbitrary non-symmetry-reduced metric perturbations, including the covariant boundary-current divergence?

This gate is deliberately not another minisuperspace/symmetry-reduced panel.

## Frozen objects and conventions

Scalar Lagrangian density, with the same Weyl-cubic convention used by Iter040–Iter051:

`L6[g] = sqrt(-g) W3[g]`.

`P^{abcd} = ∂W3/∂R_{abcd}` is the independently certified projected algebraic-Riemann derivative used since G51B1.

The bulk tensor density is frozen to the D3 assembly

`H5 = A + I - 2 sqrt(-g) D5`,

with the independently validated nested five-point covariant double divergence `D5`. No sign or coefficient search is permitted in Iter052.

For a symmetric covariant perturbation `h_ab = δg_ab`, freeze the Iyer–Wald-type potential-density convention

`Theta^mu = 2 sqrt(-g) [ P^{mu(alpha beta)nu} nabla_nu h_{alpha beta} - h_{alpha beta} nabla_nu P^{mu(alpha beta)nu} ]`.

The prospectively tested pointwise identity is

`d/dε L6[g + ε h]|_{ε=0} = H5^{ab} h_ab + ∂_mu Theta^mu`.

The left side is evaluated independently by a five-point finite difference in field-space ε. The boundary-current divergence is independently evaluated by nested five-point coordinate derivatives of the frozen `Theta`, rather than by substituting the D3 double-divergence value.

`c6` remains symbolic/unfixed and is factored out of every comparison.

## Frozen metric and perturbation families

Primary metrics are generic Lorentzian polynomial metrics depending nontrivially on all four coordinates. Perturbations are independent symmetric polynomial tensor fields with constant, linear and quadratic pieces depending on all four coordinates. Neither family is symmetry-reduced.

Conformally-flat controls use `g_ab = Omega(x)^2 eta_ab` with nontrivial all-four-coordinate polynomial `Omega` and arbitrary generic perturbations; their background Weyl tensor, W3, P and first variation should vanish within frozen numerical tolerance.

Covariance controls use fixed determinant-one linear coordinate transformations, transforming both the background metric and the perturbation tensor before recomputing the entire directional identity independently.

## Frozen production panel

12 independent lanes, `fail-fast: false`:

- Stream A: 6 fresh generic four-dimensional polynomial metric/perturbation pairs at fresh off-origin witnesses.
- Stream B: 3 all-four-coordinate conformally-flat curved null controls with generic perturbations.
- Stream C: 3 determinant-one linear-coordinate covariance pairs using fresh generic seeds.

No D3 seed/witness pair is reused as a primary A witness.

## Frozen numerical methods

Coordinate five-point steps for `H5` and `Theta` divergence: `h = 1e-3` and `5e-4`, with the finest value authoritative and the coarser value used only for stability.

Field-space five-point steps for the direct derivative: `eps = 2e-4`, `1e-4`, `5e-5`; the finest value is authoritative.

All metric-signature and inverse controls are evaluated throughout the finite-difference neighborhoods relevant to the lane.

## Frozen PASS criteria

### Common controls
- Lorentzian signature valid throughout required neighborhoods.
- max inverse residual `<= 3e-11`.
- all reported quantities finite.
- `c6_status = SYMBOLIC_UNFIXED_COEFFICIENT_ONLY`.

### Stream A
- `|direct directional derivative| >= 1e-8`.
- direct field-space derivative final-step relative change `<= 5e-5`.
- full identity relative residual `<= 3e-4` at the authoritative steps.
- identity residual change between the two coordinate-step evaluations `<= 3e-4` in absolute residual units.
- `H5` symmetry residual `<= 5e-7`.

### Stream B
- background Riemann norm `>= 1e-6`.
- `|W3| <= 2e-10` and `||P|| <= 3e-9`.
- direct first directional derivative absolute value `<= 2e-8`.
- `||H5|| <= 3e-7`.
- absolute full-identity mismatch `<= 3e-8`.

### Stream C
Each original and transformed realization must independently satisfy the Stream-A identity criteria, and additionally:
- `|det L - 1| <= 2e-12`.
- metric/perturbation transform construction residuals `<= 3e-11`.
- direct-derivative covariance relative residual `<= 5e-4`.
- bulk-plus-boundary RHS covariance relative residual `<= 5e-4`.

## Frozen classifications

Full PASS:
`PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`.

Scientific mismatch with valid controls:
`SCIENTIFIC_FAIL_ITER052_WEYL3_4D_DIRECTIONAL_VARIATION_IDENTITY`.

Invalid controls/implementation evidence:
`ITER052_IMPLEMENTATION_OR_CONTROL_INVALID`.

## Interpretation lock

A PASS would establish only a finite, genuinely four-dimensional computational certificate that the D3 bulk tensor density and the independently evaluated covariant boundary current reproduce direct first directional variations on the frozen panel. It would not prove a global theorem for every metric/variation, would not fix `c6`, would not establish quantum unitarity or absolute energy positivity, and would not make QGR an established theory.

Historical G51C and D2 failures remain unchanged regardless of Iter052 outcome.

## External analytic authority used only to freeze the boundary-current convention

The potential-current structure is frozen from the standard covariant variation of Lagrangians depending on the metric and Riemann tensor (Iyer & Wald, arXiv:gr-qc/9403028, especially their curvature variation/integration-by-parts equations 30–39). No production data were inspected in choosing this convention.
