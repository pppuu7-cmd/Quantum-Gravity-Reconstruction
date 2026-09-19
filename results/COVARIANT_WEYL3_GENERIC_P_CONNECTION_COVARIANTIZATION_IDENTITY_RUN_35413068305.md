# COVARIANT_WEYL3_GENERIC_P_CONNECTION_COVARIANTIZATION_IDENTITY — run 35413068305

Date: 2026-09-19

## Authority

- Gate: `COVARIANT_WEYL3_GENERIC_P_CONNECTION_COVARIANTIZATION_IDENTITY`
- Prospective preregistration: `a388b8fdef54742b4e6120b8f23965d604aa4e04`
- Execution binding: `a04ac058e3cd3a26d6e516db50a4c0f0053faf9f`
- Production head: `5e82f70356937d9673c11dafda2e1afe5c28748c`
- Actions run: `35413068305`
- No Weyl3 panel values were used.
- `P^{abcd}` obeyed pair antisymmetry and pair exchange only; first Bianchi was not imposed.

## Terminal classification

`GENERIC_P_DIRECT_CONVERSION_OTHER`

The direct partial-to-covariant Riemann conversion Lane D is neither exactly equal nor exactly negative to the tensor-only covariant double-divergence connection Lane G.

- `D_EQ_G = false`
- `D_EQ_NEG_G = false`
- common exact ratio `D/G = null`

## First exact formal counterexample

Canonical monomial:

`P[0,1|0,1] * g2[0,0|0,0] * h[1,1]`

Exact coefficients:

- Lane D = `1`
- Lane G = `2`

Therefore:
- direct-equality difference = `-1`;
- exact-negative difference = `3`.

This is already a counterexample to promotion of the six-cell corrected sign relation to an arbitrary pair-symmetric tensor `P` using the tensor-only Lane G formula.

## Bianchi relevance

The first counterexample involves the sectional component `P[0,1|0,1]`. Under the frozen Riemann pair symmetries, the first Bianchi identity is trivially satisfied for repeated index set `0,1,0,1`; it does not constrain this component. In four dimensions the nontrivial additional algebraic Bianchi relation lies in the four-distinct-index sector. Therefore merely imposing first Bianchi cannot remove this first mismatch.

No Bianchi-repair gate is authorized from this result.

## Structural diagnosis for the next prospective gate

The failed Lane G treated `P^{abcd}` as an ordinary contravariant tensor. However the historical partial-IBP construction differentiates

`Q^{abcd} = sqrt(|g|) P^{abcd}`,

a contravariant tensor density of weight +1.

For a weight +1 contravariant density, the covariant derivative contains the additional trace-connection term

`- Gamma^r_{d r} Q^{abcd}`.

At a normal-coordinate point its connection-jet contribution to the double divergence is

`W = -2 h_ab sum_{c,d,r} (partial_c Gamma^r_{d r}) P^{a c d b}`.

This term is derived from density weight, not from the observed residual. A separate prospective gate is required before testing whether `D = G + W`.

## Formal payloads

- Lane D term count: `912`
- Lane G term count: `1128`
- Lane D SHA256: `138c715fb96eadf5162b4442aaaeed65007f3d40ab2b7f63805fab0074d6e98c`
- Lane G SHA256: `34d9ca91b11fa47b3a7f9b77f4f833788fcdf68d9f1684dd8c375d6e4f5cc8fa`
- malformed Lane G SHA256: `23f4abde4f95df9850db590bb88434d75963acb47041f81f8629beebf47046c7`
- terminal payload SHA256: `09b55b1cbc7bbf60b74b9af6601c59390172d1dc3be676c1c38e2814df573b93`

## Jobs and immutable artifacts

Jobs:
- source lock: `105816338547`
- Lane D: `105816357736`
- Lane G: `105816357922`
- terminal: `105816384699`

Artifacts:
- source lock: ID `10575445208`, `sha256:c021fba4e5cde85a285ceed49e364a0b25a9cfb9785173645d1bd629db9896f8`
- Lane D: ID `10574014163`, `sha256:7d613b14033ee8aa90962878895838ea4e724344834ddb44232fdfc7589a01bf`
- Lane G: ID `10575315454`, `sha256:7925e59b01ea85a3c49589e94c8248d1c29fff9c7ca3a1ae9c5a25ad7fd8803f`
- terminal: ID `10575420388`, `sha256:74ceb6160f8bdea520d668aec84bacd9279b7505cd1f0a42f1e745f782e46d32`

All jobs completed successfully.

## Claim ceiling

This is a valid exact negative generic result. It does not weaken the separately terminal corrected Weyl3 six-cell certificate; instead it shows that the finite-panel closure cannot yet be promoted to arbitrary pair-symmetric `P` through the tensor-only connection channel.

Historical parent results remain immutable. `c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no experimental confirmation, global QGR theorem, quantum unitarity, UV completion, physical c6, or new-physics claim is authorized.
