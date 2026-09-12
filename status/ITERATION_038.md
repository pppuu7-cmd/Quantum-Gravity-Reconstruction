# Iteration 038 — principal refinement regularity certificate and actual fine-to-coarse blocking

Date: 2026-09-12
Status: `PREREGISTERED / READY FOR PRODUCTION`

## Why this is the next main-line gate

G37C applied the previously frozen G10B same-realization rule to all six strongest distant nonlinear
torsion roots. All six numerically completed the audit but failed the physical identity/refinement-
connected criterion. Therefore those distant finite roots remain legitimate algebraic solutions but do
not currently supply additional physical connection branches. The main line returns to the G32/G33
blocker for the **principal** physical connection branch.

G32 showed that resolved fine-path data plus uniform regularity is sufficient for a unique cylindrical
projective action limit on the tested local construction. G33 identified the precise missing authority:
a uniform positive torsion-Jacobian gap along the refinement-relevant physical branch, rather than
pointwise regularity at isolated finite levels.

Iter038 attacks that principal-branch blocker with an exact small-h certificate plus independent
finite-range and actual physical-path/loop blocking tests.

## Frozen domain and model

Use the existing G10B/G37C physical finite-torsion equations and the existing smooth conformal frame
family `Omega(x)=exp(a.x + 1/2 x.Q.x)` with no new coupling.

Frozen compact coordinate region for this gate: `K=[0,1]^4`.

The scope claim is explicitly limited to this smooth compact realization/domain. No global field-space
or arbitrary-background theorem is authorized by this gate.

## A — exact small-h principal-branch Jacobian certificate

Set `z=h*w` and divide the finite torsion residual by `h`. At `h=0`, the derivative with respect to
`w` is the fixed 24x24 linearized torsion matrix `M` built from the already frozen `o(C)` basis and six
pair constraints.

The production certificate must compute with exact integer/rational arithmetic:

- `rank(M)`;
- `det(M)`;
- a numerical singular-value cross-check.

PASS requires exact `rank(M)=24` and exact `det(M) != 0`.

Scientific authority of this exact fact: because the finite residual is analytic in `(x,h,w)` and `K`
is compact, invertibility of the common `h=0` derivative supplies a **uniform sufficiently-small-h
identity-connected local solution and positive Jacobian gap on K** by finite-dimensional implicit-
function theory plus compactness. This is structural/analytic authority, not a numerical extrapolation.
It does not give a global strong-curvature branch theorem or an explicit optimal `h0`.

## B — finite-range bridge to the analytic small-h regime

Eight frozen positions in `K` are tested independently:

`[0,0,0,0]`, `[1,0,0,0]`, `[0,1,0,0]`, `[0,0,1,0]`, `[0,0,0,1]`,
`[1,1,1,1]`, `[0.25,0.25,0.25,0.25]`, `[0.5,0.1,0.3,0.7]`.

At each position solve only the G10B principal branch from the identity seed for

`h=[1/4,1/8,1/16,1/32,1/64,1/128]`.

Record residual, metric error, torsion-Jacobian singular values, condition number, `max||L-I||`, and
`||z/h-w_linear(x)||` where `w_linear(x)` is the exact first-order source solution for the local
`grad log Omega(x)=a+Qx`.

A position lane passes iff all six solves are qualified, minimum singular value across the lane is
`>0.20`, the final two observed orders of `max||L-I||` are each `>0.8`, and the scaled-linearized error
decreases across the last three refinements. `0.20` is a frozen conservative finite-range bridge
threshold, not an asserted universal constant.

## C — actual fixed-physical-path fine-to-coarse blocking

Eight frozen path cases are tested independently using principal identity-seeded subcell solves only:

- four unit coordinate-axis paths from the origin;
- four half-unit coordinate-axis paths from base `[0.25,0.25,0.25,0.25]`.

For each path compute ordered relational transport products at `N=[4,8,16,32,64]` equal physical
subcells. A path lane passes iff every subcell solve is qualified, successive product differences
strictly decrease over the final three refinements, and final contraction ratio
`||A64-A32||/||A32-A16|| < 0.75`.

This is an actual fixed-physical-path fine-product test, not the G36 coordinate shrinking proxy.

## D — elementary loop/groupoid blocking

For each of the six coordinate planes `(i,j)` test two frozen squares:

- base `0`, side length `0.5`;
- base `[0.25,0.25,0.25,0.25]`, side length `0.5`.

Total 12 loop lanes. Build each square holonomy from four fine principal path products at
`N=[4,8,16,32]` subdivisions per side. Record trace, trace2, determinant, metric error and successive
matrix differences.

A loop lane passes iff every side solve is qualified, metric error is `<1e-7`, final two holonomy
matrix differences strictly decrease, and final contraction ratio is `<0.80`.

## Production structure

- A exact certificate: 1 lane;
- B principal-gap bridge: 8 lanes;
- C physical-path blocking: 8 lanes;
- D loop blocking: 12 lanes;
- total: **29 scientific lanes** plus aggregate, fail-fast disabled.

## Aggregate classifications

`PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING`
requires exact A PASS, all 8 B lanes, all 8 C lanes and all 12 D lanes.

`PARTIAL_SCOPED_PRINCIPAL_SMALL_H_REGULARITY_CERTIFIED_BLOCKING_INCOMPLETE`
requires A PASS but at least one B/C/D lane fails or is incomplete.

`FAIL_OR_BLOCKED_PRINCIPAL_SMALL_H_CERTIFICATE`
if the exact matrix certificate fails or controls cannot be formed.

## Consequence if full PASS

Within the frozen smooth conformal realization on compact `K`, the G32 uniform-regularity condition is
no longer merely an unsupported assumption for the principal refinement-connected branch: exact
small-h IFT authority plus the frozen finite-range bridge supplies the required local/tower refinement
regularity mechanism on this domain, while C/D independently validate the actual principal
fine-to-coarse transport/groupoid construction numerically.

This still does **not** fix absolute quantum phase normalization, `beta`, or `c6`, and it does not prove
global field-space compactness or correctness of QGR.

## Claim locks

- G37 distant algebraic roots remain nonphysical under current frozen G10B evidence;
- exact small-h IFT scope is the frozen smooth compact realization, not arbitrary strong-curvature data;
- finite blocking convergence is numerical evidence, not an analytic all-path theorem;
- no physical multiple-branch measure is authorized;
- absolute phase normalization remains unfixed;
- `beta=1` remains unauthorized;
- `c6` remains unfixed;
- theory established remains `0%`;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
