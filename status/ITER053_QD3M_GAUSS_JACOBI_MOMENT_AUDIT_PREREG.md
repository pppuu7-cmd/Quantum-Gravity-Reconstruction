# Iter053-QD3M prospective implementation audit — Gauss-Jacobi weighted moments

Frozen before QD3M implementation or production evidence.

## Gate
`ITER053-QD3M-GAUSS-JACOBI-MOMENT-NORMALIZATION-AUDIT`

## Purpose
Independently audit the numerical normalization used by Iter053-QD3 without evaluating H5 and without changing any Iter053/QD3 scientific threshold. This is an implementation/mathematics control only.

For weight `w(u)=(1-u^2)^4` on `[-1,1]`, exact moments are
- odd powers: zero;
- even powers `u^(2k)`: `Beta(k+1/2,5)`.

The physical map `x=a u`, `a=0.24`, contributes exactly `a^4` in four dimensions.

## Frozen tests
For scipy `roots_jacobi(n,4,4)`, separately for n=2 and n=3:
1. all nodes strictly inside (-1,1), all weights positive;
2. node/weight reflection symmetry residual <= 5e-15;
3. every 1D polynomial moment degree `0..(2n-1)` agrees with the analytic beta-function moment to absolute error <= 5e-14;
4. tensor-product constant moment equals `[Beta(1/2,5)]^4` to relative error <= 5e-14;
5. mapped physical constant integral equals `a^4 [Beta(1/2,5)]^4` to relative error <= 5e-14;
6. the production helper `qgr_iter053_qd3_gauss_jacobi_bulk_pilot.gj_tasks(n)` has exactly n^4 tasks and the sum of its physical weights agrees with the analytic mapped constant integral to relative error <= 5e-14.

## Frozen classes
- `PASS_DIAGNOSTIC_ITER053_QD3_GAUSS_JACOBI_MOMENTS_EXACT`
- `FAIL_DIAGNOSTIC_ITER053_QD3_GAUSS_JACOBI_MOMENT_NORMALIZATION`

## Interpretation lock
This audit cannot establish or reclassify Iter053 or QD3 scientific status. It only validates/falsifies quadrature normalization and polynomial exactness for the already-frozen QD3 implementation. No H5 evaluation, no seed changes, no threshold changes. `c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.
