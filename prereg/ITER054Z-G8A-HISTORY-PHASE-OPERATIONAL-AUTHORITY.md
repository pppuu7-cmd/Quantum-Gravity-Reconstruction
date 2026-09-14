# Iter054Z Preregistration — G8A History-Phase Operational Authority

Date: 2026-09-14
Gate: `ITER054Z-G8A-HISTORY-PHASE-OPERATIONAL-AUTHORITY`
Status at freeze: **PREREGISTERED BEFORE TARGETED G8A/DOWNSTREAM AUTHORITY AUDIT**

## TARGET HYPOTHESIS

Determine the operational role of the unresolved history phases `S_alpha` in the **quantum object already defined by current QGR authority**.

The gate distinguishes:

1. **Kraus/instrument phase gauge:** if QGR defines only outcome CP maps and/or an unobserved channel built from `K_alpha rho K_alpha^dagger`, independent rephasings `K_alpha -> exp(i theta_alpha) K_alpha` leave the defined object invariant;
2. **physical coherent history phases:** if current authority defines coherent recombination/cross-history observables containing `K_alpha rho K_beta^dagger` with `alpha != beta`, a coherent sum `sum_alpha K_alpha`, or another phase-sensitive interference object, relative `S_alpha-S_beta` are operational data.

No hypothetical future interpretation may be imported.

## EXACT OBJECT

Audit pre-existing authority only, especially:

- G8A history branch/instrument definition;
- any G8B/G9/G10 or later quantum-composition object that consumes the G8A branches;
- branch probabilities, outcome maps, unobserved channels, sequential composition and gluing rules;
- any explicitly defined coherent cross-history observable/amplitude.

Use the existing branch form

`K_alpha = 24^(-1/2) exp(i S_alpha/hbar) U_alpha`.

## FROZEN OBLIGATIONS

### A — quantum-object identity

Identify whether each authoritative use of the G8A branches is an instrument/Kraus family, a channel, a coherent amplitude sum, or another object. Do not infer semantics from notation alone.

### B — exact rephasing test

For every instrument/channel object of the form

`I_alpha(rho)=K_alpha rho K_alpha^dagger`

or

`E(rho)=sum_alpha K_alpha rho K_alpha^dagger`,

prove algebraically whether arbitrary independent branch phases cancel.

### C — sequential-history composition

Check whether the existing multilevel/history composition rule preserves the same rephasing gauge for complete history CP maps, or whether current authority recombines branches coherently at a later step.

### D — cross-history interference census

Search existing authority for any term/object containing phase-sensitive `alpha != beta` interference, such as

`K_alpha rho K_beta^dagger`, `sum_alpha K_alpha` before forming a CP map, an off-diagonal history density matrix, decoherence functional, coherent boundary amplitude, or equivalent.

### E — observable/normalization effect

Determine whether the unresolved phases affect any currently authorized branch probability, normalized channel, composition/gluing identity, or observable. Distinguish common phase gauge from independent per-branch Kraus rephasing.

### F — scope consistency with action-phase research

Earlier G25-G32 and Iter054T-Y may legitimately study action phases as prospective physical data. This gate may only downgrade their **upstream necessity for the currently defined quantum object** if exact rephasing invariance is established. It must not rewrite those historical results.

## POSITIVE CONTROL — Kraus gauge

For arbitrary operator `U_alpha`, density matrix `rho`, real `theta_alpha`, and positive branch modulus `c`, verify exactly:

`(c e^{i theta_alpha} U_alpha) rho (c e^{i theta_alpha} U_alpha)^dagger = c^2 U_alpha rho U_alpha^dagger`.

The scientific result must rely on algebra and source semantics, not a finite numerical sample.

## NEGATIVE CONTROL — coherent interference

For two nonzero branches with a coherent sum `A=K_1+K_2`, show that

`A rho A^dagger`

contains cross terms and generically changes under an independent relative rephasing of `K_2`. This control prevents promotion of Kraus gauge to all conceivable coherent-history constructions.

## PASS — operational Kraus gauge

If current QGR authority defines only instrument/channel uses of the branch family in the audited quantum layer and no authoritative cross-history coherent object is found, classify:

`PASS_SCOPED_ITER054Z_G8A_HISTORY_PHASES_ARE_KRAUS_REPHASING_GAUGE_FOR_CURRENT_DEFINED_INSTRUMENT_CHANNEL`

Scientific consequence: unresolved `S_alpha` is **not an upstream blocker for that defined CP instrument/channel**, although it remains unresolved action data for any future coherent-history/absolute-phase extension.

## PASS — physical coherent phases

If an authoritative current object explicitly contains cross-history coherent interference and requires relative phases, classify:

`PASS_SCOPED_ITER054Z_CURRENT_QGR_CONTAINS_PHASE_SENSITIVE_CROSS_HISTORY_INTERFERENCE__S_ALPHA_SOURCE_REALIZATION_REQUIRED`

The terminal result must name the exact object and source authority.

## BLOCKED

If repository authority is internally ambiguous about whether the branch alternatives are coherently or incoherently combined, classify:

`BLOCKED_OBJECT_DEFINITION_ITER054Z_G8A_HISTORY_COHERENCE_SEMANTICS_NOT_FIXED`.

## FAIL

Scientific FAIL requires an exact contradiction between simultaneously authoritative quantum-object definitions, not mere missing prose.

`SCIENTIFIC_FAIL_ITER054Z_INCONSISTENT_G8A_HISTORY_COMBINATION_RULES`.

## INVALID

INVALID for importing a hypothetical future path integral/coherent sum, ignoring an existing cross-history object, or conflating phase gauge of a CP map with phase gauge of an amplitude.

## INTERPRETATION CEILING

A Kraus-gauge PASS would not derive `S_alpha`, fix `beta` or `c6`, prove quantum unitarity, establish a global interacting measure, regulator removal, UV completion, GR recovery, experiment, new physics, or theory correctness. It would only remove unresolved branch phase from the dependency list of the specifically audited CP instrument/channel.

A coherent-phase PASS would not prove that the missing source/action map can be constructed; it would only establish that the map is operationally required.

Theory established remains `0%`.