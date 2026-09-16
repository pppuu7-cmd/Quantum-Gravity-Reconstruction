# Iter057AK — Full Dual-Kernel Parity / Symmetry Obstruction Decomposition

Status: PROSPECTIVELY PREREGISTERED; no Iter057AK decomposition/rank evidence exists at this commit.  
Date: 2026-09-16.

## Motivation and pre-gate admissibility decision

The separately frozen pre-gate audit `reviews/ITER057AK_CROSS_BACKGROUND_ADMISSIBILITY_AUDIT.md` at commit `135ba9e3f726dd50056a389ce889b895efdf8ee0` found that the current programme contains only one terminal canonical R12 on-shell seed family. Iter057AD/AF exhaust its homogeneous R12 branch freedom but do not provide independent held-out backgrounds; Iter057L is only a lower-order local jet. Therefore no source-faithful cross-background/held-out transport map can presently be frozen without inventing a background or refitting a basis.

Per the requested fallback rule, this gate keeps the terminal Iter057AF scientific object unchanged and asks how its complete exact dual kernel and obstruction class decompose.

## Frozen authorities — no mutation

Consume exactly the terminal Iter057AF obstruction object:

- Iter057AF terminal result: `230690a56e5055471054d9751985f7604ec7130d`;
- Iter057AF durable rank authority: `cb9120f7228a6083e62f2bb51c447f97a81870c2`;
- old Iter057AD column artifacts from run `35070896151`, head `041fb0046d92e5a9800dd99b0ce4e8b841242df5`:
  `10444152126,10442437521,10442003071,10444770687,10443729361,10443653309,10443899697`;
- Iter057AF lane-7 shards from run `35118287075`, head `57b8e0f61e1d77c19eca09a2bd34f48921ffc020`:
  `10459975843,10462775594,10460706453,10461754625`;
- canonical `O0` must be freshly reconstructed from the unchanged Iter057AD/Iter057AC `canonical_seed12 -> rhs14 -> left_controls` path; it may not be inferred from the terminal dual witness.

Known frozen global controls from Iter057AF are not new outcomes: `B` has shape `1456 x 1114`, `nnz=80982`, `rank(B)=1110`, hence `K=ker(B^T)` has dimension `346`; `rank([B|-O0])=1111`; canonical `O0` has 223 nonzero entries.

Iter057AG/AH/AJ data may be consumed only as positive controls after the new decomposition is constructed. In particular, AG witness coefficients may not be used to choose sectors, pivots, group actions or basis vectors.

## Prospectively frozen row-sector convention

Use exactly the Iter057AH compatibility ordering:

`i = b * len(alphas(11)) + index(beta)`, with `b in {0,1,2,3}` and `beta` a lexicographically sorted degree-11 four-index from `qgr_iter057z_dodecic_einstein_seed_completion.alphas(11)`.

Partition the 1456 compatibility coordinates *before inspecting ranks* by the frozen key

`S(b,p) = { (b,beta) : beta mod 2 = p }`,

where `p=(beta_t mod2,beta_x mod2,beta_y mod2,beta_z mod2)`. Empty sectors remain recorded as empty; nonempty sectors are processed in lexicographic `(b,p)` order. This is the exact bookkeeping parity convention already used by Iter057AH; it is not reinterpreted as a physical parity theorem.

For every sector `S`, form the exact restricted matrix

`C_S = B^T P_S : Q^{|S|} -> Q^{1114}`.

Record with exact rational arithmetic:

- sector coordinate count `n_S`;
- exact `rank(C_S)` and `nullity(C_S)`;
- `rank([C_S ; O0_S^T])`;
- `obstruction_active_S = rank([C_S ; O0_S^T]) - rank(C_S)`.

Because the added row is one-dimensional, the final quantity must be exactly 0 or 1. `1` means that the support-local kernel `ker(C_S)` contains a vector with nonzero `O0` pairing.

Also record

`D_local = sum_S nullity(C_S)` and `D_cross = 346 - D_local`.

If `D_cross=0`, the full kernel is proven to be the direct sum of the support-local sector kernels because the sectors have disjoint coordinate support. If `D_cross>0`, build a full exact kernel basis and serialize the dimension of the genuinely cross-sector remainder; do not force a direct-sum interpretation.

## Frozen primary scientific hypothesis

The strong hypothesis to test is:

> Among all prospectively frozen support-local `(b,beta mod2)` sectors, the **only** sector with `obstruction_active_S=1` is the already-known AH/AJ sector `b=0, p=(1,0,0,0)`, and its support-local kernel is one-dimensional. All other support-local dual directions, if present, annihilate `O0`.

