# Preregistration — COVARIANT_WEYL3_GENERIC_P_TENSOR_DENSITY_CONNECTION_COMPLETION

Date: 2026-09-19
Status: **FROZEN BEFORE TENSOR-DENSITY FORMAL EXPANSION**

## Parent authority

Generic pair-symmetric tensor gate:
- result commit `8f9d3d05040fa8bcd33e585583e5a9d468bb6c69`;
- run `35413068305`;
- classification `GENERIC_P_DIRECT_CONVERSION_OTHER`;
- first exact counterexample
  `P[0,1|0,1]*g2[0,0|0,0]*h[1,1]`
  with Lane D coefficient `1` and tensor-only Lane G coefficient `2`.

The first mismatch is not removable by first Bianchi because `P[0,1|0,1]` is Bianchi-unconstrained.

## Scientific question

Does the missing tensor-density weight term account exactly for the failure of the tensor-only generic Lane G?

Specifically, for

`Q^{abcd} = sqrt(|g|) P^{abcd}`

viewed as a contravariant tensor density of weight +1, does the full connection-jet part of its covariant double divergence agree exactly with the frozen direct partial-to-covariant Riemann conversion Lane D?

## Frozen tensor-density identity

For weight +1,

`nabla_d Q^{abcd}`

contains the four ordinary contravariant-index connection actions plus the density-weight term

`- Gamma^r_{d r} Q^{abcd}`.

At a normal-coordinate point, isolating only first derivatives of the connection and taking ordinary derivatives of the abstract source coefficients to vanish for this source class, the frozen double-divergence connection contribution is

`G_weighted = G_tensor + W`

with the already frozen tensor part

`G_tensor = 2 h_ab sum_{c,d,r} [`
` (partial_c Gamma^a_{dr}) P^{r c d b}`
`+(partial_c Gamma^c_{dr}) P^{a r d b}`
`+(partial_c Gamma^d_{dr}) P^{a c r b}`
`+(partial_c Gamma^b_{dr}) P^{a c d r} ]`

and the independently derived density-weight channel

`W = -2 h_ab sum_{c,d,r} (partial_c Gamma^r_{d r}) P^{a c d b}`.

No coefficient or sign may be inferred from the parent residual after this preregistration.

## Formal source basis

Exactly the parent basis:
- dimension four;
- `eta=diag(-1,1,1,1)`;
- `P^{abcd}` antisymmetric in each pair and symmetric under pair exchange;
- no first Bianchi imposed;
- symmetric `g2[ab|pq]`;
- symmetric `h[ab]`;
- canonical exact monomials `P*g2*h`.

## Independent lanes

### Lane D reference

Execute the exact frozen parent Lane D implementation blob. It is a reference only; no new science code is allowed in this lane.

### Lane W

Independently construct:
- `G_tensor`;
- `W`;
- `G_weighted = G_tensor + W`.

Serialize all three exact coefficient maps before terminal comparison.

Lane W must not import Lane D or the parent Lane G implementation.

## Mandatory controls

- exact parent Lane D blob and payload provenance;
- pair symmetries only; no Bianchi;
- exact rational arithmetic;
- no Weyl3 panel data;
- weighted lane target-blind;
- `G_tensor` control in Lane W must reproduce the frozen parent Lane G map at terminal comparison;
- the density channel `W` must be nonzero;
- malformed control `G_tensor` (density term omitted) must fail whichever exact D relation, if any, authoritative `G_weighted` satisfies;
- no tolerance, target fit, free-index permutation or post-hoc normalization.

## Frozen terminal taxonomy

- `GENERIC_P_TENSOR_DENSITY_COMPLETION_EQ_DIRECT_CONVERSION`
- `GENERIC_P_TENSOR_DENSITY_COMPLETION_EQ_NEG_DIRECT_CONVERSION`
- `GENERIC_P_TENSOR_DENSITY_COMPLETION_OTHER`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

## Interpretation ceiling

An exact equality would establish that the previously observed generic counterexample was caused by treating the integration-by-parts object as an ordinary tensor instead of the weight+1 tensor density `sqrt(|g|)P`. It would establish a generic local derivative-sector identity under pair symmetries only.

It would still not by itself prove the complete Weyl3 variational theorem outside the corrected finite panel.

Historical results remain immutable. `c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no experimental confirmation, quantum unitarity, UV completion, physical c6, or new-physics claim.
