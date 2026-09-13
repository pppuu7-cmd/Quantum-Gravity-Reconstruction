# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051 / D3 five-point full-EOM replacement production`
Project phase: `MODEL_CONSTRUCTION / WEYL3 FULL-EOM REPLACEMENT`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **90%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false**.

## Historical terminal failures retained
- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, frozen historical `A+I+2D`, 12/18 PASS. Never rewritten.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS. Never rewritten.

## D2R — terminal scoped replacement PASS
Prereg `2597fb51bc087a4332d5974db38e0641bfacccba`; head `a5f1021f8596f8e00a4a39f0d366eb276de3b397`; run `34744139101`; aggregate job `103689280172`; artifact `10312909946`; digest `sha256:714f66fb514d9046e82a8ede2e4350bf3586989060469dbcdcc415ba22f830c0`.

Classification: `PASS_SCOPED_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION`.
All 12 raw lane artifacts were consumed by the frozen aggregate: 12/12 expected, 12/12 valid, 12/12 PASS. Worst absolute component error `1.5270905373565569e-09`; worst final-step change `6.047761854580956e-09`; worst vector relative residual `7.3382674860456824e-09`; minimum historical `+2D` residual `1.4228139519895726`.

Durable result commit: `c12b9af1a4c930ed6ae703ca53d7e83d712b3a94`.

## Active D3 authoritative production
Gate: `ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT`.
Preregistration commit `f4dd9630408495e915fe3c8da1812c7690a58566` was created before implementation `cafa7cfbd5c72458decd2ee204f5b1f0aa02400a`; frozen aggregate commit `06a00065a8ac2b80e254f37fc336e894aabb5fcf`; workflow commit `63026f09ea6b1513b4ad9da4d12d8ff0cc9f8f8a`; authoritative production head `242309e900b0c815983cc161c912b0439fbbc395`; run `34746649884`.

Frozen science: `H5 = A + I - 2 sqrt(-g) D5`, where `D5` is the independently validated nested five-point covariant derivative. No coefficient fitting, sign search, or post-result threshold adjustment is permitted.

Frozen panel: 16 independent lanes: 4 fresh generic polynomial metrics, 6 fresh anisotropic Bianchi-I exact-target tests, 3 conformally-flat null controls, and 3 covariance tests. `fail-fast: false`.

Current production state at synchronization: 16 scientifically useful matrix jobs in progress, 0 queued; aggregate remains dependency-blocked until the matrix is terminal. No scientific D3 classification exists yet.

## Next authorization
Consume every D3 raw lane artifact and the frozen aggregate. Green CI alone is not a scientific PASS. Only a terminal D3 PASS may authorize the next genuinely covariant directional-variation/full-functional-derivative certificate. Do not start another symmetry-reduced panel as a substitute.

Even a D3 PASS remains a finite computational certificate, not a global theorem for arbitrary 4D metrics and not a complete quantum-gravity theory.

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
