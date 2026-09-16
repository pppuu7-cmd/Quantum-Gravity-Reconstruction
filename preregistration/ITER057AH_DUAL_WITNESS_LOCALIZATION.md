# Iter057AH — Exact Dual-Witness Localization and Factorization

Status: PROSPECTIVELY PREREGISTERED; no Iter057AH implementation or production evidence exists at this commit.  
Date: 2026-09-16.

## Purpose

Localize and compress the already-terminal Iter057AG exact dual obstruction certificate into its tensor/monomial structure. This gate is interpretive and reproducibility-oriented: it does not reopen Iter057AF, does not search for a new branch, and does not change the scientific object.

## Frozen inputs

Consume exactly:

- Iter057AF terminal result `230690a56e5055471054d9751985f7604ec7130d`;
- Iter057AG preregistration `11dfc1e4db79ff691fe121ab38281f3532f931bf`;
- Iter057AG terminal canonical witness `data/ITER057AG_CANONICAL_DUAL_WITNESS.json` frozen at `79f447491834eaa67c2516d50433be619f098dd2`;
- Iter057AG terminal result `results/ITER057AG_DUAL_OBSTRUCTION_WITNESS_TERMINAL.md` frozen at `057f6c9699c1e81cfe3042a711715bc65850f6e3`;
- the unchanged Iter057AD/Iter057AC ordering functions `left_controls`, `rhs14`, and `system`.

No witness rescaling, support reduction, coordinate reordering, mode deletion, branch refit, numerical tolerance, or c6 choice is permitted.

## Deterministic localization tasks

1. Map every nonzero canonical dual coordinate `y_i` to the exact compatibility metadata `(b,beta)` implied by the frozen `left_controls` row order: `b=0..3`, then lexicographically ordered degree-11 four-variable multi-index `beta`.
2. Construct, for each `b`, the exact rational generating polynomial

   `Y_b(t,x,y,z) = sum_beta y_(b,beta) t^beta_t x^beta_x y^beta_y z^beta_z`.

   Compute its exact symbolic factorization over `Q`; also serialize a primitive-integer normalization with a positive common denominator convention. Factorization is a reported outcome, not a pass/fail target.
3. Independently reconstruct the full canonical `y` from the localized `(b,beta,value)` table and require exact equality with the frozen Iter057AG data.
4. Reconstruct the induced witness `w^T=y^T L` and map each nonzero affine row to frozen Iter057AC metadata: gauge rows `('G',b,alpha13)` and field rows `('F',(a,b),alpha12)`.
5. Compute exact support counts and exact contributions `w_i r0_i` grouped by row type, tensor component/pair, and monomial parity class. The grouped contributions must sum exactly to `w^T r0=1`.
6. Verify directly and exactly again that `B^T y=0`, `O0^T y=1`, `w^T M14=0`, and `w^T r0=1`; no numerical zero test is allowed.
7. Determine the exact stabilizer of the tuple `(Y_0,Y_1,Y_2,Y_3)` under all six permutations of the spatial variables `(x,y,z)` by direct symbolic equality, and report it without imposing a desired symmetry.

## PASS / INVALID / BLOCKED

PASS requires successful exact localization, exact witness reconstruction, exact grouped-contribution accounting, exact residual replay, and exact polynomial reconstruction/factorization serialization.

PASS label:

`PASS_SCOPED_ITER057AH_EXACT_DUAL_WITNESS_LOCALIZED_AND_FACTORIZED_WITH_ORIGINAL_SYSTEM_ACCOUNTING`

INVALID is reserved for contradiction with the frozen Iter057AG witness or ordering/provenance. BLOCKED is reserved for technical inability to realize the deterministic localization without changing the object.

## Scope ceiling

Any structure or factorization found is a property of this frozen finite local Taylor-jet obstruction certificate only. It is not a global/all-orders no-go theorem or a physical mode-selection result. It does not fix `c6`, authorize `beta=1`, or establish experimental confirmation, quantum unitarity, regulator removal, UV completion, strong hyperbolicity, physical ghosts/stability, or KMQGB `NEW_REQUIRED`.
