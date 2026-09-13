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

## Terminal Iter051A / replacement
Historical G51A remains `SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION` (5/12). Independent Iter051A-R1 remains `PASS_REPLACEMENT_G51A_HIGH_PRECISION_METRIC_DENSITY_CERTIFICATE` (12/12), run `34729269493`, artifact `10308907565`, digest `sha256:24b077748f70585ffa4bf24c4e88f814de06db13e66dd4e899da062707217cab`.

## Terminal Iter051B0 — generic double-divergence operator gate
Durable record: `results/ITER051B0_COVARIANT_DOUBLE_DIVERGENCE_OPERATOR_FAIL.md`.

Authoritative retry provenance:
- preregistration `f983a3111c087289f6dc16703e99bb28f04668da`
- technical-only tensor-extraction repair `63c0c6416e2c22dd19b0166ceadbeebc880ed74e`
- authoritative retry head `9be326cae17e9af94a6d14517251ac3193642a57`
- run `34731863909`
- aggregate job `103656032270`
- summary artifact `10309387321`
- digest `sha256:3c6b77b4544c7063126d0928f7e433bf426cafb89888e353f0896d6663ba0f7f`
- classification `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`
- valid 8/8; PASS 0/8.

Worst metrics: direct-vs-expanded discrepancy `2.12485e-9`, P symmetry `2.78e-17`, inverse residual `4.44e-16`, but constant-frame covariance residual `0.748566` versus frozen `3e-7`.

The historical gate stays terminal FAIL. Post-terminal audit found a concrete candidate control defect in `transform_jets`: second/fourth contravariant P indices are transformed with transposed matrix placement (`jm`,`ln`) rather than (`mj`,`nl`). This cannot be repaired post hoc inside G51B0.

## Active replacement path
A new separately preregistered `Iter051B0-R1` replacement certificate is required. It must preserve the original 8 seeds, metric/P jets, finite-difference steps, discrepancy/refinement thresholds and covariance threshold, while correcting only the tensor transformation and adding an independent transformed-P tensor-law control. Only an R1 PASS can authorize a Weyl^3-specific P insertion/connection-response gate.

## Frontier lock
Full 4D covariant Weyl^3 Euler-Lagrange promotion remains blocked. Required path:
1. terminal separately preregistered G51B0-R1 replacement certificate;
2. Weyl^3-specific P insertion / connection-response certificate;
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
