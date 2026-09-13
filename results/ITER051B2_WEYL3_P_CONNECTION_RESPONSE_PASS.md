# Iter051B2 — Weyl^3 P connection-response terminal result

Date: 2026-09-13
Gate: `ITER051B2-WEYL3-P-CONNECTION-RESPONSE`

## Authority
- Prospective preregistration: `cffde199b9cd885f4d07238b8c46fdee3f966143`
- Historical initial head: `a9884403a7969d53f284f3195bea37f4ad5bbc62`
- Historical initial run: `34736978191`
- Historical initial frozen classification: `SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE` (1/4 valid/pass), retained permanently.
- Numerical-only repair: `b2d1ade45c3507e87541aaf86a304b3cbb54dbc5`
- Authoritative retry head: `0d0796cc3751f31012afc04684b5836cbf580755`
- Authoritative retry run: `34737103399`
- Aggregate job: `103670518127`
- Summary artifact: `10312171778`
- Summary digest: `sha256:f076eb8a61bd2e0cc6d648533737aca349e28c14c3cb39f1f465e857442bf568`

## Frozen retry result
`PASS_SCOPED_WEYL3_P_CONNECTION_RESPONSE_CERTIFICATE`

- artifact rows: 4/4
- valid: 4/4
- pass: 4/4
- parse errors: none

Worst frozen controls/targets:
- `P_jet_algebraic = 3.469446951953614e-17 <= 2e-10`
- `P_jet_reference_convergence = 2.4973661811983306e-07 <= 2e-5`
- `direct_final_step_change = 2.096266935658004e-07 <= 1e-5`
- `direct_vs_reference_finest = 2.5069984569780767e-07 <= 2e-5`
- `D_covariance = 5.753870859922338e-16 <= 2e-7`
- `P0_direct_covariance = 3.4830092046971933e-15 <= 2e-9`
- `max_inverse_residual = 4.440892098500626e-16 <= 1e-11`
- `zero_curvature_P_norm = 2.7216552697590953e-61 <= 2e-10`
- minimum direct/reference D norms remain safely above `1e-6`.

Raw lane artifact IDs/digests consumed by the frozen aggregate:
- lane 0: `10311153952`, `sha256:e9df44e7252be2c033165a9e0835a6c33af5e7073fb9af0174b8d3db82bcef0d`
- lane 1: `10310779544`, `sha256:665e1a3fa311baab004cee0b4be6a3f103d9ef221864e09bc463535e05848406`
- lane 2: `10311033985`, `sha256:3cc6ba8338ba7abace263b787cdd1479cb6c5c4c0d7f11c7d4fb904a5bdc361a`
- lane 3: `10311371494`, `sha256:694c347a0bb7d9580abaccd763795160c7c79f29e5bfa86a178f74c0ddf98a0f`

## Interpretation
This is a scoped numerical certificate for the actual Weyl^3 `P(R,g)` connection-response / covariant double-divergence layer on the frozen finite jet panel. It is not by itself a complete four-dimensional covariant Weyl^3 Euler-Lagrange tensor theorem. The final metric-consistent assembly/covariance/identity gate remains required.

The initial frozen failure is not overwritten: it was caused by finite-difference second-P-jet drift outside the exact linear algebraic-Riemann subspace. The retry changed only the mathematically exact reprojection of derivative jets and preserved seeds, stencils, thresholds, scientific target and interpretation.

## Claim locks
Theory established remains 0%. `c6` remains unfixed. `beta=1` remains unauthorized. No experimental confirmation, absolute-energy positivity, quantum unitarity, or KMQGB `NEW_REQUIRED` claim follows from this result.
