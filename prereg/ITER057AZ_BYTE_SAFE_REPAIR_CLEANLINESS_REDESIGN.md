# Iter057AZ — BYTE-SAFE-REPAIR-CLEANLINESS-REDESIGN

Status: PROSPECTIVELY PREREGISTERED, NOT YET PRODUCED

## Motivation
Iter057AY independently established the Git-status semantics needed to diagnose the frozen Iter057AW cleanliness-control failure: creating an empty directory does not make `git status --porcelain` dirty; adding an untracked sentinel inside it does; removing the sentinel restores clean status while the tracked-tree digest remains unchanged. This gate does not reclassify Iter057AW/AX/AU.

## Frozen object
A new byte-safe provenance-reader repair certificate derived from the Iter057AW repair logic, with cleanliness measured only over tracked historical/scientific files rather than harness-owned untracked output directories.

## Frozen controls
1. Git object output is acquired as bytes, never implicitly decoded by `subprocess(..., text=True)`.
2. UTF-8 provenance text is decoded strictly. No `errors=ignore`, `errors=replace`, Latin-1 fallback, or lossy coercion is allowed.
3. Non-UTF8 provenance deterministically returns `NON_UTF8_PROVENANCE` together with SHA256 of the original bytes and maps fail-closed to `UNRESOLVED_PROVENANCE`.
4. Synthetic invalid byte `0x8a` must exercise the non-UTF8 path.
5. Valid UTF-8 round-trip control must remain exact.
6. Historical/scientific tracked-tree cleanliness is defined prospectively as: clean tracked status before harness execution AND identical SHA256 digest of the ordered tracked-file content map before/after. Harness-owned untracked output paths are excluded from this scientific-history cleanliness predicate and must be reported separately.
7. No `git reset`, `git clean`, `.gitignore` modification, target fitting, threshold weakening, or historical result mutation is permitted.
8. No descendant science may be loaded, replayed, classified, or consumed.
9. Two independently implemented lanes must reproduce the byte-safe reader semantics, invalid-byte classification, valid UTF-8 behavior, and tracked-tree cleanliness result.
10. PASS requires all frozen controls and independent agreement. Green CI alone is not PASS.

## Authority semantics
Iter057AW remains terminal technical FAIL; Iter057AX remains terminal technical FAIL; Iter057AU remains historical BLOCKED. A scoped PASS here authorizes only a separately preregistered future dependency-adjudication retry using the certified byte-safe reader. It does not itself adjudicate descendants or establish QGR physics.

## Claim locks
Theory established = 0%; no experimental confirmation; beta remains calibration/matching only and beta=1 is not authorized; c6 remains symbolic/unfixed; finite certificates are not global theorems; G45 does not establish absolute energy positivity or quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB NEW_REQUIRED is not authorized.
