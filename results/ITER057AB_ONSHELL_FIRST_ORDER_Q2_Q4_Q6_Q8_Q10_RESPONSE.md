# Iter057AB terminal result — unrestricted on-shell O(c6) Q2/Q4/Q6/Q8/Q10 response

Date: 2026-09-16
Gate: `ITER057AB-ONSHELL-FIRST-ORDER-Q2-Q4_Q6_Q8_Q10-RESPONSE`
Frozen preregistration: `f78b028c345faa80f1e482f6a00fb9133cb9b955`
Implementation lineage: `cfdc2a96177182466eb0213720ebc182af126cb2`
Control-only compatibility-count fix: `342579bd071f471d55f235d19823842d38304a7d`
Authoritative Ubuntu production head: `8ef69240515459daad37e7e1e30aea20d38426c5`
Actions run: `35049895455`
Artifact: `10429480826`
Artifact digest: `sha256:f950587cb198e888938d57af8d4fc20d5a1ef0af86e2294dd8a8ed56c3a779f7`

## Terminal classification

`PASS_SCOPED_ITER057AB_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_Q8_Q10_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_EIGHTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN`

The terminal Ubuntu artifact matches the frozen Iter057AB gate and satisfies obligations A-K exactly.

Exact terminal evidence:

- frozen preregistration replay: `f78b028c345faa80f1e482f6a00fb9133cb9b955`;
- parent response authority: Iter057Y `cb2758238daba9ecf9c86e01e171f6c6d31c72b9`;
- parent background authority: Iter057Z `bb4fa6ccbf21e2a063467a1b0839223744866995`;
- parent corrected source authority: Iter057AA `2c84ddcb5dd22cfe06cd3a1a273b4a0e141b605e`;
- unrestricted system shape `2530 x 2860`, matrix nnz `10120`;
- exact rank `2050`, augmented rank `2050`;
- left-nullity `480`, nullity `810`;
- canonical Bianchi rank `480`;
- all `480/480` actual compatibility contractions exactly zero;
- fresh fixed-lower-response residual before Q10: degree-nine de Donder nonzero count `139`, degree-eight field/source nonzero count `260`;
- exact unrestricted Q10 particular solution: `320` nonzero normalized coefficients;
- final full covariant de Donder nonzero count through degree nine: `0`;
- final reduced `DG_g[qhat]-Shat` nonzero count through degree eight: `0`;
- final independent unreduced `DG_g[qhat]-Shat` nonzero count through degree eight: `0`;
- all authority subcontrols in the terminal artifact are true;
- exact-zero decisions use no numerical tolerance;
- `c6` status is `SYMBOLIC_UNFIXED_FACTORED_OUT`.

The later supplemental Windows rerun `35049902680` is terminal `failure`. It is not used as scientific evidence for or against the frozen gate in this terminal classification; the frozen PASS above rests on the completed authoritative Ubuntu artifact and its exact A-K controls. No claim of successful cross-platform reproduction is made here.

## Interpretation ceiling

This PASS establishes only one additional finite local first-order `O(c6)` Taylor-response layer on one canonical finite-order Einstein seed. It does not establish an all-orders or convergent solution, open-neighborhood/global/asymptotic existence, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experiment, new physics, or QGR correctness.

Historical FAIL/BLOCKED results remain preserved. Finite certificate != theorem; classical != quantum; diagnostic != closure; theory established remains `0%`.
