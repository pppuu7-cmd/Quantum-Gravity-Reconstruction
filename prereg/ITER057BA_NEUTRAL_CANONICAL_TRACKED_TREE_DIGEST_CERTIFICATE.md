# Iter057BA — Neutral Canonical Tracked-Tree Digest Certificate

Status: **PROSPECTIVELY PREREGISTERED, NOT YET IMPLEMENTED/PRODUCED**  
Date: 2026-09-17  
Parent technical evidence: Iter057AZ terminal `FAIL_TECHNICAL_ITER057AZ_INDEPENDENT_IMPLEMENTATION_OR_CONTROL_FAILURE`, durable result `87c9b6d029120aaeb38d0c5ff985df9125ae3470`.

## Question

Can two independently implemented byte-safe provenance readers reproduce the full Iter057AZ certificate when tracked-tree cleanliness is evaluated with a prospectively frozen, neutral and byte-exact canonical map serialization that was not used by either Iter057AZ lane?

## Motivation and anti-fitting rule

Iter057AZ localized the cross-lane disagreement solely to different serializations of the same unchanged ordered tracked-file content map. Both earlier serializations remain historical evidence. Iter057BA must not select either historical digest value as a target and must not fit to either implementation.

The canonical format below is new and frozen before either Iter057BA implementation exists.

## Frozen canonical tracked-tree map v1

1. Acquire tracked paths from `git ls-files -z` as raw bytes.
2. Each path must decode as strict UTF-8 for filesystem access; any path decode failure is fail-closed `NON_UTF8_TRACKED_PATH`.
3. Sort entries lexicographically by the **raw path bytes**.
4. For each entry compute `content_sha256_hex = sha256(file_bytes).hexdigest()` as lowercase ASCII.
5. Encode the path as lowercase hexadecimal ASCII: `path_hex = raw_path.hex()`.
6. Canonical byte stream is exactly:

   `b"QGR_TRACKED_TREE_MAP_V1\n" + concat(path_hex_ascii + b"\t" + content_sha256_hex_ascii + b"\n")`

   over the sorted entries.
7. The canonical tracked-tree digest is `sha256(canonical_byte_stream).hexdigest()`.
8. Empty/untracked harness output directories and files are not entries because the source set is exactly `git ls-files -z`.

This format is intentionally distinct from both Iter057AZ lane serializations.

## Frozen provenance-reader controls

Each implementation must independently establish:

- git/provenance bytes are acquired without implicit text decoding;
- strict UTF-8 only: no ignore/replace/Latin-1 fallback;
- frozen invalid `0x8a` fixture returns `NON_UTF8_PROVENANCE`, exact raw SHA256, and `UNRESOLVED_PROVENANCE`;
- valid `Weyl^3 provenance ✓` UTF-8 round trip is exact;
- tracked status is clean before and after (`git status --porcelain --untracked-files=no`);
- canonical tracked-tree digest before == after;
- a synthetic canonical-map perturbation control changes the canonical digest;
- no descendant science is loaded, replayed, classified, or consumed.

## Independence controls

- Two distinct implementation files are required.
- Neither implementation may import, call, source, or read runtime output from the other.
- Implementation SHA256 values must differ.
- Both implementations must independently emit the same normalized schema.
- Exact normalized agreement is required, including the new canonical tracked-tree digest.

## Forbidden actions

No `git reset`, `git clean`, `.gitignore` modification, historical-result mutation, target fitting, threshold weakening, lossy decode, reuse of Iter057AZ historical digest as an acceptance target, or descendant-science consumption.

## Frozen terminal classifier

- `PASS_SCOPED_ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_INDEPENDENTLY_REPRODUCED` iff both independent implementations pass every frozen control, implementation hashes differ, and normalized payloads agree exactly.
- `FAIL_TECHNICAL_ITER057BA_CANONICAL_CERTIFICATE_OR_INDEPENDENCE_CONTROL_FAILURE` if production executes but any frozen control/agreement/independence condition fails.
- `BLOCKED_ITER057BA_PRODUCTION_NOT_REALIZED` if required lane/aggregate artifacts or provenance cannot be produced.
- `INVALID_ITER057BA_CRITERIA_OR_HISTORY_MUTATED` if criteria/history are changed to obtain a favorable outcome.

## Authority ceiling

A scoped PASS certifies only the technical byte-safe reader + canonical tracked-tree cleanliness mechanism. It may authorize a **separately preregistered** future retry of the Iter057AU dependency adjudication. It does not itself reclassify Iter057AU/AW/AX/AZ and does not consume descendant science.

Theory established remains 0%; `beta=1` remains unauthorized; `c6` remains symbolic/unfixed; no global/quantum/experimental claim is authorized.
