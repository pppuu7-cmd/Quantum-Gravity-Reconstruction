# QGR Iteration 007 — All-Orders Local Gravity and Distinguishability

Date: 2026-09-12
Status: `ACTIVE / ALL_ORDERS_LOCAL_TWO_DERIVATIVE_ACTION_FIXED / FIRST_BEYOND_GR_COARSE_CORRECTION_DERIVED`
Current task completion: **55%**
Candidate-program readiness: **76%**
Active candidate: **QGR-L1**

## Starting authority

Iter006 closed the regular state/measure/composition/refinement layer and exposed then resolved a crucial finite-connection ambiguity:

- all coarse torsion roots are **not** finite; a disconnected noncompact branch exists even at the flat seed;
- the physical connection is nevertheless selected prospectively as the identity-connected refinement branch because the infinitesimal Levi-Civita connection had already been derived from `G,DG`;
- strong-curvature coarse transport is defined by products/refinement of the principal local branch, not by summing every coarse torsion root.

Authoritative records:

- `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
- `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`

## Iter007 objective

Answer two questions that now determine the scientific status of QGR:

1. Is the local nonlinear gravitational action fixed to all orders, or only through quartic order?
2. If the local infrared action is GR-like, what specific quantum/refinement structure distinguishes QGR from classical GR and potentially from other QG frameworks?

No new coefficient may be introduced merely to create novelty.

## G1 — all-orders local two-derivative action

Inputs already fixed before G1:

- Lorentzian symmetric response `G`;
- exact pullback law;
- unique torsion-free compatible connection;
- flat seed;
- unique `S2`, unique `S3`, unique `S4`;
- exact connection-density witness matching all three with one normalization.

Restrict to local metric-only scalar densities with at most two derivatives and no extra background tensors.

### Invariant count

- zero derivatives: only `sqrt(|det G|) Lambda`;
- one derivative: no metric-compatible tensor scalar;
- two derivatives: one curvature tensor, contracted by two inverse metrics.

The three naive Riemann contractions reduce to

- `G^{ac}G^{bd}R_abcd=R`;
- `G^{ad}G^{bc}R_abcd=-R`;
- `G^{ab}G^{cd}R_abcd=0`.

Thus the nonzero curvature scalar space is one-dimensional.

The flat seed and prior mass/potential/tadpole exclusions fix `Lambda=0`. The QGR quadratic normalization fixes the remaining overall factor.

Therefore, modulo a boundary term,

`S_local[G] = a integral sqrt(|det G|) R[G]`

is the unique all-orders local metric-only two-derivative completion.

The connection-density used earlier is exactly the boundary-equivalent first-derivative form of this action and already matched independently derived `S2`, `S3`, and `S4`.

Classification:

`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

Record:

- `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
- `code/qgr_iter007_g1_curvature_scalar_count.py`

## G2 — exact 24-history ordering covariance

For directional transport generators `X_i`, an ordering `pi` has

`U_pi=product exp(h X_pi)`.

The ordering-dependent second-order BCH displacement is

`delta_pi=(h^2/2) sum_(i<j) s_pi(ij)[X_i,X_j]`.

Across all `24` permutations,

`<s_(ij)>=0`.

The exact six-dimensional sign covariance has spectrum

- `1/3` with multiplicity `3`;
- `5/3` with multiplicity `3`.

After the history label is traced, the action phase cancels in each Kraus term and the leading nonunitary correction in the common-unitary interaction frame is

`Delta E(rho)=(h^4/8) sum_(a,b) C_ab [K_a,[K_b,rho]] + O(h^5)`,

where `K_(ij)=[X_i,X_j]`.

Thus the first nonunitary history-ordering correction is `O(h^4)`, curvature controlled, positive/random-unitary in origin, and has no fitted relative coefficient. The two three-dimensional `S4` sectors have fixed relative strength `1:5`.

Classification:

`PASS_SCOPED_EXACT_24_HISTORY_ORDERING_COVARIANCE_FIXES_LEADING_H4_CURVATURE_DEPENDENT_COARSE_QUANTUM_CORRECTION`.

Record:

- `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
- `code/qgr_iter007_g2_history_ordering_covariance.py`

