# Iter053 run authority

Gate: `ITER053-WEYL3-INTEGRATED-COMPACT-SUPPORT-ACTION-VARIATION`

## Initial production — numerical/infrastructure failure, not scientific classification
Authoritative production head: `7c88a797e12968cba8f0804292e348bf82784014`
Run: `34750610751`
Aggregate job: `103750238843`
Summary artifact: `10320808113`
Digest: `sha256:e6cccea46c99d1f93cf440f0d39a78bfe96dfc7f21eebacaa68690797fd0f3bc`

Frozen aggregate classification: **`ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`**.

Evidence consumed: 6/8 lane artifacts (A4+B2); C0/C1 were cancelled by hosted-runner wall-clock/resource exhaustion. The four generic A lanes were valid controls but numerically unresolved under the frozen outer-box GL3/GL4 rule. Representative A0: direct epsilon derivative final-step change `1.1769644781427364e-12`, while bulk coarse-to-fine relative change was `0.8939841560959314`; direct-vs-bulk fine residual `1.096109899568205`. This is not authorized as a scientific failure because the preregistered classifier explicitly separates numerical/infrastructure failure.

The historical Iter053 frozen science, thresholds, seeds, perturbations, quadrature orders and negative-control conditions remain unchanged. No evidence from this run may be pooled into a fresh scientific authority.

## Wall-clock-only implementation repair
Commit `4e95a8dbba3967d18f86206681bbfda46b54699e` parallelized the two independent frozen C covariance evaluations after the original C jobs hit hosted-runner wall-clock limits. It did not change seeds, points, orders, thresholds, epsilon stencil, H5 step, perturbations, action, or classifier.

Fresh retry trigger/head: `cf3466b3f0394952c384f7cfcc5bc445e7bbd4b5`
Fresh retry run: **`34769958632`**.

The fresh retry is independent authority. Do not combine it with run `34750610751`.

## Parallel numerical diagnosis
A separate preregistered diagnostic, `ITER053-QD-COMPACT-SUPPORT-QUADRATURE-CONDITIONING`, is allowed to diagnose the numerical failure but cannot reclassify Iter053. Its preregistration is `8625318f69e3104b4dc67ada0f716394fb775de5`; production run `34770383463`.

Claim locks remain: `theory_established_pct=0`; `c6` symbolic/unfixed; `beta=1` unauthorized; finite computational evidence is not a global theorem or complete quantum gravity.
