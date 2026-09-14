# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER056G / FINITE-ORDER REGULARITY BUDGET FOR ORDER-REDUCED WEYL3`
Project phase: `MODEL_CONSTRUCTION / PROSPECTIVE ORDER-REDUCED CANDIDATE MATHEMATICS`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; running not authorized.
- Historical QGR physical Weyl3 treatment selector remains absent.
- Strong hyperbolicity of the full higher-derivative theory is not established.
- Finite/symmetry-reduced sectors are not global theorems.
- Micro-to-continuum reconstruction and global interacting measure/regulator removal remain blocked.

## Latest chain

Iter056B: formal hierarchy `L0 g_n=S_n[g0,...,g_(n-1)]`, with only the lower-order linearized operator on the new coefficient.

Iter056C: the first Weyl3 source is Noether-conserved and compatible with the linearized lower-order Bianchi identity.

Iter056D: conditional on an independently supplied strongly hyperbolic lower-order gauge formulation, each perturbative coefficient equation inherits the same principal hyperbolic structure.

Iter056E: `PASS_SCOPED_ITER056E_NAIVE_FIXED_SOBOLEV_ALL_ORDER_RECURSION_HAS_DERIVATIVE_LOSS__NO_CONVERGENCE_OR_PHYSICAL_FAILURE_CLAIM`.

Iter056F: `BLOCKED_OBJECT_DEFINITION_ITER056F_NO_AUTHORITATIVE_COVARIANT_WEYL3_SOURCE_REDUCTION_OR_TAME_IDENTITY`.

Iter056G prereg `018fde277b8cd2031131f27ec3191208cd9c3e10`; result `d117f05239115830b0719e14f116c4e092b4e6db`:

`PASS_SCOPED_ITER056G_EINSTEIN_SHELL_REMOVES_WEYL3_FOURTH_METRIC_DERIVATIVES`.

For the repository Weyl-cubic object `I3=C_ab{}^{cd} C_cd{}^{ef} C_ef{}^{ab}`, the f(Riemann) differential term `-2 nabla^c nabla^d P_acdb`, with `P~C*C`, has no surviving second covariant derivative of Weyl on a smooth four-dimensional Einstein background. Differential Bianchi plus derivative commutators reduce all such terms to `(nabla C)^2` plus algebraic `R*C*C` structures. Thus the source is at most third differential order in the known lower-order metric in this representation, not fourth.

This does not set `nabla C=0`, does not prove a tame estimate or convergence, and does not authorize historical QGR order reduction.

## Current highest-information gate

Prospectively establish a finite-order truncation regularity theorem for the formal order-reduced hierarchy using the Iter056G third-order source bound and the conditional lower-order hyperbolic estimate from Iter056D.

The target is an explicit Sobolev derivative budget as a function of truncation order N. This is a candidate-version mathematical theorem only. It must not be promoted to all-order convergence, full-QGR dynamics, or physical treatment authority.

## Operational status

No active authoritative GitHub Actions production is required for this analytic gate. Heavy CI should remain idle unless an independent symbolic/numerical control becomes genuinely informative.
