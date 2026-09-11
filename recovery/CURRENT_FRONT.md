# QGR Current Research Front

Updated: 2026-09-11
Active iteration: `Iter005`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / UNIQUE_CUBIC_SELF_COUPLING_CLOSED`
Active roadmap stage: `R4 nonlinear local closure -> quartic consistency / weak-background causal stability`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **42%**
- Iter004 completion: **100%**
- Iter005 completion: **60%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Candidate state: `LINEARIZED_GAUGE_CLOSED + UNIQUE_CUBIC_NOETHER_SELF_COUPLING / QUARTIC_OPEN`
- Linearized masslessness protected: **YES, scoped**
- Zero-derivative cubic potential sector: **CLOSED / 20 of 20 excluded**
- Two-derivative cubic action space: **317** physical directions
- Cubic Noether physical kernel: **0**
- Unique exact rational cubic self-coupling: **YES, scoped**
- Relational pullback transformation algebra: **CLOSED**
- Quartic two-derivative action space: **1694** physical directions
- Quartic Noether consistency: **OPEN**
- Full all-orders nonlinear theory established: **NO**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Iter004 closed result

The natural unreduced field arena is

`H = Sym^2(W4)`,

built from the same four rank-1 relational directions. QGR-L1 is the uniquely selected linearized derivative-gauge-compatible causal two-mode branch. It forbids all `S4`-invariant onsite quadratic masses and matches the prior incidence cone.

Authoritative record: `iterations/ITERATION_004.md`.

## Iter005 G1A — algebraic cubic sector

`Sym^3(H)` contains exactly **20** `S4` singlets. The derived affine relational-frame gauge shifts span arbitrary constant symmetric field shifts, so all 20 algebraic cubic potential directions are excluded.

Classification:

`PASS_SCOPED_ZERO_DERIVATIVE_CUBIC_SECTOR_EXCLUDED`.

## Iter005 G1B — nonlinear frame transformation

Because `H` is the second moment of the rank-1 relational frame, finite local frame relabeling acts by pullback. Expanding this rule fixes

`delta_0 h_ij = D_i xi_j + D_j xi_i`

and

`delta_1 h_ij = xi^k D_k h_ij + h_kj D_i xi^k + h_ik D_j xi^k`.

The transformations obey exactly

`[delta_xi,delta_eta]G = delta_[xi,eta]G`.

Classification:

`PASS_SCOPED_RELATIONAL_FRAME_PULLBACK_FIXES_DELTA1_AND_CLOSES_TRANSFORMATION_ALGEBRA`.

## Iter005 G1B — complete cubic Noether result

The complete local bosonic `S4`-invariant total-two-derivative cubic action quotient has exact dimension

`317`.

A raw `h(Dh)(Dh)` `S4` orbit spanning set has 399 directions and kinematic rank 317.

For the fixed relational `delta_1`, the cubic Noether map has rank **317** on the physical quotient. Therefore

`ker N / kinematic_nulls = 0`.

The inhomogeneous system

`delta_0 S3 + delta_1 S2 = 0`

has an exact rational solution. In the deterministic 399-orbit raw basis it has 75 nonzero coefficients with denominators only `1,2,4,8`.

The full identity was expanded coefficient-by-coefficient in independent fields, gauge components, and momenta. The exact sparse polynomial residual is identically zero.

Therefore the physical two-derivative cubic self-coupling is unique modulo kinematic/IBP null directions.

Classification:

`PASS_SCOPED_EXACT_RATIONAL_CUBIC_NOETHER_SOLUTION_UNIQUE_MODULO_KINEMATIC_NULLS`.

Authoritative records:

- `results/ITER005_G1B_FRAME_PULLBACK_ALGEBRA.md`
- `results/ITER005_G1B_TWO_DERIVATIVE_CUBIC_COUNT.md`
- `results/ITER005_G1B_CUBIC_NOETHER_CLOSURE.md`

Reproducibility:

- `code/qgr_iter005_g1b_frame_pullback_algebra.py`
- `code/qgr_iter005_g1b_two_derivative_cubic_count.py`
- `code/qgr_iter005_g1b_noether_rank.py`
- `code/qgr_iter005_g1b_exact_noether_certificate.py`

## External sanity check

Known consistent-deformation results for a single local massless spin-2 field with at most two derivatives select the Einstein-Hilbert deformation. This agrees with the internal QGR result but was not used to select or solve the QGR cubic vertex.

No all-orders GR claim is promoted from the external agreement.

## Iter005 G2 — quartic front

The complete local bosonic `S4`-invariant quartic action quotient with total derivative degree two has exact dimension

`1694`.

The next Noether equation is therefore a precisely defined but substantially larger problem:

`delta_0 S4 + delta_1 S3 = 0`.

Both the source (`delta_1 S3`) and the linear operator (`delta_0`) are already fixed. The open questions are existence and uniqueness of `S4` modulo quartic kinematic null directions.

Record:

- `results/ITER005_G2_QUARTIC_KINEMATIC_COUNT.md`
- `code/qgr_iter005_g2_quartic_two_derivative_count.py`

## Active blocker

`BLOCKED_MISSING_QUARTIC_NOETHER_EXISTENCE_UNIQUENESS_CERTIFICATE_AND_WEAK_BACKGROUND_CHARACTERISTIC_CONE_AUDIT_FOR_QGR_L1`.

## Active gate — Iter005 G2/G3

1. Build a computationally tractable basis/quotient for the 1694-dimensional quartic action space.
2. Solve `delta_0 S4 = -delta_1 S3` without importing an Einstein-Hilbert quartic term.
3. Determine the homogeneous physical quartic kernel dimension.
4. If a quartic solution exists, linearize the interacting equations on weak nonzero backgrounds.
5. Track characteristic rank/cone and physical-mode count.
6. Reject post-hoc repairs that alter the quadratic incidence cone solely to force closure.

## Subsequent gate

Only after local quartic/background closure survives should same-realization refinement/coarse-graining begin.

## KMQGB synchronization

Last inspected KMQGB head: `f503c39177012879a80bf767282a15d0c441e2f9` (Iter324-325 merge). Global D7 remains unauthorized in the inspected snapshot.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_005.md`
4. `results/ITER005_G1B_CUBIC_NOETHER_CLOSURE.md`
5. `results/ITER005_G2_QUARTIC_KINEMATIC_COUNT.md`
6. `iterations/ITERATION_004.md`
7. `results/ITER004_G6_SELECT_L1.md`
8. `docs/CONSTITUTION.md`
9. newest Iter005 results/code
10. current KMQGB front and recent commits
