# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — internal construction-roadmap readiness only, not correctness probability and not fraction of quantum gravity solved. The increase 98 -> 99 is credited only to terminal Iter050 closure of the first generic non-symmetry-reduced curvature-direction/P-tensor prerequisite.
- Iter005–Iter050: completed in their stated scopes.
- Theory established: **0%**.
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter050 — covariant curvature-direction prerequisite
Durable record: `results/ITER050_WEYL3_COVARIANT_CURVATURE_DIRECTIONAL_VARIATION_PREREQUISITE.md`.

Frozen gate preregistered at `f711706587c3119a0b50d42deed8d188bc6cbcef`; implementation `60da97ddb8afa3b293c22fef1c8af530b476bf9e`; frozen aggregate `a6245ccb401d2caca3cc5d660d45d4b3cbda1d93`; authoritative production head `aff866ef2437b38e0981ee11f3d3b759c1710423`.

Authoritative terminal provenance:
- run `34721494038`;
- aggregate job `103628161706`;
- aggregate artifact `10305494635` (`qgr-iter050-summary`);
- digest `sha256:b61db7ae72d17071fff8790c5dc7029f9c67ec01cb4d2714bbc18fcaa219fb2e`;
- 12/12 frozen scientific lanes consumed and passed.

Aggregate extrema:
- max algebraic residual `5.551115123125783e-17`;
- max Weyl-trace residual `5.551115123125783e-17`;
- max scalar Lorentz-covariance relative discrepancy `1.6429934460979685e-14`;
- max directional-derivative covariance relative discrepancy `5.173731054391887e-14`;
- max finest-step analytic-vs-FD relative discrepancy `7.310078440487533e-08`;
- nonzero calibration `12/12`.

Terminal classification:
`PASS_SCOPED_COVARIANT_WEYL3_CURVATURE_DIRECTIONAL_VARIATION_PREREQUISITE`.

This is a genuine non-symmetry-reduced fixed-metric curvature-direction/P-tensor certificate for the local Weyl-cubic invariant on the frozen generic panel. It is **not** the complete metric functional derivative of `sqrt(-g) C^3`: metric variation of the measure/projectors and the covariant double-divergence sector remain outside Iter050.

## Current frontier — Iter051
Do not start another symmetry reduction. The next high-information programme is a full four-dimensional covariant metric-functional-derivative certificate for `sqrt(-g) C^3` with symbolic `c6`.

Planned gate: `ITER051-WEYL3-FULL-COVARIANT-METRIC-FUNCTIONAL-DERIVATIVE-CERTIFICATE`.

The gate must be prospectively preregistered before implementation and must explicitly separate at least two independently controlled ingredients:
1. algebraic metric/measure/projector variation of the Weyl-cubic density;
2. the covariant derivative contribution built from the curvature derivative/P-tensor, including the double-divergence structure.

No complete covariant Weyl^3 Euler-Lagrange claim is allowed if either component is missing, invalid, numerically unresolved, or only symmetry-reduced.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` remains unfixed;
- Iter050 is a prerequisite, not the full 4D covariant six-derivative field equation;
- finite panels and symmetry-reduced calculations are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
