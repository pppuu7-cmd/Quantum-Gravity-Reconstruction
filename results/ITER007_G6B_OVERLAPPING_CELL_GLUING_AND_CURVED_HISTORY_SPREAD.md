# QGR Iter007-G6B — overlapping B4 gluing, path composability, and curved history spread

Date: 2026-09-12
Status: `PASS_SCOPED_LOCAL_TWO_CELL_GLUING_AND_SERIAL_HISTORY_MEASURE / LOCAL_NET_AND_TWO_MODE_READOUT_OPEN`

GitHub Actions run: `34654604762`

Five independent lanes plus a fail-closed aggregate completed successfully.

## 1. Minimal B4 face gluing and exact support overlap

Treat the already derived direction-labelled `B4` cell as the Boolean incidence complex of one four-direction unit block. The minimal incidence-preserving gluing of two face-neighbour cells identifies one complete `B3` boundary face.

For one `B4`, the face vector is

`(V,E,F2,F3,F4) = (16,32,24,8,1)`.

The shared `B3` face contains

`(V,E,F2,F3) = (8,12,6,1)`.

Thus two face-neighbour local supports share exactly

- `8` vertices;
- `12` oriented edge variables;
- `6` plaquettes.

The rank-preserving automorphism group of the abstract `B3` face is the permutation group of its three atoms, so there are only `3! = 6` discrete gluing relabelings. Retaining the inherited relational direction labels selects the identity representative; forgetting the labels leaves six symmetry-equivalent maps, not a continuous coefficient family.

Among all `24^2=576` pairs of local diagonal histories for two face-neighbour cells, the number of shared fine edges has exact histogram

- `0` shared edges: `504` pairs;
- `1`: `54`;
- `2`: `12`;
- `3`: `6`.

The mean is exactly `1/6` shared edge per uniformly chosen local-history pair.

Classification:

`PASS_SCOPED_MINIMAL_INCIDENCE_PRESERVING_B4_FACE_GLUING_HAS_SHARED_B3_SUPPORT_AND_ONLY_DISCRETE_S3_RELABELING_FREEDOM`.

Boundary: this does not prove that the full global CCRC complex is uniquely a regular `Z^4` cubical lattice.

## 2. Path-groupoid composability resolves the naive 4D sequential interpretation

The existing 24-history instrument is attached to the `24` monotone paths between the two opposite vertices of one `B4` cell. Its coarse morphism therefore has source `n` and target

`n + (1,1,1,1)`.

Classify translated neighbouring cells by a shift `delta in {0,1}^4`. The intersection dimension is `4-|delta|`.

- `|delta|=1`: four face-neighbour cases, sharing a `B3` face;
- `|delta|=2`: six `B2` intersections;
- `|delta|=3`: four `B1` intersections;
- `|delta|=4`: one common-vertex case.

The diagonal history morphism of the shifted cell is serially composable after the first diagonal **only if** its source equals the first target. This requires uniquely

`delta=(1,1,1,1)`.

Those serial cells share exactly one vertex and share no fine edges or plaquettes. In particular, **face-neighbour cells are not serial path-groupoid history-channel steps**.

Classification:

`PASS_SCOPED_FACE_ADJACENT_B4_HISTORY_INSTRUMENTS_ARE_NOT_SERIAL_PATH_GROUPOID_MORPHISMS__ONLY_OPPOSITE_VERTEX_TOUCHING_DIAGONALS_COMPOSE`.

Consequence: the previous G5B construction that sequentially applies `O(h^-4)` local cell channels to one carrier remains a useful stress upper bound, but it is not an authorized interpretation of path-groupoid evolution through all face-adjacent four-cells.

## 3. Serial branch measure is already fixed

For each history the G8A branch operator obeys

`K_alpha^dagger K_alpha = I/24`.

For serially composable coarse diagonal blocks, canonical history-register composition gives

`24^n`

equal-norm branches at level `n`, each with probability

`24^-n`.

For two blocks there are exactly `576` ordered branch pairs, each with probability `1/576`.

This result does not require the system branch operators to commute. Equal norm follows recursively from `K_beta^dagger K_beta=I/24`.

Classification:

`PASS_SCOPED_CANONICAL_SERIAL_G8A_HISTORY_COMPOSITION_FIXES_PRODUCT_UNIFORM_JOINT_BRANCH_MEASURE_WITHOUT_COMMUTATIVITY_ASSUMPTION`.

Therefore the G6A ambiguity of arbitrary product/synchronized/reversed branch laws does **not** remain for serial path-groupoid blocks. A non-product cross-block history environment would be additional structure.

## 4. Global paths on a face-overlap region do not factor into two local diagonal registers

