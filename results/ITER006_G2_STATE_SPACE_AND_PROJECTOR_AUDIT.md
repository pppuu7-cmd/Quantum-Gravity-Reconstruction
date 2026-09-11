# QGR Iter006-G2 — state-space and projector reconstruction audit

Date: 2026-09-11
Status: `PARTIAL / KINEMATIC_STATE_SPACE_DERIVED / PHYSICAL_TRANSPORT_OPEN`

## Question

Can the QGR second-moment field be embedded in a positive quantum state-space with a derived refinement/constraint structure, without reusing the early toy CCRC projector or choosing a Hilbert model only because it reproduces QGR-L1?

## G2A — direct covariance interpretation fails

A tempting minimal construction is to introduce four Hermitian relational-frame observables `X_i` and identify

`G_ij = (1/2) <X_i X_j + X_j X_i>`.

This cannot represent the QGR Lorentzian second-moment field. For every real vector `v`,

`v^i G_ij v^j = <(v.X)^2> >= 0`.

Thus any such symmetrized quantum covariance/second moment is positive semidefinite, whereas the QGR local background response has nondegenerate Lorentzian inertia `(1,3)`.

Classification:

`FAIL_SCOPED_DIRECT_HERMITIAN_COVARIANCE_INTERPRETATION_OF_G`.

This does not rule out a positive Hilbert space. It only rules out identifying the Lorentzian `G` itself with an ordinary covariance matrix of four Hermitian observables.

## G2B — Lorentzian configuration-space realization

Retain the already derived four-dimensional relational frame space `W4`. Treat `G` as a configuration/response variable in

`Q_13 = { G in Sym^2(W4*) | G nondegenerate, signature(G)=(1,3) }`.

This uses exactly ten local components and preserves the finite pullback law already derived in Iter005.

Under an invertible local frame change `A`,

`G -> A^T G A`.

For `n=4`, the induced linear map on the ten-dimensional symmetric-matrix space has Jacobian

`J_Sym2(A) = |det A|^(n+1) = |det A|^5`.

Also

`|det(A^T G A)| = |det A|^2 |det G|`.

Therefore

`dmu(G) = |det G|^(-5/2) product_{i<=j} dG_ij`

is invariant under congruence:

`dmu(A^T G A)=dmu(G)`.

This supplies a natural kinematic state-space candidate

`H_kin = L^2(Q_13, dmu)`

(up to overall measure normalization and the choice of connected/time-oriented Lorentzian component).

Classification:

`PASS_SCOPED_NATURAL_POSITIVE_KINEMATIC_HILBERT_SPACE_ON_LORENTZIAN_RESPONSE_CONFIGURATION_SPACE`.

Important boundary: this is not yet the physical Hilbert space or a finite quantum-gravity measure.

## G2C — why a unique 10x10 physical projector is the wrong object

The linear QGR field is constrained by derivative/frame redundancy. Physical modes are obtained as a quotient by four gauge directions, not by a preferred Euclidean orthogonal complement in the ten-component covariant field space.

A concrete 10x10 orthogonal projector therefore requires a gauge-fixing inner product/reference structure and is not canonical. Different gauge complements represent the same quotient.

Hence the early channel ansatz

`K_alpha = a P_sys`

with one assumed physical system projector `P_sys` is too restrictive and is retired as a fundamental statement.

The correct physical construction must instead use a constraint quotient / rigging map / BRST-equivalent structure, while the refinement-history normalization is handled separately.

Classification:

`PASS_SCOPED_PHYSICAL_SPACE_IS_CONSTRAINT_QUOTIENT_NOT_UNIQUE_COVARIANT_ORTHOGONAL_PROJECTOR`.

## G2D — S4 history projector is not the physical field projector

The 24 maximal `B4` histories form one `S4` orbit. The regular history representation has the unique normalized invariant vector

`|Omega> = 24^(-1/2) sum_alpha |alpha>`

and group-average projector

`P_hist = (1/24) sum_{g in S4} U_g = |Omega><Omega|`,

with exact rank one.

However `S4` also acts nontrivially on the already derived two-dimensional physical pair/polarization sector. Therefore promoting `S4` itself to a physical gauge constraint and averaging the system state over it would erase physical polarization information.

So:

- `P_hist` is a valid history-symmetry projector;
- it is **not** the physical QGR field projector;
- `S4` symmetry can fix equality of branch magnitudes but cannot be used to quotient away the two physical modes.

Classification:

`FAIL_SCOPED_IDENTIFICATION_OF_HISTORY_S4_GROUP_AVERAGE_WITH_PHYSICAL_QGR_FIELD_PROJECTOR`.

## G2E — revised projector-free history isometry

The refinement candidate should therefore be written without an assumed system projector:

`V |psi> = (1/sqrt(24)) sum_alpha |alpha> tensor U_alpha |psi>`.

If every branch transport `U_alpha` is an isometry on the physical constraint quotient, then

`V^dagger V = (1/24) sum_alpha U_alpha^dagger U_alpha = I`.

For coarse observables that do not resolve the internal history label, tracing the history register gives

`E(rho) = (1/24) sum_alpha U_alpha rho U_alpha^dagger`.

This is completely positive and trace preserving whenever the branch maps are isometries. It also resolves the earlier mixture-versus-square-of-mean ambiguity operationally: coarse second moments are obtained from the channel/marginal, not by arbitrarily squaring a mean fine frame.

At multiple levels, exact projective composition follows if the physical branch transports satisfy

`U_(alpha,beta) = U_beta U_alpha`

and the history registers tensor functorially.

## Current blocker

The branch transports `U_alpha` have not yet been derived from the same QGR local action/constraint system, and their physical isometry/unitarity has not been established. Therefore the state-space gate is not closed.

Current blocker:

`BLOCKED_MISSING_PHYSICAL_CONSTRAINT_QUOTIENT_OR_RIGGING_MAP_AND_DERIVED_FINE_HISTORY_TRANSPORTS_U_ALPHA_WITH_ISOMETRY_AND_SAME_REALIZATION_QGR_L1_RESPONSE`.

## Exact next gate

`QGR-ITER006-G2C-PERTURBATIVE_PHYSICAL_HILBERT_AND_HISTORY_TRANSPORT`

1. Construct the positive-frequency solution space of QGR-L1 modulo the four derivative gauge directions.
2. Verify that the physical on-shell fiber is two-dimensional and admits a positive inner product after the physically allowed overall kinetic-sign choice.
3. Derive the action of finite relational-frame/permutation transports on that quotient.
4. Test whether the 24 branch transports are isometries and whether their multi-level composition is associative.
5. Do not use `S4` group averaging to erase the two physical polarization modes.

## Reproducibility

See `code/qgr_iter006_g2_state_space_history_audit.py`.
