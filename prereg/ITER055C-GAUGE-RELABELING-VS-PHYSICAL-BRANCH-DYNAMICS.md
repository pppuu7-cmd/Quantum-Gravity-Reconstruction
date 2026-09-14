# Iter055C Preregistration — Gauge/Relabeling Maps versus Physical Branch Dynamics

Date: 2026-09-14
Gate: `ITER055C-GAUGE-RELABELING-VS-PHYSICAL-BRANCH-DYNAMICS`
Status at freeze: **PREREGISTERED BEFORE TARGETED COVARIANCE/BRST AUDIT**

## TARGET HYPOTHESIS

Test the most obvious existing-map rescue of the Iter055A/B blocker:

> QGR may already possess canonical invertible actions on the full finite configuration object through local frame/gauge transformations, graph/event relabelings, or relational covariance maps. Determine whether any such pre-existing map can be identified with the 24 B4 history maps required by G8A, and whether it remains a physically distinct branch dynamics after QGR constraint/BRST descent.

The gate is counterexample-first: an invertible/unitarily implementable map that is pure gauge on the physical quotient does **not** count as physical history dynamics.

## EXACT OBJECT

Audit only pre-existing authority for:

- the finite G7B configuration object `X_Gamma={(G_v,A_e)}`;
- local frame/Lorentz/gauge transformations of `G_v`, `A_e`, frame variables and source/response data;
- graph/event/S4/B4 relabeling actions where explicitly defined;
- QGR constraint equivalence relation `R_g` and G8C BRST/constraint descent;
- G8D physical quotient/operational channel semantics;
- any relational event-update map that changes the physical configuration rather than only its representation.

No new branch transformation may be invented.

## FROZEN OBLIGATIONS

### A — full-configuration map

A candidate rescue map must act on the complete finite configuration object required by G7B/G8A, not only on tangent vectors or labels.

### B — canonical invertibility

The action must be invertible on one fixed domain from pre-existing authority.

### C — B4-history identification

There must be an explicit authority map from the 24 maximal B4 histories `alpha` to 24 candidate transformations. Similar cardinality, S4 covariance, or notation is insufficient.

### D — physical quotient test

Determine whether the candidate action is part of the QGR gauge/constraint equivalence relation. If physical states/observables identify `x` and `g.x`, then the transformation is representation redundancy rather than distinct branch dynamics unless a separate relational observable makes the branch action physical.

### E — branch distinction after quotient

At least two B4 branches must act differently on a physical/gauge-invariant observable or physical state if the map is to count as branch dynamics. Difference only in frame components, gauge labels, or basis convention is insufficient.

### F — measure/unitary relevance

If the map is invertible and measure/quasi-invariance authority exists, record that it may admit a Koopman/RN unitary. But unitary implementability alone does not override D/E.

### G — non-gauge event-update census

Search existing QGR authority for a canonical invertible full-configuration event-update map independent of gauge/relabeling. If one exists, distinguish it sharply from the gauge action and test whether B4 histories are actually its compositions.

## POSITIVE CONTROLS

- QGR has exact covariance/frame compatibility structures.
- G8A explicitly formulates a constraint-descent criterion `U_alpha R_g = R_(phi_alpha(g)) U_alpha`.
- G8C/G8D contain physical quotient/descent semantics that can distinguish kinematic maps from physical dynamics.

## NEGATIVE CONTROLS

Reject as physical branch dynamics:

- a local Lorentz/frame change that leaves all gauge-invariant observables unchanged;
- a graph relabeling/permutation with no relationally fixed labels;
- a basis transformation of the history register;
- an invertible map identified with B4 histories only because both are indexed by permutations;
- a BRST-exact/gauge-equivalent transformation;
- a 4x4 fiber map acting only on tensor components;
- a new relational clock/event update introduced after seeing the audit.

## PASS — non-gauge dynamics found

If a pre-existing canonical full-configuration map exists, is explicitly identified with B4 histories, and remains physically distinct after quotient, classify:

`PASS_SCOPED_ITER055C_EXISTING_NON_GAUGE_FULL_CONFIGURATION_HISTORY_DYNAMICS_FOUND__KOOPMAN_GATE_ADVANCED`

## PASS — gauge rescue ruled out

If exact full-configuration gauge/relabeling maps exist but are physically redundant after the existing quotient/descent and no pre-existing non-gauge B4 event-update map is found, classify:

`PASS_SCOPED_ITER055C_GAUGE_RELABELING_MAPS_CANNOT_REALIZE_PHYSICAL_B4_BRANCH_DYNAMICS`

This is a structural no-go for the gauge/relabeling rescue, not a proof that no future physical dynamics map can be defined.

## BLOCKED

If existing covariance/constraint authority is insufficient to decide whether the candidate maps are pure gauge or physically distinct, classify:

`BLOCKED_OBJECT_DEFINITION_ITER055C_PHYSICAL_STATUS_OF_FULL_CONFIGURATION_RELABELLING_MAPS_NOT_FIXED`.

## FAIL

A scientific FAIL requires an exact contradiction among simultaneous authoritative definitions of gauge equivalence and branch dynamics.

`SCIENTIFIC_FAIL_ITER055C_GAUGE_AND_BRANCH_DYNAMICS_DEFINITIONS_CONTRADICT`.

## INVALID

INVALID for importing a new transformation, identifying B4 histories with gauge maps post hoc, omitting physical-quotient checks, or equating kinematic invertibility with physical distinction.

## INTERPRETATION CEILING

Even a non-gauge PASS would only authorize the next quasi-invariance/Koopman-unitary audit. A gauge-rescue no-go PASS would only narrow the missing object to a genuinely physical configuration update law. Neither result establishes regulator removal, quantum unitarity, UV completion, fixes `c6`, authorizes `beta=1`, establishes GR recovery, experiment, new physics, or QGR correctness.

Theory established remains `0%`.