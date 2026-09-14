# Iter055A Preregistration — G3 to G8A Koopman/Channel Bridge Authority

Date: 2026-09-14
Gate: `ITER055A-G3-TO-G8A-KOOPMAN-CHANNEL-BRIDGE-AUTHORITY`
Status at freeze: **PREREGISTERED BEFORE TARGETED AUTHORITY AUDIT**

## TARGET HYPOTHESIS

Determine whether pre-existing QGR authority already derives, in the same Weyl-active G3/B4 realization, the complete bridge

`G3/B4 history alpha -> invertible configuration map F_alpha -> quasi-invariant configuration measure -> unitary Koopman/Radon-Nikodym operator U_alpha -> G8A branch CP map`,

so that the phase-free coarse CPTP channel can be constructed without substituting the 4x4 geometric transport matrices for Hilbert-space operators.

## MOTIVATION

Iter054Z proves that unresolved branch action phases cancel exactly from the already-defined coarse CP channel. This potentially removes a large source/action blocker from the coarse quantum layer.

However, Iter054S computes 4x4 Lorentz/metric-compatible path transports on the G3 Weyl-active tidal realization, while G8A's `U_alpha` is an operator on a kinematic configuration Hilbert space induced by a finite configuration map. These are not the same object by notation alone.

## EXACT OBJECT

Use only pre-existing authority:

- the G3 Weyl-active finite state/connection/path realization;
- the B4 24 ordering histories;
- G8A's exact normalized history instrument;
- the pre-existing QGR configuration space / kinematic measure / Hilbert construction;
- finite path/groupoid/refinement maps already derived in G6/G7/G10 or successors;
- Iter054S geometric fine-to-coarse blocking.

No new finite-dimensional surrogate Hilbert space may be introduced.

## FROZEN OBLIGATIONS

### A — same-realization configuration space

Identify an explicit configuration space `X_G3` containing the G3 microscopic variables on which each of the 24 histories acts. The map may not live only on tangent/frame indices if G8A requires a configuration transformation.

### B — history map

For each relevant history alpha, pre-existing authority must specify an invertible measurable map

`F_alpha : X_G3 -> X_G3`

or an exactly equivalent map between explicitly identified source/target configuration sectors.

The 4x4 matrix product acting on frame/tensor components is insufficient unless an existing theorem derives the full configuration map from it.

### C — measure authority and quasi-invariance

There must be an already-authorized kinematic/physical measure `mu` on the same configuration domain and an established quasi-invariance statement for `F_alpha`, sufficient to define the Radon-Nikodym derivative.

A local torsion/coarea weight on a different object is insufficient unless the bridge to `mu` is explicit.

### D — unitary implementation

Pre-existing authority must define or prove the unitary operator

`(U_alpha psi)(x) = [d(F_alpha*mu)/dmu]^(1/2) psi(F_alpha^{-1}x)`

or its convention-equivalent form, including the correct domain.

### E — 24-history identity

The branch labels of these `U_alpha` must be the same 24 B4/G3 histories used by the current Weyl-active realization, not a generic abstract family or a conformal control realization.

### F — phase-free CP map

Once A-E hold, the G8A phase-free branch CP object

`rho -> (1/24) U_alpha rho U_alpha^dagger`

and coarse channel

`E(rho)=(1/24) sum_alpha U_alpha rho U_alpha^dagger`

must be well-defined on one common Hilbert/observable domain.

### G — refinement compatibility authority

To authorize a later channel-blocking test, existing fine/coarse configuration maps or their unitary implementations must have a specified composition/refinement relation. Iter054S matrix convergence alone does not pre-satisfy G.

## POSITIVE CONTROLS

- G8A gives an exact abstract normalized history instrument conditional on unitary branch transports.
- Iter054S gives genuine same-realization Weyl-active ordered geometric transport blocking.
- G6/G7/G10 contain finite configuration/groupoid/refinement structure that may close part of the bridge.

## NEGATIVE CONTROLS

Reject as bridge closure:

- using a 4x4 Lorentz/path transport matrix directly as a Kraus operator;
- declaring metric compatibility `A^T E A=E` to be Hilbert unitarity;
- inventing a finite-dimensional Euclidean inner product for G3 vectors;
- using the torsion/coarea Jacobian as the G8A configuration measure without an explicit authority map;
- using the conformal G38 realization instead of Weyl-active G3;
- assuming quasi-invariance or an RN derivative merely from invertibility;
- importing unresolved action phases, `beta=1`, or `c6` normalization.

## PASS

PASS only if A-G are all closed by pre-existing authority in one compatible G3/B4 realization.

Classification:

`PASS_SCOPED_ITER055A_G3_B4_CONFIGURATION_MAP_KOOPMAN_UNITARY_BRIDGE_ESTABLISHED__CHANNEL_TEST_AUTHORIZED`

## BLOCKED

If the abstract G8A unitary instrument and classical G3 transports both exist but at least one of A-G lacks a same-realization bridge, classify:

`BLOCKED_OBJECT_DEFINITION_ITER055A_G3_GEOMETRIC_TRANSPORT_TO_G8A_UNITARY_CHANNEL_BRIDGE_INCOMPLETE`

The result must localize the missing object(s) exactly.

## FAIL

Scientific FAIL requires an actual incompatibility between simultaneously authoritative same-realization definitions, for example a proven failure of quasi-invariance or impossible common domain. Absence alone is BLOCKED.

Classification:

`SCIENTIFIC_FAIL_ITER055A_G3_G8A_CHANNEL_BRIDGE_INCOMPATIBLE`.

## INVALID

INVALID for wrong-realization substitution, use of the 4x4 matrices as Hilbert operators without proof, incomplete source audit, or post-prereg introduction of a new measure/Hilbert structure.

## INTERPRETATION CEILING

Even PASS would authorize only construction/testing of the phase-free coarse channel in this scoped realization. It would not prove channel refinement consistency, global regulator removal, interacting-measure existence, quantum unitarity in all sectors, UV completion, fix `c6`, authorize `beta=1`, establish GR recovery, experiment, new physics, or QGR correctness.

Theory established remains `0%`.