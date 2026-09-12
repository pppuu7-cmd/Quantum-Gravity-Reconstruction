# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter037`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / REFINEMENT-CONNECTED BRANCH ADMISSIBILITY`
Active roadmap stage: `verified finite-patch multiplicity -> larger-patch persistence -> same-realization refinement-connected admissibility -> actual two-level projective blocking -> branch measure only if multiplicity survives`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter036 completion: **100%**
- Iter037 completion: **10% / PREREGISTRATION ACTIVE**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Projective refinement-limit action mechanism: **PASS_CONDITIONAL_SCOPED**
- Principal identity-connected connection refinement: **PASS_SCOPED (G10B regular tested domain)**
- Finite-patch single-branch uniqueness: **COUNTEREXAMPLE VERIFIED_SCOPED**
- G35 distinct extendable branch patches: **8**
- G36 refinement-proxy persistent branches: **8/8**
- G36 jointly background+refinement-proxy persistent branches: **6/8**
- Physical same-realization admissibility of the six distant branches: **NOT DERIVED / ACTIVE G37**
- Full projective-refinement persistence of multiple physical branches: **NOT DERIVED**
- Physical multiple-branch measure/selection: **NOT DERIVED**
- Tower-wide uniform torsion-Jacobian gap: **NOT DERIVED**
- Global branch compactness/finiteness: **NOT DERIVED**
- Absolute source normalization `beta`: **NOT DERIVED**
- Physical Weyl-active same-realization finite absolute phase target: **NOT DERIVED**
- `c6` fixed: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter035 terminal — invariant branch verification
Run `34706686021`, head `faec0f17c49c43d97984b16cf048dc4a52a8f247`, aggregate job `103588230856`, artifact `10301772238`, digest `sha256:d41b2ec8657b27585c1d3735a6b060d21915145454a0ef5fc1e8b819de6be1a0`.

Classification: `SCIENTIFIC_PASS_SCOPED_DISTINCT_EXTENDABLE_BRANCH_COUNTEREXAMPLE`.

Eight frozen distant starts produced distinct extendable finite branch patches. This falsifies single-branch uniqueness on the tested finite patch, but is not a global/tower theorem.

Record: `results/ITER035_G35_DISTANT_BRANCH_VERIFICATION.md`.

## Iter036 terminal — larger-patch persistence and shrinking-cell proxy
Run `34708104944`, head `0d5a0be6b5d7336f42747a2b3010013f1aa51ab7`, aggregate job `103592614169`, summary artifact `10302791375`, digest `sha256:78df0730836beb3ca463c46def82b9ce07b2b2a3a66ebad191f93bd7ebbe4087`.

All **48/48** frozen lane artifacts were present and all **48** reference controls were valid. **44/48** scientific lane checks passed. All eight G35 branches passed all three shrinking-cell proxy targets. Six seeds `[0,1,3,4,5,7]` also passed all three background-amplitude targets and therefore are jointly persistent across both G36 stress families on the frozen 15-cell patch.

Classification: `SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_PERSISTS_ACROSS_BACKGROUND_AND_REFINEMENT_PROXY`.

This is strong evidence that finite-cell branch multiplicity is not merely a one-point/local solver accident. It is still only finite-patch numerical persistence: G36 shrinking-h was explicitly a local proxy, not an actual projective blocking theorem.

Record: `results/ITER036_G36_EXPANDED_PATCH_BRANCH_PERSISTENCE.md`.

## Critical governance reconciliation: G10B versus G35/G36
Earlier prospective same-realization rule G10B fixed the physical finite connection as the **identity/refinement-connected principal branch** on regular smooth data:
- `L_e(h)=I+h omega_e[G,DG]+O(h^2)` as `h -> 0`;
- the first-order `omega` must be the unique linearized Levi-Civita/torsion solution;
- coarse transport must arise as the product of fine principal transports.

Therefore G35/G36 distant algebraic roots cannot be assigned physical branch probabilities merely because they are finite-patch regular and persistent. They must first pass this previously frozen refinement-connected same-realization criterion. G8B coarea weights remain a diagnostic for isolated algebraic roots; they are not authority for summing disconnected connection roots as fundamental physical alternatives.

## Active gate — Iter037 G37
`QGR-ITER037-G37-REFINEMENT-CONNECTED-BRANCH-ADMISSIBILITY-AND-TWO-LEVEL-PROJECTIVE-BLOCKING`.

Frozen seed set: exactly the six G36 jointly persistent seeds `[0,1,3,4,5,7]`; no post-hoc branch substitution.

The gate must test, at deeper shrinking cells, whether each distant branch:
1. continues regularly without branch switching;
2. approaches identity with the required `O(h)` behavior;
3. approaches the same unique first-order connection as the G10B principal branch;
4. remains invariantly distinct or instead merges with the principal branch;
5. is compatible with **actual two-level fine-to-coarse path-groupoid blocking**, not merely the G36 h-proxy.

Scientific outcomes are asymmetric:
- if a distant branch remains projectively/refinement-connected and physically distinct, multiple physical connection branches survive scoped testing;
- if all distant roots merge into or fail the frozen principal refinement-connected criterion, G35/G36 remain valid algebraic finite-cell branch results but do not imply multiple physical continuum connection branches;
- numerical inability to track a branch is `BLOCKED/PARTIAL`, not proof of absence.

Only if at least two physically admissible branches survive G37 should a subsequent gate promote coarea relative weights into a physical branch-measure question.

## Strongest positive result
G36: **6 independently frozen distant branches** persist on a 15-cell patch across all preregistered background-amplitude and shrinking-cell proxy stresses; all 8 survive the shrinking-cell proxy family.

## Strongest blocker
`REFINEMENT_CONNECTED_SAME_REALIZATION_ADMISSIBILITY_OF_PERSISTENT_DISTANT_BRANCHES`.

## Claim locks
- theory established `0%`;
- G35/G36 are scoped numerical finite-cell results, not global/tower theorems;
- finite-patch persistence does not authorize multiple physical branches;
- G10B same-realization refinement-connected criterion is prospective and may not be weakened after seeing G35/G36;
- solver nonconvergence is not proof that a root does not exist;
- no branch cutoff/prior/regulator/post-hoc selection may be introduced to force uniqueness or normalization;
- global branch compactness/finiteness remains unproved;
- tower-wide uniform torsion-Jacobian gap remains unproved;
- physical branch probabilities/selection remain underived;
- `beta=1` unauthorized;
- `c6` unfixed;
- no physical same-realization Weyl-active finite absolute phase target yet;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
