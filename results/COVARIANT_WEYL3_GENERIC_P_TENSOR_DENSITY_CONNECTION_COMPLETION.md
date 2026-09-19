# COVARIANT_WEYL3_GENERIC_P_TENSOR_DENSITY_CONNECTION_COMPLETION — terminal result

Date: 2026-09-19

## Authority

The earlier run `35414907247` remains an immutable `BLOCKED_EXECUTION_OR_PROVENANCE` execution record. It is superseded for the frozen scientific comparison only by the prospectively preregistered execution repair below.

- scientific preregistration: `7a62dd856aec084add16af8e6793d157ef32637b`
- execution binding: `0abad7d17e3eceaed66b727cae75169a63096a9d`
- execution-repair preregistration: `7de81f357e6e8be5585ba2c1c14bd100528e5578`
- authoritative repaired production run: `35420685309`
- production head: `b692579582abc72e18124e7b8b9219da8cdf0c4c`
- source-lock job: `105837672900`
- weighted-lane job: `105837693104`
- Lane-D-reference job: `105837693114`
- terminal job: `105837713018`

## Immutable artifacts

- source-lock artifact `10577622218`, `sha256:ab15ffd2ba39eb0d01c056057dd6febe8324066ce22f191f37688cb555b11bfa`
- weighted artifact `10577467400`, `sha256:65089899f9fea90d128c126692f52e7651ce92368a8f6bca01b810984bb0acc8`
- Lane-D-reference artifact `10576743070`, `sha256:fbc54bcceafeacf219e0e5c07faf9ca6508eb19e85c85ebcb88cf6d33df3855c`
- terminal artifact `10577517264`, `sha256:0c3b3f121bee724e6a611fa8254e734b3b1c57f3d9e6ccfc9522137362248623`
- raw `terminal.json` SHA256: `ca9ef4972bc98a25eea34fab12ab8bae5acd085508f5df0a23cb331180758307`
- frozen terminal payload SHA256: `3f0f623b03ee1f829d62f53d424d390521403aa77caeb3a7066edaba720595c4`

## Frozen terminal classification

`GENERIC_P_TENSOR_DENSITY_COMPLETION_OTHER`

The prospectively frozen weight +1 tensor-density completion does **not** reproduce Lane D and does **not** reproduce its negative:

- `D_EQ_G_WEIGHTED = false`
- `D_EQ_NEG_G_WEIGHTED = false`

All frozen controls in the terminal payload are true, including exact preregistration/basis locks, reproduction of the parent Lane D and unweighted parent Lane G, a nonzero density-weight channel, and the unweighted negative control.

First direct mismatch in frozen ordering:

- monomial `P[0,1|0,1]*g2[0,0|1,1]*h[0,0]`
- Lane D coefficient `2`
- weighted coefficient `1`
- difference `1`

First mismatch against the exact-negative relation:

- monomial `P[0,1|0,1]*g2[0,0|0,0]*h[1,1]`
- Lane D coefficient `1`
- weighted coefficient `1`
- difference `2`

## Scientific scope

This is a generic formal counterexample to the tested tensor-density completion, not a global Weyl^3 theorem and not a reclassification of the immutable historical parent result. The weight +1 trace-connection term alone is insufficient to promote the corrected six-cell finite-panel certificate to a generic covariant identity. A further correction is **not authorized** by this result; any next diagnostic must be prospectively preregistered and target-blind.

Claim locks remain unchanged: `theory_established=0%`; no experimental confirmation; `c6=SYMBOLIC_UNFIXED`; `beta=1` unauthorized; corrected Q10 LOCKED; finite panels are not global theorems; no quantum-unitarity, UV-completion, physical-weight, KMQGB `NEW_REQUIRED`, or new-physics claim is authorized.
