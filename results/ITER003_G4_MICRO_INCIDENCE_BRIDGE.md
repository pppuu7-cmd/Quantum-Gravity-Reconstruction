# QGR Iter003-G4 — Microscopic Pair-Incidence Bridge

Date: 2026-09-11
Status: `PASS_SCOPED_MICROSCOPIC_LORENTZ_STRUCTURE / INCIDENCE_TO_HESSIAN_MAP_OPEN`

## Question

Can the Lorentzian structure found in G2-G3 be traced back to exact finite `B_4` incidence data rather than being introduced only as a null-link compatibility condition? And what is the lowest directional order capable of carrying nontrivial TT-like propagation?

## Exact rank-2 incidence result

The rank-2 events of the Boolean causal cell `B_d` are exactly the unordered pairs of **distinct** generators.

Therefore the canonical equal-weight pair-incidence matrix on generator space is, up to a common scale/sign,

`C_d = J - I`.

There are no diagonal self-pair entries because repeated-generator rank-2 events `{i,i}` do not exist in `B_d`.

The spectrum is exact:

- on the fully symmetric direction: eigenvalue `d-1`;
- on the `(d-1)`-dimensional sum-zero subspace: eigenvalue `-1`.

Hence for every `d>1`, the pair-incidence form is nondegenerate and has one sign opposite to the other `d-1` signs.

For `d=4`:

`spec(C_4) = (3,-1,-1,-1)`.

Thus the raw microscopic rank-2 incidence structure already carries a `(1,3)` Lorentzian signature up to overall sign convention.

This sharpens G2: the zero diagonal / null-generator structure need not be added independently if the emergent local bilinear form is reconstructed directly from rank-2 pair incidence.

## Exact inverse and match to G3

For general `d`,

`(J-I)^{-1} = -I + J/(d-1)`.

For `d=4`,

`C_4^{-1} = -I + J/3`.

Up to overall sign, this is exactly the G3 unique hyperbolic principal tensor

`G = I - J/3`.

Therefore the relative coefficient ratio `-1/3` in G3 is already encoded algebraically by the inverse of the microscopic Boolean pair-incidence form.

## First-order propagation obstruction

To test whether a lower-order microscopic update could already generate directional TT propagation, consider the most general first-order rule

`q' = sum_i T_i q_i`,

where each `q_i` is a two-component TT-like field contribution associated with one of the four generator directions and each `T_i` is an arbitrary real `2x2` matrix.

Impose exact `S_4` covariance using the G2 two-dimensional irrep.

There are initially `4 x 4 = 16` real matrix coefficients. The exact equivariance system has rank `15`, leaving a one-dimensional solution space.

The only surviving structure is

`T_0 = T_1 = T_2 = T_3 = lambda I_2`.

So a first-order direction-resolved local update can only use the fully symmetric direction sum. It cannot carry an independent spatial tensor structure or distinguish a Lorentzian light-cone geometry.

This provides a structural reason that **second directional order is the minimal nontrivial order** for a Lorentzian TT-like kinetic seed under the current symmetry assumptions.

## Scientific synthesis

Three pieces now line up without tuning a relative continuum coefficient:

1. `B_4` rank profile derives four relational directions.
2. rank-2 distinct-pair incidence gives `C_4=J-I` with Lorentzian `(1,3)` signature.
3. the inverse pair form gives `C_4^{-1}=-I+J/3`, equal up to sign to the unique G3 hyperbolic principal tensor.

This is substantially stronger than merely observing that an `S_4` matrix *can* be chosen with Lorentzian signature.

## Critical blocker

What is **not** yet derived is the physical map

`microscopic pair-incidence C  ->  linearized kinetic Hessian proportional to C^{-1}`.

The algebraic inverse relation is exact, but QGR does not yet have a microscopic amplitude/action/refinement theorem forcing the Hessian or propagator to be that inverse object.

Until this bridge is supplied, the G3 wave operator remains a highly constrained candidate linearized dynamics rather than a derived consequence of CCRC.

## Classification

`PASS_SCOPED_BOOLEAN_RANK2_DISTINCT_PAIR_INCIDENCE_HAS_CANONICAL_LORENTZ_SIGNATURE_AND_INVERSE_MATCHES_G3_PRINCIPAL_TENSOR__FIRST_ORDER_EQUIVARIANT_TT_PROPAGATION_IS_DIRECTIONALLY_TRIVIAL__INCIDENCE_TO_PHYSICAL_HESSIAN_MAP_UNPROVEN`

## Exact next gate

`QGR-ITER003-G5-AMPLITUDE-HESSIAN-CLOSURE`

Define the smallest local quantum amplitude or stationary/composition functional built from the existing CCRC projector, Boolean pair-incidence data, and exact normalization rules **before** looking at the Hessian result. Then compute its quadratic fluctuation operator.

Pass condition: the TT-sector Hessian is forced to be proportional to `C_4^{-1}` (or an equivalent operator with the same characteristic cone) with no new relative coefficient.

Fail/block condition: an arbitrary function or free Hessian ratio remains, or the desired inverse pair form must be inserted explicitly after the calculation.

Reproducibility: `code/qgr_iter003_g4_micro_incidence.py`.
