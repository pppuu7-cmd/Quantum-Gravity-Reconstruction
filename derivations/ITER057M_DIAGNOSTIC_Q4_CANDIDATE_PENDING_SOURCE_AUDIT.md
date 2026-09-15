# Iter057M diagnostic exact Q4 candidate — pending authorized source audit

Date: 2026-09-15
Gate: `ITER057M-GENERAL-QAB-SECOND-EVEN-JET-QUARTIC-EXTENSION`
Preregistration: `9760ca0324dce13cf141a9f93b6ff69ea4c75605`
Canonical rank/Bianchi checkpoint: `8a6a5a56f646b4c96fec4ac50ab392203d26475a`
Active source-component audit: Actions run `34952811799`

## Status lock

**DIAGNOSTIC ONLY — NOT AUTHORITY AND NOT AN ITER057M CLASSIFICATION.**

The exact candidate below is constructed from the accelerated finite-degree Weyl3 source evaluator. That evaluator passes sensitive homogeneity, trace-Ward and low-order Noether controls and is independently reproduced at the origin by a second analytic `P=3 Pi_W Pi_R[C^2]` implementation, but its component sign is still being replayed through the historical authorized Iter057K exact lineage in run `34952811799`.

Nothing in this note may be promoted to PASS until that four-lane audit is complete and consumed.

## Conventions

Use the frozen production presentation `(-,+,+,+)` and `kappa=2/25`. Factor out the nonzero Einstein normalization and define

`Shat_ab := A_E S_ab = -E_W3_ab`.

All Taylor coefficients below are **normalized coefficients**: a coefficient indexed by multi-index `alpha` is the derivative value at the origin in

`f(x)=sum_alpha f[alpha] x^alpha/alpha!`.

Coordinates are ordered `(t,x,y,z)`.

## Diagnostic exact source jet

The accelerated exact source candidate gives

`Shat^(0)_ab / kappa^3 = diag(-48, 208, 208, -368)`.

All time-containing second coefficients vanish. The nonzero normalized quadratic coefficients `Shat_ab[alpha]/kappa^4` are:

| pair `ab` | `alpha` | value |
|---|---|---:|
| 00 | (0,2,0,0) | -2912/3 |
| 00 | (0,0,2,0) | -2912/3 |
| 00 | (0,0,0,2) | -16064/3 |
| 11 | (0,2,0,0) | 7136/3 |
| 11 | (0,0,2,0) | 6880/3 |
| 11 | (0,0,0,2) | -19328/3 |
| 12 | (0,1,1,0) | 128/3 |
| 13 | (0,1,0,1) | -7264/3 |
| 22 | (0,2,0,0) | 6880/3 |
| 22 | (0,0,2,0) | 7136/3 |
| 22 | (0,0,0,2) | -19328/3 |
| 23 | (0,0,1,1) | -7264/3 |
| 33 | (0,2,0,0) | -14624/3 |
| 33 | (0,0,2,0) | -14624/3 |
| 33 | (0,0,0,2) | 14528/3 |

The same evaluator gives at the origin

`I3=96 kappa^3`,

`D^{ii}/kappa^3=(-12,92,92,-196)`,

`E_W3,ii/kappa^3=(48,-208,-208,368)`,

and exactly

`P.R=3 I3`,

`g^{ab} E_W3,ab = -I3`,

`[nabla_a E_W3^{ab}]_(degree <=1)=0`.

Again, the diagonal component values are under the active authorized-lineage audit and are not consumed as final authority by this note.

## Exact affine consistency diagnostic

Insert this candidate source into the frozen exact system `M vec(Q4)=r`.

All sixteen canonical Bianchi/Noether contractions vanish exactly:

`Y_(b,j)^T r = 0` for all `b,j=0..3`.

Therefore the concrete diagnostic augmented system satisfies

`rank([M|r])=rank(M)=164`.

With the 186 free Q4 directions set to zero in the canonical pivot solve, one exact particular solution has only 32 nonzero normalized coefficients. Factoring out `kappa^4`, they are:

| pair | alpha | `Q4/kappa^4` |
|---|---|---:|
| 00 | (0,0,0,4) | -215296/9 |
| 00 | (0,0,2,2) | 9856 |
| 00 | (0,2,0,2) | 9856 |
| 00 | (2,0,0,2) | -43904/3 |
| 00 | (2,0,2,0) | 61888/9 |
| 00 | (2,2,0,0) | 61888/9 |
| 00 | (4,0,0,0) | 3584/9 |
| 01 | (1,1,0,2) | -4160/9 |
| 01 | (1,1,2,0) | 640/9 |
| 01 | (1,3,0,0) | 640/3 |
| 02 | (1,0,1,2) | -4160/9 |
| 02 | (1,0,3,0) | 640/3 |
| 02 | (1,2,1,0) | 640/9 |
| 03 | (1,0,0,3) | -124160/9 |
| 03 | (1,0,2,1) | 19904/3 |
| 03 | (1,2,0,1) | 19904/3 |
| 03 | (3,0,0,1) | 3584/9 |
| 11 | (0,0,0,4) | 134272/9 |
| 11 | (0,0,2,2) | -25024/9 |
| 11 | (0,2,0,2) | -29888/9 |
| 11 | (2,0,0,2) | -7552/9 |
| 12 | (0,1,1,2) | -2432/9 |
| 13 | (0,1,0,3) | 29440/9 |
| 22 | (0,0,0,4) | 134272/9 |
| 22 | (0,0,2,2) | -29888/9 |
| 22 | (0,2,0,2) | -25024/9 |
| 22 | (2,0,0,2) | -7552/9 |
| 23 | (0,0,1,3) | 29440/9 |
| 33 | (0,0,0,4) | -193024/9 |
| 33 | (0,0,2,2) | 61376/9 |
| 33 | (0,2,0,2) | 61376/9 |
| 33 | (2,0,0,2) | 3584/9 |

The exact matrix residual is identically zero in all 180 rows.

## Independent unreduced diagnostic

The candidate Q4 was then converted from trace-reversed form back to the metric perturbation and substituted into the direct unreduced covariant linearized-Einstein formula, independently of the reduced-system solve.

Through the frozen orders:

- `nabla^a qbar_ab = 0` identically through coordinate degree three for all four `b`;
- every one of the ten independent components of `DG_ab[q]-S_ab` is identically zero through coordinate degree two.

No numerical tolerance is used in either test.

This checks the complete Iter057M algebraic/gauge/unreduced machinery for the candidate source representation. It does **not** authorize the source representation itself; that is precisely what run `34952811799` is auditing.

## Decision boundary

If the authorized Iter057K-lineage component audit agrees with the diagnostic source convention, this candidate is ready to be promoted into a durable Iter057M exact construction after the source jet and audit provenance are frozen.

If the audit disagrees, all source-specific values in this note remain diagnostic and must be discarded/recomputed. The universal rank/Bianchi result in `8a6a5a56...` is unaffected.

No terminal classification is assigned here. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; finite Taylor consistency is not an open-neighborhood/global theorem; theory established remains `0%`.