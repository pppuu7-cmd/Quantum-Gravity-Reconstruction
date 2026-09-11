# QGR Iteration 005 — Nonlinear Constraint and Self-Coupling Closure

Date: 2026-09-11
Status: `ACTIVE / UNIQUE_CUBIC_NOETHER_SELF_COUPLING_CLOSED / QUARTIC_AND_BACKGROUND_TESTS_OPEN`
Current task completion: **55%**
Candidate-program readiness: **42%**
Active candidate: **QGR-L1**

## Starting authority

Iter004 closed the linearized mass/gauge blocker. QGR-L1 is a ten-component second-moment response field on

`Sym^2(W4)`

with a uniquely selected local derivative-gauge-compatible quadratic Hessian, incidence characteristic cone, exactly two physical null modes on that cone, and no allowed `S4`-invariant onsite quadratic mass deformation.

This iteration does **not** assume a nonlinear GR completion.

## Objective

Determine whether the same relational/incidence/composition structure can generate a nonlinear completion of QGR-L1 with a closed constraint algebra and low-dimensional self-coupling freedom.

## Fixed anti-overfitting rules

Forbidden shortcuts:

- insert Einstein-Hilbert because it is known to self-couple consistently;
- import the full nonlinear diffeomorphism transformation law as an axiom;
- add arbitrary functions/counterterms after a failed closure equation;
- change the QGR-L1 quadratic kinetic cone solely to make cubic closure work;
- use a different microscopic realization for the nonlinear and linear sectors.

Any later match to GR is allowed only as an a posteriori comparison after QGR-internal selection.

## G1A — zero-derivative cubic potential census

The exact `S4` invariant count gives **20** algebraic cubic invariants on `H=Sym^2(W4)` before gauge constraints.

For constant `h` and affine relational-frame gauge parameters, the derived linear gauge law spans arbitrary constant symmetric shifts of all ten components. Since the quadratic action is derivative-only, no algebraic cubic variation can be cancelled.

Therefore all `20/20` zero-derivative cubic potential directions are excluded.

Classification:

`PASS_SCOPED_ZERO_DERIVATIVE_CUBIC_SECTOR_EXCLUDED`.

Records:

- `results/ITER005_G1A_CUBIC_POTENTIAL_CENSUS.md`
- `code/qgr_iter005_g1a_cubic_potential_census.py`

## G1B-1 — nonlinear gauge correction from relational frame pullback

The active field is a second-moment object of the existing rank-1 relational frame:

`G in Sym^2(W4)`.

A local change of relational frame therefore acts by pullback on `G`. Expanding

`G=G0+kappa h`

gives the already selected linear law

`delta_0 h_ij = D_i xi_j + D_j xi_i`

and fixes the first nonlinear correction

`delta_1 h_ij = xi^k D_k h_ij + h_kj D_i xi^k + h_ik D_j xi^k`.

No independent tensor coefficients are left once `h` remains the same second-moment object under frame composition.

The pullback transformations satisfy exactly

`[delta_xi,delta_eta]G = delta_[xi,eta]G`.

This was verified by exact rational polynomial algebra on nontrivial polynomial fields and parameters.

Classification:

`PASS_SCOPED_RELATIONAL_FRAME_PULLBACK_FIXES_DELTA1_AND_CLOSES_TRANSFORMATION_ALGEBRA`.

Records:

- `results/ITER005_G1B_FRAME_PULLBACK_ALGEBRA.md`
- `code/qgr_iter005_g1b_frame_pullback_algebra.py`

## G1B-2 — complete two-derivative cubic action space

After Bose symmetry and momentum conservation / integration-by-parts quotient, the complete local `S4`-invariant total-two-derivative cubic vertex space has exact dimension

`317`.

A raw `h(Dh)(Dh)` orbit spanning set has 399 `S4` orbits and kinematic evaluation rank 317.

Classification:

