# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `ITER057J / OPEN-NEIGHBORHOOD FIRST-ORDER BACKGROUND CONTINUATION`
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

Iter057F3 preregistration `bf64df5b213ca9977d2709c7b7fea8cab96ad688`, production run `34907701856`, durable result `0d8640c399d5cc6a81a6abb6207cd1a295e695d9`:

`PASS_SCOPED_ITER057F3_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_FULL_TENSOR_NORMALIZATION`.

This is a scoped **off-shell local operator certificate** only.

Iter057H durable result `dc8aa5f3f111df1c668e0a25c05313d762305fd8` establishes that uncorrected Ricci-flat G3/H0 is off shell for nonzero symbolic `c6` in the Einstein+Weyl3 truncation.

Iter057I preregistration `53bd47d2b21d25dfa212bfb46c81a681bb827969`, derivation `a6e9663bc32fcf4fcdaaa95133c7b7bf6e3f7bdb`, durable result `94a1b18b9281e6939ed07a19f06acbc49f655d4d` establishes only:

`PASS_SCOPED_ITER057I_LOCAL_O_C6_CONFORMAL_JET_CANCELS_G3_OFFSHELL_SOURCE_AT_POINT__SOURCE_SYMBOLS_VALID_TO_FIRST_ORDER`.

The Iter057I pointwise jet is not an open-neighborhood solution or physical-characteristic authorization.

## Active preregistered gate — Iter057J

Frozen preregistration: `0f4d3cf9e1482029382dd158aa8feef89a8d736a`.
Reduction/derivation: `5e1775dd83da8b952ea0463bfef946eb7692f632`.
Actions run: **none**.
Terminal classification: **none**.

Frozen conformal candidate:

`q_ab = 2 psi g0_ab`, with `nabla_a nabla_b psi = H_ab`,

where `H_ab = g0_ab S/6 - S_ab/2` and `S_ab=-E_W3_ab[g0]/A_E`.

The frozen-origin first curl vanishes by the source inversion/static symmetry, so the first nontrivial necessary open-neighborhood condition is the exact covariant jet

`K_ecab := [nabla_e nabla_c H_ab - nabla_e nabla_a H_cb]_0 - R_ca b{}^d(0) H_ed(0) = 0`.

This reduction does **not** terminalize Iter057J.

## Next-dependency lock

1. Evaluate the full independent component set of `K_ecab` exactly using only the repository-authoritative G3/H0 metric and covariant Weyl3 Euler tensor.
2. A single exact nonzero component is sufficient for the preregistered classification `SCIENTIFIC_FAIL_SCOPED_ITER057J_CONFORMAL_FIRST_ORDER_BACKGROUND_CONTINUATION_OBSTRUCTED__GENERAL_QAB_REMAINS_OPEN`.
3. Exact zero is **not** a PASS; it requires higher prolongation or an explicit local scalar construction under the frozen preregistration.
4. Do not introduce a fitted/numerical `c6`, post-hoc source modification, third repetitive symmetry reduction, or unpreregistered treatment selector.
5. Do not promote the Iter057F3 mixed-degree operator to physical characteristics before an on-shell or controlled perturbatively on-shell background is established.
6. If the exact repository-authoritative source representation required for `K_ecab` cannot be resolved without introducing new unfrozen geometry, stop without inventing it; the preregistered BLOCKED path remains valid.

Green CI alone is never scientific PASS.
