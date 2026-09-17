# Corrected degree-eight Weyl^3 source reconstruction

Status: **PROSPECTIVELY PREREGISTERED / NOT YET PRODUCED**  
Date: 2026-09-17

## Scientific question

Does the source-faithful Frechet `P_F = dI_3/dR` construction that corrected the degree-six Weyl^3 source continue consistently through coordinate degree eight on the established dodecic Einstein seed, and does the resulting corrected degree-eight source agree with or falsify the historical Iter057AA degree-eight source?

This is a new higher-order source-faithfulness science gate. It is not a continuation of the BA/BJ repair alphabet.

## Scientific parents

Latest corrected local-response authority:

- corrected Iter057Y terminal commit `eae9c35e408050fe1bff86e88e9492a6fcc6c8fc`;
- classification `PASS_SCOPED_ITER057Y_CORRECTED_AT_SOURCE_EXACT_Q8_RESPONSE_EXISTS`;
- terminal payload SHA256 `490967663d088b9192ab9451946aedfb2322530b991e3d1e7be685650e6903ca`.

Corrected degree-six source authority:

- Iter057AT preregistration `6039cb2ed1380b549bced3d33634362ef57345d4`;
- production head `c4e7ccc05ea1b8f4967379fc370812dfa99cce03`;
- durable corrected source `data/ITER057AT_CANONICAL_SOURCE_DEGREE6.csv`;
- file SHA256 `1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b`;
- ordered 840-vector SHA256 `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- 140 nonzero degree-six coefficients;
- `c6 = SYMBOLIC_UNFIXED`.

Source-convention authority:

- Iter057BJ terminal commit `eb1aafc711b78c5bf845448e7d4c0edb7bd1b0c2`;
- `MAP_MINUS`;
- in frozen Iter057Y convention, `S_std_corrected = -AT`.

Corrected Frechet authority lineage:

- Iter057AO terminal covariant variation authority `3246b31fde58d061f7e35cbc6be22236d1c7b2a8`;
- Iter057AQ terminal localization that the degree-six discrepancy is caused by the legacy `P` construction;
- Iter057AT independent agreement of the corrected Frechet `P_F` downstream source.

Historical degree-eight comparator:

- Iter057AA implementation `29e6fb029f2d468b81e8d7b4e6dbe18d22baedd4`;
- terminal commit `2c84ddcb5dd22cfe06cd3a1a273b4a0e141b605e`;
- historical classification `PASS_SCOPED_ITER057AA_CORRECTED_DODECIC_W3_EIGHTH_SOURCE_FIRST_PRINCIPLES_RECONSTRUCTED`.

Iter057AA is preserved as historical authority for its frozen lineage. It must not be reclassified. This gate asks whether its degree-eight source survives the subsequently established correction of the `P` construction.

## Frozen seed and geometry

Reuse the exact source-independent dodecic Einstein seed/geometry construction from

`code/qgr_iter057aa_corrected_dodecic_seed_weyl3_eighth_source_jet.py`

only for:

- canonical R12 seed materialization/provenance;
- inverse metric through the required order;
- connection and Riemann/Weyl geometry;
- exact Ricci/scalar/Einstein zero controls.

The historical Iter057AA `P` constructor and historical source coefficients are forbidden inputs to the corrected constructor lanes.

## Corrected standard-source object

The AT-like standard object is the exact covariant Euler `Edown` produced from the corrected Frechet tensor `P_F`.

For source through coordinate degree eight:

1. compute Weyl/Riemann geometry on the frozen dodecic seed;
2. construct `I3`/quadratic `Q` source-faithfully;
3. construct `P_F` by the already-authorized algebraic-Riemann Frechet solve, with sufficient truncation order for an exact degree-eight source;
4. assemble the Euler source by two independent downstream implementations;
5. serialize the complete ordered degree-eight standard vector over 10 symmetric tensor pairs x 165 degree-eight monomials = 1650 slots.

No historical X/AA target coefficient may be loaded by either corrected constructor lane.

## Mandatory degree-six reduction

Before any historical degree-eight comparison is consumed, each corrected lane must show that the degree-six projection of its standard `Edown` is byte/order/value equivalent to Iter057AT across the complete ordered 840-slot basis.

This is a hard source-faithfulness control. Failure is `INVALID_IMPLEMENTATION` or a source-construction inconsistency; it may not be repaired by fitting sign, scale, basis or `c6`.

## Source sign for historical comparison

Iter057AT is the AT-like standard `Edown` object. Iter057BJ separately established that the frozen Iter057Y/source serialization convention consumes the corrected standard source with the minus map.

Therefore define prospectively:

- corrected standard degree-eight object: `E8_std = Edown_degree8`;
- corrected historical/Y-format degree-eight source: `S8_corrected = -E8_std`.

Historical Iter057AA serialized its source as `-Edown`. Therefore comparison with Iter057AA must be:

`S8_corrected` versus historical Iter057AA degree-eight source,

never `+E8_std` versus Iter057AA.

No sign choice is allowed after observing coefficients.

## Independent lanes

### Primary corrected lane

Use the corrected Frechet `P_F` and a prospectively generalized exact transcription of the AQ/Iter057X downstream Euler assembly to degree eight.

### Independent corrected lane

Use the same already-authorized corrected Frechet `P_F` but independently assemble the covariant Euler source using the AO direct first-divergence / second-divergence construction generalized prospectively to degree eight. It must not call the primary source assembler or read the primary payload.

The shared `P_F` is not a new hypothesis here: its degree-six correction and independent Frechet authority were established by AO/AQ/AT. The new hypothesis is higher-order continuation of that corrected object.

### Historical comparator lane

Freshly replay the pinned historical Iter057AA implementation in a separate Actions job. It may not be consumed by either corrected constructor lane. It is used only by the frozen terminal comparison after both corrected lanes have produced their outputs.

## Exact controls

Required before scientific classification:

- exact seed provenance and Ricci-flat controls;
- exact arithmetic only, no tolerance;
- no historical target loaded by corrected lanes;
- Frechet `P_F` algebraic symmetries and homogeneity control through the required order;
- exact source symmetry;
- complete 1650-slot degree-eight basis in both corrected lanes;
- primary/independent corrected standard degree-eight vectors identical;
- primary/independent degree-six projections identical to Iter057AT complete 840-vector hash `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- `c6` symbolic/factored;
- historical comparator identity pinned to Iter057AA implementation and terminal authority.

