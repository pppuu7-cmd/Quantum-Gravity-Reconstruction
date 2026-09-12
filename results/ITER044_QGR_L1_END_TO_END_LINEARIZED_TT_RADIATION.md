# Iter044 — QGR-L1 end-to-end linearized TT radiation

Date: 2026-09-12
Gate: `ITER044-QGR-L1-END-TO-END-LINEARIZED-TT-RADIATION`
Status: **TERMINAL / PASS_SCOPED**

## Frozen authority
Preregistered before implementation/production in `status/ITERATION_044.md`. No production threshold was relaxed after launch.

Authoritative production:
- run: `34716363645`
- head: `e27602b367acffbc9473df95607278042fce5e02`
- aggregate job: `103616604387`
- summary artifact: `10305230612`
- summary digest: `sha256:48e15c3872ae6963582b4cada787b5c54e74e6654f1de6565d5c3b373062fadb`
- scientific lanes: **48/48 PASS**, controls valid

Frozen matrix:
- A: 24 QGR-L1 dynamics -> TT-curvature lanes
- B: 12 off-shell dispersion falsification lanes
- C: 8 gauge end-to-end robustness lanes
- D: 4 flat-background `c6 Weyl^3` linearization/decoupling lanes

## Terminal aggregate
Classification:
`PASS_SCOPED_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION_CONTRACT`

Aggregate metrics:
- `A_max_curvature_bridge_error = 5.340208237110733e-16`
- `A_max_gauge_qgr_residual = 3.829588338046111e-17`
- `A_max_tt_qgr_residual = 2.507048651523522e-16`
- `B_minimum_offshell_residual = 0.017486179466437605`
- `C_max_pure_gauge_qgr_residual = 4.3170001318188724e-17`
- `C_max_shifted_curvature_error = 3.769148233304873e-14`
- `D_max_centered_second_variation_e1 = 0.0`
- `D_max_oddness_e1 = 0.0`

All stream full-pass flags were true: A 24/24, B 12/12, C 8/8, D 4/4.

## Scientific interpretation
Within the frozen linearized flat-background domain, the internally reconstructed QGR-L1 quadratic dynamical kernel generates the expected two-mode massless TT radiative sector, has the preregistered off-shell rank/residual separation, preserves pure-gauge invariance, and bridges to the independently validated G43 radiative curvature without inserting that curvature as the dynamical input.

This is an important closure of the **linearized end-to-end radiative contract**. It is not a theorem for nonlinear or generic curved backgrounds.

## Claim guard
This result does **not** establish:
- a generic nonlinear radiation theorem;
- curved-background mode stability;
- a quantum radiation amplitude or S-matrix;
- quantum unitarity or absolute energy positivity;
- an absolute value of `beta` or `c6`;
- experimental confirmation;
- correctness/completeness of QGR as quantum gravity.

`theory_established_pct` therefore remains **0%**.