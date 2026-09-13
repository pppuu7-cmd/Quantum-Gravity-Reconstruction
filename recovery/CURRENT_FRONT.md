# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter052 / genuinely 4D covariant directional variation full retry`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANT FUNCTIONAL-VARIATION CLOSURE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Iter051 roadmap completion: **100%**.
- Iter052 completion: **40%** — initial full panel completed but is permanently control-invalid; a fresh full retry is queued after a control-only determinant fix.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established: **false** pending terminal authoritative Iter052 retry.

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
All 16/16 expected lanes were found, valid, and PASS. Worst B component relative residual `5.0113399264437624e-09`; worst B vector residual `4.36189564337193e-09`; worst D covariance residual `3.6984734831049934e-09`; minimum historical `+2D` residual `1.8708048537449804`. D3 remains a finite computational certificate, not a global theorem.

## Iter052 initial production — permanently control-invalid
Gate: `ITER052-WEYL3-4D-COVARIANT-DIRECTIONAL-VARIATION`.

Frozen authority before the initial production:
- preregistration `c49084e54428042cf59e5ac083ee49f0614a3de0`;
- scientific implementation `b9da6cdfc424d712b80db935f16f89c00f8f5b9f`;
- frozen aggregate `79dff35e80c5095688d898b78bb78d7b80768657`;
- workflow `ff68b12968fdce2b6c220880009c256406309a65`;
- initial production head `f455d413bfe50128598b6fa11d70ab79bea52183`;
- initial run `34748588704`;
- aggregate job `103701280550`;
- summary artifact `10315495921`;
- digest `sha256:3212dd4183fe73aef626ed43a77e3856c3e55b052799d99c9bd72431444a3e08`.

Frozen aggregate classification: **`ITER052_IMPLEMENTATION_OR_CONTROL_INVALID`**.

All 12 artifacts existed; 11 lanes were valid PASS. The sole invalid lane was C2 because the determinant-one transform control had `det L = 1.000000003317951`, violating frozen `|det L-1| <= 2e-12`. This is not a scientific identity failure. C2 itself had base identity residual `4.335297618863669e-10`, transformed identity residual `1.5033400152202607e-10`, direct covariance residual `3.3307732623251213e-09`, and RHS covariance residual `3.047577502781268e-09`, all far inside their scientific thresholds.

The initial run remains non-authoritative for terminal scientific classification and must never be combined with retry evidence. Authority record: `888c3d398dee4785f094037a6ad56929e18da671`.

## Active Iter052 full retry
A control-only correction in commit `da0957ee8f818195435e3804c2611b1411a01a98` preserves every frozen off-diagonal covariance-transform entry and solves the determinant's affine dependence on `L[3,3]`, giving exact machine-level determinant one for C2. No scientific identity, seed, witness, finite-difference step, coefficient, sign, or frozen threshold changed.

Fresh retry trigger/head: `d82370f18c76caebd5aa4ee567cb450a882d7bad`.
Fresh full authoritative retry run: **`34748813339`**.
At the latest synchronization the retry was queued and will rerun the entire frozen `A6+B3+C3` matrix. No evidence from the invalid initial run may be pooled into its terminal classification.

Frozen pointwise variational identity remains

`d/dε [sqrt(-g) W3](g+εh)|0 = H5^{ab} h_ab + partial_mu Theta^mu`,

with `H5 = A + I - 2 sqrt(-g) D5` and independently evaluated boundary-current divergence.

## Next authorization
Consume only the fresh full Iter052 retry. If it PASSes, write a durable result and then prospectively preregister a genuinely stronger integrated compact-support action-variation certificate or a quantum amplitude/measure closure gate. If the retry FAILs with valid controls, preserve the result and independently diagnose it without weakening the contract.

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
