# Iter054N Preregistration — Torsion Coarea/Jacobian Weyl3 Datum Audit

Date: 2026-09-14
Gate: `ITER054N-TORSION-COAREA-JACOBIAN-WEYL3-DATUM-AUDIT`
Parent blocker: terminal Iter054M `BLOCKED_OBJECT_DEFINITION_ITER054M_QUANTUM_MEASURE_CLOSURE_INCOMPLETE`.

## Objective

Test the strongest existing internal candidate for the missing nonhomogeneous microscopic `c6` datum: the regular-stratum torsion coarea/Jacobian factor already derived in Iter006 and identified for follow-up in Iter011.

## Frozen scientific questions

1. On the already-established same-field-content Weyl-active finite-cell background, does `Delta log|det J_T|` have a stable refinement asymptotic expansion relative to the flat/reference determinant?
2. Does the leading nontrivial curvature dependence contain a cubic/Weyl3-sensitive component with the expected tidal-amplitude parity/power and a controlled cell-size scaling?
3. Is the contribution canonically normalized by the already-fixed torsion/coarea construction, or does any free multiplicative/penalty coefficient enter?
4. Does current QGR authority derive a same-realization map from the positive real coarea weight to the coherent Lorentzian phase `exp(iS/hbar)`?
5. If such a map exists, does it nonhomogeneously lift the free `c6` phase direction? If no map exists, the measure datum and phase coefficient remain distinct.

## Frozen interpretation rules

- Curvature dependence alone is not a `c6` match.
- A positive real factor `|det J_T|^{-1}` or `-log|det J_T|` is not automatically a Lorentzian action phase.
- No arbitrary torsion penalty strength may be introduced.
- No external continuum loop/EFT coefficient may be imported as the target.
- `beta=1` remains unauthorized.
- `c6` remains symbolic/unfixed unless a same-realization nonhomogeneous phase identity is actually derived.
- Finite-cell fits require prospective refinement and amplitude controls; no post-hoc power selection.

## Frozen controls

Where the existing implementation supports them, use:

- flat/conformally-flat control where continuum Weyl3 vanishes;
- Weyl-active positive controls from the established same-field-content tidal background;
- multiple frozen cell sizes sufficient to distinguish leading powers;
- sign-reversed tidal amplitude to separate even versus odd/cubic response;
- a deliberately rescaled Jacobian-weight-to-phase map as a negative control: if such a rescaling is equally admissible under current authority, absolute `c6` matching is not authorized.

## Terminal classifications

- `PASS_SCOPED_ITER054N_CANONICAL_NONHOMOGENEOUS_WEYL3_PHASE_DATUM_DERIVED` only if all five scientific questions close prospectively, including an explicit same-realization map into coherent phase and lifting of the `c6` null direction.
- `PASS_SCOPED_ITER054N_WEYL3_SENSITIVE_MEASURE_DATUM_ONLY__C6_PHASE_MATCH_BLOCKED` if a controlled Weyl3-sensitive coarea/Jacobian datum exists but no canonical phase map is derived.
- `BLOCKED_OBJECT_DEFINITION_ITER054N_NO_CONTROLLED_WEYL3_SENSITIVE_COAREA_DATUM` if the existing construction does not supply a controlled relevant datum.
- `INVALID_ITER054N` only for implementation/provenance/control failure.

No outcome establishes QGR correctness, unitarity, UV completion, experimental confirmation, strong hyperbolicity, a full global quantum measure, or KMQGB `NEW_REQUIRED`.
