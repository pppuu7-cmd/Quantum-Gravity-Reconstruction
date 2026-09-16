# Iter057AE preregistration — full R12 branch-obstruction aggregate

Status: PROSPECTIVELY FROZEN
Gate: `ITER057AE-FULL-R12-BRANCH-OBSTRUCTION-AGGREGATE`

## Authority and dependency

This gate is an aggregation-only continuation of frozen Iter057AD preregistration `8f53a0679692f9655e162aa1a19e45124a8dc775` and terminal GitHub Actions run `35070896151` at workflow head `041fb0046d92e5a9800dd99b0ce4e8b841242df5`.

Iter057AD remains terminal `BLOCKED_ITER057AD_COMPLETE_R12_HOMOGENEOUS_BRANCH_OR_R14_OBSTRUCTION_MAP_NOT_TECHNICALLY_REALIZED` because its eight terminal matrix lanes were partial evidence and no complete exact obstruction-map aggregate was produced. The canonical Iter057AC affine-incompatibility FAIL is preserved and must replay at `h=0` before this gate may classify anything.

No Iter057AD lane may be rerun, recomputed, substituted, repaired or extended in this gate. The only scientific inputs are exactly the eight terminal artifacts attached to Actions run `35070896151`, plus the frozen Iter057AD/Iter057AC provenance needed to validate them.

## Frozen hypothesis and object

Let `h` range over the complete 1114-dimensional exact homogeneous R12 freedom already frozen by Iter057AD. Let the complete Iter057AC Bianchi/Noether compatibility space have frozen dimension 1456. Aggregate the eight existing lane blocks into the single exact affine obstruction map

`O(h) = O0 + B h`,

with `O0` the canonical `h=0` obstruction vector and `B` the complete `1456 x 1114` exact rational obstruction matrix in the previously frozen basis/order.

This gate asks only whether the full homogeneous R12 freedom can remove the Iter057AC compatibility obstruction. It does **not** solve the unrestricted R14 correction and therefore cannot by itself rescue or overturn Iter057AC.

## Frozen inputs and provenance controls

1. Consume exactly eight artifacts from Actions run `35070896151`; no artifact from another run or head is admissible.
2. Record each artifact id/name/digest and reject duplicate or missing lane provenance.
3. Require eight disjoint lane partitions whose union covers all 1114 frozen homogeneous coordinates exactly once, with no overlap, gap, reordering or post-hoc basis change.
4. Require a common 1456-dimensional compatibility-row basis and common canonical `O0` across all lanes.
5. Replay the canonical `h=0` Iter057AC obstruction before using any homogeneous columns; disagreement is INVALID.
6. Aggregate only exact integer/rational payloads. Floating-point values, numerical tolerances or modular-only decisions are INVALID.
7. Compute exact `rank(B)` and exact `rank([B|-O0])`. Independent modular ranks may be used only as diagnostics, never as the decision authority.
8. If the ranks are equal, produce an exact rational branch witness `h*` and verify `O0 + B h* = 0` exactly before a scoped PASS.
9. Preserve all frozen Iter057AD normalization, source lineage, homogeneous basis and compatibility witnesses. No normalization, sign, basis or criterion may change after evidence is seen.

## Frozen classifications

### Scoped PASS

`PASS_SCOPED_ITER057AE_FULL_R12_HOMOGENEOUS_OBSTRUCTION_MAP_ADMITS_EXACT_BRANCH__R14_RESPONSE_STILL_REQUIRED`

iff all provenance/coverage/replay controls pass, `rank(B)=rank([B|-O0])`, an exact rational `h*` is exported, and direct exact substitution gives `O(h*)=0` in all 1456 compatibility rows.

A PASS authorizes only a separately preregistered unrestricted R14 response gate on that exact branch. It does not establish an R14 solution.

### Scientific FAIL

`SCIENTIFIC_FAIL_ITER057AE_FULL_R12_HOMOGENEOUS_FREEDOM_CANNOT_REMOVE_R14_BIANCHI_NOETHER_OBSTRUCTION`

iff all provenance/coverage/replay controls pass and exact arithmetic gives

`rank([B|-O0]) > rank(B)`.

This would show that the entire frozen 1114-dimensional Iter057AD homogeneous family cannot remove the Iter057AC compatibility obstruction within this finite local construction. It is not a global theorem.

### BLOCKED

`BLOCKED_ITER057AE_EIGHT_LANE_TERMINAL_ARTIFACTS_DO_NOT_REALIZE_COMPLETE_EXACT_OBSTRUCTION_MAP`

iff the frozen eight terminal artifacts do not contain enough exact, mutually compatible information to construct the complete map and exact decision objects without recomputing lane science.

A missing required object is a valid terminal BLOCKED result.

### INVALID

`INVALID_ITER057AE_PROVENANCE_COVERAGE_REPLAY_BASIS_NORMALIZATION_OR_EXACTNESS_CONTROL`

iff an artifact comes from the wrong run/head, lane coverage is duplicated/incomplete/reordered, the canonical `h=0` obstruction does not replay, a basis/normalization is changed, partial evidence is generalized, or floating/numerical tolerance determines the result.

## Interpretation ceiling

This is a finite exact aggregation/compatibility diagnostic. Even a scoped PASS does not establish an R14 correction, higher Einstein-seed completion, corrected Weyl3 source degree ten, an all-orders series, convergence/open-neighborhood existence, global/asymptotic completion, physical hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, UV completion, experiment, or QGR correctness.

Historical FAIL/BLOCKED classifications remain authoritative. `c6` remains symbolic/unfixed. `beta=1` remains unauthorized. Finite certificate != theorem; classical != quantum; diagnostic != closure; theory established remains `0%`.
