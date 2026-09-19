# Preregistration — COVARIANT_WEYL3_A7_CONNECTION_FORMAL_MONOMIAL_IDENTITY_ADJUDICATION

Date: 2026-09-19
Status: **FROZEN BEFORE FORMAL EXPANSION**

## Parent authorities

1. Primitive localization:
   - result commit `199ecea77c9138c4a166d1ffc7143ce2d0de34be`;
   - run `35411484392`;
   - A/B shared connection inputs agree, while legacy C first diverges at `dGamma:0,0,0,1`.

2. Multicoordinate neutral extraction:
   - result commit `17b79ca06ff2208e9b09a8ec74fa509a18e5ec4c`;
   - run `35411657960`;
   - classification `MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_B`;
   - all 64 dGamma and all 64 deltaGamma channels reproduce exactly before full-tensor comparison.

3. Parent tensor localization:
   - run `35407870461`;
   - finite witness relation `A_EQ_NEG_B=true`.

These are frozen evidence. The formal gate must not use their numerical component or scalar values as targets.

## Scientific question

When Lane A tensor-Hessian and Lane B direct GammaGamma constructions are expanded algebraically in an abstract exact source basis, are their complete 256-component connection tensors identical, exact negatives, or neither?

## Formal source basis

No numerical panel data are permitted.

Treat the independent source symbols as:

- symmetric background second metric jets `g2[ab|pq]`, canonicalized only by `a<=b` and `p<=q`;
- symmetric perturbation values `h[ab]`, canonicalized only by `a<=b`.

Use fixed Minkowski inverse metric `eta=diag(-1,1,1,1)`, frozen `i=j=0`, and dimension four.

Expand every component into an exact rational coefficient map over canonical bilinear monomials

`g2[ab|pq] * h[cd]`.

No numerical substitution, random evaluation, simplification by a parent target, sign fitting, free-index permutation, Riemann convention change, or post-hoc normalization is allowed.

## Lane A

Expand exactly the already-frozen tensor-Hessian construction used by the parent gate, but replace every metric jet and perturbation value by formal source symbols.

## Lane B

Independently expand exactly the already-frozen direct GammaGamma construction, again using formal source symbols and without importing Lane A helpers.

## Frozen comparison

Serialize for each free component `(a,b,c,d)` in lexicographic order:
- the sorted exact monomial coefficient map;
- its canonical SHA256.

Then determine over all 256 components:
- `A_FORMAL_EQ_B`;
- `A_FORMAL_EQ_NEG_B`.

If neither holds, record the first free component and first canonical monomial with exact coefficient mismatch.

Mandatory malformed control: flip exactly one frozen outer sign in a non-authoritative control copy and require that neither formal equality relation survives.

## Terminal taxonomy

- `FORMAL_CONNECTION_TENSOR_A_EQ_B`
- `FORMAL_CONNECTION_TENSOR_A_EQ_NEG_B`
- `FORMAL_CONNECTION_TENSOR_OTHER`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

## Interpretation ceiling

A terminal `A_EQ_NEG_B`, combined with the separately terminal target-blind multicoordinate match to B, would localize the remaining A/B discrepancy to a structural sign in the implemented tensor-Hessian identity relative to the repository GammaGamma convention. It would not itself authorize rewriting historical results or changing the parent formula. Any corrected replay requires a separate prospective gate.

`c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no global QGR, unitarity, UV-completion, experimental, or new-physics claim.
