# QGR Iteration 007 — All-Orders Local Gravity and Distinguishability

Date: 2026-09-12
Status: `ACTIVE / ALL_ORDERS_LOCAL_ACTION_FIXED / FIRST_BEYOND_GR_CORRECTION_AND_PATH_SCALING_DERIVED`
Current task completion: **65%**
Candidate-program readiness: **78%**
Active candidate: **QGR-L1**

## Starting authority

Iter006 closed the regular state/measure/composition/refinement layer and retained a crucial negative result rather than hiding it:

- all coarse torsion roots are **not** finite; a disconnected noncompact branch exists even at the flat seed;
- the physical connection is selected prospectively as the identity-connected refinement branch because the infinitesimal Levi-Civita connection had already been derived from `G,DG`;
- strong-curvature coarse transport is products/refinement of the principal local branch, not a sum over all algebraic coarse roots.

Authoritative records:

- `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
- `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`

## Objective

1. Determine whether the local nonlinear gravitational action is fixed to all orders.
2. Derive the first QGR-specific finite-refinement correction beyond classical GR.
3. Determine its refinement scaling, Lorentz properties, and a normalized operational observable.
4. Do not introduce a free coefficient merely to create novelty or hide an inconvenient finite-scale effect.

## G1 — all-orders local two-derivative action

Inputs fixed independently before G1:

- Lorentzian symmetric response `G`;
- exact pullback law;
- unique torsion-free compatible connection;
- flat seed;
- unique `S2`, unique `S3`, unique `S4`;
- exact connection-density witness matching all three with one normalization.

For local metric-only scalar densities with at most two derivatives and no extra background tensors:

- zero derivatives: only `sqrt(|det G|) Lambda`;
- one derivative: no metric-compatible scalar;
- two derivatives: one curvature tensor contracted by two inverse metrics.

The three naive Riemann contractions reduce to

- `G^{ac}G^{bd}R_abcd=R`;
- `G^{ad}G^{bc}R_abcd=-R`;
- `G^{ab}G^{cd}R_abcd=0`.

Thus the nonzero curvature-scalar space is one-dimensional. The flat seed and prior tadpole/mass/potential exclusions fix `Lambda=0`; the QGR quadratic normalization fixes the remaining overall factor.

Therefore, modulo a boundary term,

`S_local[G] = a integral sqrt(|det G|) R[G]`

is the unique all-orders local metric-only two-derivative completion.

Classification:

`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

Records:

- `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
- `code/qgr_iter007_g1_curvature_scalar_count.py`

## G2 — exact 24-history ordering covariance

For directional transport generators `X_i`,

`U_pi=product exp(h X_pi)`.

The ordering-dependent BCH displacement begins at

`delta_pi=(h^2/2) sum_(i<j) s_pi(ij)[X_i,X_j]`.

Across all `24` permutations,

`<s_(ij)>=0`.

The exact six-dimensional sign covariance has spectrum

- `1/3` with multiplicity `3`;
- `5/3` with multiplicity `3`.

After tracing the history label, the leading nonunitary correction in the common-unitary interaction frame is

`Delta E(rho)=(h^4/8) sum_(a,b) C_ab [K_a,[K_b,rho]] + O(h^5)`,

where `K_(ij)=[X_i,X_j]`.

Thus the first nonunitary history-ordering correction is `O(h^4)`, curvature controlled, positive/random-unitary in origin, and has no fitted relative coefficient. The two three-dimensional `S4` sectors have fixed relative strength `1:5`.

Classification:

`PASS_SCOPED_EXACT_24_HISTORY_ORDERING_COVARIANCE_FIXES_LEADING_H4_CURVATURE_DEPENDENT_COARSE_QUANTUM_CORRECTION`.

Records:

- `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
- `code/qgr_iter007_g2_history_ordering_covariance.py`

## G3 — finite-cell Lorentz covariance audit

An explicit continuous `C`-preserving rational boost preserves the correct induced two-form metric but does not preserve the G2 ordering covariance. At `r=2`, `33` covariance-difference entries are nonzero and the largest exact difference is `8/3`.

Therefore the finite-cell correction has microscopic `S4` symmetry rather than full continuous Lorentz invariance.

Classification:

`PASS_SCOPED_FINITE_CELL_HISTORY_ORDERING_CORRECTION_HAS_ONLY_MICROSCOPIC_S4_SYMMETRY_AND_BREAKS_CONTINUOUS_LORENTZ_AT_O_H4`.

Records:

