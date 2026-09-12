# QGR Iter036 G36 — expanded-patch branch persistence

Date: 2026-09-12
Status: `SCIENTIFIC_PASS_SCOPED_SAME_BRANCH_PERSISTS_ACROSS_BACKGROUND_AND_REFINEMENT_PROXY`

## Reproducibility

Authoritative GitHub Actions run: `34708104944`.

- head: `0d5a0be6b5d7336f42747a2b3010013f1aa51ab7`
- frozen production matrix: **48 lanes** + aggregate
- all 48 reference controls valid
- aggregate job: `103592614169`
- aggregate artifact: `10302791375`
- aggregate digest: `sha256:78df0730836beb3ca463c46def82b9ce07b2b2a3a66ebad191f93bd7ebbe4087`

## Frozen aggregate result

- expected lanes: **48**
- found unique lanes: **48**
- reference-control-valid lanes: **48**
- promoted lane passes: **44**
- refinement-proxy persistent G35 seed indices: **[0,1,2,3,4,5,6,7]**
- background-persistent G35 seed indices: **[0,1,3,4,5,7]**
- jointly persistent G35 seed indices: **[0,1,3,4,5,7]**

The eight seed indices refer to the exact frozen G35 witness set from `status/ITERATION_036.md`; no post-hoc branch subset was introduced before production.

## Scientific interpretation

Every one of the eight G35 verified distinct finite torsion branch witnesses survived the full frozen local shrinking-cell proxy grid `h in [0.75,0.50,0.35]` on the expanded 15-cell patch while remaining numerically resolvable and invariantly distinct under the preregistered criteria.

Six of those eight same frozen witnesses also survived all three background-amplitude targets `gamma in [0.8,1.0,1.2]`, and therefore satisfy the preregistered joint-persistence criterion.

This substantially weakens the hypothesis that G35 was only a one-cell/one-background numerical-basin artifact. It establishes scoped numerical persistence across a larger finite patch and the tested deformations.

It does **not** establish persistence in the full QGR projective refinement limit, a global branch-count theorem, tower-wide compactness/finiteness, or a physical branch probability/selection rule.

## Claim locks

- finite 15-cell numerical persistence = **PASS_SCOPED**;
- full projective-refinement branch persistence = **NOT DERIVED**;
- global branch compactness/finiteness = **NOT DERIVED**;
- tower-wide uniform torsion-Jacobian gap = **NOT DERIVED**;
- physical multiple-branch measure/selection = **NOT DERIVED**;
- solver nonconvergence is not proof of root absence;
- absolute normalization `beta` remains underived;
- `c6` remains unfixed;
- theory established = **0%**;
- KMQGB `NEW_REQUIRED` remains unauthorized unless benchmark authority changes.

## Next gate

Separate two remaining failure modes rather than repeating G36:

1. deeper shrinking-cell continuation with branch-separation scaling and torsion-Jacobian-gap diagnostics;
2. larger spatial patch-radius extension with multi-parent/path consistency checks.
