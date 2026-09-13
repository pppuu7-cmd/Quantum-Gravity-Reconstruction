# Iter051A-R1 preregistration — independent high-precision Weyl3 metric-density derivative certificate

Date: 2026-09-13
Status: **FROZEN BEFORE IMPLEMENTATION/PRODUCTION**

## Motivation and scope
Terminal G51A remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION` (5/12 frozen lanes). D1 localized four failures to float64 centered-FD turnover; D2 independently showed the complex-step reference is stable on the other three. No failed criterion is weakened or reclassified.

R1 is a **new replacement certificate**, not a rerun and not a retroactive modification of G51A. It tests only the algebraic metric/measure/Weyl-projector directional derivative of `sqrt(-g) Weyl^3`; it does not include connection response or the covariant double-divergence sector G51B.

## Frozen witnesses
Exactly the 12 original G51A lanes `0..11`, with unchanged seeds `4001 + 131*lane`, unchanged construction of `R`, `h`, Minkowski base metric, and unchanged two coordinate transformations. No witness selection after results.

## Independent numerical certificate
Each lane is evaluated with arbitrary precision arithmetic at **80 dps and 120 dps**. The same density is reconstructed directly with arbitrary-precision tensor contractions.

For each precision:
1. compute a complex-step directional derivative with `epsilon = 1e-40`;
2. compute a 5-point centered derivative for `t = 1e-3, 5e-4, 2.5e-4`;
3. Richardson-extrapolate the two finest 5-point estimates assuming O(t^4): `D_R = D(h/2) + (D(h/2)-D(h))/15`;
4. independently recompute density and directional response after both frozen coordinate transformations.

## Frozen controls and thresholds
A lane is scientifically valid only if all are true:
- Lorentzian signature is preserved for every real stencil point;
- algebraic Riemann residual <= `1e-30` in arbitrary precision reconstruction;
- Weyl trace residual <= `1e-28`;
- nonzero calibration: `|density| > 1e-8` and `|directional derivative| > 1e-8`;
- relative difference `complex-step` vs Richardson derivative <= `1e-12` at both 80 and 120 dps;
- relative change of complex-step derivative from 80 to 120 dps <= `1e-24`;
- relative change of Richardson derivative from 80 to 120 dps <= `1e-18`;
- density covariance residual <= `1e-20` and directional covariance residual <= `1e-18` at 120 dps.

Relative errors use floor `1e-30`.

## Frozen aggregate interpretation
- `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` iff exactly 12 lanes are present and all 12 pass every frozen criterion.
- `SCIENTIFIC_FAIL_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` iff all expected lanes are validly produced but at least one frozen scientific criterion fails.
- malformed/missing artifacts, exceptions, dependency failures, or runner problems are `INFRASTRUCTURE_OR_NUMERICAL_FAIL` and do not count as scientific failure.

## Consequence lock
Even a 12/12 R1 PASS establishes only a replacement **algebraic metric-density directional-response certificate** on the frozen generic finite panel. It does not erase the historical G51A FAIL, does not establish the complete 4D Weyl3 Euler-Lagrange tensor, and does not authorize theory correctness. A separate prospectively frozen G51B connection-response/double-divergence certificate remains mandatory before full-EOM assembly.

## Claim locks
Theory established = 0%; no experimental confirmation; `c6` unfixed; `beta=1` unauthorized; no global theorem from finite panels; no KMQGB `NEW_REQUIRED` authorization.
