# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter052 / genuinely 4D covariant directional variation production`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANT FUNCTIONAL-VARIATION CLOSURE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **100%**.
- Iter052 completion: **25%** — preregistration, implementation, frozen aggregate, workflow and production launch complete; scientific matrix is still running.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false** pending terminal Iter052 classification.

## Historical terminal failures retained
- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, frozen historical `A+I+2D`, 12/18 PASS. Never rewritten.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS. Never rewritten.

## Conditioning and replacement chain
- D2N run `34742201899`: `PASS_DIAGNOSTIC_D2N_NEAR_NULL_ERROR_COLLAPSES_UNDER_INDEPENDENT_FIVE_POINT_STENCIL`, 8/8. The historical B3 angular absolute error collapsed from `7.838355602488458e-09` to `1.743008620663677e-11` under the independent five-point stencil.
- D2Z run `34742259726`: `DIAGNOSTIC_EXACT_NEAR_ZERO_CONDITIONING_CONFIRMED`. The B3 witness radius `1.2` lies only `6.496177377135481e-06` from a simple exact zero of reduced `E_S`; radial relative conditioning `kappa = 184721.51595166072`.
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

Representative raw B3 and D1 logs were inspected. Green CI alone was not used as scientific authority. D3 remains a finite computational certificate, not a global theorem.

## Active Iter052 authoritative production
Gate: `ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION`.

Authority frozen before production:
- preregistration `c49084e54428042cf59e5ac083ee49f0614a3de0`;
- implementation `b9da6cdfc424d712b80db935f16f89c00f8f5b9f`;
- frozen aggregate `79dff35e80c5095688d898b78bb78d7b80768657`;
- workflow `ff68b12968fdce2b6c220880009c256406309a65`;
- production head `f455d413bfe50128598b6fa11d70ab79bea52183`;
- run `34748588704`.

Frozen pointwise variational identity:

`d/dε [sqrt(-g) W3](g+εh)|0 = H5^{ab} h_ab + partial_mu Theta^mu`,

with the D3 bulk tensor density `H5 = A + I - 2 sqrt(-g) D5` and an independently evaluated covariant boundary-current divergence. No coefficient fitting, sign search or post-result threshold adjustment is permitted.

Frozen matrix is `A6+B3+C3 = 12` lanes with `fail-fast:false`: six fresh generic all-four-coordinate polynomial metric/perturbation pairs, three curved conformally-flat all-four-coordinate null controls, and three determinant-one coordinate-covariance pairs. At the latest synchronization all **12/12 scientific jobs are in progress** inside the frozen scientific step; no terminal scientific classification exists yet.

Only a terminal aggregate plus raw-lane inspection can classify Iter052. Green CI alone is insufficient. A PASS would be a finite genuinely four-dimensional variational certificate, not a global theorem or complete quantum-gravity theory.

## Next authorization
Do not start a dependent successor while Iter052 is nonterminal. If Iter052 PASSes, prospectively preregister either a stronger compact-support integrated-action variation certificate or a quantum amplitude/measure closure gate. If it FAILs with valid controls, preserve the FAIL and independently diagnose the bulk/boundary decomposition without weakening the frozen contract.

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
