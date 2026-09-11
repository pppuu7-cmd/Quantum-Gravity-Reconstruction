# QGR Iteration 006 — Quantum Measure / Composition and Projective Refinement Reconstruction

Date: 2026-09-11
Status: `ACTIVE / KINEMATIC_STATE_SPACE_AND_SEED_HISTORY_ISOMETRY_DERIVED / DYNAMIC_PHYSICAL_DESCENT_OPEN`
Current task completion: **65%**
Candidate-program readiness: **55%**
Active local candidate: **QGR-L1**

## Starting authority

Iter005 closed the local two-derivative nonlinear bootstrap through quartic order and established scoped weak-background characteristic stability. It also exposed a genuine same-realization refinement ambiguity: marginal second moments and second moments of coherently composed mean frames are not generically equal.

R5 therefore reconstructs the primitive state/measure/composition object rather than choosing an RG/coarse rule after the fact.

## G1 — history-register normalization candidate

The 24 maximal `B4` histories admit a normalized history-register isometry with branch amplitude magnitude

`1/sqrt(24)`

and branch channel weight

`1/24`.

This remains the lead composition architecture, but the original ansatz `K_alpha=a P_sys` is no longer regarded as fundamental because QGR does not possess a preferred covariant 10-component orthogonal physical projector.

Classification:

`PASS_SCOPED_HISTORY_REGISTER_NORMALIZATION_CANDIDATE`.

## G2A — direct covariance interpretation rejected

If four Hermitian operators `X_i` are used and

`G_ij=(1/2)<X_i X_j+X_j X_i>`,

then for every real `v`,

`v^i G_ij v^j = <(v.X)^2> >= 0`.

Therefore an ordinary Hermitian covariance/second-moment matrix cannot equal the nondegenerate Lorentzian QGR response field.

Classification:

`FAIL_SCOPED_DIRECT_HERMITIAN_COVARIANCE_INTERPRETATION_OF_G`.

## G2B — positive kinematic Hilbert space on Lorentzian response configurations

Treat the already derived `G in Sym^2(W4*)` as a configuration/response variable rather than a covariance matrix.

Define

`Q_13={G=G^T | signature(G)=(1,3), det G != 0}`.

Under a local frame congruence

`G -> A^T G A`,

the induced Jacobian on the ten-dimensional symmetric-matrix space is

`|det A|^5`.

Since

`|det(A^T G A)|=|det A|^2 |det G|`,

the measure

`dmu(G)=|det G|^(-5/2) product_{i<=j} dG_ij`

is exactly congruence invariant.

Hence a natural positive kinematic state-space is

`H_kin=L^2(Q_13,dmu)`

up to overall measure normalization and connected/time-orientation choice.

Classification:

`PASS_SCOPED_NATURAL_POSITIVE_KINEMATIC_HILBERT_SPACE_ON_LORENTZIAN_RESPONSE_CONFIGURATIONS`.

Record: `results/ITER006_G2_STATE_SPACE_AND_PROJECTOR_AUDIT.md`.
Reproducibility: `code/qgr_iter006_g2_state_space_history_audit.py`.

## G2C — physical state is a constraint quotient, not a preferred 10x10 projector

The QGR covariant field has four derivative gauge directions. Physical modes are therefore represented by a quotient, not by a unique Euclidean orthogonal complement.

A concrete 10x10 `P_sys` requires gauge-fixing data and is not canonical. The early toy CCRC projector is retired as a candidate physical QGR projector.

This also blocks an incorrect alternative: the `S4` group-average over the 24 history orderings cannot be identified with the physical field projector, because `S4` acts nontrivially on the independently derived two-dimensional physical polarization sector. Treating the whole `S4` as gauge would erase physical modes.

Classification:

`PASS_SCOPED_PHYSICAL_SPACE_IS_CONSTRAINT_QUOTIENT_AND_HISTORY_S4_IS_SYMMETRY_NOT_FIELD_GAUGE_PROJECTOR`.

## G2D — exact symmetric-seed physical Hilbert quotient

For every fundamental cover covector `e_i`, QGR-L1 has

- `rank H(e_i)=4`;
- `dim ker H(e_i)=6`;
- `rank R(e_i)=4`;
- `im R(e_i) subset ker H(e_i)`.

Therefore

`P_i = ker H(e_i) / im R(e_i)`

has exact dimension two.

Using the positive `S4`-invariant seed norm on the ten component labels gives a positive quotient norm without selecting a gauge complement.

The one-cell seed physical mode space

`H_seed = direct_sum_i P_i`

has exact dimension

`4*2=8`.

`S4` permutation matrices map cover fibers, Hessian kernels, and gauge images equivariantly and are orthogonal for the seed norm. Therefore they induce unitary maps on `H_seed` while retaining the two polarization modes.

The 24-history isometry

