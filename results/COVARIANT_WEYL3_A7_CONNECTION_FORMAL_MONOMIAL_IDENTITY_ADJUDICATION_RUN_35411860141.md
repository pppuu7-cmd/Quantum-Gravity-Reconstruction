# COVARIANT_WEYL3_A7_CONNECTION_FORMAL_MONOMIAL_IDENTITY_ADJUDICATION — run 35411860141

Date: 2026-09-19

## Authority

- Gate: `COVARIANT_WEYL3_A7_CONNECTION_FORMAL_MONOMIAL_IDENTITY_ADJUDICATION`
- Prospective preregistration: `bbb4e90e46ddd1aded691a1d780e10dbe0313e51`
- Execution binding: `b9b96d900532a4eb89af50e2a8a46c5c698d88b6`
- Production head: `5aa634af669dfa166a0336367aad2f45612a42b6`
- Actions run: `35411860141`
- No panel data or numerical witness is used in the formal lanes.

## Terminal classification

`FORMAL_CONNECTION_TENSOR_A_EQ_NEG_B`

Across the complete 256-component tensor, expanded over the exact canonical bilinear source basis

`g2[ab|pq] * h[cd]`,

the formal coefficient map of Lane A is exactly the negative of Lane B.

- `A_FORMAL_EQ_B = false`
- `A_FORMAL_EQ_NEG_B = true`

The negative relation has no mismatch in any free component or canonical monomial.

## First direct A=B mismatch

Free component:

`(a,b,c,d)=(0,1,0,1)`

Canonical monomial:

`g2[0,0|0,0]*h[1,1]`

Exact coefficients:

- A = `-1/4`
- B = `1/4`

## Controls

All frozen controls passed:
- all 256 components serialized;
- exact source basis identical;
- both independent formal lanes ready;
- prospective preregistration exact;
- malformed outer-sign control rejects direct equality;
- malformed outer-sign control also rejects exact-negative equality.

Thus the exact-negative result is not a comparator artifact insensitive to sign mutations.

## Payloads

- Lane A formal SHA256: `ba7ed7b7eb2b8fa66dbc07ffd6b6a66f7f2896f242257c6830e77cb56b6f2c32`
- Lane B formal SHA256: `09ee351958f9f066a84b581194275fffc73c123744f24c6b8cdff26ce4693034`
- malformed-control SHA256: `d6c321a2446bbcaf9c4035ff1c54b7e4249e2f1f62bd482a82b20373a6ff2b34`
- Lane A payload SHA256: `94251c7634debbab93320db98adc02fa426b10060c5c0fa0975f603b4849b149`
- Lane B payload SHA256: `5b72e341b2f5d3b5fe3c48ee8c27ffc936607c598fbbceae7f9e364be18a6951`
- terminal payload SHA256: `5e627b46b3ad201694e3730b9ae373d73705b85a4b52fafe7914a6a0bd5266db`

## Jobs and immutable artifacts

Jobs:
- source_lock: `105812905915`
- lane_a: `105812934592`
- lane_b: `105812934627`
- terminal: `105812971014`

Artifacts:
- source lock: ID `10573788021`, `sha256:9f261cf1c3ae311f798000bb4dc6069bd763249566c27872ef5662a4288e343c`
- Lane A: ID `10573748135`, `sha256:8a629f4f231a4cabf67c7b092b00ff133ab714029b0109f377cdd17a071170c0`
- Lane B: ID `10574293810`, `sha256:79355022477ccf95224914cdf8d0452ad0ae95959a71b6122469835dc942f096`
- terminal: ID `10574668477`, `sha256:0d903a305206f3c330192a644a50c6ad41bbfc13cc79474479872c66179f6c68`

All jobs completed successfully.

## Scientific consequence

Together with terminal multicoordinate neutral extraction `17b79ca06ff2208e9b09a8ec74fa509a18e5ec4c`, which independently reproduced all connection factors and matched Lane B exactly, the remaining A/B discrepancy is now structurally localized to the implemented tensor-Hessian identity: relative to the repository GammaGamma construction, Lane A carries an overall exact sign across the complete formal tensor.

This does not authorize changing Lane A retrospectively. The next admissible question is which Riemann/covariant-Hessian convention produces that sign, using a separate prospective convention-identity audit derived directly from the repository's defining Riemann formula.

## Locks

Historical terminal results remain immutable. `c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no experimental confirmation; no global QGR theorem, quantum unitarity, UV completion, physical c6, or new-physics claim is authorized.
