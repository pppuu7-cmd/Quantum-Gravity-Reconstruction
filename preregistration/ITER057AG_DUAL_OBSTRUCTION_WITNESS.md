# Iter057AG — Exact Dual Obstruction Witness

Status: PROSPECTIVELY PREREGISTERED; no implementation or production evidence at this commit.  
Date: 2026-09-16.

## Purpose

Convert terminal Iter057AF rank inconsistency into one compact exact dual certificate that can be checked without recomputing the global rational ranks. This gate does not change or reopen Iter057AF; it certifies the already terminal finite-order obstruction by an explicit Farkas-type witness.

## Frozen scientific object

Consume exactly the terminal Iter057AF object and provenance:

- Iter057AF preregistration `564b3c18b3cf3391a72287138007aa23ebdc37b0`;
- terminal result `230690a56e5055471054d9751985f7604ec7130d`;
- frozen rank authority `data/ITER057AF_EXACT_OBSTRUCTION_RANK_AUTHORITY.json`;
- complete exact obstruction map `B` of shape `1456 x 1114`, assembled only from immutable Iter057AD lanes 0–6 and the four terminal-success Iter057AF lane-7 subshards in the same column order `0..1113`;
- canonical exact obstruction `O0=L*r0` under the unchanged Iter057AD evaluator semantics;
- terminal ranks `rank(B)=1110` and `rank([B|-O0])=1111`.

No basis/order change, lane recomputation/substitution, lower-jet refit, mode removal, numerical tolerance, c6 fixing, or scientific-object mutation is permitted.

## Deterministic witness definition

Find `y in Q^1456` satisfying

`B^T y = 0` and `O0^T y = 1`.

The normalization `O0^T y=1` is frozen prospectively; sign/scale may not be chosen after inspection.

For reproducibility the canonical witness must be the free-variables-zero solution obtained from exact rational RREF of the ordered augmented system

`[ B^T ; O0^T ] y = (0,...,0,1)^T`,

with witness coordinates ordered exactly by the frozen `1456` Iter057AD Bianchi/Noether compatibility rows. Pivot/free ordering is the natural ascending coordinate order `0..1455`. Numerical pivoting/rank decisions are forbidden.

## Required exact controls

A scoped PASS certificate requires all of the following:

1. Exact replay of the complete AF lane payload provenance, unique coverage `0..1113`, `B_shape=[1456,1114]`, `B_nnz=80982`, canonical `O0` nonzero count `223`, `L*M14=0`, lower authority true and inverse true.
2. Exact replay `rank(B)=1110` and `rank([B|-O0])=1111` or an equivalent exact consistency check on the witness system.
3. A serialized sparse canonical `y` with no floating-point values.
4. Direct independent exact residual check `B^T y = 0` in all `1114` coordinates.
5. Direct independent exact normalization check `O0^T y = 1`.
6. Form the induced original-system row witness `w^T = y^T L`; serialize its nonzero exact coefficients and verify independently that `w^T M14 = 0` in all `6800` columns and `w^T r0 = 1`.
7. Exact zero decisions use no tolerance.

If the exact canonical witness cannot be technically realized, classify BLOCKED. If any consumed terminal AF authority/control is contradicted, classify INVALID and reopen audit rather than changing the frozen criterion. This gate has no authorized scientific PASS-to-branch-lift path: Iter057AF remains terminal FAIL regardless; the purpose is only compact certification of that FAIL.

## Scoped PASS label

`PASS_SCOPED_ITER057AG_EXACT_DUAL_OBSTRUCTION_WITNESS_CERTIFIES_ITER057AF_BRANCH_INCONSISTENCY`

## Scope ceiling

A PASS is only a compact exact certificate for the frozen finite local Iter057AD/AF Taylor-jet branch problem. It is not a global/all-orders no-go theorem, does not rule out differently prospectively defined scientific objects, and does not establish or refute quantum gravity as a whole.

Claim locks remain unchanged: theory established `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no quantum unitarity, regulator removal, UV completion, strong-hyperbolicity, physical-ghost, or KMQGB `NEW_REQUIRED` claim is authorized.
