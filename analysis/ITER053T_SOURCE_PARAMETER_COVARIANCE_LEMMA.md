# Exact source-parameter covariance lemma for the corrected weighted pushforward

Date: 2026-09-14
Status: analytic identity / implementation audit aid. This note uses no partial substantive values from active Iter053T productions and assigns no terminal scientific classification.

## Setup

Let the linear coordinate change be

`x = L y`

with nonsingular constant `L`. Let `u` denote the source parameter in the original compact-support cube and set

`x=u`, `y=L^-1 u`.

Let the metric perturbation polynomial factor be a covariant symmetric tensor `p_x(u)`. Its transformed components are

`p_y(u) = L^T p_x(u) L`.

Let `H^{ab}` be the variational tensor density defined by

`delta S = integral d^4x H_x^{ab}(x) delta g^x_ab(x)`.

Coordinate invariance of `delta S` gives the contravariant density transformation law

`H_y(y) = |det L| L^-1 H_x(x) L^-T`.

For the frozen Iter053T shears, `det L=1`, so this reduces to

`H_y = L^-1 H_x L^-T`.

## Exact contraction identity

Using Frobenius/index contraction,

`H_y : p_y`

becomes

`|det L| (L^-1 H_x L^-T) : (L^T p_x L)`.

In indices,

`H_y^{ij} p^y_ij`
`= |det L| (L^-1)^i_a (L^-1)^j_b H_x^{ab} L^c_i L^d_j p^x_cd`
`= |det L| H_x^{ab} p^x_ab`.

Therefore

**`H_y(L^-1 u) : [L^T p_x(u)L] = |det L| [H_x(u):p_x(u)]`.**

For every frozen Iter053T shear,

**`H_y(L^-1 u) : [L^T p_x(u)L] = H_x(u):p_x(u)`**

pointwise in exact arithmetic.

This is independent of the compact-support bump, quadrature order, node distribution and seed.

## Consequence for the source-parameter integral

Write the compact perturbation as

`h_x(u)=B(u)p_x(u)`.

After retaining `u` as the integration/source parameter, the intended reduced weighted representation is

`I_x = integral_du B(u) [H_x(u):p_x(u)]`.

For `det L=1`, the transformed representation is

`I_y = integral_du B(u) [H_y(L^-1u):L^T p_x(u)L]`.

The exact contraction identity gives

`I_y = I_x`.

For general constant `L`, the coordinate Jacobian and tensor-density factor must be treated consistently; the current frozen C shears avoid this extra bookkeeping because `det L=1`.

## Consequence for tensor Gauss-Jacobi quadrature

The Iter053T representation uses the same source nodes `u_k` and the same external tensor Gauss-Jacobi weights `w_k`, where the Jacobi weight already contains `B(u)` once.

At any fixed quadrature order `q`, define

`Q_x(q)=sum_k w_k [H_x(u_k):p_x(u_k)]`,

`Q_y(q)=sum_k w_k [H_y(L^-1u_k):L^T p_x(u_k)L]`.

If the pointwise tensor-density law is satisfied exactly, then every summand is identical for `det L=1`, hence

**`Q_y(q)=Q_x(q)` for every quadrature order q separately.**

Thus corrected frame covariance and quadrature convergence are logically distinct obligations:

1. covariance at GJ2 or GJ3 tests object transformation / implementation consistency;
2. GJ2->GJ3 change tests whether that common discrete representation is converged toward the continuous weighted integral.

A frame-covariance failure at fixed q cannot be repaired merely by increasing quadrature order if the same source nodes and weights are used in both frames; it points to transformation/object/numerical-H evaluation mismatch.

## Exact legacy double-weight contrast

The legacy transformed Iter053R extraction produces

`p_legacy_y(u) = B(u) L^T p_x(u)L`.

Therefore, even if H transforms perfectly,

`H_y:p_legacy_y = B(u) [H_x:p_x]`

for `det L=1`.

The external Gauss-Jacobi measure already supplies another `B(u)`, so the legacy discrete sum represents

`sum_k w_k B(u_k) [H_x(u_k):p_x(u_k)]`,

where `w_k` itself corresponds to the first support factor. Equivalently the continuous target is weighted by `B^2`, not `B`.

Hence the legacy C discrepancy is not a quadrature-coordinate covariance effect: it is an object mismatch between the base and transformed reduced integrands.

## Relation to the two active Iter053T companion gates

The two prospectively frozen active gates test different numerical consequences of this lemma:

- the primary weighted-support gate tests the wrapper/factorization identity, corrected fixed-order covariance, GJ2->GJ3 convergence, legacy B^2 negative control and corrected-vs-legacy improvement;
- the nodewise companion tests the corrected contraction on all 81 GJ3 nodes for three frozen H5 derivative steps, with a wrong-congruence negative control.

Their raw evidence and terminal classifications remain independent under their respective preregistrations. This lemma must not be used to substitute a PASS for either numerical gate.

## Interpretation ceiling

This is an exact conditional coordinate/tensor-density identity. It does not establish that the numerical H5 implementation satisfies its transformation law everywhere, does not establish quadrature convergence, does not establish the full A4+B2+C2 functional-variation gate, and does not authorize any quantum, c6, beta=1, GR, UV, experimental or theory-establishment claim.
