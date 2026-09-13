# Retrospective quantitative localization of the terminal Iter053R C failure

Date: 2026-09-14
Status: retrospective analysis of already-terminal Iter053R evidence. This note does **not** change the historical Iter053R classification and is not scored as evidence for any active Iter053T gate.

Historical authority remains:

`SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`

Run: `34782291893`.

## C0 historical raw result

Artifact: `qgr-iter053r-C-0`, artifact ID `10325644670`, digest `sha256:531bbe29117cd131c6b47082e520a41a11c0724d2263c2b0589589e1c2dcb5b8`.

### Base frame

- direct GL8 finest: `2.08304927239695e-05`
- GJ3 bulk: `2.083049311864391e-05`
- identity relative residual: `1.8946954668914336e-08`
- GJ2->GJ3 relative change: `4.055110455131349e-05`
- direct GL7->GL8 change: `1.9186981121709975e-08`
- final epsilon-step change: `3.2693153187337665e-13`
- `generic_pass = true`

Thus the C0 base frame was already a clean generic PASS under the frozen Iter053R thresholds.

### Transformed frame

- direct GL8 finest: `2.0830492723902683e-05`
- transformed GJ3 bulk: `6.406449825022739e-06`
- direct covariance residual: `3.2076700199377417e-12`
- weighted bulk covariance residual: `0.6924484798063288`
- transformed identity residual: `0.6924484739781775`
- transformed GJ2->GJ3 change: `0.29241022512664006`
- `generic_pass = false`

The transformed direct integral agrees with the base frame to approximately `3.2e-12`; only the reduced weighted representation is suppressed and nonconvergent at the frozen low orders.

The transformed/base fine weighted ratio is

`6.406449825022739e-06 / 2.083049311864391e-05 = 0.3075515201936711`.

## C1 historical raw result

Artifact: `qgr-iter053r-C-1`, artifact ID `10326293753`, digest `sha256:10cf2b10676fc775e49823659a4015dbd73c51edd518ea633a4d73d874bf85f2`.

### Base frame

- direct GL8 finest: `4.5653276528492235e-05`
- GJ3 bulk: `4.56532713144173e-05`
- identity relative residual: `1.1421031149881121e-07`
- GJ2->GJ3 relative change: `1.7398797438059896e-05`
- direct GL7->GL8 change: `1.508264162589636e-08`
- final epsilon-step change: `2.3362701831859964e-13`
- `generic_pass = true`

Thus the C1 base frame was also a clean generic PASS.

### Transformed frame

- direct GL8 finest: `4.565327652848866e-05`
- transformed GJ3 bulk: `1.4035727142873432e-05`
- direct covariance residual: `7.837043562402833e-14`
- weighted bulk covariance residual: `0.6925581291599372`
- transformed identity residual: `0.6925581642729449`
- transformed GJ2->GJ3 change: `0.2921168408364991`
- `generic_pass = false`

Again, transformed direct covariance is essentially machine-level while only the weighted representation is strongly suppressed.

The transformed/base fine weighted ratio is

`1.4035727142873432e-05 / 4.56532713144173e-05 = 0.3074418708400629`.

## Cross-lane structural pattern

The two independent C seeds produce transformed/base fine weighted ratios

- C0: `0.3075515201936711`
- C1: `0.3074418708400629`

which differ by only `1.0964935360818773e-04` in absolute ratio.

At the same time:

- both base sides satisfy all generic thresholds;
- both transformed direct integrals remain covariant to `~1e-12` or better;
- both transformed weighted branches show approximately `0.6925` covariance loss;
- both transformed GJ2->GJ3 changes are approximately `0.292`.

This highly repeatable suppression across two different metric/perturbation seeds is consistent with a deterministic common multiplicative weighting mismatch rather than a seed-specific physical covariance failure.

## Relation to the wrapper-depth diagnosis

The source-level audit independently established that the transformed legacy reducer receives `B(u)p(u)` through `TransformPerturbation.base`, even though the external Gauss-Jacobi measure already supplies one `B(u)`. The base reducer receives only `p(u)`.

Therefore the legacy transformed side represents a `B^2`-weighted integral while the base side represents the intended `B`-weighted integral.

The terminal C raw data exhibit exactly the qualitative pattern predicted by that object mismatch:

1. base direct/weighted identity is healthy;
2. transformed direct identity is healthy under coordinate change;
3. only transformed reduced weighted bulk is systematically suppressed;
4. low-order convergence worsens because the second `B` remains inside the reduced integrand;
5. suppression is nearly seed-independent across C0/C1.

This is a retrospective mechanistic localization only. The active prospectively frozen Iter053T gates remain responsible for testing the corrected source-faithful path under their own independent classifiers.

## Interpretation ceiling

Nothing in this note reclassifies Iter053R, establishes a corrected replacement PASS, proves a global functional-derivative theorem, fixes `c6`, authorizes `beta=1`, opens quantum amplitude/measure closure, establishes GR/UV recovery, or changes `theory established = 0%`.
