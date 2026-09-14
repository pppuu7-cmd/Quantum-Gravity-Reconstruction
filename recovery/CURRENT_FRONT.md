# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER056J / PHYSICAL TREATMENT SELECTOR FOR WEYL3 DYNAMICS`
Project phase: `MODEL_CONSTRUCTION / DYNAMICAL-TREATMENT AUTHORITY`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; running not authorized.
- Historical QGR physical Weyl3 treatment selector remains absent.
- Strong hyperbolicity of the exact full higher-derivative theory is not established.
- Micro-to-continuum reconstruction and global interacting measure/regulator removal remain blocked.

## Terminal formal-mathematics chain

Iter056G:
`PASS_SCOPED_ITER056G_EINSTEIN_SHELL_REMOVES_WEYL3_FOURTH_METRIC_DERIVATIVES`.

Iter056H:
`PASS_SCOPED_ITER056H_FINITE_ORDER_TRUNCATION_HAS_EXPLICIT_HS_PLUS_2N_REGULARITY_BUDGET`.
For fixed N, a conservative sufficient budget is `g_0 in H^{s+2N}` and `g_n in H^{s+2(N-n)}`.

Iter056I:
`PASS_SCOPED_ITER056I_ALL_FORMAL_COEFFICIENT_SOURCES_ARE_RECURSIVELY_BIANCHI_COMPATIBLE`.

Iter056J prereg `988a39962ead180f00b42a600fd4b7b60a8c6d37`; result `82a1adba8fcd66e245970448ff6fbb47380d34a1`:
`PASS_SCOPED_CONDITIONAL_ITER056J_EVERY_FIXED_FINITE_ORDER_TRUNCATION_HAS_SEQUENTIAL_LOCAL_SOLUTION`.

Under an independently supplied strongly hyperbolic lower-order gauge formulation, compatible initial data, the Iter056G source reduction and Iter056H regularity budget, every fixed finite formal order-reduced truncation can be solved sequentially on a sufficiently short common local interval.

## Scientific consequence

The prospective order-reduced **finite-N mathematical candidate** is not presently blocked by an internal finite-order PDE inconsistency in the audited scope. The surviving blocker is upstream and physical: QGR has no established principle that selects this treatment over the exact higher-derivative equations or another admissible treatment.

Do not confuse mathematical viability of a prospective candidate version with historical QGR authority.

## Current highest-information gate

Audit the complete repository authority for a physical treatment selector. A valid selector must independently justify why the Weyl3 correction is to be interpreted perturbatively/order-reduced (or instead exactly), using a QGR-owned physical principle rather than continuity alone, mathematical convenience, desire to remove fast modes, or post-hoc ghost avoidance.

If no such candidate-owned selector exists, record a terminal missing-authority result rather than inventing one. If one exists, prospectively freeze its exact physical content and falsification test before using it downstream.

## Operational status

No active authoritative GitHub Actions production is required at this moment. Scheduled automation remains in short-orchestrator mode.
