# Outcome-independent implementation plan for a possible corrected full Iter053 replacement

Date: 2026-09-14
Status: **implementation planning only**. This is not a preregistration, not an authorization to launch a new scientific gate, and contains no partial substantive evidence from active Iter053T productions.

## Purpose

If and only if the two independently preregistered active Iter053T companion gates terminally support the source-faithful corrected weighted pushforward, the next candidate gate should be a distinct prospectively preregistered full A4+B2+C2 replacement of Iter053R.

The historical Iter053R result remains permanently `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`.

The replacement must preserve the original Iter053R scientific object, seeds, quadrature orders, direct derivative stencil, H5 derivative step, controls, thresholds and interpretation ceiling. The only implementation correction should be the transformed C weighted polynomial-factor extraction.

## Minimal code-level correction

The Iter053R reducer currently conflates two different objects:

1. the full compact perturbation used by direct variation / signature / collar controls;
2. the unfactored polynomial tensor source used after the compact bump has already been absorbed into the Gauss-Jacobi measure.

The replacement should make this distinction explicit.

### Recommended reducer interface

Replace the implicit extraction

`p = base_pert.base.jets(u)[0]`

inside `weighted_bulk` by an explicit polynomial source, e.g.

`weighted_bulk(metric, poly_source, order, u_to_coord=None, p_transform=None, sample=False)`

with

`p = poly_source.jets(u)[0]`.

No other H5, Gauss-Jacobi or geometric operation should change.

### A/B lanes

For all A and B lanes:

- direct perturbation object remains `pert = CompactPerturbation(seed)`;
- polynomial source passed to weighted integration is exactly `pert.base`;
- `p_transform=None`;
- all direct GL7/GL8, epsilon, signature, inverse, collar, null, W3/P/H5 and wrong-sign controls remain byte-for-byte semantically equivalent to Iter053R.

Thus A/B must be unchanged scientifically and should act as regression controls against accidental broad refactoring.

### C base side

For the base frame:

- direct perturbation remains `pert`;
- weighted polynomial source is `pert.base`;
- geometry is evaluated at `u`;
- no tensor transform is applied to the polynomial source.

### C transformed side

For the transformed frame:

- direct perturbation remains `pt = TransformPerturbation(pert,L)`;
- direct/support/collar controls continue to evaluate `pt` at `y=L^-1 u` exactly as in Iter053R;
- transformed metric remains `mt = TransformMetric(metric,L)`;
- weighted geometry is evaluated at `y=L^-1 u`;
- weighted polynomial source must be the **original unfactored** `pert.base`, evaluated at source parameter `u`;
- only then apply `p_transform(p)=L^T p L`;
- exactly one external Gauss-Jacobi compact-support weight is used.

In particular, the replacement must never use `pt.base.jets(u)` to obtain the reduced polynomial factor.

## Scientific-contract invariants to preserve

A future preregistration, if authorized, should inherit the original Iter053R contract without relaxation:

### Panel

- A4 generic compact-support 4D lanes;
- B2 conformally-flat/null lanes;
- C2 determinant-one coordinate-covariance lanes;
- same seeds and same shears as Iter053R;
- no seed selection, dropping or replacement.

### Integration and derivative inputs

- support radius `A=0.24`;
- weighted H5 GJ2 and GJ3, Jacobi `alpha=beta=4` in all four coordinates;
- direct support-domain GL7 and GL8;
- symmetric epsilon stencil `(2e-4,1e-4,5e-5)` with finest `5e-5`;
- H5 coordinate derivative step `5e-4`.

### Original validity controls

- Lorentzian signature at all required nodes/epsilon points;
- maximum inverse residual `<=3e-11`;
- all scored outputs finite;
- compact-support collar control `<=1e-13`;
- C: `|det L-1|<=2e-12`;
- C transformed metric/perturbation algebra residual `<=3e-11`.

### Original A thresholds

- `|direct_GL8| >= 1e-10`;
- final epsilon step change `<=5e-4`;
- direct GL7->GL8 relative change `<=5e-4`;
- weighted H5 GJ2->GJ3 relative change `<=2e-3`;
- fine direct_GL8 vs bulk_GJ3 relative residual `<=3e-3`;
- coarse-to-fine identity-residual absolute change `<=3e-3`.

### Original B thresholds

- `|direct_GL8| <=5e-8`;
- `|bulk_GJ3| <=5e-8`;
- sampled `|W3| <=2e-10`;
- sampled `||P|| <=3e-9`;
- sampled `||H5|| <=3e-7`.

### Original C thresholds

- both frames independently satisfy applicable A thresholds;
- direct integrated covariance residual `<=2e-3`;
- weighted H5 bulk covariance residual `<=2e-3`.

### Original negative control

For every generic A lane retain

`H5_wrong = A + I + 2 sqrt(-g) D5`.

Require:

- wrong-sign residual larger than correct-sign residual on every A lane;
- at least one A lane wrong-sign residual `>=1e-2`.

No sign scan, coefficient fit or lane-specific convention is allowed.

## Recommended parallel execution architecture

A future authorized workflow should maximize independent hosted-runner parallelism without changing lane semantics:

- matrix jobs A0, A1, A2, A3;
- matrix jobs B0, B1;
- for C0 and C1, either one self-contained job per C lane or independent predeclared base/transformed computational subjobs followed by a deterministic per-C combiner; if split, the C scientific verdict must still be computed only after both frozen sides are present;
- `fail-fast:false` everywhere;
- one frozen aggregate after every required A/B/C artifact is terminal;
- no partial lane values used to alter another lane;
- raw artifact and digest retention for every lane and the aggregate.

For simplicity and lower provenance risk, one job per C lane remains preferable unless wall-clock evidence shows the two sides should be split. If split is chosen, that architecture must itself be frozen before substantive execution.

## Regression / object-identity controls recommended for the future preregistration

Without changing the original scientific thresholds, the replacement can add implementation-validity controls that are logically implied by the intended object:

1. A/B weighted results must be generated through the explicit `poly_source=pert.base` path, demonstrating no hidden wrapper-depth dependency.
2. C transformed reducer should record the class/object identity of the polynomial source and confirm it is the underlying `Perturbation`, not `CompactPerturbation` or `TransformPerturbation`.
3. At frozen non-substantive structural test nodes, verify the replacement polynomial factor equals `L^T pert.base.jets(u)[0] L` exactly to numerical roundoff.
4. Retain the historical legacy extraction only as an optional implementation negative control; it must not be substituted for or mixed into the corrected scientific integral.

These controls should classify object-path mismatch as INVALID rather than as a physical scientific FAIL.

## Interpretation ceiling

Even if a future full corrected A4+B2+C2 replacement terminally passes, it would be only a finite genuinely four-dimensional compact-support computational certificate for the Weyl3 functional-variation object under the frozen panel. It would not be a global functional derivative theorem, quantum amplitude/measure closure, unitarity, UV completion, full GR recovery, experimental confirmation, new physics, fixed `c6`, authorization of `beta=1`, or theory establishment.

## Current lock

Do not convert this plan into a preregistration or launch while either active Iter053T companion production is non-terminal. Their terminal outcomes determine whether the full corrected replacement is scientifically admissible at all.
