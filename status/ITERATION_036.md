# Iteration 036 — branch persistence under background deformation and refinement proxy

Status: PREREGISTERED / READY FOR PRODUCTION
Date: 2026-09-12

## Motivation

Iter035 G35 produced `SCIENTIFIC_PASS_SCOPED_DISTINCT_EXTENDABLE_BRANCH_COUNTEREXAMPLE`:
8 of 24 preregistered lane/scale pairs survived independent root polishing, metric compatibility,
one-star neighbor extension, and gauge-invariant plaquette-holonomy separation from the reference branch.

Iter036 asks a harder question: do any of those same verified finite branch patches persist when the
local neighborhood is enlarged and the conformal background is deformed, and do they survive a
controlled shrinking-cell proxy rather than existing only at one finite coordinate scale?

This remains a scoped numerical stress test. It is not a projective-limit theorem and does not prove
global nonuniqueness, tower-wide branch existence, compactness, or phenomenology.

## Frozen seed set

Use exactly the eight G35 verified lane/scale pairs:
`(0,3), (1,2), (1,3), (2,2), (2,3), (3,1), (4,2), (5,3)`.

The baseline branch is reconstructed using the same deterministic seeds, `C`, `o(C)` basis,
nonlinear 24-equation torsion system, conformal field coefficients, and start scales as G35.

## Two independent stress families

### A — background-amplitude persistence

For each of the eight verified seeds, continue both the reference and candidate roots from
`gamma=1` to each frozen target `gamma in [0.8, 1.0, 1.2]`, with normalized cell scale `h=1`.

### B — shrinking-cell refinement proxy

For each of the eight verified seeds, continue both roots from `h=1` to each frozen target
`h in [0.75, 0.50, 0.35]`, with `gamma=1`.

Here `h` rescales the coordinate argument of the same conformal background before evaluating
neighbor frames. This is explicitly a **local shrinking-cell proxy**, not the full QGR projective
refinement map and not evidence of a tower-wide continuum limit by itself.

Total production lanes: `8 x 3 + 8 x 3 = 48`.

## Expanded patch

At every target, both branches are tested on the frozen 15-cell two-shell patch

- origin;
- four first neighbors `e_i`;
- four axial second neighbors `2 e_i`;
- six mixed second neighbors `e_i + e_j`.

This supports plaquette-holonomy invariants at the origin and at all four first-neighbor base cells.

## Frozen lane promotion criteria

A lane is `VERIFIED_SCOPED_EXPANDED_PATCH_PERSISTENT_DISTINCT_BRANCH` iff all are true:

1. continuation of both reference and candidate origin roots reaches the target without a residual-qualified step failure;
2. target candidate origin residual `< 1e-9`;
3. maximum target candidate origin metric-compatibility error `< 1e-7`;
4. target origin edge transport differs from the target reference by `> 1e-4` and its trace/trace2/determinant fingerprint differs by `> 1e-7`;
5. the reference extends to all 15 cells with residual `< 1e-8` and metric error `< 1e-7`;
6. the candidate extends to all 15 cells with residual `< 1e-8` and metric error `< 1e-7`;
7. expanded-patch plaquette-holonomy invariant distance from the reference is `> 1e-6`.

Thresholds and target grids are frozen before production.

## Aggregate promotion criteria

For each G35 seed separately:

- `BACKGROUND_PERSISTENT` requires that seed to pass all three gamma targets;
- `REFINEMENT_PROXY_PERSISTENT` requires that seed to pass all three h targets;
- `JOINTLY_PERSISTENT` requires the same seed to satisfy both conditions.

Terminal aggregate classifications:

- `SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_PERSISTS_ACROSS_BACKGROUND_AND_REFINEMENT_PROXY`: at least one seed is `JOINTLY_PERSISTENT` and all required reference controls for its six lanes are valid.
- `PARTIAL_SCOPED_PERSISTENCE_ONLY`: at least one seed is persistent in one family, but no seed passes both families.
- `NO_VERIFIED_PERSISTENT_BRANCH_IN_FROZEN_STRESS`: all required controls are valid but no seed is persistent across either complete family.
- `CONTROL_INVALID_OR_INCOMPLETE`: missing lanes or invalid reference controls prevent the corresponding scientific conclusion.

## Claim locks

- G35/Iter036 finite branches are scoped numerical branch patches, not a global branch-count theorem.
- Solver nonconvergence is not evidence of root absence.
- The refinement proxy is not the full projective refinement limit.
- Global compactness/finiteness remains unproved.
- Tower-wide uniform torsion-Jacobian gap remains unproved.
- Absolute normalization `beta` remains underived.
- `c6` remains unfixed.
- KMQGB `NEW_REQUIRED` remains unauthorized unless benchmark authority changes.
- Theory established remains `0%`.
