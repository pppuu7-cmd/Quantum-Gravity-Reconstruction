# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **75%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Closed prerequisites
Historical G51A remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`; independent Iter051A-R1 is `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` (12/12), run `34729269493`, artifact `10308907565`, digest `sha256:24b077748f70585ffa4bf24c4e88f814de06db13e66dd4e899da062707217cab`.

Historical G51B0 remains `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`; independent G51B0-R1 is `PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE` (8/8), run `34734247977`, aggregate job `103662730311`, artifact `10310119784`, digest `sha256:a211e21b2190d0d4c7acd2f58bb75da43ab59d36af03762d42dd9f5c1afa78b7`.

Iter051B1 is terminal `PASS_SCOPED_WEYL3_P_INSERTION_CERTIFICATE` (8/8), run `34736761744`, aggregate job `103669479104`, artifact `10311710726`, digest `sha256:6ea83543ff58b2ac42bd02e166fed3534f37f09459e6cd55616ac1c4090fd3f0`. Durable result: `results/ITER051B1_WEYL3_P_INSERTION_PASS.md`.

## Iter051B2 — actual Weyl^3 P connection response
Prospective preregistration: `cffde199b9cd885f4d07238b8c46fdee3f966143`.
Initial implementation: `467425bb30fcf410940bb5627c5adeb7f2e9d963`; aggregate implementation: `8a33fa56922e519185ae264acaa5621783547f6a`; initial head `a9884403a7969d53f284f3195bea37f4ad5bbc62`.

Initial run `34736978191`, aggregate job `103670192517`, summary artifact `10311148731`, digest `sha256:c12216eac614c0105420f83e5fceb73d937cd9f429d5e2d0eb095020e33c1131` is permanently recorded as frozen `SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE` with valid/pass `1/4`. Durable audit: `results/ITER051B2_INITIAL_FROZEN_FAIL_NUMERICAL_SUBSPACE_DRIFT.md`.

Post-terminal causal audit localized the only failing frozen predicate to round-off/subtractive-cancellation drift of second finite-difference P derivative jets outside the exact algebraic-Riemann subspace: worst residual `1.609823385706477e-09` vs `2e-10`. All connection-response target metrics themselves were inside frozen thresholds: direct-vs-reference `2.5076338423438444e-07 < 2e-5`; direct final-step change `2.0962669356580043e-07 < 1e-5`; extracted-reference convergence `2.4933117531487735e-07 < 2e-5`; D covariance `5.351292093284897e-16 < 2e-7`; P0 covariance `3.4830092046971933e-15 < 2e-9`.

Because the algebraic-Riemann projector is linear, derivatives of an exactly subspace-valued P field remain in that subspace. A separate retry applies only that same fixed projector to finite-difference extracted `partial P` and `partial partial P`, without changing seeds, stencils, thresholds, target or interpretation.

Numerical-only repair commit: `b2d1ade45c3507e87541aaf86a304b3cbb54dbc5`.
Authoritative retry head: `0d0796cc3751f31012afc04684b5836cbf580755`.
Authoritative retry run: `34737103399`.
All four scientific lanes have completed green; terminal classification is **not yet assigned** because aggregate job `103670518127` remains queued. Green lanes alone are not a scientific PASS.

## Frontier lock
Full 4D covariant Weyl^3 Euler-Lagrange promotion remains blocked. Required path:
1. **closed:** generic double-divergence replacement certificate;
2. **closed:** actual Weyl^3 algebraic P-insertion certificate;
3. **active:** actual Weyl^3 P connection-response / covariant double-divergence retry — await frozen aggregate;
4. only after terminal PASS: final metric-consistent full-EOM assembly/covariance/identity checks.

No third repetitive symmetry reduction is authorized.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite/symmetry-reduced panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
