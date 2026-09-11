# QGR Iter003-G2 — Tetrahedral Lorentz / TT-like Sector Audit

Date: 2026-09-11
Status: `PASS_SCOPED_KINEMATIC_SEED / DYNAMICS_NOT_CLOSED`

## Question

Can the symmetric `B_4` causal seed support a nontrivial tensor-like perturbation sector and a Lorentzian-signature seed without inserting a continuum background metric or Einstein-Hilbert action?

## Exact finite setup

Take the four relational generators of `B_4` and the six unordered generator pairs `(ij)`. Small pair-incidence/gluing perturbations therefore live in a six-dimensional real vector space.

The `S_4` permutation action on the four generators induces the standard action on the six two-element subsets. This six-dimensional representation decomposes exactly as

`6 = 1 + 3 + 2`.

A convenient realization is:

- `1D scalar`: all six pair perturbations equal;
- `3D vector-like`: `x_ij = u_i + u_j` with `sum_i u_i = 0`;
- `2D balanced sector`: `sum_{j != i} x_ij = 0` for every generator `i`.

For the unsigned `K_4` vertex-edge incidence matrix `M`, the balanced sector is exactly `ker(M)`, and `rank(M)=4`, so its dimension is exactly `2`.

An exact basis is

`TT1 = (0, 1, -1, -1, 1, 0)`

`TT2 = (1, 0, -1, -1, 0, 1)`

in edge order `(01,02,03,12,13,23)`.

Reproducibility: `code/qgr_iter003_tetrahedral_lorentz_sector.py`.

## Conditional Lorentzian frame result

The most general `S_4`-invariant symmetric bilinear form on the four-dimensional generator space is

`g = alpha I + beta J`.

This is purely a consequence of generator equivalence under `S_4`.

Now add one explicit candidate causal hypothesis:

> the four elementary equivalent causal generators are null links of the emergent local bilinear form.

Then every diagonal entry must vanish, hence

`alpha + beta = 0`.

Up to one physically irrelevant overall scale,

`g_0 = I - J`.

Its eigenvalues are

`(-3, +1, +1, +1)`

with the negative direction along `(1,1,1,1)` and the three positive directions in the sum-zero subspace. Therefore the null-link hypothesis plus `S_4` equivalence fixes a Lorentzian `(1,3)` signature seed, up to overall sign and scale.

### Scope guard

This is **conditional**. The null-link interpretation is not yet derived from the earlier CCRC axioms. It is a candidate microscopic causal postulate being tested because it is background-metric-free and highly constraining. It must not be retroactively treated as proved.

## Exact TT-like properties of the two-dimensional sector

Embed a pair perturbation `x_ij` as a symmetric `4x4` matrix `H` with zero diagonal and off-diagonal entries `H_ij=x_ij`.

For every vector in the two-dimensional balanced sector:

`H (1,1,1,1)^T = 0`.

Thus it is exactly transverse to the distinguished symmetric direction of `g_0`.

Since

`g_0^{-1} = I - J/3`,

the same balance conditions imply

`Tr(g_0^{-1} H) = 0`.

Hence the sector is exactly background-traceless as well.

So the finite `S_4` seed contains a **two-dimensional transverse-traceless-like sector**.

This dimensionality is suggestive because a 3+1-dimensional massless spin-2 field has two physical helicities after continuum gauge reduction. However, no identification is authorized: finite `S_4` representation dimension is not a graviton theorem.

## Refinement / transfer rigidity

The two-dimensional sector is irreducible under the tested `S_4` action. Direct commutant calculation gives a one-dimensional commutant: every `S_4`-equivariant linear transfer operator on this sector is

`T = lambda I`.

If exact CCRC refinement is additionally idempotent,

`T^2 = T`,

then

`lambda in {0,1}`.

Therefore a nonzero surviving TT-like mode has uniquely

`lambda = 1`,

with no continuous transfer coefficient introduced at this level.

This is a useful rigidity result: symmetry plus exact refinement does not allow an arbitrary propagation multiplier on the two-dimensional sector.

## Path-level witness

Define the first-order response of a maximal `B_4` chain to a pair perturbation as the sum of perturbations on the three adjacent generator pairs in that chain ordering.

For both exact basis vectors `TT1` and `TT2`, over all `24` maximal chains:

- mean response = `0`;
- variance = `2`.

Thus the TT-like perturbation is not identically absent microscopically, while first-order scalar path normalization is unchanged.

## What has and has not been achieved

### Established in scope

- exact `S_4` decomposition `6=1+3+2`;
- exact two-dimensional balanced pair sector;
- conditional derivation of Lorentzian signature from `S_4` equivalence + null elementary links;
- exact transversality of the 2D sector to the symmetric direction;
- exact tracelessness with respect to the conditional Lorentzian background form;
- exact one-parameter equivariant transfer commutant, reduced to `lambda=0 or 1` by idempotent refinement;
- nonzero microscopic path response with zero scalar mean.

### Not established

- that elementary CCRC cover links must be null;
- local Lorentz invariance beyond finite tetrahedral symmetry;
- diffeomorphism/gauge symmetry;
- a hyperbolic wave equation;
- massless dispersion;
- spin-2 representation of the Lorentz/Poincare group;
- Einstein equations;
- equivalence principle;
- continuum limit;
- normalized physical clock/rod observable.

## Classification

`PASS_SCOPED_CONDITIONAL_LORENTZIAN_TETRAHEDRAL_FRAME_AND_2D_TRANSVERSE_TRACELESS_LIKE_SECTOR__NO_GRAVITON_OR_GR_DYNAMICS_CLAIM`

## Main blocker revealed

The exact idempotent transfer law is very rigid but, by itself, gives only `T=I` for a surviving mode. That is persistence, not a derived hyperbolic wave operator.

The next gate must therefore ask whether **multi-cell causal composition generates a second-order/hyperbolic kinetic operator from the same local closure rules**, rather than inserting a continuum d'Alembertian or Einstein-Hilbert term by hand.

## Exact next gate

`QGR-ITER003-G3-DISCRETE-HYPERBOLIC-PROPAGATION`

Construct the smallest multi-cell causal lattice/complex carrying the 2D balanced sector and derive the linearized update solely from CCRC composition, normalization, and local causal constraints. Test whether the resulting characteristic polynomial has a genuine hyperbolic/light-cone structure and whether the two TT-like modes propagate without extra tunable kinetic coefficients.
