# Iter054B preregistration — Weyl3 principal Hessian and well-posedness obligation

Date frozen: 2026-09-14

Gate: `ITER054B-WEYL3-PRINCIPAL-HESSIAN-AND-WELLPOSEDNESS-OBLIGATION`

## Purpose

Determine, without physical over-interpretation, whether the cubic Weyl invariant has the expected background-dependent second variation/Hessian structure on a frozen finite algebraic Weyl-operator panel, and explicitly separate that result from the still-missing gauge-fixed covariant metric principal symbol and PDE well-posedness analysis.

This is **not** a full covariant Weyl3 EOM calculation and is not a physical ghost/spectrum gate.

## Frozen algebraic realization

Use exact rational symmetric trace-free `6 x 6` matrices as a finite Weyl-operator proxy on bivector space. Define

`F(W) = Tr(W^3)`.

For symmetric trace-free directions `H,K`, the frozen target identity is

`D^2 F_W[H,K] = 3 Tr(W(HK+KH))`.

The gate audits only this algebraic Hessian identity and its background dependence.

## Streams

### A0 — exact symbolic Hessian identity

For symbolic commuting amplitude parameters `s,t`, verify exactly that the coefficient of `s*t` in `Tr((W+sH+tK)^3)` equals `3 Tr(W(HK+KH))` on a frozen exact-rational noncommuting matrix triple. Negative control: omit one ordering term and require nonzero mismatch.

PASS iff exact residual is zero and negative-control residual is nonzero.

### A1 — frozen panel symmetry/scaling

Use 12 deterministic exact-rational symmetric trace-free triples `(W,H,K)`. For every panel member require:

- exact equality to the Hessian target;
- `D2(W;H,K)=D2(W;K,H)`;
- linear background scaling `D2(lambda W;H,K)=lambda D2(W;H,K)` for frozen `lambda=7/5`.

PASS iff 12/12 satisfy all exact identities and at least 10/12 have nonzero Hessian value.

### B0 — null versus Weyl-active activation

For 12 frozen direction pairs require exact `D2(0;H,K)=0`. For the corresponding 12 frozen nonzero trace-free `W`, require at least 10/12 nonzero Hessian values.

PASS iff the null panel is 12/12 exact zero and active count >=10.

### B1 — authority boundary / fail-closed obligation

This stream is a deterministic logical classifier, not a physics computation. Given the currently established inputs:

- algebraic Hessian available;
- full gauge-fixed covariant metric principal symbol unavailable;
- hyperbolicity estimate unavailable;
- energy estimate unavailable;
- constraint propagation proof unavailable;

it must return:

`WELLPOSEDNESS_NOT_AUTHORIZED_FROM_ALGEBRAIC_HESSIAN_ALONE`.

Negative control: if all missing PDE obligations are synthetically toggled true, classifier must no longer return the fail-closed state.

PASS iff both conditions hold.

## Aggregate rule

Terminal PASS only if A0/A1/B0/B1 are present, parseable, controls-valid and PASS.

Exact PASS classification:

`PASS_SCOPED_ITER054B_WEYL3_PRINCIPAL_HESSIAN_ACTIVATION_WELLPOSEDNESS_NOT_AUTHORIZED`

Otherwise classify `SCIENTIFIC_FAIL_OR_INVALID_ITER054B`.

## Interpretation lock

A PASS establishes only that the frozen finite algebraic cubic-Weyl proxy has the expected background-linear Hessian activation and that present evidence is insufficient to authorize well-posed exact higher-derivative dynamics. It does **not** establish the gauge-fixed covariant metric principal symbol, characteristic cone, strong/weak hyperbolicity, a physical extra-mode count, ghost sign, stability, unitarity, UV completion, full GR recovery or new physics.

`c6` remains symbolic/unfixed. `beta=1` remains unauthorized. Theory established remains `0%`.

No thresholds or witnesses may be weakened after outputs are observed.
