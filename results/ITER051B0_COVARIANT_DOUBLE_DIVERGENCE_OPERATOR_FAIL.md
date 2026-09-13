# Iter051B0 — terminal result

Classification: `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`.

Authoritative provenance:
- preregistration: `f983a3111c087289f6dc16703e99bb28f04668da`
- implementation: `1357dbe0cf9c453efd1e02eeba44eed0b434760f`
- aggregate: `a696ee8b899d6ba6129065394fc55690607f48ac`
- first launch head: `5cb496a90eae3b60f4ab75beed43c50531d16562`
- technical-only covariance tensor extraction repair: `63c0c6416e2c22dd19b0166ceadbeebc880ed74e`
- authoritative retry head: `9be326cae17e9af94a6d14517251ac3193642a57`
- authoritative retry run: `34731863909`
- aggregate job: `103656032270`
- summary artifact: `10309387321`
- summary digest: `sha256:3c6b77b4544c7063126d0928f7e433bf426cafb89888e353f0896d6663ba0f7f`

Frozen aggregate:
- valid lanes: 8/8
- PASS lanes: 0/8
- max finest direct-vs-expanded relative discrepancy: `2.1248485401445406e-09`
- max P-symmetry residual: `2.7755575615628914e-17`
- max inverse residual: `4.440892098500626e-16`
- max constant-frame covariance residual: `0.7485664439316078`

Interpretation: the frozen gate is terminal FAIL because the covariance criterion is part of the preregistered scientific predicate and fails in every lane. Direct nested finite differences and the explicit expanded implementation nevertheless agree very closely, so the observed failure is localized to the covariance/control layer or to a shared noncovariant structural error; this does not authorize post-hoc repair or PASS promotion.

Post-terminal code audit identified a concrete candidate control defect: `transform_jets` applies the contravariant frame matrix with transposed index placement on the second and fourth P indices (`jm`, `ln` rather than `mj`, `nl`). Because production results have already been viewed, the historical G51B0 result remains immutable. Any corrected check must be a new prospectively preregistered replacement certificate.

Scope lock: no Weyl^3-specific P insertion, no full 4D covariant Weyl^3 EOM, no value of c6, no beta=1, no energy-positivity/unitarity claim is authorized.