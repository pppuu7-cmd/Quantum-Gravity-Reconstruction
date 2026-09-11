# KMQGB -> QGR Scientific Handoff

Purpose: import lessons from the independent Known-Models Quantum-Gravity Benchmark as construction constraints without modifying or reinterpreting KMQGB verdicts.

## Authority boundary

At QGR bootstrap (2026-09-11), the KMQGB global decision remains `NOT_YET_AUTHORIZED`; D2 remains not closed, D4 remains globally partial/not closed, and D7 remains not closed. Therefore QGR construction is scientifically useful as a parallel candidate program, but KMQGB has **not** established that a new theory is necessary.

The handoff below encodes failure modes to avoid. It is not a claim that every known framework fails.

## Imported failure-mode classes

### F1 — Same-realization fragmentation
Evidence for the UV, continuum, GR, and observable endpoints may exist separately but not in one identified realization.

QGR response: architecture must preserve a traceable object/parameter identity through the full chain.

### F2 — Normalization / regulator / extension underdetermination
Formal amplitudes can exist while finite normalized physical objects require extra prescriptions, extension data, regulator choices, or counterterms.

QGR response: prefer a construction where finiteness/extension data are fixed by the dynamics, symmetry plus consistency, or another explicit physical principle. Count residual freedom instead of hiding it.

### F3 — Symmetry does not automatically determine dynamics
Recent KMQGB LQG-front work shows that strong permutation and rotational symmetry can greatly reduce local freedom yet still leave a nontrivial invariant coefficient space. As of Iter323, a scoped formal K5 model retains a 28-dimensional joint S5 x SO(3) invariant space requiring actual dynamical coefficients. This is a theory-specific scoped result, not a no-go.

QGR response: do not assume “maximal symmetry” uniquely fixes the model. Require a dynamical mechanism for residual coefficients.

### F4 — Formal algebraic recovery is weaker than physical measure support
An unrestricted algebraic sector sum can reconstruct a standard object while a physically admissible causal measure may have restricted support or different weights.

QGR response: distinguish algebraic identities from physical measure/weight theorems.

### F5 — Component objects need not inherit full representation properties
A branch/component of a representation decomposition may fail to be a representation even when the completed object is one.

QGR response: prove composition/gluing at the exact object level actually used by the candidate.

### F6 — Standard finiteness theorems may not transfer to modified causal objects
Polynomial boundedness or similarity to a known finite object does not automatically establish noncompact integrability of a modified object.

QGR response: prove applicability conditions or derive a direct finite normalized certificate.

### F7 — Ordinary cutoff divergence does not equal a no-go
Observed homogeneous or multiscale divergences create an extension/renormalization burden, but do not alone rule out canonical distributional or renormalized definitions.

QGR response: distinguish `ordinary_limit_diverges` from `no_consistent_extension_exists`.

### F8 — More numerical precision cannot repair a missing map
When the blocker is structural (parameter identity, normalization, observable matching, theorem applicability), heavy compute is not the next scientific step.

QGR response: use structural gates before expensive numerical campaigns.

## Design priorities inferred for QGR

QGR should preferentially search for architectures with:

1. intrinsically low functional freedom;
2. prospective finite/extension rules rather than post-hoc counterterms;
3. exact composition/gluing identities at the physical-object level;
4. a single UV-to-IR realization;
5. 4D Lorentzian GR recovery with explicit corrections;
6. normalized observables and error propagation;
7. cheap early falsifiers.

## Claim lock inherited from KMQGB

Until KMQGB itself changes state under its frozen rules, QGR must preserve all of the following:

- known frameworks are not collectively declared wrong;
- `BLOCKED` remains distinct from `FAIL`;
- QGR is a candidate construction, not an authorized necessity claim;
- `NEW_REQUIRED` is not asserted as a KMQGB verdict;
- theory-specific LQG findings are not universalized into quantum-gravity no-go statements.

## Synchronization rule

This handoff is a snapshot. Before any major QGR promotion gate (R2 -> R3, R4 -> R5, R7 -> R8), inspect the current KMQGB recovery front and append a dated delta file if genuinely new failure modes or benchmark requirements have appeared. Do not silently rewrite historical QGR constraints.
