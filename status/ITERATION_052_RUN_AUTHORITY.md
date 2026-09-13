# Iter052 production run authority

Date: 2026-09-13
Gate: `ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION`

## Initial production run — implementation/control invalid

- Prospective preregistration: `c49084e54428042cf59e5ac083ee49f0614a3de0`
- Scientific implementation: `b9da6cdfc424d712b80db935f16f89c00f8f5b9f`
- Frozen aggregate: `79dff35e80c5095688d898b78bb78d7b80768657`
- Workflow: `ff68b12968fdce2b6c220880009c256406309a65`
- Production head: `f455d413bfe50128598b6fa11d70ab79bea52183`
- Run: `34748588704`
- Aggregate job: `103701280550`
- Summary artifact: `10315495921`
- Summary digest: `sha256:3212dd4183fe73aef626ed43a77e3856c3e55b052799d99c9bd72431444a3e08`
- Frozen aggregate classification: **`ITER052_IMPLEMENTATION_OR_CONTROL_INVALID`**.

All 12 expected artifacts were present. Eleven lanes were valid PASS. The sole invalid lane was covariance lane C2.

### Exact reason C2 is invalid

The frozen covariance control requires `|det L - 1| <= 2e-12`. C2 produced

`det L = 1.000000003317951`,

so the determinant-one construction missed the frozen tolerance by roughly three orders of magnitude.

The underlying scientific quantities in C2 were nevertheless well inside the frozen scientific thresholds:

- base identity relative residual `4.335297618863669e-10`;
- transformed identity relative residual `1.5033400152202607e-10`;
- direct-derivative covariance relative residual `3.3307732623251213e-09`;
- bulk-plus-boundary RHS covariance relative residual `3.047577502781268e-09`;
- metric transform residual `4.336808689942018e-19`;
- perturbation transform residual `1.3877787807814457e-17`.

These values do not rescue the frozen run: the failed determinant-one control makes the initial production run non-authoritative for terminal scientific classification.

## Control-defect diagnosis

The implementation constructed the C2 cyclic shear and then attempted to enforce determinant one by dividing `L[3,3]` by the already-computed determinant. For a non-triangular cyclic shear this is not algebraically valid because the determinant is affine, not purely multiplicative, in that matrix element.

The authorized control-only correction preserves every frozen off-diagonal matrix entry and solves the affine determinant equation for `L[3,3]`:

1. evaluate `d0 = det L` at `L[3,3]=0`;
2. evaluate `d1 = det L` at `L[3,3]=1`;
3. set `L[3,3] = (1-d0)/(d1-d0)`.

For the frozen C2 off-diagonal entries this gives `L[3,3]=1.0000576` and `det L=1.0` at double precision.

No scientific formula, identity, seed, witness point, finite-difference step, threshold, sign, or coefficient is changed.

## Retry authority rule

The initial run `34748588704` remains permanently classified as `ITER052_IMPLEMENTATION_OR_CONTROL_INVALID` and must not be combined with retry evidence. A fresh full 12-lane production retry is required for terminal scientific authority after the control-only determinant fix.
