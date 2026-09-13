# Iter051C-D3 — Five-point full-EOM replacement certificate

Date: 2026-09-13
Gate: `ITER051C-D3-FIVEPOINT-FULL-EOM-REPLACEMENT`

## Authority

- Prospective preregistration: `f4dd9630408495e915fe3c8da1812c7690a58566`
- Scientific implementation: `cafa7cfbd5c72458decd2ee204f5b1f0aa02400a`
- Frozen aggregate: `06a00065a8ac2b80e254f37fc336e894aabb5fcf`
- Workflow: `63026f09ea6b1513b4ad9da4d12d8ff0cc9f8f8a`
- Authoritative production head: `242309e900b0c815983cc161c912b0439fbbc395`
- Run: `34746649884`
- Aggregate job: `103696159498`
- Summary artifact: `10314332790`
- Summary digest: `sha256:2fc0e26074e37eaa16d34cf7538f5abe1e5ec45279f0b77d714969deaafe1fb8`

## Frozen assembly

The prospectively frozen replacement assembly is

`H5 = A + I - 2 sqrt(-g) D5`,

where `D5` is the independently validated nested five-point covariant double-divergence operator. No coefficient fitting, sign search, or post-result threshold adjustment was performed.

## Frozen panel and result

The workflow consumed all 16 expected raw lane artifacts:

- A: 4 fresh generic polynomial four-dimensional metrics;
- B: 6 fresh anisotropic Bianchi-I exact-target variational tests;
- C: 3 conformally-flat curved null controls;
- D: 3 coordinate-covariance tests.

All 16 lanes were valid and all 16 passed.

Frozen aggregate classification:

`PASS_SCOPED_G51C_D3_FIVEPOINT_FULL_EOM_REPLACEMENT_CERTIFICATE`

Aggregate diagnostics:

- passes/fails: `16/0`;
- worst A final-step change: `1.5516325058248675e-08`;
- worst B component relative residual: `5.0113399264437624e-09`;
- worst B vector relative residual: `4.36189564337193e-09`;
- minimum historical `A+I+2D` B residual: `1.8708048537449804`;
- worst conformally-flat C `H` norm: `1.7521251266667764e-39`;
- worst D covariance relative residual: `3.6984734831049934e-09`.

Representative raw witnesses were inspected, not just the green CI result. B3 gave component residuals approximately `1.31e-12`, `5.87e-10`, `2.53e-10` and vector residual `4.19e-10`, while the historical `+2D` assembly had residual `1.9908`. D1 gave covariance residual `3.6985e-09` with nonzero `H` norm `0.08951`.

## Interpretation

This closes the prospectively defined finite D3 computational replacement panel and strongly supports the `-2D5` assembly on the tested generic, anisotropic, null, and covariance sectors. It does **not** rewrite the historical G51C or D2 failures; both remain durable terminal results under their original frozen contracts.

This is still a finite computational certificate. It does not establish a global theorem for arbitrary four-dimensional metrics, does not by itself establish the full covariant functional derivative of the action, and does not establish QGR correctness.

## Claim locks

- `theory_established_pct = 0`;
- `c6` remains symbolic/unfixed;
- `beta=1` is not authorized as physics;
- no experimental confirmation;
- absolute energy positivity and quantum unitarity are not established;
- full covariant six-derivative EOM remains unestablished pending a genuinely four-dimensional directional/full-functional-derivative certificate.
