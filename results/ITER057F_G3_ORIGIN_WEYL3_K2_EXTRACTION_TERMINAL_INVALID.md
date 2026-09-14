# Iter057F terminal result — historical extraction contract INVALID

Date: 2026-09-15
Gate: `ITER057F-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-EXTRACTION`
Preregistration: `8df569f7414a9d634b72e54264b529245b356288`
Implementation: `15b77a71280aa755601a7c5fd20253ed723650a0`
Production head/workflow: `e7c74847184e826ed3331c107b2a9ad54b2dab90`
Production run: `34905773224`

## Terminal classification

**`INVALID_ITER057F_FULL_EOM_EXTRACTION_OR_CONVENTION_CONTROL`**

This is an implementation/control-definition INVALID result, not a scientific failure of the Weyl3 degree-two block.

The classification is terminal before the remaining diagnostic lanes finish because the frozen contract requires **every** basis lane to satisfy the direct exact-`L4` comparison. Multiple already-terminal, otherwise-valid lanes fail that mandatory predicate for a subsequently localized exact normalization reason. No remaining lane can restore the all-lane PASS condition.

## Decisive frozen-control evidence

### Basis lane 7

The full-EOM extraction itself is numerically well controlled:

- amplitude `L2` relative change: `2.885e-5`;
- stencil `L2` relative change: `1.56e-5`;
- held-out-frequency residual: `5.24e-6`;
- `L4` amplitude/stencil convergence also at few-parts-in-`1e-5`.

But the frozen exact control compared the extracted full-EOM `L4` column directly to the Iter054C bivector-Hessian column `Q[:,7]`.

Historical target:

`Q[:,7]` has representative entries `(+0.06,-0.12,+0.06,...)`.

Extracted full-EOM column:

`(+0.480003,-0.959998,+0.480000,...)`.

Thus the lane fails the frozen direct-equality predicate with relative residual approximately seven, even though the extracted column is stable.

### Basis lane 6

A second independent nonzero-Q lane gives the same pattern:

- held-out-frequency residual `1.95e-6`;
- amplitude `L2` change `2.61e-5`;
- stencil `L2` change `1.61e-5`;
- exact historical `Q[:,6]` has representative entries `(-0.18,+0.18)`;
- extracted `L4` gives `(-1.440001,+1.439998)`.

Again the stable full-EOM result is eight times the historical target.

### Basis lane 8

The exact Iter054C `Q` column is identically zero. The extracted `L4` is numerical noise at roughly `1e-6` absolute scale, but the frozen implementation normalized by a `1e-10` denominator floor and therefore generated an artificial huge relative residual. Relative amplitude/stencil convergence of an exact-zero target is likewise ill-posed.

The `L2` measurement in this lane itself showed good amplitude/stencil convergence (`~1e-4`) and held-out-frequency residual `4.87e-5`.

## Exact post-localization cause

After the first nonzero-Q lane exposed a systematic factor, the representation normalization was derived analytically and committed separately as

`725c1e180641e05bc5701ccbb193bd34168e8dd2`.

The unrestricted full tensor scalar is

`I3_full = C_ab{}^{cd} C_cd{}^{ef} C_ef{}^{ab}`,

while Iter054C's six-dimensional independent-bivector operator uses `J=tr(W^3)` with one representative per antisymmetric pair. Exact pair-orientation counting gives

**`I3_full = 8 J`.**

Therefore

**`L4_full = 8 Q_Iter054C`**,

not the frozen Iter057F target `L4=Q`.

The factor is an exact representation conversion, not an empirical fit. It also explains lanes 6 and 7 quantitatively at the numerical convergence level.

## Additional pre-output control qualification

Before any Iter057F lane output, audit `e3d9826b8f21eabf9d3b1e5326f0e3f464ce0598` had already shown that the frozen isolated subprincipal predicate

`L2[k_(a xi_b)]=0`

is not a generally valid standalone curved-background Ward identity. Lower-order diffeomorphism identities mix subprincipal blocks with background-dependent pieces.

A valid exact trace-Ward control was frozen instead, and its later normalization was corrected by the same exact factor-eight bridge before using any L2 trace output.

## Why this is INVALID rather than SCIENTIFIC_FAIL

The scientific extraction object was not falsified. The terminal lanes show converged full-EOM responses and excellent even-frequency held-out prediction. What failed was the frozen **comparison convention/control definition**:

- nonzero columns were compared to a target low by an exact factor eight;
- the exact-zero column was assessed by an ill-posed relative-to-zero metric;
- one lower-order gauge control was overconstrained.

Under the preregistered classification these defects require `INVALID`, and the historical gate is not repaired post hoc.

## Successor authority

- Iter057F2 remains diagnostic only because it was prospectively frozen before the factor-eight bridge but inherited the same normalization error.
- Iter057F3 is a separately preregistered fresh production using the exact analytic full-tensor targets `8Q` and `8T`, a proper exact-zero column control, and the exact trace-Ward identity.

No Iter057F raw lane is promoted to F3 PASS evidence.

## Claim locks

This INVALID result does not fix `c6`, establish full characteristics/hyperbolicity, select a physical treatment, or alter quantum/theory claim locks. Theory established remains `0%`.