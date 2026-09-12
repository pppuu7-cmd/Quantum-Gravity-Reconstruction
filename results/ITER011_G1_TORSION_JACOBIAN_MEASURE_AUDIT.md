# Iter011 G1 — torsion-Jacobian measure audit

Date: 2026-09-12

Authoritative workflow run: `34666229043` at commit `601a375dfb2c4add1fa29858649e37c77b90b8f2`.

Artifacts:
- refinement scaling: `10289361811`, sha256 `84227a18c155a5d1cca698fc2389d0428ad886ac59dee8788ac454ee89c704fc`
- amplitude parity: `10289297017`, sha256 `3fd5b12a757273cb8efcc28cd16e5a1294bc2f16d3917640f1521343d19d2fed`
- local composition: `10289501683`, sha256 `f32f7c500ea22f91b1a7025d0a7e350967cd52e49a23807486abb74c95bd7658`
- aggregate: `10288932058`, sha256 `24daa97a5e84c4a153684276f7c1db2d0f1e05cf5319757e1a67d9ca61161ecf`

All three numerical lanes and the aggregate completed successfully.

## Results

### Flat-subtracted refinement scaling

For the Weyl-active G3 background at `kappa=0.08`, the flat-subtracted sum of `log|det dT/domega|` was

- h=0.5: `-9.167327480724907e-3`
- h=0.25: `-6.097921285856955e-4`
- h=0.125: `-3.8193063772951064e-5`
- h=0.0625: `-1.8787601732128678e-6`
- h=0.03125: `+3.345239463214966e-7`

The fitted absolute refinement slope is `3.7826601007995553`, close to an `h^4` measure-sector correction over the tested range. The last point is already near numerical-cancellation scale and should not be over-interpreted.

The torsion solve remained regular on the tested sequence: maximum residual below `8.2e-13` and minimum Jacobian singular value above about `0.385`.

### Tidal-amplitude parity

At h=0.125, a cubic polynomial diagnostic in kappa gives coefficients

`[-4.106358e-6, -6.014654e-3, +6.204841e-4]`

for `(kappa, kappa^2, kappa^3)` respectively.

The even component dominates. The odd/even absolute ratios at |kappa| = 0.04, 0.08, 0.12 are approximately

`1.76e-2, 3.80e-4, 6.60e-3`.

Thus the present Jacobian signal is primarily parity-even/quadratic in the tidal amplitude. A small odd component is visible numerically but is not yet certified as a continuum Weyl^3 term; dedicated refinement tests are required.

### Naive local cell-product composition

One dyadic 4D subdivision gives a large mismatch between the coarse flat-subtracted log-weight and the sum over 16 fine-cell log-weights:

- coarse h=0.25: relative defect `0.77924`
- coarse h=0.125: relative defect `0.77266`

This is **not** a scientific failure of the coarea construction. It shows that the local per-cell determinant cannot be naively multiplied over cells with duplicated shared-boundary variables. The correct glued coarea/Haar measure must account for shared connection variables and constraint coupling.

## Scientific decision

`JACOBIAN_REAL_MEASURE_DATUM_DOES_NOT_LIFT_C6_COHERENT_PHASE_NULL_DIRECTION`

The torsion/coarea Jacobian is a positive real measure factor derived from the constraint map. No canonical relation has been derived that converts `log|det dT/domega|` into the coherent Lorentzian phase `i S / hbar`. Therefore this audit does not determine a microscopic numerical `c6`, even if a curvature-cubic contribution survives later refinement.

The dominant observed effect is compatible with an `h^4`, parity-even measure correction rather than the missing six-derivative Weyl^3 phase normalization.

## Next gates

1. Refine the small odd component in h to decide whether it is a continuum contribution or a discretization tail.
2. Derive the correct glued Haar/coarea measure on shared connection variables; do not use naive independent-cell multiplication.
3. Continue the independent search for a nonhomogeneous microscopic coherent phase/action datum with nonzero Weyl^3 sensitivity.

## Claim guards

- `c6 fixed = NO`.
- No new-physics claim follows from this measure correction.
- No conversion from real coarea weight to Lorentzian action phase is authorized.
- No global strong-curvature measure theorem is implied.
