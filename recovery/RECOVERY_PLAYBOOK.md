# QGR Recovery Playbook

This file is the primary cross-chat/session continuation method. Never rely on remembered percentages.

## Minimal recovery sequence
1. Read `recovery/state.json` and `recovery/CURRENT_FRONT.md`.
2. Read `protocol/QGR_READINESS_SEMANTICS.json` and `protocol/QGR_PROGRAMME_READINESS_100_CONTRACT.json`.
3. Read `protocol/QGR_GATE_REGISTRY.json`, `docs/CONSTITUTION.md`, historical `docs/KMQGB_HANDOFF.md`, the dated delta registry and the KMQGB interface pin.
4. Inspect commits after recovery state; fresh repository authority beats chat memory.
5. Keep `science_sync.last_terminal_science` distinct from `science_sync.next_preregistered_science`.

## Canonical infrastructure state
Programme infrastructure is **100%** only in the research-program / roadmap sense. Authorization was obtained under the prospectively frozen A–P contract with 16/16 primary and independent Critic agreement. Re-run both evaluators whenever an infrastructure authority changes; a future failure must be treated fail-closed and repaired rather than ignored.

## Readiness axes
`repository_infrastructure_pct`, `candidate_program_pct`, and `theory_established_pct` are independent. Programme 100 means complete executable/recoverable/fail-closed research architecture only. It never means theory completion.

## Scientific-state preservation
`BLOCKED != FAIL`; `INVALID != FAIL`; CI green != scientific PASS; `PASS_SCOPED` != global/all-orders PASS. Missing evidence is not evidence of impossibility. Historical terminal results are immutable; corrected authorities use the dependency/supersession protocol rather than rewriting history.

## Verification commands
- `python code/qgr_programme_readiness_validator.py --kmqgb-root <pinned checkout> --require-100`
- `python code/qgr_programme_readiness_critic.py --kmqgb-root <pinned checkout>`
- `python code/qgr_clean_recovery_test.py`

The declared percentage is not evidence for either evaluator.

## KMQGB boundary
Do not modify KMQGB/RQIR. Before R2->R3, R4->R5 or R7->R8, inspect fresh KMQGB and append a dated delta only for new methodological/interface obligations. Candidate-specific benchmark outcomes may not become QGR construction targets. Drift returns `KMQGB_INTERFACE_VERSION_DRIFT` until a new adapter/delta is prospectively versioned.

## Heavy-compute rule
Structural blockers forbid heavy compute. Compute requires a defined mathematical object, observable, normalization, frozen comparison question, expected information gain and stopping rule.

## Current identity
Project: **Quantum Gravity Reconstruction (QGR)**. Programme infrastructure: **100%**. Theory established: **0%**. Last terminal science: `ITER057AQ`. Next preregistered science: `ITER057AR`, presently `PREREGISTERED_NOT_PRODUCED` unless fresh repository evidence says otherwise.
