# QGR Iteration 003 — 4D Lorentzian/GR Seed Gate

Date: 2026-09-11
Status: `ACTIVE / G2_KINEMATIC_LORENTZ_SEED_PASSED / HYPERBOLIC_DYNAMICS_OPEN`
Current task completion: **60%**
Canonical candidate-program readiness: **24%**
Physical ansatz promoted: **NO**
Lead architecture: **A / CCRC**

## Objective

Test whether the A/CCRC architecture can move beyond a directed chain toward a genuinely branching/recombining causal complex with a derived local dimension notion and then toward a Lorentzian tensor-like sector, while preserving exact rigidity and without inserting a background metric or Einstein-Hilbert action.

## Predeclared fatal rule

Reject A/CCRC in its current reconstruction form if obtaining a 4D Lorentzian/GR regime requires any of the following solely to hit the target:

- inserting a continuum background metric;
- assuming an Einstein-Hilbert action;
- choosing an arbitrary continuum/spectral function after the fact;
- adding gate-specific free coefficients with no generating principle;
- switching to a different realization for the GR limit.

## G1 — Boolean causal cell `B_d`

Define the events of `B_d` as all subsets of a set of `d` independent relational generators. The causal order is set inclusion. Elementary causal links add one generator.

The rank profile is

`N_r = C(d,r)`

with generating polynomial

`R_d(x)=(1+x)^d`.

Thus the combinatorial direction count `d` is recoverable from relational-order data.

For `B_4`:

- event count: `16`;
- rank profile: `(1,4,6,4,1)`;
- maximal causal chains: `4!=24`.

Retaining the CCRC projector `P=I-J/3`, `P^2=P`, every four-step chain has kernel `P^4=P`. Equal-chain symmetry plus exact coarse/refinement consistency requires

`24 w_4 P = P`,

so

`w_4=1/24`.

More generally `w_d=1/d!`.

Classification:

`PASS_SCOPED_DERIVED_COMBINATORIAL_DIMENSION_AND_UNIQUE_PATH_NORMALIZATION`.

Reproducibility: `code/qgr_iter003_boolean_causal_cell.py`.

## G2 — exact `S_4` perturbation decomposition

The four `B_4` relational directions define six unordered direction pairs. Small pair-incidence/gluing perturbations therefore form a six-dimensional representation of `S_4`.

The representation decomposes exactly as

`6 = 1 + 3 + 2`.

A concrete realization is:

- `1D`: scalar/common pair perturbation;
- `3D`: vector-like sector `x_ij=u_i+u_j`, `sum_i u_i=0`;
- `2D`: balanced sector satisfying `sum_{j!=i} x_ij=0` for every `i`.

The two-dimensional sector is exactly the kernel of the unsigned `K_4` vertex-edge incidence matrix. Since that matrix has rank four, the sector dimension is exactly two.

One exact basis in pair order `(01,02,03,12,13,23)` is

`TT1=(0,1,-1,-1,1,0)`

`TT2=(1,0,-1,-1,0,1)`.

Detailed record: `results/ITER003_G2_TETRAHEDRAL_LORENTZ_SECTOR.md`.
Reproducibility: `code/qgr_iter003_tetrahedral_lorentz_sector.py`.

## Conditional Lorentzian seed

The most general symmetric bilinear form on the four generator directions invariant under all `S_4` permutations is

`g=alpha I + beta J`.

G2 tests the explicit candidate causal hypothesis that the four equivalent elementary causal generators are null links of the emergent local bilinear form. Then diagonal entries vanish:

`alpha+beta=0`.

Up to overall scale,

`g_0=I-J`.

Its eigenvalues are

`(-3,+1,+1,+1)`.

Therefore `S_4` equivalence plus the null-cover hypothesis fixes a Lorentzian `(1,3)` signature seed without inserting a continuum background metric.

This result is **conditional**: the null-cover interpretation has not yet been derived from earlier CCRC axioms and is not promoted to a theorem of QGR.

## TT-like property

Embed a pair perturbation as a symmetric `4x4` matrix `H` with zero diagonal and off-diagonal entries `H_ij=x_ij`.

For every vector in the exact 2D balanced sector,

`H (1,1,1,1)^T=0`.

Also, since

`g_0^{-1}=I-J/3`,

one has exactly

`Tr(g_0^{-1}H)=0`.

Thus the two-dimensional finite sector is transverse to the distinguished symmetric direction and traceless relative to the conditional Lorentzian seed.

Classification:

`PASS_SCOPED_CONDITIONAL_LORENTZIAN_TETRAHEDRAL_FRAME_AND_2D_TRANSVERSE_TRACELESS_LIKE_SECTOR__NO_GRAVITON_OR_GR_DYNAMICS_CLAIM`.

The equality of this sector dimension with the two continuum graviton helicities is only suggestive. Finite `S_4` representation dimension is not a Lorentz/Poincare spin-2 theorem.

## Refinement rigidity and blocker

The direct commutant audit of the two-dimensional `S_4` representation shows that every `S_4`-equivariant linear transfer map is

`T=lambda I`.

If exact CCRC refinement remains idempotent,

`T^2=T`,

then

`lambda in {0,1}`.

A surviving nonzero mode therefore has `lambda=1` with no continuous transfer coefficient.

This is strong rigidity but not yet dynamics: `T=I` gives persistence, not a derived hyperbolic wave equation or dispersion law.

A path-response test over all 24 maximal `B_4` chains gives, for each exact TT-like basis vector:

- mean first-order response: `0`;
- variance: `2`.

So the mode is microscopically nonzero while first-order scalar path normalization is unchanged.

## What remains open

Still unproved:

- derivation, rather than assumption, of null elementary links;
- approximate local Lorentz invariance beyond finite tetrahedral symmetry;
- diffeomorphism/gauge redundancy;
- a hyperbolic kinetic operator;
- massless dispersion;
- Lorentz/Poincare spin-2 transformation law;
- Einstein dynamics;
- equivalence principle;
- continuum locality;
- normalized clock/rod observable.

## Exact next gate — Iter003-G3

`QGR-ITER003-G3-DISCRETE-HYPERBOLIC-PROPAGATION`

1. Carry the exact 2D balanced sector on the smallest repeated/multi-cell causal complex.
2. Start from the most general local, linear, `S_4`-covariant quadratic/second-order update compatible with the already derived conditional null frame.
3. Determine whether its principal symbol is fixed, up to physically irrelevant overall scale, by locality + symmetry + null-link structure rather than by fitting a continuum target.
4. Check whether a genuine hyperbolic/light-cone characteristic surface appears.
5. Check whether both TT-like components propagate with the same operator by representation rigidity.
6. Record a blocker instead of inserting a d'Alembertian by hand if the operator is underdetermined.

The gate is passed only as a scoped linearized seed if the relative kinetic structure is fixed prospectively and no new gate-specific function is introduced.
