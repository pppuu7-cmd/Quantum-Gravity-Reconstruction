# Iter057AY — Empty-directory Git-status semantics diagnostic

Status: PROSPECTIVELY PREREGISTERED, NOT YET PRODUCED

## Frozen question
Identify the exact Iter057AX attribution-control failure without changing Iter057AU/AW/AX classifications, dependency semantics, historical targets, or consuming/replaying descendant science.

## Frozen hypothesis
The sole Iter057AX lane failure is `post_dirty_exactly_harness_output=false` because Git does not represent an empty untracked directory in `git status --porcelain=v1 -z`. Iter057AX created `iter057aw-output/` but no file inside it before reading status, so the expected entry `?? iter057aw-output/` was not realizable.

## Frozen evidence target
Two independent target-blind lanes must reproduce, on the frozen AW implementation `1c4963a4bcc84a5bf331f0173c76b05d7a6a1864`:
1. pre-harness porcelain status is empty;
2. creating only empty `iter057aw-output/` leaves porcelain status empty;
3. tracked-tree SHA256 is unchanged;
4. after creating a sentinel file only inside that directory, porcelain status becomes exactly `?? iter057aw-output/` (or the byte-equivalent Git porcelain representation documented by the lane payload);
5. removing the sentinel restores empty porcelain status;
6. no descendant scientific payload is read, produced, replayed, compared, or reclassified.

Primary and independent lane JSON must agree bit-for-bit on the normalized observations and controls. Exact raw porcelain bytes and SHA256 digests must be serialized before terminal classification.

## Classification
PASS_SCOPED only if all frozen controls pass independently. Otherwise FAIL_TECHNICAL/BLOCKED fail-closed. Green CI alone is not PASS.

## Locks
Iter057AU remains BLOCKED. Iter057AW and Iter057AX remain terminal technical FAILs. Theory established=0%; no experimental confirmation; beta=1 unauthorized; c6 symbolic/unfixed; no global-theorem, unitarity, regulator-removal, UV-completion, new-physics, physical-weight, or KMQGB NEW_REQUIRED promotion.