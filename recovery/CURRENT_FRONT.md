# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `POST-ITER056E / WEYL3 COVARIANT SOURCE-REDUCTION OR TAME IDENTITY`
Project phase: `MODEL_CONSTRUCTION / PROSPECTIVE ORDER-REDUCED CANDIDATE MATHEMATICS`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed; regulator running is not authorized.
- Historical QGR physical Weyl3 treatment selector remains absent (Iter054G-R).
- Mixed-order exact QGR evolution reduction remains undefined (Iter054F).
- Micro-to-continuum reconstruction and global interacting measure/regulator removal remain blocked.
- Finite/symmetry-reduced panels remain scoped and are not global theorems.

## Prospective perturbative candidate chain

Iter056A: regular formal-series membership excludes the singular fast branch in the scalar control, but is not historical QGR authority.

Iter056B (`298292c78132930fdaf9753842f7d3fd50952369` -> `f0f225877cf78282d9a5b6212af216bd7c9eb35f`):

`PASS_SCOPED_ITER056B_FORMAL_HIERARCHY_USES_ONLY_LOWER_ORDER_LINEARIZED_OPERATOR_ON_EACH_NEW_COEFFICIENT__PHYSICAL_QGR_TREATMENT_NOT_AUTHORIZED`.

For `E0[g]+lambda E1[g]=0` with a regular formal expansion,

`L0 g_n = S_n[g0,...,g_(n-1)]`,

where `L0=D E0[g0]`; the higher-derivative operator does not act on the new unknown at the same perturbative order.

Iter056C (`b21a783d328f7de165f210032bd0ebd21ff7ad04` -> `442a3293c4344a9da852a664141975c75ef91c00`):

`PASS_SCOPED_ITER056C_WEYL3_FIRST_ORDER_SOURCE_IS_NOETHER_CONSERVED_AND_LINEARIZED_BIANCHI_COMPATIBLE__SOLVABILITY_NOT_ESTABLISHED`.

Diffeomorphism invariance of `integral sqrt(|g|) C^3` gives the off-shell Noether identity for its Euler-Lagrange tensor, so the first formal source is compatible with the lower-order linearized Bianchi identity.

Iter056D (`48542590c8bd292bc4eaa9ad9666d0e7eab4eee2` -> `00595b70062511aa469c064492900d200794fba4`):

`PASS_SCOPED_CONDITIONAL_ITER056D_FORMAL_ORDER_REDUCED_COEFFICIENT_EQUATIONS_INHERIT_LOWER_ORDER_STRONG_HYPERBOLICITY__QGR_GAUGE_OBJECT_STILL_MISSING`.

Conditional on an independently supplied strongly hyperbolic lower-order gauge formulation, the same principal symbol controls every perturbative coefficient equation because the higher-derivative terms occur only in the known source.

Iter056E prereg `02c632207ccfcd5d39e967c525e7ae65ed1713b2`; result `22d01a9b5f3af5935ef25184dec96f26d5dbc5fc`:

`PASS_SCOPED_ITER056E_NAIVE_FIXED_SOBOLEV_ALL_ORDER_RECURSION_HAS_DERIVATIVE_LOSS__NO_CONVERGENCE_OR_PHYSICAL_FAILURE_CLAIM`.

Under standard hyperbolic Sobolev bookkeeping, a source with `q` derivatives of a known coefficient requires greater regularity of that coefficient than a single fixed `H^s` assumption supplies. For algebraic-curvature Weyl3, the metric Euler-Lagrange equation is generically up to fourth differential order even though `C^3` is called a six-derivative EFT operator. Thus a naive fixed-Sobolev all-order recursion is not closed without additional structure.

This does **not** prove divergence or physical inconsistency. Finite truncation with enough smoothness, analytic/Gevrey scales, tame estimates, or genuine covariant cancellations remain possible.

## Current highest-information gate

Determine prospectively whether the Weyl3 Euler-Lagrange source possesses a covariant/on-shell reduction or tame identity that lowers the effective derivative demand of `S_n` while preserving the Iter056C Noether/Bianchi identity.

Permitted evidence:

- a derived covariant identity;
- a source-faithful full functional derivative/directional-variation certificate exposing cancellations;
- a prospectively versioned lower-order equation substitution rule with a proof that it preserves the conserved source structure;
- a tame estimate that closes an explicitly stated regularity ladder.

Not permitted:

- post-hoc deletion of fourth derivatives;
- assuming the desired order reduction because it is common in EFT;
- using a third symmetry-reduced sector as a substitute for the covariant object;
- promoting finite-order success to all-order convergence or physical treatment authority.

## Orthogonal fixed blockers

- Iter055V: micro-to-continuum reconstruction `R_h` missing.
- Iter054G-R: exact vs order-reduced physical treatment not source-selected.
- Iter054F: QGR-specific mixed-order evolution/gauge object not defined.
- Global interacting measure/regulator removal remains blocked.

## Operational note

Current GitHub Actions state at synchronization: **0 queued / 0 in_progress**. No CI load is justified for exact formal identities unless a genuinely computational covariant source object is produced. Last genuine production computation remains Iter054S run `34863358893`, aggregate job `104041675332`, summary artifact `10355162999`, digest `sha256:71460c1167ae6e29dfd5e49135ba96636c33e14ebc742592f423ad54f1e57da0`.
