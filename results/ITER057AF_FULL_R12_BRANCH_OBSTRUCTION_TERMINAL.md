# Iter057AF — terminal full-R12 branch obstruction result

Gate: `ITER057AF-LANE7-EXACT-PAYLOAD-COMPLETION-AND-FULL-OBSTRUCTION-RANK-DECISION`  
Status: `TERMINAL_SCIENTIFIC_FAIL_EXACT_PRODUCTION_CONSUMED`  
Date: 2026-09-16

## Prospective authority

- Preregistration: `564b3c18b3cf3391a72287138007aa23ebdc37b0`.
- Frozen lane evaluator head: `57b8e0f61e1d77c19eca09a2bd34f48921ffc020`.
- Authoritative four-shard Actions run: `35118287075`.
- Complete exact rank evaluator implementation: `f11c3a8460a0d21307af1c56a1e2fdb3ef54d329`.
- Rank-evaluator workflow head: `f56832558452631d2dd3b677c8c0149f33902ab9`.
- Rank-evaluator Actions run: `35134013268`.
- Raw rank artifact: `10462271546` (`iter057af-exact-obstruction-rank-fast`).
- Raw artifact digest: `sha256:afb1fc3fd3c5f2d664e59b855f3ba3d5fd7155af8b9670bf3724d3bcf2a76074`.
- Scientific payload SHA256: `70c7129b578489890e234e34ff6dbc483a6d13839379b03e94f2ae1ae717667a`.
- Frozen rank-authority record: `data/ITER057AF_EXACT_OBSTRUCTION_RANK_AUTHORITY.json`.

## Lane-7 exact completion

The prospectively frozen original lane-7 interval `[973,1114)` was reproduced as four deterministic exact subshards:

- `[973,1009)`: job `104869224210`, artifact `10459975843`, digest `sha256:ba390a87e432dd2a14e1390198e8f79e15170961bcf69942b8992b77f09d488c`.
- `[1009,1044)`: job `104869223437`, artifact `10462775594`, digest `sha256:fe9502483e3badd569c386ac05c47dd81a0da58d1ba9b07296189660b0355112`.
- `[1044,1079)`: job `104869223327`, artifact `10460706453`, digest `sha256:0f3ffd14506d47dedd79b535962f5ef2e53e8b2e15da125660a794d24b7a51b5`.
- `[1079,1114)`: job `104869222812`, artifact `10461754625`, digest `sha256:2119642c2a7cdfe0b0aa023fae06e4792a1aae5d0a9dde32398c6e1b3db30840`.

All four subshards are terminal Actions successes. Every subshard reproduces the frozen structural controls: `M12=(4316,4550)`, rank `3436`, homogeneous-kernel dimension `1114`, exact M12 annihilation, `M14=(6790,6800)`, `L14=(1456,6790)`, exact `L14*M14=0`, canonical obstruction count `223`, canonical lower-authority provenance true, and inverse control true.

As an independent diagnostic only, every one of the 141 newly reproduced lane-7 sparse rational columns agrees exactly with the corresponding column in historical Iter057AD artifact `10440479824`; mismatch count is zero in all four subranges. The historical Iter057AD/Iter057AE BLOCKED classifications remain preserved because those gates did not realize the complete prospectively required aggregate object.

## Complete exact obstruction map

The terminal evaluator consumes only the seven immutable usable Iter057AD lane artifacts plus the four Iter057AF subshards for the map `B`. It recomputes the frozen canonical obstruction as `O0=L*r0` using the unchanged Iter057AD evaluator semantics. It does not refit lower jets, change the R12 basis/order, restrict modes, or use numerical rank/zero tolerances.

Controls consumed from the raw artifact:

- complete unique homogeneous-column coverage `0..1113`: **true**;
- duplicate columns: **none**;
- `B` shape: **`1456 x 1114`**;
- exact sparse nonzero entries in `B`: **80,982**;
- canonical `O0` nonzero count: **223**;
- `L14*M14=0`: **true**;
- canonical lower-authority provenance: **true**;
- canonical inverse control: **true**;
- all eleven lane payload hashes and exactness controls: **true**.

Exact rational ranks computed with the recorded exact backend are:

- `rank(B) = 1110`;
- `rank([B|-O0]) = 1111`.

Therefore `O0` is not in the image of the complete frozen 1114-dimensional R12 homogeneous branch map. No exact branch vector `h*` can remove the R14 Bianchi/Noether compatibility obstruction within this unrestricted frozen branch family.

## Terminal classification

`SCIENTIFIC_FAIL_ITER057AF_COMPLETE_EXACT_R12_HOMOGENEOUS_FREEDOM_CANNOT_REMOVE_R14_BIANCHI_NOETHER_OBSTRUCTION`

This is exactly the preregistered FAIL condition: the complete exact aggregate has `rank([B|-O0]) > rank(B)`. Because the affine obstruction equation is inconsistent, the PASS-only requirements to construct `h*`, solve the unrestricted R14 system, and replay the nonlinear residuals are not applicable: no such `h*` exists for this frozen branch problem.

## Scope ceiling

This result is a finite local exact Taylor/jet obstruction certificate for the specific prospectively frozen Iter057AD/Iter057AF construction. It does **not** establish a global or all-orders no-go theorem for gravity, does not exclude other prospectively defined ansatz families or different scientific objects, and does not establish quantum gravity, experimental confirmation, unitarity, regulator removal, or UV completion.

Historical PASS/FAIL/BLOCKED authorities remain preserved. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.
