# QGR Iter007-G6A — joint history composition and local/global scaling

Date: 2026-09-12
Status: `PASS_SCOPED_COMPOSITION_AUDIT / JOINT_HISTORY_GLUING_BLOCKED`
GitHub Actions run: `34653478008`
Head: `f6327f8505443c96c652bb4a30ca9dbc8f9828ed`

## Objective

Determine whether the four-dimensional marginality warning from G5B already implies a local continuum decoherence/Lorentz-violation prediction, and determine how much of the cross-cell history law is fixed by the exact local `1/24` normalization.

Three independent GitHub Actions lanes plus the aggregate completed successfully.

## G6A.1 — local marginals do not determine the joint history law

Let `s_pi` be the six pair-order signs of a local `B4` history. Construct three exact two-cell joint laws, each with **exactly uniform `1/24` marginal history probability in each cell**:

1. product: `p(pi,sigma)=1/576`;
2. synchronized: `sigma=pi`, weight `1/24`;
3. reversed: `sigma=reverse(pi)`, weight `1/24`.

All three satisfy the same local history normalization.

For the covariance of the summed pair-sign displacement, the exact variance traces are

- product: `12`;
- synchronized: `24`;
- reversed: `0`.

The reversed law cancels the second-order ordering displacement exactly because every pair sign changes sign under total order reversal.

Classification:

`BLOCKED_LOCAL_1_OVER_24_HISTORY_NORMALIZATION_DOES_NOT_FIX_CROSS_CELL_CORRELATIONS`.

Interpretation: local normalization alone cannot authorize a network decoherence coefficient. In particular, choosing the reversed/anticorrelated law now in order to cancel the finite-cell effect would be a forbidden post-hoc rescue.

## G6A.2 — natural Boolean compositions

Two simple global completions already compatible with the local Boolean language were enumerated exactly.

### Serial ordinal sum

Two causal `B4` cells in strict sequence have

`24 * 24 = 576`

global maximal chains, corresponding to free choice of one local permutation in each cell.

### Disjoint concurrent completion

Treat two disjoint four-generator cells as one `B8` global Boolean order. There are

`8! = 40320`

global maximal chains.

For every pair of local `B4` orders there are exactly

`C(8,4)=70`

interleavings. Thus the restrictions of a uniform global `B8` chain to the two local cells are exactly product-uniform.

Classification:

`PASS_SCOPED_NATURAL_SERIAL_AND_DISJOINT_BOOLEAN_COMPOSITIONS_DO_NOT_GENERATE_CANCELLING_LOCAL_ORDER_CORRELATIONS`.

Boundary: adjacent overlapping cells with shared microscopic events are not specified by the current local `B4` construction. Their gluing law is the missing microscopic object.

## G6A.3 — local versus extensive/global purity

The G5B four-volume stress test sequentially applied `O(b^4)` small-cell channels to the same two-level carrier. This correctly demonstrates that integrated channel weight can be marginal, but it does not by itself represent a spatially extended quantum field.

A separate tensor-factor stress toy was therefore evaluated:

- `b^3` independent spatial subsystems in a fixed spatial volume;
- each subsystem experiences `b` causal time-cell channels over a fixed duration;
- the same exact 24-history one-cell channel is used.

The local reduced-state purity loss scales numerically as

`b^-3`,

consistent with the one-dimensional causal-path result.

Meanwhile the global product-state extensive quantity

`-log P_global = -b^3 log P_local`

approaches a nonzero constant (about `0.03459` in the recorded toy normalization).

Classification:

`PASS_SCOPED_LOCAL_REDUCED_PURITY_RECOVERS_AS_H3_WHILE_EXTENSIVE_GLOBAL_LOG_PURITY_IS_MARGINAL`.

Thus the earlier `h^0` four-dimensional counting is an **extensive/global warning**, not a theorem that a local physical two-mode observable has finite Lorentz-violating decoherence in the continuum.

## Aggregate conclusion

The network problem is now sharply localized:

1. the local 24-history law and cell channel are fixed;
2. causal-path local purity effects are irrelevant as `h^3` in the tested regular regime;
3. natural non-overlapping Boolean compositions give product local orders;
4. cross-cell correlations are nevertheless **not fixed** by local marginals alone;
5. extensive global purity and local reduced purity have different continuum scaling.

Therefore the next required object is not an arbitrary correlation coefficient but the microscopic **overlapping-cell gluing / field-support law** of the CCRC realization.

## Active blocker

`BLOCKED_MISSING_DERIVED_OVERLAPPING_CELL_HISTORY_GLUING_AND_FIELD_SUPPORT_MAP`.

## Next gate — G6B

`QGR-ITER007-G6B-DERIVE_OVERLAPPING_CELL_GLUING_AND_FIELD_SUPPORT_FROM_CCRC`

1. define how neighboring `B4` cells share boundary/events in the same relational complex;
2. enumerate the induced global partial orders and their restrictions to local history registers;
3. derive, rather than choose, the joint history measure from composition/refinement symmetry;
4. identify which cells act on the same physical quotient fiber versus spacelike tensor factors;
5. compute local and extensive normalized observables under that derived support map;
6. accept any surviving anisotropic channel if it follows from the gluing law; do not tune cross-cell correlations to cancel it.

## Reproducibility

- `.github/workflows/qgr-iter007-g6a-history-composition.yml`
- `code/qgr_iter007_g6a_joint_history_law.py`
- `code/qgr_iter007_g6a_poset_composition.py`
- `code/qgr_iter007_g6a_spatial_factorization.py`
- `code/qgr_iter007_g6a_aggregate.py`
