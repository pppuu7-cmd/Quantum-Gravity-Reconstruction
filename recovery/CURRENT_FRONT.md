# QGR Current Research Front

Updated: 2026-09-19

## Programme status

`candidate_program_roadmap_readiness = 100%` is infrastructure/roadmap readiness only. `theory_established = 0%`. No experimental confirmation.

## Latest terminal scientific result

`COVARIANT_WEYL3_A7_CONNECTION_MULTICOORDINATE_NEUTRAL_EXTRACTION`

- preregistration: `58284ae7f71e73db5c2d71d157bc74bd7d646030`
- execution binding: `4fe4634a1b026bd73233e1082efe52bfcda91bf9`
- authoritative run: `35411657960` (`completed/success`)
- production head: `45bf70a9f861fb56128690c6b25bf085c070e87a`
- terminal artifact: `10574678132` (`weyl3-a7-connection-multicoordinate-terminal`)
- artifact digest: `sha256:c3a03181a9e50580f293741b06528448fa4c88249de246600c232a50bbf7a59f`
- terminal payload SHA256: `cb12107f846dbe74c13536500fa8449d5e9e1797428bf12bb8e62f32f34e2eba`
- durable result commit: `001f552883f0ff0e1e4f505c0f35859026ad45a6`
- classification: `MULTICOORDINATE_NEUTRAL_EXTRACTION_MATCHES_LANE_B`

Frozen witness remains `OFFSHELL_A / d=7 / (i,j)=(0,0)` and frozen component remains `(a,b,c,d)=(0,1,0,1)`.

The target-blind multicoordinate neutral polynomial construction passed all frozen mandatory controls before comparison: all 64 `dGamma(j=0)` channels and all 64 `deltaGamma_phi(i=0)` channels reproduce exactly, the full 256-component tensor was serialized, and the neutral tensor hash

`702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4`

matches frozen Lane B exactly. It does not match Lane A or legacy Lane C. The frozen component value is

`-89350652201/169388331840`.

Historical terminal results remain immutable; legacy C is not reclassified and no post-hoc parent repair is authorized.

## Previous localization authority

`COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION` remains preserved as the parent localization authority:

- preregistration: `7b9d2ffb84993f04e467c0a9ea6bf650327f6b62`
- execution binding: `e75a093089c3393d2587cb79420a3b00faa813cc`
- authoritative run: `35411484392`
- production head: `f07613a376cf2a2ba83754ba04291eeb5b6e1d27`
- durable result commit: `199ecea77c9138c4a166d1ffc7143ce2d0de34be`
- classification: `COMPONENT_0101_PRIMITIVE_DIVERGENCE_LOCALIZED`

## Next bounded step

No new gate is selected by this terminal-consumption step. The latest <=10 commits observed at run start contain newer mainline work beyond the recovery snapshot, including tip `265c18fa2ddea1a660e4d06365cf6524e5f0ce44`. The next run must begin again from `CURRENT_FRONT.md`, `state.json`, and the latest <=10 commits, then reconcile those newer commits without scanning broad history. Do not retroactively alter the frozen multicoordinate criteria or historical terminal classifications.

## Locks

`c6=SYMBOLIC_UNFIXED`; corrected Q10 LOCKED; `theory_established=0%`; no experimental confirmation; `beta=1` unauthorized; finite certificates are not global theorems; classical != quantum; diagnostic != closure; no quantum-unitarity, UV-completion, physical-c6, KMQGB `NEW_REQUIRED`, or new-physics claim is authorized.