`V psi = 24^(-1/2) sum_pi |pi> tensor U_pi psi`

is therefore exactly normalized on the symmetric seed **without** a system projector.

Classification:

`PASS_SCOPED_SYMMETRIC_B4_SEED_PHYSICAL_HILBERT_QUOTIENT_AND_UNITARY_HISTORY_ISOMETRY`.

Record: `results/ITER006_G2C_SEED_PHYSICAL_HILBERT_AND_UNITARY_HISTORY.md`.
Reproducibility: `code/qgr_iter006_g2c_seed_physical_hilbert.py`.

## G3A — branch transport from the same QGR connection

Endpoint metrics alone do not determine an edge transport: metric compatibility leaves a six-dimensional Lorentz stabilizer freedom.

QGR already contains the missing data through the forty first-jet components `D_i G_jk`. These uniquely determine the torsion-free metric-compatible connection

`Gamma^k_ij=(1/2)G^{kl}(D_iG_lj+D_jG_li-D_lG_ij)`.

No independent connection field or coupling is introduced.

For a frozen/semiclassical background, an ordered history carries

`A_alpha=P product_r exp[-Delta_r Gamma_(i_r)]`.

Different history orderings differ by the curvature/holonomy of this same connection rather than by arbitrary branch functions.

For fixed frame transports, congruence invariance of `dmu` makes the corresponding Koopman maps unitary on `H_kin`. Therefore the history-register isometry remains exactly normalized at frozen-background level.

Classification:

`PASS_SCOPED_QGR_FIRST_JET_UNIQUELY_GENERATES_SEMICLASSICAL_HISTORY_TRANSPORT_AND_HOLONOMY`.

Record: `results/ITER006_G3A_DERIVED_HISTORY_TRANSPORT.md`.

## G3B — linear quantum lift of configuration-dependent transport

A configuration-dependent classical transport does not require state-dependent nonlinear quantum mechanics.

Let a history define an invertible quasi-invariant configuration-space map

`F_alpha:X->X`.

It induces the linear Koopman/Radon-Nikodym unitary

`(U_alpha psi)(G)=[d(F_alpha*mu)/dmu(G)]^(1/2) psi(F_alpha^(-1)G)`.

If

`F_(alpha,beta)=F_beta o F_alpha`,

then Radon-Nikodym chain rule gives exact quantum composition

`U_(alpha,beta)=U_beta U_alpha`.

Thus the 24-history isometry and multi-level projective composition can remain linear and unitary even when the classical map is nonlinear in `G`.

Classification:

`PASS_SCOPED_CONFIGURATION_DEPENDENT_TRANSPORT_HAS_LINEAR_UNITARY_KOOPMAN_LIFT_IF_ACTUAL_QGR_MAP_IS_INVERTIBLE_AND_QUASI_INVARIANT`.

Record: `results/ITER006_G3B_CONTROLLED_CONFIGURATION_TRANSPORT.md`.

## Current blocker

The remaining gap is no longer generic “need a Hilbert space”. It is sharply localized:

`BLOCKED_MISSING_EXPLICIT_FINITE_COMPLEX_QGR_MAP_F_ALPHA_WITH_PROVED_CONSTRAINT_EQUIVARIANCE_QUASI_INVARIANCE_AND_TWO_MODE_PHYSICAL_DESCENT_ON_NONTRIVIAL_CURVED_CONFIGURATIONS`.

The compatible connection supplies the infinitesimal/frozen-background transport, but a finite discrete map on the actual fine complex has not yet been proved unique or physical.

## Exact next gate — Iter006-G4

`QGR-ITER006-G4-DISCRETE_CONNECTION_MAP_AND_CONSTRAINT_EQUIVARIANCE`

1. Construct a finite-cell `F_alpha` from the existing QGR first-neighbor data without arbitrary interpolation.
2. Test its invertibility or define the minimal isometric quantum instrument if strict invertibility fails.
3. Prove/refute equivariance with the derivative/frame constraint structure.
4. Compute the Radon-Nikodym factor for the actual candidate measure.
5. Test preservation of the two-mode physical quotient on a nontrivial curved toy configuration.
6. Verify exact two-level projective composition.
7. Reject any added history phase, weight, or transport function not generated by `G`, its compatible connection, or the frozen composition rule.

## Claim locks

- QGR does not yet have a complete physical Hilbert/rigging construction for generic curved configurations.
- QGR does not yet have a finite interacting quantum measure.
- The symmetric-seed history isometry is not a proof of full dynamical coarse graining.
- The early CCRC toy projector is not a physical QGR projector.
- Continuum/RG closure, normalized observables, and KMQGB passage remain open.

## Progress accounting

- Iter006 completion: **65%**.
- Candidate-program readiness: **55%**.
- These are construction-roadmap metrics, not probabilities of correctness.