## Prospectively allowed terminal outcomes

### Historical source survives correction

`PASS_SCOPED_CORRECTED_DEGREE8_SOURCE_RECONSTRUCTED_AND_HISTORICAL_ITER057AA_DEGREE8_SURVIVES_FRECHET_CORRECTION`

Requires all corrected controls and exact equality of `S8_corrected = -E8_std` to the fresh historical Iter057AA degree-eight vector across all 1650 slots.

### Historical source is corrected at degree eight

`PASS_SCOPED_CORRECTED_DEGREE8_SOURCE_RECONSTRUCTED_AND_HISTORICAL_ITER057AA_DEGREE8_DIFFERS_AFTER_FRECHET_CORRECTION`

Requires all corrected controls and at least one exact degree-eight mismatch against historical Iter057AA. This is a valid scientific result, not a failure. The historical AA/AB higher-order lineage then remains historical but is not authorized as the corrected higher-order lineage.

### Scientific/source inconsistency

`FAIL_SCIENTIFIC_SCOPED_CORRECTED_FRECHET_SOURCE_DOES_NOT_EXTEND_CONSISTENTLY_TO_DEGREE8`

Reserved for a valid target-blind corrected construction in which the two independently authorized downstream source assemblies disagree, or another exact higher-order source identity fails despite valid implementation/provenance controls.

### Invalid / blocked

`INVALID_IMPLEMENTATION_CORRECTED_DEGREE8_SOURCE_CONTROL_FAILURE`

or

`BLOCKED_CORRECTED_DEGREE8_SOURCE_EXECUTION`.

Implementation/provenance failures must not be promoted as scientific contradictions.

## Counterexample-first interpretation

The cheapest destructive test is the mandatory degree-six reduction to Iter057AT. If it fails, no historical degree-eight comparison is scientifically meaningful and the branch stops.

If degree six passes but corrected primary/independent degree-eight vectors disagree, the higher-order extension itself is not established.

Only after both pass may the historical AA comparator be used.

## Consequence for Q10 lineage

No corrected Q10 replay is authorized by preregistration alone.

- If historical AA survives exactly, a corrected-Q10 replay may reuse the degree-eight source only after a new prospective replay contract using the already-corrected Q8 response.
- If AA differs, old Iter057AB cannot be promoted into the corrected lineage; a durable corrected degree-eight source must be materialized before any corrected Q10 gate.

## Claim ceiling

This gate is L1/higher-order local source consistency only.

It does not determine `c6`, establish nonlinear completion, continuum/refinement consistency, a quantum measure, regulator independence, UV completion, experimental confirmation, or an established theory.

`c6 = SYMBOLIC_UNFIXED`.

`beta = 1` remains unauthorized.

`theory_established = 0`.
