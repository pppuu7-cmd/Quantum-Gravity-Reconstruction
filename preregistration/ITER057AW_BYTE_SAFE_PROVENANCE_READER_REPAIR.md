# Iter057AW — byte-safe provenance reader repair

Status: **PROSPECTIVELY FROZEN**
Date: 2026-09-17
Gate: `ITER057AW_BYTE_SAFE_PROVENANCE_READER_REPAIR`

## Purpose

Iter057AV terminally localized the unchanged frozen Iter057AU execution defect to a reproducible `UnicodeDecodeError` in the provenance-reader path. Iter057AU remains historically BLOCKED and no descendant science is authorized for replay or consumption here. This gate repairs only byte handling in the provenance reader and validates that repair target-blind before any dependency adjudication is rerun.

Frozen parent authority: Iter057AU implementation `30aa968631d3c7f0ea82ea054b2abb14492748b3`; Iter057AU preregistration/census `616859890df95057556d265612c53da839a5848a`; Iter057AV preregistration `bfb6f31b9385d076695d7c3d199bf7da7b06bcc4`; Iter057AV production `f92d67e6f1c8f619c8f0c8292bbd313ca6c7fdb7`; Iter057AV run `35214572158`; artifact `10493153837`; digest `sha256:c1d2543242706c0792f7be4aa9a688dd204bf27b38967759b897c3ed1fc14668`; normalized error `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8a in position 287: invalid start byte`.

## Frozen offending path and repair policy

The frozen Iter057AU reader invokes `git show <ref>:<path>` via Python `subprocess.run(..., text=True, stdout=PIPE, ...)` in `read_at()`. This implicitly decodes stdout as text before the classifier can handle non-UTF-8 bytes. The repair is restricted to this boundary and equivalent bounded provenance reads.

1. Git stdout MUST be captured as bytes (`text=False` / no implicit decoding).
2. Candidate textual provenance MUST be decoded with strict UTF-8. No locale-dependent decoding and no lossy `errors=ignore` or `errors=replace` is permitted.
3. If a candidate path cannot be decoded as strict UTF-8, the reader MUST return a deterministic `NON_UTF8_PROVENANCE` condition carrying only path/ref plus SHA256 of raw bytes; it MUST NOT crash and MUST NOT inspect or infer semantic content from undecodable bytes.
4. Any scientific record whose required provenance depends on such an undecodable object MUST fail closed as `UNRESOLVED_PROVENANCE`; undecodable evidence MUST NOT be treated as evidence of independence or dependence.
5. Existing dependency vocabulary, regexes, record census, DAG propagation, evidence rules, source ordering, thresholds, historical targets and scientific classifications are frozen unchanged.
6. No descendant scientific result may be replayed, recomputed, consumed or reclassified in Iter057AW. Iter057AU remains historically BLOCKED.

## Frozen negative controls

Before any later AU replacement gate is permitted, the repaired reader must pass all of these target-blind controls:

- valid ASCII/UTF-8 fixture round-trips byte-for-byte to the same decoded text;
- a synthetic fixture containing byte `0x8a` deterministically returns `NON_UTF8_PROVENANCE` and raw-byte SHA256 without exception;
- invalid UTF-8 cannot be silently dropped/replaced;
- identical invalid bytes produce identical sentinel/fingerprint in two independent executions;
- repository historical result tree remains clean;
- no descendant scientific payload is produced or consumed;
- the repair diff is confined to byte/decode handling plus dedicated technical tests/workflow/documentation required for this gate.

## Terminal classifications

`PASS_SCOPED_ITER057AW_BYTE_SAFE_PROVENANCE_READER_REPAIR_CERTIFIED` iff all frozen byte-handling controls and two independent technical reproductions pass exactly. PASS authorizes only a separately prospectively preregistered replacement dependency-adjudication run; it does not reclassify Iter057AU.

`FAIL_TECHNICAL_ITER057AW_BYTE_SAFE_REPAIR_CONTROL_FAILURE` iff the repaired reader executes but any frozen byte-handling or fail-closed control fails reproducibly.

`BLOCKED_ITER057AW_BYTE_SAFE_REPAIR_NOT_REALIZED` iff required technical evidence cannot be produced.

`INVALID_ITER057AW_SEMANTIC_DRIFT_OR_DESCENDANT_REPLAY` iff dependency semantics, scientific criteria, census, historical targets, or descendant outcomes are changed/read for tuning, or descendant science is replayed.

## Claim ceiling

Technical repair only. `c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established = 0%; no experimental confirmation; finite certificate != theorem; classical != quantum; diagnostic != closure; KMQGB `NEW_REQUIRED` unauthorized.
