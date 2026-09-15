# Iter057M terminal result — general q_ab second-even-jet / quartic extension

Date: 2026-09-15
Gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`
Exact derivation: `443d52b759232addf580cb70d7f6b5fedcce9519`

## Terminal classification

**`PASS_SCOPED_ITER057M_GENERAL_QAB_QUARTIC_JET_EXTENDS_THROUGH_SECOND_EVEN_SOURCE_ORDER__OPEN_NEIGHBORHOOD_NOT_ESTABLISHED`**

This is exactly the prospectively frozen maximum scoped PASS classification.

## Exact evidence

The source-owned G3/H0 + Iter056X Weyl3 second jet is exposed by the exact finite-Taylor evaluator `f9181c7dda617ce4061fa90e73164e6cdbecd714` and independently component-normalized by the prospectively frozen equivalence audit:

- audit result `688994108d3b28d9cdf7d7926236bece78222a94`;
- Actions run `34954206549`;
- artifact `10390318470`;
- digest `sha256:ab331b2093e7d26e1d5f609f08e81c70739bb79d88a9a210a73ffc5b8155cd92`.

The full unrestricted quartic space contains 350 exact coefficients. The frozen coefficient matrix has

`shape=(180,350)`, `rank=164`, `nullity=186`, `left-nullity=16`.

Its complete left nullspace is the canonical 16-dimensional Bianchi/de Donder compatibility space. For arbitrary source coefficients the exact affine identity is

`Y_(b,j)^T r = [nabla^a S_ab]_(degree-one,j)`.

For the actual G3/H0 Weyl3 source, all sixteen contractions vanish exactly and

`rank([M|r])=rank(M)=164`.

An exact unrestricted particular Q4 exists. The canonical pivot solution has 32 nonzero normalized coefficients and zero residual in all 180 gauge+field rows; 186 homogeneous directions remain explicit.

## Independent unreduced production control

Fresh exact Q4 control run:

- workflow head `489bfbd845a98decad44aa271f0f6d3d810f116d`;
- Actions run `34954412091`;
- job `104332863586`;
- artifact `10390657547`;
- digest `sha256:78aca057d3fd2ef4db1d7e746e188c625a02eda14c41c902fcee642bf886208c`.

Every aggregate control is true:

- exact source controls;
- augmented rank equals exact rank;
- 16/16 compatibility contractions zero;
- exact particular-solution residual zero;
- independent unreduced controls pass.

Direct unreduced substitution reports

`nabla^a qbar_ab = 0`

through cubic coordinate order for all four components, and

`DG_ab[q]-S_ab = 0`

through quadratic coordinate order for all ten independent symmetric components, identically and without numerical tolerance.

## Frozen obligations A-G

All seven preregistered obligations are satisfied exactly:

A. source second jet — PASS;
B. operator coefficient jet — PASS;
C. unrestricted Q4 generality — PASS;
D. de Donder through cubic order — PASS;
E. field equation through quadratic order — PASS;
F. independent unreduced substitution — PASS;
G. source/Noether compatibility — PASS.

No restricted conformal/diagonal/static-component/plane-wave/spherical ansatz was used to infer general solvability. `c6` was not fitted or fixed.

## Relation to previous fronts

Iter057J remains a scientific FAIL of the conformal continuation only. Iter057L established unrestricted local second-jet solvability; Iter057M now extends that unrestricted correction through the next nontrivial even source order.

Historical Iter057K remains a technical BLOCKED production attempt. Its historical classification is not retroactively changed; the new finite-Taylor exact implementation bypasses its global-rational runtime problem with an independently controlled mathematically equivalent local-jet representation.

## Scope ceiling

This PASS remains a finite local Taylor certificate. It does not establish an actual open-neighborhood solution, convergence of the formal correction series, global/asymptotic boundary conditions, physical characteristics, strong hyperbolicity, ghosts, stability, unitarity, regulator removal, UV completion, experiment, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.