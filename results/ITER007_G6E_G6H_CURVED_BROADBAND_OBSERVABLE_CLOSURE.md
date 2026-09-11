# QGR Iter007 G6E-G6H — Curved physical pairing and broadband observable closure

Date: 2026-09-12
Status: `PASS_SCOPED_CURVED_CHARACTERISTIC_HILBERT_PLUS_NORMALIZED_BROADBAND_TWO_MODE_COMPARATOR / ABSOLUTE_SCALE_OPEN`

## Scope

This record consolidates the post-G6D observable/readout work. It does not claim experimental confirmation, a universal decoherence coefficient, or an absolute physical microscopic scale.

## G6E — convention repair and positive physical pairing

GitHub Actions run `34657301235`: five lanes plus aggregate `SUCCESS`.

A convention drift between the earlier contravariant incidence form `C=J-I` and the covariant response seed was audited explicitly. The unique simple S4-equivariant bridge used here is

`S = I - J/6`,

with

`S^T C S = C^-1 = E`.

The finite-curvature torsion/history calculation was then rerun microscopically with the Iter005-consistent covariant seed `E=C^-1`, rather than merely relabeling indices.

On the repaired G9 branch the refinement slopes were

- relative history trace RMS: `4.070548027603509`;
- common-target null Gram RMS: `4.098438841731989`;
- branch-pair barycentric rapidity scalar RMS: `4.0685627405001945`.

Thus the previously observed history splitting remains `O(h^4)` after the same-realization convention repair.

The trace-reversed covariant bilinear on symmetric perturbations has the four derivative-gauge directions as its exact radical on the six-dimensional characteristic kernel and leaves a positive two-dimensional quotient. Hence the physical characteristic space has a positive finite-frame-covariant pairing without inserting a branch-dependent polarization basis.

A relational timelike-screen construction gives a concrete representative/readout of the same two modes but is not promoted as a new fundamental norm.

For overlapping regular regions, a positive finite measure admits disintegration over the common B3 boundary pushforward. Conditional independence is neither required nor inferred.

## G6F — normalized characteristic wavepackets

GitHub Actions run `34657631926`: three lanes plus aggregate `SUCCESS`.

The invariant future-null-cone measure and the positive two-mode quotient pairing define a common target characteristic direct-integral Hilbert space on the regular one-particle/readout domain.

For two normalized Lorentz-covariant envelope families, exact branch overlaps are

`A_0(gamma)=2/(1+gamma)`

and

`A_1(gamma)=4(2+gamma)/(3(1+gamma)^2)`.

The continuous packet scale cancels from the normalized overlap, while the profile does not. On repaired G9 the normalized history-mixture envelope losses have slopes

- `m0`: `4.070780612231773`;
- `m1`: `4.070701231283697`.

The fine-scale coefficient ratio tends to `1.333333315328487`, i.e. the analytic `4/3` ratio. Therefore the `h^4` refinement order is robust across these preparations, while the coefficient is preparation dependent.

## G6G — polarization holonomy

GitHub Actions run `34657905251`: three lanes plus aggregate `SUCCESS`.

For relative branch Lorentz holonomies on repaired G9:

- Lorentz Lie-generator RMS slope: `2.0290239063330713`;
- quadratic Casimir `r^2-b^2` slope: `4.054146011907256`;
- quadratic Casimir `r.b` slope: `4.049341788512877`;
- finite trace-defect slope: `4.054213669711921`.

In a fully specified relational detector/standard section, the central-ray Wigner-angle spread has slope `1.9763871610069832`. A fixed linear spin-2 preparation therefore has pair-overlap loss slope `3.952583281626355`.

Combining the normalized envelope with this specified polarization in the narrow-packet approximation gives slope `4.005063892783682`.

This closes a scoped polarization comparator but still leaves a central-ray approximation and preparation-dependent coefficient.

## G6H — full broadband coherent two-mode integral

GitHub Actions run `34658915788`: four lanes plus aggregate `SUCCESS`.

The radial future-null-cone integral is performed analytically, so no arbitrary UV momentum cutoff enters the normalized comparator. A compact angular quadrature was independently validated against the exact G6F envelope overlaps.

For every target null direction and every one of the 24 histories, the calculation recomputes

- the branch-dependent source momentum;
- the finite little-group/Wigner element;
- the physical spin-2 rotation;
- the normalized branch overlap.

Thus the G6G narrow-packet approximation is removed.

Full broadband coherent two-mode history-mixture loss slopes are

- radial profile `m0`: `4.034237010354219`;
- radial profile `m1`: `4.034735702727535`.

For the `m0` profile, changing the prepared/readout polarization gives

- envelope-only control: `4.092362452141089`;
- fixed linear spin-2: `4.05492344294805`;
- definite helicity: `4.059195890628427`.

All tested normalized broadband preparations therefore retain the same scoped `O(h^4)` refinement order, while their coefficients remain preparation/readout dependent.

## Consolidated classification

`PASS_SCOPED_CONVENTION_REPAIRED_CURVED_TWO_MODE_POSITIVE_PAIRING_COMMON_CHARACTERISTIC_HILBERT_AND_CUTOFF_FREE_BROADBAND_24_HISTORY_COMPARATOR_WITH_ROBUST_H4_REFINEMENT_ORDER`.

## What is now closed in scope

- the C versus C^-1 convention inconsistency for the tested same-realization finite-curvature chain;
- a positive covariant two-dimensional characteristic quotient pairing;
- regular B3 boundary measure disintegration;
- common-target characteristic Hilbert construction;
- normalized finite-history wavepacket overlaps;
- physical polarization/Wigner transport in a specified detector section;
- full momentum-dependent broadband two-mode integration without a momentum cutoff;
- repeated numerical confirmation that the first normalized history-mixture loss is `O(h^4)` on the repaired G9 refinement sequence.

## What remains open

The coefficient of a physical experiment is not a universal number. It depends on preparation/readout, as expected for an observable comparator. More importantly, the current QGR normalization chain has not yet fixed the absolute physical cell scale `h` separately from the overall microscopic normalization `kappa`.

Therefore no experimental decoherence rate, Lorentz-violation magnitude, or Planck-scale numerical prediction is authorized by G6E-G6H alone.

Next gate: `G7A_MICROSCOPIC_SCALE_OR_MATTER_DETECTOR_COUPLING_CLOSURE`.
