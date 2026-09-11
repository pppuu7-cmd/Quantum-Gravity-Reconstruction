# QGR Iteration 002 — G0 Architecture Matrix

Date: 2026-09-11
Status: `ACTIVE / MATRIX_GENERATED / KILL_TESTS_NOT_YET_EXECUTED`
Current task completion: **45%**
Canonical candidate-program readiness: **24%** (unchanged pending a promotable branch)

## Objective

Generate genuinely distinct candidate architecture classes under Constitution v1.0 before writing a preferred QGR action/amplitude. Score them prospectively and predeclare cheap kill tests.

This iteration does **not** claim novelty for the architecture classes themselves. Several primitives have analogues in existing research traditions; the purpose is to identify a reconstruction architecture that may later become distinct through its jointly imposed closure rules.

## Fixed scoring

Scores 0-4 use the dimensions from `docs/ARCHITECTURE_MATRIX_TEMPLATE.md`:
`O,C,K,F,G,L,S,R,Q,E`.

A high preliminary score does not promote a branch. Fatal gates and kill tests dominate totals.

---

## Branch A — CCRC: Constraint-Closed Relational Complex

### Primitive
Finite relational events/cells with typed adjacency and orientation data. Quantum states are amplitudes over finite labelled relational complexes. Geometry is not a fundamental background variable; geometric operators must be reconstructed from relational labels/invariants.

### Dynamics concept
Do not choose independent local amplitudes freely. Define a small generating set of local consistency constraints and seek a physical projector/measure whose composition, causal admissibility, and refinement consistency fix the allowed amplitudes.

### Candidate rigidity mechanism
`constraint closure + exact gluing + refinement consistency + normalization` jointly determine or sharply reduce local coefficients.

### Main risk
The consistency equations may either have no nontrivial solution or reproduce a known spin-foam/group-field-type structure with the same extension freedom.

### Prospective cheap kill tests
A1. **Composition test:** show that the proposed constrained gluing is associative / refinement-compatible on the smallest nontrivial complexes.
A2. **Geometry test:** construct at least one nonzero geometric observable from relational data without inserting a continuum metric.
A3. **Rigidity test:** solve the smallest coefficient system and verify that consistency reduces the coefficient space to finite low dimension rather than leaving arbitrary functions.

### Preliminary score
- O=4
- C=3
- K=4
- F=2
- G=3
- L=2
- S=3
- R=4
- Q=3
- E=2
- **Total = 30/40**

Status: `PARTIAL / HIGH_PRIORITY_FOR_KILL_TESTS`

---

## Branch B — CQCG: Compositional Quantum-Channel Geometry

### Primitive
Finite local quantum systems/operator algebras connected by physically admissible quantum channels or compositional morphisms. The primitive structure is operational/compositional rather than geometric.

### Dynamics concept
Seek a restricted class of channels selected by global consistency, reversibility/causal conditions where appropriate, symmetry, and a variational or fixed-point principle. Geometry is reconstructed from distinguishability/correlation/response structure rather than assumed adjacency lengths.

### Candidate rigidity mechanism
`complete positivity / physical probability + compositional consistency + causal factorization + extremal/fixed-point condition`.

### Main risk
It may naturally reconstruct information geometry but fail to generate a dynamical 4D Lorentzian metric satisfying Einstein equations without importing extra geometric structure.

### Prospective cheap kill tests
B1. **Lorentzian-signature test:** determine whether causal/signature structure can arise intrinsically rather than by an external graph/time label.
B2. **Geometry-content test:** determine whether channel invariants support tensorial geometric observables beyond generic information distance.
B3. **Dynamics-rigidity test:** count admissible channel families after constraints; reject if arbitrary channel functions remain.

### Preliminary score
- O=4
- C=4
- K=3
- F=3
- G=2
- L=1
- S=2
- R=4
- Q=4
- E=3
- **Total = 30/40**

Status: `PARTIAL / HIGH_RIGIDITY_BUT_GR_ROUTE_WEAK`

---

## Branch C — PCMH: Projectively Consistent Causal Measure on Histories

### Primitive
A directed family of finite causal histories/complexes with coarse-graining maps. The fundamental object is a consistent family of finite-resolution quantum measures/amplitudes rather than a single fixed lattice.

### Dynamics concept
Define finite-level measures and require exact projective/cylindrical consistency under coarse graining. The continuum object, if it exists, is the compatible limit. Causality is encoded in the admissible-history category rather than imposed only after summation.

### Candidate rigidity mechanism
`projective consistency + causal support + normalization + symmetry` fixes admissible finite-level measures.

### Main risk
Projective consistency may still permit a huge measure family, or the physically interesting Lorentzian continuum may not exist.

### Prospective cheap kill tests
C1. **Two-level consistency test:** construct the smallest refinement pair and solve the exact pushforward consistency equation.
C2. **Freedom-count test:** measure the dimension of the compatible finite-level measure family; reject if it grows uncontrollably with refinement.
C3. **Causal normalization test:** verify normalized interference/measure rules on the smallest causal history set without post-hoc regulator choices.

