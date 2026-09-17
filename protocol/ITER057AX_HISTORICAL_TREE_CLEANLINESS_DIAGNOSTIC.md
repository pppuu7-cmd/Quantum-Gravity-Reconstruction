# Iter057AX — Historical-tree cleanliness diagnostic

Status: PROSPECTIVELY PREREGISTERED BEFORE IMPLEMENTATION
Date: 2026-09-17

## Scope

Technical, target-blind diagnosis only. This gate may explain the reproducible `historical_result_tree_clean=false` control observed in terminal Iter057AW. It MUST NOT rerun Iter057AU, classify dependency descendants, consume/replay descendant science, alter historical results, or change any scientific threshold/target.

## Frozen inputs

- Iter057AW preregistration: `4a137c9cc17858fb8e43875d169dc0a28ae3bb1d`.
- Iter057AW implementation: `1c4963a4bcc84a5bf331f0173c76b05d7a6a1864`.
- Iter057AW production head: `c9f6422245e652caaecfbaa8cef8e91b1361af85`.
- Iter057AW authoritative run: `35220098375`.
- Iter057AW terminal artifact: `10496493918`.
- Iter057AW terminal artifact digest: `sha256:c85315aa4e396fe77d8e828f00ffdd0303f2557716a2c9f7688febb4f9d85d11`.
- Iter057AW classification remains permanently `FAIL_TECHNICAL_ITER057AW_BYTE_SAFE_REPAIR_CONTROL_FAILURE`.

## Frozen diagnostic question

Does the AW cleanliness failure arise solely because the workflow creates the untracked harness-output directory `iter057aw-output/` before evaluating `git status --porcelain`, rather than from a mutation of tracked historical/scientific repository content?

## Required controls

1. Reproduce the AW ordering exactly: create `iter057aw-output/` before cleanliness inspection.
2. Record raw `git status --porcelain` lines before harness output creation and after harness output creation.
3. Separate tracked-file mutations from untracked harness-generated paths without deleting, ignoring, staging, or modifying repository files.
4. PASS is permitted only if the pre-harness tracked tree is clean, the post-harness dirty set is exhaustively attributable to the newly created `iter057aw-output/` harness path, and tracked historical/scientific content remains byte-identical.
5. Any tracked mutation, pre-existing dirty path, additional untracked path, ambiguous status entry, or inability to prove attribution => FAIL/BLOCKED, never PASS.
6. Two independent lanes must reproduce the same normalized status classification and tracked-tree digest.
7. No descendant science may be produced, consumed, replayed, or reclassified.
8. No historical Iter057AU/AW result may be rewritten or retroactively promoted.

## Forbidden repairs in this gate

No `.gitignore` changes; no cleanup before measurement; no `git reset/clean`; no reinterpretation of AW terminal classification; no dependency-semantic changes; no target loading; no scientific computation.

## Claim locks

`theory established = 0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; finite certificates are not global theorems; G45 does not establish absolute energy positivity or quantum unitarity; G35–G37 distant roots do not authorize physical weights; KMQGB `NEW_REQUIRED` unauthorized.
