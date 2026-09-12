# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter036`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / BRANCH-PERSISTENCE AND REFINEMENT STRESS`
Active roadmap stage: `verified finite-patch branch multiplicity -> larger-patch persistence -> refinement proxy -> branch measure/selection`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter035 completion: **100%**
- Iter036 completion: **25% / PRODUCTION ACTIVE**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Projective refinement-limit action mechanism: **PASS_CONDITIONAL_SCOPED**
- Local weak-cell principal curvature lift: **PASS_SCOPED**
- Local/compact-patch torsion regularity mechanism: **PASS_SCOPED**
- Finite-patch single-branch uniqueness: **COUNTEREXAMPLE VERIFIED_SCOPED**
- Verified distinct extendable G35 branch patches: **8**
- Branch persistence on larger patch / deformation: **UNDER TEST (G36)**
- Tower-wide uniform torsion-Jacobian gap: **NOT DERIVED**
- Global branch compactness/finiteness: **NOT DERIVED**
- Physical multiple-branch measure/selection: **NOT DERIVED**
- Absolute source normalization `beta`: **NOT DERIVED**
- Physical Weyl-active same-realization finite absolute phase target: **NOT DERIVED**
- `c6` fixed: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter034 terminal — distant-branch discovery
Run `34705929851`, head `46423cb63a899b4c5a4077be81b003edc2d95280`, aggregate job `103585911907`, artifact `10300838970`, digest `sha256:05b0ee793eac19e50f89774fc24af6d619479d07825e4a16ba36fd4808d740de`.

Classification: `NUMERICAL_COUNTEREXAMPLE_CANDIDATE_DISTINCT_FINITE_TRANSPORT_ROOT_FOUND_FROM_LARGE_START_SCAN__REQUIRES_HIGH_PRECISION_AND_BRANCH_EQUIVALENCE_VERIFICATION_BEFORE_PROMOTION`.

Frozen scan: 24 distant-start trials, 22 residual-qualified roots, 10 transport-separated candidates. Stronger-background continuation completed 25/30 requested steps with minimum observed successful torsion-Jacobian singular gap `0.18363503160521438`. Solver nonconvergence was not interpreted as root absence.

Record: `results/ITER034_G34_NONLINEAR_TORSION_RUNAWAY_STRESS.md`.

## Iter035 terminal — invariant branch verification
Authoritative run `34706686021`, head `faec0f17c49c43d97984b16cf048dc4a52a8f247`, aggregate job `103588230856`, artifact `10301772238`, digest `sha256:d41b2ec8657b27585c1d3735a6b060d21915145454a0ef5fc1e8b819de6be1a0`.

All 24/24 frozen verification lanes completed; 22 had residual-qualified origin candidates; reference controls were valid; **8** lane/scale pairs passed independent polishing, metric compatibility, invariant edge separation, all-four-neighbor extension, and plaquette-holonomy invariant separation:
`(0,3,6.0), (1,2,3.0), (1,3,6.0), (2,2,3.0), (2,3,6.0), (3,1,1.5), (4,2,3.0), (5,3,6.0)`.

Classification: `SCIENTIFIC_PASS_SCOPED_DISTINCT_EXTENDABLE_BRANCH_COUNTEREXAMPLE`.

Interpretation: uniqueness is numerically false on the verified finite patch in this tested realization. This is **not** a global branch-count/nonuniqueness theorem and does not establish infinite or tower-persistent branches.

Record: `results/ITER035_G35_DISTANT_BRANCH_VERIFICATION.md`.

## Active gate — Iter036 G36
`QGR-ITER036-G36-BRANCH-PERSISTENCE-LARGER-PATCH-BACKGROUND-AND-REFINEMENT-PROXY`.

Preregistered in `status/ITERATION_036.md` before production.

Production run: `34708104944`.
Head at launch: `0d5a0be6b5d7336f42747a2b3010013f1aa51ab7`.
Matrix: **48 lanes**, fail-fast disabled.

Frozen seed set: exactly the 8 verified G35 branch witnesses, with no post-hoc subset selection.

Two stress families:
1. background-amplitude persistence at `gamma in [0.8, 1.0, 1.2]`, `h=1`;
2. shrinking-cell local refinement proxy at `h in [0.75, 0.50, 0.35]`, `gamma=1`.

At every target, reference and candidate branches are tested on the frozen **15-cell two-shell patch**. Lane promotion requires continuation success, small residual, metric compatibility, invariant edge distinction, complete 15-cell extension, and expanded-patch holonomy-invariant separation.

Aggregate PASS requires at least one **same frozen G35 seed** to pass all three background targets and all three refinement-proxy targets. The refinement proxy is explicitly not the full projective-refinement theorem.

## Strongest positive result
G35 established reproducible scoped finite-patch branch multiplicity: **8 distinct extendable invariant branch patches** survived the frozen independent verification gate.

## Strongest blocker
`FINITE_BRANCH_PERSISTENCE_REFINEMENT_AND_PHYSICAL_BRANCH_WEIGHT_SELECTION`.

The immediate question is whether the same branches persist on a larger patch and under controlled deformation/shrinking-cell stress. Even if G36 passes, global compactness/finiteness, full projective-refinement persistence, and a non-arbitrary physical measure/selection rule over multiple branches remain open.

## Claim locks
- theory established `0%`;
- G35 is a scoped numerical finite-patch counterexample, not a global theorem;
- G36 shrinking-cell mode is a refinement proxy, not the full projective limit;
- solver nonconvergence is not proof that a root does not exist;
- global branch compactness/finiteness remains unproved;
- tower-wide uniform torsion-Jacobian gap remains unproved;
- physical branch probabilities/selection remain underived;
- `beta=1` unauthorized;
- `c6` unfixed;
- no physical same-realization Weyl-active finite absolute phase target yet;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
