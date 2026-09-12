# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter009`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / INTERACTING_QUANTUM_MEASURE_AND_RADIATIVE_STABILITY`
Active roadmap stage: `R10 interacting quantum completion / c6 microscopic matching or observable decoupling`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **90%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **100%**
- Iter008 completion: **100%**
- Iter009 completion: **75%**
- Theory established: **0%**
- Active candidate: `QGR-L1`
- All-orders local metric-only two-derivative action: **PASS_SCOPED**
- Finite-depth history instrument: **PASS_SCOPED at arbitrary finite depth under verified branch-lift conditions**
- Naive global normalized interacting vacuum weight: **BLOCKED**
- Pure-vacuum curvature-squared physical bulk directions at first correction order: **0 after rank-2 field-redefinition quotient**
- Ricci-flat parity-even six-derivative bulk dimension: **1**, represented by `Weyl^3`
- `c6` fixed by current QGR microscopic authority: **NO**
- Existing G6H fixed-geometry broadband code path: **does not use branch action phases or c6 explicitly**
- Infinite-refinement operator/channel limit: **OPEN**
- Independent KMQGB pass: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

Readiness is an internal construction-roadmap metric, not probability of correctness and not fraction of quantum gravity solved.

## Iter009 G1-G2

G1 run `34662453224` blocked the naive global vacuum weight because of the infinite scale orbit and unsuppressed flat zero mode. G2 run `34663104103` established normalized `L2` states and arbitrary finite-depth CPTP/isometric history composition, and proved both parity-even curvature-squared pure-vacuum bulk directions EOM-redundant at first correction order.

Records:
- `results/ITER009_G1_MEASURE_AND_RADIATIVE_CENSUS.md`
- `results/ITER009_G2_FINITE_OPERATOR_AND_FIELD_REDEFINITION_CLOSURE.md`

## Iter009 G3 — first physically nonredundant local vacuum class

Run `34663353057`: **6 lanes + aggregate SUCCESS**.

In 4D Ricci-flat vacuum, the parity-even algebraic curvature-cubed sector is one-dimensional. Derivative-curvature six-derivative bulk terms reduce in the scoped vacuum sector by EOM/IBP/Bianchi identities to the same `Weyl^3` class. A Petrov-D-type Weyl block `diag(-2,1,1)` gives nonzero cubic trace.

The local correction has the dimensional form

`S6=a_cont*c6*h^4*integral(Weyl^3)`

and therefore scales relatively as

`c6*Gamma^2*(ell_Q^2 R_eff)^2`.

This is the same formal `O(h^4)` order as the previously constructed history effect. Current repository authority does not fix `c6`.

Classification:
`PARTIAL_SCOPED_ON_SHELL_PARITY_EVEN_PURE_VACUUM_SIX_DERIVATIVE_OPERATOR_SHAPE_COLLAPSES_TO_ONE_WEYL_CUBED_CLASS__ITS_QGR_COEFFICIENT_C6_IS_UNFIXED_AND_COMPETES_AT_THE_SAME_OH4_ORDER_AS_THE_HISTORY_EFFECT`.

Record: `results/ITER009_G3_SIX_DERIVATIVE_PHYSICAL_OPERATOR_CENSUS.md`.

## G6H scope audit before G4

The actual G6H implementation was inspected. `qgr_iter007_g6h_common.py` obtains branch Lorentz maps from `solve_paths(h)` and constructs source momenta, little-group/Wigner rotations and normalized overlaps. `qgr_iter007_g6h_broadband_profile.py` computes the broadband history-mixture purity from those branch transports. Neither file inserts `S_alpha`, an action phase, or `c6`.

Therefore the existing G6H result is a fixed-geometry transport comparator. This does **not** prove a fully self-consistent curved solution is `c6`-independent, because `c6 Weyl^3` can in principle modify the curved branch geometry/equations of motion.

## Active blocker

`MISSING_SAME_REALIZATION_MICROSCOPIC_DERIVATION_OR_OBSERVABLE_DECOUPLING_OF_C6_AND_UNIFORM_INFINITE_REFINEMENT_OPERATOR_CONTROL`

## Active gate — G4

`QGR-ITER009-G4-MICROSCOPIC-C6-MATCHING-OR-OBSERVABLE-DECOUPLING-AND-CHANNEL-CONVERGENCE`

Parallel tests:

1. construct the explicit family `S_lambda=S_EH+lambda*a_cont*h^4*integral(Weyl^3)` and test whether all already frozen lower-order/two-derivative data leave `lambda` free;
2. compute first/second variation of `Weyl^3` about the exact flat seed;
3. compute quadratic activation on a nonzero-Weyl background;
4. prove cancellation of arbitrary scalar branch phases in the traced Kraus channel;
5. freeze the scope of the existing G6H code as fixed-geometry/action-phase-independent, while retaining self-consistent curved dynamics as open;
6. derive a sufficient uniform channel convergence bound and compare it with current evidence.

## KMQGB synchronization

Latest observed KMQGB head: `12a28d7b58c082b2f817cf3d0296ea9e11267097` (`Iter388: add CMB transport scope guard`). Authoritative recovery remains older with `NOT_YET_AUTHORIZED`, `new_required_authorized=false`, `D7=NOT_CLOSED`.

## Claim locks

- theory established remains `0%`;
- no experimental confirmation;
- no microscopic `c6` value claim;
- no claim complete leading `O(h^4)` EFT is one-parameter while self-consistent curved `c6` response is open;
- existing G6H one-parameter claim remains only for its fixed-geometry comparator;
- no global normalized vacuum measure claim;
- no infinite-refinement operator-limit claim;
- no independent KMQGB pass or `NEW_REQUIRED` authorization;
- no claim QGR is unique/correct as a full quantum-gravity theory.
