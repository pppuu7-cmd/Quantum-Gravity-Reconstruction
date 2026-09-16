# Iter057AJ — Exact symmetry-sector uniqueness of the scalar dual certificate

Status: PROSPECTIVELY PREREGISTERED; no Iter057AJ rank/dimension evidence exists at this commit.  
Date: 2026-09-16.

## Purpose

Determine whether the terminal Iter057AI single scalar generator is uniquely selected up to overall scale inside the exact symmetry sector terminally identified by Iter057AH, rather than being one arbitrary representative among several independent certificates with the same support/symmetry.

This is a structural analysis of the already-frozen Iter057AF obstruction map and Iter057AG/AH/AI witness. It is not a new branch search and does not alter the scientific object.

## Frozen inputs

Consume exactly:

- Iter057AF complete exact obstruction object `B : Q^1114 -> Q^1456` and canonical `O0`, with authority `data/ITER057AF_EXACT_OBSTRUCTION_RANK_AUTHORITY.json` at commit `cb9120f7228a6083e62f2bb51c447f97a81870c2` and its immutable source artifacts;
- Iter057AG canonical dual witness `data/ITER057AG_CANONICAL_DUAL_WITNESS.json`, authority commit `79f447491834eaa67c2516d50433be619f098dd2`;
- Iter057AH localization authority corrected at `e4c82732af6a0a150c5f2aa245e58a63b2d09c13`;
- Iter057AI terminal compression authority `data/ITER057AI_SINGLE_GENERATOR_COMPRESSION.json` at commit `ae566abe0115a0616bfe20f328b0865b84110cfd` and terminal result `67b3e3bb95c3d29681249d8ca469e0ee035c0a95`;
- the unchanged Iter057AD compatibility ordering `b=0,1,2,3` with degree-11 multi-indices in canonical `z.alphas(11)` order.

No witness rescaling except for explicit final normalization, no support pruning, no basis mutation, no post-hoc symmetry choice, no numerical tolerance, and no change to `B` or `O0` is permitted.

## Frozen sectors

Define `S_parity` as the 56 compatibility coordinates with:

- `b=0`;
- degree-11 multi-index `alpha=(t,x,y,z)` having parity `(1,0,0,0)`.

This is exactly the full support sector terminally identified by Iter057AH.

Define `S_S3` as the exact fixed subspace of `S_parity` under all six permutations of the three spatial exponents `(x,y,z)`. Construct its basis prospectively by orbit sums of canonical monomials; do not infer the basis from the Iter057AG coefficients.

Let `P_parity` and `P_S3` be the exact embedding matrices into `Q^1456`.

## Exact tests

Compute with exact rational/integer arithmetic:

1. `C_parity = B^T P_parity` and its exact rank/nullity.
2. `C_S3 = B^T P_S3` and its exact rank/nullity.
3. The restriction of the canonical obstruction functional `O0^T` to `ker(C_S3)`.
4. Reconstruct the Iter057AG canonical witness in both sector coordinate systems and verify direct exact membership in `ker(C_parity)` and `ker(C_S3)`.
5. If `nullity(C_S3)=1`, construct the primitive exact generator of that one-dimensional kernel independently from the AG coefficients, normalize it by `O0^T y=1`, and compare coefficient-by-coefficient with the terminal Iter057AG witness / Iter057AI scalar generator.
6. Independently replay `B^T y=0` and `O0^T y=1` in the original 1456/1114 coordinates.

## Decision rule

PASS is authorized only if:

- all frozen provenance and coverage controls pass;
- `S_parity` has exactly 56 coordinates;
- the independently constructed `S_S3` orbit-sum basis is complete and exact;
- `nullity(C_S3)=1`;
- `O0` is nonzero on that one-dimensional kernel;
- the independently reconstructed normalized generator equals the terminal Iter057AG/AI generator exactly;
- original-coordinate replay gives `B^T y=0` and `O0^T y=1` with no tolerance.

PASS label:

`PASS_SCOPED_ITER057AJ_S3_PARITY_SECTOR_DUAL_CERTIFICATE_UNIQUE_UP_TO_SCALE`

If the exact `S3`-invariant kernel dimension is not one, or the normalized independent generator differs from frozen AG/AI authority while all provenance controls pass, classify:

`SCIENTIFIC_FAIL_SCOPED_ITER057AJ_S3_PARITY_SECTOR_CERTIFICATE_NOT_UNIQUE_AS_PREREGISTERED`

Implementation/provenance inability is BLOCKED/INVALID, not scientific FAIL.

## Scope ceiling

A PASS would establish uniqueness only inside the prospectively frozen finite-dimensional `b=0`, odd-time/even-spatial, `S3`-invariant compatibility sector of the existing Iter057AF obstruction map. It is not uniqueness among all possible left certificates, not an all-orders/global theorem, and not a physical symmetry/gauge/stability statement.

Claim locks remain unchanged: theory established `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no c6 running/fitting; no quantum unitarity, regulator removal, UV completion, strong hyperbolicity, physical-ghost/stability or KMQGB `NEW_REQUIRED` claim is authorized.
