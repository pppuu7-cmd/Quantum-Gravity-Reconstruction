# Iteration 044 — end-to-end QGR-L1 linearized radiative dynamics contract

Date: 2026-09-12
Status: `PREREGISTERED / IMPLEMENTATION NOT YET INSPECTED`

## Scientific question

Does the already-derived QGR-L1 **dynamical kinetic operator**, without inserting a TT solution by hand, possess exactly the two massless radiative physical modes on the internally derived incidence cone, and do those QGR dynamical modes map through the corrected observable layer to the independent TT radiative curvature validated by Iter043?

This gate starts from QGR dynamical authority, not from the analytic TT curvature used as the input object in Iter043.

## Frozen upstream authority

No new continuum theory is inserted. The allowed inputs were independently established before this gate:

1. `ITER004_G6_SELECT_L1`: QGR-L1 is the unique selected two-mode derivative-gauge-closed branch in the frozen `Sym^2(W4)` family; its characteristic form is `C=J-I`; all `S4`-invariant onsite quadratic masses are forbidden.
2. `ITER005_G1B_CUBIC_NOETHER_CLOSURE` and `ITER005_G2_EXACT_QUARTIC_NOETHER_CLOSURE`: nonlinear pullback/Noether consistency exists beyond quadratic order.
3. `ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION`: in the metric-only local at-most-two-derivative sector the all-orders action is fixed as the unique curvature scalar density up to the already fixed normalization and boundary term.
4. G42R: all-coordinate observable reconstruction is the valid frame convention for covariance tests.
5. Iter043: the corrected observable layer independently passed the held-out analytic TT radiative geometry gate.

The a-posteriori identification of the QGR-L1 kinetic operator with the standard massless spin-2 operator is **not** used as a fitting criterion here. Production must reconstruct the frozen QGR-L1 Hessian from its exact S4/Noether construction.

## Frozen incidence-to-orthonormal chart

Use the internally derived contravariant incidence form

`C = J-I`.

Freeze the deterministic orthonormal eigenbasis

- `t=(1,1,1,1)/2`, eigenvalue `+3`;
- `s1=(1,-1,0,0)/sqrt(2)`;
- `s2=(1,1,-2,0)/sqrt(6)`;
- `s3=(1,1,1,-3)/sqrt(12)`, each eigenvalue `-1`.

Let `O=[t,s1,s2,s3]`, `eta=diag(1,-1,-1,-1)`, and

`A = diag(sqrt(3),1,1,1) O^T`,

so prospectively `C = A^T eta A` and `A C^{-1} A^T = eta`.

For a Minkowski-chart covector `p`, incidence covector is `k=A^{-1}p`. For a covariant perturbation, `h_inc=A^{-1} h_M A^{-T}` and conversely `h_M=A h_inc A^T`.

No chart parameter is fitted in production.

## Frozen held-out radiative panel

Reuse the *parameter panel* of Iter043 only to permit an exact end-to-end comparison, not its result values:

- amplitude `a=0.013`;
- wave number `K=1.7`;
- propagation directions `x,y,z`;
- polarization mixing angles `psi=[0,pi/8,pi/4,3pi/8]`;
- phases `phi=[0.23,1.07]`.

This gives 24 independent end-to-end lanes.

## Stream A — QGR-L1 dynamics -> TT curvature, 24 lanes

For each frozen direction/polarization/phase:

1. reconstruct the exact QGR-L1 Hessian from the complete S4-invariant quadratic two-derivative Noether family and the frozen `t=1/2` branch;
2. form null Minkowski covector `p=K(1,-n)` and incidence covector `k=A^{-1}p`;
3. construct the two-component transverse-traceless polarization in the orthonormal chart and pull it back to `h_inc`;
4. test the QGR equation `H_QGR(k) h_inc = 0` directly;
5. independently construct the four derivative-gauge directions `delta h_ab=k_a xi_b+k_b xi_a`;
6. build the linearized Riemann tensor from the QGR dynamical mode in incidence coordinates, transform all four covariant indices with `A`, and compare it with the direct orthonormal TT curvature.

Frozen PASS per lane requires:

- `|p^T eta p| < 1e-12` and `|k^T C k| < 1e-12`;
- QGR Hessian numerical rank `4` at relative SVD tolerance `1e-10`;
- gauge-map rank `4`;
- every gauge-vector normalized QGR residual `<1e-10`;
- pulled-back TT-mode normalized QGR residual `<1e-10`;
- transformed incidence-curvature/direct-TT-curvature relative Frobenius error `<1e-10`;
- direct TT curvature norm `>1e-10`.

