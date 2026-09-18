# Prospective execution-only repair — QF degree-budget gate

Frozen before repair implementation.

Parent gate preregistration: `10643a75f85da4ea447d00115006d78714ecfa24`.
Blocked production: run `35289118484`, durable terminal record commit `3dfe93f716094bfa805598117e86831f58faa803`.

## Authorized repair only

The next production attempt may change only execution plumbing required to make the already-frozen script import and execute its existing dependencies:
1. set the lane `PYTHONPATH` to include `code` (the location used by the previously validated first-divergence workflow), while retaining `scripts` if needed;
2. install the same pinned SymPy dependency (`sympy==1.14.0`) used by the previously validated constructor workflow if required by those imported modules.

No scientific code, q=6..10 ladder, source operator, seed, AT target, hashes, classification logic, thresholds, signs, normalizations, coefficient values, or claim scope may change. No post-hoc sign/scale fitting. Both independent lanes and frozen aggregate remain mandatory.

The failed run is permanently technical/non-authoritative for scientific classification. The repaired attempt must receive a new run ID/head and must be classified only from its raw lane evidence and frozen aggregate.

Claim locks unchanged: theory established=0%; no experimental confirmation; beta=1 unauthorized; c6 symbolic/unfixed; corrected Q10 locked; no global theorem/unitarity/UV/new-physics claim; KMQGB NEW_REQUIRED unauthorized.
