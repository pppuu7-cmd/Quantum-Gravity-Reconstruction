# Iter057AM — held-out no-refit cross-background R14 obstruction transport

Status: **PROSPECTIVELY FROZEN BEFORE ANY HELD-OUT R14 OUTCOME**
Date: 2026-09-16
Parent background-authority terminal: `84d26921f6dd77ef1437c0f854a1543d76bc8360`
Parent AL preregistration: `c712f5034963048a8ab9a4ad812a47000a89be47`
Frozen AL manifest: `eabf19dbf32463127bd574032742a116e18267a6`
Manifest payload SHA256: `1e58ef49d36ac75efdd066f6b55ce2e48d9d8bce0307a9283ebe4483b026888f`
Durable AL aggregate authority: `983b6be90004077a76b3476c9854f5eba4542399`

## Scientific question

On the genuinely independent, prospectively held-out exact on-shell R12 background `AL-R1-4`, does the complete unrestricted 1114-dimensional homogeneous R12 freedom fail to remove the coordinate-degree-12 / R14 Bianchi-Noether compatibility obstruction, without any refit of background, basis, gauge, normalization, truncation order, compatibility map or decision statistic?

This is the first genuine held-out test of whether the finite-order AF obstruction class persists beyond the original frozen realization.

## Frozen held-out authority

Held-out seed: **`AL-R1-4`**.

It was selected only by the Iter057AL rule frozen before nonlinear completion: lexicographically last surviving `seed_serialization` among the prospectively frozen candidates.

Source production evidence:

- Actions run `35150321723`;
- job `104976691209`;
- artifact `10468978252`;
- artifact digest `sha256:93009fefb07e858cd50f335a96210d8b3405ff4cfc94dce6d50b6d7ebc809cdf`;
- candidate scientific payload SHA256 `5484179f3d86414918d0aed05e4c5a63dca802f4f8f1631c8259e8bf576c9fc5`;
- curvature-shape invariant `J=392/20577`, distinct from canonical AF `J=1/6`.

No held-out R14 residual, O0, obstruction-map column, rank defect, witness, support sector or pairing was inspected before this preregistration.

## Frozen equations, basis and conventions

All conventions are inherited unchanged from terminal Z/AC/AD/AF:

1. metric signature `eta=diag(-1,1,1,1)`;
2. `kappa=2/25`;
3. flat de Donder local-series gauge convention;
4. normalized symmetric trace-reversed metric Taylor coefficients;
5. exact rational arithmetic only for terminal classification;
6. unrestricted pure degree-12 homogeneous correction space = right kernel of the same complete `M12` principal complex, dimension 1114;
7. deterministic right-null basis = RREF pivot/free-coordinate convention already used by Iter057AD/AF;
8. R14 affine system has the same complete unrestricted pure degree-14 principal matrix and canonical Bianchi/Noether left map `L14` as AC/AD;
9. coordinate degree 12 Einstein and degree 13 de Donder residual form the R14 affine RHS;
10. `O0 = L14*r0` is freshly computed on the held-out R12 background;
11. each obstruction-map column is the exact directional change `L14*(r(h_j)-r0)` for the frozen R12 kernel direction `h_j`, or an algebraically equivalent exact linearization proved against direct finite-difference controls before use.

No additional homogeneous freedom, coordinate transformation, basis tuning or background-dependent normalization may be introduced.

## Frozen comparison quantities

Cross-background comparison is structural only.  The held-out result will report:

- complete obstruction map shape and exact nnz;
- `rank(B)`;
- `rank([B|-O0])`;
- `dim ker(B^T)`;
- `dim(ker(B^T) ∩ O0^perp)`;
- obstruction quotient dimension, defined as the difference of the preceding two dimensions;
- exact nonzero count of freshly computed `O0`;
- existence/nonexistence of an exact normalized dual witness `y` with `B^T y=0`, `O0^T y=1`;
- complete Bianchi/Noether and source/background replay controls.

The following are **not** decision criteria and may not be imposed post hoc:

