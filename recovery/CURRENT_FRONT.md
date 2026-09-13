# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter053 / integrated compact-support Weyl3 action variation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANT FUNCTIONAL-VARIATION CLOSURE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **100%**.
- Iter052 completion: **100%**.
- Iter053 completion: **10%** — prospectively preregistered; implementation/production not yet created.
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

Prospective authority:
- preregistration `c49084e54428042cf59e5ac083ee49f0614a3de0`;
- scientific implementation `b9da6cdfc424d712b80db935f16f89c00f8f5b9f`;
- frozen aggregate `79dff35e80c5095688d898b78bb78d7b80768657`;
- workflow `ff68b12968fdce2b6c220880009c256406309a65`.

Initial run `34748588704` remains permanently `ITER052_IMPLEMENTATION_OR_CONTROL_INVALID`: C2 determinant-one control had `det L=1.000000003317951`, outside frozen control tolerance. Authority record `888c3d398dee4785f094037a6ad56929e18da671`.

Control-only fix `da0957ee8f818195435e3804c2611b1411a01a98` changed only determinant-one transform construction; scientific identity, seeds, witnesses, steps and thresholds were unchanged.

Authoritative fresh retry:
- head `d82370f18c76caebd5aa4ee567cb450a882d7bad`;
- run **`34748813339`**;
- aggregate job **`103702164522`**;
- summary artifact **`10315226969`**;
- digest **`sha256:b4b8c4b75046541f25b6a5f3f469e2d59e94c2b6571a6f1645b6e94f53f82009`**;
- durable result commit `a4ef2219c60d55dc0913e1a7c696ed949028c7bc`.

Fresh retry classification: **`PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`**.

All 12/12 fresh lanes were found, valid and PASS; no initial invalid evidence was pooled. Streams: A6+B3+C3. Worst A identity relative residual `2.0319192562122008e-09`; worst B absolute identity mismatch `1.789685316967841e-20`; worst C direct covariance residual `7.863429053040412e-11`; worst C RHS covariance residual `2.439292835420146e-09`.

Interpretation remains scoped: this is a finite genuinely-4D computational directional-variation certificate, not a global functional-analytic theorem and not a complete QG theory.

## Active Iter053 — prospectively frozen before implementation
Gate: `ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION`.
Preregistration commit: **`55f57ef10f5ebc103fef5b5bad48f3eeed75133e`**.

The next gate integrates the Weyl3 action and the independently assembled bulk response over a genuinely 4D domain using perturbations with an analytic compact-support collar, so the boundary-current term vanishes independently. Frozen panel: A4 generic compact-support lanes, B2 conformally-flat null controls, C2 determinant-one covariance controls; fixed coarse/fine quadrature orders; fixed epsilon stencil; historical `+2D` wrong-sign negative control; no coefficient fitting or post-hoc retuning.

At this synchronization Iter053 has not yet been implemented or run. This is the only authorized next primary gate; another symmetry-reduced minisuperspace panel is forbidden as a substitute.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
