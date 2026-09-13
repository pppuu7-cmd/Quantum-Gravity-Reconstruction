# Iter053T source-level derivation — why the legacy transformed weighted path carries `B^2`

Date: 2026-09-14

Status: analytic/code-path derivation supporting the prospectively frozen Iter053T gate. This note does not assign the Iter053T terminal classification and does not use partial Iter053T numerical evidence.

## 1. Compact perturbation factorization

`code/qgr_iter053_compact_support_action.py` defines

`CompactPerturbation(seed).base = Perturbation(seed)`

and

`h(u) = B(u) p(u)`

where

`B(u)=prod_i b_i(u_i)`,
`b_i(s)=(1-(s/A)^2)^4`

inside the support cube.

Therefore, for an untransformed compact perturbation object `pert`,

`pert.base.jets(u)[0] = p(u)`.

## 2. What the Gauss-Jacobi weights already contain

Iter053R uses

`roots_jacobi(order,4,4)`

in each source coordinate and maps `u=A z`. The Jacobi weight is

`(1-z)^4 (1+z)^4 = (1-z^2)^4`.

After `u=A z`, this is exactly the one-dimensional compact-support factor `b_i(u_i)`, and the product rule supplies

`B(u)=prod_i b_i(u_i)`

once. The implementation factor `(A**4)*prod(w_i)` is the four-dimensional coordinate scaling together with the Jacobi weights.

Thus the weighted reducer must contract H5 only with the **unfactored** polynomial tensor `p(u)`.

## 3. Base Iter053R path

In the base branch, Iter053R calls

`weighted_bulk(metric, pert, order)`

with `pert` a `CompactPerturbation`. Inside `weighted_bulk` it evaluates

`p = base_pert.base.jets(u)[0]`.

Because `base_pert.base` is `Perturbation`, this returns `p(u)`. Hence the total weighted integrand represents

`B(u) [H_x(u):p(u)]`.

This is the intended factorization.

## 4. Transformed wrapper depth

`TransformPerturbation` is defined by

`TransformPerturbation(base,L).base = base`.

For Iter053R C lanes, the wrapper is constructed as

`pt = TransformPerturbation(pert,L)`

where `pert` is already a `CompactPerturbation`.

Therefore

`pt.base = pert = CompactPerturbation`,

not the polynomial `Perturbation` nested one level further down.

The transformed Iter053R branch then calls

`weighted_bulk(mt, pt, ..., p_transform=lambda p: L.T@p@L)`.

Inside the same generic reducer,

`base_pert.base.jets(u)[0]`

now means

`pt.base.jets(u)[0] = pert.jets(u)[0] = B(u)p(u)`.

After `p_transform`, the tensor used in the contraction is

`B(u) L^T p(u) L`.

## 5. Consequence

The transformed branch still uses the same external Gauss-Jacobi weight that already supplies one `B(u)`. Therefore its effective weighted integrand is

`B(u) * [ H_y(L^-1 u) : ( B(u) L^T p(u)L ) ]`

or

`B(u)^2 [ H_y(L^-1 u) : L^T p(u)L ]`.

For `det L=1` and a correctly transforming H5 density, the source-faithful representation should instead be

`B(u) [ H_y(L^-1 u) : L^T p(u)L ]`.

Thus the legacy transformed Iter053R path and the base path are not representations of the same weighted integral.

## 6. Why this specifically predicts the observed pattern

This object-path defect predicts all of the qualitative features already frozen as historical Iter053R evidence:

1. The direct support-domain transformed integral can remain covariant because it evaluates the full transformed compact perturbation and does not perform this weighted factor extraction.
2. The base weighted branch can converge because it extracts `p(u)` at the correct wrapper depth.
3. The transformed weighted branch is systematically suppressed because an extra `0 <= B(u) <= 1` multiplies its integrand.
4. Low-order GJ convergence can deteriorate because after the Jacobi rule has absorbed one support polynomial, a second nonconstant `B(u)` remains inside the nominally smooth reduced integrand.

These are mechanism-level predictions, not an Iter053T PASS. The prospectively frozen numerical lanes must still establish the source-faithful corrected covariance and the legacy negative controls.

## 7. Correct source-faithful path tested by Iter053T

Iter053T retains the original source coordinate `u=x`, evaluates transformed geometry at

`y=L^-1 u`,

uses exactly one external Jacobi support weight `B(u)`, and transforms only

`p_y(u)=L^T p(u)L`.

The historical Iter053R classification remains immutable regardless of Iter053T outcome.

## Claim ceiling

This derivation identifies an implementation-path mismatch. It does not establish the integrated corrected gate, a global Weyl3 equation, quantum consistency, quantum amplitude/measure, fixed `c6`, `beta=1`, GR recovery, UV completion, new physics, or theory establishment.