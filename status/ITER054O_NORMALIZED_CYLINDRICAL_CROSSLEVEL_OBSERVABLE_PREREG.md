# Iter054O Preregistration — Normalized Cylindrical Cross-Level Observable Audit

Date: 2026-09-14
Gate: `ITER054O-NORMALIZED-CYLINDRICAL-CROSSLEVEL-OBSERVABLE`
Parent blockers: Iter054M category-E incomplete; Iter054N c6 phase datum blocked.

## Objective

Test whether QGR can close the normalized cross-level observable object independently of the still-missing absolute `c6` identity, using only already-authorized coherent-history/operator ingredients.

## Frozen candidate class

Preferred candidate is a normalization-quotiented coherent-history phase ratio/difference or normalized channel characteristic/expectation value. It must avoid the globally normalized oscillatory vacuum partition weight already blocked by Iter009.

## Frozen requirements

A candidate is accepted only if all are explicit:

1. `MICRO_DEFINED`: microscopic history/operator definition using already-authorized QGR ingredients;
2. `IR_DEFINED`: corresponding IR effective definition with `c6` symbolic/unfixed;
3. `COMMON_SCALE_CANCELLED`: common normalization/source-scale direction cancels algebraically; no `beta=1` convention;
4. `CYLINDRICAL_CONSISTENCY`: prospective finite refinement/cylindrical consistency on a frozen family;
5. `WEYL3_SENSITIVITY`: observable changes under a frozen Weyl3-active variation and has a Weyl-flat/control null where appropriate;
6. `NO_PHYSICAL_WEIGHT_IMPORT`: no use of G35-G37 distant roots as physical weights and no external target.

## Frozen negative controls

- multiply all microscopic amplitudes by a common nonzero normalization and verify quotient invariance;
- rescale the common source calibration direction and verify only unauthorized absolute-scale pieces change;
- remove the Weyl3 contribution and require the Weyl3-sensitive component to vanish on the relevant control;
- deliberately use the globally normalized oscillatory partition function route and require it to be rejected by authority.

## Terminal classifications

- `PASS_SCOPED_ITER054O_NORMALIZED_CYLINDRICAL_CROSSLEVEL_OBSERVABLE_DEFINED__C6_IDENTITY_STILL_MISSING` only if all six requirements pass.
- `BLOCKED_OBJECT_DEFINITION_ITER054O_CROSSLEVEL_OBSERVABLE_INCOMPLETE` if one or more required definitions/controls are absent.
- `INVALID_ITER054O` only for provenance/procedure/control failure.

Even PASS does not fix `c6`, authorize `beta=1`, establish the full quantum measure, theory correctness, unitarity, UV completion, strong hyperbolicity, experimental confirmation, or KMQGB `NEW_REQUIRED`.