`PASS_SCOPED_COMPLETE_KINEMATIC_TWO_DERIVATIVE_CUBIC_VERTEX_COUNT_317`.

Records:

- `results/ITER005_G1B_TWO_DERIVATIVE_CUBIC_COUNT.md`
- `code/qgr_iter005_g1b_two_derivative_cubic_count.py`

## G1B-3 — exact cubic Noether solve

For the already fixed `delta_1`, define the cubic Noether equation

`delta_0 S3 + delta_1 S2 = 0`.

### Uniqueness

The Noether map on the raw 399-orbit spanning set has modular rank **317**. Because the physical cubic action quotient has exact dimension 317, this proves that the rational Noether map has full physical rank and that the homogeneous physical kernel vanishes:

`ker N / kinematic_nulls = 0`.

Thus for fixed relational `delta_1` there is at most one physical two-derivative cubic self-coupling.

### Existence

The inhomogeneous system is consistent. An exact rational solution was reconstructed with

- 75 nonzero raw orbit coefficients;
- denominators only `1,2,4,8`.

The full momentum-space identity was expanded coefficient-by-coefficient in independent field, gauge, and momentum variables. The exact sparse polynomial residual contains zero nonvanishing coefficients:

`delta_0 S3 + delta_1 S2 == 0`.

Therefore the cubic self-coupling exists and is unique modulo kinematic/IBP-null directions.

Classification:

`PASS_SCOPED_EXACT_RATIONAL_CUBIC_NOETHER_SOLUTION_UNIQUE_MODULO_KINEMATIC_NULLS`.

Records:

- `results/ITER005_G1B_CUBIC_NOETHER_CLOSURE.md`
- `code/qgr_iter005_g1b_noether_rank.py`
- `code/qgr_iter005_g1b_exact_noether_certificate.py`

## External sanity check — not an input

Classical deformation analyses of a single massless spin-2 field under locality and at-most-two-derivative assumptions are known to select the Einstein-Hilbert deformation. This is consistent with the QGR result but was not used in the internal selection or solve.

No all-orders GR claim is promoted from this comparison.

## What Iter005 has established so far

In scope QGR-L1 now has:

1. structurally protected linear masslessness;
2. exact two physical modes on the incidence cone;
3. a nonlinear gauge correction derived from the second-moment frame ontology;
4. exact closure of the transformation algebra;
5. exclusion of all algebraic cubic potentials;
6. a unique local two-derivative cubic self-coupling satisfying the exact Noether equation.

## Active gate — G2/G3

`QGR-ITER005-G2_G3-QUARTIC_CONSISTENCY_AND_WEAK_BACKGROUND_CAUSAL_STABILITY`

1. Construct the quartic Noether equation generated by the already fixed pullback transformation and unique cubic vertex.
2. Determine whether a quartic action exists without adding a new free interaction function.
3. Check whether the deformation closes recursively or a genuine fourth-order obstruction appears.
4. Linearize the interacting equations around weak nonzero relational backgrounds and track the principal characteristic cone.
5. Determine whether the two physical modes remain two and whether the incidence/Lorentz cone is preserved or deforms controllably.
6. Do not insert Einstein-Hilbert as a repair if the quartic equation fails.

## Subsequent gate — same-realization refinement

Only after quartic/local nonlinear consistency survives should QGR begin same-realization refinement/coarse-graining. Do not splice a separate continuum theory into the IR.

## Claim locks

Until the quartic/background/refinement gates close:

- QGR is not yet an all-orders nonlinear gravity theory;
- Einstein equations are not yet internally derived;
- equivalence principle is not yet derived;
- continuum/refinement limit is not proved;
- quantum interacting measure is not defined;
- KMQGB `NEW_REQUIRED` remains unauthorized.

## Progress accounting

- Iter005 completion: **55%**.
- Candidate-program readiness: **42%**.
- These are construction-roadmap metrics, not probabilities of correctness.
