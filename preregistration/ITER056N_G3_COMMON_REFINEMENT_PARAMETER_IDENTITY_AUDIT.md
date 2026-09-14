# Iter056N preregistration — G3 common refinement-parameter identity audit

Date: 2026-09-14

Gate: `ITER056N-G3-COMMON-REFINEMENT-PARAMETER-IDENTITY-AUDIT`

## Frozen authority cutoff

`091463e97182e05d125e788ec565eb46f9a3061d`

Only authority at or before this cutoff may establish that the parameters were already the same object. The audit may inspect implementation semantics and derive algebraic identities from already-frozen definitions, but may not introduce a new physical identification.

## Motivation

Iter056M localized the strongest near-intersection:

- Iter054S: actual Weyl-active G3 fine-to-coarse geometric transport refinement;
- Iter040/041: actual treatment-blind normalized Weyl3 response kernel with finite-`h` convergence in the G10/G3 weak-tidal family.

A common overlap observable is admissible only if their refinement scales refer to the same finite geometric primitive or are connected by an already-authorized exact map. Numerical resemblance is insufficient.

## Frozen question

Does frozen QGR authority establish that the finite subdivision/refinement parameter used in Iter054S and the finite-cell spacing `h` used in Iter040/041 are one source-faithful refinement variable (or related by a uniquely derived exact geometric map) on the same G3 weak-tidal realization?

## Frozen obligations

A. **Same continuum/field realization.** The compared lanes must be the same G10/G3 weak static tidal family, with an explicitly matchable Hessian/geometry and amplitude, not merely two Weyl-active backgrounds.

B. **Same finite geometric primitive.** The Iter054S transport subdivision must correspond to the same edge/cell displacement on which the Iter040/041 holonomy-curvature/Weyl proxy is defined, or an exact pre-existing map between those primitives must be stated.

C. **Same refinement operation.** Increasing Iter054S subdivision and decreasing Iter040/041 `h` must implement the same parent→fine geometric refinement operation, not independent numerical discretizations that happen to approach the same continuum field.

D. **Source-faithful scale map.** If the symbols differ (`N`, segment length, `h`, etc.), their relation must follow uniquely from fixed physical path/cell geometry and existing QGR definitions. No arbitrary constant, coordinate convention, unit choice, interpolation or fitted mapping may be inserted.

E. **Object-provenance compatibility.** The Weyl-response sample and transport sample must be evaluable on the same finite G3 data object without importing a new source/boundary normalization, `beta=1`, `c6` value, treatment choice, or synthetic branch data.

## Required sources

At minimum inspect:

- Iter054S preregistration, implementation and terminal result;
- Iter040 preregistration, implementation and terminal result;
- Iter041 preregistration/implementation/result only as needed to verify inherited `h` semantics;
- the original G10/G3 weak-tidal realization used by both lines;
- any direct shared helper/module imported by both constructions.

## Frozen terminal classifications

1. `PASS_SCOPED_ITER056N_G3_COMMON_REFINEMENT_PARAMETER_IDENTITY_AUTHORIZED`
   - iff A–E are all established from frozen source semantics.
   - This only authorizes a successor overlap-observable construction; it is not itself a micro→continuum theorem.

2. `BLOCKED_OBJECT_DEFINITION_ITER056N_G3_TRANSPORT_AND_WEYL_RESPONSE_REFINEMENT_SCALES_NOT_YET_IDENTIFIED`
   - iff the same continuum family is shared but at least one of B–E lacks an already-authorized exact identity/map.

3. `SCIENTIFIC_FAIL_ITER056N_G3_REFINEMENT_PARAMETER_IDENTITY_FALSE`
   - iff frozen definitions positively show the parameters/refinement operations are incompatible objects, not merely under-specified.

4. `INVALID_AUDIT_ITER056N_SOURCE_OR_PROVENANCE_INCOMPLETE`
   - iff required source semantics cannot be inspected reliably.

## Prohibited moves

- no setting `h=L/N` unless that equality follows from the frozen implementations/geometry;
- no rescaling coordinates to make the grids match;
- no choosing one Iter040 amplitude after seeing which matches Iter054S unless exact same-amplitude authority already exists in the frozen family;
- no treating background Weyl activity as Weyl3 observable identity;
- no new microscopic source/measure/branch weight;
- no `beta=1`, fitted `c6`, or treatment-specific dynamics.

## Interpretation ceiling

Even PASS establishes only a common finite G3 refinement parameter suitable for a prospective shared observable. It does not establish the shared observable itself, a global regulator removal, microscopic measure, treatment selector, `c6` identity, quantum unitarity or QGR correctness.

Theory established remains 0%; `c6` symbolic/unfixed; `beta=1` unauthorized.