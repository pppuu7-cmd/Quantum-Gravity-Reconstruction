# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter053 / integrated compact-support Weyl3 action variation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANT FUNCTIONAL-VARIATION CLOSURE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **100%**.
- Iter052 completion: **100%**.
- Iter053 operational completion: **35%** — first production classified numerical/infrastructure failure; fresh retry and independent quadrature-conditioning diagnostic are active.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established as a global theorem: **false**.

## Historical failures retained
- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, historical frozen `A+I+2D`, 12/18 PASS.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS.
Neither is rewritten by later replacement gates.

## Iter051 D3 — terminal scoped PASS
Run `34746649884`, aggregate job `103696159498`, artifact `10314332790`, digest `sha256:2fc0e26074e37eaa16d34cf7538f5abe1e5ec45279f0b77d714969deaafe1fb8`.
Classification: `PASS_SCOPED_G51C_D3_FIVEPOINT_FULL_EOM_REPLACEMENT_CERTIFICATE`, 16/16 valid PASS.

## Iter052 — terminal genuinely-4D scoped PASS
Gate: `ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION`.
Fresh retry head `d82370f18c76caebd5aa4ee567cb450a882d7bad`; run `34748813339`; aggregate job `103702164522`; artifact `10315226969`; digest `sha256:b4b8c4b75046541f25b6a5f3f469e2d59e94c2b6571a6f1645b6e94f53f82009`; durable result commit `a4ef2219c60d55dc0913e1a7c696ed949028c7bc`.
Classification: **`PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`**, 12/12 valid PASS. Worst A identity relative residual `2.0319192562122008e-09`; worst B absolute identity mismatch `1.789685316967841e-20`; worst C direct covariance residual `7.863429053040412e-11`; worst C RHS covariance residual `2.439292835420146e-09`.
This remains a finite genuinely-4D computational certificate, not a global theorem.

## Active Iter053
Gate: `ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION`.
Prospective frozen authority: preregistration `bb0b755f25f14b89dd44b6f16da309d0d0796d05`; implementation `f52c7b067c77acbcd3d59b15749f92abca672433`; aggregate `6862f94bef33f092c7a8d820fa3d71769b3d4a2e`; workflow `6ec44a1f40df0220e5a9ec30988fca10ea35b733`.

### Initial production: numerical/infrastructure failure
Head `7c88a797e12968cba8f0804292e348bf82784014`; run `34750610751`; aggregate job `103750238843`; artifact `10320808113`; digest `sha256:e6cccea46c99d1f93cf440f0d39a78bfe96dfc7f21eebacaa68690797fd0f3bc`.
Classification: **`ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`**. Six of eight artifacts existed (A4+B2); C0/C1 hit hosted-runner wall-clock/resource cancellation. A controls were valid but frozen quadrature was unresolved: representative A0 direct epsilon derivative step change `1.1769644781427364e-12` while bulk GL3->GL4 relative change was `0.8939841560959314` and the fine identity residual was `1.096109899568205`. This is not a scientific FAIL.
Authority record: `status/ITER053_RUN_AUTHORITY.md`, commit `da56d56ad4ad45849b34cb4766265007b81059ea`.

### Fresh wall-clock retry
Implementation-only C repair commit `4e95a8dbba3967d18f86206681bbfda46b54699e` executes the two already-frozen covariance sides concurrently without changing science, seeds, points, orders, thresholds, epsilon stencil or H5 step.
Fresh retry head `cf3466b3f0394952c384f7cfcc5bc445e7bbd4b5`; run **`34769958632`**. A4+B2+C2 jobs are currently in progress. Do not pool the first production evidence into this retry.

### Parallel Iter053-QD quadrature-conditioning diagnostic
Gate `ITER053-QD-COMPACT-SUPPORT-QUADRATURE-CONDITIONING`; prereg `8625318f69e3104b4dc67ada0f716394fb775de5`; implementation `49fa54a281ad4741e45fccf5de6078fc85882a36`; aggregate `a6e62f43e22c777f2ea67ef7aa7fbe921999da6e`; workflow `76e5b85f76249a3111edd48221d056829c7e08df`; production head `32c1da71923a4e023183f78d9bb8205cb99ae19f`; run **`34770383463`**.
This diagnostic cannot reclassify Iter053. It tests the preregistered numerical hypothesis that outer-box GL3 has only `1^4=1` nonzero compact-support node and GL4 only `2^4=16`, causing support aliasing; it compares that parameterization with support-domain quadrature using the exact pure-bump integral and cheap direct-action density only, without H5 fitting or threshold changes.

## Next authorization
1. Consume all fresh retry `34769958632` raw artifacts and frozen aggregate when terminal.
2. Consume Iter053-QD `34770383463` independently.
3. If QD confirms quadrature aliasing, any support-domain/sparse/composite replacement must be a separately prospectively preregistered scientific replacement gate; the original Iter053 numerical failure remains unchanged.
4. If a future valid scientific replacement PASSes, write a durable result before moving to a stronger quantum amplitude/measure or global functional-analysis front.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
