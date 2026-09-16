# Iter057AD preregistration — R12 homogeneous branch test of the R14 obstruction

Status: PROSPECTIVELY FROZEN
Date: 2026-09-16
Gate: `ITER057AD-R12-HOMOGENEOUS-BRANCH-R14-OBSTRUCTION-LIFT`

Parent authorities:

- Iter057Z terminal dodecic seed PASS: `bb4fa6ccbf21e2a063467a1b0839223744866995`.
- Iter057Z canonical R12 particular authority: `5bfe62e887dd627c76c41080187eadc3d95e0c45` / `data/ITER057Z_CANONICAL_R12_NORMALIZED.csv`.
- Iter057AC terminal canonical-path scientific FAIL: `905fc6f4fdfd06da73802c4442c746db5e6d87e6`.

## Scientific question

Is the Iter057AC degree-14 affine incompatibility specific to the deterministic canonical R12 particular representative, or does it persist throughout the **entire exact 1114-dimensional homogeneous solution family** left unfixed by Iter057Z?

This is an explicitly branched alternative-seed test. It does not erase, revise, reinterpret or rescue the terminal canonical-path result `SCIENTIFIC_FAIL_ITER057AC_AFFINE_INCOMPATIBILITY`.

## Frozen branch family

Reconstruct exactly the Iter057Z unrestricted degree-twelve complex

`M12 R12 = r12`

with frozen structural data

`shape(M12)=(4316,4550)`, `rank(M12)=3436`, `nullity(M12)=1114`, `left-nullity(M12)=880`.

Let `R12*` be the frozen canonical Iter057Z particular solution and let `{H_i}_{i=1}^{1114}` be a deterministic exact basis of the **complete** right nullspace of the same normalized `M12`:

`M12 H_i = 0`.

Define the separate branch family

`R12(h) = R12* + sum_i h_i H_i`,

with all 1114 rational branch parameters initially free. No subset, symmetry reduction or hand-selected modes are allowed.

The historical canonical branch remains the point `h=0` and remains terminal FAIL at Iter057AC.

## Frozen degree-14 obstruction object

For each branch point, keep every lower seed layer through R10 unchanged and recompute from the full branch metric the fresh coordinate-degree-twelve Einstein/de Donder affine right-hand side for a pure degree-14 correction R14.

Use the same unrestricted normalized degree-14 coefficient space and universal principal complex frozen in Iter057AC:

- 6800 R14 unknowns;
- `shape(M14)=(6790,6800)`;
- `rank(M14)=5334`;
- right nullity `1466`;
- complete left/Bianchi-Noether rank `1456`.

Reconstruct a deterministic exact complete left-null basis `L14` satisfying `L14 M14 = 0`.

Define the branch obstruction vector

`O(h) := L14 r14(h)`.

By exact degree counting, the coordinate-degree-twelve residual is affine in a pure degree-twelve homogeneous perturbation. This must be verified directly: all second derivatives of `r14(h)` with respect to branch parameters, or an equivalent exact coefficient-level test, must vanish. Therefore expose

`O(h)=O0 + B h`

with exact rational `B` of size `1456 x 1114` before any consistency decision.

The canonical point must replay Iter057AC exactly: `O(0)` has the same frozen nonzero compatibility content, including canonical rank mismatch `5334 -> 5335` and 223 nonzero compatibility contractions under the same canonical left-basis convention or an explicitly proven equivalent basis transformation.

## Frozen obligations

A. Replay all lower canonical seed authorities through R10 exactly and the Iter057Z R12 particular authority exactly.

B. Reconstruct the complete 1114-dimensional exact R12 right nullspace; prove its rank/dimension and `M12 H=0` exactly.

C. For a symbolic branch vector `h`, verify the Iter057Z equations remain satisfied through Einstein coordinate degree ten and de Donder degree eleven for every homogeneous direction.

D. Recompute the degree-twelve nonlinear residual from the full branch metric. Historical/inferred Iter057AC right-hand sides may be used only for replay comparison, never substituted for the branch computation.

