# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter053 / integrated compact-support Weyl3 action variation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANT FUNCTIONAL-VARIATION CLOSURE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **100%**.
- Iter052 completion: **100%**.
- Iter053 operational completion: **55%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established as a global theorem: **false**.

## Preserved historical failures
- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, 12/18 PASS.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS.
Neither is rewritten by later replacement gates.

## Iter052 — terminal genuinely-4D scoped PASS
Run `34748813339`; aggregate job `103702164522`; artifact `10315226969`; digest `sha256:b4b8c4b75046541f25b6a5f3f469e2d59e94c2b6571a6f1645b6e94f53f82009`; result commit `a4ef2219c60d55dc0913e1a7c696ed949028c7bc`.
Classification: `PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`, 12/12 valid PASS. Finite computational certificate only.

## Iter053 original gate — preserved numerical/infrastructure failure
Preregistration `bb0b755f25f14b89dd44b6f16da309d0d0796d05`; initial run `34750610751`; aggregate job `103750238843`; artifact `10320808113`; digest `sha256:e6cccea46c99d1f93cf440f0d39a78bfe96dfc7f21eebacaa68690797fd0f3bc`.
Classification: **`ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`** because C0/C1 hit hosted-runner wall-clock cancellation. This classification is permanent historical authority and is not rewritten by later diagnostics/replacements.

### Fresh original-contract retry
Wall-clock-only repair `4e95a8dbba3967d18f86206681bbfda46b54699e`; retry head `cf3466b3f0394952c384f7cfcc5bc445e7bbd4b5`; run **`34769958632`**.
Current status: **in progress**, A4+B2+C2 under original frozen GL3/GL4 contract. No evidence pooling from the first production.

## Diagnostic chain
- QD run `34770383463`: `PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED`; artifact `10321557741`; digest `sha256:001adec3865c9d0083e842fccbc99676b914eeed6bb5e862c07008d0f1570c6b`.
- QD2 run `34770521310`: `PASS_DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_CONVERGED_BY_GL8`; artifact `10322290890`; digest `sha256:bc30c712c33fca891656cede20e5de73f8c0404da99e25257a961d82a02b160a`.
- QD3M run `34771761543`: `PASS_DIAGNOSTIC_ITER053_QD3_GAUSS_JACOBI_MOMENTS_EXACT`; job `103762519052`; artifact `10321744441`; digest `sha256:fbfd56dfbad2293c070a49e6bc02d4d0119f13e5db84f6a10025f4dbff1d749c`.

## QD3 — terminal weighted H5 pilot PASS
Gate `ITER053-QD3-WEIGHTED-BULK-GAUSS-JACOBI-PILOT`; prereg `b12b8f1fbf8605a17d7b35191812323b1c61dde8`; production head `ec14bd4c5ec7ebe8523bb7c06e789d20fdcef89f`.
Run **`34770675902`**; job **`103759575844`**; artifact **`10322517083`**; digest **`sha256:5d7d7d616660a3843a097c4cd23305ee473df16c14c8b323015284926dd89bcf`**; durable result commit **`4522328868d6e018d22619d5d31cfe811487c92e`**.
Classification: **`PASS_DIAGNOSTIC_ITER053_WEIGHTED_GJ3_BULK_PILOT_PROMISING`**.

Frozen evidence:
- GJ2 bulk `9.065790207702158e-06`; GJ3 bulk `9.066610617407998e-06`.
- GJ2→GJ3 relative change `9.048692399614629e-05`.
- Direct GL7→GL8 relative change `5.086275142547632e-08`.
- Direct GL8 `9.066613706546225e-06`.
- GJ3 H5 bulk vs direct GL8 residual **`3.407157652190216e-07`**.
- Wrong-sign residual **`1.944220429443305`**.
- Signature/inverse controls valid.

QD3 is diagnostic only; it does not reclassify original Iter053 or establish full A4+B2+C2 closure.

## Iter053R — prospectively preregistered scientific replacement
Gate: **`ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`**.
Preregistration commit: **`952c6321bbb54530a6881ae357c149256249187f`**.
Status: **PREREGISTERED / NOT IMPLEMENTED**.

Frozen before any Iter053R implementation/production:
- full A4+B2+C2 panel, `fail-fast:false`;
- weighted H5 tensor Gauss-Jacobi `alpha=beta=4`, coarse GJ2 and fine GJ3;
- independent direct support-domain GL7/GL8 action variation;
- H5 remains `A+I-2 sqrt(-g)D5`, derivative step `5e-4`;
- generic thresholds retain the original scientific targets: direct epsilon and GL7→GL8 changes `<=5e-4`, weighted bulk GJ2→GJ3 `<=2e-3`, fine identity residual `<=3e-3`;
- B null thresholds and C determinant-one covariance thresholds retained;
- historical wrong-sign `A+I+2 sqrt(-g)D5` must be worse on every A lane and `>=1e-2` on at least one A lane;
- no retuning, lane dropping, seed selection, evidence pooling or threshold weakening after implementation/production evidence.

Allowed terminal classes are only PASS scoped, scientific FAIL, control/implementation invalid, or numerical/infrastructure fail as frozen in the preregistration. Even PASS remains a finite genuinely-4D compact-support computational certificate; `c6` stays symbolic and theory established remains 0%.

## Current authorization
1. Consume fresh retry `34769958632` when terminal under its original classifier.
2. Iter053R implementation is authorized by terminal QD3 and preregistration `952c6321bbb54530a6881ae357c149256249187f`, but must not change frozen science.
3. Production classification requires every raw A4+B2+C2 artifact plus frozen aggregate.
4. Only a terminal Iter053R PASS may credit compact-support functional-variation closure and permit transition toward quantum amplitude/measure closure.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
