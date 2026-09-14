# Iter056S terminal result — balanced B4 pair tensor to tidal cubic-shape bridge

Date: 2026-09-14
Gate: `ITER056S-BALANCED-B4-PAIR-TENSOR-TO-TIDAL-CUBIC-SHAPE-HELDOUT-VALIDATION`

Hypothesis-generation note: `e89913217b12ff37cadcf7510d77e954fac55ecb`
Prospective preregistration: `f3e0daf1f164953c382753867ccba80852ec8283`
Exact proof: `6aaf230e310da1c7305a85e164e258d34c9061cf`
Reproducibility implementation: `6c50b61684f3bdb418bb7f1c1a31fb4ae74df8bd`
Reproducibility workflow: `55ecc1699c9bf4a4660df9cdd54b4298afeb976e`
Frozen production head: `9e81cf94bdbe69e38a58b1242077ba3c11e61033`

## Authoritative production provenance

Authoritative held-out run: `34896461228` — terminal `success` on the frozen production head.

Aggregate job: `104156268611` — terminal `success`.

Frozen summary artifact: `10369815451` (`iter056s-summary`).

Frozen summary artifact digest: `sha256:155403a5097a311d462d56bd942d79496e3ea799e62f730b7e086fcc9fce10f0`.

Raw lane provenance consumed before terminal classification:

- lane 0: job `104151689867`; artifact `10369219622`; digest `sha256:77f1887e462237cdb7da0bd21abd0e615bf3d674b4d36881fe28e59fa2f42f6b`;
- lane 1: job `104151689701`; artifact `10369785317`; digest `sha256:d7c73bf4b9b10c7a28b016adaee70a631780a9daea5acbb6f00d550ed0a6a0bd`;
- lane 2: job `104151689702`; artifact `10369616299`; digest `sha256:fc583904d26ad45b4b734ef4c73d3291bc4645785706b36b511cc8679e14926c`;
- lane 3: job `104151689616`; artifact `10369064619`; digest `sha256:69a503a7ef9842d5d701846fd9e0b2e500a16339b8f4ecb45c9ed5e946e4eff8`;
- lane 4: job `104151689352`; artifact `10369630726`; digest `sha256:6e2a81e39898a46e2075043a7029bcd8968015d34bd300a1230e5c30afe0ffaa`;
- lane 5: job `104151689870`; artifact `10369656139`; digest `sha256:72f82800433fe0ff3ccd42786df74ff07b965d5c6807f658f6d77a02cc80a2e2`;
- lane 6: job `104151689495`; artifact `10368789716`; digest `sha256:1d6f37426783db34c3bb0a8184045e7e065ec6e41e1f4b4181a98ca6f59dd44a`;
- lane 7: job `104151689759`; artifact `10368433898`; digest `sha256:ad744784bf0a7772d042d32034f16371c2ee7dba71d624149453b587ac586295`.

The aggregate reported `complete=true`, `implementation_valid=true`, `pass=true`, all eight lane flags `true`, and empty `missing_lanes`, `duplicates`, and `parse_errors`. The aggregate classification exactly matches the prospectively frozen ceiling below.

## Terminal classification

**`PASS_SCOPED_CONDITIONAL_ITER056S_BALANCED_PAIR_SECTOR_HAS_EXACT_TIDAL_CUBIC_SHAPE_BRIDGE`**

The classification is now supported by both the generic exact algebraic proof and the fully consumed independent held-out production validation. Green CI alone was not used as scientific authority.

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

The generic proof implies every preregistered rational lane and all 24 permutation checks. The raw held-out run independently confirmed those frozen controls.

The cubic-null lane `a=-b != 0` is nonzero while `Tr(H_sp^3)=0` exactly.

The frozen unbalanced control leaves the H0-shape class as required, while the balanced lanes reproduce the exact shape. The production aggregate accepted all eight lanes under the preregistered expectations; no thresholds or scientific targets were changed after outputs.

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

## Successor chain already opened prospectively after the proof

Later preregistered/terminal work must be read together with this final production provenance rather than overwritten by it. Iter056T/U strengthen the scale-free spectral/weak-Weyl shape bridge; Iter056V records the missing absolute microscopic-to-tidal amplitude normalization; Iter056W audits whether the same microscopic balanced-pair shape has an already-owned parent→child refinement rule. None of those later steps changes the scoped Iter056S claim ceiling.