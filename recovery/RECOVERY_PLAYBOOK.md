# QGR Recovery Playbook

This file is the primary cross-chat/session continuation method.

## Minimal recovery sequence

When starting from another chat/session, do **not** rely on remembered percentages or an old conversation summary. Recover QGR from the repository in this order:

1. Read `recovery/state.json`.
2. Read `recovery/CURRENT_FRONT.md`.
3. Read the newest file in `iterations/`.
4. Read `docs/CONSTITUTION.md` before proposing or promoting any candidate architecture.
5. Read `docs/KMQGB_HANDOFF.md` and then inspect the current KMQGB recovery front for changes since the last QGR synchronization.
6. Inspect the most recent QGR commits after the commit recorded in `state.json`.
7. Continue only from the exact next gate recorded in `CURRENT_FRONT.md` unless new evidence explicitly changes the priority.

## Required status report at every research iteration

Every substantive QGR iteration should report and record at least:

- QGR iteration number;
- overall candidate-program readiness percentage;
- current task completion percentage;
- active roadmap stage;
- active hypothesis/branch, if any;
- strongest new result;
- strongest surviving blocker;
- whether any claim lock changed;
- whether KMQGB/RQIR synchronization was checked;
- exact next falsification/completion gate.

Percentages are workflow/readiness indicators only. They are not probabilities that the theory is true.

## Backup discipline

At the end of every substantive iteration:

1. Create/update `iterations/ITERATION_NNN.md` with assumptions, derivations/computations, result class, scope boundary, and next gate.
2. Update `recovery/CURRENT_FRONT.md` to the newest scientific front.
3. Update `recovery/state.json` so a machine/session can resume without parsing prose history.
4. If a new general methodological lesson was learned, append a versioned document under `docs/` rather than silently editing the frozen constitution.
5. If KMQGB introduced a genuinely new failure mode relevant to QGR, append a dated handoff delta; do not rewrite the historical snapshot.
6. Record exact commit SHAs or provenance for external benchmark facts that materially constrain the candidate.

## Scientific-state preservation

Never convert between these states during recovery merely to simplify the story:

- `BLOCKED` != `FAIL`;
- `PARTIAL` != `PASS`;
- `PASS_SCOPED` != family/global PASS;
- a divergent ordinary regulator limit != proof that no distributional/renormalized extension exists;
- an inherited readiness marker != evidence of correctness.

## Branch recovery rule

If multiple candidate architectures are being explored, each branch must have:

- a unique branch ID;
- fixed assumptions;
- prospective kill criteria;
- parameter/free-function count;
- status (`PROPOSED`, `PARTIAL`, `BLOCKED`, `FAIL_SCOPED`, `PROMOTABLE`, `REJECTED`);
- reason for status.

Never merge evidence from incompatible branches into a single PASS.

## Heavy-compute rule

Before launching expensive computation, record why the blocker is computational rather than structural. Do not use more compute as a substitute for a missing theorem, undefined observable, unknown normalization, or absent parameter map.

## Emergency reconstruction

If `CURRENT_FRONT.md` and `state.json` disagree:

1. prefer the newest Git commit with explicit scientific provenance;
2. inspect the latest iteration log;
3. treat the inconsistency as a recovery defect;
4. repair both recovery files before advancing the science.

If an old chat claims a stronger scientific result than the repository, the repository wins unless the stronger result can be independently reconstructed and committed with provenance.

## Current identity

Project: **Quantum Gravity Reconstruction (QGR)**
Repository: `pppuu7-cmd/Quantum-Gravity-Reconstruction`
Initial scientific construction target: `QGR-G0` — minimum viable ontology and dynamical closure architecture.
