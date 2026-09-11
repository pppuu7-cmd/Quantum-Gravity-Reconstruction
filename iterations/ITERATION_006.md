# QGR Iteration 006 — Quantum Measure / Composition and Projective Refinement Reconstruction

Date: 2026-09-11
Status: `ACTIVE / PHYSICAL_ALGEBRA_AND_NORMALIZED_HISTORY_INSTRUMENT_RECONSTRUCTED / GLOBAL_STRONG_CURVATURE_BRANCH_FINITENESS_OPEN`
Current task completion: **94%**
Candidate-program readiness: **64%**
Active local candidate: **QGR-L1**

## Starting authority

Iter005 closed the local two-derivative nonlinear bootstrap through quartic order and established scoped weak-background characteristic stability. It also exposed a same-realization refinement ambiguity: a curved coarse state containing only the local second moment `G` loses fine holonomy information.

Iter006 therefore reconstructs the state/measure/composition layer without importing the old toy projector, normalized noncompact-Haar averaging, or history-dependent weights.

## G1 — 24-history normalization

The 24 maximal `B4` ordering histories admit branch amplitude magnitude

`1/sqrt(24)`

and channel weight

`1/24`.

The early ansatz `K_alpha=a P_sys` is retired as fundamental because the physical field sector is a constraint quotient, not the image of a preferred covariant `10x10` orthogonal projector.

Classification: `PASS_SCOPED_HISTORY_REGISTER_NORMALIZATION`.

## G2 — state-space reconstruction

### G2A: covariance no-go

A symmetrized second moment of four Hermitian operators is positive semidefinite, so the Lorentzian QGR response `G` cannot be an ordinary Hermitian covariance matrix.

Classification: `FAIL_SCOPED_DIRECT_HERMITIAN_COVARIANCE_INTERPRETATION_OF_G`.

### G2B: positive kinematic Hilbert space

Define

`Q_13={G=G^T | signature(G)=(1,3), det G != 0}`.

Under congruence `G->A^T G A`, the induced Jacobian on the ten-dimensional symmetric-matrix space is `|det A|^5`, while `|det G|` gains `|det A|^2`. Hence

`dmu(G)=|det G|^(-5/2) d^10G`

is congruence invariant and

`H_kin=L^2(Q_13,dmu)`

is a natural positive kinematic state space.

### G2C: physical quotient

At every fundamental cover covector `e_i`:

- `rank H(e_i)=4`;
- `dim ker H(e_i)=6`;
- `rank R(e_i)=4`;
- `im R subset ker H`.

Therefore

`dim[ker H(e_i)/im R(e_i)]=2`.

The four-cover symmetric-seed physical mode space has exact dimension `8`. `S4` acts unitarily between these quotient fibers and is a symmetry, not a field-gauge projector.

Records:

- `results/ITER006_G2_STATE_SPACE_AND_PROJECTOR_AUDIT.md`
- `results/ITER006_G2C_SEED_PHYSICAL_HILBERT_AND_UNITARY_HISTORY.md`

## G3 — history transport from the same QGR object

The forty first-jet components `D_iG_jk` determine the torsion-free compatible connection

`Gamma^k_ij=(1/2)G^{kl}(D_iG_lj+D_jG_li-D_lG_ij)`.

History ordering therefore changes transport through curvature/holonomy of the same QGR connection, not arbitrary branch functions.

An invertible quasi-invariant configuration map `F_alpha` induces the linear Koopman/Radon-Nikodym unitary

`(U_alpha psi)(G)=[d(F_alpha*mu)/dmu(G)]^(1/2) psi(F_alpha^-1 G)`.

Composition obeys `U_(beta o alpha)=U_beta U_alpha`.

Records:

- `results/ITER006_G3A_DERIVED_HISTORY_TRANSPORT.md`
- `results/ITER006_G3B_CONTROLLED_CONFIGURATION_TRANSPORT.md`

## G4 — exact finite frame/holonomy lift

The Lorentzian response admits

`G=F^T C F`,

with

`Q_13 ~= O(C) \ GL(4)`, `16-6=10`.

For edge `v->w`,

`A_wv=F_w^-1 L_wv F_v`, `L_wv in O(C)`

is invariant under local internal Lorentz frame changes and obeys exact metric compatibility

`A_wv^T G_w A_wv=G_v`.

The six-dimensional endpoint ambiguity is therefore the Lorentz connection fiber, not six new physical couplings.

Record: `results/ITER006_G4_FRAME_HOLONOMY_LIFT.md`.

## G5 — local discrete Levi-Civita uniqueness

Finite plaquette torsion closure is

`e_i(v)+L_i^-1 e_j(v+i)=e_j(v)+L_j^-1 e_i(v+j)`.

At the symmetric seed the exact `24x24` connection Jacobian has

