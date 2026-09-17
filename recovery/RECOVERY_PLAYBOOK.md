# QGR Recovery Playbook

This file is the primary cross-chat/session continuation method. Never rely on remembered percentages.

## Minimal recovery sequence

1. Read `recovery/state.json`.
2. Read `recovery/CURRENT_FRONT.md`.
3. Read `protocol/QGR_READINESS_SEMANTICS.json` and `protocol/QGR_PROGRAMME_READINESS_100_CONTRACT.json`.
4. Read `protocol/QGR_GATE_REGISTRY.json` for R0-R9 protocol/status separation.
5. Read `docs/CONSTITUTION.md`.
6. Read historical `docs/KMQGB_HANDOFF.md`, then `docs/kmqgb_deltas/REGISTRY.json` and `protocol/QGR_KMQGB_INTERFACE_PIN.json`.
7. Inspect commits after the SHA represented by recovery state; fresh repository authority beats chat memory.
8. Keep `science_sync.last_terminal_science` distinct from `science_sync.next_preregistered_science`.

## Readiness axes

`repository_infrastructure_pct`, `candidate_program_pct`, and `theory_established_pct` are independent. Programme 100 means complete executable/recoverable/fail-closed research architecture only. It never means theory completion.

## Scientific-state preservation

`BLOCKED != FAIL`; `INVALID != FAIL`; CI green != scientific PASS; `PASS_SCOPED` != global/all-orders PASS. Missing evidence is not evidence of impossibility. Historical terminal results are immutable; corrected authorities use the dependency/supersession protocol rather than rewriting history.

## Programme 100 recovery

A clean session must be able to run:

- `python code/qgr_programme_readiness_validator.py --kmqgb-root <pinned checkout> --require-100`
- `python code/qgr_programme_readiness_critic.py --kmqgb-root <pinned checkout>`
- `python code/qgr_clean_recovery_test.py`

The declared percentage is not evidence for either evaluator. If any A–P obligation fails, keep candidate-program readiness <=99 and report the exact failed obligation.

## KMQGB boundary

Do not modify KMQGB/RQIR. Before R2->R3, R4->R5 or R7->R8, inspect fresh KMQGB and append a dated delta only for new methodological/interface obligations. Candidate-specific benchmark outcomes may not become QGR construction targets. Drift from the pinned v1.3 interface returns `KMQGB_INTERFACE_VERSION_DRIFT` until a new adapter/delta is prospectively versioned.

## Heavy-compute rule

Structural blockers forbid heavy compute. Compute requires a defined mathematical object, observable, normalization, frozen comparison question, expected information gain and stopping rule.

## Current identity

Project: **Quantum Gravity Reconstruction (QGR)**. Last terminal science: `ITER057AQ`. Next preregistered science: `ITER057AR`, presently `PREREGISTERED_NOT_PRODUCED` unless fresh repository evidence says otherwise.
