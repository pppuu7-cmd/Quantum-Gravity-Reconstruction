# QGR Current Research Front

Updated: 2026-09-15
Primary active front: `ITER057J / OPEN-NEIGHBORHOOD ONSHELL OR CONTROLLED PERTURBATIVE BACKGROUND CONTINUATION`
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

## Newly consumed authoritative production — Iter057F3

Preregistration: `bf64df5b213ca9977d2709c7b7fea8cab96ad688`
Implementation: `4d5e72b0a50ffe54a85df012de219e840580cbdb`
Production head: `9b1a6779d4e2893e59a83a86ef543080afa1db5a`
Run: `34907701856`
Aggregate job: `104197162608`
Summary artifact: `10373609114`
Summary artifact digest: `sha256:24b1a94dec959f5593b476d99898fb4f7d223c41e046fea096d08860f84b4b1f`
Durable result: `0d8640c399d5cc6a81a6abb6207cd1a295e695d9`

Terminal classification:

`PASS_SCOPED_ITER057F3_G3_ORIGIN_WEYL3_K2_BLOCK_EXTRACTED_WITH_EXACT_FULL_TENSOR_NORMALIZATION`.

All ten raw lane artifacts and the frozen aggregate were consumed before classification. Aggregate controls: `complete=true`, `implementation_valid=true`, `lane_pass_count=10`, no parse errors, `L4_exact_Qfull_relative_residual=4.345767554384006e-06`, `L4_bilinear_symmetry_relative_residual=2.5367033099401844e-06`, and `L2_trace_Ward_vector_relative_residual=8.51614187200353e-05`. The exact-zero Qfull column was controlled by a global absolute scale predicate rather than an ill-posed relative-to-zero metric.

The extracted Weyl3 `L2` block is therefore a scoped **off-shell local operator certificate** on the source-owned G3/H0 origin. This does not yet authorize physical characteristic or hyperbolicity claims.

## Binding on-shell interpretation locks

Iter057H (`dc8aa5f3f111df1c668e0a25c05313d762305fd8`) proves that uncorrected Ricci-flat G3/H0 is off shell for nonzero symbolic `c6` in the Einstein+Weyl3 truncation.

Iter057I preregistration `53bd47d2b21d25dfa212bfb46c81a681bb827969`, derivation `a6e9663bc32fcf4fcdaaa95133c7b7bf6e3f7bdb`, durable result `94a1b18b9281e6939ed07a19f06acbc49f655d4d` establishes only:

`PASS_SCOPED_ITER057I_LOCAL_O_C6_CONFORMAL_JET_CANCELS_G3_OFFSHELL_SOURCE_AT_POINT__SOURCE_SYMBOLS_VALID_TO_FIRST_ORDER`.

The conformal Hessian jet cancels the Weyl3 source at one point through first order in symbolic `c6` while preserving the pointwise source symbols to that order. It is **not** an open-neighborhood solution, convergence theorem, constraint-propagation result, or global background construction.

## Active question

Can the Iter057I pointwise formal correction be extended to a source-authorized on-shell or perturbatively on-shell Weyl-active background on an open neighborhood, with explicit compatibility/Bianchi/constraint control, before any physical characteristic analysis?

## Next-dependency lock

1. Prospectively preregister the smallest open-neighborhood/controlled-perturbative background-extension gate.
2. Do not use a third repetitive symmetry reduction as a substitute for a genuinely covariant/local continuation argument.
3. Keep `c6` symbolic/unfixed and do not introduce a post-hoc treatment selector or fitted background correction.
4. Only after an on-shell or controlled perturbatively on-shell background is established may the mixed `Einstein k2 + c6 Weyl3(L2+L4)` operator be considered for physical characteristic questions.
5. Quantum amplitude/measure closure remains an orthogonal fallback if this background gate is not technically executable.

Green CI alone is never scientific PASS.
