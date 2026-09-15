# Iter057R terminal result — corrected Einstein-seed Weyl3 second source jet

Date: 2026-09-15
Gate: `ITER057R-CORRECTED-SEED-WEYL3-SECOND-SOURCE-JET`
Preregistration: `582ff376a59458270b7074d5470dedfba85896af`
Corrected implementation: `3db68ebc21b5bac124c3a7206d7a74d87645c142`
Workflow head: `cc41b51e6ae0601140bdc699e9c7b41e5fd1560d`
Actions run: `34956884376`
Job: `104340972108`
Artifact: `10391406650` (`iter057r-corrected-seed-weyl3-second-source`)
Artifact digest: `sha256:cd3841e228dbb6009bfb8667d911d934364ea9cc489cbf73d59c993c906f82f6`

## Terminal classification

**`PASS_SCOPED_ITER057R_CORRECTED_EINSTEIN_SEED_WEYL3_SECOND_SOURCE_JET_EXACTLY_EXPOSED__ONSHELL_O_C6_Q2_Q4_RECONSTRUCTION_CAN_RESTART`**

This is exactly the prospectively frozen maximum scoped PASS.

## Seed and exact controls

The evaluator replays the exact canonical Iter057Q sextic seed and performs full four-dimensional exact Fraction polynomial algebra:

`metric degree 6 -> curvature/Weyl degree 4 -> P degree 4 -> D,E_W3 degree 2`.

Every frozen control passes exactly:

- Iter057Q replay;
- inverse identity through coordinate degree four;
- seed Ricci/scalar zero through degree four;
- `P.R=3 I3` through degree four;
- symmetry of `E_W3_ab` through degree two;
- trace Ward identity through degree two;
- Noether divergence through degree one;
- even seed parity;
- vanishing first partial derivatives of the Euler source at the origin;
- exact replay of the terminal Iter057P point source.

No numerical tolerance or finite difference is used.

The preserved point data remain

`I3(0)/kappa^3=96`,

`E_W3,ab(0)/kappa^3=diag(-240,-384,-384,432)`.

## Authoritative corrected source

Factor out the finite nonzero Einstein normalization and define

`Shat_ab := A_E S_ab = -E_W3,ab`.

The corrected on-shell zeroth-order source is

**`Shat^(0)_ab/kappa^3 = diag(240,384,384,-432)`**.

The complete nonzero normalized coordinate-degree-two coefficients `Shat_ab[alpha]/kappa^4`, with `alpha=(t,x,y,z)`, are:

- `00`: `t^2=-448`, `x^2=3936`, `y^2=3936`, `z^2=-26240`;
- `01`: `t x=2896`;
- `02`: `t y=2896`;
- `03`: `t z=-6240`;
- `11`: `t^2=10736`, `x^2=6832`, `y^2=7952`, `z^2=-14960`;
- `12`: `x y=-560`;
- `13`: `x z=-3952`;
- `22`: `t^2=10736`, `x^2=7952`, `y^2=6832`, `z^2=-14960`;
- `23`: `y z=-3952`;
- `33`: `t^2=-19904`, `x^2=-10272`, `y^2=-10272`, `z^2=2816`.

All other normalized degree-two coefficients vanish exactly.

There are 22 nonzero degree-two coefficients in total, including 7 with a time index.

At the frozen `kappa=2/25`, the artifact contains the corresponding exact rationals; no decimal approximation is needed for the decision.

## Comparison with historical off-shell G3 source

The historical Iter057M source was reconstructed on the uncompleted/off-shell G3 seed. Both its point source and its second source jet differ from the corrected Einstein-seed source above.

In particular, the historical source had no time-containing degree-two coefficients, while the corrected six-jet seed generates seven exact time-containing coefficients.

Therefore the old Iter057M affine RHS cannot be transplanted into the corrected-seed problem. Only the source-independent universal Q4 principal matrix/Bianchi machinery may be reused.

## Consequence

The next admissible constructor is a fresh `O(c6)` first-order quadratic+quartic correction on the canonical Einstein-completed seed:

`A_E DG_ab[q] + E_W3,ab[g_seed]=0`

through coordinate degree two.

The quadratic correction must use the new `Shat^(0)`. The quartic affine RHS must use the new `Shat^(2)` and the corrected background coefficient jet. Exact de Donder, Bianchi/Noether and independent unreduced substitution controls remain mandatory.

## Scope ceiling

This PASS exposes only the corrected-seed Weyl3 source through coordinate degree two. It does not yet construct the corresponding `O(c6)` correction, prove an all-orders/open-neighborhood Einstein+Weyl3 background, establish convergence/global boundary data, physical characteristics, hyperbolicity, ghosts, stability, unitarity, regulator removal, UV completion, experiment, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.