- rank `24`;
- determinant `11664` in the recorded rational basis;
- zero homogeneous kernel.

Hence the implicit-function theorem gives locally unique finite torsion-free holonomies near the symmetric seed from the existing frame data.

Record: `results/ITER006_G5_DISCRETE_LEVI_CIVITA_UNIQUENESS.md`.
Code: `code/qgr_iter006_g5_discrete_torsion_rank.py`.

## G6 — projective closure boundary

Ordered-chain blocking is exactly projective because edge transports and RN factors compose.

A generic curved coarse state containing only local `G` is not closed: loop holonomy can affect future transport while being invisible to local `G`.

Classification:

- `PASS_SCOPED_EXACT_ORDERED_CHAIN_PROJECTIVE_COMPOSITION`;
- `FAIL_SCOPED_GENERIC_CURVED_G_ONLY_PROJECTIVE_CLOSURE`.

Record: `results/ITER006_G6_PROJECTIVE_CLOSURE_AND_HOLONOMY.md`.

## G7A — weak-curvature observable sector

The local torsion-free metric-compatible curvature sector reduces

`36 -> 21 -> 20`

components after pair symmetries and first Bianchi. Thus weak-curvature local coarse data can be represented by `G(10)+Riemann(20)` before field equations are used.

Record: `results/ITER006_G7A_WEAK_CURVATURE_OBSERVABLE_COUNT.md`.

## G7B — exact strong-curvature path-groupoid closure

For a finite connected graph define

`X_Gamma={(G_v,A_e) | A_e^T G_t A_e=G_s}`.

For a path `p=e_n...e_1`,

`A_p=A_(e_n)...A_(e_1)`.

Metric compatibility is telescopic and path concatenation is represented exactly. Coarse blocking assigns to a coarse edge the product of the fine transports along the represented path, so two-level and direct fine blocking agree exactly.

Loop holonomies are retained rather than truncated to weak-curvature tensors. For a connected graph with `V` vertices and `E` edges, a spanning-tree description leaves `b1=E-V+1` independent fundamental cycle holonomies.

Classification:

`PASS_SCOPED_EXACT_STRONG_CURVATURE_PATH_GROUPOID_OBSERVABLE_ALGEBRA_WITH_ASSOCIATIVE_BLOCKING`.

Record: `results/ITER006_G7B_STRONG_CURVATURE_PATH_GROUPOID_CLOSURE.md`.

## G8A — normalized interacting history instrument

For each history define

`K_alpha=24^(-1/2) exp(i S_alpha/hbar) U_alpha`,

where `S_alpha` is the real QGR branch action on the currently verified local domain and `U_alpha` is the unitary branch transport.

Then exactly

`K_alpha^dagger K_alpha=(1/24)I`,

`sum_alpha K_alpha^dagger K_alpha=I`.

Therefore

`V psi=sum_alpha |alpha> tensor K_alpha psi`

is an isometry and

`E(rho)=sum_alpha K_alpha rho K_alpha^dagger`

is CPTP after the history label is traced. The branch modulus is fixed; interaction information appears only through the action phase and the derived transport.

Classification:

`PASS_SCOPED_EXACT_NORMALIZED_INTERACTING_HISTORY_INSTRUMENT_WITH_NO_FREE_BRANCH_WEIGHTS`.

Record: `results/ITER006_G8A_NORMALIZED_INTERACTING_HISTORY_INSTRUMENT.md`.

## G8B — regular-stratum rigging and torsion-branch measure

Internal `O(1,3)` redundancy is removed algebraically by the gauge-invariant variables `(G_v,A_e)`, so no normalized noncompact Haar average is required.

On a finite-complex regular stratum where the derivative/frame constraint rank is constant, a local transverse quotient exists. In a regular local slice `chi=0`, the quotient density is

`dmu_phys=dmu_kin delta(chi) |det(Dchi.R)|`.

For possible multiple torsion-free connection roots `L_r`, impose the torsion equations with the invariant **unnormalized** group measure. On isolated regular roots, delta/coarea reduction fixes relative weights

`w_r proportional to j_Haar(L_r)/|det(dT/domega)_(L_r)|`.

Near the seed there is one regular root with nonzero determinant. No arbitrary branch probabilities are introduced.

Global strong-curvature finiteness remains open if the root set becomes singular, continuous, infinite, or escapes along noncompact connection directions.

Record: `results/ITER006_G8B_REGULAR_STRATUM_RIGGING_AND_BRANCH_MEASURE.md`.

## G8C — BRST algebraic physical descent

The already derived frame-pullback algebra closes exactly:

`[delta_xi,delta_eta]G=delta_[xi,eta]G`.

Define

`sG=L_cG`, `sc=-(1/2)[c,c]`.

