# Iter053-QD3M — Gauss-Jacobi moment/normalization audit

## Authority
- Gate: `ITER053-QD3M-GAUSS-JACOBI-MOMENT-NORMALIZATION-AUDIT`
- Prospective preregistration commit: `a1809ae3f3d55e8700546af642daf9f9f5f19c29`
- Implementation commit: `7745f253bb84e77356d96af9344255c8a7e379b0`
- Workflow commit: `881e88fc90fa4ff6be69359fec256bc2f8e486ea`
- Production head: `cc2ad005a3605a40c602e7d372e5f9ae36706b28`
- Run: `34771761543`
- Job: `103762519052`
- Artifact: `10321744441` (`qgr-iter053-qd3m-result`)
- Artifact digest: `sha256:fbfd56dfbad2293c070a49e6bc02d4d0119f13e5db84f6a10025f4dbff1d749c`

## Frozen classification
**`PASS_DIAGNOSTIC_ITER053_QD3_GAUSS_JACOBI_MOMENTS_EXACT`**

## Results
For weight `(1-u^2)^4` and the exact four-dimensional map `x=a u`, `a=0.24`:

- GJ2: 16 tensor tasks; worst 1D analytic-moment absolute error `1.1102230246251565e-16`; reflection residual `0`; mapped constant-integral relative error `7.49113563028748e-16`; production-helper physical weight-sum relative error `7.49113563028748e-16`.
- GJ3: 81 tensor tasks; worst 1D analytic-moment absolute error `2.220446049250313e-16`; reflection residual `0`; mapped constant-integral relative error `1.1985817008459965e-15`; production-helper physical weight-sum relative error `1.1985817008459965e-15`.
- All nodes were strictly inside `(-1,1)` and all weights positive.
- All frozen tolerances (`5e-14`) passed by large margins.

## Interpretation
This validates the Gauss-Jacobi `alpha=beta=4` polynomial exactness, tensor-product normalization, `a^4` Jacobian, and the production helper's task-weight normalization used by QD3. It does **not** establish QD3 weighted-H5 convergence and cannot reclassify Iter053. QD3 run `34770675902` remains the independent H5 bulk-vs-direct pilot.

Claim locks remain unchanged: `c6` symbolic/unfixed; `beta=1` unauthorized; theory established `0%`; finite diagnostics are not global theorems.
