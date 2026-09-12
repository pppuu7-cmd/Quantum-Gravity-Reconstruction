# Iter045 — QGR-L1 relative TT residue/signature audit

Date: 2026-09-12
Gate: `ITER045-QGR-L1-RELATIVE-TT-RESIDUE-SIGNATURE`
Status: **TERMINAL / PASS_SCOPED**

## Frozen authority
Scientific object preregistered before implementation in `status/ITERATION_045.md`, preregistration commit `d08b131bc94007460b9ea517460f4d57e432fc16`.

Implementation:
- lane code commit `a483681222a93eac73d9ce92365b19bbf90c9969`
- aggregate commit `6d368ac30bdeff1bfa1671cb3f15c57fe53e02a9`
- workflow commit `a4f03fb58105042a775f7940a33d628e98782901`
- explicit trigger commit `cad39c37bfdc56e8b66d0d45e907eb2a33d18d09`

Authoritative production:
- run: `34716924227`
- head: `cad39c37bfdc56e8b66d0d45e907eb2a33d18d09`
- aggregate job: `103616970603`
- summary artifact: `10305091648`
- summary digest: `sha256:3a80f6865140410aadc521d6b5e7eb8f612c30ff4b2c062656632513faff56d4`
- scientific lanes: **18/18 PASS**, controls valid

Accidental workflow-definition-push run `34716911042` remains `+0 / NON_AUTHORITATIVE_DUPLICATE` under `status/ITERATION_045_RUN_AUTHORITY.md` and is not combined with the authoritative evidence.

## Terminal aggregate
Classification:
`PASS_SCOPED_QGR_L1_TWO_POLARIZATION_RELATIVE_RESIDUE_DEGENERACY`

Aggregate metrics:
- `max_cross_coefficient_relative_spread = 5.107025913275723e-15`
- `max_cross_polarization_mixing = 5.775329183325975e-16`
- `max_on_shell_projected_kernel_relative_norm = 1.2823839481978124e-15`
- `max_plus_coefficient_relative_spread = 3.7747582837255346e-15`
- `max_plus_cross_relative_difference = 1.4432899320127063e-15`
- `min_relative_sign_product = 0.24999999999999853`

## Scientific interpretation
On the frozen held-out linearized panel, the two physical TT polarizations have degenerate relative kinetic/pole coefficients, the same relative sign, and no resolved polarization mixing at the preregistered numerical precision.

This closes a relative two-polarization signature check that is distinct from the G44 dispersion/curvature bridge.

## Claim guard
The result determines only **relative** two-polarization structure. It does **not** determine the overall action sign, absolute energy positivity, quantum unitarity, nonlinear stability, `beta`, or `c6`, and it is not experimental confirmation.

`theory_established_pct` remains **0%**.