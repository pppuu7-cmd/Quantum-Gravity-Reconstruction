# Iteration 037 — deeper refinement separation scaling and large-radius branch extension

Status: `PREREGISTERED / READY FOR PRODUCTION`
Date: 2026-09-12

## Motivation

Iter036 closed its frozen gate with
`SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_PERSISTS_ACROSS_BACKGROUND_AND_REFINEMENT_PROXY`:
44/48 lanes passed, all 48 reference controls were valid, all eight G35 witnesses survived the
shrinking-cell proxy through `h=0.35`, and six witnesses were jointly persistent across all frozen
background and refinement-proxy targets.

Iter037 does not repeat that test. It separates two remaining ways the branch evidence could fail:

1. **continuum-side coalescence / conditioning failure** — distinct finite branches may merge or
   become numerically singular as `h` is reduced further;
2. **spatial extension failure** — a branch that closes on a 15-cell patch may fail or become
   path-dependent on a larger patch.

All conclusions remain scoped numerical statements. This gate is not the full QGR projective-limit
theorem and cannot by itself establish global nonuniqueness or a continuum physical branch sector.

## Frozen seed set

Use exactly the six Iter036 jointly persistent seed indices:
`[0,1,3,4,5,7]`.

Mapping to the original G35 `(lane, scale_index)` witnesses remains the frozen Iter036 mapping.
No replacement seed may be introduced after production starts.

## Stream A — deeper shrinking-cell separation scaling

For each of the six frozen seeds, continue reference and candidate branches from the G35 baseline
through the target grid

`h in [0.25, 0.18, 0.12, 0.08]`, with `gamma=1`.

Each target is an independent matrix lane. At the target:

- both origin roots must remain residual-qualified and metric-compatible;
- both branches are extended on the same frozen 15-cell two-shell patch used in G36;
- invariant edge fingerprints and expanded plaquette-holonomy differences are recorded;
- the minimum singular value and condition number of the 24x24 origin torsion Jacobian are recorded
  separately for reference and candidate roots;
- raw branch-coordinate distance and the diagnostic `||z_candidate-z_reference||/h` are recorded.

The coordinate-distance diagnostic is explicitly **not gauge-invariant** and cannot promote a
physical claim; it is retained only to diagnose finite-root coalescence/runaway. Scientific branch
resolution continues to require invariant edge/holonomy separation.

### Frozen Stream-A lane criteria

A target lane is `DEEP_REFINEMENT_RESOLVED_DISTINCT_PATCH` iff:

1. both origin continuations reach target `h` with residual `<1e-9` and metric error `<1e-7`;
2. both 15-cell patches are complete, each cell residual `<1e-8` and metric error `<1e-7`;
3. expanded holonomy comparison is available;
4. either expanded holonomy invariant distance `>1e-9` **or** invariant edge-fingerprint distance
   `>1e-9` (numerically resolved finite-h distinction criterion);
5. candidate and reference origin Jacobian minimum singular values are finite and `>1e-8`.

The `1e-9` distinction threshold is a numerical-resolution threshold, not a physical continuum scale.
Failure below it is classified as unresolved/coalescing at this precision, not proof of equality.

A seed is `DEEP_REFINEMENT_SEQUENCE_PASS` only if it passes all four target h values.

## Stream B — larger positive-orthant patch-radius extension

For each of the same six frozen seeds, test radii `R in [3,4]` at `gamma=1, h=0.5`.

The patch is the positive-orthant integer simplex
`P_R = {x in Z^4_{>=0}: sum_i x_i <= R}`.
Thus `|P_3|=35` and `|P_4|=70` cells.

Each non-origin cell is solved independently from **every available immediate parent** `x-e_i`.
Multi-parent arrival is not hidden by choosing only the best path. For a cell to be promoted:

- every available parent continuation must reach residual `<1e-8` and metric error `<1e-7`;
- the independently parent-derived finite Lorentz matrices must agree with maximum pairwise matrix
  distance `<1e-5`;
- one deterministic representative (lowest residual, with lexicographic parent tie-break) is then
  frozen for the next shell.

Reference and candidate patches are both required to close. At least all elementary plaquettes whose
base and two positive neighbors lie inside the patch are compared by the same trace/trace2/determinant
holonomy invariants as G35/G36.

### Frozen Stream-B lane criteria

A radius lane is `LARGE_RADIUS_PATH_CONSISTENT_DISTINCT_BRANCH` iff:

1. reference patch contains exactly `C(R+4,4)` cells and all parent-consistency controls pass;
2. candidate patch contains exactly `C(R+4,4)` cells and all parent-consistency controls pass;
3. all cell residual/metric thresholds above pass;
4. candidate/reference patch holonomy invariant distance `>1e-8`;
5. origin invariant edge-fingerprint distance `>1e-9`.

A seed is `RADIUS4_SEQUENCE_PASS` only if it passes both `R=3` and `R=4`.

## Production matrix

- Stream A: `6 seeds x 4 h targets = 24` lanes.
- Stream B: `6 seeds x 2 radii = 12` lanes.
- Total: **36 independent production lanes** plus aggregate.
- GitHub matrix must use fail-fast disabled; intended maximum parallelism: **24**.

## Aggregate classifications

For each seed separately compute Stream-A and Stream-B sequence status.

Terminal aggregate classes:

- `SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_SURVIVES_DEEPER_REFINEMENT_AND_RADIUS4_PATH_CONSISTENCY`:
  at least one same frozen seed passes all four deeper-h lanes and both radius lanes, with all required
  reference controls valid.
- `PARTIAL_SCOPED_DEEP_REFINEMENT_OR_RADIUS_PERSISTENCE_ONLY`:
  no seed passes both streams, but at least one seed passes a complete stream.
- `NO_FULL_SEQUENCE_PASS_IN_FROZEN_G37_STRESS`:
  all required reference controls are valid but no seed passes either complete stream.
- `CONTROL_INVALID_OR_INCOMPLETE`:
  missing lanes or invalid reference controls prevent the corresponding conclusion.

## Claim locks

- finite-h numerical persistence is not a proof of a continuum/projective-limit branch;
- fixed numerical distinction thresholds do not establish a nonzero asymptotic limit;
- the local `h` deformation remains a shrinking-cell proxy, not the full QGR refinement map;
- positive-orthant radius growth is a controlled finite spatial patch, not global compactness;
- parent-path agreement is numerical consistency, not an analytic cocycle theorem;
- solver nonconvergence is not proof of root absence;
- global branch compactness/finiteness remains unproved;
- tower-wide uniform torsion-Jacobian gap remains unproved;
- physical branch measure/selection remains underived;
- absolute source normalization `beta` remains underived;
- `c6` remains unfixed;
- theory established remains `0%`;
- KMQGB `NEW_REQUIRED` remains unauthorized unless benchmark authority changes.
