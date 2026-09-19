# Preregistration — COVARIANT_WEYL3_A7_PARTIAL_COVARIANT_HESSIAN_CONVERSION_SIGN_AUDIT

Date: 2026-09-19
Status: **FROZEN BEFORE CONVERSION IMPLEMENTATION**

## Parent authorities

Formal A/B adjudication:
- result commit `8ee3437b0cad15ff2d47d6b87840b38bdc535c81`;
- run `35411860141`;
- classification `FORMAL_CONNECTION_TENSOR_A_EQ_NEG_B`.

Independent multicoordinate neutral extraction:
- result commit `17b79ca06ff2208e9b09a8ec74fa509a18e5ec4c`;
- run `35411657960`;
- classification `MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_B`.

These results are frozen evidence and may be used only by the terminal comparator, not by the conversion derivation.

## Scientific question

For the repository's exact all-lowered Riemann derivative ordering, what connection tensor is required when rewriting the partial-second-derivative metric variation in terms of covariant Hessians?

Does the independently derived partial-to-covariant conversion tensor equal formal Lane A, formal Lane B, or neither?

## Frozen differential-geometric identity

For an arbitrary covariant rank-two field `s_ad`,

`nabla_c nabla_b s_ad`

is defined by applying the Levi-Civita covariant derivative to the covariant rank-three tensor `nabla_b s_ad`.

At a normal-coordinate point where `Gamma=0`, retain the mixed coefficient with:
- perturbation scalar `phi` satisfying `partial_r phi = delta_{ri}`;
- background connection first jet `partial_j Gamma`;
- frozen `i=j=0`.

The connection contribution `C_nabla(c,b;a,d)` must be derived directly from the tensor definition of `nabla_c nabla_b s_ad`, including the connection acting on all three covariant indices `b,a,d`.

The exact identity is then

`partial_c partial_b s_ad = nabla_c nabla_b s_ad - C_nabla(c,b;a,d)`

at the frozen mixed order.

No sign may be chosen from parent A/B results.

## Repository Riemann derivative ordering

Use the repository defining second-metric-derivative ordering exactly:

`1/2 [ g_ad,bc + g_bc,ad - g_ac,bd - g_bd,ac ]`.

Therefore construct the formal conversion tensor

`K_abcd = -1/2 [ C_nabla(c,b;a,d) + C_nabla(d,a;b,c) - C_nabla(d,b;a,c) - C_nabla(c,a;b,d) ]`.

This expression is frozen before implementation and target comparison.

## Formal basis

Use the same exact source basis as the parent formal gate:
- symmetric `g2[ab|pq]`;
- symmetric `h[cd]`;
- fixed `eta=diag(-1,1,1,1)`;
- canonical monomials `g2[ab|pq]*h[cd]`;
- all 256 free components in lexicographic order.

No panel data, numerical witness, A/B helper import, A/B tensor hash, A/B coefficient, or target sign may appear in the derivation implementation.

## Mandatory controls

- exact rational arithmetic;
- all 256 components serialized;
- direct tensor-definition derivation includes the connection action on derivative index `b` and tensor indices `a,d`;
- malformed control omitting the derivative-index connection term must fail to match both frozen parent formal tensors;
- target hashes are allowed only in the terminal comparator;
- no tolerance, random evaluation, free-index permutation, Riemann-convention switch, or post-hoc normalization.

## Frozen terminal taxonomy

- `PARTIAL_COVARIANT_CONVERSION_MATCHES_FORMAL_A`
- `PARTIAL_COVARIANT_CONVERSION_MATCHES_FORMAL_B`
- `PARTIAL_COVARIANT_CONVERSION_MATCHES_NEITHER`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

## Interpretation ceiling

A match to formal B would identify the A/B sign discrepancy as the distinction between the connection term *inside* the covariant Hessian and the opposite-sign conversion term required to replace the repository's partial second derivatives by covariant Hessians. Historical results remain immutable; any corrected Hessian replay requires a separate prospective gate.

`c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no global QGR, quantum-unitarity, UV-completion, experimental, or new-physics claim.
