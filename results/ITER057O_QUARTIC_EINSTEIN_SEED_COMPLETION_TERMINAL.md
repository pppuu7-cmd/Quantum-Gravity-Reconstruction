# Iter057O terminal result — quartic c6^0 Einstein-seed completion

Date: 2026-09-15
Gate: `ITER057O-QUARTIC-EINSTEIN-SEED-COMPLETION`
Preregistration: `f4d06a6b97cb063bca8887731d7999d010863e93`
Implementation: `d72c71f0296120d1d8a720b2d85886007dcb9c95`
Workflow head: `a19cc7c44212982c4ab49ab68ec412b6438f381b`
Actions run: `34955436259`
Job: `104336254393`
Artifact: `10391082054` (`iter057o-quartic-einstein-seed`)
Artifact digest: `sha256:e40fde949ec688e2be507ee9e54b8efb960c650d4d15e51b4a911d5e5b4c3d84`

## Terminal classification

**`PASS_SCOPED_ITER057O_QUARTIC_EINSTEIN_SEED_COMPLETES_G3_THROUGH_QUADRATIC_ORDER__WEYL3_SOURCE_MUST_BE_RECOMPUTED`**

This is exactly the prospectively frozen maximum scoped PASS.

## Exact construction

Consume the complete Iter057N quadratic Einstein residual and parameterize the unrestricted trace-reversed quartic seed correction

`rbar_ab=(1/24)R4_ab,cdef x^c x^d x^e x^f`.

The coefficient system is the full `180 x 350` gauge+Einstein polynomial complex. Exact arithmetic gives

`rank(M)=164`,

`rank([M|r])=164`,

all 16 canonical Bianchi compatibility contractions exactly zero, and quartic homogeneous nullity `186`.

The canonical pivot particular solution has 21 nonzero normalized coefficients after factoring out `kappa^2`. No restricted conformal/diagonal/static-component/spherical/plane-wave ansatz is used.

## Origin preservation

Because the correction starts at coordinate degree four, the fresh-run controls verify exactly

`r(0)=0`, `partial r(0)=0`, `partial^2 r(0)=0`.

Therefore the corrected seed preserves the frozen origin metric, connection and Riemann/Weyl tensor exactly. In particular the original electric-Weyl eigenvalues at the origin remain unchanged.

The combined G3 quadratic seed plus quartic correction also satisfies the frozen linear de Donder condition exactly through the required orders.

## Independent full-metric nonlinear control

The production evaluator does not rely only on the flat-principal/reduced solve. It constructs

`g_seed = g_G3 + r^(4)`

and recomputes the nonlinear Levi-Civita connection, Ricci tensor, scalar and Einstein tensor through coordinate degree two.

Fresh-run output gives all ten independent components exactly zero:

`G_00=G_01=G_02=G_03=G_11=G_12=G_13=G_22=G_23=G_33=0`

through the frozen degree. Ricci and scalar curvature vanish through the same degree as well.

Every frozen exact control is `true`, including inverse identity, origin-data preservation, Bianchi compatibility, exact linear-system residual, and full nonlinear Einstein substitution. No numerical tolerance is used.

## Consequence

Iter057N showed that the unchanged G3/H0 metric is not a valid `c6^0` neighborhood seed. Iter057O repairs that defect through the first nonlinear coordinate order without changing the frozen origin curvature.

This does **not** restore authority to the old G3/H0 Weyl3 Euler source. The quartic correction changes fourth derivatives of the metric at the origin, while `E_W3` contains the double covariant divergence of `P` and is generically fourth order in the metric.

Therefore `E_W3[g_seed](0)` and every successor Weyl3 source jet must be recomputed from the corrected seed before any `O(c6)` correction is consumed.

## Scope ceiling

This PASS is only a local Einstein-seed completion through coordinate degree two. It does not establish Ricci-flatness to all orders, a convergent/open-neighborhood vacuum metric, global/asymptotic boundary conditions, or a solution of Einstein+Weyl3.

`c6` remains symbolic/unfixed and was not used in this zeroth-order seed construction; `beta=1` remains unauthorized; theory established remains `0%`; no experimental, hyperbolicity, ghost, stability, unitarity, regulator-removal or UV-completion claim is authorized.