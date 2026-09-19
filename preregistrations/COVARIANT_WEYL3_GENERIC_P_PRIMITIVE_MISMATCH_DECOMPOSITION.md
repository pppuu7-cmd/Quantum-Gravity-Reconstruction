# Preregistration — COVARIANT_WEYL3_GENERIC_P_PRIMITIVE_MISMATCH_DECOMPOSITION

Date: 2026-09-19
Status: **FROZEN BEFORE PRIMITIVE DECOMPOSITION EXECUTION**

## Parent authority

The authoritative tensor-density completion is commit `3d6f236c9e1f9e169bc6c4d2463c05e111efac87`, run `35420685309`, classification `GENERIC_P_TENSOR_DENSITY_COMPLETION_OTHER`.

Frozen parent scientific preregistration: `7a62dd856aec084add16af8e6793d157ef32637b`.
Frozen execution binding: `0abad7d17e3eceaed66b727cae75169a63096a9d`.
Frozen Lane-D blob: `d7c14040166bcbb71c2eb8db6cf0d001e83d44e8`.
Frozen weighted-lane blob: `b8d85923315018c7b50f4cd30399ea228cbb0bf9`.

The first authoritative direct mismatch in frozen ordering is
`P[0,1|0,1]*g2[0,0|1,1]*h[0,0]`, with Lane D coefficient `2` and weighted coefficient `1`.
This witness is an observation anchor only. No primitive lane may read Lane D or any terminal residual while constructing its source-side decomposition.

## Frozen question

Can the generic tensor-density source side be decomposed target-blind into primitive covariant channels so that the residual against Lane D can be localized without inventing a new correction?

## Frozen source object

Dimension four, `eta=diag(-1,1,1,1)`, exact rational arithmetic.
`P^{abcd}` is antisymmetric in each pair and symmetric under pair exchange, with **no first Bianchi identity**.
`g2[ab|pq]` and `h[ab]` are symmetric within each displayed pair.
Canonical monomials are exact `P*g2*h` terms.

The source-side connection-jet expression is decomposed before target comparison into:

1. `T_a = 2 h_ab sum_{c,d,r} (partial_c Gamma^a_{dr}) P^{r c d b}`;
2. `T_c = 2 h_ab sum_{c,d,r} (partial_c Gamma^c_{dr}) P^{a r d b}`;
3. `T_d = 2 h_ab sum_{c,d,r} (partial_c Gamma^d_{dr}) P^{a c r b}`;
4. `T_b = 2 h_ab sum_{c,d,r} (partial_c Gamma^b_{dr}) P^{a c d r}`;
5. density-weight trace channel `W = -2 h_ab sum_{c,d,r} (partial_c Gamma^r_{dr}) P^{a c d b}`;
6. derivative/product-rule channel `DP`, frozen to zero for this source class because ordinary derivatives of abstract `P` are set to zero at the normal-coordinate point;
7. density/product-rule channel `SQRTG_PRODUCT`, frozen to zero at the normal-coordinate point because first derivatives of `sqrt(|g|)` vanish there;
8. pair-symmetry bookkeeping, recorded explicitly as oriented contribution counts plus the canonicalized exact maps. Pair symmetries only are allowed; Bianchi reduction is forbidden.

The aggregate source map is frozen as
`G_primitive = T_a + T_c + T_d + T_b + W + DP + SQRTG_PRODUCT`.
No extra coefficient, sign, index permutation, normalization, Hamiltonian, clock, source normalization, or residual-fitted term may be added after this preregistration.

## Independent execution lanes

Two matrix lanes, `primary` and `independent`, must construct all primitive maps without loading Lane D, the parent weighted payload, or any residual. They may share only the frozen mathematical definitions and canonical serialization contract; their channel-construction loops must be independently structured.

A separate reference job may execute only the exact frozen Lane-D and weighted-lane blobs. Terminal comparison occurs only after all source-side primitive maps have been serialized.

## Mandatory controls

- exact source-lock on this preregistration ancestry and the frozen Lane-D / weighted-lane blobs;
- pair symmetries only, no first Bianchi;
- exact rational arithmetic, no tolerance;
- no Weyl3 finite-panel data;
- both primitive lanes target-blind until serialization;
- `primary` and `independent` primitive maps agree exactly;
- `DP == 0` and `SQRTG_PRODUCT == 0` under the frozen source assumptions;
- primitive aggregate reproduces the exact frozen parent weighted map before any Lane-D classification;
- density-weight channel is nonzero;
- pair-symmetry bookkeeping is emitted and no Bianchi reduction is applied;
- no descendant/historical result is rewritten or reclassified.

## Frozen terminal taxonomy

- `GENERIC_P_PRIMITIVE_DECOMPOSITION_EQ_DIRECT_CONVERSION`
- `GENERIC_P_PRIMITIVE_DECOMPOSITION_EQ_NEG_DIRECT_CONVERSION`
- `GENERIC_P_PRIMITIVE_DECOMPOSITION_OTHER_LOCALIZED`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

`OTHER_LOCALIZED` means only that the frozen primitive source decomposition is internally reproduced and the exact residual against Lane D is nonzero and serialized. It does **not** authorize another correction.

## Interpretation ceiling

This gate is a local exact diagnostic under the stated generic pair symmetries. It may identify which already-frozen primitive channels contribute to the first mismatch and whether the explicitly frozen derivative/product-rule channels vanish. It cannot establish a global Weyl3 variational theorem, quantum unitarity, UV completion, physical `c6`, a new Hamiltonian/clock/update rule, or any new-physics claim.

Historical FAIL/BLOCKED results remain immutable. `c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `beta=1` unauthorized; finite certificate != theorem; classical != quantum; diagnostic != closure; `theory_established=0%`.