This hypothesis is frozen before the new sector ranks are computed.

A PASS does **not** require `D_cross=0`; cross-sector directions are allowed, but any additional exact obstruction-active support-local sector falsifies the unique-channel hypothesis.

## Full-kernel obstruction quotient

Independently verify globally that

- `dim K = 346`;
- `dim(K intersect O0^perp)=345`;
- therefore the obstruction quotient `K/(K intersect O0^perp)` is exactly one-dimensional.

Construct at least one exact basis/witness for the quotient without importing AG coefficients, normalize it by `O0^T y=1`, and only then compare coefficient-by-coefficient with the terminal Iter057AG witness as a positive control.

## Frozen spatial S3 diagnostics

No S3 symmetry of the *full* kernel is assumed.

Test two prospectively frozen coordinate actions for all six permutations of `(x,y,z)`:

1. `T_AH`: the literal Iter057AH polynomial convention — permute the three spatial entries of `beta` while leaving `b` fixed;
2. `T_tensor`: permute the spatial entries of `beta` and, for `b in {1,2,3}`, permute that spatial free index by the same permutation; `b=0` remains fixed.

For each action and each group element, test exact preservation of `K=ker(B^T)`. If an action does not preserve `K`, report the exact failing permutation/action and mark an S3 irrep decomposition under that action `NOT_DEFINED_NONINVARIANT`; do not project or refit the kernel.

Only if all six actions preserve `K`, compute exact S3 isotypic dimensions with the frozen rational projectors

- `P_triv=(1/6) sum_g T_g`,
- `P_sign=(1/6) sum_g sign(g) T_g`,
- standard-isotypic dimension = `dim K - dim(P_triv K) - dim(P_sign K)`,

and verify the standard-isotypic dimension is even. Test whether `O0` pairs nontrivially with each invariant isotypic subspace. No desired irrep outcome is imposed.

## Independent Critic / reproduction lane

A separate implementation, without consuming the primary output, must reconstruct the same immutable columns and fresh canonical `O0`, then independently verify:

- complete unique column coverage and all artifact provenance;
- global ranks `1110/1111` and `dim K=346`;
- every nonempty sector rank/nullity/activity using a different exact algorithm/backend where practical;
- the deterministic sector list/counts from degree-11 combinatorics;
- zero-`O0` negative control gives zero active sectors;
- scaling `O0 -> 2 O0` leaves all sector activity flags unchanged;
- after the new result is fixed, AG/AJ witness support and normalization replay the reported AH sector as a positive control.

Outcome-sensitive primary rank results must not be used to choose Critic sectors, pivots or thresholds.

## Terminal classifications

Primary PASS label, if the frozen unique-channel hypothesis holds and all exact controls/reproduction agree:

`PASS_SCOPED_ITER057AK_FULL_DUAL_KERNEL_DECOMPOSITION_IDENTIFIES_UNIQUE_AH_PARITY_OBSTRUCTION_CHANNEL`

Scientific FAIL label if exact authority is valid but one or more additional prospectively frozen support-local sectors have nonzero obstruction pairing, or the AH sector is not the claimed one-dimensional active sector:

`SCIENTIFIC_FAIL_ITER057AK_UNIQUE_AH_PARITY_OBSTRUCTION_CHANNEL_HYPOTHESIS_FALSE`

A non-invariant S3 action by itself is **reported as a structural result**, not used to relabel a true unique parity-channel result as FAIL; it means only that the corresponding full-kernel irrep decomposition is not defined.

Technical inability to realize the complete exact decomposition/reproduction:

`BLOCKED_ITER057AK_COMPLETE_EXACT_DUAL_KERNEL_DECOMPOSITION_NOT_TECHNICALLY_REALIZED`

Authority/provenance mismatch, numerical tolerance, sector mutation, AG-coefficient leakage into sector construction, or post-outcome regrouping:

`INVALID_ITER057AK_AUTHORITY_EXACTNESS_OR_NO_REFIT_CONTROL_FAILURE`

## Scope ceiling

This gate decomposes only the terminal finite local Iter057AF obstruction object on the same frozen local background. It is explicitly **not** cross-background evidence and cannot establish background-independence, an all-orders/global no-go theorem, physical parity/rotation symmetry, strong hyperbolicity, ghost/stability claims, unitarity, regulator removal, UV completion or experiment.

Claim locks remain unchanged: theory established `0%`; `c6` symbolic/unfixed; `beta=1` unauthorized; no `c6` fitting/running or new physical branch is authorized.
