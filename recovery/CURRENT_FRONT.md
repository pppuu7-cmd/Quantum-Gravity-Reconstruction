# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **75%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Historical failures / independent replacements
Historical G51A remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION` (5/12); independent Iter051A-R1 remains `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` (12/12), run `34729269493`, artifact `10308907565`, digest `sha256:24b077748f70585ffa4bf24c4e88f814de06db13e66dd4e899da062707217cab`.

Historical G51B0 remains `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR` (0/8), run `34731863909`, artifact `10309387321`, digest `sha256:3c6b77b4544c7063126d0928f7e433bf426cafb89888e353f0896d6663ba0f7f`. Independent G51B0-R1 remains `PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE` (8/8), run `34734247977`, aggregate job `103662730311`, artifact `10310119784`, digest `sha256:a211e21b2190d0d4c7acd2f58bb75da43ab59d36af03762d42dd9f5c1afa78b7`.

## Terminal Iter051B1 — actual Weyl^3 algebraic P insertion
Durable record: `results/ITER051B1_WEYL3_P_INSERTION_PASS.md`.

Prospective provenance:
- preregistration `cbaf060790e56e4fed27290651c40104cdbbf7d9`
- implementation `2e6f2b2430061f3d770ba727ede83d542ede5057`
- aggregate implementation `25c02c988e60a97476f51f2f1fdb047d8edd0169`
- authoritative head `d1f066538f18bc058564eb74a623a701295592aa`
- run `34736761744`
- aggregate job `103669479104`
- summary artifact `10311710726`
- digest `sha256:6ea83543ff58b2ac42bd02e166fed3534f37f09459e6cd55616ac1c4090fd3f0`
- valid `8/8`; PASS `8/8`
- classification `PASS_SCOPED_WEYL3_P_INSERTION_CERTIFICATE`.

Frozen worst values: P algebraic/Bianchi residual `1.1102230246251565e-16`; held-out directional derivative residual `1.2426726755610543e-14`; Euler/homogeneity residual `1.1070610622745507e-14`; P covariance residual `2.576554420675959e-15`; scalar covariance residual `1.1778614790479231e-14`; conformally-flat `|I3| = 3.8316754883881717e-47`; conformally-flat `||P|| = 2.048186428515155e-31`. All are well inside the prospectively frozen thresholds.

Interpretation is scoped: this closes the finite algebraic Weyl^3 curvature-insertion prerequisite. It is **not** the complete 4D Weyl^3 metric Euler-Lagrange tensor.

## Active path
The next authorized gate is a **prospectively preregistered Weyl^3-specific connection-response / covariant double-divergence certificate using actual P(R,g) jets**. It must include nontrivial metric connection jets, nonconstant algebraic-curvature jets, independent derivative routes, constant-frame covariance, convergence and null/nonzero controls. A generic P surrogate or another symmetry reduction cannot substitute.

Only a PASS of that connection-response layer may authorize final full-EOM assembly/covariance/identity checks.

## Frontier lock
Full 4D covariant Weyl^3 Euler-Lagrange promotion remains blocked. Required path:
1. **closed:** generic double-divergence replacement certificate;
2. **closed:** actual Weyl^3 algebraic P-insertion certificate;
3. **next:** actual Weyl^3 P connection-response / covariant double-divergence certificate;
4. final full-EOM assembly and covariance/identity checks.

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
