# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **60%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter051A / replacement
Historical G51A remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION` (5/12). Independent Iter051A-R1 remains `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` (12/12), run `34729269493`, artifact `10308907565`, digest `sha256:24b077748f70585ffa4bf24c4e88f814de06db13e66dd4e899da062707217cab`.

## Historical Iter051B0
Historical G51B0 remains `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`, run `34731863909`, aggregate job `103656032270`, artifact `10309387321`, digest `sha256:3c6b77b4544c7063126d0928f7e433bf426cafb89888e353f0896d6663ba0f7f`, valid 8/8 and PASS 0/8. Its frozen covariance failure is not rewritten.

## Terminal Iter051B0-R1 — independent replacement certificate
Durable record: `results/ITER051B0_R1_COVARIANT_DOUBLE_DIVERGENCE_REPLACEMENT_PASS.md`.

Prospective provenance:
- preregistration `93776b77e59da737d6448056e52458b47322d502`
- implementation `fd1642e1e873b0b68f7eb0e334c4054c3e80ecc0`
- aggregate `6e9962d83af392047eee26aec2c6b40aee58b3cb`
- authoritative head `c9b59b5c93845fdbc989ad68a3d9c32ebc968721`
- run `34734247977`
- aggregate job `103662730311`
- summary artifact `10310119784`
- digest `sha256:a211e21b2190d0d4c7acd2f58bb75da43ab59d36af03762d42dd9f5c1afa78b7`
- valid `8/8`; PASS `8/8`
- terminal classification `PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE`.

Frozen worst metrics: direct-vs-expanded `1.2319087175184468e-09 < 4e-7`; covariance `1.1655100058513393e-11 < 3e-7`; inverse-transform `4.440892098500626e-16 < 3e-12`; metric-transform `8.881784197001252e-16 < 3e-12`; independent P-transform `5.027629253303725e-15 < 3e-12`.

Interpretation is scoped: the generic double-divergence/covariance implementation prerequisite is qualified. This is not yet a Weyl^3-specific P-insertion or complete 4D Weyl^3 Euler–Lagrange certificate.

## Active path
The next authorized gate is a **prospectively preregistered Weyl^3-specific P-insertion / connection-response certificate**. It must test an actual Weyl^3 curvature derivative/insertion, not another generic tensor or symmetry-reduced surrogate. Independent directional-derivative, Riemann-symmetry, covariance and normalization/homogeneity controls must be frozen before production. Only after that layer passes may final full-EOM assembly/covariance/identity checks be opened.

## Frontier lock
Full 4D covariant Weyl^3 Euler-Lagrange promotion remains blocked. Required path:
1. **closed:** generic double-divergence replacement certificate;
2. **next:** Weyl^3-specific P insertion / connection-response certificate;
3. final full-EOM assembly and covariance/identity checks.

No third repetitive symmetry reduction is authorized.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite/symmetry-reduced panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
