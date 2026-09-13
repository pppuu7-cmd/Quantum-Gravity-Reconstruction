# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **85%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Closed prerequisites
Historical G51A remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`; independent Iter051A-R1 is `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` (12/12), run `34729269493`, artifact `10308907565`, digest `sha256:24b077748f70585ffa4bf24c4e88f814de06db13e66dd4e899da062707217cab`.

Historical G51B0 remains `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`; independent G51B0-R1 is `PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE` (8/8), run `34734247977`, aggregate job `103662730311`, artifact `10310119784`, digest `sha256:a211e21b2190d0d4c7acd2f58bb75da43ab59d36af03762d42dd9f5c1afa78b7`.

Iter051B1 is terminal `PASS_SCOPED_WEYL3_P_INSERTION_CERTIFICATE` (8/8), run `34736761744`, aggregate job `103669479104`, artifact `10311710726`, digest `sha256:6ea83543ff58b2ac42bd02e166fed3534f37f09459e6cd55616ac1c4090fd3f0`.

## Iter051B2 — actual Weyl^3 P connection response
Prospective preregistration: `cffde199b9cd885f4d07238b8c46fdee3f966143`.
Initial run `34736978191`, aggregate job `103670192517`, summary artifact `10311148731`, digest `sha256:c12216eac614c0105420f83e5fceb73d937cd9f429d5e2d0eb095020e33c1131` remains permanently recorded as frozen `SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE` (1/4 valid/pass).

Post-terminal causal audit localized that failure to finite-difference second-P-jet drift outside the exact linear algebraic-Riemann subspace. Numerical-only repair commit: `b2d1ade45c3507e87541aaf86a304b3cbb54dbc5`.

Authoritative retry head: `0d0796cc3751f31012afc04684b5836cbf580755`.
Authoritative retry run: `34737103399`.
Aggregate job: `103670518127`.
Summary artifact: `10312171778`.
Digest: `sha256:f076eb8a61bd2e0cc6d648533737aca349e28c14c3cb39f1f465e857442bf568`.
Terminal classification: **`PASS_SCOPED_WEYL3_P_CONNECTION_RESPONSE_CERTIFICATE` (4/4 valid, 4/4 PASS)**.

Worst frozen values: `P_jet_algebraic=3.469446951953614e-17`; `P_jet_reference_convergence=2.4973661811983306e-07`; `direct_final_step_change=2.096266935658004e-07`; `direct_vs_reference_finest=2.5069984569780767e-07`; `D_covariance=5.753870859922338e-16`; `P0_direct_covariance=3.4830092046971933e-15`; `zero_curvature_P_norm=2.7216552697590953e-61`. All are inside their prospectively frozen thresholds.

Durable result: `results/ITER051B2_WEYL3_P_CONNECTION_RESPONSE_PASS.md`.

## Frontier lock
Full 4D covariant Weyl^3 Euler-Lagrange promotion remains blocked pending one final gate. Required path:
1. **closed:** generic double-divergence replacement certificate;
2. **closed:** actual Weyl^3 algebraic P-insertion certificate;
3. **closed:** actual Weyl^3 P connection-response / covariant double-divergence certificate;
4. **next/active authorization:** prospectively preregister and then implement final metric-consistent full-EOM assembly/covariance/identity checks with `c6` symbolic.

No third repetitive symmetry reduction is authorized. A successful final assembly gate would still be a finite numerical/covariant certificate on its frozen panel, not a proof of quantum unitarity, experimental confirmation, or a complete quantum-gravity theory.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite/symmetry-reduced panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
