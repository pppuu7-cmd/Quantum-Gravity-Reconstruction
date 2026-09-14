# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `Iter054F / strong-hyperbolicity evolution-object definition`
Project phase: `MODEL_CONSTRUCTION / WEYL3 HYPERBOLICITY OBJECT DEFINITION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Strong hyperbolicity / Weyl3 well-posedness: **not established**.
- A complete mixed-order first-order evolution reduction with gauge/constraint subsystem and symmetrizer notion: **not established**.
- Quantum amplitude/measure transition: **not authorized**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID results are immutable.

## Iter054D — TERMINAL SCOPED PASS

Classification: **`PASS_SCOPED_ITER054D_WEYL3_PRINCIPAL_ORDER_GAUGE_COMPLETION_QUOTIENT_INVARIANCE_HYPERBOLICITY_NOT_AUTHORIZED`**.

Run `34811376305`; finite exact fourth-order principal gauge-completion / quotient-invariance certificate only. It does not define the full mixed-order evolution system or prove hyperbolicity.

## Iter054E — TERMINAL SCOPED PASS after control-only exact retry

Gate: `ITER054E-MIXED-ORDER-EINSTEIN-WEYL3-CHARACTERISTIC-REGIME-AUDIT`.

Provenance:

- preregistration `ed62acf961cae4a0d200364285d94a56e61a294d`
- implementation `0366422137d4e8c665b3e10e6280acb6d338f3b1`
- initial production head `59c5a09ac693c79bdc1827efa91e283cf30a36ab`
- initial run `34815920355`: **`ITER054E_IMPLEMENTATION_OR_CONTROL_INVALID_A0_STRUCTURAL_EQUALITY`**; permanently historical, not a scientific FAIL
- control-only repair `f7d996b401e147d736b91b23b7e3ef97ff546b61`
- authoritative exact-retry run `34817023061`
- aggregate job `103889834227`
- summary artifact `10336742062`
- digest `sha256:b7e0dce1e44b44ac1b9425427db3d33bdf88271f8ab42762f006a4155eb36bc9`
- terminal classification **`PASS_SCOPED_ITER054E_EINSTEIN_WEYL3_MIXED_ORDER_REGIME_SEPARATION_STRONG_HYPERBOLICITY_NOT_AUTHORIZED`**

All four frozen streams A0/A1/B0/B1 passed on the exact retry. Within the frozen exact scalar/eigenchannel proxy `P=z+eps*lambda*z^2`, the GR-connected branch `z=0` is exact and the extra branch `z=-1/(eps*lambda)` is singular as `eps -> 0`. Malformed missing-Einstein and wrong-order controls are rejected exactly.

Durable notes:

- `results/ITER054E_INITIAL_IMPLEMENTATION_INVALID.md`
- `results/ITER054E_TERMINAL_RESULT.md`

Interpretation lock: finite exact symbolic regime-separation proxy only. No full tensor characteristic determinant, open-region real-characteristic theorem, uniform diagonalizability, symmetrizer, constraint propagation, energy estimate, physical mode/ghost/residue statement, or quantum claim follows.

## Exact current blocker / Iter054F

The next fatal-consistency question is **object definition before hyperbolicity computation**.

A genuine strong-hyperbolicity test requires an explicitly fixed evolution object, not only a determinant/root proxy. At minimum the QGR authority must specify:

1. state vector / reduction variables;
2. first-order-in-time (or equivalently rigorous accepted higher-order) evolution system;
3. time direction and spatial covector domain;
4. gauge variables and gauge-fixing evolution equations;
5. constraint variables and principal constraint-propagation subsystem;
6. principal evolution matrix `A(n)` or equivalent object whose eigensystem is being tested;
7. admissible norm / symmetrizer notion and open background/covector region;
8. mapping back to the mixed Einstein + symbolic-`c6` Weyl3 equations and GR limit.

Iter054D/E explicitly leave these obligations unresolved. Repository search currently supplies no separate established first-order reduction or symmetrizer authority. Therefore the highest-information next gate is a prospectively frozen `ITER054F-WEYL3-MIXED-ORDER-STRONG-HYPERBOLICITY-OBJECT-DEFINITION-AUDIT`.

It must include an exact counterexample showing that identical real characteristic polynomials/eigenvalues can coexist with diagonalizable and defective/Jordan evolution matrices. Root reality alone is therefore insufficient for strong hyperbolicity.

## Locked next sequence

1. Prospectively preregister Iter054F before any substantive verdict.
2. Audit whether existing QGR authority already fixes the complete evolution object above.
3. Include exact positive control with a symmetrizable wave-type system and exact negative control with real repeated eigenvalues but a defective Jordan block sharing the same characteristic polynomial as a diagonalizable matrix.
4. If the required QGR evolution object is missing, terminalize `BLOCKED_OBJECT_DEFINITION` with the exact missing formulation/reduction; do **not** invent a preferred reduction post hoc.
5. Only if the object is independently fixed may a separate open-region strong-hyperbolicity/symmetrizer gate run.
6. Physical mode/ghost/stability and quantum amplitude/measure remain downstream.
