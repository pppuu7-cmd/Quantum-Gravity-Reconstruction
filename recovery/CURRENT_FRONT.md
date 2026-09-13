# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter053 / integrated compact-support Weyl3 action variation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANT FUNCTIONAL-VARIATION CLOSURE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **100%**.
- Iter052 completion: **100%**.
- Iter053 operational completion: **45%** — original production is a preserved numerical/infrastructure failure; fresh frozen retry remains active; QD/QD2 have isolated and resolved the direct-action quadrature diagnosis; weighted H5 bulk pilot is active.
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
Classification: **`ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`**. Six of eight artifacts existed (A4+B2); C0/C1 hit hosted-runner wall-clock/resource cancellation. Representative A0 had direct epsilon step change `1.1769644781427364e-12` but bulk GL3->GL4 relative change `0.8939841560959314` and fine identity residual `1.096109899568205`. This is not a scientific FAIL.
Authority record commit: `da56d56ad4ad45849b34cb4766265007b81059ea`.

### Fresh frozen retry
Wall-clock-only C repair commit `4e95a8dbba3967d18f86206681bbfda46b54699e`; fresh retry head `cf3466b3f0394952c384f7cfcc5bc445e7bbd4b5`; run **`34769958632`**. A4+B2+C2 remain active under the original frozen GL3/GL4 scientific contract. No evidence is pooled from the first production.

### Iter053-QD — terminal numerical diagnosis PASS
Gate `ITER053-QD-COMPACT-SUPPORT-QUADRATURE-CONDITIONING`; run **`34770383463`**; aggregate job `103758873038`; artifact `10321557741`; digest `sha256:001adec3865c9d0083e842fccbc99676b914eeed6bb5e862c07008d0f1570c6b`; durable result commit `acaa7debe3f44aeec0c15d5356a48581e55b0a2c`.
Classification: **`PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED`**, 8/8. Outer-box GL3 had exactly 1 nonzero compact-support tensor node and GL4 exactly 16. Support-domain GL5 improved the exact pure-bump quadrature error by at least `1.2101080028298477e14`, confirming severe support aliasing. This diagnostic cannot reclassify Iter053.

### Iter053-QD2 — terminal direct-action convergence PASS
Gate `ITER053-QD2-SUPPORT-DIRECT-QUADRATURE-CONVERGENCE`; prereg `5b85e850f4ad38d8b3dcc07958c6a3f664a4f5f7`; production head `ddf266c2b7e33bac6a8942fb099e60a76ac78aac`; run **`34770521310`**; aggregate job `103759533568`; artifact `10322290890`; digest `sha256:bc30c712c33fca891656cede20e5de73f8c0404da99e25257a961d82a02b160a`; durable result commit `d88f0837de21e80237da0fe1d5344268f9b1d317`.
Classification: **`PASS_DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_CONVERGED_BY_GL8`**, 8/8. Worst generic GL6->GL7 relative change `1.8944968469868708e-4`; worst GL7->GL8 change `8.031564672079293e-8`; worst null |GL8| `9.672771482817587e-18`. Direct-action quadrature is therefore numerically resolved on the exact support cube, but H5 bulk is not yet certified.

### Iter053-QD3 — active weighted H5 bulk pilot
Gate `ITER053-QD3-WEIGHTED-BULK-GAUSS-JACOBI-PILOT`; prereg `b12b8f1fbf8605a17d7b35191812323b1c61dde8`; implementation `471781570e1216c455e490681493e9e41ce078cd`; workflow `3c8e5640176ebe96abc826de7b7986728d61bfc3`; head `ec14bd4c5ec7ebe8523bb7c06e789d20fdcef89f`; run **`34770675902`**.
A0-only diagnostic pilot uses the exact factorization `h=B p` and tensor Gauss-Jacobi weight `(1-u^2)^4` to evaluate the expensive H5 bulk on 16/81 weighted nodes (GJ2/GJ3), against independently converged direct support GL7/GL8. It is diagnostic only and cannot establish Iter053 PASS.

## Next authorization
1. Consume fresh retry `34769958632` when terminal; preserve its original frozen classifier.
2. Consume QD3 `34770675902`. If weighted GJ3 is prospectively `promising`, preregister a **new** scientific replacement gate before any full A4+B2+C2 weighted-H5 implementation.
3. Any replacement must preserve the action, H5=`A+I-2sqrt(-g)D5`, seeds/negative-control logic or prospectively state fresh seeds, and coordinate covariance; no post-hoc threshold weakening.
4. Only after a terminal replacement PASS may Iter053 functional-variation closure be credited and the program move to quantum amplitude/measure closure.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