## G3 — finite-cell Lorentz covariance audit

Use the explicit continuous `C`-preserving rational boost from Iter004 and its induced two-form representation.

Control: the natural two-form metric induced by `C` is preserved exactly.

Test: the G2 ordering covariance is not preserved. At the recorded `r=2` witness, `33` covariance-difference entries are nonzero and the largest exact difference is `8/3`.

Therefore the finite-cell correction has microscopic `S4` symmetry, not full continuous Lorentz invariance.

Classification:

`PASS_SCOPED_FINITE_CELL_HISTORY_ORDERING_CORRECTION_HAS_ONLY_MICROSCOPIC_S4_SYMMETRY_AND_BREAKS_CONTINUOUS_LORENTZ_AT_O_H4`.

Record:

- `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
- `code/qgr_iter007_g3_lorentz_covariance_audit.py`

## G4 — positive-covariance Lorentz no-go

The ordering covariance is positive definite. If a nonzero positive-definite covariance were invariant under the full represented continuous Lorentz group, the representation would be conjugate into `O(6)` and therefore bounded.

But the two-form Lorentz representation contains unbounded boosts. Hence a nonzero positive covariance on the full nontrivial pair/two-form sector cannot be exactly full-Lorentz invariant.

The exact QGR boost witness shows rapidly growing transformed covariance norm for `r=2,4,8,16`.

Therefore exact finite-cell Lorentz invariance cannot be restored by a normalized positive orientation average. Lorentz recovery must occur because the correction itself is suppressed/vanishes under refinement, or the model predicts a finite microscopic preferred-frame effect.

Classification:

`PASS_SCOPED_NONZERO_POSITIVE_ORDERING_CHANNEL_CORRECTION_CANNOT_HAVE_EXACT_FULL_CONTINUOUS_LORENTZ_INVARIANCE_AT_FINITE_CELL_SCALE`.

Record:

- `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`
- `code/qgr_iter007_g4_positive_covariance_lorentz_nogo.py`

## Current scientific interpretation

QGR now separates cleanly into two layers:

### Local continuum gravitational sector

Within the metric-only, at-most-two-derivative class, the all-orders action is uniquely fixed and is algebraically the Einstein-Hilbert action of the emergent response metric `G` on the zero-cosmological flat branch.

### Finite-refinement quantum sector

The 24-history composition produces a fixed curvature-dependent random-unitary coarse correction beginning at `O(h^4)`. This correction retains microscopic `S4` structure and therefore is not exactly Lorentz invariant at finite cell size.

This is the first internally derived candidate distinction between QGR and classical GR.

## Active blocker / next gate — G5

`QGR-ITER007-G5-REFINEMENT_SCALE_AND_NORMALIZED_OBSERVABLE_CLOSURE`

1. derive how the `O(h^4)` history-ordering correction scales under repeated blocking/refinement;
2. determine whether it is an irrelevant correction that vanishes fast enough in the continuum limit;
3. identify a normalized operational observable sensitive to the correction;
4. map the six commutator/curvature components into that observable without arbitrary matching functions;
5. determine whether the microscopic scale `h` is predicted, bounded, or remains a free parameter;
6. compare the resulting tensor/scale structure with existing Lorentz-violation/decoherence constraints only after the observable map is fixed;
7. do not add orientation weights or noncompact averaging to erase the finite-scale anisotropy.

## Claim locks

- no experimental Lorentz violation is claimed yet;
- the physical microscopic scale `h` is not yet identified;
- no normalized beyond-GR observable is closed yet;
- higher-derivative quantum/RG operators beyond the history correction are not yet classified;
- no independent KMQGB pass;
- KMQGB `NEW_REQUIRED` remains unauthorized;
- QGR is not claimed unique as a full quantum-gravity theory.

## Progress accounting

- Iter007 completion: **55%**.
- Candidate-program readiness: **76%**.
- These are construction-roadmap metrics, not probabilities of correctness.
