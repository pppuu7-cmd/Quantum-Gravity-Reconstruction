# Iter056I — all-order formal Bianchi compatibility result

Date: 2026-09-14
Preregistration commit: `1047050115a5b0ba05c625499a7cd543a1d57200`

## Classification

`PASS_SCOPED_ITER056I_ALL_FORMAL_COEFFICIENT_SOURCES_ARE_RECURSIVELY_BIANCHI_COMPATIBLE`

## Derivation

Let the exact diffeomorphism-invariant metric equation be

`E_ab[g,epsilon]=0`,

with formal bookkeeping parameter `epsilon=c6`, and exact Noether identity

`nabla_g^a E_ab[g,epsilon] = 0`.

Expand

`g(epsilon)=g_0 + epsilon g_1 + epsilon^2 g_2 + ...`

and

`E[g(epsilon),epsilon] = sum_{n>=0} epsilon^n E^(n)`.

The covariant derivative itself also expands,

`nabla_g = nabla_0 + sum_{k>=1} epsilon^k Delta_nabla^(k)`,

where each `Delta_nabla^(k)` depends only on `g_1,...,g_k` and their derivatives.

Taking the coefficient of `epsilon^n` in the exact Noether identity gives

`nabla_0^a E^(n)_ab + sum_{k=1}^n (Delta_nabla^(k) E^(n-k))_b = 0`.

Assume inductively that all coefficient equations below order n hold:

`E^(0)=...=E^(n-1)=0`.

Then every connection-variation term in the sum contains a lower equation coefficient and vanishes. Therefore

`nabla_0^a E^(n)_ab = 0`.

By the Iter056B hierarchy decomposition,

`E^(n) = L0 g_n - S_n[g_0,...,g_(n-1)]`.

The background linearized Noether/Bianchi identity gives

`nabla_0^a (L0 g_n)_ab = 0`

for every admissible perturbation in the linearized lower-order theory. Hence

`nabla_0^a S_(n,ab) = 0`.

Thus each formal source is recursively compatible with the lower-order constraint operator provided all lower coefficient equations hold. No separate order-by-order tuning of the source is required.

## Relation to Iter056C

Iter056C established the first Weyl3 source compatibility explicitly. Iter056I upgrades the formal statement: first-order compatibility is not an isolated accident; it is the n=1 instance of the coefficient expansion of the exact diffeomorphism Noether identity.

## Scope and limitations

The result assumes:
- the metric action used in the formal candidate sector is diffeomorphism invariant;
- the expansion is treated formally;
- lower-order coefficient equations are satisfied before invoking the n-th compatibility condition.

It does not establish solvability of `L0 g_n=S_n`, gauge fixing, global existence, convergence of the formal series, a physical order-reduction selector, or quantum consistency.

`theory established = 0%` remains unchanged.