The union of two face-neighbour `B4` cells is the minimal `2x1x1x1` rectangular block. A monotone path across it contains five elementary steps: the overlap direction twice and the remaining three directions once.

Hence the number of global monotone paths is

`5!/2! = 60`,

not `24^2=576`.

Only `6` of those `60` global paths can be written as the edge union of two complete overlapping-cell diagonals. They are exactly the histories in which the repeated overlap direction occurs first and last, while the middle three directions occur in arbitrary order.

Thus only `10%` of global paths admit that two-local-diagonal interpretation.

Classification:

`PASS_SCOPED_GLOBAL_PATHS_ON_A_FACE_OVERLAP_REGION_DO_NOT_FACTOR_INTO_TWO_INDEPENDENT_B4_DIAGONAL_HISTORY_REGISTERS`.

This independently confirms that assigning one independent 24-history channel to every overlapping face-neighbour cell overcounts the global path alternatives.

## 5. Concrete curved-background 24-history spread

Use the already existing Iter006 G9 deterministic finite-curvature conformal branch. For each physical cell size

`h = 1, 1/2, 1/4, 1/8`,

solve the same discrete torsion-free equations on all 16 vertices needed by the 24 paths from one cell corner to the opposite corner. Construct all 24 finite transports `A_pi`.

For every ordered pair form the relative loop

`H_(q,p)=A_q^-1 A_p`.

Because both paths have the same endpoints, a local frame change conjugates `H_(q,p)`. Therefore

`tr(H_(q,p))`

is gauge-conjugation invariant.

Use the reference-free branch-permutation-symmetric diagnostic

`delta_(q,p)=tr(H_(q,p))-4`.

Across all `24^2=576` ordered pairs the RMS values are approximately

- `h=1`: `4.74615e-2`;
- `h=1/2`: `3.00040e-3`;
- `h=1/4`: `1.91026e-4`;
- `h=1/8`: `1.20994e-5`.

A log-log fit gives

`RMS(delta) proportional h^3.9786`.

The scaled values `RMS(delta)/h^4` remain in the narrow range `0.04746 ... 0.04956`.

All relative loops preserve the seed Lorentz form and determinant to numerical errors below about `1e-14`.

Classification:

`NUMERICALLY_VERIFIED_SCOPED_CURVED_B4_PAIRWISE_HISTORY_HOLONOMY_TRACE_SPREAD_IS_NONZERO_AND_SCALES_AS_H4`.

This provides a concrete curved-background, dimensionless, reference-free history-spread diagnostic at the same `h^4` order as the leading traced quantum history correction. It is **not** yet the two-mode quantum purity prediction.

## G6B conclusion

The central G6A ambiguity is now sharply separated into two cases.

### Serial coarse path evolution

Closed in scope:

- the relevant cells touch at one opposite vertex rather than sharing a face;
- the G8A branch measure is exactly product-uniform;
- no adjustable cross-cell correlation coefficient exists.

### Geometrically overlapping face-neighbour regions

They share a `B3` support and are not serial history-channel morphisms. Their correct treatment is a **local quantum net / overlapping-region algebra** problem. A joint sequential history probability law is not the missing object.

Therefore the active blocker becomes

`BLOCKED_MISSING_QUANTUM_LOCAL_NET_FOR_OVERLAPPING_B4_SUPPORTS_AND_CURVED_PHYSICAL_TWO_MODE_READOUT`.

## Next gate

`QGR-ITER007-G6C-LOCAL-NET-OF-OVERLAPPING-SUPPORTS-AND-CURVED-TWO-MODE-READOUT`

1. assign local observable/operator algebras to finite B4 subcomplexes using the existing `(G_v,A_e)` path-groupoid data;
2. prove isotony/restriction consistency and determine overlap-intersection structure;
3. distinguish algebraic commutation from Hilbert tensor factorization;
4. derive when disjoint supports factorize and what boundary/gauge constraints obstruct factorization;
5. construct the physical two-mode readout on a generic curved quotient fiber without inserting an arbitrary `2x2` map;
6. only then evaluate normalized local purity/decoherence numerically.

Claim lock: do not sum a history channel once per face-adjacent cell, do not invent correlated histories for non-composable cells, and do not call the `h^4` holonomy-spread diagnostic experimental decoherence.

## Reproducibility

- `code/qgr_iter007_g6b_cubical_gluing_support.py`
- `code/qgr_iter007_g6b_diagonal_composability.py`
- `code/qgr_iter007_g6b_serial_instrument_measure.py`
- `code/qgr_iter007_g6b_rectangular_overlap_paths.py`
- `code/qgr_iter007_g6b_g9_curved_history_spread.py`
- `code/qgr_iter007_g6b_aggregate.py`
- `.github/workflows/qgr-iter007-g6b-overlap-gluing.yml`
