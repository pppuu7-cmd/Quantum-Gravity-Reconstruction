# QGR Iteration 006 — Quantum Measure / Composition and Projective Refinement Reconstruction

Date: 2026-09-11
Status: `ACTIVE / STATE_SPACE_TRANSPORT_AND_LOCAL_DISCRETE_CONNECTION_RECONSTRUCTED / PHYSICAL_MEASURE_AND_STRONG_CURVATURE_CLOSURE_OPEN`
Current task completion: **82%**
Candidate-program readiness: **58%**
Active local candidate: **QGR-L1**

## Starting authority

Iter005 closed the local two-derivative nonlinear bootstrap through quartic order and established scoped weak-background characteristic stability. It also exposed a genuine same-realization refinement ambiguity: marginal second moments and second moments of coherently composed mean frames are not generically equal.

R5 therefore reconstructs the primitive state/measure/composition object rather than choosing an RG/coarse rule after the fact.

## G1 — history-register normalization candidate

The 24 maximal `B4` histories admit a normalized history-register isometry with branch amplitude magnitude `1/sqrt(24)` and branch channel weight `1/24`.

The original ansatz `K_alpha=a P_sys` is no longer fundamental because QGR does not possess a preferred covariant ten-component orthogonal physical projector.

Classification: `PASS_SCOPED_HISTORY_REGISTER_NORMALIZATION_CANDIDATE`.

## G2A — direct covariance interpretation rejected

For four Hermitian operators `X_i`, any symmetrized second moment satisfies

`v^i G_ij v^j=< (v.X)^2 > >=0`.

Therefore the nondegenerate Lorentzian QGR response cannot be an ordinary Hermitian covariance matrix.

Classification: `FAIL_SCOPED_DIRECT_HERMITIAN_COVARIANCE_INTERPRETATION_OF_G`.

## G2B — positive kinematic Hilbert space

Treat `G in Sym^2(W4*)` as a Lorentzian configuration/response variable on

`Q_13={G=G^T | signature(G)=(1,3), det G!=0}`.

Under `G->A^T G A`, the induced Jacobian on `Sym^2(W4)` is `|det A|^5`, while `|det G|` gains `|det A|^2`. Hence

`dmu(G)=|det G|^(-5/2) product_{i<=j}dG_ij`

is exactly congruence invariant.

Natural kinematic state-space:

`H_kin=L^2(Q_13,dmu)`.

Classification: `PASS_SCOPED_NATURAL_POSITIVE_KINEMATIC_HILBERT_SPACE_ON_LORENTZIAN_RESPONSE_CONFIGURATIONS`.

Record: `results/ITER006_G2_STATE_SPACE_AND_PROJECTOR_AUDIT.md`.
Code: `code/qgr_iter006_g2_state_space_history_audit.py`.

## G2C — constraint quotient, not a preferred system projector

The ten-component covariant field has four derivative gauge directions. Physical states are therefore represented by a quotient rather than a preferred Euclidean orthogonal complement.

A concrete `10x10 P_sys` requires gauge-fixing data and is not canonical. The early CCRC toy projector is retired as a physical QGR candidate.

The `S4` group average over histories is also not the physical field projector: `S4` acts nontrivially on the physical two-mode sector and cannot be quotiented away without erasing polarization information.

Classification: `PASS_SCOPED_PHYSICAL_SPACE_IS_CONSTRAINT_QUOTIENT_AND_HISTORY_S4_IS_SYMMETRY_NOT_FIELD_GAUGE_PROJECTOR`.

## G2D — exact symmetric-seed physical Hilbert quotient

At every fundamental cover covector `e_i`:

- `rank H(e_i)=4`;
- `dim ker H(e_i)=6`;
- `rank R(e_i)=4`;
- `im R(e_i) subset ker H(e_i)`.

Therefore

`P_i=ker H(e_i)/im R(e_i)`

has exact dimension two.

The one-cell seed physical mode space

`H_seed=direct_sum_i P_i`

has exact dimension `8`.

`S4` permutations map kernels and gauge images equivariantly and induce unitary maps on the positive seed quotient norm. Hence

`V psi=24^(-1/2) sum_pi |pi> tensor U_pi psi`

is an exact symmetric-seed history isometry without a system projector.

