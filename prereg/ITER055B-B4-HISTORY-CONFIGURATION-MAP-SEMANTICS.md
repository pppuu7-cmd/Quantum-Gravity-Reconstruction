# Iter055B Preregistration — B4 History Configuration-Map Semantics

Date: 2026-09-14
Gate: `ITER055B-B4-HISTORY-CONFIGURATION-MAP-SEMANTICS`
Status at freeze: **PREREGISTERED BEFORE TARGETED HISTORY/REFINEMENT AUDIT**

## TARGET HYPOTHESIS

Determine whether the pre-existing B4/QGR refinement-history construction itself canonically defines, for each of the 24 maximal histories, an invertible map on a fixed finite configuration space

`F_alpha : X -> X`,

or whether the history instead denotes one of the following structurally different objects:

1. a sequence of refinement/extension maps between different graph/configuration spaces;
2. a restriction/coarse-graining map that loses fine data;
3. a permutation/relabeling of the same primitive events;
4. a path/transport inside one already-given configuration;
5. a combination of these without a canonical invertible endomorphism.

The gate does not invent a new history dynamics.

## DEPENDENCY

Iter055A established that G8A's unitary branch operator requires an invertible quasi-invariant configuration map, while G3/G7B/Iter054S currently provide geometric/path transport data. Iter055B tests whether the missing `F_alpha` was already implicit in the B4 history/refinement semantics.

## EXACT OBJECT

Audit only pre-existing authority for:

- B4 primitive refinement/event operations;
- the 24 maximal ordering histories;
- configuration spaces before/after each primitive step;
- restriction/extension/blocking maps;
- path-groupoid composition;
- history normalization and symmetry;
- G10/G10B/G38 refinement structures where relevant.

Use G7B's finite configuration object `X_Gamma` as the configuration-space reference whenever the historical operation is defined there.

## FROZEN OBLIGATIONS

### A — primitive operation identity

Identify the exact mathematical operation corresponding to one primitive B4 history step.

### B — domain/codomain identity

For every step, determine whether domain and codomain are the same configuration space or different graph/refinement levels.

### C — invertibility

If a history is claimed to define `F_alpha:X->X`, invertibility must be established from existing authority. A restriction/coarse map with a nontrivial information kernel is not invertible.

### D — full-configuration action

The map must act on the complete QGR configuration object required by G7B/G8A, not only on an event label, one tangent vector, one edge transport, or one observable.

### E — branch distinction

The 24 maps must be meaningfully history distinguished. If all 24 differ only by relabeling of an auxiliary ordering basis while inducing the same physical configuration map, record that explicitly.

### F — composition

The sequential history composition law must define the complete maximal-history map without post-hoc interpolation/extension choices.

### G — fixed-domain requirement for Koopman lift

If the historical object maps between different configuration spaces `X_Gamma -> X_Gamma'`, determine whether pre-existing authority supplies a canonical identification with one fixed measured space suitable for a unitary Koopman/RN endomorphism. Do not add one in this gate.

## POSITIVE CONTROLS

- G7B gives exact path-groupoid composition and exact blocking for finite transports.
- G10/G10B and G38 give scoped refinement/restriction/blocking structures.
- B4 has 24 exact maximal ordering histories and fixed normalization.

## NEGATIVE CONTROLS

Reject as a G8A configuration map:

- a mere permutation label with no action on full configurations;
- a 4x4 tangent/frame path transport;
- a many-to-one restriction/coarse-graining map called unitary;
- a refinement embedding that requires arbitrary fine data to invert;
- an endpoint identification that forgets intermediate/loop data;
- a post-hoc interpolation, section, or extension rule introduced only to make the map invertible.

## PASS

PASS only if A-G establish a canonical invertible history map on one fixed configuration domain from pre-existing authority.

Classification:

`PASS_SCOPED_ITER055B_B4_HISTORY_CANONICALLY_DEFINES_INVERTIBLE_CONFIGURATION_MAP__KOOPMAN_QUASI_INVARIANCE_AUDIT_AUTHORIZED`

## BLOCKED

If the B4 histories are well-defined but their mathematical operation is refinement/restriction/path transport/relabeling without a canonical invertible full-configuration endomorphism, classify:

`BLOCKED_OBJECT_DEFINITION_ITER055B_B4_HISTORY_DOES_NOT_YET_DEFINE_G8A_CONFIGURATION_ENDOMORPHISM`

The terminal result must state exactly what the history object *is* and what additional map is missing.

## FAIL

Scientific FAIL requires contradictory simultaneously authoritative history-map definitions, not mere absence.

`SCIENTIFIC_FAIL_ITER055B_INCONSISTENT_B4_HISTORY_MAP_SEMANTICS`.

## INVALID

INVALID for incomplete source audit, conflating path transport with configuration dynamics, or importing an unregistered extension/section/interpolation rule.

## INTERPRETATION CEILING

Even PASS would not prove quasi-invariance, define the RN derivative, establish the G8A unitary channel, regulator removal, unitarity, UV completion, fix `c6`, authorize `beta=1`, or establish QGR correctness. It would only close the configuration-map identity needed for the next measure/unitary gate.

Theory established remains 0%.