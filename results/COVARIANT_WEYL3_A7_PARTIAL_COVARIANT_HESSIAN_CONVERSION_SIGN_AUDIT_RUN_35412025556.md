# COVARIANT_WEYL3_A7_PARTIAL_COVARIANT_HESSIAN_CONVERSION_SIGN_AUDIT — run 35412025556

Date: 2026-09-19

## Authority

- Gate: `COVARIANT_WEYL3_A7_PARTIAL_COVARIANT_HESSIAN_CONVERSION_SIGN_AUDIT`
- Prospective preregistration: `7ef60246ae816730bb702ce0d9fd7284362b3b70`
- Execution binding: `3fff3a6169f55a4b4510becd083517275592af04`
- Production head: `439982e6b9c3390d59f438a5f7e0c5da80436ce8`
- Actions run: `35412025556`

## Terminal classification

`PARTIAL_COVARIANT_CONVERSION_MATCHES_FORMAL_B`

The target-blind conversion tensor derived from the tensor definition

`partial partial = covariant Hessian - C_nabla`

matches the previously frozen formal Lane B tensor exactly.

## Exact identities

Conversion tensor SHA256:

`09ee351958f9f066a84b581194275fffc73c123744f24c6b8cdff26ce4693034`

Frozen formal Lane B SHA256:

`09ee351958f9f066a84b581194275fffc73c123744f24c6b8cdff26ce4693034`

Frozen formal Lane A SHA256:

`ba7ed7b7eb2b8fa66dbc07ffd6b6a66f7f2896f242257c6830e77cb56b6f2c32`

Negated conversion SHA256:

`ba7ed7b7eb2b8fa66dbc07ffd6b6a66f7f2896f242257c6830e77cb56b6f2c32`

Therefore:
- conversion = B exactly;
- conversion != A;
- -conversion = A exactly.

The malformed control omitting the connection action on the derivative index matches neither A nor B.

## Payloads

- conversion payload SHA256: `f952243bf67c9dc57e0a9ac8b0af20a7b3b3530e76f1587818935b3f45f55030`
- terminal payload SHA256: `ee4c5a9a24963053129c7e6bf23421a112cc26e49ba199e5b0aec80541acfe12`

## Jobs and artifacts

Jobs:
- source_lock: `105813374764`
- conversion: `105813400783`
- terminal: `105813420256`

Artifacts:
- source lock: ID `10574159171`, `sha256:22386aa47a8e3db9d8c066aa4e0fdddbead9e28aed746dd90eb273bfe42308d9`
- conversion: ID `10574369033`, `sha256:08b71c93c2b6dff2a19a5e7b3ff85e4546801b74d90fe43a2a99f202958d6bd6`
- terminal: ID `10574658653`, `sha256:865157db2c8a443842c0cbc98a8f0805356e5d34896e418c8122eabbc409f041`

All jobs completed successfully.

## Scientific consequence

The formal A/B sign discrepancy is now causally identified.

Lane A serialized the mixed connection contribution `C_nabla` that appears *inside* the covariant Hessian. But the repository Riemann formula is written with partial second derivatives; rewriting those partial derivatives in terms of covariant Hessians requires the opposite conversion term:

`partial partial = covariant Hessian - C_nabla`.

That opposite-sign conversion is exactly Lane B and is independently consistent with the full multicoordinate neutral GammaGamma extraction.

Historical Lane A results remain immutable. This gate does not yet identify which parent Fi-jet implementation must be corrected; that requires a prospective replay targeted only at the already-localized connection-source interface.

## Locks

`c6=SYMBOLIC_UNFIXED`; corrected Q10 locked; `theory_established=0%`; no experimental confirmation; no global QGR theorem, quantum unitarity, UV completion, physical c6, or new-physics claim is authorized.
