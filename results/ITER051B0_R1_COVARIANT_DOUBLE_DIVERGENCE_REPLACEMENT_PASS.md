# Iter051B0-R1 — Covariant Double-Divergence Replacement Certificate

Date: 2026-09-13

## Frozen gate
`ITER051B0-R1-COVARIANT-DOUBLE-DIVERGENCE-REPLACEMENT`

This is a separately preregistered replacement certificate. It does **not** rewrite or erase the historical Iter051B0 result, which remains `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`.

Prospective provenance:
- preregistration commit: `93776b77e59da737d6448056e52458b47322d502`
- implementation commit: `fd1642e1e873b0b68f7eb0e334c4054c3e80ecc0`
- aggregate commit: `6e9962d83af392047eee26aec2c6b40aee58b3cb`
- authoritative workflow/head: `c9b59b5c93845fdbc989ad68a3d9c32ebc968721`

Frozen science preserved the historical G51B0 witnesses, 8 lanes/seeds, finite-difference/refinement logic and thresholds. The replacement changes the independently audited tensor-frame transformation only, correcting contravariant index placement and adding independent metric/inverse/P transformation controls.

## Authoritative production
- run: `34734247977`
- aggregate job: `103662730311`
- summary artifact: `10310119784`
- summary digest: `sha256:a211e21b2190d0d4c7acd2f58bb75da43ab59d36af03762d42dd9f5c1afa78b7`
- lanes valid: `8/8`
- lanes PASS: `8/8`

Raw lane artifacts were produced for lanes 0–7 and consumed together with the aggregate. Summary-level worst values were:
- direct-vs-expanded discrepancy: `1.2319087175184468e-09` vs frozen `4e-7` maximum;
- covariance relative residual: `1.1655100058513393e-11` vs frozen `3e-7` maximum;
- inverse-transform residual: `4.440892098500626e-16` vs frozen `3e-12` maximum;
- metric-transform residual: `8.881784197001252e-16` vs frozen `3e-12` maximum;
- independent P-transform residual: `5.027629253303725e-15` vs frozen `3e-12` maximum.

Representative raw-lane checks also show refinement success and covariance/P-law residuals near machine precision; no lane-level scientific anomaly was found.

## Terminal scientific classification
`PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE`

Interpretation: the corrected generic rank-4 Riemann-symmetry tensor implementation passes the frozen numerical agreement and constant-frame covariance certificate for the double-divergence operator. This closes the generic operator/covariance prerequisite that blocked the next Weyl^3-specific insertion test.

## Scope / non-claims
This result does **not** establish the Weyl^3-specific `P^{abcd}` insertion, connection-response terms, or the complete four-dimensional covariant Weyl^3 Euler–Lagrange tensor. It does not fix `c6`, does not authorize `beta=1`, does not establish absolute energy positivity or quantum unitarity, and is not experimental confirmation. Theory established remains `0%`. The historical G51B0 FAIL remains part of the audit trail.

## Next authorized gate
Prospectively preregister a Weyl^3-specific P-insertion / connection-response certificate. No third symmetry-reduced substitute is authorized.
