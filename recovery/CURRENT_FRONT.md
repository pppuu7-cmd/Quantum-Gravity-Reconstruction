# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `Iter054G / Weyl3 dynamical-treatment selection authority`
Project phase: `MODEL_CONSTRUCTION / WEYL3 DYNAMICAL TREATMENT SELECTION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Complete mixed-order evolution reduction: **not established**.
- Physical exact-vs-order-reduced Weyl3 dynamical treatment: **not selected by current authority**.
- Quantum amplitude/measure transition: **not authorized**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID results are immutable.

## Iter054E — TERMINAL SCOPED PASS

Classification: **`PASS_SCOPED_ITER054E_EINSTEIN_WEYL3_MIXED_ORDER_REGIME_SEPARATION_STRONG_HYPERBOLICITY_NOT_AUTHORIZED`**.

Authoritative retry run `34817023061`; aggregate job `103889834227`; summary artifact `10336742062`; digest `sha256:b7e0dce1e44b44ac1b9425427db3d33bdf88271f8ab42762f006a4155eb36bc9`.

Within the frozen exact proxy `P=z+eps*lambda*z^2`, the GR-connected root `z=0` and singular root `z=-1/(eps*lambda)` are exact. This does not assign physical branch weights or establish strong hyperbolicity/spectrum.

## Iter054F — TERMINAL BLOCKED after control-only exact retry

Gate: `ITER054F-WEYL3-MIXED-ORDER-STRONG-HYPERBOLICITY-OBJECT-DEFINITION-AUDIT`.

Provenance:

- preregistration `f4838c50ded00c6d62c9ef822f1f75285eceddf9`
- initial implementation `823b4a24419f5e616eea256b6ba6359fbba30bd4`
- initial workflow head `9b719f0b54030a74a5c166e93db1a2898d90bdfe`
- initial run `34817447178`: **`ITER054F_IMPLEMENTATION_OR_CONTROL_INVALID_A1_CHARPOLY_SYMBOL_IDENTITY`**; permanently historical
- control-only repair `04cc0e065c5eb88385437f233e8f8fc22111332b`
- authoritative exact-retry run `34817585523`
- aggregate job `103892887023`
- summary artifact `10336467977`
- digest `sha256:2ff9d546b8443080fc48c6cf27c2c0b0764b7686b72aff2e53735e7d1bb8a27f`
- terminal classification **`BLOCKED_OBJECT_DEFINITION_ITER054F_MIXED_ORDER_EVOLUTION_REDUCTION_NOT_FIXED`**

All four frozen retry streams A0/A1/B0/B1 were valid. The authority census found all eight required evolution-object fields unresolved/unfixed:

1. state/reduction variables;
2. time direction and spatial covector domain;
3. first-order-in-time or rigorously specified equivalent higher-order formulation;
4. principal evolution matrix/symbol;
5. gauge variables and gauge evolution;
6. constraints and principal constraint propagation;
7. norm/symmetrizer notion and open domain;
8. map to mixed Einstein + symbolic-`c6` Weyl3 equations and GR limit.

A1 also proves exactly that identical real characteristic polynomials can coexist with diagonalizable and defective/Jordan matrices, so a root-only certificate cannot imply strong hyperbolicity.

Durable notes:

- `results/ITER054F_INITIAL_IMPLEMENTATION_INVALID.md`
- `results/ITER054F_TERMINAL_RESULT.md`

This BLOCKED result does **not** show QGR is non-hyperbolic or inconsistent. It shows that the mathematical evolution object is not yet defined sufficiently to make that claim.

## Exact current blocker / Iter054G

Before inventing a preferred evolution reduction, QGR must decide what the later `c6 Weyl^3` term means dynamically.

Two inequivalent admissible-history prescriptions are currently possible:

- exact finite-`c6` higher-derivative dynamics, retaining the complete higher-order solution space and additional initial-data structure;
- perturbative/order-reduced effective dynamics, retaining the branch analytic in the correction within a declared validity domain.

The frozen QGR constitution forbids selecting a hidden branch after observing stability/spectrum outcomes. Existing inspected authority supplies coherent action/composition and a symbolic Weyl3 coefficient but has not yet been shown to derive one of these two dynamical treatments.

Outcome-independent preparation already exists:

- `analysis/POST_ITER054F_EXACT_VS_ORDER_REDUCED_DYNAMICAL_TREATMENT_FORK.md`
- `analysis/WEYL3_DYNAMICAL_TREATMENT_SELECTION_AUTHORITY_AUDIT_PREP.md`
- `analysis/EXACT_VS_PERTURBATIVE_SOLUTION_SPACE_FACTOR_CONTROL.md`
- `analysis/STRONG_HYPERBOLICITY_CONSTRAINT_EXTENSION_NONUNIQUENESS_WITNESS.md`

## Locked next sequence

1. Prospectively preregister `ITER054G-WEYL3-DYNAMICAL-TREATMENT-SELECTION-AUTHORITY` before any terminal treatment verdict.
2. Freeze the pre-existing authority sources; later files may not retroactively provide the selector.
3. Ask whether an already-derived QGR microscopic principle selects exact finite-`c6` dynamics, perturbative/order-reduced dynamics with a derived validity domain, or neither.
4. Include exact controls showing the exact and perturbative solution spaces agree on the GR-connected analytic branch but differ by the non-analytic singular branch.
5. If no selector exists, terminalize a dynamical-treatment `BLOCKED_OBJECT_DEFINITION`; do not choose a treatment post hoc.
6. Only after a treatment is independently fixed may QGR construct its corresponding evolution reduction and then test open-region strong hyperbolicity/symmetrizers.
7. Physical mode/ghost/stability and quantum amplitude/measure remain downstream.
