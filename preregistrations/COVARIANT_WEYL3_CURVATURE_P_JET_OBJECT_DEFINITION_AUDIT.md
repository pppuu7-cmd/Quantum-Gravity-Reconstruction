# Preregistration — COVARIANT_WEYL3_CURVATURE_P_JET_OBJECT_DEFINITION_AUDIT

Date: 2026-09-19
Status: **FROZEN BEFORE SOURCE/OBJECT-DEFINITION AUDIT**

## Parent authority

The immediate authoritative diagnostic is `COVARIANT_WEYL3_GENERIC_P_PRIMITIVE_MISMATCH_DECOMPOSITION`, preregistration `c37f4381a7876385592a74d8bc1dbade2725e03a`, terminal result `42dfe4fe4d03ebe1d421e425753335948be493f2`, classification `GENERIC_P_PRIMITIVE_DECOMPOSITION_OTHER_LOCALIZED`.

The recovery front explicitly forbids residual-fitted correction and requires any covariant continuation to derive or scientifically justify relaxing the curvature-dependent `P`-jet source class, especially the frozen `DP=0` restriction.

## Frozen question

Do the exact authoritative source definitions already contain a sufficient curvature-dependent definition of `P^{abcd}` and its first ordinary derivative/jet at the normal-coordinate point to replace the abstract-source restriction `DP=0` in a future gate, without importing the observed residual or fitting a correction?

## Frozen audit inputs

Inspect **only** these two exact files at their frozen commits:

1. `preregistrations/COVARIANT_WEYL3_GENERIC_P_TENSOR_DENSITY_CONNECTION_COMPLETION.md` at `7a62dd856aec084add16af8e6793d157ef32637b`.
2. `preregistrations/COVARIANT_WEYL3_GENERIC_P_PRIMITIVE_MISMATCH_DECOMPOSITION.md` at `c37f4381a7876385592a74d8bc1dbade2725e03a`.

No repository search, recursive tree walk, historical artifact scan, Lane-D payload read, terminal residual read, or external derivation is permitted in this audit.

## Required object-definition controls

A scoped PASS requires all of the following to be explicitly present in the frozen audit inputs, without inference from the mismatch:

1. an explicit curvature-dependent mathematical definition of `P^{abcd}` sufficient to distinguish it from an abstract pair-symmetric tensor;
2. an explicit first-derivative/jet rule for `partial_e P^{abcd}` (or an exactly equivalent covariant/normal-coordinate rule) sufficient to construct the `DP` channel;
3. the index symmetries and source dependence needed to canonicalize that derivative sector without introducing a new free coefficient, normalization, permutation, Hamiltonian, clock, update rule, or source normalization;
4. no use of the observed Lane-D residual to choose any sign, coefficient, contraction, or derivative term.

The statements `ordinary derivatives of abstract P vanish for this source class` and `DP=0` are source-class restrictions, not a curvature-dependent `P`-jet definition, and therefore do not satisfy controls 1–2.

## Frozen terminal taxonomy

- `PASS_SCOPED_CURVATURE_P_JET_OBJECT_ALREADY_DEFINED`
- `BLOCKED_MISSING_CURVATURE_P_JET_OBJECT_DEFINITION`
- `INVALID_SCOPE_DRIFT`

`PASS_SCOPED_CURVATURE_P_JET_OBJECT_ALREADY_DEFINED` is allowed only if all four controls are satisfied entirely inside the two frozen files.

`BLOCKED_MISSING_CURVATURE_P_JET_OBJECT_DEFINITION` is mandatory if either the curvature dependence of `P` or its derivative/jet rule is absent. A missing required object is a valid terminal BLOCKED result and must not be repaired by invention.

`INVALID_SCOPE_DRIFT` is mandatory if classification would require inspecting any non-frozen file, residual payload, external source, or adding a new assumption.

## Interpretation ceiling

This audit can only determine whether the current authoritative covariant source definitions already contain the object needed for a future nonzero-`DP` gate. A PASS would authorize only a separately preregistered computation. A BLOCKED result means the covariant branch cannot proceed from the current two source definitions alone; a future continuation would need an independently preregistered derivation from an exact curvature-dependent `P` definition, otherwise the programme should pivot to quantum amplitude/measure closure as directed by `CURRENT_FRONT`.

Historical FAIL/BLOCKED remain immutable. No historical reclassification is authorized. `c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `beta=1` unauthorized; finite certificate != theorem; classical != quantum; diagnostic != closure; `theory_established=0%`.
