# QGR Current Research Front

Updated: 2026-09-17

## Programme infrastructure — terminal 100%

Repository infrastructure: **100%**. Candidate-program / research-programme infrastructure: **100%** with semantics **research-program / roadmap infrastructure readiness only; not probability of correctness, not theory completion, and not fraction of quantum gravity solved**. Theory established remains **0%**.

The programme-readiness regression caused by hard-coded `ITER057AQ/AR` recovery expectations during normal science progression has been repaired by commits `59f969c9f0c5c1b1cc91fd67da392921bdfb1a59`, `485df361c674a9b6fbfe6308f1319b68c2e6e576`, and `7083b251d2d02c47ddfe94bcef770b9bf1de69ef`. Programme-100 recertification run `35246742331` completed `success`; readiness validation is now invariant to science iteration labels while remaining fail-closed on state/front inconsistency.

## Last terminal science — Iter057AT

`ITER057AT` remains terminal `PASS_SCOPED_ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE_INDEPENDENTLY_REPRODUCED`.

- preregistration: `6039cb2ed1380b549bced3d33634362ef57345d4`;
- production head: `c4e7ccc05ea1b8f4967379fc370812dfa99cce03`;
- Actions run/artifact: `35198813733 / 10486973737`;
- corrected ordered 840-vector SHA256: `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- `c6` remains symbolic/unfixed.

No later technical gate promotes or reclassifies this scientific result.

## Preserved dependency-repair lineage

- `ITER057AU`: terminal `BLOCKED_ITER057AU_UNRESOLVED_PROVENANCE`, durable result `c299683e28289788c53797e5ede1cafaf09f5431`. No descendant science replayed.
- `ITER057AV`: terminal `FAIL_TECHNICAL_ITER057AV_REPRODUCIBLE_FROZEN_AU_EXECUTION_DEFECT_IDENTIFIED`; exact defect localized to strict UTF-8 decode failure on byte `0x8a` in the unchanged AU implementation.
- `ITER057AW`: terminal `FAIL_TECHNICAL_ITER057AW_BYTE_SAFE_REPAIR_CONTROL_FAILURE`; byte-safe/sentinel controls pass but frozen historical-tree-cleanliness control fails.
- `ITER057AX`: terminal `FAIL_TECHNICAL_ITER057AX_CLEANLINESS_ATTRIBUTION_NOT_ESTABLISHED`.
- `ITER057AY`: terminal `PASS_SCOPED_ITER057AY_EMPTY_DIRECTORY_GIT_STATUS_SEMANTICS_REPRODUCED`, durable result `defd025becf22b9087a4f66f13d2a38dc20880fc`; establishes only Git empty-untracked-directory semantics. Its frozen contract required two independent execution lanes, not two independent implementations, so its use of one script in separate lanes is not a formal contract violation.

Historical AU/AW/AX remain unchanged.

## Iter057AZ — terminal technical FAIL after repaired independent production

Original preregistration: `31def60c38017c8fd9595e1a2772bc75cad42aba`. The first auto-research production run `35243086938` was not authoritative for PASS because both nominal `primary` and `independent` lanes invoked the same implementation script despite frozen control 9 requiring **two independently implemented lanes**.

An execution-only repair was prospectively frozen at `3ee7468cb7f67ca668f92a2e56de13d83c9c120a`, then two distinct implementations were run at production head `d0671db9c953a487e10c115c67b602811f5a0333`.

Repaired Actions run: `35246655152`. Terminal artifact: `10507876994`, digest `sha256:f77de8442d7cf969236db3ec7d42d4042e53a919fa17932828ebe770aa9a0114`. Durable result: `87c9b6d029120aaeb38d0c5ff985df9125ae3470`.

Classification: **`FAIL_TECHNICAL_ITER057AZ_INDEPENDENT_IMPLEMENTATION_OR_CONTROL_FAILURE`**.

Both independent implementations passed all lane-local controls and had different implementation hashes, but exact normalized agreement failed only in `before_digest`/`after_digest`: each implementation preserved its own tracked-tree digest before==after, yet the two implementations serialized the ordered tracked-file content map differently before hashing. Because the repaired-attempt criterion required exact normalized agreement, this under-specification is preserved as terminal technical FAIL rather than repaired post hoc.

No descendant science was consumed or reclassified.

## Iter057BA — active neutral canonical byte-safe certificate

Preregistration: `f63f2df87d2d1abaea93daa29a311d78e331eefa`, frozen **before** either BA implementation.

The new canonical tracked-tree map serialization is neutral and intentionally differs from both AZ serializations:

`b"QGR_TRACKED_TREE_MAP_V1\n" + concat(path_hex_ascii + b"\t" + sha256(file_bytes).hexdigest().lower().ascii + b"\n")`

with entries sorted lexicographically by raw path bytes.

Independent implementations:

- primary commit `10e576fb81e47da48679a672378e0335f61baeb5`;
- independent commit `2053022c4fc17e4572ea1ed52b2b3b62abef0dc8`.

Production head/workflow: `47d5d68c6ba75c248cce1651f32d17c30e9b729b`, `.github/workflows/qgr-iter057ba-canonical-bytesafe.yml`.
Actions run: `35247035208`.
Current authoritative execution status at this update: **queued**, with both `ubuntu-latest` jobs showing `runner_id=0`; no duplicate authoritative run is launched while this run remains active. Public GitHub status reports Actions operational, so queueing alone is not classified as a repository scientific/technical failure.

A local non-authoritative synthetic diagnostic confirmed the primary and independent canonical-serialization algorithms yield the same digest on the same tracked-file map. This is diagnostic only; BA terminal classification requires Actions lane+aggregate artifacts.

## Iter057BB — prospectively frozen conditional successor, execution locked

Preregistration: `eb864872be1db63d0588296c606b759b7b1495c8`, frozen before any BA outcome.

`ITER057BB_CONDITIONAL_BYTE_SAFE_DESCENDANT_DEPENDENCY_ADJUDICATION_RETRY` may be implemented/executed **only if** BA terminates exactly as:

`PASS_SCOPED_ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_INDEPENDENTLY_REPRODUCED`.

BB keeps the original AU census frozen at commit `616859890df95057556d265612c53da839a5848a`, preserves the original dependency classes and target-blindness, uses byte-safe provenance semantics only as an execution-layer repair, requires two separately authored implementations, and still fails closed as `BLOCKED_ITER057BB_UNRESOLVED_PROVENANCE` if any classification-load-bearing provenance remains unresolved. No descendant science may be recomputed inside BB.

If BA does not PASS, BB remains execution locked.

## Claim locks

Theory established: **0%**. Experimental confirmation false. `beta=1` unauthorized. `c6` symbolic/unfixed. No strong-hyperbolicity, physical-ghost, quantum-unitarity, interacting-measure, regulator-removal, UV-completion, new-physics or KMQGB `NEW_REQUIRED` claim is authorized. Finite/local classical certificates remain finite/local classical certificates.
