# QGR Iter006-G10B — refinement-connected principal connection

Date: 2026-09-12
Status: `PASS_SCOPED_REGULAR_REFINEMENT_DOMAIN / DISCONNECTED_COARSE_ROOTS_EXCLUDED_BY_PRIOR_SAME_REALIZATION_RULE`

## Problem exposed by G10A

The finite coarse torsion polynomial has disconnected noncompact solution manifolds even at the exact flat seed.  Therefore QGR cannot define its connection by summing every algebraic torsion root or by requiring global finite-root counting on an arbitrarily coarse cell.

That is not, however, the connection definition that was fixed earlier in the reconstruction.

Before G10, QGR had already derived the infinitesimal torsion-free compatible connection from the same response field and first jets `G,DG`.  The finite connection is therefore a **derived transport** and must match that infinitesimal object under refinement.

## Prospective physical branch criterion

Define the physical finite connection branch by two requirements already fixed before the G10 counterexample:

1. on a constant flat response (`DG=0`) it approaches `L_e=I`;
2. for a regular smooth response and cell size `h->0`,

   `L_e(h)=I+h omega_e[G,DG]+O(h^2)`,

   where `omega_e` is the unique solution of the linearized torsion/Levi-Civita system.

This is the **identity-connected principal branch**.  It is not selected because distant branches are inconvenient; it is selected by the frozen same-realization condition linking the finite and infinitesimal connection objects.

## Conditional regular-domain theorem

Let `F(x)` be a regular Lorentzian frame field on a compact patch, with `F` and `F^{-1}` bounded and with bounded first and second jets.  Normalize each sufficiently small cell by the local frame at its base point.

At `h=0` the normalized finite torsion system is the symmetric seed.  Its connection Jacobian is invertible (`rank 24`, determinant `11664` in the recorded Lie-algebra basis).  The parameter-dependent implicit-function theorem therefore gives, for sufficiently small `h`, a unique local root in a neighborhood of the identity.

Because the normalized neighbor data differ from the seed by `O(h)`, this root is analytic and has

`L_e(h)=I+h omega_e+O(h^2)`.

The first coefficient is fixed by the linearized Cartan torsion equation and is the same compatible connection already obtained from the QGR first jets.

On a compact regular patch the required small-cell neighborhood can be chosen uniformly after finite covering.  Thus arbitrarily large but finite curvature does not require solving a single strong-curvature coarse torsion polynomial: refine until every cell lies on the principal local branch.

## Coarse transport

Strong-curvature coarse transport is then defined by composition of the fine principal transports.  If

`L_k=I+h omega(x_k)+O(h^2)`

with bounded/Lipschitz `omega`, the ordered product is the usual product-integral approximation and converges to the path-ordered transport as the mesh tends to zero.

This is consistent with the already established exact path-groupoid blocking rule.

## Numerical refinement audit

The deterministic finite-curvature conformal-frame family from G9 was rerun at

`h = 1, 1/2, 1/4, 1/8, 1/16`.

Using an identity/zero start at every cell, the selected root gives approximately

`max ||L-I|| = 0.5692, 0.2906, 0.1485, 0.07519, 0.03785`.

The observed convergence order tends to one (last step about `0.990`).

At `h=1/16`, the scaled connection parameters differ from the independently solved linearized torsion connection by about

`0.0066`

in the recorded 24-parameter norm.

For a fixed physical path subdivided into

`N=1,2,4,8,16`

cells, successive coarse-transport differences are approximately

`0.0338, 0.0185, 0.00972, 0.00499`,

showing the expected first-order product convergence.

## Consequence for the quantum measure

The connection is a derived function/limit of the response configuration, not an independent variable to be summed over all coarse algebraic roots.  Therefore the G8B coarea formula remains a useful diagnostic for regular auxiliary roots but is **not** the fundamental physical prescription for summing disconnected connection branches.

The normalized history instrument uses the refinement-connected principal transports.  Distant finite-cell roots that do not approach the previously derived infinitesimal connection are excluded by same-realization consistency.

## Boundary

The theorem is scoped to regular Lorentzian configurations with bounded jets and `det G` bounded away from zero on the patch.  Degenerate-metric strata or genuine curvature singularities are outside this regular refinement domain and are not thereby resolved.

Classification:

`PASS_SCOPED_REGULAR_REFINEMENT_CONNECTED_DISCRETE_LEVI_CIVITA_TRANSPORT_EXISTS_UNIQUELY_LOCALLY_AND_DEFINES_STRONG_CURVATURE_COARSE_TRANSPORT_BY_PRODUCT_LIMIT`.

## Reproducibility

- `code/qgr_iter006_g10b_refinement_connected_transport.py`
- G5 exact seed Jacobian certificate
- G9 finite-curvature branch audit
