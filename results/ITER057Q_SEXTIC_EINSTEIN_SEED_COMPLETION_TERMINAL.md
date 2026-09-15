# Iter057Q terminal result — sextic c6^0 Einstein-seed completion

Date: 2026-09-15
Gate: `ITER057Q-SEXTIC-EINSTEIN-SEED-COMPLETION`
Preregistration: `afc9098e6de828e8647aad5b1d8316b29f0b61a0`
Implementation: `d70dc4e53e1e3ae5db95162978c9e89c618f38ba`
Workflow head: `052fb130f81ea52fe9af840e42a4050415b46956`
Actions run: `34956377793`
Job: `104339311005`
Artifact: `10391933651` (`iter057q-sextic-einstein-seed`)
Artifact digest: `sha256:8b1a0afe28bbb71de0b6413c24193f8dfc3dcadbb26b78d3f008f11b2508155d`

## Terminal classification

**`PASS_SCOPED_ITER057Q_SEXTIC_EINSTEIN_SEED_COMPLETES_THROUGH_QUARTIC_EINSTEIN_ORDER__WEYL3_SECOND_SOURCE_JET_CAN_NOW_BE_RECOMPUTED`**

This is exactly the prospectively frozen maximum scoped PASS.

## Exact unrestricted sextic system

The fixed Iter057O seed has a nonzero homogeneous coordinate-degree-four Einstein residual, so a sextic correction is genuinely required.

The unrestricted trace-reversed sextic correction contains

`10 * C(9,3) = 840`

normalized coefficients. The frozen homogeneous polynomial complex contains

- 224 degree-five de Donder rows;
- 350 degree-four Einstein rows;
- 574 total rows.

Fresh exact production gives

`shape(M)=(574,840)`,

`nnz(M)=2296`,

`rank(M)=494`,

`rank([M|r])=494`,

`nullity(M)=346`,

`left-nullity(M)=80`.

The complete canonical 80-vector Bianchi basis has rank 80 and annihilates the exact matrix. All eighty affine compatibility contractions vanish exactly for the Iter057O degree-four residual.

No numerical rank tolerance is used.

## Exact particular solution

The canonical pivot solve, with all 346 homogeneous directions set to zero, gives one exact unrestricted sextic correction with 69 nonzero normalized coefficients.

The exact linear-system residual vanishes in all 574 rows. The combined G3 + quartic + sextic trace-reversed perturbation satisfies the frozen linear de Donder condition exactly through homogeneous coordinate degree five.

The sextic correction is pure coordinate degree six, hence it and all derivatives through order five vanish at the origin. Therefore it preserves all Iter057O four-jet data and, in particular, the Iter057P corrected-seed Weyl3 point source.

## Independent nonlinear full-metric control

The production evaluator constructs the completed seed

`g_seed^(6)=g_G3+r^(4)+r^(6)`

and recomputes the nonlinear Levi-Civita connection, Ricci tensor, scalar and Einstein tensor directly through coordinate degree four.

Fresh-run controls give exactly

`R_ab=0`, `R=0`, `G_ab=0`

through the full frozen order for every independent component.

All frozen controls are `true`, including:

- Iter057O replay;
- lower Einstein orders remain zero;
- degree-four contracted Bianchi identity;
- complete 574x840 matrix construction;
- exact rank 494 and left-nullity 80;
- canonical Bianchi count/rank 80 and exact matrix annihilation;
- augmented rank equals rank;
- 80/80 compatibility contractions zero;
- exact particular-solution residual zero;
- pure-degree-six jet preservation;
- combined de Donder exact;
- inverse identities through degree four;
- direct nonlinear Ricci/scalar/Einstein zero through degree four;
- preservation of the Iter057P four-jet.

## Consequence

The zeroth-order Einstein seed is now source-owned and vacuum-consistent through coordinate degree four while preserving the curvature-active origin and the exact Iter057P Weyl3 point source.

Because `E_W3` contains two covariant derivatives of an object quadratic in curvature, its coordinate-degree-two source jet can depend on the metric six-jet. That six-jet is now fixed by this Iter057Q canonical seed.

Therefore the next scientifically admissible step is a fresh exact reconstruction of the corrected-seed Weyl3 Euler tensor through coordinate degree two. The historical uncompleted-G3 second source jet from Iter057M is not reusable.

## Scope ceiling

This PASS remains a finite local vacuum-seed certificate through coordinate degree four. It is not an all-orders Ricci-flat neighborhood, convergence theorem, global/asymptotic solution, or Einstein+Weyl3 solution.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`; no experimental, physical-characteristic, hyperbolicity, ghost, stability, unitarity, regulator-removal or UV-completion claim is authorized.