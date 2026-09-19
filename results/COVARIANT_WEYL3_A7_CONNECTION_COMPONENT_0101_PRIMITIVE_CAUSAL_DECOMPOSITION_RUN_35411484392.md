# COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION — run 35411484392

Date: 2026-09-19

## Authority

- Gate: `COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION`
- Prospective preregistration: `7b9d2ffb84993f04e467c0a9ea6bf650327f6b62`
- Execution binding: `e75a093089c3393d2587cb79420a3b00faa813cc`
- Production head: `f07613a376cf2a2ba83754ba04291eeb5b6e1d27`
- Actions run: `35411484392`
- Frozen witness: `OFFSHELL_A / d=7 / (i,j)=(0,0)`
- Frozen component: `(a,b,c,d)=(0,1,0,1)`

## Terminal classification

`COMPONENT_0101_PRIMITIVE_DIVERGENCE_LOCALIZED`

All frozen provenance and reproduction controls passed. Parent full-tensor hashes and scalar controls reproduced exactly.

## First all-three primitive divergence

Frozen comparison class:

`CONNECTION_FACTOR_CHANNELS`

First lexicographic primitive channel:

`dGamma:0,0,0,1`

Exact values:

- Lane A: `1/34`
- Lane B: `1/34`
- Lane C: `0`

Therefore the neutral polynomial lane C ceases to represent the same shared connection input before the representation-specific Hessian/GammaGamma ledgers are compared.

## Pairwise localization

Shared-input comparison through
`FREE_INDEX_PLACEMENT -> METRIC_INVERSE_METRIC_CONTRACTIONS -> CONNECTION_FACTOR_CHANNELS`:

- A vs B: no divergence.
- A vs C: first divergence `dGamma:0,0,0,1`, `1/34` vs `0`.
- B vs C: first divergence `dGamma:0,0,0,1`, `1/34` vs `0`.

Full ordered-ledger first A/B divergence is representation-specific:

- class `HESSIAN_CHANNELS`
- channel `outer0:ci_i:r0:a`
- A = `-1/272`
- B = `0`

This does not by itself adjudicate the A/B sign conflict because B reaches the same tensor object through a different GammaGamma ledger.

## Frozen component values

- A = `89350652201/169388331840`
- B = `-89350652201/169388331840`
- C = `-1781797/49528752`

The parent full-tensor relation A = -B remains reproduced, while C remains unequal to either sign.

## Parent tensor reproduction

- A tensor SHA256: `6dce9ed04c9199cf36eb2a723095f7eeba3f002844c3cd9df7da33704cbdf673`
- B tensor SHA256: `702b353ada68114482ede9a4fb3c8af6d3b7af708982256e44b7c2e7909848b4`
- C tensor SHA256: `e3797c7dade7f4de601ba047be48b0ed73278333e01719e3b0d97588e783deb8`

Lane payload SHA256:

- A: `f72f0ace702e3d718bdaca34c4704e2738b3b0f279ce26114257568febee8806`
- B: `c447928e5b2dbf964c57f4b60e4fe29200fb58d71c3dcc923a52a601744e809e`
- C: `9fa2f0f39e481db6e0e13296943a59c9f37f6195e2e18f150e6e3908dc24374d`

Terminal payload SHA256:

`bc70d3aa22ebc3a1c0f8d8e79119f6f1d12c893b4c7275343e2391abd5a440a4`

## Jobs

- source_lock: `105811832091`
- lane_a: `105811853833`
- lane_b: `105811853840`
- lane_c: `105811853901`
- terminal: `105811901014`

All completed successfully.

## Immutable artifacts

- source lock: ID `10574428136`, `sha256:6e777dd890dd9551e59b667a1ba73fbef40e51f79798344dcb83e4b8f445e67e`
- lane A: ID `10574523020`, `sha256:f7e0ec87e661aebdedc374c5ea55f2c9cfe853ad5a5cbb5d64171cacd38ca037`
- lane B: ID `10574022223`, `sha256:1fe88c78ea96465f14faea054afcfb8819e3dce568c8fb8e3ac12dfcab187ae3`
- lane C: ID `10573572733`, `sha256:9359e450a3d656543cae9ccef9d27fc0387744bf21b286146cb4adaa3bbafd1c`
- terminal: ID `10574038530`, `sha256:59cd741b9812ff3f8eb08257bf97c9907228fa69747213b0085dffd3738f2783`

## Scientific interpretation ceiling

The exact new fact is that the C construction already differs from A/B at a shared connection-factor primitive, not merely after final contraction. This result does not retroactively invalidate or repair prior gates and does not authorize choosing A or B.

A separate prospective construction is required to test whether a multicoordinate neutral polynomial jet that explicitly represents mixed coordinate derivatives restores the missing `dGamma:0,0,0,1` channel.

`c6=SYMBOLIC_UNFIXED`; corrected Q10 remains locked; `theory_established=0%`; no experimental confirmation; no global QGR, unitarity, UV-completion, physical-c6, or new-physics claim is authorized.
