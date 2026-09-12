# Iter051A — Weyl3 algebraic metric-density variation

Date: 2026-09-13

## Frozen gate
Parent preregistration: `bf5615dd36b533ba536c85f4c8d7658cd7e3568c`.
Implementation: `307b4bd66a54a03fb7162c069e9d3e5fc4928d53`.
Frozen aggregate: `4cbe7971910d3108472e4ce08026a783fecca82f`.
Authoritative production head: `55e4c099516cbfe9a76ab826994cc5f28cae69c0`.

The gate tested the local algebraic metric/measure/projector variation of `sqrt(-g) C^3` on 12 generic nonsymmetry-reduced lanes. The preregistered lane criterion required valid Lorentz signature/algebraic controls, covariance controls, complex-step versus centered-finite-difference agreement, and the frozen finite-difference convergence condition. Criteria are not changed after observing the result.

## Authoritative terminal provenance
- run: `34724233650`
- aggregate job: `103635469747`
- aggregate artifact: `10307431104` (`qgr-iter051a-summary`)
- artifact digest: `sha256:17b0d975691abdee5e7cbf4fa45198f7f6b3c8e0136a017c7b3cb8c5902e8a33`
- expected/found lanes: `12/12`
- lane-level PASS: `5/12`
- nonzero calibration: `12/12`

Aggregate extrema:
- max algebraic residual: `8.326672684688674e-17`
- max Weyl-trace residual: `1.1102230246251565e-16`
- max density-covariance relative discrepancy: `1.4471991837432272e-14`
- max directional-covariance relative discrepancy: `3.355094633829336e-14`
- max finest-step complex-step/FD relative discrepancy: `1.6407915760785562e-09`

## Scientific classification
`SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`

This is a failure of the frozen G51A gate because only 5/12 lanes satisfy every preregistered criterion. Green lane jobs are not interpreted as scientific PASS; the aggregate classifier is authoritative.

The raw lane evidence localizes at least one failing lane (lane 0) to the frozen finite-difference convergence predicate: algebraic, Weyl-trace, covariance, signature and nonzero controls pass, and the finest complex-step/FD relative discrepancy is ~`1.13e-9`, but the smallest-step centered-FD error rises after reaching a smaller error at a coarser step. The gate remains failed; this observation does not authorize weakening or replacing its convergence requirement.

## Scope and claim locks
- No full covariant Weyl3 Euler-Lagrange tensor is established.
- `c6` remains symbolic and unfixed.
- Theory established remains `0%`.
- This terminal result does not invalidate Iter050's narrower fixed-metric curvature-direction prerequisite.
- A separately preregistered numerical-order diagnostic may determine whether the 7/12 G51A failures are consistent with centered-FD roundoff turnover, but such a diagnostic cannot retroactively convert G51A to PASS.
