# Iter053R weighted-H5 compact-support Weyl3 action variation — terminal result

Date: 2026-09-14

## Authority

Gate: `ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`

- preregistration: `952c6321bbb54530a6881ae357c149256249187f`
- implementation: `d8481ae49a093626740e71c6b0c233ca74641819`
- aggregate classifier: `f80c822765452ba4eb9f034ddf58c9f2fa0e25a3`
- workflow: `b2c979e4fbafc942b53d0a8eb8d99db0091a6d03`
- production head: `6946680a5261eeb56a4496ae36a99098853d33d8`
- run: `34782291893`
- aggregate job: `103804601776`
- summary artifact: `10326722690`
- summary artifact digest: `sha256:4ad7ad0190ea50a8928bbf9ef47b22f80616e7810513ba778ea3f1058c0023a9`

Raw artifacts:

- A-0: `10326283860`, `sha256:9d30aa6d8384e5a09f3072455019d8c3eb13c40a4b2f249ee95d8c5c288211a5`
- A-1: `10326905558`, `sha256:b3cc689b5cd4b524a4f0d797076b79d0d43dc2a158150c6efd022ab7ea87d90b`
- A-2: `10326910412`, `sha256:af45cb027ae5fe41f6e0fe967a5d3ba078a294d733eb827ad3a36521921be438`
- A-3: `10326652350`, `sha256:f46518ac36b498aa219e7b6c0667ec13268fdb1305ed46e8184d9fe97ee8c6db`
- B-0: `10326064928`, `sha256:fe0a9ecd96e177061bc35be312d3b98f7319bcba34572db294ee53d4ec83a10a`
- B-1: `10326094177`, `sha256:ffe8f3ff517ec54e443bb4f185b998be94cd06eb9130bca5fcf272104fec9f7c`
- C-0: `10325644670`, `sha256:531bbe29117cd131c6b47082e520a41a11c0724d2263c2b0589589e1c2dcb5b8`
- C-1: `10326293753`, `sha256:10cf2b10676fc775e49823659a4015dbd73c51edd518ea633a4d73d874bf85f2`

All eight A4+B2+C2 lanes were present and control-valid.

## Frozen terminal classification

`SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`

This result is permanent historical authority for Iter053R. It must not be rerun, threshold-retuned or renamed as PASS.

## Aggregate evidence

- valid lanes: `8/8`
- passes: `6/8`
- A lanes: `4/4` PASS
- B lanes: `2/2` PASS
- C lanes: `0/2` PASS
- worst A GL7->GL8 change: `8.031910208417016e-08`
- worst A direct step change: `1.4726269850162446e-10`
- worst A identity residual: `2.1202940936435192e-06`
- worst A GJ2->GJ3 weighted-bulk change: `0.0003718883088132907`
- worst B abs GJ3 bulk: `6.365172576210241e-31`
- worst B abs direct GL8: `9.672771479621411e-18`
- worst C direct covariance residual: `3.2076700199377417e-12`
- worst C weighted-H5 bulk covariance residual: `0.6925581291599372`
- wrong-sign control weaker than correct on every A lane: `true`
- minimum A wrong-sign residual: `1.919437326217528`

## Failure localization already supported by production

Both C lanes show the same qualitative pattern. The direct support-domain action variation is coordinate-covariant to approximately machine/numerical precision, while the weighted H5 bulk is not.

C0:
- base GJ2/GJ3 bulk: `2.08296484191396e-05 / 2.083049311864391e-05`
- transformed GJ2/GJ3 bulk: `4.533138389425316e-06 / 6.406449825022739e-06`
- transformed GJ2->GJ3 relative change: `0.29241022512664006`
- bulk covariance residual: `0.6924484798063288`
- direct covariance residual: `3.2076700199377417e-12`

C1:
- base GJ2/GJ3 bulk: `4.56540656402576e-05 / 4.56532713144173e-05`
- transformed GJ2/GJ3 bulk: `9.935654871054144e-06 / 1.4035727142873432e-05`
- transformed GJ2->GJ3 relative change: `0.2921168408364991`
- bulk covariance residual: `0.6925581291599372`
- direct covariance residual: `7.837043562402833e-14`

These observations motivate, but do not predetermine, a new prospective diagnostic of the tensor-density transformation of the numerical H5 assembly.

## Interpretation ceiling

Iter053R does not establish compact-support Weyl3 functional-variation closure and therefore does not authorize transition to quantum amplitude/measure closure. It also does not by itself prove that the underlying covariant functional derivative is physically inconsistent: the failure may lie in the numerical H5 realization, its coordinate-derivative implementation, or the weighted transformed evaluation. A separate prospective gate is required to distinguish those possibilities.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.