# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **25%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter051A — frozen scientific failure
Durable record: `results/ITER051A_WEYL3_METRIC_DENSITY_VARIATION_SCIENTIFIC_FAIL.md`.

Authoritative provenance:
- head `55e4c099516cbfe9a76ab826994cc5f28cae69c0`
- run `34724233650`
- aggregate job `103635469747`
- artifact `10307431104`
- digest `sha256:17b0d975691abdee5e7cbf4fa45198f7f6b3c8e0136a017c7b3cb8c5902e8a33`
- classification `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`
- frozen lane PASS `5/12`, nonzero calibration `12/12`.

Aggregate algebraic/Weyl/covariance extrema remain excellent, and max finest-step complex-step/FD relative discrepancy is `1.6407915760785562e-09`, but the preregistered convergence predicate is binding and fails in seven lanes. The gate is not weakened post hoc.

## Terminal Iter051A-D1 — mixed numerical localization
Durable record: `results/ITER051A_D1_FD_ROUNDOFF_LOCALIZATION.md`.

Authoritative provenance:
- preregistration `5536412cc6b5a82535737bc60228fc8259320707`
- head `9a20884caa150dce0852b6c173174d33847d37f8`
- run `34726671235`
- aggregate job `103641908472`
- artifact `10307224793`
- digest `sha256:674b43ad674f9a9d272757df14280acbdc7ad3d5cd685f4a6eafcae68d029529`
- classification `DIAGNOSTIC_MIXED_NUMERICAL_BEHAVIOR`.

Exactly 7 original G51A failures are reproduced. Four (`1,11,3,7`) satisfy the frozen centered-FD roundoff-turnover diagnostic; three (`0,2,9`) do not. Therefore D1 does not explain the whole G51A failure and cannot promote it.

## Active Iter051A-D2 — complex-step comparator stability
Prospectively preregistered after D1 terminal:
- preregistration `3e4fdf397afc060b02250c26be30af21f0ba6ef4`
- implementation `730a57552e0924943246aa2c97ffb3d5ab1a5c42`
- aggregate `e474d56d14731d7ac63f2987800e491492a9458e`
- trigger/head `1dc54a4d312bb4fa63d45ef8fecbe3a1fcb6e1af`
- authoritative run `34726732537`.

Frozen scope is only the three D1-unlocalized lanes `[0,2,9]`. It audits five complex-step epsilons `[1e-16,1e-20,1e-24,1e-28,1e-30]` plus inherited algebraic and directional-covariance controls. This is a diagnostic only and cannot retroactively change G51A.

## Frontier lock
Full 4D covariant Weyl3 Euler-Lagrange promotion remains blocked. A valid separately preregistered G51A-class algebraic metric/measure/projector certificate and an independent G51B covariant double-divergence/connection-response certificate are both required.

Exact next action: consume Iter051A-D2 terminal artifact. If the complex-step comparator is stable 3/3, a new independent high-precision derivative certificate may be preregistered. If instability is present, audit the complex-step implementation before any replacement G51A-class production.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- finite/symmetry-reduced panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
