# QGR Iter009-G4 — c6 decoupling, G6H scope and channel-convergence boundary

Date: 2026-09-12
Status: `PARTIAL_SCOPED_C6_UNDERDETERMINED / FLAT_AND_FIXED_GEOMETRY_G6H_DECOUPLING / CURVED_SELF_CONSISTENT_AND_INFINITE_LIMIT_OPEN`

GitHub Actions run `34663799182`: 6 lanes + aggregate SUCCESS.

## G4A — explicit c6 underdetermination family

The family

`S_lambda = S_EH + lambda * a_cont * h^4 * integral(Weyl^3)`

has the same field content, parity-even pullback covariance, frozen two-derivative sector and continuum `h->0` limit for arbitrary real `lambda`. Therefore the data that uniquely fixed the local two-derivative QGR action cannot by themselves determine the six-derivative coefficient `c6`.

Classification:
`BLOCKED_SCOPED_EXISTING_TWO_DERIVATIVE_SYMMETRY_AND_CONTINUUM_DATA_ADMIT_A_CONTINUOUS_C6_FAMILY_AND_DO_NOT_FIX_C6`.

This does not prove every `lambda` arises from one exact microscopic finite-cell realization; it proves lower-order authority is insufficient to choose one.

## G4B — exact flat Hessian decoupling

At the flat QGR seed `W0=0`, write

`W(epsilon)=epsilon W1+epsilon^2 W2+...`.

Any homogeneous cubic Weyl invariant starts at `epsilon^3`. Therefore

`delta S6|flat = 0`,
`delta^2 S6|flat = 0`.

Thus `c6 Weyl^3` does not alter the flat linearized QGR-L1 Hessian, its two physical modes, or the tree-level flat characteristic cone.

Classification:
`PASS_SCOPED_C6_WEYL_CUBED_DOES_NOT_MODIFY_THE_FLAT_QGR_LINEARIZED_HESSIAN_OR_TREE_LEVEL_CHARACTERISTIC_CONE`.

## G4C — curved-background activation

For a traceless Weyl-block witness

`W0=diag(-2,1,1)`, `w=diag(1,-1,0)`,

expanding `tr((W0+epsilon w)^3)` gives coefficients

`(-6, 9, -3, 0)`.

The `epsilon^2` coefficient is nonzero, so the second variation is nonzero on a nonzero-Weyl background.

Classification:
`PASS_SCOPED_NONZERO_BACKGROUND_WEYL_CURVATURE_GENERICALLY_ACTIVATES_A_C6_DEPENDENT_QUADRATIC_RESPONSE`.

## G4D — scalar Kraus phase cancellation

For

`K_alpha=N^-1/2 exp(i S_alpha/hbar) U_alpha`,

one has exactly

`K_alpha rho K_alpha^dagger = N^-1 U_alpha rho U_alpha^dagger`.

Therefore arbitrary scalar action phases — including a `c6` contribution that enters only through `S_alpha` — cancel from the traced history-mixture channel.

Classification:
`PASS_SCOPED_ARBITRARY_SCALAR_BRANCH_ACTION_PHASES_CANCEL_EXACTLY_FROM_THE_TRACED_HISTORY_MIXTURE_CHANNEL`.

Relative action phases remain available before the history register is discarded, and `c6` can still matter indirectly if it changes the self-consistent branch maps `U_alpha`.

## G4E — actual G6H code scope

The authoritative files

- `code/qgr_iter007_g6h_common.py`,
- `code/qgr_iter007_g6h_broadband_profile.py`,
- `code/qgr_iter007_g6g_common.py`

were audited directly.

The calculation follows

`broadband_profile -> branch_lorentz -> solve_paths(torsion/connection residual) -> Lorentz/Wigner/source-momentum overlaps`.

It contains no explicit `S_alpha`, `c6`, `Weyl^3` or action-phase input, and it does not solve equations of motion corrected by `c6`.

Classification:
`PASS_SCOPED_EXISTING_G6H_IS_A_FIXED_GEOMETRY_TRANSPORT_COMPARATOR_INDEPENDENT_OF_SCALAR_BRANCH_ACTION_PHASES_AND_HAS_NO_EXPLICIT_C6_INPUT`.

Therefore the existing G6H one-parameter result remains valid in its actual fixed-geometry scope. A fully self-consistent curved solution remains open.

## G4F — channel convergence criterion

For unitary conjugation channels,

`||Ad_U-Ad_V||_diamond <= 2 ||U-V||_op`.

The same convex estimate applies to equal-weight branch mixtures. Hence a uniform dyadic estimate

`sup_alpha ||U_alpha(h_{n+1})-U_alpha(h_n)||_op <= C h_n^p`, `p>0`,

would give an absolutely summable channel sequence.

Current QGR evidence is instead specified observable/RMS scaling, not a uniform operator-norm estimate on the full branch/state domain.

Classification:
`BLOCKED_SCOPED_A_CLEAR_SUMMABLE_OPERATOR_CRITERION_EXISTS_BUT_CURRENT_QGR_DATA_DO_NOT_ESTABLISH_THE_REQUIRED_UNIFORM_BRANCH_OPERATOR_BOUND`.

## Consolidated classification

`PARTIAL_SCOPED_C6_IS_NOT_FIXED_BY_CURRENT_LOWER_ORDER_DATA_BUT_DECOUPLES_FROM_FLAT_LINEARIZED_PROPAGATION_AND_FROM_THE_EXISTING_FIXED_GEOMETRY_TRACED_G6H_CHANNEL_AS_A_SCALAR_PHASE__SELF_CONSISTENT_CURVED_C6_DYNAMICS_AND_INFINITE_REFINEMENT_REMAIN_OPEN`.

## Next gate

`QGR-ITER009-G5-LEADING-HISTORY-LOSS-C6-ORDER-AND-STRONG-REFINEMENT-CONTROL`

Test whether a self-consistent `O(h^4)c6` shift of the branch geometry can modify the leading `O(h^4)` history-mixture loss or only enters at higher order, distinguish common and branch-dependent shifts, and replace an unnecessarily strong diamond-norm demand by a justified strong-convergence criterion on the physical wavepacket domain if possible.
