# Iter051B2 — Actual Weyl^3 P Connection-Response Certificate

Date frozen: 2026-09-13
Status at freeze: **NO Iter051B2 production result inspected; production implementation not yet committed.**

## Scientific question
For the actual coefficient-free Weyl^3 curvature insertion `P(R,g)=dI3/dR` certified in Iter051B1, does a nonconstant `P(R(x),g(x))` field pass an independent covariant connection-response / double-divergence certificate on generic local Lorentzian metric and algebraic-curvature jets?

This is not a generic-P surrogate and not another symmetry reduction.

## Frozen local fields
Four independent production lanes, `lane=0..3`, with production seeds `72001 + 173*lane`. The development/calibration witness used before this preregistration is disjoint from these seeds and is non-authoritative.

For each lane define, near `x=0`:
- `g_ab(x)=eta_ab + A_c,ab x^c + 1/2 H_cd,ab x^c x^d`, with symmetric metric coefficients and frozen small amplitudes;
- an independently generated algebraic-curvature field `R_abcd(x)=R0_abcd + RL_c,abcd x^c + 1/2 RQ_cd,abcd x^c x^d`, where every coefficient has the algebraic Riemann symmetries and `RQ_cd` is symmetric in coordinate-jet indices;
- actual `P(R(x),g(x))` is recomputed pointwise by the Iter051B1 complex-step curvature derivative and algebraic-Riemann projection. No fitted generic P coefficients are permitted.

The curvature field is deliberately an independent algebraic local field in this gate; it is not yet required to equal `Riemann[g]` of the same metric jet. That metric-integrability condition is reserved for final full-EOM assembly.

## Frozen independent routes
1. **Extracted-jet route:** obtain `P0`, `partial P`, and `partial partial P` from pointwise actual `P(R(x),g(x))` using symmetric finite differences at three extraction steps `hP = [1e-3, 5e-4, 2.5e-4]`. Feed each extracted P jet together with the exact metric jets into the already replacement-qualified generic covariant double-divergence operator. The finest result is the reference for this gate.
2. **Direct nested route:** independently evaluate first covariant divergence of actual pointwise P and then its second covariant divergence using nested finite differences at `hD = [2e-3, 1e-3, 5e-4]`. This route must not reuse extracted P derivatives.
3. **Constant-frame covariance:** transform the finest extracted actual-P jets with the corrected Iter051B0-R1 tensor law, recompute the covariant double divergence, and compare to the transformed reference tensor in two fixed Lorentz frames. In addition, recompute actual P0 directly from transformed `(R0,g0)` and compare against the tensor-law transform as an integrity control.
4. **Null/control:** `R=0` with the same local metric gives Weyl `C=0`; actual P must vanish at the origin. Require a nonzero generic reference double divergence so a zero implementation cannot pass.

## Frozen thresholds
A production lane is structurally valid only if:
- all sampled metric determinants are negative (Lorentzian on the sampled stencil);
- worst metric inverse identity residual `<= 1e-11`;
- algebraic-Riemann residual of actual P0 and extracted P derivative tensors `<= 2e-10`;
- `||D_reference||_F > 1e-6`;
- direct finest result norm `> 1e-6`;
- zero-curvature actual-P null norm `<= 2e-10`.

A lane PASS requires all structural controls plus:
- finest extracted-P reference convergence (difference between the two finest extracted-jet D tensors) `<= 2e-5` relative;
- direct nested finest vs finest extracted-jet reference residual `<= 2e-5` relative;
- direct nested final step-to-step change `<= 1e-5` relative;
- worst constant-frame covariance residual of the reference double divergence `<= 2e-7`;
- worst direct P0 tensor-law covariance control `<= 2e-9`.

Aggregate PASS requires **4/4 structurally valid and 4/4 PASS**. Workflow must use `fail-fast:false` and may run all four lanes in parallel.

## Frozen terminal classifications
Only:
- `PASS_SCOPED_WEYL3_P_CONNECTION_RESPONSE_CERTIFICATE`
- `SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE`
- `INFRASTRUCTURE_OR_NUMERICAL_FAIL_G51B2` when the frozen predicates were not actually evaluated.

No threshold may be weakened after production results are visible. A technical failure may receive a minimal implementation-only repair under a new authoritative retry head without changing the frozen science.

## Interpretation lock
Even 4/4 PASS establishes only a scoped local certificate that the **actual Weyl^3 P(R,g) field**, on independent algebraic curvature and metric jets, is compatible with the qualified covariant double-divergence/connection-response machinery. It does not yet establish the complete metric variation because this gate does not impose `R=Riemann[g]` on the same jet and does not assemble the explicit algebraic metric-density term with the derivative term into the final Euler-Lagrange tensor.

A PASS authorizes only the separately preregistered final metric-consistent full-EOM assembly/covariance/identity gate. `c6` remains symbolic/unfixed; `beta=1` is not authorized; theory established remains `0%`; no positivity/unitarity or experimental claim follows.
