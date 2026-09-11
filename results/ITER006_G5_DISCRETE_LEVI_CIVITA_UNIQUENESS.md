# QGR Iter006-G5 — local discrete Levi-Civita / torsion-free holonomy uniqueness

Date: 2026-09-11
Status: `PASS_SCOPED_LOCAL_NEAR_SEED_DISCRETE_CONNECTION_UNIQUENESS`

## Objective

Determine whether the auxiliary edge holonomies introduced in G4 remain uncontrolled six-parameter freedoms per edge, or whether the existing rank-1 frame data fix them through a discrete torsion-free condition.

## Finite discrete torsion-free equation

At a vertex `v`, let `e_i(v)` be the four rank-1 frame vectors associated with the four relational directions. Let `L_i` transport internal frame vectors from `v` to the neighboring cell `v+i` and satisfy

`L_i in O(C)`.

For every unordered pair `i<j`, require equality of the two elementary plaquette paths when all vectors are compared in the frame at `v`:

`e_i(v) + L_i^(-1) e_j(v+i) = e_j(v) + L_j^(-1) e_i(v+j)`.

This is the finite discrete analogue of vanishing torsion / elementary parallelogram closure.

There are

- `C(4,2)=6` unordered direction pairs;
- four internal components per equation;
- therefore `6*4=24` scalar equations.

The four Lorentz holonomies contain

- `dim O(1,3)=6` infinitesimal parameters each;
- therefore `4*6=24` local connection unknowns.

## Linearization at the symmetric seed

Take the symmetric frame seed

`e_i^a = delta_i^a`

and

`L_i=I`.

Write

`L_i = I - omega_i + O(omega^2)`

with

`omega_i^T C + C omega_i = 0`.

The finite closure equation linearizes to

`Delta_i e_j - Delta_j e_i + omega_i e_j - omega_j e_i = 0`.

The homogeneous connection map is therefore

`{omega_i in o(C), i=0..3} -> {omega_i e_j - omega_j e_i, i<j}`.

Both domain and codomain have dimension 24.

## Exact rank certificate

Using an exact rational basis of the six-dimensional Lie algebra

`o(C)={X | X^T C + C X=0}`,

the 24 torsion equations define a `24 x 24` rational/integer coefficient matrix at the symmetric seed.

Exact result:

- matrix rank: **24**;
- determinant in the recorded rational basis: **11664**;
- determinant is nonzero.

Therefore the homogeneous kernel is zero: no infinitesimal Lorentz connection freedom survives the torsion-free equations at the seed once the neighboring frame first differences are fixed.

Classification:

`PASS_SCOPED_LINEARIZED_DISCRETE_TORSION_MAP_FULL_RANK_24_OF_24`.

## Local finite consequence

Because the finite torsion equations are smooth in the frame variables and Lorentz holonomy coordinates, and the Jacobian with respect to the 24 connection parameters is invertible at the seed, the implicit-function theorem gives a unique local solution

`L_i = L_i[e(v), e(v+i), ...]`

for sufficiently small frame deformations around the symmetric seed, modulo the already identified local internal Lorentz gauge convention.

Thus the G4 edge holonomies do **not** introduce 24 new local physical parameters near the target weak-field/refinement regime.

Classification:

`PASS_SCOPED_LOCAL_FINITE_DISCRETE_LEVI_CIVITA_HOLONOMIES_EXIST_AND_ARE_UNIQUE_NEAR_SYMMETRIC_SEED`.

## Gauge covariance

The finite torsion equations are covariant under

`e(v) -> Lambda_v e(v)`

and

`L_i -> Lambda_(v+i) L_i Lambda_v^(-1)`.

Therefore the locally unique solution transforms as a connection rather than selecting a preferred internal frame.

## What this closes

- the six-dimensional endpoint compatibility ambiguity is identified as connection-fiber data;
- a finite discrete torsion-free equation is specified without interpolation;
- its local connection Jacobian is exactly nonsingular at the QGR seed;
- auxiliary edge Lorentz freedom is locally fixed by existing rank-1 frame data/first differences rather than becoming a new coupling sector.

## What remains open

This is a **local near-seed** theorem. It does not prove:

- global existence/uniqueness for arbitrarily strong curved configurations;
- absence of disconnected finite holonomy branches far from the seed;
- exact equality between a directly coarse-solved connection and the product of fine connections;
- normalized noncompact quantum measure / rigging map;
- all-scale projective consistency.

The next decisive problem is therefore no longer local edge transport but **coarse/fine connection consistency**.

## Exact next gate

`QGR-ITER006-G6-TWO_LEVEL_PROJECTIVE_CONNECTION_CONSISTENCY`

1. Build the smallest curved two-level frame configuration with nonzero loop holonomy.
2. Solve the fine torsion-free `L_e` uniquely near the seed.
3. Coarse the frame data using the already defined history/observable marginal.
4. Independently solve the coarse torsion-free connection.
5. Compare that coarse connection with the ordered product/marginal of the fine transports.
6. Classify any mismatch as a derived curvature/RG correction; do not insert a matching counterterm by hand.

## Reproducibility

`code/qgr_iter006_g5_discrete_torsion_rank.py`.
