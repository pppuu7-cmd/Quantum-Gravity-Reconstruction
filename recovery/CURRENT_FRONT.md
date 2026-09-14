# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER055C / PHYSICAL FULL-CONFIGURATION EVENT-UPDATE LAW`
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

## Current terminal chain

- Iter054S: scoped Weyl-active G3 geometric fine-to-coarse transport blocking PASS.
- Iter054T-Y: source/history action underdefinition localized.
- Iter054Z: branch CP maps/coarse channel are phase invariant; fine history-register phase reference not operationally fixed.
- Iter055A: G3 4x4 geometric transports are not bridged to G8A configuration-space Koopman/RN unitaries.
- Iter055B: B4 histories are path/order objects inside a fixed configuration, not full-configuration endomorphisms.
- Iter055C preregistration `0adbff561977a37e3b9653ee713d8cf1fd942aaf`; terminal result `2761524c9c457db30fa43f8169f36415b6cb0026`.

## Iter055C — gauge/relabeling rescue ruled out

Classification:

`PASS_SCOPED_ITER055C_GAUGE_RELABELING_MAPS_CANNOT_REALIZE_PHYSICAL_B4_BRANCH_DYNAMICS`.

The audit separates three objects that must not be conflated:

1. Relational frame pullbacks are genuine covariance maps, but G8C/G8D place them in the gauge/BRST equivalence structure. Gauge-related representatives agree on physical observables, so invertibility or unitary implementability cannot make these maps physically distinct history branches.
2. The 24 `S4` seed maps do descend unitarily on the finite two-mode physical quotient and therefore are not simply gauge. However, their own authoritative result classifies the history-forgetting twirl as a symmetry/coarse-label conditional expectation, explicitly **not microscopic time evolution**, and leaves genuine dynamical curved transports open.
3. Generic curved G3/B4 histories remain path/order objects with geometric fiber transport inside a fixed configuration; there is still no source-faithful map `F_alpha:X_Gamma->X_Gamma` updating the complete finite configuration.

No new CI was run for Iter055C because the gate was an authority/semantics audit over existing exact results; rerunning their algebra numerically would have been a duplicate/fake load.

## Current highest-information question

The missing object is now specifically a **non-gauge physical event-update law on the complete finite configuration**.

Highest-priority next audit:

`DOES THE ALREADY-DERIVED LOWER-ORDER QGR ACTION/EQUATIONS DEFINE A CANONICAL FINITE FULL-CONFIGURATION UPDATE OR FLOW THAT CAN BE COMPOSED ALONG B4 HISTORIES, WITHOUT INTRODUCING A NEW HAMILTONIAN, CLOCK, SYMPLECTIC FORM, DISCRETIZATION OR POST-HOC UPDATE RULE?`

This must be source-first and counterexample-first. An equation of motion, stationary-action condition, fiber parallel transport, or refinement map is not automatically an invertible endomorphism of one fixed configuration space. If the current lower-order action lacks the phase-space/clock/boundary data needed to define such a map, that is a candidate-defining missing object rather than permission to invent it.

If a pre-existing physical update map is found, only then test quasi-invariance/Radon-Nikodym data and its identification with B4 branch compositions. If not, keep the G8A branch dynamics source-realization blocked and move to the next genuinely independent closure route rather than relabeling gauge symmetry as dynamics.
