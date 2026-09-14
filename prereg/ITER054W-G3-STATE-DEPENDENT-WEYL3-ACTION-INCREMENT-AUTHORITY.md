# Iter054W Preregistration — G3 State-Dependent Weyl3 Action-Increment Authority Audit

Date: 2026-09-14
Gate: `ITER054W-G3-STATE-DEPENDENT-WEYL3-ACTION-INCREMENT-AUTHORITY`
Status at freeze: **PREREGISTERED BEFORE TARGETED SOURCE/CODE AUDIT**

## TARGET HYPOTHESIS

Determine whether pre-existing QGR authority already defines a source-faithful state-dependent Weyl3 action increment

`Delta S_W3(x,d)`

or an exactly equivalent edge/cell/step functional on the G3 Weyl-active realization, sufficient to accumulate distinct branch responses along the 24 explicit permutation histories without inventing a new quadrature, measure, source profile, cell assignment, or history weight.

Iter054V proves that order-blind event-attached summation cannot resolve the histories. Iter054W therefore requires genuine intermediate-state/path dependence from pre-existing authority.

## EXACT OBJECT

Use only objects existing before this preregistration:

- G3 intermediate vertices `x in {0,1}^4` and directions `d in {0,1,2,3}`;
- the existing G3 tetrad/metric/connection data and 24 permutation histories;
- the established Weyl-active curvature/Weyl3 density machinery;
- the pre-existing QGR local action / source authority;
- G8A branch composition `K_alpha = 24^(-1/2) exp(i S_alpha/hbar) U_alpha`.

No new discretization convention may be introduced by this gate.

## DEPENDENCY BEING TESTED

Current missing arrow after Iter054U/V:

`G3 intermediate state/path/order + physical source/boundary data -> history-sensitive Weyl3 action increment -> dS_alpha/dc6`.

## FROZEN OBLIGATIONS

### A — intermediate-state object

The candidate rule must be evaluable on a specified pre-step or cell state `x` and direction/edge/cell label `d` using already-defined G3 data. A common background scalar independent of `x,d` is insufficient.

### B — Weyl3 action-density identity

The rule must use the actual pre-existing Weyl3 action contribution or its `c6` derivative, not an unrelated transport/holonomy proxy.

### C — measure / cell / domain authority

Pre-existing QGR authority must specify the measure, cell volume, integration domain, edge/cell assignment, or equivalent object that converts local Weyl3 density into an action increment. Merely having `Weyl^3(x)` values does not satisfy C.

### D — sequential composition authority

The increments must compose under the already established local-action/history rule into an `S_alpha` or `dS_alpha/dc6` for a complete four-step history. The rule must be compatible with G8A action-phase addition on concatenated histories.

### E — source/boundary normalization

Any physical source/boundary insertion required by the action increment must be already specified, or an exact differential/relative argument must remove the unresolved scale without setting `beta=1`. A symbolic placeholder is insufficient.

### F — branch resolution

The pre-existing rule must be capable of producing different responses for at least two explicit histories because of genuine intermediate-state/path/order dependence. An order-blind event-attached sum is excluded by Iter054V.

## POSITIVE CONTROLS

- G3 explicitly defines intermediate lattice states and state-dependent connection matrices `sols[x][d]`.
- G3 is Weyl-active.
- G4 supplies nonzero background Weyl3 `c6` sensitivity.
- G8A authorizes additive action phases on concatenated histories.

These controls show the audit is meaningful but do not satisfy A–F by themselves.

## NEGATIVE CONTROLS

Reject as sufficient:

- a common G4 scalar copied to all histories;
- raw `Weyl^3(x)` values with no authorized measure/cell assignment;
- transport matrix `U_alpha` used as if it were an action phase;
- new midpoint/trapezoid/path quadrature invented in this gate;
- synthetic cell volumes or history weights;
- setting `beta=1`;
- an order-blind event-attached sum;
- a rule that depends on outputs selected after the audit.

## PASS

PASS only if all A–F are closed from pre-existing authority.

Classification:

`PASS_SCOPED_ITER054W_PREEXISTING_G3_STATE_DEPENDENT_WEYL3_ACTION_INCREMENT_DEFINED__C6_STILL_UNFIXED`

## BLOCKED

BLOCKED if G3 state/path data and Weyl3 density exist but at least one of measure/cell assignment, sequential action increment, source/boundary normalization, or branch-resolving state dependence is missing.

Classification:

`BLOCKED_MISSING_REQUIRED_OBJECT_ITER054W_NO_AUTHORIZED_G3_STATE_DEPENDENT_WEYL3_ACTION_INCREMENT`

The result must list exactly which obligations A–F are open.

## INVALID

INVALID for incomplete targeted audit, provenance mismatch, use of post-prereg invented discretization, or misidentification of transport data as action data.

## INTERPRETATION CEILING

Even PASS would establish only a scoped state-dependent branch-action construction on the existing G3 realization. It would not fix `c6`, authorize `beta=1`, establish regulator removal/global measure, exact-vs-order-reduced treatment, strong hyperbolicity, unitarity, UV completion, full GR recovery, experiment, new physics, or theory correctness. Theory established remains 0%.