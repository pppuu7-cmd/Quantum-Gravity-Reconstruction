# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 completion: **45%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6` remains **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Historical Iter051A
The original frozen Iter051A remains terminal `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION` with 5/12 PASS. D1/D2 diagnostics do not retroactively alter that classification.

## Terminal Iter051A-R1 — independent replacement certificate
Durable record: `results/ITER051A_R1_HIGH_PRECISION_REPLACEMENT_CERTIFICATE_PASS.md`.

Authoritative provenance:
- preregistration `b9d4162138face206901a6caafcc851ff4c40cf8`
- implementation `7e44f9da0eaf0753d82bff0ab6b4c8a9d1c2e5f0`
- aggregate `32998973363080cdb63e76ac333af28e1e19c149`
- head `d502912a86564c5e3f7ce4df889199cbaf91d591`
- run `34729269493`
- aggregate job `103648969383`
- artifact `10308907565`
- digest `sha256:24b077748f70585ffa4bf24c4e88f814de06db13e66dd4e899da062707217cab`
- classification `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE`
- frozen lane PASS `12/12`, nonzero calibration `12/12`.

Worst frozen metrics: algebraic residual `6.05e-122`; Weyl-trace residual `7.26e-122`; complex-step precision change `2.02e-80`; Richardson precision change `2.16e-76`; CS-vs-Richardson directional discrepancy `5.11e-24`; density covariance `3.66e-120`; directional covariance `5.31e-120`.

Interpretation: R1 supplies a new independent algebraic metric/measure/projector prerequisite. It does not erase the original G51A failure and does not establish the full 4D covariant Weyl^3 EOM.

## Active Iter051B0 — covariant double-divergence operator prerequisite
Prospectively frozen before implementation:
- preregistration `f983a3111c087289f6dc16703e99bb28f04668da`
- implementation `1357dbe0cf9c453efd1e02eeba44eed0b434760f`
- aggregate `a696ee8b899d6ba6129065394fc55690607f48ac`
- workflow/head `5cb496a90eae3b60f4ab75beed43c50531d16562`

G51B0 independently checks the generic rank-4 covariant double-divergence operator using polynomial Lorentzian metric/P jets, direct nested finite differences versus an explicit analytic connection-derivative expansion, plus constant-frame covariance controls. It is an implementation prerequisite only; a PASS does not yet insert the Weyl^3-specific P tensor.

## Frontier lock
Full 4D covariant Weyl^3 Euler-Lagrange promotion remains blocked. Required remaining path is:
1. terminal G51B0 operator certificate;
2. separately preregistered Weyl^3-specific P insertion / connection-response certificate;
3. final full-EOM assembly and covariance/identity checks.

No third repetitive symmetry reduction is authorized.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- finite/symmetry-reduced panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
