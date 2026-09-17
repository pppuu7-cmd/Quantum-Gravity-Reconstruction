# Corrected degree-eight Weyl3 source reconstruction — repaired production

Date: 2026-09-17

Gate: `CORRECTED_DEGREE8_WEYL3_SOURCE_RECONSTRUCTION`

Science preregistration: `ddf4d41be23b09e5a4709149d85d85688a533fab`

Execution-only repair preregistration: `53d973eefede199dc1b6f9525c99d21ee0341660`

Repaired workflow commit: `81b88fef9ab0c377a72fbe12f1fb86620a960f2b`

Authoritative repaired Actions run: `35268357568`

Execution carrier head: `4073cc9f601dbfe91e7dedbb392de0c342e79a58`

Jobs:
- primary: `105361102644` — terminal failure after producing a raw JSON summary in the job log;
- independent: `105361102924` — terminal failure after producing a raw JSON summary in the job log;
- historical comparator: `105361103019` — terminal failure;
- frozen terminal classifier: `105366943772` — completed and classified the run.

Terminal artifact: `10517589050`

Terminal artifact ZIP digest: `sha256:a3c58fd7017e3a57da44d29c776ec7a591e140056c828448c5b9dc20f0b0dbe3`

Terminal payload SHA256: `11afef81ffcc20b58ff54738010ad345a27ad33820c7a1ad5aace37d2e8d5d11`

Frozen terminal classification: `BLOCKED_CORRECTED_DEGREE8_SOURCE_EXECUTION`.

## Raw-lane evidence consumed

The execution-only dependency/pipefail defect from run `35268178559` was repaired: Python 3.11 installed `sympy==1.14.0`, and both corrected lanes reached the scientific constructor and emitted deterministic summaries.

Both corrected lanes independently returned the same control failure:

- `degree6_projection_hash_equals_AT = false`;
- computed degree-six vector SHA256 = `2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d`;
- frozen Iter057AT ordered 840-vector SHA256 = `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- all reported intrinsic P controls passed, including antisymmetries, pair exchange, algebraic Bianchi, and `P·R = 3 I3` through the frozen orders;
- Ricci/scalar/Einstein seed controls passed;
- standard source symmetry passed;
- `c6 = SYMBOLIC_UNFIXED_FACTORED_OUT`;
- historical Iter057AA/Iter057X target was not loaded in either corrected lane.

Both lanes also independently produced the same provisional degree-eight hashes before rejecting themselves on the frozen AT-reduction control:

- standard degree-eight vector SHA256 `ca2689a43edc984c4d0aff25789b48438e1d58be183597123ee88b67345d836a`;
- Y-format minus vector SHA256 `26d576c1578e5f62458259203c4562cd5bafdb7be947a238cd0a37249d3f757e`;
- 260 nonzero degree-eight coefficients.

These degree-eight values are **not authoritative scientific results** because the prerequisite exact reduction to Iter057AT failed.

The terminal job found zero lane artifacts because the lane scripts exited nonzero before their upload steps. Therefore its frozen classification `BLOCKED_CORRECTED_DEGREE8_SOURCE_EXECUTION` is preserved. Green/failed CI status alone is not used as scientific classification.

## Scientific interpretation and next lock

This run does not establish or refute a corrected degree-eight Weyl3 source. It establishes a reproducible discrepancy between the generalized through-degree-eight constructor and the frozen Iter057AT degree-six authority. Because primary and independent lanes agree on the discrepant degree-six hash, the next useful gate must be a prospective, target-blind **degree-six reduction discrepancy localization**. It must compare the generalized constructor's degree-six projection to the durable AT 840-vector only after freezing diagnostic decompositions, and must not alter signs, normalization, source convention, thresholds, or the Iter057AT authority post hoc.

No corrected Q10 replay is authorized. No historical Iter057AA survival/difference classification is authorized.

Claim locks remain unchanged: theory established = 0%; no experimental confirmation; beta=1 unauthorized; c6 symbolic/unfixed; no global theorem, quantum unitarity, regulator removal, UV completion, or KMQGB NEW_REQUIRED claim is authorized.
