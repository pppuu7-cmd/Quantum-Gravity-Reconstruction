# Iter057AZ — Execution-only repair 1: independent-lane realization

Status: PROSPECTIVELY FROZEN BEFORE REPAIRED PRODUCTION
Date: 2026-09-17
Parent gate: `ITER057AZ_BYTE_SAFE_REPAIR_CLEANLINESS_REDESIGN`
Original preregistration: `31def60c38017c8fd9595e1a2772bc75cad42aba`
First production attempt: run `35243086938`, head `5c2f2a24e704c60404038f67677a889ad464f9be`

## Defect localized before repaired production

The first production attempt produced two successful lane payloads but both matrix jobs invoked the same implementation file, `scripts/qgr_iter057az_bytesafe_cleanliness.py`. Therefore frozen control 9 — **two independently implemented lanes** — was not realized. Green CI and matching payloads from that attempt are non-authoritative for PASS.

This is an execution/implementation defect only. No scientific or technical threshold, expected byte classification, cleanliness predicate, claim ceiling, or terminal criterion from the original Iter057AZ preregistration is changed.

## Frozen execution repair

1. Keep the original primary implementation unchanged.
2. Add a separately authored independent implementation that does not import, call, source, or copy runtime results from the primary implementation.
3. The independent implementation must reconstruct the same frozen semantics directly from the original Iter057AZ preregistration:
   - byte acquisition without implicit text decoding;
   - strict UTF-8 decode;
   - deterministic `NON_UTF8_PROVENANCE` / `UNRESOLVED_PROVENANCE` for the frozen `0x8a` fixture with exact raw SHA256;
   - exact valid UTF-8 round trip;
   - tracked-only clean status before/after;
   - identical ordered tracked-file content-map digest before/after;
   - no descendant science consumed.
4. The repaired workflow must dispatch primary and independent lanes to distinct implementation files and record both implementation SHA256 values.
5. PASS additionally requires the two implementation SHA256 values to differ, both lane payloads to report all original controls true, and the normalized payloads (excluding lane/implementation metadata) to agree exactly.
6. No descendant science may be loaded, replayed, classified, or consumed.
7. Do not alter Iter057AU/AW/AX classifications.
8. No target fitting, threshold weakening, `git reset`, `git clean`, `.gitignore` modification, lossy decoding, or historical-result mutation is allowed.

## Frozen terminal semantics for repaired attempt

- `PASS_SCOPED_ITER057AZ_BYTE_SAFE_REPAIR_INDEPENDENTLY_REPRODUCED` iff all original Iter057AZ controls pass and independent implementations reproduce the same normalized certificate.
- `FAIL_TECHNICAL_ITER057AZ_INDEPENDENT_IMPLEMENTATION_OR_CONTROL_FAILURE` if the repaired production executes but any frozen control or implementation-independence requirement fails.
- `BLOCKED_ITER057AZ_REPAIRED_PRODUCTION_NOT_REALIZED` if required artifacts cannot be produced or provenance cannot be established.
- `INVALID_ITER057AZ_CRITERIA_OR_HISTORY_MUTATED` if frozen criteria/history are altered to obtain a favorable result.

A scoped PASS authorizes only a separately preregistered future Iter057AU dependency-adjudication retry using the certified byte-safe reader. It is not descendant adjudication and does not establish QGR physics.

All existing claim locks remain unchanged; theory established remains 0%; `beta=1` remains unauthorized; `c6` remains symbolic/unfixed.
