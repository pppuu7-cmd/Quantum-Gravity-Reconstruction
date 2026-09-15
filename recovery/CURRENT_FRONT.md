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

Iter057J preregistration `0f4d3cf9e1482029382dd158aa8feef89a8d736a`, derivation `5e1775dd83da8b952ea0463bfef946eb7692f632`, durable result `70f2da96887f376f8f827d435894755bb0dc9f67` terminalized as `BLOCKED_ITER057J_EXACT_K_ECAB_SOURCE_REPRESENTATION_NOT_EXPOSED_IN_CURRENT_AUTHORIZED_IMPLEMENTATION_LINEAGE`. No Actions run was used and no scientific FAIL/PASS of the conformal ansatz was inferred.

## Active Iter057K

Prospective preregistration: `e6b894f95979d85e270cef99a48c639258057ea6`.

Frozen target: expose the already-authorized Iter056X covariant Weyl3 Euler tensor on exact analytic G3/H0 in an exact symbolic coordinate/jet representation sufficient for all second covariant derivatives entering

`K_ecab = [nabla_e nabla_c H_ab - nabla_e nabla_a H_cb]_0 - R_ca b{}^d(0) H_ed(0)`.

This gate may encode only existing authorized geometry/conventions. It may not change Iter057J criteria, introduce a new background primitive, fit c6, use a third symmetry reduction as derivation, or infer physical characteristics. Numerical finite differences are diagnostic only and cannot decide exact zero.

Required exact controls: metric inverse/symmetry; Riemann/Weyl algebraic symmetries; Weyl tracelessness; E_W3 symmetry; Noether/diffeomorphism divergence consistency to the exposed order.

### Bounded implementation checkpoints

Commit `bf01d61939371053af120567408172084d4ee4f8` adds `code/qgr_iter057k_exact_g3_geometry.py` and exposes the source-owned G3/H0 potential and metric with exact SymPy rationals, exact metric inverse, Christoffel, Riemann, Ricci, scalar-curvature and four-dimensional Weyl tensors, plus exact geometry controls.

Commit `8b7f90e6c7cb6a7d71d202f1ea70ec9081d4af81` adds `code/qgr_iter057k_exact_weyl3_lineage.py`. This is a direct exact-source transliteration of the already-used Weyl3 lineage pieces from `qgr_iter051b1_weyl3_p_insertion.py`, `qgr_iter051b0_double_divergence_operator.py`, `qgr_iter051c_full_eom.py` and `qgr_iter051c_d2n_near_null.py`. It exposes, without coefficient fitting or a new physics primitive:

- exact `I3 = C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`;
- exact projected `P^{abcd}` via symbolic directional differentiation and the same algebraic-Riemann projection;
- exact first and double covariant divergence operators for `P`;
- exact metric-density variation term `A_ab`;
- exact lowering-insertion term `I_ab`;
- the historical minus-sign assembled density `H_ab = A_ab + I_ab - 2 sqrt(-g) D_ab` used by the current numerical lineage.

The checkpoint deliberately does **not** invent a normalization converting that historical assembled density into the authorized covariant Iter056X `E_W3_ab`. That mapping is now the single narrow remaining authority dependency before the exact `E_W3` derivative oracle and frozen E-symmetry/Noether controls can be completed.

Iter057K has **no terminal classification yet**. The new source checkpoint is neither PASS nor BLOCKED and says nothing about whether `K_ecab` vanishes. No Actions run is active. CI remains intentionally idle until the covariant `E_W3` normalization is source-authorized in the exact evaluator. Green CI alone is never scientific PASS.