Jacobi plus the exact commutator law gives `s^2=0`. The generic algebraic physical observable space is therefore the ghost-number-zero cohomology `H^0(s)`.

The path-groupoid blocking map is covariant and therefore a chain map; it descends to cohomology. The history instrument also descends on domains where branch maps intertwine the constraints and the action is gauge invariant.

Classification:

`PASS_SCOPED_NILPOTENT_BRST_COMPLEX_AND_PROJECTIVE_CONSTRAINT_DESCENT`.

Record: `results/ITER006_G8C_BRST_CONSTRAINT_DESCENT.md`.

## G8D — operational physical positivity

Use the represented physical `*`-algebra `A_phys=H^0(s)` and define a physical state as a positive normalized functional `omega` on `A_phys`.

Kinematic positive density matrices induce such states by restriction. Gauge-related density matrices agree on invariant observables.

Because the coarse history channel is CPTP and gauge covariant, its dual is unital completely positive and preserves the physical observable algebra. Thus

`omega' = omega o E*`

remains positive and normalized.

Replacement principle:

- fine coherent level: isometric history-register evolution;
- coarse level after history tracing: CPTP evolution;
- physical positivity: positive normalized functionals on the physical observable algebra.

Classification:

`PASS_SCOPED_OPERATIONAL_POSITIVE_PHYSICAL_STATE_SPACE_AND_CPTP_PROJECTIVE_COARSE_EVOLUTION`.

Record: `results/ITER006_G8D_OPERATIONAL_PHYSICAL_POSITIVITY.md`.

## G9 — finite-curvature nonlinear torsion audit

A deterministic noninfinitesimal conformal-frame toy was solved with the full nonlinear finite torsion equations at the central vertex and four neighbors.

Central root diagnostics:

- residual norm about `2e-14`;
- parameter norm about `0.468`;
- smallest Jacobian singular value about `0.349`;
- condition number about `23.1`.

All six plaquette relative holonomies are nontrivial, with

`||H_ij-I||` approximately in `[0.129,0.249]`,

while `H^T C H=C` is preserved to about `1e-15`.

Twelve deterministic local restarts converged to the same transport branch within `4e-11` in matrix distance.

Classification:

`NUMERICALLY_VERIFIED_FINITE_CURVATURE_REGULAR_TORSION_BRANCH_WITH_NONZERO_HOLONOMY_AND_STABLE_LOCAL_BASIN`.

Record: `results/ITER006_G9_FINITE_CURVATURE_TORSION_BRANCH_AUDIT.md`.
Code: `code/qgr_iter006_g9_finite_curvature_torsion_toy.py`.

## Remaining blocker

The broad state-space/measure/composition ambiguity has collapsed to one principal unresolved issue:

`BLOCKED_GLOBAL_STRONG_CURVATURE_TORSION_ROOT_FINITE_REGULARITY_AND_NONCOMPACT_ESCAPE_CONTROL`.

QGR has not proved that arbitrary strong-curvature finite-complex data yield only finitely many regular torsion-free connection branches with a normalizable induced branch measure.

Potential failure modes still allowed by current evidence:

- singular roots with `det(dT/domega)=0`;
- continuous root components;
- infinitely many distinct roots;
- runaway sequences in noncompact connection directions.

## Exact next gate — Iter006-G10

`QGR-ITER006-G10-GLOBAL_TORSION_BRANCH_FINITE_MEASURE`

1. Analyze the asymptotic/noncompact directions of the finite torsion map.
2. Derive sufficient conditions excluding runaway Lorentz-rapidity solutions for nondegenerate frame data, or construct a counterexample.
3. Determine whether the regular solution set is generically finite on a finite complex.
4. Audit singular strata and branch-merger points.
5. Test whether the induced coarea branch measure remains finite under two-level blocking.
6. Fail closed if an extra regulator, branch cutoff, or history weight is needed only to force normalization.

## KMQGB synchronization

Latest observed KMQGB head: `6a979ad41012198b5e69b47494bc6d6d947dca06` (Iter334-337 authority workflow). The aggregate guard still requires strict terminal coverage beyond `1/15`, authorizes zero new terminal promotions, and keeps D7 output `NOT_AUTHORIZED`. The LQG, asymptotic-safety, and causal-set/high-value CW2 lanes remain blocked by distinct missing source-defined objects rather than family FAIL evidence.

## Claim locks

- no all-orders nonlinear QGR theorem;
- no proof of global finite strong-curvature branch measure;
- no continuum/RG theorem;
- no normalized phenomenological observable/comparator yet;
- no independent KMQGB pass;
- no `NEW_REQUIRED` authorization.

## Progress accounting

- Iter006 completion: **94%**.
- Candidate-program readiness: **64%**.
- These are construction-roadmap metrics, not probabilities of correctness.
