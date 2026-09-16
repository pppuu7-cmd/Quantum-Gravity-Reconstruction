# Iter057AH — terminal exact dual-witness localization and factorization

Gate: `ITER057AH-EXACT-DUAL-WITNESS-LOCALIZATION-AND-FACTORIZATION`  
Status: `TERMINAL_SCOPED_PASS_EXACT_PRODUCTION_CONSUMED`  
Date: 2026-09-16

## Frozen authority

- Preregistration: `9b55fb87f89456bb04d325c534cde025fcb9ad2e`.
- Implementation: `d93b3d3d19309b38c88ff4cd6e24af3ffb51ef4e`.
- Production head: `0945a9d6b5a1ae07cb60e11c20fc28b34d4e46c0`.
- Actions run/job: `35135590952` / `104927026773`.
- Raw artifact: `10462769190`, digest `sha256:ef06b9673ebf0de3d78c8dea8a773194811e7624e857ba34c97b4cf7ae57b5ea`.
- Scientific payload SHA256: `8e7c74aa9d5c154f5be7fb8bcc8f0db8937e5a605d983ea20bf9fad067b9d661`.
- Durable localization summary: `data/ITER057AH_DUAL_WITNESS_LOCALIZATION.json`, corrected summary commit `e4c82732af6a0a150c5f2aa245e58a63b2d09c13`.

The raw artifact passes every prospectively frozen localization, reconstruction, factorization, grouping, provenance, and exact-zero control.

## Exact localization of the Iter057AG witness

The canonical Iter057AG dual witness has 56 nonzero compatibility coordinates. Under the frozen Iter057AD `left_controls` ordering, all 56 lie in the single compatibility component

`b = 0`.

Every nonzero degree-11 multi-index has parity

`(t,x,y,z) mod 2 = (1,0,0,0)`.

There are exactly 56 degree-11 four-variable monomials with this parity, so the witness support is the complete odd-time/even-spatial parity sector of the `b=0` compatibility block.

The four generating polynomials satisfy

- `Y_0 != 0`, with 56 terms;
- `Y_1 = Y_2 = Y_3 = 0`.

Exact factorization over `Q[t,x,y,z]` extracts one common factor `t`:

`Y_0 = (457763671875 / 46315224704) * t * Q_10(t,x,y,z)`,

where `Q_10` is a primitive integral degree-10 polynomial. The production exact factorization routine finds no further rational polynomial factor. The complete expanded/factorized/primitive strings are serialized in the raw artifact and covered by the scientific payload hash; the durable summary stores their SHA256 digests to avoid transcription ambiguity.

Direct equality under all six permutations of `(x,y,z)` holds. Thus the exact spatial permutation stabilizer is the full `S_3` of order 6. This is a discrete symmetry statement of this certificate only; no continuous rotational or physical symmetry claim is inferred from it.

## Original affine-row localization

The induced exact witness `w^T = y^T L` has 308 nonzero affine-row coefficients, localized as:

- 84 gauge rows, all in `G_0`;
- 224 field rows, split equally as 56 each in `F_00`, `F_01`, `F_02`, `F_03`;
- no other gauge component or field tensor pair occurs.

Exact RHS contribution accounting gives:

- all gauge rows together: `0`;
- all field rows together: `1`;
- total: `1`.

By field component:

- `F_00`: `-565221982/3256539237`;
- `F_01`: `1765158751/6513078474`;
- `F_02`: `1765158751/6513078474`;
- `F_03`: `685534156/1085513079`.

These four rational contributions sum exactly to `1`. The exact replay remains

`B^T y = 0`, `O0^T y = 1`, `w^T M14 = 0`, `w^T r0 = 1`.

Therefore the finite-order obstruction is localized entirely in the time-indexed compatibility/affine-row sector of the frozen construction, while the gauge-row part of the left witness is required for annihilation of `M14` but contributes zero to the canonical right-hand side.

## Terminal classification

`PASS_SCOPED_ITER057AH_EXACT_DUAL_WITNESS_LOCALIZED_AND_FACTORIZED_WITH_ORIGINAL_SYSTEM_ACCOUNTING`

## Scope ceiling

This result localizes and compresses the already-established finite local Iter057AF/AG obstruction certificate. It is not a new branch obstruction beyond the frozen orders, not an all-orders/global theorem, and not a physical gauge-mode or causal-stability conclusion.

Claim locks remain unchanged: theory established `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no c6 running/fitting; no quantum unitarity, regulator removal, UV completion, strong-hyperbolicity, physical-ghost/stability, or KMQGB `NEW_REQUIRED` claim is authorized.
