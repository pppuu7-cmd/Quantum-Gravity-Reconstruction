# Iter054X Preregistration — Primitive Finite-Cell Lorentzian Action Authority Audit

Date: 2026-09-14
Gate: `ITER054X-PRIMITIVE-FINITE-CELL-LORENTZIAN-ACTION-AUTHORITY`
Status at freeze: **PREREGISTERED BEFORE TARGETED AUTHORITY AUDIT**

## TARGET HYPOTHESIS

Determine whether the current QGR-L1 candidate is already defined by one canonical microscopic finite-cell Lorentzian action functional (or mathematically equivalent generator) sufficient to derive the branch phases `S_alpha` used in

`K_alpha = 24^(-1/2) exp(i S_alpha/hbar) U_alpha`,

including the current six-derivative Weyl3 direction, rather than merely specifying lower-order dynamics plus a symbolic higher-derivative continuum operator.

This is a candidate-definition audit. It does not ask whether a future extension could define such an action.

## EXACT OBJECT

The target object must be a pre-existing QGR functional/rule

`S_micro[history; microscopic variables; source/boundary data]`

or an exact equivalent composition of finite-cell increments, with enough information to evaluate a concrete history in the already-defined microscopic arena.

The audit must include all relevant pre-existing authority, especially:

- QGR-L1 second-moment / connection variables;
- Iter005 exact connection-density / Noether construction;
- Iter008 frozen action normalization and coordinate-cell convention;
- G8A branch/action-phase composition;
- Iter009/010 Weyl3 operator and `c6` identifiability results;
- Iter010 microscopic-UV-action authority statements;
- G3 state/path realization;
- torsion/coarea measure authority;
- Iter054T-U-V-W source/action blockers.

## DEPENDENCY BEING TESTED

Mandatory chain segment:

`microscopic state/dynamics -> finite-cell action/generator -> concrete branch amplitude/phase -> quantum amplitude/measure`.

Without a defined action/generator, downstream quantum-amplitude claims are semantically incomplete.

## FROZEN OBLIGATIONS

### A — microscopic domain

The action must be defined on explicitly identified QGR microscopic variables/configurations/histories, not only on an emergent continuum metric.

### B — finite-cell/local rule

The action must provide a finite-cell/local density/increment or another exact microscopic prescription that can be evaluated before taking a continuum limit.

### C — Lorentzian phase identity

The same functional must be the object entering `exp(i S_alpha/hbar)` or there must be an explicit theorem/map identifying it with that branch phase. A positive real measure factor alone is insufficient.

### D — lower-order dynamics consistency

Variation/Noether/composition of the functional must reproduce or be explicitly identified with the already-authorized lower-order QGR dynamics/connection-density structure in the relevant scope.

### E — higher-derivative Weyl3 definition

The current Weyl3 direction must be supplied by an explicit microscopic finite-cell term/rule or derived from the same microscopic principle. A continuum operator shape plus free coefficient/sensitivity witness is insufficient.

### F — history/source composition

The functional must specify how source/boundary data and sequential microscopic steps combine into a concrete `S_alpha` for at least the existing G3/B4 history arena; abstract additivity without increments is insufficient.

### G — freedom accounting

All coefficients/functions introduced by the microscopic action must have an explicit status. The gate may not hide an arbitrary history-dependent function, set `beta=1`, fix `c6` by convention, or import an external target.

## POSITIVE CONTROLS

- Iter005 exact connection-density provides a genuine lower-order action construction and exact Noether closure.
- Iter008 fixes a scoped two-derivative normalization/cell convention.
- G8A supplies the semantic branch-phase composition rule.

These controls prevent the false conclusion that QGR has no action structure at all.

## NEGATIVE CONTROLS

Reject as full-object closure:

- transport matrices `U_alpha` used as phases;
- torsion/coarea positive measure used as Lorentzian action;
- synthetic `S2_alpha/S6_alpha` controls;
- continuum `Weyl^3` operator shape without a finite-cell microscopic rule;
- `h^4 Weyl^3` sensitivity witness with `a_cont/hbar=1` treated as a derived branch action;
- a newly invented path quadrature/cell assignment/source profile;
- `beta=1` or post-hoc `c6` fixing;
- lower-order connection density relabeled as a six-derivative UV completion.

## PASS

PASS only if A-G are all satisfied by pre-existing authority in one compatible realization.

Classification:

`PASS_SCOPED_ITER054X_CANONICAL_MICROSCOPIC_FINITE_CELL_LORENTZIAN_ACTION_DEFINED`

The result must still state any unresolved coefficient values and treatment selectors.

## BLOCKED

BLOCKED if a genuine lower-order action exists but the full current candidate lacks at least one mandatory object needed for its branch phases / Weyl3 extension / source-history composition.

Classification:

`BLOCKED_OBJECT_DEFINITION_ITER054X_MICROSCOPIC_ACTION_INCOMPLETE_FOR_CURRENT_QGR_L1`

The terminal note must distinguish exactly what is defined from what remains undefined.

## FAIL

A scientific FAIL requires an actual contradiction between two simultaneously authoritative definitions of the same action/generator, not mere absence of an object.

Classification:

`SCIENTIFIC_FAIL_ITER054X_INCONSISTENT_MICROSCOPIC_ACTION_DEFINITIONS`

## INVALID

INVALID for incomplete source audit, chronology/provenance mismatch, surrogate promotion, or changing the target after reading results.

## INTERPRETATION CEILING

Even PASS would establish only a microscopic-action definition in the audited realization. It would not by itself establish regulator removal/global measure, exact-vs-order-reduced treatment, strong hyperbolicity, unitarity, UV completion, full GR recovery, experiment, new physics, or theory correctness.

BLOCKED is not a theorem that no valid action can be constructed; it means the current candidate definition does not yet supply the mandatory object. Theory established remains 0%.