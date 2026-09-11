# QGR Iteration 005 — Nonlinear Constraint and Self-Coupling Closure

Date: 2026-09-11
Status: `COMPLETE / LOCAL_NONLINEAR_CLOSURE_THROUGH_QUARTIC / R5_HANDOFF_BLOCKER_IDENTIFIED`
Completion: **100%**
Candidate-program readiness after Iter005: **49%**
Active candidate: **QGR-L1**

## Objective

Test whether QGR-L1 can advance from the linearly gauge-closed causal two-mode candidate to a locally interacting theory without importing Einstein-Hilbert as a repair, and identify the exact next blocker before same-realization refinement.

## G1A — zero-derivative cubic sector

`Sym^3(H)` with `H=Sym^2(W4)` contains exactly **20** `S4` singlets. The already derived affine part of

`delta_0 h_ij = D_i xi_j + D_j xi_i`

spans arbitrary constant symmetric shifts, so every local algebraic cubic potential is forbidden.

Result:

`20/20 excluded`.

Classification: `PASS_SCOPED_ZERO_DERIVATIVE_CUBIC_SECTOR_EXCLUDED`.

## G1B — nonlinear frame law and cubic self-coupling

The second-moment relational frame transforms by pullback, fixing

`delta_1 h_ij = xi^k D_k h_ij + h_kj D_i xi^k + h_ik D_j xi^k`.

The transformations close exactly:

`[delta_xi,delta_eta]G = delta_[xi,eta]G`.

The complete local bosonic `S4` two-derivative cubic action quotient has dimension **317**. The cubic Noether map has full physical rank 317, so the homogeneous physical kernel is zero.

The inhomogeneous equation

`delta_0 S3 + delta_1 S2 = 0`

has an exact rational solution with 75 nonzero coefficients in the deterministic 399-orbit raw basis. The exact coefficient-wise residual is zero.

Classification:

`PASS_SCOPED_EXACT_RATIONAL_CUBIC_NOETHER_SOLUTION_UNIQUE_MODULO_KINEMATIC_NULLS`.

## G2 — quartic Noether closure

The complete two-derivative quartic action quotient has dimension **1694**, represented by 2066 raw `S4` orbits with 372 kinematic/IBP null directions.

### Existence

A quartic candidate was generated from the same second-moment response, incidence background, and pullback-covariant local connection-density that reproduces the already independently fixed QGR quadratic and cubic vertices.

Nontrivial lower-order certificate:

- connection-density quadratic term = `-2 S2_QGR`;
- fully symmetrized exact cubic action has 8,808 nonzero rational coefficient entries on each side;
- `S3_connection + 2 S3_QGR = 0` coefficient by coefficient.

With the same normalization the generated quartic vertex has 1,089 nonzero raw orbit coefficients. Exact expansion gives

- `delta_0 S4`: 259,596 nonzero rational coefficients;
- `delta_1 S3`: 259,596 nonzero rational coefficients;
- residual `delta_0 S4 + delta_1 S3`: **0** nonzero coefficients.

Thus quartic existence is exact.

### Uniqueness

Any homogeneous quartic Noether vertex must also be invariant under the affine subgroup of `delta_0`, where one external leg is an arbitrary zero-momentum symmetric shift.

The exact sparse affine-shift map on the 2066 raw quartic orbits has modular rank

`1694 mod p`, with `p=1000003`.

Because the independently known physical quartic quotient dimension is exactly 1694, the rational physical homogeneous kernel is zero.

Therefore `S4` is unique modulo the 372 kinematic/IBP null directions.

Classification:

`PASS_SCOPED_EXACT_QUARTIC_NOETHER_EXISTENCE_AND_UNIQUENESS_MODULO_KINEMATIC_NULLS`.

Records:

- `results/ITER005_G2_EXACT_QUARTIC_NOETHER_CLOSURE.md`
- `results/ITER005_G2_QUARTIC_UNIQUENESS_AFFINE_RANK.md`
- `code/qgr_iter005_g2_exact_quartic_noether_certificate.py`
- `code/qgr_iter005_g2_quartic_affine_rank.py`

## G3 — weak-background characteristic stability

For

`G_down = E + hbar`, `E=C^{-1}`,

the inverse response is

`G_up = C - C hbar C + C hbar C hbar C + O(hbar^3)`.

The principal characteristic form through the order controlled by `S2+S3+S4` is

`K_hbar(k)=k_i G_up^{ij} k_j`.

Exact rational tests on three nontrivial frame-deformed backgrounds show:

- gauge-map rank = 4;
- Hessian rank on `G_up`-null covectors = 4;
- Hessian rank off cone = 6;
- exactly **2** non-gauge physical null modes remain on the cone.

The tests include transformed elementary covers and transformed nontrivial null vectors `(1,1,1,-1)`, `(1,2,3,-11/6)`, `(2,-1,3,-1/4)`.

Classification:

`PASS_SCOPED_LOCAL_WEAK_BACKGROUND_CHARACTERISTIC_STABILITY`.

Records:

- `results/ITER005_G3_WEAK_BACKGROUND_CAUSAL_STABILITY.md`
- `code/qgr_iter005_g3_weak_background_cone.py`

## G4 — same-realization refinement handoff

The original `B4` coherent path normalization extends exactly:

`N_histories(n)=24^n`, `w_history(n)=24^-n`, hence total weight `1`.

Deterministic rank-1 frame maps induce canonical maps on `Sym^2(W4)`, so a same-realization **kinematic** refinement tower exists.

However generic coarse-graining is not yet unique. For fine frames `e_alpha`,

`G_mix = sum w_alpha e_alpha e_alpha^T`

and

`G_comp = (sum w_alpha e_alpha)(sum w_beta e_beta)^T`

differ by the fine-frame covariance. Thus mixture/marginal coarse-graining and coherent/additive frame composition are inequivalent unless an underlying measure/amplitude/composition object specifies which operation is physical and how cross-correlations are retained.

Classification:

`PARTIAL_KINEMATIC_SAME_REALIZATION_TOWER__BLOCKED_DYNAMIC_COARSE_GRAINING_UNTIL_MEASURE_OR_COMPOSITION_OBJECT_IS_DEFINED`.

Records:

- `results/ITER005_G4_REFINEMENT_HANDOFF.md`
- `code/qgr_iter005_g4_refinement_handoff.py`

## Iter005 decision

The local nonlinear bootstrap is closed **through quartic order**, and the local weak-background characteristic structure remains one Lorentzian cone with two physical modes.

The next blocker is no longer local self-coupling. It is the construction of the primitive quantum measure/amplitude/composition object needed to make same-realization refinement unique and testable.

Iter005 therefore closes and hands the project to R5.

## Claim locks retained

This iteration does not establish:

- all-orders nonlinear completion;
- a quantum measure or Hilbert-space completion;
- a continuum/refinement theorem;
- strong-background/global hyperbolicity;
- equivalence principle as an operational matter-coupling theorem;
- normalized experimental observables;
- independent KMQGB passage;
- that KMQGB has authorized `NEW_REQUIRED`.

## Next iteration

`QGR Iter006 — Quantum Measure / Composition and Projective Refinement Reconstruction`.