Classification: `PASS_SCOPED_SYMMETRIC_B4_SEED_PHYSICAL_HILBERT_QUOTIENT_AND_UNITARY_HISTORY_ISOMETRY`.

Record: `results/ITER006_G2C_SEED_PHYSICAL_HILBERT_AND_UNITARY_HISTORY.md`.
Code: `code/qgr_iter006_g2c_seed_physical_hilbert.py`.

## G3A — branch transport from the same QGR connection

Endpoint `G` values alone leave a six-dimensional Lorentz stabilizer ambiguity. The already present first jets `D_iG_jk` uniquely determine the torsion-free compatible connection

`Gamma^k_ij=(1/2)G^{kl}(D_iG_lj+D_jG_li-D_lG_ij)`.

For a frozen/semiclassical background an ordered history has parallel transport

`A_alpha=P product_r exp[-Delta_r Gamma_(i_r)]`.

History-order differences begin with curvature/holonomy of this same connection rather than arbitrary branch functions.

Classification: `PASS_SCOPED_QGR_FIRST_JET_UNIQUELY_GENERATES_SEMICLASSICAL_HISTORY_TRANSPORT_AND_HOLONOMY`.

Record: `results/ITER006_G3A_DERIVED_HISTORY_TRANSPORT.md`.

## G3B — linear quantum lift of configuration-dependent transport

Let a history define an invertible quasi-invariant configuration map `F_alpha:X->X`. It induces the linear Koopman/Radon-Nikodym unitary

`(U_alpha psi)(G)=[d(F_alpha*mu)/dmu(G)]^(1/2) psi(F_alpha^(-1)G)`.

If `F_(alpha,beta)=F_beta o F_alpha`, the RN chain rule gives `U_(alpha,beta)=U_beta U_alpha`.

Therefore configuration-dependent classical transport need not imply nonlinear quantum-state evolution.

Classification: `PASS_SCOPED_CONFIGURATION_DEPENDENT_TRANSPORT_HAS_LINEAR_UNITARY_KOOPMAN_LIFT_IF_ACTUAL_QGR_MAP_IS_INVERTIBLE_AND_QUASI_INVARIANT`.

Record: `results/ITER006_G3B_CONTROLLED_CONFIGURATION_TRANSPORT.md`.

## G4 — exact frame/holonomy lift for finite cells

The ten-component Lorentzian response is naturally the quotient

`G=F^T C F`, `F in GL(4)`, `F~Lambda F`, `Lambda^T C Lambda=C`.

Thus

`Q_13 ~= O(C) \ GL(4)`

on a connected component and `16-6=10` exactly.

For an oriented edge `v->w`, introduce an auxiliary Lorentz holonomy `L_wv in O(C)` and define

`A_wv=F_w^(-1)L_wv F_v`.

Then exactly

`A_wv^T G_w A_wv=G_v`.

Under `F_v->Lambda_vF_v` and `L_wv->Lambda_wL_wvLambda_v^(-1)`, `A_wv` is unchanged. Path transports compose by ordinary matrix multiplication and loop products carry curvature.

This gives an exact finite transport architecture without arbitrary interpolation, but `L_e` may not remain an unconstrained physical degree of freedom.

Classification: `PASS_SCOPED_EXACT_FRAME_HOLONOMY_FINITE_TRANSPORT_ARCHITECTURE__LEVI_CIVITA_CONSTRAINT_REQUIRED`.

Record: `results/ITER006_G4_FRAME_HOLONOMY_LIFT.md`.

## G5 — discrete torsion-free connection is locally unique near the seed

For each elementary plaquette require

`e_i(v)+L_i^(-1)e_j(v+i)=e_j(v)+L_j^(-1)e_i(v+j)`.

There are `6*4=24` scalar torsion equations and `4*6=24` infinitesimal Lorentz connection unknowns.

At the symmetric seed `e_i^a=delta_i^a`, `L_i=I`, the linearized homogeneous map is

`omega_i e_j-omega_j e_i`.

Using an exact rational basis of `o(C)`, its `24x24` matrix has

- rank `24`;
- determinant `11664` in the recorded basis;
- homogeneous kernel dimension `0`.

Therefore the implicit-function theorem gives a locally unique finite torsion-free solution for the four edge holonomies for sufficiently small frame deformations near the symmetric seed.

