# Iter057BE terminal result — Iter057Y same-iteration replay-order adjudication

Date: 2026-09-17
Gate: `ITER057BE_ITER057Y_SAME_ITERATION_REPLAY_ORDER_ADJUDICATION`
Preregistration: `5b16cb4432097fd974adf93e624f872e4620cd17`
Primary implementation: `4f8b12bc4064c5cc835ca4d6a308ab951e5632e1`
Independent implementation: `f199b96607d21b8adf1d03ddcf68ef7a24f0e8a5`
Production head: `c86d28f3008d2cb28b3447c3c121eaa3bd587564`
Workflow: `.github/workflows/qgr-iter057be-y-replay-order.yml`
Actions run: `35253679294`

Artifacts:
- primary `10511207445`, digest `sha256:965f47bd374d9a73bf0be1430a7263d29428a007df54904d408f0405ecc38b64`;
- independent `10511571822`, digest `sha256:78fd519c914e49d327b64121160620319fccbfea64540b8bad876d8d53ea4c59`;
- terminal `10512116594`, digest `sha256:0a4b9c8974c8d633ee46929d895cbe28292fca8b538e7df460d43da399256704`.

## Frozen classification

`BLOCKED_ITER057BE_ITER057Y_REPLAY_ORDER_UNRESOLVED`

Terminal payload SHA256: `db500dd3426502d7d42cb3c40229f546c7b8104fe43380f3fc0ebf72a20335f7`.

## What reproduced

Both lanes consumed the exact same five frozen evidence objects and agreed on their hashes:

- audit record SHA256 `86e1647b9febc40395b09c380e9d188b9e0b79bdd15e44ef5eb946e6c15c2680`;
- science record SHA256 `0f88c01bd1abe9bf4e37bff781c1dd68451c1eb7d761ce4af886291c8b2aa603`;
- wrapper source SHA256 `274aa62fd110f5a94cdfeb1968dc69c5322b1d774520575f61675423b7f5edef`;
- science implementation SHA256 `486e8db9855f1b387c1dfb1b9d4b21178a4463019bf32ca47b3cbd7d5f5889bb`;
- Iter057BD result SHA256 `1d673d1ef7b18398b347bd436883fdb87e31babf5521e4650ce18f41dca8cf25`.

Both lanes establish that the audit explicitly names terminal science authority `cb2758238daba9ecf9c86e01e171f6c6d31c72b9`, names corrected wrapper `8d5936b988c57d44e8a279b9d5fd4f6238a071e4`, is supplemental, and has no reverse dependency from historical science onto the later audit/wrapper.

The independent AST/call-flow lane passed every frozen control and returned `SCIENCE_BEFORE_AUDIT`. It independently established:

- wrapper imports `qgr_iter057y_onshell_q2_q4_q6_q8_response` as `y`;
- exactly one call to `y.compute()`;
- wrapper monkey-patches `y.consume_authorities` before the compute call;
- commit ancestry `98c822... -> cb2758... -> 8d5936... -> ddcb7f...`;
- wrapper commit adds the wrapper source; audit commit adds the audit record; terminal-science commit adds the science result.

## Blocking control

The primary lane failed exactly one positive control: `wrapper_metadata_only_note=false`. Every other positive primary control passed and all forbidden-action controls remained false.

The failure is attributable to the primary extractor's raw-source substring predicate: the wrapper's runtime `supplemental_reproduction_note` is expressed as adjacent Python string literals across source lines. Python concatenates those literals at compile time, but the frozen raw-source predicate searched for the concatenated semantic sentence as one contiguous source substring. Therefore this terminal gate remains BLOCKED exactly as frozen; the predicate is not weakened post hoc.

This post-terminal localization is a technical extractor diagnosis only. It does not reclassify Iter057BE and does not yet authorize Y replay.

## Authority ceiling

Historical Iter057Y remains unchanged. Iter057BD dependency membership remains unchanged. No descendant science was consumed or replayed. `c6` remains symbolic/unfixed and theory established remains 0%.
