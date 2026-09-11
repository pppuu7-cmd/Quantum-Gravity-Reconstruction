# QGR Iteration 006 — Quantum Measure / Composition and Projective Refinement Reconstruction

Date: 2026-09-11
Status: `ACTIVE / PRIMITIVE_COMPOSITION_SEARCH`
Current task completion: **20%**
Candidate-program readiness: **49%**
Active local candidate: **QGR-L1**

## Starting authority

Iter005 closed the local two-derivative nonlinear bootstrap through quartic order and established scoped weak-background characteristic stability. It also exposed the first genuine same-realization refinement ambiguity: mixture/marginal second moments and second moments of coherently composed rank-1 frames are not generically equal.

Therefore R5 begins by reconstructing the primitive measure/amplitude/composition object rather than choosing an RG rule after the fact.

## Objective

Find the minimal quantum composition structure that simultaneously provides:

1. normalized refinement over the existing 24-history `B4` cell;
2. associative multi-level composition;
3. positivity / operational probabilities at the coarse level;
4. capacity for quantum coherence before coarse history information is discarded;
5. a projective marginal rule fixing the mixture-vs-coherent coarse second-moment ambiguity;
6. compatibility with the existing QGR-L1 second-moment field and pullback law;
7. no arbitrary history-dependent functions introduced only to preserve QGR-L1.

## Candidate classes

### A — classical probability/Markov history measure

Pros: normalized, positive, associative, easy projective marginals.

Fatal limitation as a fundamental QGR primitive: ordinary classical mixtures contain no coherent interference without adding a second structure.

Status: `PARTIAL / POSSIBLE_DECOHERED_LIMIT_NOT_SELECTED_AS_FUNDAMENTAL`.

### B — direct complex scalar amplitudes on histories

Pros: interference and associative path multiplication are natural.

Open problems: positivity/Born map, projective coarse state, phase freedom, and the relation between path amplitudes and the already derived linear coarse weight `1/24` are not fixed by scalar amplitudes alone.

Status: `PARTIAL / UNDERDETERMINED`.

### C — history-register isometry / completely positive coarse channel

Let the 24 refinement histories be orthogonal labels `|alpha>` in a temporary history register, and let `P` denote an orthogonal refinement projector on a candidate physical state space. Define

`V = sum_alpha |alpha> tensor K_alpha`.

For symmetry-equivalent branches take

`K_alpha = a P`.

Isometry on the physical `P`-subspace requires

`V^dagger V = sum_alpha K_alpha^dagger K_alpha = P`,

so

`24 |a|^2 P = P`,

hence

`|a| = 1/sqrt(24)`.

After tracing the history register,

`E(rho) = sum_alpha K_alpha rho K_alpha^dagger = P rho P`.

Thus every branch contributes superoperator weight `1/24`, exactly matching the earlier coarse normalization coefficient while the underlying branch amplitude magnitude is `1/sqrt(24)`.

At `n` refinement levels:

- branch count: `24^n`;
- branch amplitude magnitude: `24^(-n/2)`;
- summed Kraus normalization remains `P`;
- the coarse CP map remains `rho -> P rho P` on the scoped idealized projector sector.

The history register can remain coherent before tracing, so interference is not forbidden by construction. The coarse marginal becomes a mixture only when the projective coarse observable algebra discards the history label.

Status: `LEAD_CANDIDATE / PASS_SCOPED_ALGEBRAIC_NORMALIZATION_AND_ASSOCIATIVITY / PHYSICAL_HILBERT_REALIZATION_MISSING`.

### D — unrestricted quantum measure / decoherence functional

General enough to encode interference and coarse marginals, but currently contains excessive functional freedom unless generated from a more rigid composition object.

Status: `BLOCKED_TOO_UNCONSTRAINED_AS_STARTING_PRIMITIVE`.

## G1 scoped result

The isometry/CP-channel construction is the first candidate that explains why the same refinement can carry

- amplitude magnitude `1/sqrt(24)` at the fine coherent level,
- weight `1/24` at the coarse channel level,

without identifying the earlier `1/24` kernel weight with a quantum amplitude by fiat.

Classification:

`PASS_SCOPED_CHANNEL_LEVEL_REFINEMENT_NORMALIZATION_CANDIDATE`.

## Critical blocker

The projector `P` used in early CCRC toy models was a finite label-space projector. It has **not** been established as the physical Hilbert-space projector of QGR-L1.

Therefore the channel construction may not be promoted until QGR supplies:

- a state/Hilbert or generalized probabilistic space whose second-moment response is `G`;
- a physical refinement projector/constraint operator;
- an observable algebra identifying which history information is retained or traced;
- a demonstration that QGR-L1 local dynamics is the response/effective sector of this same object.

## Exact next gate — Iter006-G2

`QGR-ITER006-G2-STATE_SPACE_AND_PROJECTOR_RECONSTRUCTION`

1. Construct the smallest state-space realization carrying four rank-1 relational directions and a ten-component second-moment response `Sym^2(W4)`.
2. Derive, rather than assume, the constraint/refinement projector whose coarse channel can realize the `24`-history normalization.
3. Determine whether the projector is unique up to unitary equivalence or leaves uncontrolled functional freedom.
4. Define the coarse observable algebra and test whether projective marginalization fixes the second-moment refinement map.
5. Reject any realization chosen solely because its low-energy response reproduces QGR-L1.

## Claim locks

- QGR does not yet have a physical Hilbert-space completion.
- The early CCRC toy projector is not yet a physical QGR projector.
- The CP-channel construction is a scoped algebraic candidate, not a quantum-gravity theory.
- Continuum/RG closure and KMQGB passage remain open.
