# Iter057AN — second independent-background no-refit R14 obstruction replication

Status: **PROSPECTIVELY FROZEN BEFORE ANY `AL-R1-3` R14 OUTCOME**
Date: 2026-09-16
Parent background authority: Iter057AL terminal `84d26921f6dd77ef1437c0f854a1543d76bc8360`
Parent first held-out replication: Iter057AM terminal `36531ef7a2c50fbf4055cfdbc42c7ae0ef02299f`
Frozen Iter057AL manifest: `eabf19dbf32463127bd574032742a116e18267a6`

## Scientific question

Does the same finite-order structural obstruction criterion used in Iter057AM persist, without any refit, on a **second** independent exact on-shell R12 background authority, `AL-R1-3`, for which no R14 obstruction quantity has yet been computed?

This gate tests multi-background robustness rather than coefficient equality.

## Prospectively frozen test background

Second replication background: **`AL-R1-3`**.

Source authority:

- Iter057AL run `35150321723`;
- job `104976691419`;
- artifact `10468837671`;
- artifact digest `sha256:53ec55e0f99dec4eac538ac369136bc8808f7a6855d01f68d7e48dc4db029d45`;
- scientific payload SHA256 `6fdf87a15d783e601c02c63b49cfd55a45b83eb258d5decf4ca1e46b5ad0141a`;
- frozen curvature-shape invariant `J=2025/59582`.

`AL-R1-3` is inequivalent to both canonical AF (`J=1/6`) and AM held-out `AL-R1-4` (`J=392/20577`) by the same Iter057AL invariant rule.  It was not used to select the Iter057AM obstruction statistic, rank target, basis, witness support or generator coefficients.

No `AL-R1-3` R14 residual, O0, obstruction-map column, rank, witness or obstruction pairing was inspected before this preregistration.

## Frozen conventions and exact map

Exactly the Iter057AM conventions are reused, without modification:

- `eta=diag(-1,1,1,1)`, `kappa=2/25`;
- flat de Donder local-series convention;
- complete deterministic exact RREF basis of the 1114-dimensional R12 homogeneous kernel;
- complete R14 affine system and canonical Bianchi/Noether left map;
- exact rational arithmetic for classification;
- no additional homogeneous freedoms, coordinate changes, gauge changes, basis reordering or background-specific normalization.

The complete map remains `B: Q^1114 -> Q^1456`, with freshly reconstructed background-specific `O0`.

## Frozen direct-operator control rule

The direct bilinear `G2 x h12` directional operator established in Iter057AM may be reused **only after** it passes coefficient-for-coefficient against the full nonlinear `AL-R1-3` finite difference on the same pre-existing fixed control indices `0,557,1113`.

Those indices are frozen before any `AL-R1-3` R14 calculation and may not be replaced if a control fails.  Failure of a control invalidates the optimized path and requires the full nonlinear path or BLOCKED classification; it does not authorize choosing other controls.

## Frozen decision quantities

Report exactly:

- shape and exact nnz of complete `B`;
- exact `rank(B)`;
- exact `rank([B|-O0])`;
- `dim ker(B^T)`;
- `dim(ker(B^T) cap O0^perp)`;
- obstruction quotient dimension;
- fresh `O0` nonzero count;
- existence/nonexistence of an exact normalized dual witness `B^T y=0`, `O0^T y=1`.

The following are **not criteria**:

- matching AF rank 1110;
- matching AM rank 1114;
- matching O0 nonzero count 223;
- matching any coordinate coefficient;
- parity/S3 support;
- 56-coordinate witness;
- equality to AG/AI generator;
- equality of map nnz 80982 or 81096.

## Exact rank certificate rule

The rational Flint aggregate remains the primary exact backend.

An independent exact certificate may use the ordered prime list `[1000003,1000033,1000037]`, selecting the first prime for which every rational denominator in the complete map and O0 is invertible.  The prime choice is denominator-dependent only, never rank-dependent.  Full column rank modulo such a prime is an exact proof of the corresponding rational full-column rank through a nonzero maximal minor.

A separate exact backend or certificate must reproduce the decision quantities.

## No-refit firewall

After this preregistration, outcome may not change:

- test background;
- R12 kernel basis or ordering;
- R14 compatibility basis;
- equations/source;
- gauge/coordinates;
- normalization;
- truncation order;
- control indices;
- rank/certificate acceptance rule;
- PASS/FAIL criteria.

## Terminal classification

### PASS_SCOPED

`PASS_SCOPED_ITER057AN_SECOND_INDEPENDENT_BACKGROUND_REPRODUCES_ONE_DIMENSIONAL_R14_OBSTRUCTION_CLASS`

iff all authority/control/no-refit checks pass, the complete exact map is realized, and

- `rank([B|-O0])=rank(B)+1`;
- obstruction quotient dimension is exactly 1;
- an exact normalized dual witness exists with `B^T y=0`, `O0^T y=1`.

### SCIENTIFIC_FAIL

`SCIENTIFIC_FAIL_ITER057AN_VALID_SECOND_BACKGROUND_HAS_NO_R14_OBSTRUCTION_AFTER_COMPLETE_R12_FREEDOM`

iff all controls pass and `rank([B|-O0])=rank(B)`.

### BLOCKED

`BLOCKED_ITER057AN_COMPLETE_EXACT_SECOND_BACKGROUND_OBSTRUCTION_MAP_NOT_REALIZED`

for incomplete map/coverage or technical exact-computation failure.

### INVALID

`INVALID_ITER057AN_NO_REFIT_AUTHORITY_OR_EXACTNESS_CONTROL_FAILURE`

for authority mismatch, outcome-dependent tuning, failed direct controls used anyway, numerical-tolerance classification or changed frozen scientific object.

## Interpretation ceiling

Even PASS would establish only finite-order replication on two independent additional backgrounds plus the original AF realization.  It would support a **multi-background finite-local robustness statement**, not an all-orders/global theorem. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no stability, unitarity, UV, regulator-removal or experimental claim is authorized; theory established remains `0%`.
