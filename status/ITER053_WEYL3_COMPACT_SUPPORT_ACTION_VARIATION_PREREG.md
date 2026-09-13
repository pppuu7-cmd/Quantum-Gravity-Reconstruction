# Iter053 prospective preregistration — integrated compact-support Weyl3 action variation

Frozen before implementation or production evidence review.

## Gate
`ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION`

## Scientific question
For genuinely four-dimensional non-symmetry-reduced Lorentzian metric backgrounds and smooth compactly supported metric perturbations, does the finite integrated Weyl3 action directional derivative agree with the integrated bulk Euler response built from the independently validated five-point `H5 = A + I - 2 sqrt(-g) D5`, with the boundary term eliminated by compact support?

The target identity is

`d/dε ∫_Ω sqrt(-g(ε)) W3[g(ε)] d^4x |_{0} = ∫_Ω H5^{ab} h_ab d^4x`

provided the perturbation and its required derivatives vanish in a collar of `∂Ω`.

## Frozen panel
Three independent scientific streams, `fail-fast:false`:

### A — generic compact-support action lanes (4 lanes)
- Four new generic 4D polynomial metric seeds not used in Iter052.
- Four new perturbation seeds multiplied by a fixed C2 compact bump supported strictly inside the integration box.
- Fixed integration domain `Ω=[-0.32,0.32]^4`; bump support contained in `[-0.24,0.24]^4` with a nonzero boundary collar.
- Two frozen tensor-product Gauss-Legendre orders: coarse `n=5` and fine `n=7` per coordinate.
- Direct action derivative uses the same symmetric five-point epsilon stencil at `ε=(2e-4,1e-4,5e-5)` and is compared at the finest epsilon.
- Bulk integral uses the independently assembled five-point `H5` and the same fine quadrature rule.

### B — conformally-flat null controls (2 lanes)
- Two new conformally-flat 4D Lorentzian backgrounds and independent compact bumps.
- Require Weyl3 density, P tensor, H5 response and integrated direct variation to remain numerically null within frozen absolute tolerances.

### C — determinant-one linear-coordinate covariance controls (2 lanes)
- Two new generic metric/perturbation lanes and exact determinant-one transforms.
- Repeat the integrated identity in both coordinate frames over the correspondingly transformed integration domain.
- Require direct integrated derivative and integrated bulk response to agree across frames within frozen covariance tolerance.

## Frozen validity controls
A lane is invalid, not a scientific FAIL, if any of the following fail:
- Lorentzian signature at all quadrature nodes used in the fine panel and all required ±epsilon perturbations.
- metric inverse residual `<=3e-11`.
- finite numerical values throughout.
- compact-support collar: perturbation amplitude and first derivatives exactly zero (analytic construction) on and outside the frozen support boundary; numerical spot checks `<=1e-13`.
- determinant-one transform controls for stream C: `|det L-1| <=2e-12` and transformed metric/perturbation algebra residuals `<=3e-11`.

## Frozen scientific thresholds
For A lanes:
- fine direct integrated derivative magnitude `>=1e-9`;
- direct epsilon final-step relative change `<=2e-4`;
- fine direct-vs-bulk relative residual `<=8e-4`;
- coarse-to-fine identity residual absolute change `<=8e-4`;
- bulk coarse-to-fine relative change `<=5e-4`.

For B lanes:
- integrated `|direct| <=5e-8`;
- integrated `|bulk| <=5e-8`;
- sampled `|W3| <=2e-10`;
- sampled `||P|| <=3e-9`;
- sampled `||H5|| <=3e-7`.

For C lanes:
- both frames independently satisfy the A thresholds;
- direct integrated covariance relative residual `<=1e-3`;
- bulk integrated covariance relative residual `<=1e-3`.

## Negative/control requirements
- Include one deliberately wrong historical sign control using `A+I+2 sqrt(-g)D5`; on each generic A lane its integrated residual must exceed the correct residual and at least one A lane must have wrong-sign residual `>=1e-2`.
- No coefficient fitting, sign scan, epsilon retuning, quadrature-order retuning, lane dropping or threshold changes after production evidence is visible.

## Frozen classifier
Only the following terminal scientific outputs are allowed after all raw artifacts are consumed:
- `PASS_SCOPED_ITER053_WEYL3_INTEGRATED_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE`
- `SCIENTIFIC_FAIL_ITER053_WEYL3_INTEGRATED_COMPACT_SUPPORT_ACTION_VARIATION`
- `ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`
- `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`

## Interpretation lock
Even a full PASS is a finite integrated 4D computational certificate, not a global proof of the full functional derivative on arbitrary field space, not experimental confirmation, and not a complete quantum-gravity theory. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains 0%. A third repetitive symmetry-reduced minisuperspace gate is not an allowed substitute.