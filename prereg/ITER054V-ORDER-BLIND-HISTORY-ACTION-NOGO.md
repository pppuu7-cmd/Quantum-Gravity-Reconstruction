# Iter054V Preregistration — Order-Blind History-Action Accumulation No-Go

Date: 2026-09-14
Gate: `ITER054V-ORDER-BLIND-HISTORY-ACTION-NOGO`
Status at freeze: **PREREGISTERED BEFORE STRUCTURAL RESULT**

## TARGET HYPOTHESIS

Test whether the 24 explicit G3/B4 permutation histories can acquire distinct Weyl3 action responses from an order-blind event-attached additive accumulation rule.

The prospective hypothesis is:

> Any additive history-response rule whose contribution is attached only to each of the four event/direction identities and is independent of the intermediate configuration, step position, history label, ordering context, pair/commutator data, and future/past steps is exactly permutation invariant across all 24 histories. Therefore such a rule cannot supply branch-resolved `dS_alpha/dc6`.

This is a structural class no-go, not a claim that the unknown physical QGR Weyl3 action must belong to this class.

## EXACT OBJECT

Use the existing G3/B4 history set

`PERMS = permutations({0,1,2,3})`,

so every maximal history contains each event/direction exactly once.

Use the G8A branch structure

`K_alpha = 24^(-1/2) exp(i S_alpha / hbar) U_alpha`.

Define the frozen **order-blind event-attached additive class** `C_OB` by

`D_p = sum_{r=1}^4 a_{p_r}`

for every history `p=(p_1,p_2,p_3,p_4)`, where each `a_d` may be an arbitrary scalar or operator-valued quantity attached to event/direction identity `d`, but it may not depend on:

- the intermediate occupancy/configuration before the step;
- the step position `r`;
- the complete history label `p`;
- previously or subsequently applied directions;
- ordered pairs/commutators/nonlocal cross-terms;
- a history-specific source weight or measure.

For the Weyl3 question, `D_p` is interpreted only schematically as a candidate branch response such as `dS_p/dc6`; no physical values are assigned.

## DEPENDENCY BEING TESTED

Iter054U established that the missing object is an authorized history-resolved Weyl3 action accumulation rule. Iter054V asks which minimal structural dependence is mathematically necessary for branch resolution.

## FROZEN INPUTS

1. `PERMS=list(itertools.permutations(range(4)))` from the existing QGR history implementation.
2. G8A's 24 symmetry-equivalent maximal ordering histories and equal branch amplitude magnitude.
3. No physical `S_alpha`, `beta`, `c6`, quadrature, cell weight, source profile, or measure is introduced.

## POSITIVE CONTROL

For arbitrary formal event-attached weights `(a0,a1,a2,a3)`, prove exactly that every permutation has

`D_p = a0+a1+a2+a3`.

An optional concrete witness `(2,3,5,7)` must give `17` for all 24 permutations, but the scientific result must rest on the exact proof, not the finite witness.

## NEGATIVE / SCOPE CONTROL

Use a state-dependent sequential rule outside `C_OB` to prove that additive composition in general need not be permutation invariant.

Let the intermediate occupancy state be `x in {0,1}^4`, initially zero. For a step in direction `d`, define

`f(x,d)=x_0` if `d=1`, and `0` otherwise,

then update the corresponding occupancy bit after the contribution is evaluated.

The histories `(0,1,2,3)` and `(1,0,2,3)` must give different totals. This control prevents overclaim from `C_OB` to all local/state-dependent action rules.

## PASS

PASS only if:

1. exact permutation invariance is proved for the entire frozen class `C_OB`;
2. all 24 histories contain exactly the same event multiset;
3. the state-dependent sequential negative control distinguishes at least two histories;
4. the conclusion is limited to: branch-resolved action requires structure outside `C_OB`, such as intermediate-state/path dependence, explicit ordering dependence, or nonlocal/cross-term/source dependence.

Classification:

`PASS_SCOPED_ITER054V_ORDER_BLIND_EVENT_ATTACHED_ADDITIVE_ACTION_CANNOT_RESOLVE_G3_HISTORIES`

## FAIL

FAIL if two frozen histories in `C_OB` can have unequal `D_p` without violating the class definition.

Classification:

`SCIENTIFIC_FAIL_ITER054V_ORDER_BLIND_PERMUTATION_INVARIANCE`

## BLOCKED

BLOCKED if the repository history set cannot be verified to be the 24 permutations of the same four event identities.

Classification:

`BLOCKED_OBJECT_DEFINITION_ITER054V_HISTORY_MULTISET_IDENTITY_NOT_ESTABLISHED`

## INVALID

INVALID for chronology/provenance/object mismatch or if the negative control is accidentally inside `C_OB`.

## INTERPRETATION CEILING

Even PASS does not define the physical QGR branch action, does not authorize a particular state-dependent/path-dependent rule, does not assign `S_alpha` or `dS_alpha/dc6`, does not set `beta=1`, does not fix `c6`, and does not establish a global measure, regulator removal, strong hyperbolicity, unitarity, UV completion, full GR recovery, experiment, new physics, or theory correctness.

A PASS only narrows the missing object: any physically branch-resolving accumulation must contain prospectively justified order/state/path/nonlocal information beyond order-blind event-attached summation.