E. Reconstruct the complete Iter057AC universal R14 principal matrix and complete rank-1456 left/Bianchi-Noether space exactly.

F. Verify exact affine dependence `O(h)=O0+B h` and replay the Iter057AC canonical obstruction at `h=0`.

G. Decide the full unrestricted branch-lift system

`B h = -O0`

by exact rank/augmented-rank arithmetic only. Record `rank(B)`, `rank([B|-O0])`, branch nullity and a complete compatibility witness if inconsistent.

H. If the branch-lift system is consistent, construct one deterministic exact `h*`, form `R12(h*)`, recompute the fresh R14 affine system, construct at least one exact unrestricted R14 particular solution, and retain the full R14 homogeneous nullspace.

I. For any PASS candidate, independently reconstruct the full branched metric and require exact inverse identity, de Donder through degree thirteen, and Ricci/scalar/Einstein tensors through coordinate degree twelve to vanish. No reduced-system success alone is sufficient.

J. Preserve the canonical history: no file or authority representing canonical Iter057Z/AC coefficients or classifications may be overwritten. Any branch coefficients must be stored under explicit Iter057AD branch authority names.

K. No floating-point rank, tolerance, fitted threshold, restricted ansatz, source normalization change, `c6` choice, `beta=1`, Hamiltonian/clock/update invention, or post-evidence criterion change is allowed.

## Decision rules

Maximum scoped PASS:

`PASS_SCOPED_ITER057AD_FULL_R12_HOMOGENEOUS_BRANCH_CONTAINS_EXACT_R14_EXTENDABLE_SEED__CANONICAL_ITER057AC_FAIL_REMAINS_PRESERVED`

iff obligations A-K pass exactly, `rank(B)=rank([B|-O0])`, an exact branch point `h*` is constructed, the resulting unrestricted R14 affine system is exactly consistent, and the independent full nonlinear replay vanishes through the frozen order.

Scientific FAIL:

`SCIENTIFIC_FAIL_ITER057AD_R14_OBSTRUCTION_PERSISTS_ACROSS_COMPLETE_ITER057Z_R12_HOMOGENEOUS_FAMILY`

iff A-G and J-K pass exactly but `rank([B|-O0]) > rank(B)`, proving that no member of the complete Iter057Z 1114-dimensional homogeneous R12 family removes the frozen R14 compatibility obstruction while lower layers through R10 remain fixed.

BLOCKED:

`BLOCKED_ITER057AD_COMPLETE_R12_HOMOGENEOUS_BRANCH_OR_R14_OBSTRUCTION_MAP_NOT_TECHNICALLY_REALIZED`

if the complete exact nullspace, branch residual, obstruction map, or required independent replay cannot be realized without changing the frozen problem.

INVALID:

`INVALID_ITER057AD_CANONICAL_HISTORY_MUTATION_RESTRICTED_BRANCH_INCOMPLETE_KERNEL_OR_EXACTNESS_CONTROL`

if the canonical failed path is overwritten/reclassified, fewer than the complete 1114 homogeneous directions are treated as the branch space, lower layers through R10 are refitted, a restricted ansatz is generalized, the canonical Iter057AC obstruction does not replay, numerical zero/rank is used, or frozen controls are weakened after evidence.

## Interpretation ceiling

A PASS establishes only existence of one explicitly branched finite local seed through metric degree fourteen / Einstein coordinate degree twelve inside the complete Iter057Z R12 homogeneous family. It does not restore the failed canonical branch, authorize corrected Weyl3 source degree ten on the canonical path, prove an all-orders/convergent/open-neighborhood/global solution, or establish any quantum claim.

A FAIL is likewise finite and branch-family scoped; it does not exclude alternative branches involving earlier homogeneous layers, nonlocal/global constructions, or quantum completion.

Historical FAIL/BLOCKED results remain preserved. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; finite certificate != theorem; classical != quantum; diagnostic != closure; theory established remains `0%`.
