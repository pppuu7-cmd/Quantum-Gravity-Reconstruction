# Iter057AG — terminal exact dual obstruction witness

Gate: `ITER057AG-EXACT-DUAL-OBSTRUCTION-WITNESS`  
Status: `TERMINAL_SCOPED_PASS_EXACT_PRODUCTION_REPRODUCED`  
Date: 2026-09-16

## Frozen authority

- Preregistration: `11dfc1e4db79ff691fe121ab38281f3532f931bf`.
- Primary implementation: `b5061677948d88f26756ef73834877ea19f3c1a8`.
- Primary production head: `37541d1d79563a36041d608cfc348c83c6c481c2`.
- Primary Actions run/job: `35134514563` / `104923416472`.
- Primary raw artifact: `10462603134`, digest `sha256:0bbb9a73aad28186c56d321802de588d803b217d644bf96c68709d2611b72425`.
- Independent integer-cleared RREF implementation: `f3a4a2e0adb1eb17b41cc58c642260f09fb6f4a8`.
- Independent production head: `ae9a4d3028b3103b32a32d45890035c5cf46e9b9`.
- Independent Actions run/job: `35134804154` / `104924391091`.
- Independent raw artifact: `10462823185`, digest `sha256:5585d48124fb1525946452e9134ac4d7659ec34c98ab418d63b08e5c29f9354c`.
- Canonical durable witness data: `data/ITER057AG_CANONICAL_DUAL_WITNESS.json`, frozen at commit `79f447491834eaa67c2516d50433be619f098dd2`.

The two production lineages serialize the same complete scientific payload, with identical ordered canonical `y`, identical induced `w`, identical controls, and the same scientific payload SHA256:

`5ecb962af9a1265a8846a6d8de4cd0885c2b53bea630a5729a8c069aae9fd9da`.

## Exact certificate

Iter057AF established for the complete frozen branch map

`O(h) = O0 + B h`,  with `B : Q^1114 -> Q^1456`,

that

- `rank(B) = 1110`,
- `rank([B|-O0]) = 1111`,
- `B_nnz = 80,982`,
- canonical `O0` has 223 nonzero compatibility coordinates.

Iter057AG constructs the prospectively normalized exact rational dual witness `y in Q^1456` as the free-variables-zero solution of the exact RREF system

`B^T y = 0`,

`O0^T y = 1`.

The canonical witness has **56 nonzero rational coordinates**. Direct exact replay gives:

- `B^T y = 0` in all 1114 branch coordinates;
- `O0^T y = 1` exactly;
- normalized witness-system rank = `1111`;
- no numerical tolerance is used.

The induced original affine-row witness

`w^T = y^T L`

has **308 nonzero rational coefficients**. Independent direct exact replay gives:

- `w^T M14 = 0` in all 6800 R14 columns;
- `w^T r0 = 1` exactly.

Thus the finite-order incompatibility is certified directly: if an exact solution of the frozen branch-corrected R14 affine problem existed, multiplying its equation by `w^T` would give `0 = 1`.

## Terminal classification

`PASS_SCOPED_ITER057AG_EXACT_DUAL_OBSTRUCTION_WITNESS_CERTIFIES_ITER057AF_BRANCH_INCONSISTENCY`

This PASS certifies the already-terminal Iter057AF finite-order scientific FAIL; it does not reverse it and does not create a branch lift.

## Scope ceiling

The certificate applies only to the prospectively frozen finite local Iter057AD/Iter057AF Taylor-jet construction and ordering. It is not an all-orders or global no-go theorem, does not rule out differently prospectively defined scientific objects, and does not establish or refute quantum gravity as a whole.

Claim locks remain unchanged: theory established `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no c6 running/fitting; no quantum unitarity, regulator removal, UV completion, strong-hyperbolicity, physical-ghost, or KMQGB `NEW_REQUIRED` claim is authorized.
