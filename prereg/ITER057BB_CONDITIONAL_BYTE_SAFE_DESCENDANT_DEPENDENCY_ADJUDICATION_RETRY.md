# Iter057BB — Conditional Byte-Safe Descendant Dependency Adjudication Retry

Status: **PROSPECTIVELY PREREGISTERED / EXECUTION LOCKED**  
Date: 2026-09-17

## Execution lock

This gate may be implemented or executed **only if** Iter057BA terminates as exactly:

`PASS_SCOPED_ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_INDEPENDENTLY_REPRODUCED`.

If Iter057BA is FAIL/BLOCKED/INVALID, Iter057BB remains unexecuted and must not be used to bypass that result.

## Purpose

Retry the scientific-dependency adjudication originally frozen in Iter057AU after replacing only the proven execution-layer provenance-reader defect with the independently reproduced byte-safe/canonical reader authority. Determine, without replaying descendant science, which post-Iter057X scientific records are direct/transitive load-bearing descendants of the legacy degree-six Weyl3 source, which are independent, and which remain unresolved.

## Frozen parent authorities

- Original Iter057AU preregistration: `616859890df95057556d265612c53da839a5848a`.
- Historical Iter057AU terminal BLOCKED: durable result `c299683e28289788c53797e5ede1cafaf09f5431`, classification `BLOCKED_ITER057AU_UNRESOLVED_PROVENANCE`.
- Iter057AV establishes that unchanged AU execution failed reproducibly at implicit UTF-8 decode of byte `0x8a`; no descendant science was consumed.
- Iter057AZ remains a terminal technical FAIL and is not a reader authority.
- Iter057BA may become the technical reader authority only under the exact execution lock above.
- Iter057AT corrected ordered 840-vector authority remains fixed: SHA256 `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.
- `c6` remains symbolic/unfixed.

## Frozen census and target blindness

The scientific-result census is frozen to the **same preregistration snapshot used by Iter057AU**, commit `616859890df95057556d265612c53da839a5848a`. Results created after that snapshot (including AU through BA technical diagnostics) are not members of the dependency census and must not influence classification.

No descendant scientific outcome/classification may be used as a target while deciding dependency. No descendant scientific computation may be replayed inside this gate.

## Frozen dependency classes

Every censused post-Iter057X scientific result record must receive exactly one:

- `DIRECT_LOAD_BEARING_DEPENDENT`
- `TRANSITIVE_LOAD_BEARING_DEPENDENT`
- `INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE`
- `UNRESOLVED_PROVENANCE`

Definitions are unchanged from Iter057AU. `UNRESOLVED_PROVENANCE` remains fail-closed for replay planning.

## Frozen byte-safe provenance semantics

Only execution mechanics are repaired:

1. `git show`, tree/file enumeration, commit-file inspection and other provenance acquisition must return bytes without implicit `text=True` decoding.
2. Text-like provenance is decoded as strict UTF-8.
3. A non-UTF8 provenance object is represented deterministically by its raw SHA256 plus `NON_UTF8_PROVENANCE`; it must never be silently ignored/replaced/coerced.
4. A non-UTF8 object may still contribute graph identity through raw SHA/path/commit metadata, but no textual dependency statement may be inferred from undecodable bytes.
5. If a classification would require textual content from an undecodable provenance object and no independent byte-level/explicit reference evidence resolves it, that record is `UNRESOLVED_PROVENANCE`.
6. Historical files are read-only; no reset/clean/rewrite is allowed.

The canonical tracked-tree map serialization, if used for historical-tree integrity, is exactly Iter057BA v1 and not outcome-dependent.

## Frozen method

Reapply the original Iter057AU method to the frozen census:

1. construct a machine-readable DAG from repository provenance only — explicit input paths, imports, recorded source hashes, workflow inputs, result manifests, commit lineage and recovery lineage;
2. classify every census record exactly once;
3. propagate transitive dependency only along explicit acyclic earlier-result dependencies;
4. produce a deterministic replay queue containing direct/transitive dependents only, earliest scientifically load-bearing descendant first;
5. provide evidence path(s) for every classification;
6. produce a complete list of undecodable provenance objects and whether each is classification-load-bearing;
7. do not recompute descendant science.

## Independent reproduction

Two separately authored implementations are required. They must not import/call/read each other's classification payload. Both must use the same frozen census and class definitions but may use genuinely independent parsing/graph algorithms.

Scoped PASS requires:

- complete identical census;
- every record classified exactly once;
- deterministic acyclic DAG;
- deterministic replay queue with no independent record;
- evidence path for each classification;
- exact ordered classification agreement between implementations;
- exact replay-queue agreement;
- exact agreement on undecodable provenance object identities and load-bearing flags;
- historical tracked-tree integrity preserved;
- no descendant science consumed;
- no claim lock promoted.

## Frozen terminal classifier

- `PASS_SCOPED_ITER057BB_BYTE_SAFE_DESCENDANT_DEPENDENCY_ADJUDICATION_INDEPENDENTLY_REPRODUCED` iff every acceptance criterion passes and there are zero classification-load-bearing unresolved records.
- `BLOCKED_ITER057BB_UNRESOLVED_PROVENANCE` if execution is valid but at least one census classification remains unresolved because provenance is insufficient/undecodable.
- `FAIL_TECHNICAL_ITER057BB_INDEPENDENT_REPRODUCTION_OR_DAG_CONTROL_FAILURE` if the implementations execute but disagree or a frozen technical/DAG/integrity control fails.
- `INVALID_ITER057BB_CRITERIA_HISTORY_OR_TARGET_BLINDNESS_VIOLATED` if criteria/history/census are mutated, descendant outcomes are used as targets, or descendant science is consumed.

Green CI alone is not PASS.

## Authority ceiling and next decision

A PASS only adjudicates dependency and authorizes a separately preregistered replay of the **earliest** load-bearing descendant in the frozen replay queue. A BLOCKED identifies the exact unresolved provenance barrier. Neither result changes historical classifications by itself.

Theory established remains 0%; no experiment; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
