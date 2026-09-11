# QGR Iter007 G7A — Microscopic scale identifiability

Date: 2026-09-12
Status: `BLOCKED_SCOPED_ABSOLUTE_MICROSCOPIC_SCALE_NOT_IDENTIFIABLE_FROM_CURRENT_QGR_NORMALIZATION_CHAIN`

## Objective

After G6H closed a normalized model-side broadband two-mode comparator for specified preparations, determine whether the current QGR chain fixes the physical microscopic cell scale `h` strongly enough to turn the dimensionless/refinement `O(h^4)` result into an absolute phenomenological number.

## Reproducibility

GitHub Actions run `34659176245`: four lanes plus aggregate `SUCCESS`.

An earlier run `34659076333` failed closed because one lightweight rank script unnecessarily imported NumPy although the workflow intentionally had no NumPy dependency. The criterion was not changed; the script was replaced by dependency-free exact elementary arithmetic and the new run passed.

## G7A-1 — four-dimensional refinement power counting

The QGR response/metric fluctuation is dimensionless in the current continuum matching. One first difference obeys

`Dq ~ h partial q`.

The microscopic quadratic action contains two first differences,

`S_micro^(2) ~ kappa sum_cells (Dq)^2`,

while the number of four-cells in a fixed physical four-volume scales as

`N_cells ~ h^-4`.

Therefore

`S_micro^(2) -> (c_geom kappa / h^2) integral d^4x (partial q)^2`,

where `c_geom` is the fixed geometric conversion factor associated with the precise cell/continuum convention.

Thus the continuum Einstein-Hilbert normalization has the form

`a_cont = c_geom kappa / h^2`.

The exponent of `h` is fixed by the already selected four-dimensional refinement structure; the exact numerical `c_geom` is not needed for the identifiability result below.

Classification:
`PASS_SCOPED_DIMENSIONAL_REFINEMENT_MATCHING_FIXES_CONTINUUM_NORMALIZATION_ONLY_THROUGH_KAPPA_OVER_H2`.

## G7A-2 — rank-one identifiability

In logarithmic microscopic parameters,

`log a = const + log kappa - 2 log h`.

The normalization Jacobian is the one-row matrix

`[1, -2]`,

with rank exactly one. Its null direction can be taken as

`(delta log kappa, delta log h)=(2,1)`.

Equivalently,

`h -> lambda h`,
`kappa -> lambda^2 kappa`

leaves the continuum gravitational normalization unchanged.

Classification:
`BLOCKED_SCOPED_CONTINUUM_GR_NORMALIZATION_ALONE_CANNOT_IDENTIFY_KAPPA_AND_H_SEPARATELY`.

## G7A-3 — the broadband history effect resolves the same direction but cannot calibrate itself

The leading normalized G6H history correction scales as `h^4` for all tested specified broadband preparations. Along the exact continuum-normalization degeneracy,

`h^4 -> lambda^4 h^4`.

Hence two microscopic realizations with the same continuum GR normalization can predict different absolute magnitudes of the history correction.

This makes the broadband correction a genuine second-scale probe, but not an absolute prediction until either `kappa` or `h` is independently fixed.

Classification:
`BLOCKED_SCOPED_H4_HISTORY_AMPLITUDE_VARIES_ALONG_THE_EXACT_CONTINUUM_NORMALIZATION_DEGENERACY`.

## G7A-4 — authority audit

The authoritative microscopic action record `ITER003_G5_PAIR_ACTION.md` explicitly retains one overall coefficient `kappa` and states that it is the only free overall normalization/coupling at that stage.

The later all-orders local action inherits the selected quadratic normalization; it does not independently derive an absolute microscopic length.

No existing authoritative QGR result fixes `kappa` or identifies `h` with a physical Planck length.

Classification:
`BLOCKED_SCOPED_AUTHORITATIVE_QGR_CHAIN_STILL_CONTAINS_ONE_FREE_OVERALL_MICROSCOPIC_NORMALIZATION_AND_NO_DERIVED_ABSOLUTE_H_RULE`.

## Consolidated conclusion

The current QGR construction predicts, in scope,

- the existence and structure of the 24-history correction;
- its normalized channel/readout construction;
- its robust `O(h^4)` refinement order on the repaired finite-curvature benchmark;
- preparation/readout dependence of its numerical coefficient.

It does **not** yet predict the absolute physical value of `h`, because the low-energy gravitational normalization fixes only `kappa/h^2`.

Therefore setting `h=l_P`, setting `kappa=1` as a physical statement, or quoting an experimental decoherence/Lorentz-violation rate from G6H would be an additional hypothesis and is not authorized.

## Next gate

`G7B_MICROSCOPIC_NORMALIZATION_PRINCIPLE_OR_MATTER_COUPLING_SECOND_SCALE`

Two legitimate routes can lift the one-dimensional degeneracy without post-hoc calibration:

1. derive a microscopic quantum/amplitude normalization that fixes `kappa` from the same CCRC realization; or
2. derive a universal matter/detector coupling that supplies a second independent physical-scale relation.

Fail closed if either route requires declaring `h` to be the Planck length by convention or fitting `kappa` solely to obtain a desired observable magnitude.
