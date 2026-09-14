# Iter056B preregistration — generic formal order-reduction hierarchy

Date: 2026-09-14
Gate: `ITER056B-GENERIC-FORMAL-ORDER-REDUCTION-HIERARCHY`

## Frozen question
For a regular formal solution of a mixed-order functional equation

`E0[g] + lambda E1[g] = 0`,

where `E0` is lower differential order and `E1` may be higher differential order, is the new unknown coefficient `g_n` at every perturbative order governed only by the lower-order linearization `L0 = D E0[g0]`, with every contribution involving `E1` built entirely from lower-order coefficients `g_0,...,g_(n-1)` because of the explicit factor `lambda`?

This is a generic mathematical candidate architecture, not historical QGR treatment authority.

## Frozen assumptions
1. `E0` and `E1` admit formal Frechet/Taylor expansions about a background `g0` on the stated formal domain.
2. `g(lambda)=sum_(n>=0) lambda^n g_n` is a regular formal series.
3. `E0[g0]=0` at zeroth order.
4. Gauge degeneracy/invertibility of `L0` is **not** assumed; the gate concerns which operator multiplies the new coefficient, not whether it can yet be inverted.
5. Boundary conditions, constraints, convergence and physical treatment are outside this gate.

## Frozen obligations
1. Derive orders `lambda^0`, `lambda^1` and `lambda^2` explicitly.
2. Prove at arbitrary order `n>=1` that the coefficient linear in the new unknown `g_n` is exactly `D E0[g0] g_n`.
3. Prove that `E1` cannot act on `g_n` at the same order because the prefactor `lambda` shifts its Taylor contribution by one power.
4. Identify the general form
   `L0 g_n = S_n[g0,...,g_(n-1)]`
   with `S_n` known once lower orders are known.
5. State clearly that `S_n` may contain high derivatives of lower-order fields; “order reduced” means the operator on the new unknown is lower order, not that the source is derivative-free.
6. Preserve gauge/constraint caveat: if `L0` has gauge nullspace, a QGR-specific gauge/constraint formulation is still required.

## Frozen classifications
- `PASS_SCOPED_ITER056B_FORMAL_HIERARCHY_USES_ONLY_LOWER_ORDER_LINEARIZED_OPERATOR_ON_EACH_NEW_COEFFICIENT__PHYSICAL_QGR_TREATMENT_NOT_AUTHORIZED` if the arbitrary-order statement follows.
- `FAIL_SCOPED_ITER056B_HIGHER_DERIVATIVE_OPERATOR_ACTS_ON_NEW_COEFFICIENT_AT_SAME_ORDER` if the explicit `lambda E1` structure still produces `D E1[g0] g_n` at order `lambda^n`.
- `INVALID_ITER056B_FORMAL_TAYLOR_ASSUMPTIONS_INSUFFICIENT` only if the frozen formal expansion cannot define the hierarchy.

## Interpretation ceiling
A PASS establishes a generic formal perturbative/order-reduction architecture and motivates a separately versioned candidate formulation. It does not derive the full Weyl3 Euler-Lagrange tensor, fix gauge/constraints, prove solvability/convergence/remainder control, authorize the treatment physically for QGR, establish hyperbolicity/unitarity/UV/GR/experiment, or fix beta/c6.

No GitHub Actions run is preregistered; this is exact formal functional analysis.
