# Iter053 prospective preregistration — integrated compact-support Weyl3 action variation

Frozen before implementation or production evidence review. This revision supersedes the initial preregistration draft **before any Iter053 implementation or production run existed**. It changes only the prospective numerical quadrature design to a compute-safe tensor panel; no Iter053 evidence had been observed.

## Gate
`ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION`

## Scientific question
For genuinely four-dimensional non-symmetry-reduced Lorentzian metric backgrounds and smooth compactly supported metric perturbations, does the finite integrated Weyl3 action directional derivative agree with the integrated bulk Euler response built from the independently validated five-point `H5 = A + I - 2 sqrt(-g) D5`, with the boundary term eliminated by compact support?

Target identity:

`d/dε ∫_Ω sqrt(-g(ε)) W3[g(ε)] d^4x |_{0} = ∫_Ω H5^{ab} h_ab d^4x`

provided the perturbation and its required derivatives vanish in a collar of `∂Ω`.

## Frozen panel
Three independent scientific streams, `fail-fast:false`.

### A — generic compact-support action lanes (4 lanes)
- Four new generic 4D polynomial metric seeds not used in Iter052.
- Four new perturbation seeds multiplied by a fixed compact polynomial bump with value, first and second derivatives vanishing at the support boundary.
- Integration domain `Ω=[-0.32,0.32]^4`; bump support is `[-0.24,0.24]^4`, leaving a nonzero boundary collar.
- Tensor-product Gauss-Legendre orders are prospectively frozen at coarse `n=3` and fine `n=4` per coordinate (81 and 256 nodes). This replaces the initial 5/7 draft before implementation because nested five-point H5 evaluation makes 5/7 needlessly expensive; no Iter053 scientific output existed at the time of this freeze.
- Direct action derivative uses the symmetric five-point epsilon stencil at `ε=(2e-4,1e-4,5e-5)` and is compared at the finest epsilon.
- Bulk integral uses independently assembled five-point `H5`; coordinate derivative step is frozen at `5e-4`.

### B — conformally-flat null controls (2 lanes)
- Two new conformally-flat 4D Lorentzian backgrounds and independent compact bumps.
- Require Weyl3 density, P tensor, H5 response and integrated direct variation to remain numerically null within frozen absolute tolerances.

### C — determinant-one linear-coordinate covariance controls (2 lanes)
- Two new generic metric/perturbation lanes and exact determinant-one transforms.
- Transform both metric and perturbation and integrate over the correspondingly transformed parallelepiped using the same reference Gauss nodes; `det L=1` makes the integration measure comparison direct.
- Require direct integrated derivative and integrated bulk response to agree across frames within frozen covariance tolerance.

## Frozen validity controls
A lane is invalid, not a scientific FAIL, if any of the following fail:
- Lorentzian signature at all fine quadrature nodes and required ±epsilon perturbations.
- metric inverse residual `<=3e-11`.
- all output numbers finite.
- compact-support collar analytic construction verified by boundary spot checks: perturbation value and first derivatives `<=1e-13`.
- stream C: `|det L-1| <=2e-12`, transformed metric and perturbation algebra residuals `<=3e-11`.

## Frozen scientific thresholds
A lanes:
- fine direct integrated derivative magnitude `>=1e-10`;
- direct epsilon final-step relative change `<=5e-4`;
- fine direct-vs-bulk relative residual `<=3e-3`;
- coarse-to-fine identity residual absolute change `<=3e-3`;
- bulk coarse-to-fine relative change `<=2e-3`.

B lanes:
- integrated `|direct| <=5e-8`;
- integrated `|bulk| <=5e-8`;
- sampled `|W3| <=2e-10`;
- sampled `||P|| <=3e-9`;
- sampled `||H5|| <=3e-7`.

C lanes:
- both frames independently satisfy the A thresholds;
- direct integrated covariance relative residual `<=2e-3`;
- bulk integrated covariance relative residual `<=2e-3`.

## Negative/control requirements
- Deliberately wrong historical sign control `A+I+2 sqrt(-g)D5` is evaluated on every A lane. Its integrated residual must exceed the correct-sign residual on every generic A lane, and at least one A lane must have wrong-sign residual `>=1e-2`.
- No coefficient fitting, sign scan, epsilon retuning, quadrature-order retuning, lane dropping or threshold change is allowed after implementation/production evidence becomes visible.

## Frozen classifier
Only:
- `PASS_SCOPED_ITER053_WEYL3_INTEGRATED_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE`
- `SCIENTIFIC_FAIL_ITER053_WEYL3_INTEGRATED_COMPACT_SUPPORT_ACTION_VARIATION`
- `ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`
- `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`

## Interpretation lock
Even a full PASS is a finite integrated 4D computational certificate, not a global proof of the full functional derivative on arbitrary field space, not experimental confirmation and not a complete quantum-gravity theory. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains 0%. A third repetitive symmetry-reduced minisuperspace gate is not an allowed substitute.