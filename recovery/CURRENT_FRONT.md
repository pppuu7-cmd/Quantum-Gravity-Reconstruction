# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051 / post-G51C-D2 near-null conditioning diagnostic`
Project phase: `MODEL_CONSTRUCTION / WEYL3 NEAR-NULL NUMERICAL CONDITIONING`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **85%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false**.

## Historical G51C — terminal FAIL
Run `34741060700`, aggregate job `103680844833`, artifact `10311749167`, digest `sha256:1b4a324a05666a2ff0c67bdb922e87efc600d70d481ab380bb4532baf43c8c99`.
Classification: **`SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`**. Frozen `A+I+2D` assembly: 12/18 PASS, exact reduced-EL Stream B 0/6. This is never rewritten.

## G51C-D1 — terminal diagnostic localization
Run `34741524418`, aggregate job `103682017568`, artifact `10313265535`, digest `sha256:38dcc34cf1502bef249ad315461e35a0ac3ad4ad02df3f58e1a3826d52829412`.
Classification: **`DIAGNOSTIC_LOCALIZED_G51C_COEFFICIENT_PATTERN`**.
Diagnostic fit `(A,I,J)=(0.9999999910,0.9999999924,-1.9999999868)` with global residual `1.64e-7`; historical +2J residual `2.04`. Diagnostic only.

## G51C-D2 — terminal FAIL with one near-null spherical witness
Prospective preregistration `72d42c480c23723b1d185d73816e8c3db5cf809a`; implementation `fb5d87918ab91c2a318465f9f638bf029a512084`; aggregate `054f169a68dd0eef545f9b110b8ed2557f29571c`; workflow `c2d1063d1ffdf6f3a9d3d6d05ddcb97b5602580d`; production head `a18d7d054d3612f9ccfbe235b509c51c7890f3ff`.

Authoritative run `34741924103`; aggregate job `103683219373`; summary artifact `10312601307`; digest `sha256:dcdef4dff571b1ba3350a2e6acec7478e1aec1b6847d5fc7765c17d82b931c78`.

Terminal classification: **`SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`**.
All controls valid; 20/20 artifacts present; **19/20 PASS**:
- A held-out Bianchi-I: 8/8 PASS, worst corrected residual `3.2810328446797246e-06`;
- B independent spherical exact reduced EL: 3/4 PASS;
- C generic 4D covariance/symmetry: 4/4 PASS, worst covariance `6.129475301102737e-08`;
- D conformally-flat null controls: 4/4 PASS.

The sole fail is spherical B3. Exact angular reduced target `E_S=-3.994998616073071e-07`; corrected prediction `-3.916615060048186e-07`; absolute discrepancy about `7.84e-09`, but componentwise relative residual `0.019620421321179977`, above frozen `1e-3`. Other B3 components have residuals `1.72e-6` and `4.62e-8`; final-step change `3.27e-6` is well inside threshold. Historical +2D residual is `1.88036`.

The D2 threshold is not relaxed and D2 remains FAIL. Durable result: `results/ITER051C_D2_SIGN_HELDOUT_VALIDATION_FAIL.md`.

## Active authorization
The next authorized gate is **not** G51C-R1. First run a separately preregistered numerical-conditioning diagnostic on the near-null spherical sector. It should compare the existing nested 3-point central derivative with an independently implemented higher-order 5-point covariant stencil and test a frozen panel spanning ordinary and near-zero angular reduced coefficients around the B3 region.

The diagnostic must answer whether the B3 discrepancy scales down under higher-order differentiation and whether the `-2D` candidate remains stable through a near-zero sign/cancellation region. It may not retroactively change D2's classification or thresholds.

Only a successful independent conditioning diagnosis may authorize a fresh replacement held-out validation gate. Full G51C-R1 remains blocked until then.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- full covariant six-derivative EOM not established;
- finite panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