The rank-4/nullity-6 result plus four independent gauge nulls supplies exactly two non-gauge null directions on the tested characteristic covector.

## Stream B — off-shell dispersion falsification, 12 lanes

Use 3 propagation directions x 4 polarization mixtures. For each lane keep `omega=K` and test spatial-frequency ratios

`r=[0.8,0.9,1.0,1.1,1.2]`

with `p=K(1,-r n)`.

Frozen PASS requires:

- at `r=1`, `rank(H_QGR)=4` and normalized TT residual `<1e-10`;
- at every `r != 1`, `rank(H_QGR)=6` and normalized TT residual `>1e-3`;
- the unique minimum residual over the five frozen ratios occurs at `r=1`;
- `|k^T C k|<1e-12` at `r=1` and `|k^T C k|>1e-3` off shell.

This is a finite falsification panel for the frozen linearized dispersion relation, not a global spectral theorem.

## Stream C — gauge end-to-end robustness, 8 lanes

Freeze eight representatives spanning directions/polarization/phase combinations and deterministic gauge covectors `xi` generated from fixed integer vectors normalized to unit Euclidean norm.

For each lane add a nonzero pure-gauge perturbation to the QGR TT mode.

Frozen PASS requires:

- pure-gauge normalized QGR residual `<1e-10`;
- QGR residual of `h_TT + delta h` remains `<1e-10`;
- linearized Riemann of the pure-gauge plane-wave perturbation has normalized magnitude `<1e-10` relative to the physical TT curvature;
- end-to-end radiative curvature of the gauge-shifted mode agrees with the unshifted result to `<1e-10` relative Frobenius error.

## Stream D — six-derivative coefficient decoupling at linear order, 4 lanes

The currently authorized leading six-derivative direction is `c6 * Weyl^3`, with `c6` explicitly unfixed.

Freeze four generic non-type-N linearized curvature witnesses generated from deterministic off-shell symmetric perturbations. For each witness test field scalings `epsilon=[-2,-1,0,1,2]` in arbitrary common units.

Because linearized Weyl curvature is first order in the perturbation, a genuine cubic Weyl density must be cubic in `epsilon` around the flat background. PASS requires:

- `W3(0)=0` to absolute tolerance `1e-14`;
- oddness `W3(+e)+W3(-e)` normalized by max nonzero magnitude `<1e-12` for e=1,2;
- cubic scaling `W3(2)/W3(1)=8` within relative error `<1e-10` when the denominator is nonzero;
- centered second variation `[W3(+e)+W3(-e)-2W3(0)]/e^2` normalized by max nonzero magnitude `<1e-12`.

Thus a PASS says only that the `c6 Weyl^3` operator contributes no quadratic Hessian about the flat branch and therefore cannot alter the **linearized** QGR-L1 propagator/dispersion. It does not fix c6 and does not control nonlinear/higher-background propagation.

## Production matrix

- A: 24 lanes;
- B: 12 lanes;
- C: 8 lanes;
- D: 4 lanes;
- total: **48 scientific lanes** + aggregate;
- fail-fast disabled;
- maximum safe parallelism target: 24.

## Frozen aggregate classifications

`PASS_SCOPED_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION_CONTRACT`
requires all 48 lanes to pass with valid controls.

`PARTIAL_SCOPED_QGR_L1_LINEARIZED_RADIATION_CONTRACT`
if controls are valid and at least one complete stream passes but one or more scientific streams fail.

`FAIL_SCOPED_QGR_L1_LINEARIZED_RADIATION_CONTRACT`
if controls are valid and the QGR dynamical/observable bridge fails without a complete positive stream sufficient for PARTIAL.

`ITER044_CONTROL_OR_IMPLEMENTATION_INVALID`
if frozen authority reconstruction, chart identities, artifact completeness, or required controls are invalid.

No threshold may be changed after production results are inspected.

## Claim locks

Even full PASS establishes only a scoped **linearized end-to-end QGR-L1 radiative contract** on the frozen finite panel. It does not establish:

- generic nonlinear gravitational-wave solutions;
- global hyperbolicity or a global spectral theorem;
- quantum radiation amplitudes;
- experimental confirmation;
- a physical absolute microscopic scale;
- `beta=1`;
- a value for `c6`;
- all-orders quantum finiteness/renormalizability;
- independent KMQGB acceptance;
- a complete quantum-gravity theory.

Theory established remains `0%`.
