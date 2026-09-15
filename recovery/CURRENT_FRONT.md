# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `POST-ITER057J / EXACT ITER056X E_W3 SOURCE EXPOSURE FOR K_ECAB`
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

## Consumed authority before Iter057J

Iter057F3 durable result `0d8640c399d5cc6a81a6abb6207cd1a295e695d9`:

`PASS_SCOPED_ITER057F3_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_FULL_TENSOR_NORMALIZATION`.

This remains a scoped off-shell local operator certificate only.

Iter057H establishes that uncorrected Ricci-flat G3/H0 is off shell for nonzero symbolic `c6` in the Einstein+Weyl3 truncation.

Iter057I durable result `94a1b18b9281e6939ed07a19f06acbc49f655d4d` establishes only the pointwise first-order conformal cancellation jet; it is not an open-neighborhood solution.

## Terminal Iter057J result

Frozen preregistration: `0f4d3cf9e1482029382dd158aa8feef89a8d736a`.
Reduction/derivation: `5e1775dd83da8b952ea0463bfef946eb7692f632`.
Durable result: `70f2da96887f376f8f827d435894755bb0dc9f67`.
Actions run: **none**.

Terminal classification:

`BLOCKED_ITER057J_EXACT_K_ECAB_SOURCE_REPRESENTATION_NOT_EXPOSED_IN_CURRENT_AUTHORIZED_IMPLEMENTATION_LINEAGE`.

The frozen first nontrivial obstruction remains

`K_ecab := [nabla_e nabla_c H_ab - nabla_e nabla_a H_cb]_0 - R_ca b{}^d(0) H_ed(0)`.

A bounded source audit of the current consumed implementation lineage identified `code/qgr_iter057f_g3_origin_weyl3_k2.py` as exposing the analytic G3/H0 metric jets and exact algebraic Weyl controls, but its Weyl3 Euler response is obtained through the numerical `d2n.assemble_minus5(...)` finite-difference path. It does not expose an exact symbolic coordinate `E_W3_ab[g0](x)` or exact covariant derivative oracle sufficient for the second derivatives of `H_ab` required by `K_ecab`.

The frozen Iter057J contract forbids replacing an exact-zero decision by empirical tolerance. Therefore no numerical K value was consumed and no scientific FAIL or PASS was inferred. This is a source-representation BLOCKED result only; the conformal candidate itself remains scientifically undecided.

## Next-dependency lock

1. Prospectively preregister the smallest exact-source exposure/implementation gate for the already-authorized covariant Iter056X Weyl3 Euler tensor on the exact analytic G3/H0 metric.
2. The new gate may expose/encode only existing authorized geometry and conventions; it must not modify Iter057J criteria or introduce a new background primitive.
3. The exposed object must be sufficient to obtain the exact covariant derivatives entering the full independent component set of `K_ecab`.
4. Numerical finite-difference values may be diagnostics only and may not decide exact zero.
5. Keep `c6` symbolic/unfixed; no fitted coefficient, third repetitive symmetry reduction, post-hoc treatment selector, or physical-characteristic claim.
6. Once the exact source representation exists, Iter057J may be re-entered or superseded only under a prospectively frozen exact evaluation contract.

Green CI alone is never scientific PASS.
