# Iter053T terminal result

Date: 2026-09-14

## Primary gate

Gate: `ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`

- preregistration: `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation: `d996463e53aaa3a7a736488bd393f01beb56f162`
- production head: `df76ae7e59c92a30958572d963e6c4204f9c163b`
- run: `34788261104`
- aggregate job: `103828912630`
- summary artifact: `10329638555`
- digest: `sha256:312079d2cc1a07b7af12763aedb0f980879117bfda3185be34ca096321bf7faa`
- classification: `ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED`

Frozen aggregate: valid/complete; structural factorization PASS; corrected numeric lanes PASS; GJ2→GJ3 convergence PASS; legacy GJ3 negative controls PASS; legacy-to-corrected improvement PASS. Worst corrected integrated covariance residual `2.0590650746290315e-09`; worst corrected nodewise covariance residual `3.4581493704057676e-08`; worst structural factorization residual `2.152344524141186e-16`. C0 corrected GJ3 covariance residual `1.2518957930421278e-09` versus legacy `0.6924484798485422`; C1 corrected `2.2171978395835512e-10` versus legacy `0.6925581291599372`.

## Independent nodewise companion

Gate: `ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`

- preregistration: `74d033551f0eb4060f9621cd9e9e10b00e57700a`
- implementation: `bfa059335b44eb6ac730e8b98d04a08fcb243bb0`
- production head: `75a30221c9a61d4a2484a9d0181cb3330d2104c0`
- run: `34788222635`
- aggregate job: `103828894352`
- summary artifact: `10329224173`
- digest: `sha256:1c330cf704500654659a653bce9fac397b9b7b00495172935702cac3f626b9a0`
- classification: `ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED`

Frozen aggregate: 6/6 lanes PASS and valid; minimum nontrivial node count 81; worst nodewise contraction relative residual `8.409160670944214e-08`; worst weighted-GJ3 sum covariance residual `6.140021540682663e-09`; minimum wrong-congruence residual `0.13608019032461305`.

## Scientific classification and scope

The two independently preregistered gates agree that the historical transformed weighted path double-counted compact support (`B(u)^2`) and that the source-faithful single-weight pushforward restores covariance in the frozen finite panel. Historical Iter053R remains immutable `SCIENTIFIC_FAIL`; this result does not reclassify it.

This terminal result authorizes execution of the already prospectively frozen Iter053U replacement gate. It does **not** establish the complete covariant Weyl3 metric EOM, global validity, physical ghost content, unitarity, UV completion, experimental confirmation, `c6`, or `beta=1`. Theory established remains 0%.
