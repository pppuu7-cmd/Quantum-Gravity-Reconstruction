# Iter056S terminal result — balanced B4 pair tensor to tidal cubic-shape bridge

Date: 2026-09-14
Gate: `ITER056S-BALANCED-B4-PAIR-TENSOR-TO-TIDAL-CUBIC-SHAPE-HELDOUT-VALIDATION`

Hypothesis-generation note: `e89913217b12ff37cadcf7510d77e954fac55ecb`
Prospective preregistration: `f3e0daf1f164953c382753867ccba80852ec8283`
Exact proof: `6aaf230e310da1c7305a85e164e258d34c9061cf`
Reproducibility implementation: `6c50b61684f3bdb418bb7f1c1a31fb4ae74df8bd`
Reproducibility workflow: `55ecc1699c9bf4a4660df9cdd54b4298afeb976e`
Reproducibility trigger/head: `9e81cf94bdbe69e38a58b1242077ba3c11e61033`
GitHub Actions run: `34896461228` — queued at terminal-proof time; not used as scientific authority.

## Terminal classification

**`PASS_SCOPED_CONDITIONAL_ITER056S_BALANCED_PAIR_SECTOR_HAS_EXACT_TIDAL_CUBIC_SHAPE_BRIDGE`**

The classification is established by a generic exact algebraic proof, not by numerical thresholds or by runner availability. The proof is stronger than the eight frozen held-out lanes because it holds for arbitrary `a,b`.

## Exact result

For the source-owned Iter003-G2 balanced pair sector

`x = a TT1 + b TT2`,

with

`TT1=(0,1,-1,-1,1,0)`,

`TT2=(1,0,-1,-1,0,1)`,

the symmetric pair tensor has the exact fixed eigenbasis

- `t=(1,1,1,1)` with eigenvalue `0`;
- `v_a=(-1,1,-1,1)` with eigenvalue `2a`;
- `v_b=(-1,-1,1,1)` with eigenvalue `2b`;
- `v_c=(1,-1,-1,1)` with eigenvalue `-2(a+b)`.

Therefore on the sum-zero three-dimensional spatial subspace selected by the conditional G2 Lorentzian seed,

`H_sp = diag(2a,2b,-2(a+b))`

in a fixed orthonormal basis.

The spatial tensor is exactly traceless and has exact cubic invariant

`Tr(H_sp^3) = -24 a b (a+b) = 3 det(H_sp)`.

This invariant is unchanged by all 24 S4 generator permutations because they act by conjugation and preserve the symmetric direction.

## Frozen H0 shape

For the preregistered special direction `a=b=3/2`,

`spec(H_sp)=(3,3,-6)=3(1,1,-2)`.

Thus the **exact eigenvalue shape** of the G3/Iter040 H0 weak-static tidal Hessian `diag(1,1,-2)` already occurs inside the source-owned G2 balanced pair sector.

No amplitude identification is made.

## Controls

The generic proof implies every preregistered rational lane and all 24 permutation checks.

The cubic-null lane `a=-b != 0` is nonzero while `Tr(H_sp^3)=0` exactly.

The frozen unbalanced control `H_bad=H+(1/7)(E_01+E_10)` violates `H_bad t=0` exactly, so the result is not a tautology for arbitrary zero-diagonal pair matrices.

The fixed preregistered orthonormal spatial basis has the same trace, quadratic invariant, cubic invariant and determinant because it is related to the exact fixed eigenbasis by a 3D orthogonal transformation inside the invariant sum-zero subspace.

## Scientific meaning

This is the first exact source-owned bridge found in the current sequence that does not require the blocked G15 identification of four event variables with frame scales:

`B4 BALANCED PAIR PERTURBATION`

` -> TRACELESS SYMMETRIC TENSOR ON THE G2 SPATIAL SUBSPACE`

` -> EXACT CUBIC SHAPE INVARIANT`.

It shares the H0 tidal eigenvalue shape used by the continuum G3/Weyl3 response program.

## Critical conditional scope

The result inherits Iter003-G2's explicit conditional assumption: the decomposition into a Lorentzian symmetric-time direction plus three-dimensional spatial complement uses the candidate null-link interpretation of the four elementary generators. G2 explicitly did not derive that null-link postulate from earlier CCRC axioms.

Therefore this is a **conditional kinematic representation/invariant bridge**, not an unconditional microscopic derivation of spacetime curvature.

## What is not established

The PASS does not establish that a microscopic pair perturbation physically equals the G3 tidal Hessian on one realized geometry. It does not identify:

- pair amplitude with `kappa`;
- combinatorial response scale with physical response (`beta` remains free);
- the pair cubic with the continuum Weyl3 action coefficient;
- `c6`;
- curvature normalization;
- branch phases/configuration maps;
- a global micro→continuum map;
- exact versus order-reduced dynamical treatment;
- global interacting measure/regulator removal;
- quantum unitarity, UV completion, full GR recovery, experiment, new physics or QGR correctness.

Theory established remains `0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized.

## Highest-information successor

The next gate should test **multi-shape, not single-H0, overlap** between this exact 2D balanced pair sector and the already-frozen Iter040/041 weak-tidal response panel.

The key question is representation-theoretic and can be frozen before inspection:

Does the Iter040/041 trace-free tidal-shape family contain an already-identifiable two-dimensional S4/tetrahedral subspace whose normalized quadratic/cubic invariants are exactly those of the G2 balanced pair tensor, on more than the single H0 direction?

A PASS would strengthen the bridge from one spectral coincidence to a finite-dimensional shape-manifold correspondence. It still would not identify amplitudes or couplings.