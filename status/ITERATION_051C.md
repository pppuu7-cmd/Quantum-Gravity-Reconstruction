# Iter051C — Final full covariant Weyl^3 Euler–Lagrange assembly

Date: 2026-09-13
Gate: `ITER051C-FULL-WEYL3-EOM-ASSEMBLY`

## Prospective authority
This file is committed before implementation and production. Frozen scientific criteria below must not be weakened after production.

## Question
Can the independently closed Iter051 prerequisites be assembled into one metric-consistent four-dimensional coefficient tensor for the variation of

`S6 = c6 ∫ d^4x sqrt(-g) I3`,  `I3 = C_ab^{  cd} C_cd^{  ef} C_ef^{  ab}`,

with `c6` kept symbolic/unfixed, and can that assembled tensor satisfy independent metric-consistent, reduced-variation, null and frame-covariance checks?

## Frozen assembly convention
All production code uses the coefficient `H^{mn}` defined by

`δ[ sqrt(-g) I3 ] = H^{mn} δg_mn + total derivative`

for symmetric covariant metric variation `δg_mn`.

Let
- `A^{mn}` be the Iter051A-R1 algebraic metric-density derivative at fixed all-lower `R_abcd`;
- `P^{abcd} = ∂I3/∂R_abcd`, with algebraic-Riemann projection as closed by Iter051B1;
- `R^e_bcd = g^{ef} R_fbcd`;
- `D^{mn} = ∇_b ∇_a P^{a m b n}`, using the corrected covariant double-divergence convention closed by Iter051B0-R1 / Iter051B2.

The frozen assembled coefficient is

`H^{mn} = A^{mn} + sqrt(-g) * sym_{mn}[ P^{m b c d} R^n_bcd ] + 2 sqrt(-g) D^{mn}`.

No coefficient or sign may be changed after production. A mismatch against the independent exact reduced variation is a scientific/assembly failure, not permission to retune the formula.

## Frozen production matrix — 18 scientific lanes

### Stream A — 4 generic metric-consistent 4D local jets
Four deterministic seeds. Each lane constructs a smooth Lorentzian polynomial metric jet through fourth coordinate order, derives its Levi-Civita connection and all-lower Riemann tensor from that same metric, constructs `A`, actual Weyl^3 `P`, and the covariant double divergence by independent finite-difference connection response, then assembles `H`.

Required:
- Lorentz signature on all stencil points;
- inverse residual <= `2e-11`;
- Riemann algebraic residual <= `2e-9`;
- `P` algebraic residual <= `2e-9`;
- assembled `H` symmetry residual <= `3e-7`;
- nonzero calibration `||H|| > 1e-7`;
- final-step change of `H` across frozen derivative steps <= `2e-3`.

### Stream B — 6 independent exact G48 reduced-Euler–Lagrange cross-checks
Use the six already-frozen G48 power-law pairs
`(-1/2,1/3), (1/4,3/4), (-2/3,1/2), (2/5,-1/5), (3/2,1/4), (-1/4,5/6)`
at frozen positive witness times `[1/2, 2/3, 1, 3/2, 2, 3]`.

For `N=1, a=t^p, b=t^q`, convert assembled `H` to reduced coefficients by
- `E_N(pred) = -2 N H^{00}`;
- `E_a(pred) = 2 a H^{11}`;
- `E_b(pred) = 2 b (H^{22}+H^{33})`.

Compare to the exact, independently derived G48 generalized Euler–Lagrange formulas already frozen in `code/qgr_iter048_weyl3_variational.py`.

Required:
- each of `E_N,E_a,E_b` nonzero for the frozen lane;
- maximum relative residual to exact G48 target <= `3e-4`;
- final-step change <= `2e-4`.

This stream is the decisive sign/coefficient falsification control: no post-hoc adjustment of the assembly is allowed.

### Stream C — 4 conformally-flat null controls
Use four nontrivial spatially-flat isotropic FLRW profiles with nonzero Riemann curvature. Required:
- nonzero Riemann calibration;
- `|I3| <= 2e-10`;
- `||P|| <= 3e-9`;
- `||H|| <= 2e-7`.

### Stream D — 4 constant Lorentz-frame covariance lanes
Use four deterministic generic metric-consistent polynomial witnesses and transform the complete metric function by determinant-one constant Lorentz maps. Recompute the full assembled tensor independently in the transformed frame.

With `g' = L^T g L` and the corresponding coordinate pullback, the density coefficient must obey the frozen contravariant law
`H' = L^{-1} H L^{-T}`
for `det L = +1`.

Required covariance relative residual <= `8e-4`, with inverse/metric transformation controls <= `2e-11` and nonzero `H` calibration.

## Frozen numerical derivative schedule
Connection/double-divergence evaluations use central finite differences at steps
`h = [1.0e-3, 5.0e-4, 2.5e-4]`.
Algebraic metric-density and curvature directional gradients use complex-step differentiation with the existing Iter051A-R1/B1 conventions. No production fitting is allowed.

## Aggregate classification
Full PASS requires all 18 unique scientific lane artifacts, valid controls, and 18/18 lane PASS:

`PASS_SCOPED_FULL_COVARIANT_WEYL3_EOM_ASSEMBLY_CERTIFICATE`

Any scientifically valid mismatch:
`SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`

Missing/invalid controls or implementation/infrastructure failure:
`ITER051C_CONTROL_OR_IMPLEMENTATION_INVALID`

## Interpretation lock
Even a full PASS establishes a scoped four-dimensional covariant assembly/certificate for the coefficient multiplying the still-unfixed `c6` operator. It does **not** determine `c6`, authorize `beta=1`, prove QGR correct, prove absolute energy positivity or quantum unitarity, constitute experimental confirmation, or turn finite-panel numerical checks into a global theorem. `theory established` remains `0%`.

Historical G51A/G51B0/G51B2 failures remain in the audit trail and are not rewritten.
