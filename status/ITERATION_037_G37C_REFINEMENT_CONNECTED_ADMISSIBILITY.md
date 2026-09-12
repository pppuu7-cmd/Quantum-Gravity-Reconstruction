# Iteration 037 G37C — frozen G10B refinement-connected same-realization admissibility audit

Date: 2026-09-12
Status: `PREREGISTERED / READY FOR PRODUCTION`

## Governance reason for this addendum

G35/G36 discovered and verified persistent **algebraic finite-cell** torsion branches. However, the
prospective G10B rule predates those discoveries and already fixes the physical finite connection as
the identity/refinement-connected branch satisfying

`L_e(h) = I + h omega_e[G,DG] + O(h^2)`

with the unique linearized torsion/Levi-Civita `omega`, and defines strong-curvature coarse transport
through products of fine principal transports.

Therefore the G37 deeper-h/radius stress is useful but cannot by itself promote distant algebraic
roots to multiple physical connection branches. G37C directly audits the same six G36 jointly
persistent witnesses against the older G10B same-realization criterion. The G10B criterion and the
thresholds below are frozen before G37C production and may not be relaxed after observing outcomes.

## Frozen seed set

Exactly the six G36 jointly persistent seed indices `[0,1,3,4,5,7]`. No substitution.

## Frozen cell-size sequence

At the physical origin continue each distant branch from `h=1` through the diagnostic targets

`h = [1/4, 1/8, 1/16, 1/32]`.

Continuation uses intermediate log-spaced steps and the preceding branch point as its only branch
seed. A solver failure is `BLOCKED_NUMERICALLY`, not evidence that the branch is absent.

At every target also solve the G10B principal branch independently from the identity/zero seed.

## Frozen G10B diagnostics

For each candidate target record:

1. `max_i ||L_i-I||` and its observed refinement order;
2. `||z(h)/h - omega_linear||`, where `omega_linear` is the unique 24-parameter linearized torsion solution used by G10B;
3. candidate/principal root distance (diagnostic only; not gauge-invariant);
4. invariant edge-transport fingerprint distance candidate versus principal;
5. residual and metric compatibility.

### Finite-sequence identity/first-order compatibility criterion

A distant branch is `G10B_FIRST_ORDER_COMPATIBLE_SCOPED` only if all target solves are valid and:

- the last two observed orders of `max ||L-I||` are each `> 0.8`;
- `max ||L-I|| / h` stays below `5` times the maximum corresponding principal-branch ratio on the same frozen grid;
- the candidate scaled-linearized error decreases over the final two refinements;
- final `h=1/32` scaled-linearized error `< 0.05`.

These finite thresholds are a numerical audit of the previously fixed asymptotic rule, not a proof of
an `O(h^2)` theorem.

## Actual fixed-physical-path fine-product audit

For the physical path `x:0 -> e0`, compute candidate and principal relational transports using
`N=[4,8,16,32]` equal subcells. At each candidate subcell, solve the finite torsion root starting only
from the previously tracked candidate root at the preceding subcell; principal cells use the identity
start as in G10B.

Let `A_N` be the ordered product of fine relational edge transports. Candidate path-product convergence
passes only if:

- every subcell solve has residual `<1e-8` and metric error `<1e-7`;
- successive candidate differences `||A_8-A_4||`, `||A_16-A_8||`, `||A_32-A_16||` decrease strictly;
- the final contraction ratio `||A_32-A_16|| / ||A_16-A_8|| < 0.75`.

This is the same physical-path product-limit logic used prospectively in G10B, now applied to each
distant witness. It is stronger than the G36 local shrinking-h proxy.

## Frozen per-seed classification

- `REFINEMENT_CONNECTED_MERGE_TO_PRINCIPAL_SCOPED` if first-order compatibility and path-product convergence both pass and, at `h=1/32`, candidate/principal root distance `<1e-6` and invariant edge-fingerprint distance `<1e-9`.
- `FINITE_RESOLUTION_REFINEMENT_CONNECTED_DISTINCT_CANDIDATE` if first-order compatibility and path-product convergence both pass but the merge thresholds above are not met. This does **not** establish a distinct continuum branch; it requires deeper/projective testing.
- `DISTANT_BRANCH_FAILS_G10B_SAME_REALIZATION_ADMISSIBILITY_SCOPED` if every required numerical solve is valid but either the frozen first-order criterion or path-product convergence criterion fails.
- `BLOCKED_NUMERICALLY` if required continuation/path solves are not residual/metric qualified; this is not evidence of physical inadmissibility.

## Aggregate classification

- if at least one seed is `FINITE_RESOLUTION_REFINEMENT_CONNECTED_DISTINCT_CANDIDATE`:
  `PARTIAL_SCOPED_PHYSICALLY_ADMISSIBLE_DISTINCT_CANDIDATE_REQUIRES_DEEPER_PROJECTIVE_LIMIT`;
- else if no seed is blocked and every seed is either merge or fail:
  `SCOPED_EVIDENCE_G35_G36_DISTANT_ROOTS_DO_NOT_YET_SUPPLY_ADDITIONAL_PHYSICAL_CONNECTION_BRANCHES_UNDER_FROZEN_G10B`;
- otherwise:
  `PARTIAL_BLOCKED_G10B_ADMISSIBILITY_AUDIT`.

## Claim locks

- finite-sequence scaling is not an analytic asymptotic proof;
- a finite-resolution distinct candidate is not a proven distinct continuum branch;
- G10B criteria cannot be weakened post hoc to preserve multiplicity;
- solver nonconvergence is not proof of root absence or inadmissibility;
- G35/G36 remain valid algebraic finite-cell branch results regardless of G37C physical classification;
- no physical branch probabilities are authorized unless multiple same-realization admissible branches survive;
- theory established remains `0%`;
- `beta` and `c6` remain unfixed;
- KMQGB `NEW_REQUIRED` remains unauthorized absent benchmark authority.
