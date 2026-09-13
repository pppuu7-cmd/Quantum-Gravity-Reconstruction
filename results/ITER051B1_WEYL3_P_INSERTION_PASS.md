# Iter051B1 — Weyl^3 P-Insertion Certificate

Date: 2026-09-13

## Frozen gate
`ITER051B1-WEYL3-P-INSERTION-CERTIFICATE`

Prospective preregistration was committed before implementation and production:
- preregistration commit: `cbaf060790e56e4fed27290651c40104cdbbf7d9`
- implementation commit: `2e6f2b2430061f3d770ba727ede83d542ede5057`
- aggregate implementation commit: `25c02c988e60a97476f51f2f1fdb047d8edd0169`
- authoritative workflow/head: `d1f066538f18bc058564eb74a623a701295592aa`

## Authoritative production
- run: `34736761744`
- aggregate job: `103669479104`
- summary artifact: `10311710726`
- summary digest: `sha256:6ea83543ff58b2ac42bd02e166fed3534f37f09459e6cd55616ac1c4090fd3f0`
- structurally valid lanes: `8/8`
- PASS lanes: `8/8`

All eight raw lane artifacts were downloaded by the frozen aggregate and their artifact identities/digests were verified. Direct raw lane logs inspected were consistent with the aggregate and showed all frozen booleans true; no lane-level anomaly was found.

Raw lane artifacts:
- lane 0: artifact `10311322081`, digest `sha256:6c7cf5eecb8fb57c4529e91f35d2b4caf820dc57cd0e52784d1f25213a284191`
- lane 1: artifact `10311685362`, digest `sha256:f1cb080a20fb7434b39b997b6c202d817eb359e0b8a48197199893d13e8c685f`
- lane 2: artifact `10311356073`, digest `sha256:6d92bcd438ba7db2050c38e0bb44bfdb93f795d591eef0c24b4d9e19d17fb5f6`
- lane 3: artifact `10311222870`, digest `sha256:43f7d00299f2c9af96e22224cd0bc264f96b792c37d9a27e12593429d5fc2bb1`
- lane 4: artifact `10310873955`, digest `sha256:cb8c710bbd6b1eb7b4bfa561ee32a9139869f65221a1b77e85b68b7031664757`
- lane 5: artifact `10311570517`, digest `sha256:d324ff6f3c554e57421ed09ce8b7815f86f7e822179418321d3b93785a46c9cc`
- lane 6: artifact `10310589579`, digest `sha256:c53f9b946662f21584c91b6afd3c3582d482562a7f850b84479144c5c5631cb7`
- lane 7: artifact `10311635459`, digest `sha256:93f5b01f6ad062c35d1d7a14340700d184d660dac57e7693774be0902b52c72d`

## Frozen aggregate result
Terminal scientific classification:

`PASS_SCOPED_WEYL3_P_INSERTION_CERTIFICATE`

Worst values across the 8 frozen lanes:
- input algebraic-Riemann residual: `1.1102230246251565e-16` (threshold `1e-11`)
- input Weyl-trace residual: `1.1102230246251565e-16` (threshold `1e-10`)
- projected P algebraic/Bianchi residual: `1.1102230246251565e-16` (threshold `2e-11`)
- held-out directional-derivative residual: `1.2426726755610543e-14` (threshold `2e-10`)
- cubic Euler/homogeneity residual: `1.1070610622745507e-14` (threshold `2e-10`)
- P Lorentz-frame covariance residual: `2.576554420675959e-15` (threshold `2e-9`)
- scalar I3 covariance residual: `1.1778614790479231e-14` (threshold `1e-10`)
- conformally-flat null |I3|: `3.8316754883881717e-47` (threshold `1e-11`)
- conformally-flat null ||P||: `2.048186428515155e-31` (threshold `2e-10`)
- nonzero calibration: min `|I3| = 0.007284806836403011`, min `||P|| = 0.2845256108551596`.

## Scientific interpretation
On this frozen finite generic panel, an explicit coefficient-free Weyl^3 curvature insertion `P = dI3/dR` reconstructed by component complex-step differentiation and algebraic-Riemann projection agrees with an independent analytic Weyl directional derivative, obeys the cubic Euler identity, transforms covariantly under the tested Lorentz frames, and vanishes on the conformally-flat null as required.

This closes the Weyl^3-specific **algebraic P-insertion prerequisite** for the next connection-response layer.

## Scope / claim locks
This is not the complete four-dimensional covariant Weyl^3 Euler-Lagrange tensor. The connection/covariant-derivative response of the actual Weyl^3 P tensor and final EOM assembly remain open. `c6` remains unfixed; `beta=1` is not authorized; no experimental confirmation, positivity/unitarity theorem, or KMQGB `NEW_REQUIRED` claim follows. Theory established remains `0%`.

## Next authorized gate
A separately prospectively preregistered **Weyl^3-specific connection-response / covariant double-divergence certificate** using actual P(R,g) jets, followed only on PASS by final full-EOM assembly/covariance/identity checks.
