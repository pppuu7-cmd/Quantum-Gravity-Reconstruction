# Quantum Gravity Reconstruction (QGR)

A constraint-driven research program for constructing and attempting to falsify a candidate quantum-gravity model.

## Status

- Repository phase: `BOOTSTRAP_COMPLETE / MODEL_CONSTRUCTION_ACTIVE`
- QGR iteration: `Iter001`
- Repository infrastructure readiness: **100%**
- Canonical candidate-program readiness: **24%** (carried from the KMQGB Candidate Gravity R3 baseline; this is not a claim that a physical theory is 24% proven)
- Promoted physical ansatz: **none**
- Theory established: **false**
- Benchmark winner: **false**
- KMQGB global decision: `NOT_YET_AUTHORIZED`

## Scientific role

QGR is deliberately separate from:

1. **RQIR** — frozen methodology / reconstruction and comparator logic.
2. **KMQGB** — independent benchmark of known quantum-gravity frameworks and future candidates.
3. **QGR** — construction space for a new candidate model.

QGR must not modify benchmark criteria in order to make its own candidate pass. The candidate is built here and later exported to the frozen RQIR/KMQGB evaluation machinery.

## Core principle

Do not begin from a preferred beautiful formula and retrofit tests around it. Begin from a frozen set of scientific obligations and known failure modes, construct the smallest sufficiently rigid dynamical object that can satisfy them, and try to kill it early.

## Mandatory design obligations

A promotable QGR candidate must eventually provide, in one internally identified realization:

- a mathematically defined microscopic state/dynamical structure;
- a controlled quantum dynamics or amplitude/measure with explicit normalization rules;
- a canonical or physically justified treatment of regulator removal / distributional extension / renormalization, rather than an unconstrained counterterm catalogue;
- a causal and probabilistically consistent physical sector;
- a controlled 4D Lorentzian low-energy route to Einstein/GR behavior;
- explicit parameter identity from microscopic to infrared descriptions;
- at least one normalized observable calculable on both sides of the UV-to-IR chain;
- a common-domain comparator with propagated theoretical/numerical uncertainty;
- low enough functional freedom that the construction can genuinely fail;
- at least one discriminating prediction, exclusion region, or nontrivial structural theorem not inserted as an input.

These are obligations, not assumptions that a solution exists.

## Fail-closed governance

Allowed scientific states include `PASS`, `PARTIAL`, `FAIL`, and `BLOCKED`. `BLOCKED` means required evidence or an object is missing; it is never silently converted into `FAIL`. Missing evidence is never treated as evidence of impossibility.

No statement such as “all known models are wrong”, “a new model is required”, or “QGR is correct” is authorized unless the corresponding independent benchmark gate explicitly permits it.

## Repository map

- `docs/CONSTITUTION.md` — frozen construction rules and anti-overfitting policy.
- `docs/ROADMAP.md` — staged construction and falsification roadmap.
- `docs/KMQGB_HANDOFF.md` — benchmark-derived obligations imported into QGR without changing KMQGB.
- `recovery/CURRENT_FRONT.md` — human-readable current research front.
- `recovery/state.json` — machine-readable recovery state.
- `recovery/RECOVERY_PLAYBOOK.md` — minimal instructions for resuming QGR from another chat/session.
- `iterations/ITERATION_001.md` — bootstrap iteration and first scientific target.

## Immediate research target

`QGR-G0`: identify the **minimum viable ontology and dynamical closure architecture** that can satisfy the frozen obligations without importing uncontrolled functional freedom.

No physical ansatz is promoted during Iter001. Candidate branches may be proposed, scored, and killed, but promotion requires passing the pre-ansatz gate in `docs/ROADMAP.md`.