- `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
- `code/qgr_iter007_g3_lorentz_covariance_audit.py`

## G4 — positive-covariance Lorentz no-go

The ordering covariance is positive definite. If a nonzero positive covariance were invariant under the full represented continuous Lorentz group, the representation would be conjugate into an ordinary compact orthogonal group. But the two-form Lorentz representation contains unbounded boosts and has no trivial scalar subrepresentation supporting the required nonzero positive covariance.

Therefore a nonzero positive finite-cell ordering correction cannot be exactly full-Lorentz invariant.

Lorentz recovery must occur because the correction vanishes under refinement, or finite physical `h` predicts a suppressed preferred-frame effect.

Classification:

`PASS_SCOPED_NONZERO_POSITIVE_ORDERING_CHANNEL_CORRECTION_CANNOT_HAVE_EXACT_FULL_CONTINUOUS_LORENTZ_INVARIANCE_AT_FINITE_CELL_SCALE`.

Records:

- `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`
- `code/qgr_iter007_g4_positive_covariance_lorentz_nogo.py`

## G5A — fixed-path refinement scaling

One sufficiently small cell has

`E_h = I + h^4 D + O(h^5)`.

For a smooth bounded connection/curvature field on a physical causal path of fixed length `L`, subdivide into

`N=L/h`

cells. Sequential composition gives

`Delta E_path = O(N h^4)=O(L h^3)`.

The first cross terms are `O(N^2 h^8)=O(L^2 h^6)` and accumulated local `O(h^5)` remainders are `O(L h^4)`.

Therefore at fixed path length

`h -> h/b`

suppresses the leading correction by

`b^-3`.

This establishes **path-level refinement irrelevance**. It is not yet promoted to a four-dimensional/network RG eigenvalue.

## G5A — normalized purity observable

Write `K_a=-iH_a` with Hermitian induced curvature generators `H_a`. For a density matrix,

`P=Tr(rho^2)`

is dimensionless and normalized. G2 implies

`Delta P = -(h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho]) + O(h^5)`.

Since the exact covariance `C` is positive definite,

`Delta P <= 0`.

For pure input,

`1-P_out = (h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho]) + O(h^5)`.

No free decoherence coefficient is introduced; the tensor coefficient is the exact microscopic ordering covariance.

Classification:

`PASS_SCOPED_FIXED_PATH_H3_REFINEMENT_IRRELEVANCE_AND_NORMALIZED_PURITY_LOSS_OBSERVABLE_FORM__PHYSICAL_MICRO_SCALE_OPEN`.

Records:

- `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`
- `code/qgr_iter007_g5_path_scaling_and_purity.py`

## Current scientific interpretation

QGR now separates into two internally connected layers.

### Local continuum gravitational sector

Within the metric-only, at-most-two-derivative class, the all-orders action is fixed and is algebraically the Einstein-Hilbert action of the emergent response metric `G` on the zero-cosmological branch.

### Finite-refinement quantum sector

The 24-history composition produces a fixed curvature-dependent random-unitary coarse correction beginning at `O(h^4)`. It has microscopic `S4` structure, is not exactly Lorentz invariant at finite cell scale, and is irrelevant along a fixed smooth causal path as `O(L h^3)`.

A normalized observable form now exists through purity loss, but the physical scale `h` remains unresolved.

## Active blocker / next gate — G5B/G6

`QGR-ITER007-G5B-PHYSICAL_SCALE_AND_FULL_NETWORK_RG_CLOSURE`

1. determine whether QGR fixes the microscopic/refinement scale `h`, only bounds it, or leaves one dimensionful parameter;
2. derive full graph/four-dimensional blocking of the ordering correction rather than extrapolating the path result;
3. map the six induced curvature generators to the physical two-mode quotient for a specified preparation/readout protocol;
4. evaluate the normalized purity-loss coefficient on at least one concrete physical background;
5. only then compare to Lorentz-violation/decoherence constraints;
6. classify other leading higher-derivative/refinement operators to ensure the history term is genuinely leading;
7. do not add orientation weights, noncompact averaging, or an arbitrary decoherence coefficient.

## Claim locks

- no experimental Lorentz violation is claimed yet;
- physical microscopic scale `h` is not yet fixed;
- purity-loss **form** is closed, but no numerical phenomenological prediction is closed;
- full network/4D RG scaling remains open;
- higher-derivative/refinement operators are not yet completely classified;
- no independent KMQGB pass;
- KMQGB `NEW_REQUIRED` remains unauthorized;
- QGR is not claimed unique as a full quantum-gravity theory.

## Progress accounting

- Iter007 completion: **65%**.
- Candidate-program readiness: **78%**.
- These are construction-roadmap metrics, not probabilities of correctness.
