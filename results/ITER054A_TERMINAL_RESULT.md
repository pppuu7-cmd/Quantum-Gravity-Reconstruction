# Iter054A Terminal Result — Weyl3 derivative order and regime separation

Date: 2026-09-14

Gate: `ITER054A-WEYL3-DERIVATIVE-ORDER-AND-REGIME-SEPARATION`

Status: **TERMINAL SCOPED PASS**

Classification: `PASS_SCOPED_ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION`

## Frozen provenance

- preregistration commit: `6164dd1bbbdea45c0599334f3df5b5e66ac19121`
- implementation commit: `077c16cdb7d17e9a7be18572d570b857a51de675`
- production head: `4f207f1e7c24d848de2d3aa240727dbf11a95424`
- authoritative run: `34800952154`
- aggregate job: `103843400312`
- summary artifact: `10331268039`
- summary digest: `sha256:e835300668f9f946277b0c3f613a4602411c9499c536af4eb4fa5fb73b6364a7`

Lane artifacts:

- A0 job `103843352288`, artifact `10331082600`, digest `sha256:d42b7268ba59ea2e907bef3ada92babee8f2c79a65c7400ba001985e97261105`
- A1 job `103843352434`, artifact `10331796423`, digest `sha256:5a2c11e23542e3f745dac880fdc97f0ebb6b2df53995edf13ee0d147acc0e18f`
- B0 job `103843352464`, artifact `10331092591`, digest `sha256:4a5d6c06b0b9e993f21c9199b8fb4b8e5c64dc95d6daa0b1e599b7e1f1fcc89d`
- B1 job `103843352458`, artifact `10331243182`, digest `sha256:7da436e1fc46864617c3f635784cfd1ec23f4efd8ff368140101ae3feebfc1ab`

## Frozen evidence consumed

A0: for the curvature-cubic jet proxy `L=(q'')^3`, exact Euler–Lagrange order is 4, with nonzero fourth-derivative coefficient `6 q''`; the derivative-of-curvature negative control `L=(q''')^2` is sixth order.

A1: all 12/12 frozen exact-rational cubic curvature-component constructions have maximum derivative order 4 and nonzero fourth-derivative coefficient.

B0: the linearized fourth-order principal coefficient is background activated: `6 R`; it vanishes at the zero-curvature control and is nonzero at the frozen nonzero-curvature control.

B1: the exact polynomial contains a GR-connected branch and a second branch singular as the perturbative parameter tends to zero; the analytic GR-connected branch remains zero through the frozen fourth order. This is regime separation only.

The frozen aggregate found A0/A1/B0/B1, no missing streams or parse errors, and all four streams passed with valid controls.

## Interpretation lock

This result establishes only derivative-order and exact-vs-perturbative/order-reduced bookkeeping for the frozen audit. It does **not** establish a physical extra-mode count, ghost sign, stability, hyperbolicity, well-posedness, quantum unitarity, UV completion, or a complete global covariant Weyl3 metric Euler–Lagrange tensor.

`c6` remains symbolic/unfixed. `beta=1` remains unauthorized. Theory established remains **0%**.

Next scientific obligation: a prospectively frozen Weyl3 principal-part/Hessian and well-posedness-obligation gate on Weyl-active versus conformally-flat backgrounds before any physical spectrum/ghost interpretation.
