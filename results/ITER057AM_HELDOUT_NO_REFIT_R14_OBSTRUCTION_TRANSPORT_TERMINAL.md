# Iter057AM terminal result — held-out no-refit R14 obstruction transport

Date: 2026-09-16
Gate: `ITER057AM-HELDOUT-NO-REFIT-R14-OBSTRUCTION-TRANSPORT`
Preregistration: `d555671e69d2be898c7cfdd470f072bbb810a0be`
Held-out background authority: Iter057AL terminal `84d26921f6dd77ef1437c0f854a1543d76bc8360`
Durable AM authority: `64e09f0cc0121a509989036da42abce38e288e99`

## Terminal classification

**`PASS_SCOPED_ITER057AM_HELDOUT_NO_REFIT_R14_OBSTRUCTION_CLASS_PERSISTS_ON_INDEPENDENT_ONSHELL_BACKGROUND`**

## What was genuinely held out

The tested background was `AL-R1-4`, selected by the Iter057AL lexicographic held-out rule before any R14 obstruction quantity was computed.  It is inequivalent to the original AF seed by the prospectively frozen curvature-shape invariant `J=392/20577` versus AF `J=1/6`.

The AM preregistration froze the held-out background, complete 1114-dimensional R12 homogeneous basis, R14 compatibility map, gauge/coordinate/normalization conventions, truncation order, exact decision statistic and PASS/FAIL rules before fresh held-out `O0` or any obstruction-map column was inspected.

No equality of coordinate coefficients, AF rank, O0 support, parity/S3 sector or AG/AI generator was a decision criterion.

## Exact held-out result

Fresh held-out baseline:

- `O0` has 223 nonzero exact compatibility components (reported, not preregistered as a criterion);
- the held-out R12 authority independently replays Ricci/scalar/Einstein through coordinate degree 10 and flat de Donder through degree 11 exactly;
- the R12 homogeneous basis is the frozen deterministic exact RREF kernel, dimension 1114;
- the frozen R14 Bianchi/Noether left map annihilates `M14` exactly.

The complete held-out obstruction map has

- shape `1456 x 1114`;
- `nnz = 81096`;
- **`rank(B)=1114`**;
- **`rank([B|-O0])=1115`**;
- `dim ker(B^T)=342`;
- `dim(ker(B^T) cap O0^perp)=341`;
- therefore the obstruction quotient dimension is exactly **1**.

An independently reconstructed exact held-out witness satisfies

- `B^T y = 0` exactly;
- `O0^T y = 1` exactly;
- 56 nonzero rational coordinates.

The fresh witness was constructed from held-out `B/O0` without AG coefficients inside the pre-existing terminal-AH `b=0, parity=1000` coordinate sector.  Only after construction was it compared with AG; after normalization it agrees coefficient-by-coefficient with the pre-existing AG direction.  The un-normalized transported AG witness itself also annihilates the held-out map exactly and has nonzero pairing

`O0^T y_AG = 2326092237439/1482087190528`.

This coefficient agreement is supplemental and was not used as the AM decision criterion.

## Exact rank proof and independent reproduction

The primary exact rational Flint aggregate used the complete immutable 1114-column production map:

- run/job `35152805152 / 104984995635`;
- artifact `10469608520`;
- artifact digest `sha256:276396bf9c86acd3b09912e1a839b2c81c8a0f7f93064b51848daa21bb22f23d`;
- scientific payload SHA256 `d6e9bf4860c171323aff0c6d46f4e02d33489256ad51fdcafaca02d09e3186c2`.

A second exact rank proof used no rational RREF backend.  With the first fixed admissible certificate prime `p=1000003`, all rational denominators are invertible and both matrices have full column rank modulo `p`: 1114 for `B` and 1115 for `[B|-O0]`.  Hence corresponding maximal minors are nonzero over the rationals and the rational ranks are exactly 1114 and 1115.

The full modular certificate payload is byte-identical on local, Linux Actions and Windows Actions:

- implementation `e36fa99a1413b7db96b1997bfc8fc19fc43f3bf0`;
- workflow head `f4e4519b1ce1f1a67b3329af34edecf511c68961`;
- run `35153301125`;
- Linux job/artifact `104986643962 / 10469936936`, digest `sha256:d4da174010f4a5bfaec6640781ad4ec08a3fc0cf97973d43753c6cc5e0ddddac`;
- Windows job/artifact `104986643449 / 10469791911`, digest `sha256:3017efee293ef514fee83445b21bf9189c951ea3799544e554ca64b91c5209ed`;
- scientific payload SHA256 **`081dc4341346d3abb47395a6024abe524680e3d5ffec90803a055510cd9c82e1`**.

All eight production shard payload hashes were independently recomputed from raw JSON and all 1114 production columns were compared coefficient-for-coefficient against a separate local direct implementation: **0 mismatches**.

The optimized direct `G2 x h12` operator was authorized only after fixed pre-frozen columns `0,557,1113` matched the full nonlinear held-out finite difference coefficient-for-coefficient.  Their exact nonzero counts were respectively `26`, `72`, and `24` in both paths.

## New scientific fact

The AF obstruction is **not** merely an accident of the original single frozen background: the same one-dimensional finite-order obstruction class persists on a genuinely independent, prospectively held-out, source-faithful on-shell background without refit.

However the detailed linear algebra is background-dependent:

- original AF: `rank(B)=1110`, `dim ker(B^T)=346`;
- held-out AM: `rank(B)=1114`, `dim ker(B^T)=342`.

Thus persistence is at the level of the nonzero one-dimensional obstruction quotient, not equality of the complete obstruction map or all kernel dimensions.

## Claim ceiling

This is one independent held-out finite-local replication at the frozen R14 order.  It is **not** an open-neighborhood, all-orders or global no-go theorem.  It establishes no physical stability, hyperbolicity, ghost, quantum unitarity, UV-completion, regulator-removal or experimental claim.  `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.

## Highest-information next gate

Prospectively repeat the same unchanged structural criterion on at least one more independent Iter057AL authority that has never had R14 data inspected.  `AL-R1-3` is the highest-information next replication candidate.  No comparison rule, rank target, witness support or generator coefficient may be changed based on the Iter057AM outcome.
