# Iter051A-D1 — finite-difference roundoff localization

Date: 2026-09-13

Preregistration: `5536412cc6b5a82535737bc60228fc8259320707`.
Implementation: `ea474bafa31ecb31bbc19d103706307427e45001`.
Aggregate: `7bcadb5cdc7869ac1ffd294d1436d2698288d889`.
Authoritative head: `9a20884caa150dce0852b6c173174d33847d37f8`.

Authoritative terminal provenance:
- run `34726671235`
- aggregate job `103641908472`
- aggregate artifact `10307224793`
- digest `sha256:674b43ad674f9a9d272757df14280acbdc7ad3d5cd685f4a6eafcae68d029529`
- expected/found lanes `12/12`
- recomputed original G51A failures `7`

Frozen classification:
`DIAGNOSTIC_MIXED_NUMERICAL_BEHAVIOR`

Original failing lane IDs: `[0,1,11,2,3,7,9]`.
Roundoff-turnover localized lane IDs: `[1,11,3,7]`.
Thus 4/7 failing lanes satisfy the preregistered roundoff-turnover diagnostic and 3/7 do not.

Aggregate extrema:
- max minimum relative FD/complex-step discrepancy over the diagnostic grid: `1.4761995649159607e-09`
- max final absolute discrepancy: `1.4091826663897855e-10`

Interpretation is strictly diagnostic. The terminal G51A result remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`; this result does not authorize changing its finite-difference convergence predicate. Because three failing lanes are not localized by the frozen roundoff criterion, a comparator-stability audit is required before designing any replacement high-precision certificate.
