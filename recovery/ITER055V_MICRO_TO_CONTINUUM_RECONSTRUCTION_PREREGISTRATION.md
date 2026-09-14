# Iter055V preregistration — microscopic-to-continuum reconstruction authority

Date: 2026-09-14
Gate: `ITER055V-MICRO-TO-CONTINUUM-RECONSTRUCTION-AUTHORITY`

## Frozen question
Does existing QGR authority define an explicit topology-controlled map `R_h` from finite microscopic/coarse path-groupoid configuration data `(G_v,A_e)` to a continuum response/metric/connection or characteristic one-particle field, strong enough that its dual/adjoint or a controlled inverse on its range can induce the missing continuum-to-B3 attachment of Iter055T/U?

## Frozen authority set
Audit only existing QGR sources relevant to emergence/matching:

1. early definition of continuum response/metric variables from microscopic response data;
2. weak-curvature `G + Riemann(20)` and strong-curvature path-groupoid blocking results;
3. G7A microscopic-continuum power counting and normalization;
4. torsion-free discrete connection reconstruction;
5. any explicit interpolation, reconstruction, convergence topology, sampling theorem, finite-element map, cell average or continuum-limit morphism;
6. later benchmark codes only as negative controls unless their evaluation/sampling rule is explicitly promoted to general authority.

## Frozen obligations
1. Identify an explicit domain, codomain and formula for `R_h` beyond asymptotic scaling notation.
2. Require control of convergence/topology sufficient to pair with continuum test functions or characteristic Hilbert data.
3. Require covariance/gauge compatibility on the stated scope.
4. Require that the map acts on generic allowed microscopic data, not only on one chosen analytic benchmark inserted into lattice coordinates.
5. If only a continuum field -> discrete benchmark evaluation exists, do not invert it post hoc.
6. If an explicit `R_h` exists only in weak-curvature/local scope, classify only that scope and determine whether its dual actually reaches the finite B3 variables needed by the current bridge.

## Frozen classifications
- `PASS_SCOPED_ITER055V_SOURCE_DEFINED_MICRO_TO_CONTINUUM_RECONSTRUCTION_CAN_SEED_B3_ATTACHMENT` only if a source-defined map with sufficient topology/covariance exists and its dual/range structure can prospectively seed the missing attachment.
- `BLOCKED_OBJECT_DEFINITION_ITER055V_MICRO_TO_CONTINUUM_RECONSTRUCTION_MAP_NOT_SOURCE_DEFINED` if the repo contains continuum ansatzes, scaling, curvature expansions and benchmark sampling but no generic topology-controlled reconstruction map.
- `PASS_SCOPED_PARTIAL_ITER055V_WEAK_CURVATURE_RECONSTRUCTION_EXISTS__INSUFFICIENT_FOR_CURRENT_B3_BRIDGE` if a real weak/local reconstruction exists but does not cover the required finite B3/one-particle sector.
- `INVALID_PROVENANCE_ITER055V_MICRO_CONTINUUM_AUTHORITY_CONFLICT` only if existing authorities disagree on the object identity.

## Interpretation ceiling
A PASS would only supply emergence/sector-identification structure; it would not define interacting boundary dynamics. A BLOCKED result would move the candidate-defining gap upstream from discretization choice to the micro-continuum emergence map itself. No beta/c6/Weyl3/regulator/unitarity/UV/GR/experiment/theory claim follows.

No GitHub Actions run is preregistered; this is a source/object-definition audit.
