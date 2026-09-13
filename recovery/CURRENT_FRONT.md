# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter052 / genuinely 4D covariant directional variation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANT FUNCTIONAL-VARIATION CLOSURE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **100%**.
- Iter052 initial completion: **5%**.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false** pending a genuinely four-dimensional variational certificate.

## Historical terminal failures retained
- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, frozen historical `A+I+2D`, 12/18 PASS. Never rewritten.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS. Never rewritten.

## Conditioning and replacement chain
- D2N run `34742201899`: `PASS_DIAGNOSTIC_D2N_NEAR_NULL_ERROR_COLLAPSES_UNDER_INDEPENDENT_FIVE_POINT_STENCIL`, 8/8. The historical B3 angular absolute error collapsed from `7.838355602488458e-09` to `1.743008620663677e-11` under the independent five-point stencil.
- D2Z run `34742259726`: `DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_CONFIRMED`. The B3 witness radius `1.2` lies only `6.496177377135481e-06` from a simple exact zero of the reduced `E_S`; radial relative conditioning `kappa = 184721.51595166072`.
- D2R run `34744139101`: `PASS_SCOPED_G51C_D2R_FRESH_SPHERICAL_REPLACEMENT_VALIDATION`, 12/12.

## D3 — terminal scoped PASS
Gate: `ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT`.

Authority:
- preregistration `f4dd9630408495e915fe3c8da1812c7690a58566`;
- implementation `cafa7cfbd5c72458decd2ee204f5b1f0aa02400a`;
- frozen aggregate `06a00065a8ac2b80e254f37fc336e894aabb5fcf`;
- workflow `63026f09ea6b1513b4ad9da4d12d8ff0cc9f8f8a`;
- production head `242309e900b0c815983cc161c912b0439fbbc395`;
- run `34746649884`;
- aggregate job `103696159498`;
- summary artifact `10314332790`;
- digest `sha256:2fc0e26074e37eaa16d34cf7538f5abe1e5ec45279f0b77d714969deaafe1fb8`;
- durable result commit `36be4c7caf7fe6facd2b1a2e13234c4048b83234`.

Frozen classification: **`PASS_SCOPED_G51C_D3_FIVEPOINT_FULL_EOM_REPLACEMENT_CERTIFICATE`**.
All 16/16 expected lanes were found, valid, and PASS: 4 fresh generic metrics, 6 fresh anisotropic exact-target tests, 3 conformally-flat null controls, and 3 covariance controls. Worst B component relative residual `5.0113399264437624e-09`; worst B vector residual `4.36189564337193e-09`; worst D covariance residual `3.6984734831049934e-09`; minimum historical `+2D` residual `1.8708048537449804`.

Representative raw B3 and D1 logs were inspected. Green CI alone was not used as scientific authority.

D3 is a finite computational certificate. It does not erase historical failures, prove a global theorem for arbitrary 4D metrics, or establish QGR correctness.

## Active Iter052 frontier
The next authorized gate must be genuinely four-dimensional and variational, not another symmetry-reduced panel. Prospectively freeze a local/full functional-variation identity for

`L6 = sqrt(-g) W3`

under arbitrary non-symmetry-reduced metric perturbations `h_{mu nu}(x)`, comparing a direct directional derivative of `L6` with the frozen D3 tensor contraction plus the independently defined covariant boundary-current divergence. The metric and perturbation families must depend nontrivially on all four coordinates, `c6` remains symbolic, and no coefficient fitting/sign search is permitted.

A successful finite Iter052 panel may establish a scoped four-dimensional variational certificate, but it still will not by itself prove a global theorem or a complete quantum-gravity theory.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- full covariant six-derivative EOM not yet established;
- finite panels are not global theorems;
- G45 does not establish absolute energy positivity or quantum unitarity;
- G35–G37 distant roots do not authorize physical weights;
- no KMQGB `NEW_REQUIRED` authorization.
