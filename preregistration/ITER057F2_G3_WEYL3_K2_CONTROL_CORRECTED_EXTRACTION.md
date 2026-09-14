# Iter057F2 preregistration — control-corrected G3-origin Weyl3 degree-two extraction

Date: 2026-09-15
Gate: `ITER057F2-G3-ORIGIN-WEYL3-DEGREE2-BLOCK-CONTROL-CORRECTED-EXTRACTION`

## Timing and historical lock

This successor is frozen after Iter057F basis lane 8 became terminal but while the other nine Iter057F basis lanes were still running and before the Iter057F aggregate existed.

Iter057F remains immutable under its original contract. The present gate does not reclassify or repair Iter057F.

The successor is required because two control-definition defects were identified:

1. the exact Iter054C `Q` matrix for the frozen G3/H0 background and `k=(1,1,0,0)` has one structurally zero input column, basis index 8 = `(23)`. Relative errors/convergence ratios normalized only by a `1e-10` floor are ill-posed for this exact-null column;
2. the pre-output methodology audit `e3d9826b8f21eabf9d3b1e5326f0e3f464ce0598` established that isolated `L2[k_(a xi_b)]=0` is not a generally valid curved-background subprincipal Ward identity. A valid exact trace-Ward identity was prospectively frozen instead in Iter057G (`d428fc70e000f9eda1d30b9e662e63cfa1a40c93`) and its exact target vector was committed pre-output as `3bf10b324911a98df5d093e58f55abd4fae4f7aa`.

No numerical result from the still-running nonzero-Q lanes is used to choose the present thresholds.

## Frozen scientific object

The scientific extraction object is unchanged from Iter057F:

- source-owned G3/H0 origin;
- `(-,+,+,+)` convention;
- `kappa=0.08=2/25`;
- null `k=(1,1,0,0)`;
- ten symmetric metric basis inputs;
- plane-wave perturbation `epsilon H_j cos(s k.x)`;
- corrected full-EOM assembly `A+I-2 sqrt(-g) D5`;
- frequencies `s=0,1,2`, held-out `s=3/2`;
- epsilon panel `2e-4,1e-4`;
- D5 stencil panel `1e-3,5e-4`;
- extraction `R(s)=L0+s^2 L2+s^4 L4` by the frozen three-point formulas.

No frequency, amplitude, stencil, source or exact-Q object changes are permitted.

## Frozen exact-Q structure

Construct the exact Iter054C G3/H0 `Q` matrix before numerical extraction. In the frozen basis order, its rank is 4 and **only column 8 is identically zero**.

Let

`Qscale = ||Q||_F`.

The zero-column identity must be verified symbolically. Any different zero-column pattern is INVALID.

## Frozen controls

A. Source/signature validity: identical to Iter057F.

B. `L2` amplitude convergence: identical to Iter057F, relative change <= `5e-3` for all ten lanes.

C. `L2` stencil convergence: identical to Iter057F, relative change <= `1e-2` for all ten lanes.

D. Held-out frequency: identical to Iter057F, relative Frobenius residual <= `3e-3` for all ten lanes.

E. Nonzero exact-`L4` columns: for each `j != 8`, retain the original direct no-fit exact column residual <= `2e-2`, and retain the original `L4` amplitude/stencil relative-convergence thresholds (`5e-3`, `1e-2`).

F. Exact-null `L4` column 8: do **not** divide by an arbitrary tiny denominator. For every extracted `L4_8` on the full two-epsilon x two-stencil panel require

`||Bcol_8||_2 / Qscale <= 2e-2`.

This inherits the original 2% exact-Q scale tolerance at the full-operator scale. No relative amplitude/stencil convergence predicate is applied to a quantity whose exact target is zero.

G. Aggregate exact `L4`: assembled bilinear `L4` matrix must satisfy the original aggregate controls:

- symmetry residual <= `2e-3`;
- full exact-Q relative residual <= `2e-2`.

H. Exact trace-Ward control: replace the invalid isolated subprincipal gauge-null predicate by the already prospectively frozen Iter057G identity. In basis order `(00,01,02,03,11,12,13,22,23,33)`, the exact target is

`T=(-6,12,0,0,-6,0,0,-18,0,18)/625`.

At the finest extraction require per-lane

`abs(trace_eta(L2_j)-T_j) / max(abs(T_j), ||L2_j||_F, 1e-10) <= 1e-2`

and aggregate vector residual <= `5e-3`.

No per-component sign/scale adjustment is allowed.

I. Result reporting: record `L2` norm/singular values/numerical rank, trace vector, and action on the two-dimensional non-gauge Einstein null complement. No desired `L2` rank/sign is a PASS criterion.

## Production rule

Maximum scientific authority requires a **fresh production under this corrected frozen contract**. Historical Iter057F raw measurements may be used only for diagnosis or implementation verification, not as the sole production evidence for F2 PASS.

Implementation-only performance caching is allowed iff it is algebraically identical to the corrected five-point operator and is verified on a frozen equality control before production. No lower-accuracy stencil or reduced frequency panel is allowed.

## Frozen classifications

Maximum PASS:

`PASS_SCOPED_ITER057F2_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_CORRECTED_EXACT_CONTROLS`.

INVALID:

`INVALID_ITER057F2_FULL_EOM_EXTRACTION_OR_CORRECTED_CONTROL`.

No scientific FAIL is tied to a preferred `L2` rank/sign.

## Interpretation ceiling

This remains a finite-precision local extraction at one source-owned background point and null covector. It does not establish the full characteristic variety, hyperbolicity, physical cone splitting, ghost content, stability, energy, treatment selection, unitarity or UV completion.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.