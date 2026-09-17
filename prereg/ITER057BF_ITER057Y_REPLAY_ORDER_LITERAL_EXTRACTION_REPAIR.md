# Iter057BF — Iter057Y Replay-Order Literal-Extraction Repair

Status: **PROSPECTIVELY PREREGISTERED / NOT YET PRODUCED**  
Date: 2026-09-17

## Motivation

Iter057BE terminally classified `BLOCKED_ITER057BE_ITER057Y_REPLAY_ORDER_UNRESOLVED`. Its independent AST/call-flow lane passed every frozen criterion and established `SCIENCE_BEFORE_AUDIT`. Its primary exact-reference/text lane passed every positive criterion except `wrapper_metadata_only_note`.

Post-terminal inspection localized that single failure to the primary extractor's representation-level predicate: the wrapper's `supplemental_reproduction_note` runtime value is written as adjacent Python string literals across source lines. Python concatenates those literals at compile time, while the primary BE predicate searched for the semantically concatenated sentence as one contiguous raw-source substring.

This new gate does not reclassify Iter057BE. It prospectively repairs only that extraction mechanism.

## Frozen parents

- Iter057BE preregistration: `5b16cb4432097fd974adf93e624f872e4620cd17`.
- Iter057BE production head: `c86d28f3008d2cb28b3447c3c121eaa3bd587564`.
- Iter057BE Actions run: `35253679294`.
- Iter057BE primary artifact: `10511207445`, digest `sha256:965f47bd374d9a73bf0be1430a7263d29428a007df54904d408f0405ecc38b64`.
- Iter057BE independent artifact: `10511571822`, digest `sha256:78fd519c914e49d327b64121160620319fccbfea64540b8bad876d8d53ea4c59`.
- Iter057BE terminal artifact: `10512116594`, digest `sha256:0a4b9c8974c8d633ee46929d895cbe28292fca8b538e7df460d43da399256704`.
- Iter057BE terminal payload SHA256: `db500dd3426502d7d42cb3c40229f546c7b8104fe43380f3fc0ebf72a20335f7`.
- Iter057BE durable BLOCKED result: `ab1ca6e342902f06421c2debb1d9c06e1adfcff8`.

The five evidence-object hashes are frozen exactly as observed in Iter057BE:

- audit record: `86e1647b9febc40395b09c380e9d188b9e0b79bdd15e44ef5eb946e6c15c2680`;
- science record: `0f88c01bd1abe9bf4e37bff781c1dd68451c1eb7d761ce4af886291c8b2aa603`;
- wrapper source: `274aa62fd110f5a94cdfeb1968dc69c5322b1d774520575f61675423b7f5edef`;
- science implementation: `486e8db9855f1b387c1dfb1b9d4b21178a4463019bf32ca47b3cbd7d5f5889bb`;
- Iter057BD result: `1d673d1ef7b18398b347bd436883fdb87e31babf5521e4650ce18f41dca8cf25`.

## Sole authorized repair

The repaired primary extractor must preserve every Iter057BE primary evidence test unchanged except `wrapper_metadata_only_note` acquisition.

For that one field it must:

1. read the exact frozen wrapper source bytes at commit `8d5936b988c57d44e8a279b9d5fd4f6238a071e4`;
2. tokenize Python source without executing/importing the wrapper;
3. locate the assignment to `obj['supplemental_reproduction_note']`;
4. collect only Python STRING tokens belonging to that assigned parenthesized literal expression;
5. evaluate each isolated literal token with standard Python literal semantics and concatenate them in source order;
6. verify the resulting exact semantic value contains both:
   - `Corrected only Iter057V provenance metadata validation`;
   - `scientific inputs, coefficients, affine system, solve and replay are unchanged.`

No other primary criterion may be changed. The primary extractor may not inspect the independent payload or use the desired scheduling verdict as input.

## Frozen independent lane

The independent lane is the unchanged Iter057BE implementation `scripts/qgr_iter057be_y_order_independent.py`, whose BE artifact implementation SHA256 is frozen as:

`ea42d3fafece8ee8bb22ca5c832c4334625b872c5eda77c1478ef4b8dda6c62b`.

It must be rerun from source and reproduce all BE independent controls. No independent criterion may be modified.

## Frozen terminal criteria

The Iter057BE scheduling criteria are unchanged. `PASS_SCOPED_ITER057BF_ITER057Y_REPLAY_BUNDLE_ORDER_SCIENCE_BEFORE_AUDIT_REPAIRED_PRIMARY_AND_INDEPENDENTLY_REPRODUCED` requires:

- exact five evidence hashes in both lanes;
- repaired primary all controls pass;
- unchanged independent all controls pass;
- distinct implementation paths/hashes;
- exact science authority and wrapper references;
- audit-to-science and wrapper-to-science-call relations true;
- audit supplemental true;
- reverse dependency absent;
- exact agreement `ordering_relation = SCIENCE_BEFORE_AUDIT`;
- exact agreement `same_iteration_bundle = execution_order = [Y science result, Y Actions provenance audit]`;
- atomic bundle true in both lanes;
- no science replay, later-descendant consumption, historical mutation, BD membership change, target leakage or claim-lock promotion.

`BLOCKED_ITER057BF_REPAIRED_ORDERING_EVIDENCE_NOT_REALIZED` applies if required extraction cannot be realized.

`FAIL_TECHNICAL_ITER057BF_REPAIRED_PRIMARY_OR_INDEPENDENT_DISAGREEMENT` applies if valid lanes disagree or another frozen control fails.

`INVALID_ITER057BF_HISTORY_TARGET_BLINDNESS_OR_SCOPE_VIOLATED` applies to any forbidden mutation/replay/target leakage.

Green CI alone is not PASS.

## Authority semantics

A scoped PASS would supersede only the technical execution blocker of Iter057BE and establish the same-iteration replay scheduling bundle. Iter057BE remains historical BLOCKED. The PASS would authorize prospectively preregistering a corrected Iter057Y science-first bundle replay, not perform that replay itself.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
