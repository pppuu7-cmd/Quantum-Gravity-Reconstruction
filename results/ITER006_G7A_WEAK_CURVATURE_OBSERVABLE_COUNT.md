# QGR Iter006-G7A — minimal weak-curvature holonomy/curvature observable count

Date: 2026-09-11
Status: `PASS_SCOPED_WEAK_CURVATURE_OBSERVABLE_COUNT_20`

## Objective

Determine the minimal local information beyond `G` needed to retain history/path-order effects in a weakly curved coarse block, without storing arbitrary independent loop matrices or using field equations prematurely.

## Raw curvature data

In four relational directions there are

`C(4,2)=6`

independent oriented plaquette/direction pairs.

The torsion-free compatible connection takes values in

`o(1,3)`

with dimension six.

Thus a raw local curvature two-form has

`6*6=36`

components before the Levi-Civita algebraic symmetries are imposed.

## Levi-Civita algebraic reduction

Write the curvature with all indices lowered as `R_ijkl`. Metric compatibility and the torsion-free connection give the algebraic symmetries

- `R_ijkl = -R_jikl`;
- `R_ijkl = -R_ijlk`;
- `R_ijkl = R_klij`;
- first Bianchi: `R_i[jkl]=0`.

Treating antisymmetric index pairs as a six-dimensional space, pair-exchange symmetry first makes `R` a symmetric `6 x 6` matrix with

`6*7/2 = 21`

components.

In four dimensions the first Bianchi identity removes one further independent component, leaving

`21-1 = 20`.

Therefore the weak-curvature local holonomy content of the derived Levi-Civita connection has exactly **20** independent off-shell components.

Classification:

`PASS_SCOPED_LOCAL_WEAK_CURVATURE_HOLONOMY_DATA_REDUCES_FROM_36_TO_20_LEVI_CIVITA_COMPONENTS`.

## Coarse-state implication

To leading nontrivial area order,

`W_ij = I + R_ij * Area_ij + higher orders`.

Hence a locally slowly varying coarse state that retains

- the ten-component `G`, and
- the twenty-component Levi-Civita curvature sector

contains enough information to predict leading history-order/holonomy effects without keeping arbitrary independent loop matrices.

This is a controlled weak-curvature statement, not an exact strong-curvature truncation theorem.

## Important guard

No field equations were used. In particular the count is **not** reduced from 20 to the ten Weyl components by assuming vacuum Einstein equations. Doing so at this stage would be circular.

## What remains open

- strong-curvature finite holonomy may require genuinely nonlocal/group-valued loop data rather than only local `R_ijkl`;
- derivatives of curvature can enter larger-block transport;
- the quantum operator algebra and physical inner product for these coarse curvature observables remain to be constructed;
- normalized interacting amplitudes remain open.

## Next use

Use the 20-component curvature sector as the minimal weak-curvature candidate when testing projective coarse closure and quantum observable reconstruction.
