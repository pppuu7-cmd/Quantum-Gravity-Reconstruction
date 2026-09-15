# Iter057X independent artifact-only reproduction

Date: 2026-09-16

Gate: `ITER057X-CORRECTED-DECIC-SEED-WEYL3-SIXTH-SOURCE-JET`

Frozen preregistration: `b5f88ced655c4fa409c4ccb9c27eb84054ecfad7`.

## Independence

This reproduction was completed while the official Ubuntu and Windows Iter057X Actions runs were still queued. It therefore did not consume an Iter057X production payload.

The standalone evaluator did not import the Iter057U, Iter057W, or official Iter057X implementation. It reconstructed the canonical seed from already-terminal workflow artifacts only:

- Iter057O R4 artifact `10391082054`: 21 normalized coefficients;
- Iter057Q R6 artifact `10391103676`: 69 normalized coefficients;
- Iter057T R8 artifact `10408050133`: 153 normalized coefficients;
- Iter057W R10 artifact `10423276358`: 283 normalized coefficients;
- terminal Iter057U artifact `10415573459`: 90 source coefficients at degrees 0/2/4, used only for the frozen lower-source replay.

The quadratic base seed was reconstructed with `kappa=2/25` and the already-frozen G2 polynomial. All polynomial and tensor arithmetic used Python `Fraction`; no floating zero/rank tolerance was used.

## Exact result

Classification:

`PASS_SCOPED_ITER057X_CORRECTED_DECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_SIXTH_EVEN_ORDER__O_C6_Q8_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED`

Source nonzero counts by coordinate degree:

- degree 0: 4;
- degree 1: 0;
- degree 2: 22;
- degree 3: 0;
- degree 4: 64;
- degree 5: 0;
- degree 6: 140.

Degree-six source statistics:

- nonzero normalized coefficients: `140`;
- time-containing: `82`;
- off-diagonal: `60`.

`I3(0)/kappa^3 = 96`.

Canonical JSON serialization of the complete sparse source has SHA-256:

`7992941270ddae93bb4540ced0c03c9bdb1427b0c2d665c4e27720ea86a798fd`.

The complete result JSON has SHA-256:

`15241042ad0a17ce4c778e19cc18757a185e4bd430e351f4bd9b76965a8c37b7`.

A second clean execution produced a byte-identical complete result JSON and the same two digests.

## Frozen controls

Every preregistered scientific control passed exactly:

- canonical R4/R6/R8/R10 artifacts passed and all layers were pure/unique at degrees 4/6/8/10;
- exact R10 count = 283;
- inverse identity through coordinate degree 8;
- Ricci tensor, scalar curvature and Einstein tensor exactly zero through degree 8;
- direct tensor construction of the Weyl3 Euler source through degree 6;
- `P.R = 3 I3` exactly through degree 6;
- lowered Euler tensor symmetric exactly through degree 6;
- trace Ward identity exactly through degree 6;
- covariant Noether divergence exactly zero through degree 5;
- all source coefficients at odd degrees 1, 3 and 5 exactly zero;
- terminal Iter057U degree-0/2/4 source replay exact coefficient-by-coefficient, with no missing, extra or unequal values;
- complete symmetric-tensor basis accounting `10+40+100+200+350+560+840 = 2100`.

## Scope

This is an independent reproducibility certificate, not yet an official main-branch terminalization. The official Iter057X runs must still be consumed independently when they complete.

The result establishes only the finite local corrected-seed Weyl3 Euler source through coordinate degree six. It does not solve the next O(c6) Q8 response, fix/sign-select/run `c6`, establish an all-orders or convergent solution, or authorize any physical/quantum completion claim. `c6` remains symbolic/unfixed and theory-established remains `0%`.
