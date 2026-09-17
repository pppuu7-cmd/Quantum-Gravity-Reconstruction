# Iter057AZ — terminal technical FAIL

Gate: `ITER057AZ_BYTE_SAFE_REPAIR_CLEANLINESS_REDESIGN`  
Original preregistration: `31def60c38017c8fd9595e1a2772bc75cad42aba`  
Execution-only repair freeze: `3ee7468cb7f67ca668f92a2e56de13d83c9c120a`  
Repaired production head: `d0671db9c953a487e10c115c67b602811f5a0333`  
Actions run: `35246655152` (`completed/success`)  
Terminal artifact: `10507876994`  
Artifact digest: `sha256:f77de8442d7cf969236db3ec7d42d4042e53a919fa17932828ebe770aa9a0114`  
Aggregate payload SHA256: `68857021127fe2acc867a84d11ef155a73868c9f107113dfa45f5233b88c62f6`

Classification: **`FAIL_TECHNICAL_ITER057AZ_INDEPENDENT_IMPLEMENTATION_OR_CONTROL_FAILURE`**.

## Why this is a FAIL

The initial run `35243086938` was non-authoritative for PASS because both nominal lanes invoked the same implementation file, violating frozen control 9 (`two independently implemented lanes`). This defect was frozen prospectively before repaired production and was not repaired by weakening any criterion.

The repaired run used two distinct implementations:

- primary: `scripts/qgr_iter057az_bytesafe_cleanliness.py`, SHA256 `90933bdf6245026911d22fddf68a4e5dfb7b4cc37a4081024a8947a8a6382f8f`;
- independent: `scripts/qgr_iter057az_bytesafe_cleanliness_independent.py`, SHA256 `662250929cd1646964d4edcb8d36bb19ef24159f4abf29b40fc84e4cc16410f8`.

Both lane-local control sets passed completely, including strict byte acquisition/UTF-8 behavior, deterministic `NON_UTF8_PROVENANCE -> UNRESOLVED_PROVENANCE` for the frozen `0x8a` fixture, exact valid UTF-8 round trip, tracked status clean before/after, unchanged tracked-tree digest within each implementation, and `no_descendant_science_consumed=true`.

However, the prospectively frozen repaired-attempt criterion also required exact normalized agreement across the two independent implementations. That criterion failed:

- primary normalized SHA256: `6b4f9ab0a7fda1349aa1745064cb8c4968fa83d9263fabff0330e0b23750cd4f`;
- independent normalized SHA256: `0e198bef708afd02254bd43b77dffecdbd68e354f74a3e932fc492f8aa307b88`.

The only normalized-field disagreements were `before_digest` and `after_digest`. Within each lane, before==after, but the two implementations serialized the ordered tracked-file content map differently before hashing. Primary uses `path_bytes + NUL + sha256(content).digest()` records; the independent implementation used an 8-byte path-length prefix plus path bytes plus content digest. The original Iter057AZ preregistration froze the *meaning* of the tracked-file map digest but did not canonically freeze its cross-implementation serialization.

Because exact cross-lane normalized agreement was prospectively required by the repair freeze, this under-specification cannot be repaired post hoc inside Iter057AZ. The terminal technical FAIL is therefore preserved.

## Scope

This result is technical only. It does not reclassify Iter057AU, Iter057AW, or Iter057AX. No descendant science was loaded, replayed, classified, or consumed. It establishes neither QGR physics nor any theorem.

A future gate may prospectively freeze a neutral canonical serialization for the tracked-file content map and independently reproduce the byte-safe certificate under that serialization. Such a gate must not choose a serialization by fitting to either Iter057AZ lane output.

Claim locks are unchanged: theory established remains 0%; `beta=1` remains unauthorized; `c6` remains symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
