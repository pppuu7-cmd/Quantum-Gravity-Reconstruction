# Iter056N analysis — G3 common refinement-parameter identity

Date: 2026-09-14
Preregistration: `5991091b03c91f98532d28ff9759ae9c4c0f33e0`
Frozen cutoff: `091463e97182e05d125e788ec565eb46f9a3061d`

## Frozen verdict table

| Obligation | Verdict | Reason |
|---|---|---|
| A same continuum/field realization | YES, scoped | Iter054S freezes `code/qgr_iter010_g3_common.py`, G3 weak static tidal `Phi=(kappa/2)(x^2+y^2-2z^2)`. Iter040 H0 is exactly `diag(1,1,-2)` and `phi_general=0.5*kappa*s^T H0 s`, reproducing the same tidal potential and tetrad family. |
| B same finite geometric primitive | YES | In both constructions `h` multiplies the integer lattice coordinate before the same `RMI` physical-coordinate map. The finite connection is solved on unit index displacements, so one index edge has physical displacement set by the same `h`. |
| C same refinement operation | NOT ESTABLISHED | Iter054S defines an actual parent/fine operation on a fixed physical path/loop: `N={2,4,8,16}`, `h=ell/N`, then ordered child products are compared across N. Iter040/041 evaluate the local curvature/Weyl proxy independently at a list of `h` values and call this finite numerical continuum-proxy/refinement evidence. They do not define a parent cell as a composition/sum of identified child Weyl3 cells, nor a history/amplitude/measure parent→child map. |
| D source-faithful scale map | YES for the scale itself | Iter054S source-locks `h=ell_path/N` (or loop side/N). G3 defines physical coordinates as `RMI@(h*x)`. Iter040 uses the same physical meaning of `h`; no fitted multiplicative constant is needed to identify the lattice displacement. |
| E object-provenance compatibility | YES at common finite points; NOT sufficient for cross-level closure | Iter054S's Weyl control literally calls `g3.curvature_proxy(0.05,0.08)`. Iter040 Stream B includes H0 at `h=0.05,kappa=0.08`, and its H0 generalized source is algebraically the same G3 field/connection/holonomy-curvature construction. Thus a common finite G3 data point exists without beta/c6/treatment choices. What is absent is the required W3 parent→children relation across scales. |

## Exact source identity

Original G3:

`phi_minkowski(y,kappa) = 0.5*kappa*(y1^2+y2^2-2*y3^2)`

`y = RMI @ (h*x)`.

Iter040 H0:

`H0 = diag(1,1,-2)`

`phi_general(y,kappa,H0) = 0.5*kappa*s^T H0 s`

with the same `y = RMI @ (h*x)` and the same weak-field tetrad form. Hence the H0 field is not merely analogous; it is the G3 tidal field generalized through a matrix-valued Hessian parameterization.

Both solve the same six-generator Lorentz connection from the same torsion parallelogram closure and reconstruct curvature from the logarithm of the same type of path holonomy divided by `h^2`.

## Exact scale identity in Iter054S

For a fixed physical path length `ell_path=0.20`, Iter054S freezes

`h = ell_path/N`

with `N={2,4,8,16}` and `x_index = b/h + n e_i`, so `g3.tetrad_at(x_index,h,kappa)` evaluates the same physical background while the path is subdivided.

The corresponding path spacings are `0.10,0.05,0.025,0.0125`. Thus `h=0.10` and `h=0.05` are also members of the Iter040/041 Weyl-response refinement panels. This overlap is source-derived, not fitted.

Iter054S further uses the exact common point `h=0.05,kappa=0.08` for its Weyl-activity control. Iter040 Stream B includes `kappa=0.08` at `h=0.05` for H0. Therefore there is an exact common finite G3 geometry point across the two programs.

## Why criterion C still fails

The existence of a common physical spacing does not by itself define one cross-level object.

Iter054S has a genuine composition map:

`P_N = L_{N-1} ... L_0`

on a fixed physical path, and analogous ordered products on fixed physical loops.

Iter040/041 instead evaluate a local curvature/Weyl estimator at several cell spacings. Their frozen contracts require convergence/trend of quantities such as `W3`, `W3/tr(H^3)` and normalized cubic residuals, but do not state that a coarse W3 cell equals or is mapped to a specified collection of fine W3 cells.

Therefore `h` is already a common finite-geometry scale, while the **Weyl3 parent→child composition rule** is not already part of repository authority.

Promoting independent `h` samples to a microscopic cylindrical/refinement map would violate the Iter056N frozen prohibition against identifying analogous numerical resolutions by convention.

## Consequence

The obstruction is now narrower than Iter056M:

- no new regulator variable is needed;
- no arbitrary scale factor between transport `h` and Weyl-response `h` is needed;
- the same G3 finite geometry can host both calculations;
- the missing object is specifically a source-faithful parent→children/cylindrical rule for a normalized Weyl3 action/response object on that common G3 lattice family.

This is a construction problem, not a scale-identification problem.