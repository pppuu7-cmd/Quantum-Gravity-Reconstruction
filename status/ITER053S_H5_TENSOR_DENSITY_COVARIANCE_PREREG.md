# Iter053S prospective preregistration — H5 tensor-density covariance localization

Date frozen: 2026-09-14

## Gate

`ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION`

This is a new diagnostic/localization gate motivated by the terminal Iter053R scientific FAIL. It does not rerun or reclassify Iter053R.

## State and dependency

Iter053R is permanently `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`: A4+B2 passed, while both determinant-one C covariance lanes failed only in the weighted H5 bulk. Direct support-domain action variation remained covariant at ~1e-12, whereas weighted H5 covariance residuals were ~0.6925 and transformed GJ2->GJ3 changes were ~0.292.

Before any replacement compact-support closure can be considered, the object identity of the numerical `H5=A+I-2 sqrt(-g)D5` realization must be established under coordinate change.

## Target hypothesis

For a scalar action density and covariant metric perturbation, write the first variation as

`delta S = integral d^4x H_x^{ab} h^x_ab`.

Under the frozen linear coordinate map `x = L y`, with `M=L^{-1}`, the required tensor-density law is

`H_y = |det L| M H_x M^T`,

while

`h_y = L^T h_x L`.

The frozen Iter053R C maps satisfy `det L = 1`, so the density factor is one.

The gate tests whether the implemented numerical H5 obeys this law pointwise and localizes any violation between the algebraic contribution `A+I` and the derivative contribution `T_D=-2 sqrt(-g) D5`.

## Frozen inputs

Reuse exactly the two Iter053R C metric/perturbation seeds and `shear(i)` maps for `i=0,1`; no new seed selection.

Probe points in original `x` coordinates:

- `P0 = (0,0,0,0)`
- `P1 = (0.08,-0.06,0.05,-0.04)`

Both lie strictly inside the compact-support cube `|x_i|<0.24`.

For each `(C index, probe)` evaluate the numerical H5 assembly at coordinate derivative steps

- `h = 1.0e-3`
- `h = 5.0e-4`
- `h = 2.5e-4`

using the existing five-point derivative construction. No step may be changed after production evidence.

The transformed point is always `y=M x`.

## Parallel lanes

### Lane A — exact algebra/control lane

For deterministic generic symmetric matrices `H,p` and both frozen `L` matrices, verify exactly/numerically to machine precision that

`tr[(M H M^T)^T (L^T p L)] = tr[H^T p]`

for `det L=1`.

Also evaluate the deliberately wrong congruence `L^T H L` as a negative control; at least one frozen case must disagree by relative residual `>=1e-2`.

### Lane B — pointwise direct-density covariance control

At every `(C index, probe)` use the existing five-point epsilon directional derivative with finest epsilon `5e-5` in base and transformed frames. Because `det L=1`, the directional action density must agree with relative residual `<=2e-6`.

Failure invalidates interpretation of the H5 localization.

### Lane C — H5 tensor-density transformation

For each `(C index, probe,h)` compute base and transformed:

- total `H5`;
- algebraic `A+I`;
- derivative-density term `T_D=-2 sqrt(-g)D5`.

Transform base quantities with `M Q M^T` and compare to quantities computed directly in transformed coordinates.

Record normalized Frobenius residuals using denominator `max(||Q_transformed||,||Q_expected||,1e-30)`.

Also compare pointwise scalar contractions with the frozen polynomial perturbation factor `p` transformed as `L^T p L`.

### Lane D — step-convergence aggregate

For each `(C index, probe)`, aggregate the three frozen derivative steps. No post-hoc lane dropping is allowed.

## Validity controls

A production lane is INVALID if any required value is non-finite, Lorentzian signature/control used by existing H5 assembly fails, inverse residual exceeds `3e-11`, `|det L-1|>2e-12`, transformed metric/perturbation algebra residual exceeds `3e-11`, or the exact Lane-A contraction control fails at `2e-12`.

## Frozen localization thresholds

At the finest step `h=2.5e-4`:

- direct-density covariance control: `<=2e-6`;
- algebraic `(A+I)` tensor-density residual: `<=2e-5`;
- total H5 tensor-density residual target: `<=2e-3`;
- derivative-density `T_D` residual target: `<=2e-3`;
- pointwise `H:p` contraction covariance target: `<=2e-3`.

For a term whose finest residual exceeds its target, step behavior is classified as convergent only if the residual strictly decreases across `1e-3 -> 5e-4 -> 2.5e-4` for every failing `(C index,probe)` instance. This convergence flag is diagnostic and does not convert an above-threshold result to PASS.

## Frozen terminal classifications

After all required lanes are present:

1. If validity/reference controls fail:
   `ITER053S_INVALID_IMPLEMENTATION_OR_REFERENCE_CONTROL`

2. If `(A+I)` exceeds `2e-5` at any finest-step probe while controls are valid:
   `ITER053S_ALGEBRAIC_H5_COVARIANCE_DEFECT_LOCALIZED`

3. If `(A+I)` passes everywhere but `T_D` or total H5 exceeds `2e-3` at any finest-step probe:
   `ITER053S_D5_COVARIANCE_DEFECT_LOCALIZED`

4. If algebraic, `T_D`, total H5 and contraction residuals all satisfy their targets at every finest-step probe:
   `ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`

The aggregate must additionally report whether any above-target residuals strictly decrease with step, but this does not alter classifications 2 or 3.

## Interpretation ceiling

A covariance-confirmed result would only remove pointwise H5 transformation as the explanation for Iter053R C failure and would then authorize a separate quadrature/pushforward convergence gate. A localized defect would identify an implementation/model-definition blocker requiring a new prospectively frozen correction gate.

No result here reclassifies Iter053R, establishes global Weyl3 EOM, opens quantum amplitude/measure, fixes `c6`, authorizes `beta=1`, establishes quantum unitarity, GR recovery, new physics, or theory establishment. `theory established=0%` remains locked.