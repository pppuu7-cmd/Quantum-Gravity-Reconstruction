# Iteration 050 — terminal covariant Weyl^3 curvature-directional prerequisite

Date: 2026-09-13

## Frozen authority
- Preregistration commit: `f711706587c3119a0b50d42deed8d188bc6cbcef`
- Implementation commit: `60da97ddb8afa3b293c22fef1c8af530b476bf9e`
- Frozen aggregate commit: `a6245ccb401d2caca3cc5d660d45d4b3cbda1d93`
- Authoritative production head: `aff866ef2437b38e0981ee11f3d3b759c1710423`
- Run: `34721494038`
- Aggregate job: `103628161706`
- Aggregate artifact: `10305494635` (`qgr-iter050-summary`)
- Artifact digest: `sha256:b61db7ae72d17071fff8790c5dc7029f9c67ec01cb4d2714bbc18fcaa219fb2e`

## Frozen classification
`PASS_SCOPED_COVARIANT_WEYL3_CURVATURE_DIRECTIONAL_VARIATION_PREREQUISITE`

All 12/12 preregistered generic non-symmetry-reduced lanes passed the frozen gate and all controls. Aggregate extrema:
- max algebraic-curvature residual: `5.551115123125783e-17` (`<=1e-11` frozen threshold);
- max Weyl-trace residual: `5.551115123125783e-17` (`<=1e-10`);
- max Lorentz scalar-covariance relative discrepancy: `1.6429934460979685e-14` (`<=1e-9`);
- max analytic directional-derivative covariance relative discrepancy: `5.173731054391887e-14` (`<=1e-8`);
- max finest-step analytic-vs-centered-FD relative discrepancy: `7.310078440487533e-08` (`<=2e-6`);
- nonzero calibration lanes: `12/12` (frozen minimum `10/12`).

The aggregate consumed all 12 lane artifacts and reproduced their recorded SHA256 digests before classification.

## Scientific interpretation
This closes a genuine non-symmetry-reduced fixed-metric curvature-direction/P-tensor prerequisite for the local Weyl-cubic invariant on the frozen four-dimensional algebraic-curvature panel. It independently validates the cubic directional derivative, finite-difference convergence, Lorentz-basis covariance, algebraic-curvature/Weyl-trace controls, conformally-flat null calibration, and nontrivial activation.

It does **not** establish the complete metric functional derivative of `sqrt(-g) C^3`: metric variation of the measure/projectors and the covariant double-divergence contribution remain outside Iter050. It is not a global theorem and does not fix `c6`.

## Claim locks preserved
- theory established = `0%`;
- no experimental confirmation;
- `beta` remains an explicit matching/calibration parameter and `beta=1` is not authorized as physics;
- `c6` remains symbolic and unfixed;
- finite panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical multiple-branch weights;
- KMQGB `NEW_REQUIRED` remains unauthorized.

## Next permitted gate
A prospectively preregistered full covariant metric-functional-derivative programme for `sqrt(-g) C^3`, explicitly separating the algebraic metric/measure variation from the derivative `nabla nabla P` sector and requiring an independent directional-variation certificate before any full-EOM claim.
