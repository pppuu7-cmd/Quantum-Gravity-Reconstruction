# Iter057AJ — terminal exact symmetry-sector uniqueness

Gate: `ITER057AJ-SYMMETRY-SECTOR-UNIQUENESS`  
Status: `TERMINAL_SCOPED_PASS_EXACT_PRODUCTION_CONSUMED`  
Date: 2026-09-16

## Frozen authority

- Preregistration: `1ba092655a159dfa8dea5d9d0832346ff451dda0`.
- Implementation: `444e26abb153f4d5912ac196b45758565d4a3110`.
- Production head: `698321a7dab2ce0e118466bbd20e5ff0424c008a`.
- Actions run/job: `35140088767` / `104942150184`.
- Raw artifact: `10465106571`, digest `sha256:98ae15cf1dd9e2bc8a9180d5816a5b4896f28961a536fc2bf9bf2d9b8c440bb2`.
- Scientific payload SHA256: `aa628c5b328ccc4b21e69864c9de080a50814725158e0d645545c8329aa71e98` (independently recomputed from the 2221-byte canonical payload with the hash field removed).
- Durable authority: `data/ITER057AJ_SYMMETRY_SECTOR_UNIQUENESS.json`, commit `bc09581da51fc9ad0e04a4cc8b1eb6a66def60dd`.

## Exact result

The prospectively frozen Iter057AH support sector consists of exactly 56 compatibility coordinates: `b=0` and degree-11 parity `(t,x,y,z) mod 2 = (1,0,0,0)`.

Using the complete immutable Iter057AF obstruction matrix `B`, the restricted exact dual system

`C_parity = B^T P_parity`

has

- shape `1114 x 56`;
- `nnz = 2241`;
- exact rank `55`;
- exact nullity `1`.

Therefore the dual certificate is already unique up to scale in the full 56-dimensional odd-time/even-spatial `b=0` parity sector, before imposing spatial permutation symmetry.

Independently constructing the exact fixed subspace under all six spatial permutations gives a 16-dimensional `S3` orbit-sum basis. The compressed system

`C_S3 = B^T P_S3`

has

- shape `1114 x 16`;
- `nnz = 1187`;
- exact rank `15`;
- exact nullity `1`.

Thus imposing `S3` does not choose one direction from a larger parity-sector kernel. Rather, the unique parity-sector kernel direction is itself `S3` invariant.

## Independent generator reconstruction

The one-dimensional kernel was constructed from `B` without using the Iter057AG witness coefficients. Its primitive integer coefficient vector is

`[231,63,35,35,63,231,63,21,15,21,63,35,15,15,35,35,21,35,63,63,231,-126,-42,-30,-42,-126,-42,-18,-18,-42,-30,-18,-30,-42,-42,-126,105,45,45,105,45,27,45,45,45,105,-140,-84,-140,-84,-84,-140,315,315,315,-1386]`.

Before normalization its exact obstruction pairing is

`O0^T y_primitive = -3308230336/45318603515625 != 0`.

After exact normalization to `O0^T y=1`, the independently reconstructed 1456-coordinate witness agrees coefficient-by-coefficient with the terminal Iter057AG witness and therefore with the Iter057AI scalar generator. Direct replay gives

- `B^T y = 0` in all 1114 branch coordinates;
- `O0^T y = 1` exactly;
- no numerical tolerance.

A separate local exact reconstruction directly from the eleven raw AD/AF column artifacts obtained the same structural ranks; its frozen structural payload SHA256 is `83c84b82b8b9f851a4dcc7f7eb6cd3775c6fa96226b7eea25fbe2d3a8068a331`.

## Terminal classification

`PASS_SCOPED_ITER057AJ_S3_PARITY_SECTOR_DUAL_CERTIFICATE_UNIQUE_UP_TO_SCALE`

This strengthens only the structural understanding of the existing finite-order Iter057AF/AG obstruction certificate. It establishes uniqueness inside the prospectively frozen 56-dimensional parity sector; it is not uniqueness among all possible certificates, not an all-orders/global no-go theorem, and not a physical rotational/gauge/stability conclusion.

Claim locks remain unchanged: theory established `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no c6 running/fitting; no quantum unitarity, regulator removal, UV completion, strong hyperbolicity, physical-ghost/stability or KMQGB `NEW_REQUIRED` claim is authorized.