No six-parameter physical holonomy freedom per edge survives locally once the frame first differences are fixed.

Classification: `PASS_SCOPED_LOCAL_FINITE_DISCRETE_LEVI_CIVITA_HOLONOMIES_EXIST_AND_ARE_UNIQUE_NEAR_SYMMETRIC_SEED`.

Record: `results/ITER006_G5_DISCRETE_LEVI_CIVITA_UNIQUENESS.md`.
Code: `code/qgr_iter006_g5_discrete_torsion_rank.py`.

## G6 — projective composition and curved-block closure

Along an ordered causal chain, projective composition is exact:

`A_coarse=A_n...A_1`, `F_coarse=F_n o ... o F_1`, `U_coarse=U_n...U_1`.

Thus no new normalization appears under chain blocking.

For a generic multi-direction curved block, however, a local coarse `G` alone does not retain loop holonomy. Distinct fine configurations can agree on a chosen coarse second moment while producing different later ordered transports.

Therefore a `G`-only state description is not generically projectively/Markov closed in curved blocks.

Minimal repair: retain **derived** coarse connection/holonomy observables obtained from products of the already constrained fine transports. These are not new couplings.

Classification:

- `PASS_SCOPED_EXACT_ORDERED_CHAIN_PROJECTIVE_COMPOSITION`;
- `FAIL_SCOPED_GENERIC_CURVED_PROJECTIVE_CLOSURE_OF_LOCAL_G_ONLY_STATE_DESCRIPTION`.

Record: `results/ITER006_G6_PROJECTIVE_CLOSURE_AND_HOLONOMY.md`.

## G7A — minimal weak-curvature holonomy sector

A local curvature two-form has `6` plaquette orientations times `6` Lorentz generators = `36` raw components.

Metric compatibility, torsion-free pair symmetries and first Bianchi reduce the local off-shell Riemann sector to

`20`

independent components in four dimensions.

Therefore in a locally slowly varying weak-curvature block, the minimal candidate coarse information is

- ten components of `G`;
- twenty derived curvature components;

for leading holonomy prediction.

No field equations were used; the count is deliberately not reduced to Weyl-10.

Classification: `PASS_SCOPED_LOCAL_WEAK_CURVATURE_HOLONOMY_DATA_REDUCES_FROM_36_TO_20_LEVI_CIVITA_COMPONENTS`.

Record: `results/ITER006_G7A_WEAK_CURVATURE_OBSERVABLE_COUNT.md`.

## Current blocker

The remaining Iter006 blocker is now concentrated in the genuinely quantum/global part:

`BLOCKED_MISSING_GENERIC_PHYSICAL_RIGGING_OR_CONSTRAINT_HILBERT_COMPLETION_PLUS_NORMALIZED_INTERACTING_MEASURE_AND_STRONG_CURVATURE_PROJECTIVE_HOLONOMY_CLOSURE`.

Local/near-seed state-space and transport reconstruction is substantially closed, but QGR still lacks a full physical quantum measure and a strong-curvature coarse observable theorem.

## Exact next gate — Iter006-G7B/G8

`QGR-ITER006-G7B_PHYSICAL_RIGGING_AND_STRONG_CURVATURE_MEASURE`

1. Specify the minimal coarse holonomy observable algebra beyond the weak-curvature 20-component approximation.
2. Construct the physical constraint/rigging completion of `H_kin` without normalized noncompact-Haar fiction.
3. Define the interacting quantum amplitude/measure using the same QGR local action and frame-connection variables.
4. Prove positivity/unitarity or state the precise replacement principle.
5. Test two-level coarse/refinement consistency on a nontrivial curved block.
6. Keep all holonomy weights derived; do not add history-dependent functions or counterterms to force closure.

## Claim locks

- QGR does not yet have a complete generic curved physical Hilbert/rigging construction.
- QGR does not yet have a finite normalized interacting quantum measure.
- Weak-curvature `G+Riemann20` closure is not a strong-curvature truncation theorem.
- The early CCRC toy projector is not a physical QGR projector.
- Continuum/RG closure, normalized operational observables, and KMQGB passage remain open.

## Progress accounting

- Iter006 completion: **82%**.
- Candidate-program readiness: **58%**.
- These are construction-roadmap metrics, not probabilities of correctness.
