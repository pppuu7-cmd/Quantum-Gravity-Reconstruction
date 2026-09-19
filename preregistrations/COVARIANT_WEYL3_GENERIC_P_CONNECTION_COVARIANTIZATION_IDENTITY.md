# Preregistration — COVARIANT_WEYL3_GENERIC_P_CONNECTION_COVARIANTIZATION_IDENTITY

Date: 2026-09-19
Status: **FROZEN BEFORE GENERIC FORMAL EXPANSION**

## Parent motivation and claim firewall

The corrected Weyl3 six-cell certificate is terminal:
- result commit `eb05fa6eb0cb3a3b642f302b87c1ebf280e110c3`;
- run `35412692881`;
- classification `CORRECTED_PARENT_SIX_CELL_EXACT_MATCH`.

The historical parent FAIL `e26208cec90566001b65640775d2e58d0429bf5c` remains immutable.

This gate does **not** use Weyl3 panel values. Its purpose is to test whether the localized connection-covariantization sign relation is a generic local tensor identity in the derivative sector.

## Formal source space

Work in dimension four at a normal-coordinate point with fixed
`eta = diag(-1,1,1,1)`.

No curvature panel, Weyl tensor, I3 value, directional seed, frozen cell, or numerical target is permitted.

Independent exact symbols:

1. `P^{abcd}` with only the algebraic pair symmetries
   - `P^{abcd}=-P^{bacd}`
   - `P^{abcd}=-P^{abdc}`
   - `P^{abcd}=P^{cdab}`

   No first-Bianchi identity is imposed in this first generic gate. Thus the result, if exact, is stronger than one relying on Bianchi.

2. symmetric background second metric jets
   `g2[ab|pq]=g2[ba|pq]=g2[ab|qp]`.

3. symmetric perturbation values
   `h[ab]=h[ba]`.

Canonical monomials are exact rational coefficients of

`P[pair|pair] * g2[pair|pair] * h[pair]`.

## Lane D — direct partial-to-covariant Riemann conversion

For each `i=0,1,2,3`, derive target-blind the connection tensor `K_abcd(i,i)` from

`partial partial = covariant Hessian - C_nabla`

using the repository Riemann derivative ordering

`1/2 [g_ad,bc + g_bc,ad - g_ac,bd - g_bd,ac]`.

Construct the diagonal formal scalar

`D = sum_i sum_abcd P^{abcd} K_abcd(i,i)`.

Serialize the complete canonical coefficient map before any comparison.

## Lane G — covariant double-divergence connection jet

Independently derive the connection-jet contribution at a normal-coordinate point to

`2 h_ab nabla_c nabla_d P^{a c d b}`

with `P` treated as an abstract tensor whose ordinary derivatives are zero for this isolated source class.

The frozen formal expression is

`G = 2 h_ab sum_{c,d,r} [`
` (partial_c Gamma^a_{dr}) P^{r c d b}`
`+(partial_c Gamma^c_{dr}) P^{a r d b}`
`+(partial_c Gamma^d_{dr}) P^{a c r b}`
`+(partial_c Gamma^b_{dr}) P^{a c d r} ]`.

Here every `partial_c Gamma` is derived from the abstract `g2` basis and eta.

Serialize the complete canonical coefficient map independently of Lane D.

## Frozen comparison

Determine exactly:
- `D_EQ_G`
- `D_EQ_NEG_G`

If neither holds, record:
- first canonical monomial mismatch for direct equality;
- first canonical monomial mismatch for exact-negative equality;
- whether all nonzero overlapping coefficients admit one common exact rational ratio, for diagnosis only.

A malformed control removes the derivative-index term
`(partial_c Gamma^d_{dr}) P^{a c r b}`
from a copy of Lane G. It must not satisfy whichever exact relation, if any, the authoritative Lane G satisfies.

## Frozen terminal taxonomy

- `GENERIC_P_DIRECT_CONVERSION_EQ_COVARIANT_GAP`
- `GENERIC_P_DIRECT_CONVERSION_EQ_NEG_COVARIANT_GAP`
- `GENERIC_P_DIRECT_CONVERSION_OTHER`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

No new relation may be invented after result inspection.

## Interpretation ceiling

An exact relation would establish a generic local derivative-sector tensor identity under pair symmetries, independent of the Weyl3 finite panel. It would not by itself prove the complete Weyl3 variational theorem, because algebraic curvature/metric-variation sectors and global integration assumptions remain distinct.

`c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no experimental confirmation, quantum unitarity, UV completion, physical c6, or new-physics claim.
