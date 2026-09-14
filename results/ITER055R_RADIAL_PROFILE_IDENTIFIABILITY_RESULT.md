# Iter055R terminal result — radial-profile identifiability on spacelike B3

Date: 2026-09-14
Preregistration: `ab11ba41f8f8ef9e272888cdfcf5eafd8bcba9df`

## Terminal classification

`PASS_SCOPED_NONUNIQUENESS_ITER055R_RADIAL_PROFILE_REMAINS_INFINITE_DIMENSIONAL_NEW_PROFILE_INPUT_REQUIRED`

## 1. Covariance/refinement constrain scaling, not the dimensionless shape

On the Iter055P spacelike-B3 scope, the radial envelope class is

`phi_(h,n)(k)=h f(h n.k)`

with future-timelike unit normal `n` and

`integral_0^infinity s |f(s)|^2 ds < infinity`.

Lorentz covariance follows because `n.k` is a scalar when `n` and `k` transform together. Refinement `h -> h/r` is the unitary cone dilation already derived in Iter055P. Neither statement imposes a differential or integral equation that selects one normalized `f`.

Thus, at the class level, the normalized shape lives on the unit sphere of the infinite-dimensional weighted Hilbert space

`L2(R_+, s ds)`.

## 2. Two exact inequivalent normalized witnesses

Define

`f0(s)=2 exp(-s)`.

Then

`integral_0^infinity s |f0(s)|^2 ds = 4 * integral s exp(-2s) ds = 1`.

Define

`f1(s)=sqrt(8/3) s exp(-s)`.

Then

`integral_0^infinity s |f1(s)|^2 ds = (8/3) * integral s^3 exp(-2s) ds = (8/3)*(3/8)=1`.

The ratio `f1/f0` is proportional to `s`, so the two profiles are not related by an overall phase or normalization. Both generate bounded normalized smearing families with the same Lorentz-covariance and refinement-dilation law.

Therefore existing class-level constraints admit at least two operationally distinct profiles and in fact an infinite-dimensional family.

## 3. Existing G6H controls independently support profile freedom

The G6H broadband machinery explicitly validates more than one radial benchmark profile (`m0` and `m1`) and reproduces the corresponding exact normalized envelope overlaps. Its source does not select one as universal; it uses them as preparation/readout profiles.

This historical control is consistent with the exact function-space result: the one-particle observable machinery is compatible with multiple radial shapes.

## 4. Existing locality authority does not collapse the family

G6C/G6E locality fixes region restriction, shared-B3 matching, fiber-product support and measure disintegration. It does not impose a source-defined equation on the momentum-space radial shape `f`.

Iter055M already found no source-defined compact-support, finite-element, Gaussian, detector or refinement kernel that could supply such an equation. Importing the Iter053 bump or a G6G/G6H preparation profile would be post-hoc profile selection.

Hence locality/refinement/covariance, as currently defined, do not reduce the radial profile to one equivalence class.

## Scientific consequence

On spacelike B3 boundaries the bridge architecture is now separated into:

- **derived:** relational timelike normal anchor;
- **derived:** symbolic-`h` norm-preserving scale/refinement law;
- **not derived:** dimensionless radial profile shape `f`;
- **not derived:** angular/polarization/tensor kernel and B3 observable attachment;
- **not derived:** absolute physical calibration of `h`.

The profile shape is therefore explicit new bridge input unless a new independent physical principle is added prospectively.

A successor gate should not merely choose a convenient `f`. It should identify a candidate-owned principle capable of ranking/falsifying profile families — for example a source-locality/minimal-resolution/moment condition if such a principle can be independently motivated — and calibrate it against negative controls before examining desired dynamics.

## Claim ceiling

No preferred radial profile, concrete complete kernel, all-boundary bridge, interacting dynamics, absolute `h`, beta/c6 fixing, Weyl3 treatment, regulator removal, full unitarity, UV completion, GR recovery, experiment or theory establishment follows. Theory established remains 0%.

No GitHub Actions run was required; the result is exact function-space analysis.
