# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER055B / CANONICAL FULL-CONFIGURATION DYNAMICS VS GAUGE RELABELING`
Project phase: `MODEL_CONSTRUCTION / QUANTUM AMPLITUDE-MEASURE SOURCE REALIZATION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- Physical exact-vs-order-reduced Weyl3 treatment selector: **absent**.
- Global interacting measure/regulator removal: **not established**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID/BLOCKED results remain immutable.

## Recovered auto-research chain

The substantive auto-research/action chain through Iter055B and the historical G25-G38/G31-G37 programmes has been re-read against preregistrations, implementations, terminal results and Actions rather than commit titles alone.

Key current facts:

- exact lower-order QGR action exists; full current source-normalized/Weyl3 microscopic branch action does not;
- G25-G28 narrow the source freedom to `J(n)=beta*n`, with `beta` still unfixed; their beta-free phase ratios are not mapped to the 24 G3/B4 ordering histories;
- G31-G32 give local/conditional projective action integration but not absolute phase normalization;
- Iter054S gives scoped Weyl-active G3 geometric fine-to-coarse transport blocking;
- Iter054T-Y localize source/history action underdefinition;
- Iter054Z proves all branch CP maps and the history-forgotten coarse channel are exactly invariant under independent branch rephasing, while the fine history-register phase reference remains operationally undefined;
- Iter055A proves that the G3 4x4 geometric transports are not yet bridged to the G8A configuration-space Koopman/RN unitaries;
- Iter055B proves that the 24 B4 histories are path/order objects carrying geometric fiber transport inside a fixed configuration, not yet full-configuration dynamics maps `F_alpha:X->X`.

## Iter054Z — phase dependency split

Preregistration `9c78ba250c97e2853c731d26faa07b4f054639a1`.
Result `e239959034118fe7002120ae988455443166760f`.

Classification:

`BLOCKED_OBJECT_DEFINITION_ITER054Z_G8A_HISTORY_COHERENCE_SEMANTICS_NOT_FIXED`.

Exact durable subresult:

`K_alpha -> exp(i theta_alpha) K_alpha`

leaves each branch CP map and

`E(rho)=sum_alpha K_alpha rho K_alpha^dagger`

unchanged. Thus unresolved `S_alpha` is not a blocker for the established coarse CPTP channel. The fine isometry changes only by a diagonal unitary on the auxiliary history register; no fixed noncommuting register observable/phase reference has been authorized.

## Iter055A — G3 to G8A channel-object bridge BLOCKED

Preregistration `99af4f18b1151c2da4185bf42799b282be48ba44`.
Result `cf065c7777fdb7f7dec34965db207c16c56fefd1`.

Classification:

`BLOCKED_OBJECT_DEFINITION_ITER055A_G3_GEOMETRIC_TRANSPORT_TO_G8A_UNITARY_CHANNEL_BRIDGE_INCOMPLETE`.

G7B supplies the finite graph configuration object `X_Gamma={(G_v,A_e)}` and exact path-groupoid blocking. Iter054S supplies concrete Weyl-active 4x4 path transports. G8A supplies the conditional theorem that an **invertible quasi-invariant configuration map** induces a unitary Koopman/Radon-Nikodym operator.

Missing bridge:

`G3 history/path in one configuration -> full configuration map F_alpha -> quasi-invariant measure -> RN derivative -> Hilbert-space U_alpha`.

Metric compatibility of a 4x4 Lorentz transport is not Hilbert-space unitarity.

## Iter055B — B4 history semantics BLOCKED

Preregistration `c014dc24bd296bf0b8ff09131d4e420800b8a34b`.
Result `28024bae10d658075711743a8b7e3883ba033c61`.

Classification:

`BLOCKED_OBJECT_DEFINITION_ITER055B_B4_HISTORY_DOES_NOT_YET_DEFINE_G8A_CONFIGURATION_ENDOMORPHISM`.

Under current authority a B4 maximal history is:

> a combinatorial ordering/permutation together with a path through an already-given finite configuration, carrying an invertible metric-compatible fiber transport.

The 24 histories are geometrically distinct on curved cells: relative holonomy spread is nonzero. But the path product acts between local frame/tangent fibers and does not update the complete configuration point `(G_v,A_e)`.

G7B/G10B exact path composition and refinement-connected transport therefore do not by themselves define

`F_alpha:X_Gamma->X_Gamma`.

Refinement/coarse maps between different graph levels are also not invertible fixed-domain endomorphisms unless extra reconstruction data are supplied.

## Current highest-information question

The most obvious possible pre-existing rescue is the QGR covariance/gauge/relabeling action on the complete finite configuration object.

Prospective next gate:

`CAN THE EXISTING FRAME / GAUGE / RELATIONAL RELABELING ACTION SUPPLY THE MISSING INVERTIBLE FULL-CONFIGURATION MAP F_alpha, AND IF SO IS IT PHYSICAL BRANCH DYNAMICS OR PURE GAUGE ON THE G8C/G8D PHYSICAL QUOTIENT?`

This is counterexample-first. A gauge transformation may be a perfectly good invertible/quasi-invariant map on kinematic configuration space while being physically redundant after constraint descent. Such a map must not be promoted to history dynamics merely because it yields a unitary Koopman operator.

If no non-gauge event-update endomorphism already exists, the G8A branch dynamics remains a candidate-defining missing object and the phase-free channel cannot yet be source-realized.
