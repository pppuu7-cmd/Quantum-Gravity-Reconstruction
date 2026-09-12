# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter009`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / INTERACTING_QUANTUM_MEASURE_AND_RADIATIVE_STABILITY`
Active roadmap stage: `R10 interacting quantum completion / leading history-loss c6 order and strong refinement control`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **91%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **100%**
- Iter008 completion: **100%**
- Iter009 completion: **85%**
- Theory established: **0%**
- Active candidate: `QGR-L1`
- Finite-depth history instrument: **PASS_SCOPED**
- Naive global normalized interacting vacuum weight: **BLOCKED**
- First nonredundant Ricci-flat parity-even local correction: **one Weyl^3 class**
- `c6` fixed: **NO**
- Flat QGR-L1 Hessian dependence on `c6`: **none through second variation**
- Nonzero-Weyl curved Hessian dependence on `c6`: **generic**
- Existing G6H fixed-geometry comparator explicit `c6` dependence: **none**
- Full self-consistent curved leading-loss `c6` dependence: **ACTIVE TEST**
- Infinite-refinement full operator limit: **OPEN**
- Independent KMQGB pass: **NO**

## Iter009 completed gates

G1 run `34662453224` blocked the naive global vacuum weight but preserved the operator route.

G2 run `34663104103` established normalized L2 states and arbitrary finite-depth history-channel normalization, and removed both curvature-squared pure-vacuum bulk directions by an exact rank-2 field-redefinition audit.

G3 run `34663353057` reduced the parity-even Ricci-flat six-derivative bulk sector to one nontrivial `Weyl^3` class and found its coefficient `c6` unfixed.

G4 run `34663799182` proved:

- lower-order QGR data admit an explicit continuous `c6` family;
- `Weyl^3` has zero first and second variations at the exact flat seed;
- nonzero background Weyl curvature generically activates a `c6` quadratic response;
- scalar branch action phases cancel exactly from the traced Kraus channel;
- actual G6H code is a fixed-geometry transport/overlap comparator with no explicit action phase or `c6` input;
- a sufficient uniform operator convergence condition is known but not yet established by the current RMS/scalar data.

Record: `results/ITER009_G4_C6_DECOUPLING_AND_CHANNEL_SCOPE.md`.

## Active gate — G5

`QGR-ITER009-G5-LEADING-HISTORY-LOSS-C6-ORDER-AND-STRONG-REFINEMENT-CONTROL`

Tests:

1. expand branch generators `X_alpha=h^2 A_alpha+c6 h^4 B_alpha+...` and determine the first `c6` order in pairwise mixture loss;
2. test exact purity invariance under common geometry/unitary shifts;
3. test branch-dependent `c6 h^4` corrections and cross-order with the existing `h^2` branch spread;
4. keep absolute coherent observables separate from history-mixture purity;
5. extend the repaired-G9 numerical relative Lorentz-generator scaling toward smaller `h` and test the `h^-2` rescaled spread;
6. use exact packet-overlap formulas to test strong convergence on the specified physical packet domain without claiming full operator-norm convergence.

## Active blocker

`MISSING_ORDER_CLASSIFICATION_OF_SELF_CONSISTENT_C6_EFFECT_ON_HISTORY_MIXTURE_LOSS_AND_STRONG_INFINITE_REFINEMENT_CONTROL_ON_THE_SPECIFIED_PACKET_DOMAIN`

## KMQGB lock

Latest observed head remains `12a28d7b58c082b2f817cf3d0296ea9e11267097`; authoritative recovery remains `NOT_YET_AUTHORIZED`, `new_required_authorized=false`, `D7=NOT_CLOSED`.

## Claim locks

- theory established `0%`;
- no experimental confirmation;
- no microscopic `c6` value;
- no claim all observables are `c6` independent;
- no full-Hilbert operator-norm/infinite-refinement completion;
- no independent KMQGB pass or `NEW_REQUIRED` authorization.
