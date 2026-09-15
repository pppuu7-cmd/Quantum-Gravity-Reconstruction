# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `ITER057K / EXACT ITER056X E_W3 SOURCE EXPOSURE FOR K_ECAB`
Project phase: `FULL LOCAL MIXED-ORDER WEYL3 LINEARIZATION / ONSHELL BACKGROUND PROGRAMME`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- No experimental confirmation.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; running/fitting not authorized.
- No physical Weyl3 treatment selector is established.
- Strong hyperbolicity of the exact full higher-derivative theory is not established.
- Global interacting measure/regulator removal remains blocked.
- Finite/refinement, local-symbol and symmetry-reduced certificates are not global theorems.
- Classical consistency is not quantum consistency/unitarity.
- KMQGB `NEW_REQUIRED` is not authorized.

## Consumed authority

Iter057F3 durable result `0d8640c399d5cc6a81a6abb6207cd1a295e695d9` is a scoped off-shell local operator certificate only. Iter057H establishes uncorrected Ricci-flat G3/H0 is off shell for nonzero symbolic c6. Iter057I establishes only a pointwise first-order conformal cancellation jet.

Iter057J preregistration `0f4d3cf9e1482029382dd158aa8feef89a8d736a`, derivation `5e1775dd83da8b952ea0463bfef946eb7692f632`, durable result `70f2da96887f376f8f827d435894755bb0dc9f67` terminalized as `BLOCKED_ITER057J_EXACT_K_ECAB_SOURCE_REPRESENTATION_NOT_EXPOSED_IN_CURRENT_AUTHORIZED_IMPLEMENTATION_LINEAGE`. No scientific FAIL/PASS of the conformal ansatz was inferred.

## Active Iter057K

Prospective preregistration: `e6b894f95979d85e270cef99a48c639258057ea6`.

Frozen target: expose the already-authorized Iter056X covariant Weyl3 Euler tensor on exact analytic G3/H0 in an exact symbolic coordinate/jet representation sufficient for all second covariant derivatives entering

`K_ecab = [nabla_e nabla_c H_ab - nabla_e nabla_a H_cb]_0 - R_ca b{}^d(0) H_ed(0)`.

This gate may encode only existing authorized geometry/conventions. It may not change Iter057J criteria, introduce a new background primitive, fit c6, use a third symmetry reduction as derivation, or infer physical characteristics. Numerical finite differences are diagnostic only and cannot decide exact zero.

Required exact controls: metric inverse/symmetry; Riemann/Weyl algebraic symmetries; Weyl tracelessness; E_W3 symmetry; Noether/diffeomorphism divergence consistency to the exposed order.

### Exact-source implementation authority

- `bf01d61939371053af120567408172084d4ee4f8`: exact source-owned G3/H0 geometry and geometry controls in `code/qgr_iter057k_exact_g3_geometry.py`.
- `8b7f90e6c7cb6a7d71d202f1ea70ec9081d4af81`: exact Weyl3 lineage transliteration.
- `90bde0d5c89e92f6b3436c2ba3e22f5af55ab1f0`: source-authorized normalization lookup from terminal Iter056X authority `5b2acf5a47f4ba66fb126bdeab28505dd0dfb852`, establishing `H5^{ab}=sqrt(-g) E_W3^{ab}` in the same covariant-metric convention.
- `605846b1fce5568f968a9cba7c3b721322c6a63d`: exact first/second covariant derivative oracle for the authorized lowered `E_W3_ab`, plus exact E-symmetry and Noether-divergence evaluators. It carries no numerical tolerance and keeps `c6` factored out/symbolic.

## Active exact-control production

Workflow commit: `8a9feed7512732b8e4389060c9d305d5dddf9fb7`.
Workflow: `.github/workflows/qgr-iter057k-exact-controls.yml` (`qgr-iter057k-exact-controls`).
Production head: `8a9feed7512732b8e4389060c9d305d5dddf9fb7`.

The workflow is push-triggered by its creation commit and uses a `fail-fast: false` matrix with independent lanes:

`geometry`, `lineage`, `ew3-symmetry`, `noether`, `derivative-oracle`.

Each lane writes a JSON artifact. An `aggregate` job, running with `if: always()`, produces only the frozen terminal artifact `iter057k-terminal-aggregate`. The aggregate deliberately carries `scientific_classification: null`; classification is reserved for the next bounded constructor run under the frozen preregistration.

The Actions run id was not recorded in this launch step. **No lane result or partial science has been consumed and Iter057K has no terminal classification.**

## Next bounded step

Identify only the Actions run created from workflow commit `8a9feed7512732b8e4389060c9d305d5dddf9fb7` for `qgr-iter057k-exact-controls`.

- If nonterminal: check status/head provenance only; do not consume lane outputs, do not duplicate the run, and finish.
- If terminal: validate only preregistration `e6b894f95979d85e270cef99a48c639258057ea6` plus the terminal aggregate artifact `iter057k-terminal-aggregate`, classify strictly by the frozen Iter057K PASS/BLOCKED/INVALID rules, update recovery, and finish.

Do not alter Iter057J criteria, fit `c6`, use numerical tolerances as exact-zero evidence, add a third symmetry reduction, infer physical characteristics, or assign PASS from green CI alone.

Green CI alone is never scientific PASS.