- equality of held-out `rank(B)` to AF rank 1110;
- equality of O0 support/nonzero count to 223;
- equality of any coordinate coefficient;
- AH parity localization;
- S3 invariance;
- a 56-coordinate witness;
- equality of the AI scalar generator;
- any sign/scale choice chosen after outcome.

## Held-out firewall / no-refit rule

After this preregistration it is forbidden to change, based on held-out outcome:

- the held-out seed;
- R12 kernel basis or its ordering;
- R14 compatibility basis;
- gauge or coordinates;
- normalization;
- equations/source;
- truncation order;
- obstruction statistic;
- rank backend acceptance rule;
- PASS/FAIL definitions.

If a frozen object is technically unavailable, classify BLOCKED rather than substitute a more convenient object.

## Exact production and reproduction obligations

A. Reconstruct `AL-R1-4` from its immutable Iter057AL artifact and verify its scientific payload hash and all AL exact controls before any R14 computation.

B. Independently replay held-out vacuum Einstein through coordinate degree 10 and flat de Donder through degree 11.

C. Reconstruct complete 1114-dimensional exact R12 homogeneous kernel with exact annihilation by `M12`.

D. Freshly compute held-out `r0`, `L14`, `O0`, and verify `L14*M14=0` exactly.

E. Compute all 1114 columns of the held-out obstruction map. Sharding is allowed only by prospectively fixed column ranges and must cover each column exactly once.

F. Aggregate only terminal shard artifacts; verify coverage, provenance and exact hashes.

G. Compute `rank(B)` and `rank([B|-O0])` exactly. At least one independent exact rank backend / integer-cleared Critic must reproduce the decision quantities.

H. If incompatible, independently construct and replay a normalized exact dual witness `B^T y=0`, `O0^T y=1`.

I. Negative/control fixtures must include zero-O0 compatibility and at least one direct finite-difference replay of any optimized linearized column evaluator if such optimization is used.

## Terminal classification

### PASS_SCOPED

`PASS_SCOPED_ITER057AM_HELDOUT_NO_REFIT_R14_OBSTRUCTION_CLASS_PERSISTS_ON_INDEPENDENT_ONSHELL_BACKGROUND`

iff all exact authority/no-refit controls pass and

- `rank([B|-O0]) = rank(B)+1`, equivalently `O0` is not in `col(B)`;
- obstruction quotient dimension is exactly 1;
- an exact normalized dual witness exists and replays `B^T y=0`, `O0^T y=1`.

No equality to AF coordinate data or AF rank is required.

### SCIENTIFIC_FAIL

`SCIENTIFIC_FAIL_ITER057AM_HELDOUT_VALID_BACKGROUND_HAS_NO_R14_OBSTRUCTION_AFTER_COMPLETE_R12_HOMOGENEOUS_FREEDOM`

iff the held-out background is valid, the complete exact map is realized, all controls pass, and

- `rank([B|-O0]) = rank(B)`, equivalently the complete unrestricted homogeneous R12 freedom can absorb the held-out R14 compatibility residual.

This FAIL must not be rescued by changing basis/background/normalization or comparison rule.

### BLOCKED

`BLOCKED_ITER057AM_COMPLETE_HELDOUT_EXACT_OBSTRUCTION_MAP_NOT_TECHNICALLY_REALIZED`

for incomplete exact map, incomplete shard coverage, unavailable authority, or exact-computation failure that prevents the frozen decision.

### INVALID

`INVALID_ITER057AM_HELDOUT_FIREWALL_AUTHORITY_EXACTNESS_OR_NO_REFIT_CONTROL_FAILURE`

for outcome-dependent seed/basis/normalization/equation/truncation changes, invalid AL provenance, numerical-tolerance classification, or failed frozen controls.

## Claim ceiling

Even a PASS is one held-out replication of one finite local obstruction order, not a global/all-orders no-go theorem. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no stability, unitarity, UV, regulator-removal or experimental claim is authorized; theory established remains `0%`.
