# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER056I / CONDITIONAL LOCAL EXISTENCE FOR FINITE ORDER-REDUCED TRUNCATIONS`
Project phase: `MODEL_CONSTRUCTION / PROSPECTIVE ORDER-REDUCED CANDIDATE MATHEMATICS`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; running not authorized.
- Historical QGR physical Weyl3 treatment selector remains absent.
- Strong hyperbolicity of the full higher-derivative theory is not established.
- Micro-to-continuum reconstruction and global interacting measure/regulator removal remain blocked.

## Latest chain

Iter056G:
`PASS_SCOPED_ITER056G_EINSTEIN_SHELL_REMOVES_WEYL3_FOURTH_METRIC_DERIVATIVES`.
The covariant Einstein-shell source can be reduced to `(nabla C)^2` plus algebraic curvature terms, removing second derivatives of Weyl and bounding the known-source metric differential order by 3.

Iter056H prereg `efd833bdd346a2a0f3aaa00aa69843a54b721a2f`; result `96d53cd442ad5bac1fb4e890973b247130f0d7c1`:
`PASS_SCOPED_ITER056H_FINITE_ORDER_TRUNCATION_HAS_EXPLICIT_HS_PLUS_2N_REGULARITY_BUDGET`.
For any fixed truncation order N, a conservative budget `g_0 in H^{s+2N}` with `g_n in H^{s+2(N-n)}` closes the derivative bookkeeping under the conditional lower-order hyperbolic estimate. This is not uniform in N and does not imply convergence.

Iter056I prereg `1047050115a5b0ba05c625499a7cd543a1d57200`; result `ff49d6805b521a9edbd89881597cb9bb8189caf9`:
`PASS_SCOPED_ITER056I_ALL_FORMAL_COEFFICIENT_SOURCES_ARE_RECURSIVELY_BIANCHI_COMPATIBLE`.
The exact diffeomorphism Noether identity implies inductively that every formal source `S_n` satisfies the background linearized Bianchi/constraint compatibility condition once all lower coefficient equations hold.

## Current highest-information gate

Combine Iter056B/D/G/H/I into one prospectively frozen **conditional finite-N local-existence theorem** for the formal order-reduced coefficient hierarchy.

The theorem may assume an independently supplied strongly hyperbolic lower-order gauge formulation and constraint-compatible initial data. It must state the explicit regularity budget and solve coefficients sequentially with the same lower-order principal operator. It must not be promoted to all-order convergence or historical QGR physical treatment authority.

If this gate passes, the main remaining obstruction in this branch is no longer internal formal mathematical consistency of finite-N truncations; it is the missing physical principle selecting this prospective treatment as QGR dynamics.

## Operational status

No GitHub Actions production is needed for this analytic theorem unless a genuinely independent control is introduced. Scheduled automation remains in short-orchestrator mode.