### Preliminary score
- O=3
- C=4
- K=4
- F=3
- G=2
- L=2
- S=4
- R=3
- Q=3
- E=2
- **Total = 30/40**

Status: `PARTIAL / HIGH_SAME_REALIZATION_POTENTIAL`

---

## Branch D — LCSD: Lorentzian Causal-Spectral Dynamics

### Primitive
An algebra/state together with a causal-spectral operator whose invariants encode geometry. The primitive object is algebraic/spectral rather than a discretized metric.

### Dynamics concept
Seek dynamics from spectral consistency plus causal/state conditions, with the spectrum/operator jointly constrained across scales. Geometric observables are reconstructed spectrally.

### Candidate rigidity mechanism
`algebraic representation + causal spectral constraints + spectral normalization + fixed-point/consistency law`.

### Main risk
Euclidean/spectral reconstruction may be much easier than Lorentzian causal dynamics; a generic spectral functional can hide arbitrary functions and reproduce the same underdetermination QGR is trying to avoid.

### Prospective cheap kill tests
D1. **Lorentzian reconstruction test:** identify a finite toy object where causal order/signature is recoverable from the exact algebraic-spectral data.
D2. **Functional-freedom test:** determine whether dynamics require an arbitrary spectral function; reject absent a principle fixing it.
D3. **Composition test:** establish how two microscopic subsystems glue without destroying the causal-spectral constraints.

### Preliminary score
- O=3
- C=2
- K=3
- F=3
- G=4
- L=2
- S=3
- R=3
- Q=3
- E=3
- **Total = 29/40**

Status: `PARTIAL / GEOMETRY_STRONGER_THAN_COMPOSITION`

---

## Branch E — RQEC: Relational Quantum Error-Correcting Geometry

### Primitive
Finite relational quantum degrees of freedom with constrained isometric encoding maps. Robust subspaces encode emergent collective/geometric information; no background metric is accepted as fundamental input.

### Dynamics concept
Search for encoding/composition rules fixed by consistency and local recoverability, then test whether geometry and gravitational dynamics emerge from the same code structure.

### Candidate rigidity mechanism
`isometry + recoverability + compositional consistency + symmetry/minimality`.

### Main risk
Error-correcting structure may explain robustness/emergence of geometry while failing to derive Lorentzian causal dynamics and Einstein evolution. It may also smuggle a graph/boundary geometry into the code architecture.

### Prospective cheap kill tests
E1. **Background-independence test:** verify that dimensional/adjacency structure is derived rather than hard-coded in the encoder.
E2. **Causal test:** determine whether a physical causal relation follows from code/channel structure without an external time ordering.
E3. **GR-content test:** identify any mechanism capable of generating dynamical curvature equations rather than only kinematic area/entropy relations.

### Preliminary score
- O=4
- C=4
- K=2
- F=4
- G=3
- L=1
- S=2
- R=4
- Q=4
- E=3
- **Total = 31/40**

Status: `PARTIAL / HIGHEST_RAW_SCORE_BUT_FATAL_GR_RISK`

---

## Matrix summary

| Branch | Core strength | Dominant risk | Score | Current status |
|---|---|---|---:|---|
| A — CCRC | direct causal/compositional reconstruction and high falsifiability | may reproduce known amplitude freedom | 30/40 | PARTIAL / high priority |
| B — CQCG | quantum/compositional consistency and low-level rigidity | weak Lorentzian-GR mechanism | 30/40 | PARTIAL |
| C — PCMH | strongest explicit same-realization/refinement logic | measure family may remain huge | 30/40 | PARTIAL / high priority |
| D — LCSD | direct geometry reconstruction | Lorentzian composition and arbitrary spectral functional | 29/40 | PARTIAL |
| E — RQEC | strong finite quantum consistency/rigidity | gravity dynamics may not emerge | 31/40 | PARTIAL |

## Decision

`NO_PROMOTION_YET`.

The highest raw score (E) is **not** declared the winner because its weakest dimension is precisely the required Lorentzian/GR route. Score maximization cannot override a fatal scientific risk.

The next efficient move is to execute a first cheap-kill round on **A, C, and E** because together they test three different rigidity mechanisms:

- A: closure-generated amplitudes;
- C: projective measure consistency;
- E: isometric/recoverability constraints.

B and D remain live comparison controls but are not first in the kill-test queue.

## Iter002 progress accounting

Completed:
- architecture generation;
- common scoring rubric;
- preliminary scoring;
- prospective kill-test declaration;
- no-promotion decision.

Not completed:
- explicit toy constructions;
- algebraic kill tests;
- freedom-count calculations;
- any physical ansatz promotion.

Therefore current task completion is set to **45%**, while canonical candidate-program readiness remains **24%** until a branch clears the pre-ansatz gate.

## Exact next gate

`QGR-G0-KILL-ROUND-1`:

1. Build the minimal nontrivial A/CCRC complex and test composition + coefficient closure.
2. Build a two-resolution C/PCMH toy history system and solve its exact pushforward consistency equations.
3. Build a minimal E/RQEC relational encoder and test whether adjacency/causal structure is derived or merely inserted.

Reject a branch early if a fatal gate is triggered. Do not rescue it by adding new arbitrary functions after the test outcome.
