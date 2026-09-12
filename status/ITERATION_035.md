# Iteration 035 — G35 distant torsion branch verification

Status: PREREGISTERED / READY FOR PRODUCTION
Date: 2026-09-12

## Frozen scientific object
Reconstruct the exact deterministic large-start family used in Iter034 G34 for all 6 lanes x 4 start scales `[0.5, 1.5, 3.0, 6.0]` using the same nonlinear 24-equation finite torsion system. For every residual-qualified origin candidate, independently polish and test whether it defines a numerically distinct, metric-compatible branch patch rather than a raw-coordinate basin artifact.

## Frozen promotion criteria
A lane is `NUMERICALLY_VERIFIED_SCOPED_DISTINCT_EXTENDABLE_FINITE_TORSION_BRANCH_PATCH` iff all are true:
1. independent polished origin residual `< 1e-9`;
2. maximum origin metric-compatibility error `< 1e-7`;
3. origin edge transport differs from the reference by `> 1e-4` and its trace/trace2/determinant fingerprint differs by `> 1e-7`;
4. all four neighboring cells extend with residual `< 1e-8` and metric error `< 1e-7`;
5. plaquette-holonomy invariant distance from the reference patch is `> 1e-6`.

These thresholds are frozen before production results.

## Controls
- Reference branch must itself extend to all four neighboring cells and produce plaquette invariants.
- Same `C`, generator basis, conformal frame family and deterministic RNG seeds as Iter034/G9 lineage.
- Solver failure/nonconvergence is not evidence of root absence.

## Aggregate interpretation
- `SCIENTIFIC_PASS_SCOPED_DISTINCT_EXTENDABLE_BRANCH_COUNTEREXAMPLE`: at least one lane satisfies all frozen promotion criteria and the reference controls are valid.
- `NO_VERIFIED_DISTINCT_PATCH_IN_FROZEN_SCAN`: reference controls valid but zero lanes satisfy all promotion criteria.
- `CONTROL_INVALID`: reference patch controls fail in any production lane; no scientific branch conclusion is allowed.

Even a PASS is only a scoped finite-patch numerical counterexample to uniqueness in this realization. It is not a theorem of global nonuniqueness, not a complete QG theory, and does not establish tower-wide existence or physical phenomenology.

## Next gate rule
If PASS, freeze a branch-persistence/refinement gate across a larger neighboring-cell patch and multiple background amplitudes before any global conclusion. If zero verified patches, preserve the negative scan result and return to compactness/coercivity authority rather than weakening thresholds.
