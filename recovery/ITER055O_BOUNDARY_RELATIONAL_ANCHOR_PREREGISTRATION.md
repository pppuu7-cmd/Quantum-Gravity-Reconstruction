# Iter055O preregistration — boundary relational smearing anchor: direction versus physical scale

Date: 2026-09-14
Gate: `ITER055O-BOUNDARY-RELATIONAL-SMEARING-ANCHOR`

## Frozen question
Do existing QGR shared-B3/B4 geometric data already provide the additional relational datum required by Iter055N to label a covariant smearing family, and if so do they fix both (a) a covariant boundary direction/frame anchor and (b) a physical radial/UV smearing scale?

## Frozen authority set
Audit only existing QGR authority:

- G6C/G6E shared B3 face/configuration geometry and boundary measure;
- finite-frame/metric transformation rules already used by G6F/G6G/G6H;
- G7A and related scale/normalization results;
- G6G/G6H preparation/readout scales;
- Iter053 compact-support scale as a negative control.

No new boundary normal convention, observer, clock, lattice spacing, Planck length, cutoff, detector width or scale may be added.

## Frozen obligations
1. **Directional anchor:** determine whether a shared non-null B3 face plus the physical metric supplies a covariantly transforming normal/co-normal or equivalent local frame datum on the regular domain, rather than merely a coordinate axis label.
2. **Scale anchor:** determine whether existing authority fixes a physical length/momentum scale associated with that boundary anchor that can set the radial profile of an `L2` smearing kernel.
3. Distinguish physical metric normalization from an unfixed coordinate/microscopic lattice parameter.
4. Do not use G6G/G6H preparation widths as candidate-owned scale unless the source explicitly promotes them beyond preparation/readout data.
5. Do not use Iter053 `SUPPORT=0.24`, bump exponent, `beta`, `c6`, or an unfixed microscopic `h` as bridge scale.
6. Permit a partial classification: direction may be source-derivable while physical scale remains missing.

## Frozen classifications
- `PASS_SCOPED_ITER055O_BOUNDARY_GEOMETRY_SUPPLIES_DIRECTION_AND_PHYSICAL_SMEARING_SCALE` only if both a covariant relational direction/frame and a source-fixed physical profile scale are already determined.
- `PASS_SCOPED_PARTIAL_ITER055O_BOUNDARY_DIRECTION_ANCHOR_EXISTS__PHYSICAL_SMEARING_SCALE_UNFIXED` if regular shared-boundary geometry determines a covariant direction/frame anchor but no source-fixed physical radial scale.
- `BLOCKED_OBJECT_DEFINITION_ITER055O_BOUNDARY_RELATIONAL_ANCHOR_NOT_SOURCE_DEFINED` if even the direction/frame anchor cannot be constructed source-faithfully on the audited regular domain.
- `INVALID_PROVENANCE_ITER055O_BOUNDARY_SCALE_AUTHORITY_CONFLICT` only if existing scale authorities conflict irreconcilably.

## Interpretation ceiling
A partial PASS would permit future kernel families to depend covariantly on the boundary direction/normal but would still forbid selecting a radial width/profile scale. It would not define a concrete bridge, dynamics, beta, c6, Weyl3 treatment, regulator removal, unitarity, UV completion, GR recovery, experiment or theory establishment.

No GitHub Actions run is preregistered; this is a source/geometric authority audit.
