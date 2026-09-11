# QGR Iter003-G3 — Discrete Hyperbolic Kinetic Seed

Date: 2026-09-11
Status: `PASS_SCOPED_LINEARIZED_HYPERBOLIC_SEED / MICROSCOPIC_DERIVATION_OPEN`

## Question

Given the exact two-dimensional TT-like `S_4` sector found in G2, can the repeated `B_4` causal-cell construction support a local hyperbolic linearized propagation operator without fitting independent kinetic coefficients to the desired continuum answer?

## Assumptions frozen for this gate

The gate does **not** assume Einstein equations or a continuum background metric. It uses only:

1. repeated identical `B_4` cells;
2. locality at one-cell finite-difference order;
3. linearization around the symmetric seed;
4. a quadratic/second-order principal update, as the minimal nontrivial linearized kinetic order;
5. exact `S_4` covariance among the four causal generator directions;
6. the G2 requirement that the four elementary causal cover directions lie on the characteristic/null cone of the emergent propagation geometry;
7. the G2 result that the two-dimensional internal TT-like representation has one-dimensional commutant.

The microscopic origin of assumption 4 is **not yet derived** and remains the main blocker after this gate.

## Most general directional principal tensor

For four equivalent generator directions, every real symmetric `S_4`-invariant principal tensor is

`G^{ij} = A delta^{ij} + B`.

Thus the directional kinetic sector has two coefficients before constraints.

The inverse is

`(G^{-1})_ij = (1/A) delta_ij - B/[A(A+4B)]`.

The diagonal entries are

`(A+3B)/[A(A+4B)]`.

If the four elementary causal cover directions `e_i` are null tangent directions of the inverse propagation metric, then

`(G^{-1})_ii = 0`,

which gives the exact condition

`A + 3B = 0`.

Therefore

`B/A = -1/3`.

After removing the overall field/action normalization, there is no relative kinetic coefficient left.

A convenient normalization is

`G = I - J/3`.

Its inverse is

`g = I - J`,

exactly the conditional Lorentzian form obtained independently in G2.

## Hyperbolicity

On the symmetric direction `(1,1,1,1)`, `G` has eigenvalue `-1/3`.

On the three-dimensional sum-zero subspace, it has eigenvalue `+1`.

Hence the principal signature is

`(-,+,+,+)`.

Writing momentum as an orthogonal decomposition

`p = p_0 u_0 + p_perp`,

with `u_0=(1,1,1,1)/2`, the continuum principal polynomial is

`K(p) = -(1/3) p_0^2 + |p_perp|^2`.

So the characteristic equation `K(p)=0` is a nonempty Lorentzian cone. A rescaling of the time coordinate removes the harmless factor `1/3`.

## Exact discrete realization

On the repeated cell lattice, let `D_i^+` and `D_i^-` denote forward and backward finite differences along generator direction `i`. The minimal real quadratic lattice operator associated with the fixed principal tensor is

`L = sum_{ij} G^{ij} D_i^- D_j^+`.

This is an exactly `S_4`-invariant finite-difference operator. Its long-wavelength principal symbol is the Lorentzian form above.

No d'Alembertian coefficient ratio is imported from continuum GR: the ratio is fixed by `S_4` covariance plus the null-cover condition on the inverse propagation geometry.

## Two-component degeneracy

From G2, the exact commutant of the two-dimensional TT-like `S_4` representation is one-dimensional. Therefore any `S_4`-equivariant kinetic operator acts on the two internal components proportionally to the identity.

Consequently the two TT-like components receive the same principal operator and no extra polarization-dependent coefficient is available at this level.

## Parameter count

Before constraints:

- directional principal coefficients: `A,B`;
- internal 2x2 coefficient freedom compatible with `S_4`: one scalar multiplier.

After null-cone compatibility and removal of overall normalization:

- relative directional kinetic freedom: `0`;
- polarization splitting freedom: `0`;
- physically irrelevant common normalization: `1`.

This is a strong rigidity result for the linearized seed.

## Classification

`PASS_SCOPED_S4_COVARIANT_NULL_LINK_CONDITION_FIXES_UNIQUE_LORENTZIAN_HYPERBOLIC_PRINCIPAL_TENSOR_UP_TO_SCALE_AND_DEGENERATE_2D_TT_LIKE_PROPAGATION__NONLINEAR_GR_AND_MICROSCOPIC_KINETIC_ORIGIN_UNPROVEN`

## Critical scope guard

This is **not yet a derivation of a graviton or GR**.

Not established:

- why the microscopic CCRC amplitude/refinement law must generate a quadratic second-order kinetic term;
- continuum limit existence;
- local Lorentz group rather than only an `S_4` seed approaching it;
- gauge/diffeomorphism redundancy;
- masslessness protected beyond the linear principal symbol;
- nonlinear self-coupling;
- Einstein equations;
- universal matter coupling/equivalence principle;
- normalized operational observables.

## Strongest blocker after G3

The relative hyperbolic operator is fixed once a second-order local kinetic principle is accepted, but **that kinetic principle itself has not yet been derived from the finite CCRC composition law**.

Therefore the next gate is not to tune dispersion further. It is to derive, or fail to derive, the quadratic update from microscopic cell amplitudes/refinement.

## Exact next gate

`QGR-ITER003-G4-MICROSCOPIC-TO-KINETIC-DERIVATION`

Construct the smallest repeated-cell amplitude/refinement rule extending the existing projector/path-normalization structure. Linearize it around the symmetric `B_4` state and determine whether its Hessian/principal update is forced to be proportional to `I-J/3` without inserting that matrix by hand.

If the microscopic rule leaves an arbitrary Hessian ratio or requires choosing the Lorentzian tensor after seeing the target, record `BLOCKED` or `FAIL_SCOPED` rather than promoting the model.

Reproducibility: `code/qgr_iter003_g3_hyperbolic_operator.py`.
