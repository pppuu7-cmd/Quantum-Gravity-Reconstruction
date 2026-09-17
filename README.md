# Quantum Gravity Reconstruction (QGR)

A constraint-driven research program for constructing and attempting to falsify a candidate quantum-gravity model.

## Canonical status — 2026-09-17

- Repository infrastructure readiness: **100%**.
- Candidate-program / research-programme infrastructure readiness: **99%**, pending the prospectively frozen A–P completion validation.
- Candidate-program semantics: **research-program / roadmap infrastructure readiness only; not probability of correctness, not theory completion, and not fraction of quantum gravity solved**.
- Theory established: **0% / false**.
- Global interacting measure established: **false**.
- Regulator removal established: **false**.
- Experimental confirmation: **false**.
- Last terminal science: `ITER057AQ` — scoped causal-localization PASS.
- Next preregistered science: `ITER057AR` — `PREREGISTERED_NOT_PRODUCED`; it is independent of programme-infrastructure closure.

The historical **24%** Candidate Gravity marker in the bootstrap-era roadmap was imported from external KMQGB bookkeeping. It is preserved as history only and is superseded as a current QGR programme-readiness metric by `recovery/state.json` and `protocol/QGR_READINESS_SEMANTICS.json`.

## Separation of axes

Repository readiness, programme-architecture readiness, and scientific theory establishment are independent. A 100% programme infrastructure state, if executable validation authorizes it, means the scientific machine is fully specified and recoverable; it does not mean QGR is correct or complete.

## Scientific role

QGR is deliberately separate from RQIR (frozen methodology/comparator logic) and KMQGB (independent benchmarking). QGR must not modify benchmark criteria to make its own candidate pass. `BLOCKED != FAIL`; CI success is never scientific PASS.

## Programme infrastructure entrypoints

- `preregistration/QGR_PROGRAMME_INFRASTRUCTURE_100_COMPLETION.md` — prospectively frozen 99 -> 100 criteria.
- `protocol/QGR_PROGRAMME_READINESS_100_CONTRACT.json` — machine completion contract.
- `protocol/QGR_GATE_REGISTRY.json` — executable R0-R9 state machine.
- `schemas/qgr_candidate_export_v1.schema.json` — native QGR candidate export.
- `protocol/QGR_KMQGB_INTERFACE_PIN.json` — frozen KMQGB v1.3 intake pin.
- `code/qgr_programme_readiness_validator.py --require-100` — primary fail-closed evaluator.
- `code/qgr_programme_readiness_critic.py` — independent evaluator that does not trust the declared percentage.
- `recovery/CLEAN_SESSION_RECOVERY_MANIFEST.json` — chat-memory-free recovery test.

## Scientific governance

Construction remains subject to `docs/CONSTITUTION.md`, same-realization identity, explicit parameter/function freedom, prospective preregistration, independent criticism where required, provenance, and claim ceilings. Missing quantum measure, regulator removal, UV->IR map, normalized observable, GR map or benchmark object may legitimately remain `BLOCKED` inside fully complete programme infrastructure.

Current scientific details live in `recovery/CURRENT_FRONT.md`; recovery state lives in `recovery/state.json`.
