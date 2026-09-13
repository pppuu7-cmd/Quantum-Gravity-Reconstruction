# Iter051A-D2 — Complex-step comparator stability

Date: 2026-09-13
Status: **TERMINAL DIAGNOSTIC PASS (scoped)**
Classification: `DIAGNOSTIC_COMPLEX_STEP_STABLE_3_OF_3`

## Frozen question
For the three original G51A failing lanes not localized by D1 (`0,2,9`), test the complex-step derivative comparator at epsilons `1e-16,1e-20,1e-24,1e-28,1e-30`, retaining inherited algebraic and directional-covariance controls. This diagnostic cannot retroactively promote terminal G51A.

## Authoritative provenance
- preregistration: `3e4fdf397afc060b02250c26be30af21f0ba6ef4`
- implementation: `730a57552e0924943246aa2c97ffb3d5ab1a5c42`
- aggregate implementation: `e474d56d14731d7ac63f2987800e491492a9458e`
- authoritative head/run trigger: `1dc54a4d312bb4fa63d45ef8fecbe3a1fcb6e1af`
- run: `34726732537`
- aggregate job: `103642066679`
- aggregate artifact: `10307943436`
- aggregate digest: `sha256:2a0e90b2a6f3cdfc64f44fdce879062dd43419bfed36e1f87b97cd612888ac4c`

## Frozen aggregate result
- found lanes: `3/3`
- passes: `3/3`
- lane ids: `[0,2,9]`
- max relative spread across complex-step epsilons: `8.771226570866013e-15`
- max inherited directional-covariance relative residual: `6.224741437388768e-15`

## Scientific interpretation
The complex-step comparator is stable on all three D1-unlocalized lanes under the prospectively frozen epsilon audit. Therefore the remaining unexplained G51A failures are not attributable to instability of the complex-step reference at the tested epsilons. Combined with D1, the evidence supports designing a **new, independently preregistered high-precision G51A-class certificate** rather than weakening the failed float64 centered-FD convergence predicate.

This result does **not** change the terminal classification of Iter051A: `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION` remains authoritative. It does not establish the full covariant Weyl^3 metric Euler-Lagrange tensor and gives no credit to G51B.

## Claim locks
- theory established = 0%;
- `c6` remains unfixed;
- `beta=1` remains unauthorized;
- no experimental confirmation;
- no global theorem from finite panels;
- KMQGB `NEW_REQUIRED` remains unauthorized.
