# QGR Current Research Front

Updated: 2026-09-11
Active iteration: `Iter006`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / LOCAL_NONLINEAR_THROUGH_QUARTIC / QUANTUM_COMPOSITION_SEARCH`
Active roadmap stage: `R5 — state/measure/composition and same-realization refinement`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **49%**
- Iter005 completion: **100%**
- Iter006 completion: **20%**
- Lead architecture: `A / CCRC`
- Active local candidate: `QGR-L1`
- Local candidate state: `LINEARIZED_GAUGE_CLOSED + UNIQUE_CUBIC + UNIQUE_QUARTIC + WEAK_BACKGROUND_CAUSAL_STABLE`
- Quartic Noether existence: **PASS_SCOPED exact**
- Quartic homogeneous physical kernel: **0**
- Weak-background local characteristic stability: **PASS_SCOPED**
- Full all-orders nonlinear theory established: **NO**
- Physical Hilbert/state-space completion: **NO**
- Dynamic same-realization coarse-graining: **BLOCKED pending measure/composition object**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Iter005 closed result

### Cubic

The local two-derivative cubic action quotient has dimension 317. The fixed relational pullback `delta_1` gives a full-rank cubic Noether map and a unique exact rational cubic self-coupling modulo kinematic nulls.

### Quartic existence

The physical quartic action quotient has dimension 1694. A quartic coefficient generated from the same second-moment/pullback connection-density reproduces the already fixed QGR quadratic and cubic vertices with one common overall normalization.

Exact coefficient expansion gives

`delta_0 S4 + delta_1 S3 == 0`

with 259,596 nonzero rational coefficients on each side and **0** nonzero residual coefficients.

### Quartic uniqueness

The affine subgroup of `delta_0` yields a sparse necessary homogeneous-invariance map on the 2066 raw quartic `S4` orbits. Its modular rank is exactly **1694** mod `p=1000003`.

Because the physical quartic quotient dimension is exactly 1694, the rational physical homogeneous quartic kernel is zero.

Thus `S4` is unique modulo the 372 kinematic/IBP null directions.

### Weak-background causal stability

For `G_down=E+hbar`, the local characteristic form is

`K_hbar(k)=k_i G_up^{ij} k_j`,

with

`G_up=C-C hbar C+C hbar C hbar C+...`.

Exact rational tests on nontrivial frame-deformed backgrounds give Hessian rank 4 on the deformed null cone, rank 6 off cone, gauge rank 4, and exactly two physical null modes on cone.

### Refinement handoff

A coherent kinematic `B4` tower exists with exact normalization `24^n * 24^-n = 1`. Deterministic frame maps act functorially on `Sym^2(W4)`.

Generic dynamic coarse-graining is nevertheless ambiguous: a marginal mixture second moment and the second moment of a composed mean frame differ by fine-frame covariance/cross-correlation data. QGR may not choose between them without a primitive state/measure/composition object.

Authoritative record: `iterations/ITERATION_005.md`.

## Iter006 G1 — primitive composition search

Four classes were separated: classical history probabilities, direct complex path amplitudes, history-register isometry/CP channels, and unrestricted quantum measures.

Current lead is the history-register isometry / CP-channel architecture.

For 24 symmetry-equivalent branches and a candidate orthogonal physical projector `P`, take

`K_alpha=a P`.

Isometry on the `P` subspace fixes

`|a|=1/sqrt(24)`.

After tracing the history register,

`E(rho)=sum K_alpha rho K_alpha^dagger=P rho P`,

so each history carries coarse channel weight `1/24`. At `n` levels the branch count is `24^n`, branch amplitude magnitude is `24^(-n/2)`, and normalization remains exact.

Classification:

`PASS_SCOPED_CHANNEL_LEVEL_REFINEMENT_NORMALIZATION_CANDIDATE`.

Critical guard: the old CCRC projector was a toy label-space projector, not yet the physical QGR projector.

## Active blocker

`BLOCKED_MISSING_PHYSICAL_QGR_STATE_SPACE_REFINEMENT_PROJECTOR_AND_OBSERVABLE_ALGEBRA_LINKING_THE_HISTORY_CHANNEL_TO_THE_SAME_QGR_L1_SECOND_MOMENT_RESPONSE`.

## Active gate — Iter006-G2

`QGR-ITER006-G2-STATE_SPACE_AND_PROJECTOR_RECONSTRUCTION`

1. Construct the smallest state-space realization carrying four rank-1 relational directions and ten second-moment response components.
2. Derive the refinement/constraint projector rather than importing the early toy `P`.
3. Determine whether that projector is unique up to unitary equivalence.
4. Define the coarse observable algebra and whether history labels are retained or traced.
5. Show that the same object produces QGR-L1 response dynamics before attempting a continuum/RG claim.

## KMQGB synchronization

Latest observed repository head: `e806bea830402b03e9c8c9ddcbfda3224d06178e` (Iter333 cross-face transport CI).

Iter333 scoped result reduces 15 labeled K3/K4 lower strata to two `S5` normalization orbits but explicitly does not supply the missing jet values or source-defined glue. LQG remains partial/blocked and D7 remains unauthorized. The published recovery front itself is still synchronized only through Iter304, so newer commits are treated as scoped deltas, not a replacement global decision.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_006.md`
4. `results/ITER006_G1_CHANNEL_COMPOSITION_CANDIDATE.md`
5. `iterations/ITERATION_005.md`
6. `results/ITER005_G2_EXACT_QUARTIC_NOETHER_CLOSURE.md`
7. `results/ITER005_G2_QUARTIC_UNIQUENESS_AFFINE_RANK.md`
8. `results/ITER005_G3_WEAK_BACKGROUND_CAUSAL_STABILITY.md`
9. `results/ITER005_G4_REFINEMENT_HANDOFF.md`
10. `docs/CONSTITUTION.md`
11. newest Iter006 results/code
12. current KMQGB scoped deltas + authoritative benchmark front
