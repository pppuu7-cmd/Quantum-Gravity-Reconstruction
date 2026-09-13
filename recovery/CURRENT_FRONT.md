# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **30%**.
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

The failed preregistered convergence predicate remains binding. It is not weakened post hoc.

## Terminal Iter051A-D1 — mixed numerical localization
Durable record: `results/ITER051A_D1_FD_ROUNDOFF_LOCALIZATION.md`.

- run `34726671235`
- aggregate job `103641908472`
- artifact `10307224793`
- digest `sha256:674b43ad674f9a9d272757df14280acbdc7ad3d5cd685f4a6eafcae68d029529`
- classification `DIAGNOSTIC_MIXED_NUMERICAL_BEHAVIOR`.

Four of seven original failures (`1,11,3,7`) satisfy the frozen centered-FD roundoff-turnover diagnostic; three (`0,2,9`) do not.

## Terminal Iter051A-D2 — complex-step comparator stable
Durable record: `results/ITER051A_D2_COMPLEX_STEP_STABILITY.md`.

Authoritative provenance:
- preregistration `3e4fdf397afc060b02250c26be30af21f0ba6ef4`
- implementation `730a57552e0924943246aa2c97ffb3d5ab1a5c42`
- aggregate `e474d56d14731d7ac63f2987800e491492a9458e`
- head `1dc54a4d312bb4fa63d45ef8fecbe3a1fcb6e1af`
- run `34726732537`
- aggregate job `103642066679`
- artifact `10307943436`
- digest `sha256:2a0e90b2a6f3cdfc64f44fdce879062dd43419bfed36e1f87b97cd612888ac4c`
- classification `DIAGNOSTIC_COMPLEX_STEP_STABLE_3_OF_3`.

Frozen result: `3/3` lanes pass, max relative spread across epsilons `8.771226570866013e-15`, max inherited directional-covariance relative residual `6.224741437388768e-15`. Therefore the remaining D1-unlocalized failures are not explained by instability of the complex-step comparator on the tested epsilon range.

This diagnostic does **not** retroactively promote G51A. Terminal G51A remains a scientific FAIL.

## Frontier lock
Full 4D covariant Weyl3 Euler-Lagrange promotion remains blocked. A valid separately preregistered G51A-class algebraic metric/measure/projector certificate and an independent G51B covariant double-divergence/connection-response certificate are both required.

Exact next action: prospectively preregister and run an **independent high-precision replacement G51A-class derivative certificate** on all 12 original lanes. It must use frozen witnesses and no post-hoc threshold changes. Only a new certificate can supply algebraic metric-density credit; G51B/full-EOM promotion remains blocked until then.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- finite/symmetry-reduced panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
